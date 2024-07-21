---
layout: wordpress-import
status: published
published: true
title: Fronting Tomcat with Apache HTTPD to Remove Ports and Context Paths
modified: 2018-01-15T22:38:08-05:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 281
wordpress_url: http://dltj.org/2007/09/apache-httpd-and-tomcat/
date: '2007-09-19 22:31:33 -0400'
date_gmt: '2007-09-20 02:31:33 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- apache
- httpd
- tomcat
- web development
- usability
- howto
comments:
- id: 23259
  author: Fronting Tomcat with Apache HTTPD to Remove Ports and Context Paths
  author_email: ''
  author_url: http://www.dzone.com/links/fronting_tomcat_with_apache_httpd_to_remove_ports.html
  date: '2007-09-20 00:01:18 -0400'
  date_gmt: '2007-09-20 04:01:18 -0400'
  content: "<!--%kramer-ref-pre%-->[...] DataGazetteer via dltj.org Submitted: Sep
    19 / 22:36        Fronting Tomcat with Apache HTTPD to Remove Ports and Context
    Paths This How-To guide shows a combination of software and configuration to clean
    up URLs by removing [...]<!--%kramer-ref-post%-->"
- id: 23334
  author: Caveat Lector &raquo; So now I know
  author_email: ''
  author_url: ''
  date: '2007-09-20 17:17:29 -0400'
  date_gmt: '2007-09-20 21:17:29 -0400'
  content: "<!--%kramer-ref-pre%-->[...] This is how I shoulda done it. [...]<!--%kramer-ref-post%-->"
- id: 23555
  author: chuck
  author_email: simpson.cl@gmail.com
  author_url: ''
  date: '2007-09-22 19:34:41 -0400'
  date_gmt: '2007-09-22 23:34:41 -0400'
  content: |-
    If you have other (non-tomcat) content under Apache's docroot you
    may want to add the following rewrite conditions to proxy requests
    only if they are not in the doc root. # if request is not a file or
    directory RewriteCond %{REQUEST_FILENAME} !-f RewriteCond
    %{REQUEST_FILENAME} !-d # then rewrite the request and proxy to
    Tomcat RewriteRule ^/(.*) ajp://localhost:8009/context_path/$1 [P]
- id: 23563
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2007-09-22 20:34:02 -0400'
  date_gmt: '2007-09-23 00:34:02 -0400'
  content: Great tip, Chuck -- thanks for adding the comment.
- id: 23751
  author: Apache Tomcat 6.0.14 | Antlinux
  author_email: ''
  author_url: http://www.antlinux.com/stateofthehttpd/httpd-2007Q2/apache-tomcat
  date: '2007-09-24 23:32:27 -0400'
  date_gmt: '2007-09-25 03:32:27 -0400'
  content: |-
    <!--%kramer-ref-pre%-->[...] new users/groups on Debian. Here's a site that describes how
    to set up the JK proxy, as well as a blog post on how to set up
    Apache/Tomcat using AJP. previous&nbsp;up mod_perl 2.0.3 By brian
    at 13Sep2007 - 15:46 | Apache HTTP Server | Java | Shell [...]<!--%kramer-ref-post%-->
- id: 24527
  author: The Library Shelf - Today&#8217;s Top Blog Posts from Librarians - Powered
    by SocialRank
  author_email: ''
  author_url: http://thelibraryshelf.com/fronting-tomcat-with-apache-httpd-to-remove-ports-and-context-paths-in-disruptive-library-technology-jester/
  date: '2007-10-01 06:16:13 -0400'
  date_gmt: '2007-10-01 10:16:13 -0400'
  content: |-
    [...] Fronting Tomcat with Apache HTTPD to Remove Ports and Context
    Paths in Disruptive Library Technology... [...]
- id: 34040
  author: How do I connect my tomcat app to apache 2 so the paths aren't lame? - Stack
    Overflow
  author_email: ''
  author_url: http://stackoverflow.com/questions/230644/how-do-i-connect-my-tomcat-app-to-apache-2-so-the-paths-arent-lame
  date: '2008-10-23 18:07:20 -0400'
  date_gmt: '2008-10-23 22:07:20 -0400'
  content: "<!--%kramer-ref-pre%-->[...] it looks like this is kind of a pain in the
    rear. [...]<!--%kramer-ref-post%-->"
