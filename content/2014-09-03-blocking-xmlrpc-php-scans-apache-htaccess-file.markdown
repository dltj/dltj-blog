---
layout: wordpress-import
status: published
published: true
title: 'Blocking /xmlrpc.php Scans in the Apache .htaccess File'
modified: 2014-09-04T02:41:47+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 19848
wordpress_url: http://dltj.org/?p=19848
date: '2014-09-03 22:41:47 -0400'
date_gmt: '2014-09-04 02:41:47 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- WordPress
- apache
- security
- http
comments:
- id: 662567
  author: Rohan
  author_email: rohan.milton@gmail.com
  author_url: ''
  date: '2014-10-03 12:40:01 -0400'
  date_gmt: '2014-10-03 16:40:01 -0400'
  content: Brilliant, worked for me! Thanks.
- id: 662642
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2014-10-03 21:24:17 -0400'
  date_gmt: '2014-10-04 01:24:17 -0400'
  content: 'Your welcome! I''m glad you found it helpful. '
- id: 670431
  author: Clay
  author_email: cmaney@gmail.com
  author_url: ''
  date: '2014-11-30 10:34:45 -0500'
  date_gmt: '2014-11-30 15:34:45 -0500'
  content: This was just what I needed... I had previously blocked this with the Files
    directive, but it was still killing the CPU.  This is much better.  Thanks!
- id: 683618
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2015-12-30 10:48:32 -0500'
  date_gmt: '2015-12-30 15:48:32 -0500'
  content: Good point, Marcus -- it would be much better to use firewall rules to
    prevent this kind of activity from reaching the web server at all.  The fail2ban
    wiki has more details about using it to <a href="http://www.fail2ban.org/wiki/index.php/Category:HTTP"
    rel="nofollow">stop requests to web servers</a>.
- id: 685349
  author: mattileblanc
  author_email: mattijsspierings@gmail.com
  author_url: http://www.b-u-t.net
  date: '2016-02-03 18:48:05 -0500'
  date_gmt: '2016-02-03 23:48:05 -0500'
  content: "Hi, this worked for me. I can see in my access log it returns a 403 so
    it shouldn't kill my php process. However, it might create huge log files right,
    or do those guys stop pinging me after a while? Otherwise I should just block
    that particular IP address?\r\n\r\nThanks"
- id: 685364
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2016-02-04 09:24:46 -0500'
  date_gmt: '2016-02-04 14:24:46 -0500'
  content: In my experience, whoever was doing it gave up after a while.  I left the
    rule in, but I stopped seeing the scans.  In my case it was coming from a number
    of IP addresses, so there wasn't just one that I could block.
---
<p>Someone out there on the internet is repeatedly hitting this blog's /xmlrpc.php service, probably looking to enumerate the user accounts on the blog as a precursor to a password scan (as described in <a href="http://www.saotn.org/huge-increase-wordpress-xmlrpc-php-post-requests/" title="Huge increase in WordPress xmlrpc.php POST requests | Sysadmins of the North">Huge increase in WordPress xmlrpc.php POST requests</a> at Sysadmins of the North).  My access logs look like this:</p>
```text
176.227.196.86 - - [04/Sep/2014:02:18:19 +0000] "POST /xmlrpc.php HTTP/1.0" 200 291 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
195.154.136.19 - - [04/Sep/2014:02:18:19 +0000] "POST /xmlrpc.php HTTP/1.0" 200 291 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
176.227.196.86 - - [04/Sep/2014:02:18:19 +0000] "POST /xmlrpc.php HTTP/1.0" 200 291 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
176.227.196.86 - - [04/Sep/2014:02:18:21 +0000] "POST /xmlrpc.php HTTP/1.0" 200 291 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
176.227.196.86 - - [04/Sep/2014:02:18:22 +0000] "POST /xmlrpc.php HTTP/1.0" 200 291 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
176.227.196.86 - - [04/Sep/2014:02:18:24 +0000] "POST /xmlrpc.php HTTP/1.0" 200 291 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
195.154.136.19 - - [04/Sep/2014:02:18:24 +0000] "POST /xmlrpc.php HTTP/1.0" 200 291 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
176.227.196.86 - - [04/Sep/2014:02:18:26 +0000] "POST /xmlrpc.php HTTP/1.0" 200 291 "-" "Mozilla/4.0 (compatible: MSIE 7.0; Windows NT 6.0)"
```
<p>By itself, this is just annoying -- but the real problem is that the PHP stack is getting invoked each time to deal with the request, and at several requests per second from different hosts this was putting quite a load on the server.  I decided to fix the problem with a slight variation from what is suggested in the Sysadmins of the North blog post.  This addition to the .htaccess file at the root level of my WordPress instance rejects the connection attempt at the Apache level rather than the PHP level:</p>
```text
RewriteCond %{REQUEST_URI} =/xmlrpc.php [NC]
RewriteCond %{HTTP_USER_AGENT} .*Mozilla\/4.0\ \(compatible:\ MSIE\ 7.0;\ Windows\ NT\ 6.0.*
RewriteRule .* - [F,L]
```
<p>Which means:</p>
<ol>
<li>If the requested path is /xmlrpc.php, and</li>
<li>you are sending this particular agent string, then</li>
<li>send back a 403 error message and don't bother processing any more Apache rewrite rules.</li>
</ol>
<p>If you need to use this yourself, you might find that the HTTP_USER_AGENT string has changed.  You can copy the user string from your Apache access logs, but remember to preface each space or each parenthesis with a backslash.</p>
