---
layout: wordpress-import
status: published
published: true
title: 'DLTJ Updated, Readers Yawn'
modified: 2008-01-28T03:44:34+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 319
wordpress_url: http://dltj.org/article/dltj-updated-readers-yawn/
date: '2008-01-27 22:44:34 -0500'
date_gmt: '2008-01-28 03:44:34 -0500'
category: Meta Category
categories:
- Meta Category
tags:
- WordPress
- system administration
comments:
- id: 31581
  author: Weblog Tools Collection &raquo; Blog Archive &raquo; Reformatting WordPress
  author_email: ''
  author_url: http://weblogtoolscollection.com/archives/2008/02/25/reformatting-wordpress/
  date: '2008-02-26 12:25:18 -0500'
  date_gmt: '2008-02-26 17:25:18 -0500'
  content: "<!--%kramer-ref-pre%-->[...] talked about my own experience on my blog.
    The real show-stopper for me was the renumbering of posts. That caused all sorts
    of [...]<!--%kramer-ref-post%-->"
---
<p>At least I hope that is the correct headline.  I've been having some problems with this installation of WordPress lately -- in particular, I could no longer activate or deactivate plugins -- and the only solution offered in the WordPress codex was to start with a fresh installation of WordPress.  Now you know how I spent my free time this weekend.  While doing so, I updated the <a href="http://www.plaintxt.org/themes/barthelme/">Barthelme</a> theme and along the way gained some really need Semantic Web coolness to the underlying XHTML of the blog pages.  The version of Barthelme is still a heavily, heavily hacked one, but hopefully the clean up this weekend will make it possible to keep up with new versions of the underlying theme files without major headaches.  I also updated all of the plugins and cleaned out lots of old cruft in the plugins directory and in the theme files.  As a result, the pages seem to load faster.  Maybe that is just my wishful thinking.</p>
<p>Like the headline says, the average reader shouldn't notice a difference.  One thing I did change was the Permalink structure; I removed the year and month from the URLs and just put the postings behind the word "article".  There are HTTP 301 ("Permanently Moved") redirects in place, so your browser will be quietly redirected to the new location.  If you do notice anything wrong, let me know:<br />
<!--cforms--></p>
<p>Also, a word of warning for those that try to fix their own WordPress blog, the process of getting your posts, content, and taxonomy terms from your old instance to your new instance is really, really broken.  The suggested way to move content is by Exporting to a WordPress-specific XML format on your old blog, then importing it into your new blog.  This caused many problems.  First, if you are using a 2.3.x version of WordPress, you'll run into <a href="http://trac.wordpress.org/ticket/5330">a bug where tags are given numbers rather than the names</a>.  The patch -- a one line change to the import PHP script -- works as advertised.  But then you'll find that, if you have ever deleted a post or term, the act of importing the content will reassign new, sequential IDs -- skipping over the deleted IDs in the old database as if they were never there.  That's okay, except many <em>other</em> plugins (most notably in my case, <a href="http://wordpress.org/extend/plugins/in-series/">In-Series</a>) rely on the IDs remaining constant because the ID number is stored in other tables.  So save yourself a lot of trouble and just copy over the required tables in your underlying database.  I used PhpMyAdmin to copy the wp_comments, wp_posts, wp_terms, wp_term_relationships, and wp_term_taxonomy tables from the old database to the new.  And everything just worked right after that.</p>