- id: 35201
  author: JSR 168 and JSR 286 Portlet Development Blog - News, Articles, Tutorials,
    Tips, Tricks and Hints
  author_email: ''
  author_url: http://portletwork.blogspot.com/2009/04/rewriting-urls-in-web-application-using.html
  date: '2009-04-14 16:42:48 -0400'
  date_gmt: '2009-04-14 20:42:48 -0400'
  content: "<!--%kramer-ref-pre%-->[...] I found an article explaining some extra
    steps needed to get things up and working. Together with another useful guide,
    I was able to set things up producing the result I wanted.This set up is not specific
    to WebLogic. [...]<!--%kramer-ref-post%-->"
- id: 66789
  author: Wie verbinde ich mein Kater auf ca. 2 Apache, die Wege sind nicht lahm?
  author_email: ''
  author_url: ''
  date: '2010-04-27 15:48:16 -0400'
  date_gmt: '2010-04-27 19:48:16 -0400'
  content: "<!--%kramer-ref-pre%-->[...] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &nbsp;
    es sieht aus wie dieses ist eine Art Schmerz im R&uuml;cken.  Apache ist buchst&auml;blich
    Umschreiben Seiten, wie es sie dient ...  Ich denke, ich werde einen [...]<!--%kramer-ref-post%-->"
- id: 72647
  author: "&iquest;C&oacute;mo puedo conectar mi aplicaci&oacute;n Tomcat para Apache
    2 que los caminos no son cojo?"
  author_email: ''
  author_url: ''
  date: '2010-06-07 13:43:54 -0400'
  date_gmt: '2010-06-07 17:43:54 -0400'
  content: "<!--%kramer-ref-pre%-->[...] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &nbsp;
    parece que esta es una especie de dolor en la parte trasera.  Apache es, literalmente,
    volver a escribir las p&aacute;ginas, ya que les sirve ...  Creo que voy a [...]<!--%kramer-ref-post%-->"
