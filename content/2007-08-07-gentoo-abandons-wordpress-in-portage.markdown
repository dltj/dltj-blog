---
layout: wordpress-import
status: published
published: true
title: 'Gentoo Abandons WordPress in Portage'
modified: 2007-08-07T14:43:05+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 269
wordpress_url: http://dltj.org/2007/08/gentoo-abandons-wordpress-in-portage/
date: '2007-08-07 10:43:05 -0400'
date_gmt: '2007-08-07 14:43:05 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- WordPress
- Gentoo
comments: []
---
<p>I don't think this has been widely announced, but while waiting for an update to <a href="http://www.gentoo.org/" title="Gentoo Linux homepage">Gentoo</a>'s portage entry for <a href="http://wordpress.org/" title="WordPress homepage">WordPress</a> to cover <a href="http://wordpress.org/development/2007/08/wordpress-222-and-2011/" title="WordPress 2.2.2 and 2.0.11 announcement">the latest security and bug fixes</a>, I discovered in the comments of <a href="http://bugs.gentoo.org/show_bug.cgi?id=168529" title="Gentoo Bug 168529 - www-apps/wordpress" &amp;lt;="2.1.1 AdminPanel CSRF/XSS">a bug in Gentoo's bugzilla database</a> that they are making no effort to support WordPress on Gentoo.  I think this is really a poor move on Gentoo's part.  As one of the bug commenters noted, "Wordpress is, in general, a good product with an extremely active user community and good upstream maintenance."  ((<a href="http://bugs.gentoo.org/show_bug.cgi?id=168529#c16" title="Gentoo Bug 168529 - www-apps/wordpress" <="2.1.1 AdminPanel CSRF/XSS">Comment  #16</a> on bug #168529 from Stephen Ulmer dated 2007-03-17 16:09:26 0000 ))</p>
<p>A <a href="http://www.gentoo.org/security/en/glsa/glsa-200703-23.xml" title="Gentoo Linux Security Advisory -- WordPress: Multiple vulnerabilities"><abbr title="Gentoo Linux Security Advisory">GLSA</abbr> was issued for WordPress vulnerabilities in March</a> -- problems that have since been fixed -- with this 'resolution':</p>
<blockquote><p>Due to the numerous recently discovered vulnerabilities in WordPress, this package has been masked in the portage tree. All WordPress users are advised to unmerge it.</p></blockquote>
<p>Now I'll admit that I should not be expecting updates to packages that have been hard masked, but really -- is this any way to treat the world's most popular blogging software?  In any case, I've abandoned Gentoo's ebuild for WordPress and have reverted to the <a href="http://codex.wordpress.org/Installing/Updating_WordPress_with_Subversion" title="Installing/Updating WordPress with Subversion">Subversion method for updating a WordPress installation</a>.  So here is a heads-up to do something similar should you find yourself in the same situation.</p>
<p>[20070812T2046 update:  The portage keepers <a href="http://bugs.gentoo.org/show_bug.cgi?id=168529#c31" title="Gentoo Bug 168529 - www-apps/wordpress" <="2.1.1 AdminPanel CSRF/XSS">bumped the version of Wordpress to 2.2.2</a> in Portage yesterday.]</p>
