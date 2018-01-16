---
layout: wordpress-import
status: publish
published: true
title: Update to 'Embedded Web Video in a Standards-Compliant, Accessible, and Successful
  Way'
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 187
wordpress_url: http://dltj.org/2007/02/update-to-embedded-web-video/
date: '2007-02-21 15:41:09 -0500'
date_gmt: '2007-02-21 20:41:09 -0500'
categories:
- Raw Technology
tags:
- video
- digital libraries
- perl
- section508
- accessibility
- web standards
comments:
- id: 12693
  author: 'Barrierefreies Webdesign: Einfach f&uuml;r Alle - eine Initiative der Aktion
    Mensch'
  author_email: ''
  author_url: ''
  date: '2007-03-02 12:03:11 -0500'
  date_gmt: '2007-03-02 17:03:11 -0500'
  content: '<!--%kramer-pre%-->Wie man Videos trotzdem sauber einbettet beschreibt
    Peter Murray in dem aktualisierten Artikel: &raquo;Update to &rsaquo;Embedded
    Web Video in a Standards-Compliant, Accessible, and Successful Way&lsaquo;&laquo;.  <i>(<a
    href="http://translate.google.com/translate?u=http://www.einfach-fuer-alle.de/blog/index.php%3Fid%3DP2007"
    rel="nofollow">translated</a>)</i><!--%kramer-post%-->'
- id: 29158
  author: Webrichtlijnen over online audio en video - Stichting Bartim
  author_email: ''
  author_url: http://accessibility.nl/internet/artikelen/audiovideo
  date: '2008-01-11 09:31:06 -0500'
  date_gmt: '2008-01-11 13:31:06 -0500'
  content: "<!--%kramer-ref-pre%-->[...] http://dltj.org/2007/02/update-to-embedded-web-video/
    [...]<!--%kramer-ref-post%-->"
---
With the release of Microsoft's [Windows Media Player version 11](http://www.microsoft.com/windows/windowsmedia/player/11/default.aspx), the Microsoft Media Server (MMS) protocol is [officially no longer supported](http://web.archive.org/web/20121021035215/http://www.microsoft.com/windows/windowsmedia/licensing/netprokit.aspx). (Except, of course, for the confusing/amusing footnote on that page that says 'mms://' URIs are "highly recommended" as a [protocol rollover URL](http://msdn2.microsoft.com/en-gb/library/aa390673.aspx) — only Microsoft can at the same time make something deprecated and highly recommended.) As Ryan Eby noted earlier this year, those generating ASX files for Windows Media Player need to adjust their scripts.

Last year I published an entry called [Embedded Web Video in a Standards-Compliant, Accessible, and Successful Way](http://localhost:4000/article/standards-compliant-web-video/) on how to embed (without using the non-standard &lt;embed&gt; tag) video on an HTML page. It has been one of the most widely read articles on_DLTJ.org_, and so I wanted to publish an updated version of the script from that article to take into account this new wrinkle from Microsoft. The change is at line #41 below:


{% highlight perl %}
#!/usr/bin/perl -w
# Copyright (C) 2006-2007 OhioLINK
#
# This file is part of the OhioLINK Digital Resource Commons (DRC) Project.
#
# The OhioLINK DRC is free software; you can redistribute it and/or
# modify it under the terms of the Affero General Public License as
# published by Affero, Inc. -- either version 1 of the License, or
# (at your option) any later version.
#
# The OhioLINK DRC Project is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY -- without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Affero General Public License for more details.
#
# You should have received a copy of the Affero General Public
# License in the LICENSE.txt file that comes with the DRC project;
# if not, write to DRC Development Team, OhioLINK, 2455 North Star Rd,
# Suite 300, Columbus, OH 43221, USA.

if (!$ENV{PATH_INFO}) {
  print "Location: http://no-path-info-given/\r\n\r\n";
} else {
  ($format,$id) = $ENV{PATH_INFO} =~ q#^/+(.*?)/(.*)$#;

  if ($format =~ /Quicktime/i) {
    print "Location: http://video.ohiolink.edu/blah/Quicktime/$id\r\n\r\n";
  } elsif ($format =~ /Real/i) {
    print "Location: http://video.ohiolink.edu:8080/ramgen/blah/Real/$id\r\n\r\n";
  } elsif ($format =~ /Windows/i) {
    ($winType,$winFile) = $id =~ q#^(.*?)/(.*)$#;
    if ($winType =~ /asx/i) {
      $winFile =~ s/\..*$//;
      print >> "EoMarkup";
Content-type: video/x-ms-asf

<asx version="3.0">
<copyright>(c) 2005 - xxx</copyright>
<entry>
<ref href="mms://video.ohiolink.edu/blah/Windows/$winFile.wmv?SAMI=http://rave.ohiolink.edu/dmc/blah/windows/smi/$winFile.smi">
</ref><ref href="http://video.ohiolink.edu/blah/Windows/$winFile.wmv?SAMI=http://rave.ohiolink.edu/dmc/blah/windows/smi/$winFile.smi"></ref>
<copyright>(c) 2005 - xxx</copyright>
</entry>
</asx>
EoMarkup
    } elsif ($winType =~ /wmv/i) {
      print "Location: mms://video.ohiolink.edu/blah/Windows/$winFile\r\n\r\n";
    } elsif ($winType =~ /smi/i) {
      use LWP::UserAgent;
      $ua = LWP::UserAgent->new;
      $ua->agent("$0-lwp/0.1 " . $ua->agent);
      $req = HTTP::Request->new(GET => "http://video.ohiolink.edu:8080/blah/Windows/$winFile");
      # send request
      $res = $ua->request($req);
      # check the outcome
      if ($res->is_success) {
        print "Content-type: application/smil\r\n\r\n";
        print $res->decoded_content;
      } else {
        print "Location: http://error-from-remote-server/$winType/$winFile/".$res->code."/".$res->message."\r\n\r\n";
      }
    } else {
      print "Location: http://invalid-Windows-format-given/$winType/$winFile\r\n\r\n";
    }
  } else {
    print "Location: http://invalid-format-given/$format/$id\r\n\r\n";
  }
}
{% endhighlight %}

Thanks to Neil Bennett at the University of Southern Maine for contacting OhioLINK about the problem, providing some very helpful diagnostics, and pointing us to the URL to the protocol table mentioned above. It is also worth noting that the A List Apart website posted a new article about [sane ways of embedding Flash content](http://alistapart.com/articles/flashembedcagematch) that builds upon the same work in the original 'Embedded Web Video...' article. It might be time to update some of the techniques used in the original article, but that'll need to wait for another time.

The text was modified to remove a link to http://blog.ryaneby.com/archives/windows-media-player-11-and-mms/ on January 19th, 2011.