- id: 231755
  author: exist-open - Preferred Method of Virtual Hosting eXist Under Apache/Tomcat
  author_email: ''
  author_url: http://exist.2174344.n4.nabble.com/Preferred-Method-of-Virtual-Hosting-eXist-Under-Apache-Tomcat-td4216487.html
  date: '2012-03-15 12:00:08 -0400'
  date_gmt: '2012-03-15 16:00:08 -0400'
  content: "<!--%kramer-ref-pre%-->[...] somewhere. Is there a solution to this? I
    tried `mod_proxy_html` following [this tutorial](http://dltj.org/article/apache-httpd-and-tomcat/)
    but only got server errors. Would `mod_proxy_xml` do the trick? Or is there another,
    preferred [...]<!--%kramer-ref-post%-->"
- id: 234448
  author: pledbrook
  author_email: ''
  author_url: http://twitter.com/pledbrook/status/182768359220330496
  date: '2012-03-22 09:59:07 -0400'
  date_gmt: '2012-03-22 13:59:07 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">@dominicclifton Marc&#39;s replied. It sounds
    like you need URL rewriting: http://t.co/iTxYHrZx</span></span>'
- id: 243768
  author: Luke Meyer
  author_email: sosiouxme@gmail.com
  author_url: http://sosiouxme.wordpress.com/
  date: '2012-04-17 11:01:12 -0400'
  date_gmt: '2012-04-17 15:01:12 -0400'
  content: "I'm curious why you went with:\r\nRewriteEngine     on\r\nRewriteRule
    ^(/.*)      ajp://localhost:8009/context_path/$1    [P]\r\n\r\nWhen ProxyPass
    can do the same \"rewriting\" job somewhat more clearly:\r\n\r\nProxyPass / ajp://localhost:8009/context_path/\r\n\r\nOther
    than that, thanks for a concise approach to showing how this problem can be addressed,
    sometimes.\r\n\r\nOne added note: if your app uses AJAX or deals with URLs in
    JavaScript in any way, chances are that mod_proxy_html won't be able to rewrite
    them properly and you'll still get references to Tomcat's URLs leaking out to
    the public. For this reason, it is by far simplest and safest to just deploy your
    application on Tomcat at the same path (context) that is used on the proxy. You
    can always deploy with a context descriptor in order to specify any path you want
    (it does not have to match the WAR file name)."
- id: 243833
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2012-04-17 15:51:37 -0400'
  date_gmt: '2012-04-17 19:51:37 -0400'
  content: Luke -- do be honest I don't remember why I went with the RewriteRule rather
    than the ProxyPass.  I have a vague memory of there being a reason, but the actual
    thought is lost to the mists of time.  Thanks for the added note about AJAX and
    JavaScript URLs.
- id: 252244
  author: Fronting Tomcat with Apache HTTD to remove ports and context paths &laquo;
    Lisa and Philip Blog
  author_email: ''
  author_url: http://lisaandphilip.wordpress.com/2010/11/04/fronting-tomcat-with-apache-httd-to-remove-ports-and-context-paths/
  date: '2012-05-23 12:01:37 -0400'
  date_gmt: '2012-05-23 16:01:37 -0400'
  content: "<!--%kramer-ref-pre%-->[...] http://dltj.org/article/apache-httpd-and-tomcat/
    [...]<!--%kramer-ref-post%-->"
- id: 529999
  author: John
  author_email: john@nowhere.com
  author_url: ''
  date: '2013-04-22 01:57:39 -0400'
  date_gmt: '2013-04-22 05:57:39 -0400'
  content: I always wondered why AJP did not override request.getContextPath() the
    same way it does with request.getServerPort(), request.getScheme(), request.getServerName()...
    Maybe there's a good (technical?) reason I'm not aware of.
- id: 656264
  author: Integrace Apache a Tomcat s mod_proxy &mdash; Virtage Devblog &mdash; java,
    eclipse, eclipse rcp, eclipse rap, swt, jface, osgi, ubuntu, sysadmin, linux,
    derby, javadb, jetty
  author_email: ''
  author_url: http://devblog.virtage.cz/2014/02/integrace-apache-a-tomcat-s-mod_proxy/
  date: '2014-03-20 10:33:48 -0400'
  date_gmt: '2014-03-20 14:33:48 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;] Ide&aacute;ln&iacute; je se absolutn&iacute;ch
    URL zbavit. Když to ale opravdu nejde je jedin&yacute;m ře&scaron;en&iacute;m
    proch&aacute;zet obsah HTML a nahrazovat v&scaron;echny lok&aacute;ln&iacute;
    URL veřejn&yacute;mi ekvivalenty. Tuto prostředkově n&aacute;ročnou operaci dok&aacute;že
    modul mod_proxy_html, kter&yacute; v&scaron;ak nen&iacute; ve standardn&iacute;
    distribuci Apache. Kdyby v&aacute;s zaj&iacute;mali detaily. [&#8230;]<!--%kramer-ref-post%-->"
---
In this How-To guide, I show a combination of software and configuration to clean up URLs by removing the port numbers of the Java servlet engine (Tomcat) and the context path of the application. The goal is to create "[cool URLs](http://www.w3.org/Provider/Style/URI)" that are are short (removing the unnecessary context path) and follow conventions (using the default port "80" rather than "8080"). OhioLINK also uses a custom access control module -- built for Apache HTTPD -- which makes the fronting of Apache HTTPD for Tomcat even more desirable.

## Requirement

We're making use of the latest line of development for the Apache HTTPD series: [version 2.2.x](http://httpd.apache.org/docs/2.2/). The inclusion of [mod_proxy_ajp](http://httpd.apache.org/docs/2.2/mod/mod_proxy_ajp.html) -- replacing the custom "mod_jk" with a module that extends the httpd proxy engine -- in the latest major release of HTTPD makes our task much easier. This solution also uses HTTPD's mod_rewrite and an add-on module called [mod_proxy_html](http://apache.webthing.com/mod_proxy_html/). No additions or changes are needed to the stock Tomcat installation.

## The Plan

There are two overall tasks that we're going to ask the HTTPD server to do. First, receive the incoming HTTP request and proxy it to the Tomcat servlet engine using the AJP protocol. Second, rewrite the URL paths of the headers and the X/HTML body from the Tomcat servlet engine to eliminate any instances of the context path. In a visual sense, what we are trying to is rewrite the path so it can be processed by Tomcat (the green box) then remove the extraneous parts of the path in the resulting headers and X/HTML (the red box):

<table cellpadding="2" cellspacing="0">
<tr>
<td align="right"><i>Public Request URLs:&nbsp;&nbsp;</i></td>
<td colspan="2" align="right">http://e.com</td>
<td colspan="2">/remaining/path?and=params</td>
</tr>
<tr>
<td align="right"><i>URLs sent to Tomcat:&nbsp;&nbsp;</i></td>
<td>http://e.com</td>
<td style="background-color: #FFFFCC; padding-right: 0; margin-right: 0; border-left: 1px solid green; border-top: 1px solid green; border-bottom: 1px solid green;">:8080</td>
<td style="background-color: #FFFFCC; padding-left: 0; margin-left: 0; border-right: 1px solid green; border-top: 1px solid green; border-bottom: 1px solid green;">/context_path</td>
<td>/remaining/path?and=params</td>
</tr>
<tr>
<td align="right"><i>URLs as output by Tomcat:&nbsp;&nbsp;</i></td>
<td>http://e.com</td>
<td style="background-color: #FFFFCC; padding-right: 0; margin-right: 0; border-left: 1px solid red; border-top: 1px solid red; border-bottom: 1px solid red;">:8080</td>
<td style="background-color: #FFFFCC; padding-left: 0; margin-left: 0; border-right: 1px solid red; border-top: 1px solid red; border-bottom: 1px solid red;">/context_path</td>
<td>/next/page</td>
</tr>
<tr>
<td align="right"><i>URLs as seen by browser:&nbsp;&nbsp;</i></td>
<td colspan="2" align="right">http://e.com</td>
<td colspan="2">/next/page</td>
</tr>
</table>

The first half of this problem, modifying a request as they come into the Apache HTTPD server, will be handled by a [mod_rewrite](http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html) rule that rewrites the request to something Tomcat can understand then internally redirects it Tomcat via the AJP proxy. (Note that we are not using simply [ProxyPass](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html#proxypass) here because we want to send the request through the AJP interface to the Tomcat server, and [RewriteRule](http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html#rewriterule) allows us to do that with a `[P]` flag at the end of the RewriteRule line.) The second uses a combination of [ProxyPassReverse](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html#proxypassreverse) (a part of Apache-supplied mod_proxy extension that adjusts the URL in the Location, Content-Location and URI headers), [ProxyPassReverseCookiePath](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html#proxypassreversecookiepath) (also a part of the Apache-supplied mod_proxy extension; it rewrites the path string in Set-Cookie headers), and [ProxyHTMLURLMap](http://apache.webthing.com/mod_proxy_html/config.html) (from mod_proxy_html, a third-party extension that rewrites URLs inside X/HTML documents).

## Preparations

The 'mod_proxy_html' extension is likely new to your Apache HTTPD installation, so we need to download the source, compile it, and move it into the proper directory. Fortunately, this is rather straight forward:

{% highlight bash %}
wget 'http://apache.webthing.com/mod_proxy_html/mod_proxy_html-2.5.2.c'
apxs -c -I/usr/include/libxml2 -i mod_proxy_html-2.5.2.c
{% endhighlight %}

Note that we are not using the mod_proxy_html author's 3.0 version here. In my set-up, the 3.0 version was causing Apache HTTPD to dump core on _every_request (whether proxied or not), and the prior release works just fine for our purposes. The `apxs` line will compile, link, and copy the resulting library to the Apache modules directory for us.

## The Configuration

This is the contents a 'tomcat-proxy.conf' file that is placed in the 'conf.d' directory of the Apache HTTPD configuration directory (most likely `/etc/httpd/conf.d/tomcat-proxy.conf`, although your installation may vary).

{% highlight config %}
#
#  Information about 'mod_proxy_html' can be found at 
#   http://apache.webthing.com/mod_proxy_html/
LoadFile    /usr/lib/libxml2.so
LoadModule  proxy_html_module    modules/mod_proxy_html-2.5.2.so

# DON'T TURN ProxyRequests ON!  Bad things will happen
# http://httpd.apache.org/docs/2.2/mod/mod_proxy.html#access
# http://www.akadia.com/services/prevent_abuse_proxy.html
ProxyRequests off

# Necessary to have mod_proxy_html do the rewriting
RequestHeader      unset  Accept-Encoding

# Rewrite the URLs to proxy ("[P]") into the Tomcat server
RewriteEngine     on
RewriteRule ^(/.*)      ajp://localhost:8009/context_path/$1    [P]

# Be prepared to rewrite the HTML/CSS files as they come back
# from Tomcat
SetOutputFilter proxy-html

# Rewrite JavaScript and CSS files in addition to HTML files
ProxyHTMLExtended on

# Output Strict XHTML (add "Legacy" to the end of the line below
# to output Transitional XHTML)
ProxyHTMLDoctype XHTML 

# Rewrite HTTP headers and HTML/CSS links for everything else
ProxyPassReverse /context_path/ /
ProxyPassReverseCookiePath /context_path/ /
ProxyHTMLURLMap /context_path/ /
{% endhighlight %}

That's pretty much all there is to it.  You should note that mod_proxy_html, like any HTML scraper, requires modestly well-formed X/HTML.  If the markup is bad, the output from mod_proxy_html is likely to be unpredictable.
