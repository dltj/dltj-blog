---
layout: wordpress-import
status: published
published: true
title: 'Sakai gets JSR-170 support; possible integration point with FEDORA?'
modified: 2006-11-08T18:32:56+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 143
wordpress_url: http://dltj.org/2006/11/sakai-gets-jsr170/
date: '2006-11-08 13:32:56 -0500'
date_gmt: '2006-11-08 18:32:56 -0500'
category: Library Technology
categories:
- Fedora
- Unified Content Repository
- Sakai
tags:
- Sakai
- digital libraries
- jsr170
- Fedora Repository
comments:
- id: 33905
  author: DSpace 2.0/Modelling Services - DSpace Wiki
  author_email: ''
  author_url: https://wiki.duraspace.org/display/DSPACE/DSpace+2.0+Modelling+Services
  date: '2008-09-28 18:16:52 -0400'
  date_gmt: '2008-09-28 22:16:52 -0400'
  content: '<!--%kramer-ref-pre%-->[...] http://dltj.org/article/fedora-plus-sakai-3/trackback/
    http://dltj.org/article/sakai-gets-jsr170/trackback/    Retrieved from "http://wiki.dspace.org/index.php/DSpace_2.0/Modelling_Services"
    Category: DSpace [...]<!--%kramer-ref-post%-->'
---
<p>Earlier this year, I was on a quest to hook a <a href="http://www.fedora.info/" title="FEDORA home page">FEDORA content repository</a> into the <a href="http://www.sakaiproject.org/" title="Sakai Project Homepage">Sakai collaboration and learning environment</a>.  What looked at first to be a fairly easy integration turned out to be <span class="removed_link" title="http://issues.sakaiproject.org/confluence/x/ikE">rather complicated</span> and I set the project aside for another time.  Today brings word from <a href="http://blog.tfd.co.uk/" title="Ian Boston&#039;s Sakai Blog">Ian Boston</a> of a <a href="http://issues.sakaiproject.org/confluence/display/RES/JSR-170" title="JSR-170 - Project: Resources - Confluence">JSR-170 implementation in Sakai</a>:</p>
<blockquote><p>During the Summer of 2006, I did a JSR-170 Implementation of ContentHostingService as a prototype against the then Trunk 2.2 ContentHostingService. The implementation took the ContentHostingService API and re-implemented it using JSR-170 under the covers. It was done in in such a way as to allow JSR-170 clients (eg WebDAV implementations) to use the JSR-170 API directly and still obey the Sakai AuthZ implementation.<br />
<address><a href="http://issues.sakaiproject.org/confluence/display/RES/JSR-170" title="JSR-170 - Project: Resources - Confluence">JSR-170 - Project: Resources - Sakai Confluence</a></address>
</blockquote>
<p><a href="http://www.jcp.org/en/jsr/detail?id=170" title="The Java Community Process(SM) Program - JSRs: Java Specification Requests - detail JSR# 170">JSR 170</a>, as you might recall, is the "specification for a Java platform API for accessing content repositories in a uniform manner." <footnote>"JSR-170," <i>Wikipedia, The Free Encyclopedia,</i> <a href="http://en.wikipedia.org/wiki/Content_repository_API_for_Java?oldid=84044565">http://en.wikipedia.org/wiki/Content_repository_API_for_Java?oldid=84044565</a> (accessed November 8, 2006)</footnote>  What makes this implementation most interesting,  I think, is Ian's last sentence &mdash; using a WebDAV implementation to speak directly to the JSR-170 content repository while taking into account the AuthZ settings in Sakai.</p>
<p>Now we need a JSR-170 implementation on top of FEDORA to complete the pairing.  We'd want Sakai's AuthZ settings to be reflected in FEDORA's XACML rules, of course, the the mind boggles a bit about how to get this done, but hopefully we can get back to it again soon and see if we can make it work.
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://issues.sakaiproject.org/confluence/x/ikE on January 13th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.tfd.co.uk/blogs/sakaiblog/ to http://blog.tfd.co.uk/ on January 19th, 2011.</p>
