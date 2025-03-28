---
layout: wordpress-import
status: published
published: true
title: 'Possible Resolution to Technorati Update Problem'
modified: 2006-09-12T01:49:59+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 114
wordpress_url: http://dltj.org/2006/09/resolving-technorati-update-problem/
date: '2006-09-11 21:49:59 -0400'
date_gmt: '2006-09-12 02:49:59 -0400'
category: Raw Technology
categories:
- Meta Category
- Raw Technology
tags:
- WordPress
- Extended Live Archive
- technorati
- feedburner
comments:
- id: 4047
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-09-15 18:58:37 -0400'
  date_gmt: '2006-09-15 22:58:37 -0400'
  content: For whatever reason -- the intervention of Technorati staff or the changes
    that I describe in this post -- <span class="removed_link" title="http://www.technorati.com/blogs/http://dltj.org">DLTJ
    is still being actively indexed</span> by Technorati's spiders.  Let's hope it
    continues!...
---
<p>Up until about an hour ago, Technorati refused to update <span class="removed_link" title="http://www.technorati.com/blogs/http%3A%2F%2Fdltj.org">its database of postings to DLTJ</span>, and having reached the 31-day point of no updates I was starting to wonder what to do about it.  I came up with two theories for which I put in fixes to the configuration and theme setup of DLTJ, but in the end I'm not sure if either definitively provides a solution for anyone else in the same situation.  In the spirit of helping out one's neighbors, though, here are the theories and fixes.  DLTJ is a standalone (e.g. not hosted) Wordpress 2.0.4 installation, so YMMV.</p>
<h2>Theory #1:  Technorati Doesn't Like Feedburner</h2>
<p>I read some blog posts and messages in the Feedburner forums that suggested blogs that use Feedburner were causing Technocrati to hick-up and not index content.  My solution is to let Technorati see the raw feed and not get redirected to Feedburner.  This is accomplished with additions to the Apache mod_rewrite rules in the <code>.htaccess</code> file.

```text
<ifmodule mod_rewrite.c>
RewriteEngine On
# These Rules redirect all feed traffic, except that of Technorati and FeedBurner itself, to FeedBurner
RewriteBase /
RewriteCond %{HTTP_USER_AGENT} !^FeedBurner.*$
RewriteCond %{HTTP_USER_AGENT} !^Technorati.*$
RewriteCond %{QUERY_STRING} ^feed=(feed|rdf|rss|rss2|atom)$
RewriteRule ^(.*)$ http://feeds.dltj.org/DisruptiveLibraryTechnologyJester [R,L]
RewriteCond %{HTTP_USER_AGENT} !^FeedBurner.*$
RewriteCond %{HTTP_USER_AGENT} !^Technorati.*$
RewriteRule ^(feed|rdf|rss|rss2|atom)/?(feed|rdf|rss|rss2|atom)?/?$ http://feeds.dltj.org/DisruptiveLibraryTechnologyJester [R,L]
RewriteCond %{HTTP_USER_AGENT} !^FeedBurner.*$
RewriteCond %{HTTP_USER_AGENT} !^Technorati.*$
RewriteRule ^wp-(feed|rdf|rss|rss2|atom).php http://feeds.dltj.org/DisruptiveLibraryTechnologyJester [R,L]
</ifmodule>
```
If it the HTTP User-Agent string doesn't begin with <code>FeedBurner</code> or <code>Technorati</code>, it falls through to the Wordpress-supplied feed mechanisms.</p>
<h2>Theory #2:  A Too-Complicated Home Page Confuses Technorati</h2>
<p>In addition to looking at the feeds themselves, Technorati will look at the home page of the blog to see if the items still appear as "current" (presumably).  About a month ago I put in place a <a href="/">modestly complicated, hand-coded home page</a> that puts an instance of <a href="http://www.sonsofskadi.net/extended-live-archive/" title="http://www.sonsofskadi.net/extended-live-archive/">Extended Live Archive</a> front and center.  Since this is JavaScript-driven and pushes the list of recent posts pretty far down the HTML page, I wondered if this could be screwing up the Technorati spider.  The solution here was to sniff the User-Agent string in the theme's <code>index.php</code> file in order to strip away all of the cruft for Technorati's spider.<br />
```php
$useragent = getenv("HTTP_USER_AGENT");
if (preg_match("/Technorati/i", "$useragent")) {
   // do the un-fancy, barebones stuff for Technorati
} else {
   // do the really nice stuff for everyone else
}
```
(Remember to surround the appropriate parts of the PHP markup with <code>&lt;?php</code> and <code>?&gt;</code>...)</p>
<h2>Why I May Never Know If Either of These Is Needed</h2>
<p>Shortly after I put these two changes in place (literally, after a week of sending e-mails to Technorati's tech support and two hours after coding these fixes) I got a note from Technorati saying:</p>
<blockquote><p>
  Please accept my sincerest apologies for the delay in getting back to you.  We've been experiencing a backlog in support and are working hard to address everyone.  I've taken a look at the issue regarding picking up your pings for "dltj.org".  After making a small adjustment, I've sent our spiders to revisit your page and your blog has been indexed with your most recent posts.  </p>
<p>http://technorati.com/blogs/dltj.org/</p>
<p>  Everything now appears to be working as it should, but please let us know if you experience any problems in the future.  Do not hesitate to contact us if you have any other questions.  We apologize for any inconvenience.  Thank you for using Technorati!
</p></blockquote>
<p>...and indeed Technorati's index for DLTJ has been updated.  So I may never know if it was a problem on my end or Technorati's end.</p>
<p>Figuring that these two changes can't do any harm and might actually be doing some good, I plan to leave them in place for a while and see if DLTJ keeps getting indexed.  The first test comes with this posting, which will cause Technorati to be pinged and hopefully this post will be picked up and indexed.  If not, it'll be back to the drawing board.</p>
