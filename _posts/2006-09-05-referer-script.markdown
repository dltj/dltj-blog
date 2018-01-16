---
layout: wordpress-import
status: publish
published: true
title: Script for Testing HTTP Referer Headers
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 111
wordpress_url: http://dltj.org/2006/09/referer-script/
date: '2006-09-05 16:12:59 -0400'
date_gmt: '2006-09-05 21:12:59 -0400'
categories:
- Raw Technology
tags:
- referer
- perl
- libraries
comments: []
---
I've just had the third occasion where in support of a user I suspect that user has a piece of software which is blocking or modifying the HTTP "referrer" header that comes normally with most interactions between a web browser and a web server.  Rather than asking that user to run a complicated test I found elsewhere on the web, I whipped up a little ditty that tests for this with (hopefully) non-technical words and advice.  At the bottom of this post is the source code for the script; feel free to take it and modify it for your own circumstances.

The URL to start the test is <span class="removed_link" title="http://www.ohiolink.edu/cgi-bin/check-refer.pl">http://www.ohiolink.edu/cgi-bin/check-refer.pl</span>.

I suspect most everyone will see the "correct behavior" as a result of the test.  For the sake of describing the problem completely, there are two possible "error" messages that one might see, though, if something is wrong.  First, if there was not a "Referrer" field received at the web server:

> Either your browser did not return a 'Referrer' URL as a result of following the link on the previous page or an intermediary has stripped the referrer URL from your browser's request before it reached this server. (This symptom can also happen if you typed the results URL, http://www.ohiolink.edu/cgi-bin/check-refer.pl/test, directly in the browser address window rather beginning from the start page.)

Second, if what was received was not what was expected:

> As a result of following the link on the previous page, your browser returned this as the 'Referrer' field:<br /><span style="font-family:monospace; margin-left: 5em; margin-top: 1em;">[... something else ...]</span>
> This was not what was expected, and as a result you may have problems using some OhioLINK services.
> This value should be <em>http://www.ohiolink.edu/cgi-bin/check-refer.pl</em> instead.
> (Make sure you start from <span class="removed_link" title="http://www.ohiolink.edu/cgi-bin/check-refer.pl">http://www.ohiolink.edu/cgi-bin/check-refer.pl</span> when performing this test.)
> For assistance with correcting this problem, please see <a href="http://karmak.org/2004/reftest/fix" title="HTTP_REFERER Fix">this support page from karmak.org</a>.

This 'referrer problem' seems to be happening more as a result of personal firewall software and other "helpful" agents.  Setting aside for the moment the question of whether relying on the HTTP Referer <footnote>By the way, "Referer" is not a typo here &mdash; it is arguably a typo in the original HTTP specification</footnote> URL is an acceptable or wise programming choice, if one of your standard troubleshooting tactics doesn't work you may want to try this one.

#!/usr/bin/perl
##
###########################################################################
##
##  Program:  check-refer.pl
##
##  Purpose:  Test the referrer header from the user's browser
##
##  Version:  1.0  5-Sep-2006
##
##  Author:   Peter Murray
##
##  Legalities:
##            Copyright 2006 by OhioLINK
## This file is part of the OhioLINK Digital Resource Commons (DRC) Project.
##
## The OhioLINK DRC is free software; you can redistribute it and/or
## modify it under the terms of the Affero General Public License as
## published by Affero, Inc. -- either version 1 of the License, or
## (at your option) any later version.
##
## The OhioLINK DRC Project is distributed in the hope that it will be
## useful, but WITHOUT ANY WARRANTY -- without even the implied warranty
## of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## Affero General Public License for more details.
##
## You should have received a copy of the Affero General Public
## License in the LICENSE.txt file that comes with the DRC project;
## if not, write to DRC Development Team, OhioLINK, 2455 North Star Rd, 
## Suite 300, Columbus, OH 43221, USA.
##
##  Revision History:
##    1.0   5-Sep-2006  peter  Initial Version
##
##

use CGI qw(escapeHTML url http);
use CGI::Carp;
use strict;

BEGIN {
  $SIG{'__DIE__'} = sub {
    print "Content-type: text/html\r\n\r\n";
    print "<html><head><title>COMPILE TIME ERROR.</title></head>\n";
    print "<body><h1>COMPILE TIME ERROR.</h1>This should never happen.  Further details:\n";
    print join "\n<br />",@_;
    print "</body></html>\n";
    exit;
  };
}

$SIG{'__DIE__'} = 'handle_die';

eval("main");
if ($@) {
    print "Content-type: text/plain\n\n",
              "The script failed because the error\n$@\noccurred.";
}

sub main {
# @output will be used in each one of these cases below to store the
# temporary array of HTML while we check for an error returning from the
# subroutine.
my @output;


## Now start doing some real work.

# Initialize the CGI module, and get any form variables into FORM::
my($query) = new CGI;
$query->import_names('FORM');

# Split the parameters from the URL line by the slash character (after removing
# the leading slash).  We will cycle through each one of these below.
my($path_info);
($path_info = $ENV{'PATH_INFO'}) =~ s/^\///;
my(@params) = split(/\//, $path_info);

#
# Now we start cycling through the @params array looking for specific keywords.
$_ = shift @params;
if ((!defined($_)) || ($_ eq 'start')) {
 # If there is nothing following the script file name (e.g., no PATH_INFO) or if the
 # contents of the first parameter is 'start', then generate the introdution page
  @output = initial_page();
} elsif ($_ eq 'test') {
 # If the first parameter is 'test' then run the tests on the referrer header
  @output = test_results();
} else {
 # The command was unknown -- either an error in coding or someone trying to hack
 # the script.  Return an error.
  push @output, HTMLheader("Sorry -- I don't understand."), < < "EoHTML", HTMLfooter();
I'm sorry, but I don't understand the $_ command.  Try starting from <a href="./">the beginning</a>.
EoHTML
}

# Write out the HTML that has been gathered in @output
outputHTML (@output);

# And we're done!
exit;
}  ## End of sub main()



sub initial_page {
  my @output;
  my $url = url();
  push @output, HTMLheader("Check Your Referrer Field");
  push @output, < < EoHTML;
  

To begin a test of how OhioLINK receives the "Referrer" field from your web browser, click on the following link:

<p style="font-size: 120%; width: 100%; text-align: center; border: 1px solid gray;">
<a href="$url/test">Start Referrer Test</a>


EoHTML
  push @output, HTMLfooter();
  return @output;
}


sub test_results {
  my @output;
  
  my $referrer = http('HTTP_REFERER');
  my $trueReferrer = url(-full=>1);
  push @output, HTMLheader("Results of Test for Referrer Field");
  
  if ((!defined($referrer)) || ($referrer eq "")) {
    push @output, "","Either your browser did not return a 'Referrer' URL as a result of following the link on the previous page or an intermediary has stripped the referrer URL from your browser's request before it reached this server.  (This symptom can also happen if you typed the results URL, <em>$trueReferrer/test</em>, directly in the browser address window rather beginning from the <a href="\"$trueReferrer\">start page</a>.)","";
  } else {
    push @output, "","As a result of following the link on the previous page, your browser returned this as the 'Referrer' field:<br /><span style="\"font-family:monospace; margin-left: 5em; margin-top: 1em;\">$referrer</span>","</p>";
  }
  
  if ($referrer eq $trueReferrer) {
    push @output, "","This is what was expected.","";
  } else {
    push @output, < < "EoHTML";
<p>
This was not what was expected, and as a result you may have problems using some OhioLINK services.  
This value should be <em>$trueReferrer</em> instead.  
(Make sure you start from <a href="$trueReferrer">$trueReferrer</a> when performing this test.)


For assistance with correcting this problem, please see <a href="http://karmak.org/2004/reftest/fix" title="HTTP_REFERER Fix">this support page from karmak.org</a>.

EoHTML
  }
  push @output, HTMLfooter();
  return @output;
}


sub outputHTML() {
  my @output=@_;
  print "Content-type: text/html\n\n";
  print join("\n",@output),"\n";
}

sub HTMLheader(@) {
 my($title,$h1,$style) = @_;
 
 $h1=$title if !defined($h1);
 $style = "" if !defined($style);
 
 return < < "EoHTML"
< !doctype html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="robots" content="none"/>
    <title>$title</title>
    <link rel="stylesheet" type="text/css" href="/style/ohiolink.css"/>
    <style type="text/css"><!--/*-->< ![cdata[/*><!--*/
       $style
    /*]]>*/--></style>
</head>
<body>
<p align="right"><img src="/images/bar-header.jpg" alt="" />
<h1>$h1</h1>
EoHTML
}

sub HTMLfooter() {
  return < < EoHTML
</p></body>
</html>
EoHTML
}

##
## SUBROUTINE handle_die
##
##   Get an error key for the program, open up the error text file, find and
##   print the text specific for that error, make the user feel special with
##   a message, then EXIT THE SCRIPT.
##
##   Parameters: Text key of the error message, plus additional parameters
##   Returns:    --none--  handle_die WILL EXIT THE SCRIPT
sub handle_die {
  my(@addl_info) = split /\|/,@_[0];
  my($error_key) = shift @addl_info;
  my($package, $filename, $line, $subroutine) = caller(0);
  my($progName, $paramURL);

  print "Content-type: text/html\n\n";
  print HTMLheader('Program Error');
  print "

</p><p>This program encountered an error in the <b>$subroutine</b> routine at line <b>$line</b> of <b>$progName</b>.";
  print "The error key is <b>$error_key</b>.  The parameter URL is <b>$paramURL</b>.</p>\n";
  if (scalar(@addl_info) > 0) {
    print "<p>Some additional info:\n</p><ul><li>\n </li><li>";
    print join "\n </li><li>",@addl_info;
    print "\n</li></ul>\n";
  }
  print HTMLfooter();
  exit;
}
