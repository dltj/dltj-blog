---
layout: wordpress-import
status: published
published: true
title: 'SSL for WordPress Admin and the Problem with  XMLHttpRequest'
modified: 2008-03-20T15:38:34+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 344
wordpress_url: https://dltj.org/article/wordpress-ssl-xmlhttprequest/
date: '2008-03-20 11:38:34 -0400'
date_gmt: '2008-03-20 15:38:34 -0400'
category: Meta Category
categories:
- Meta Category
tags:
- WordPress
- ssl
- fix_admin_ssl
- XMLHttpRequest
- ajax
comments:
- id: 32725
  author: John Fink
  author_email: john.fink@gmail.com
  author_url: http://libgrunt.blogspot.com
  date: '2008-03-20 12:55:23 -0400'
  date_gmt: '2008-03-20 16:55:23 -0400'
  content: We have been wrestling with admin SSL and AJAX calls on our wpmu install
    for, oh geez, months and months and months.  If this does work, you are (once
    again) my hero.  Honest.  Hopefully it will function in wpmu like it does for
    your wp.
- id: 32726
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-03-20 12:57:45 -0400'
  date_gmt: '2008-03-20 16:57:45 -0400'
  content: I don't know anything about WPmu specifically, but if it works for you,
    great!  (Be sure to report back here one way or the other.)
- id: 32729
  author: Library Web Chic &raquo; Blog Archive &raquo; WordpressMU Migration Drama
  author_email: ''
  author_url: http://www.librarywebchic.net/wordpress/2008/03/19/wordpressmu-migration-drama/
  date: '2008-03-20 18:49:33 -0400'
  date_gmt: '2008-03-20 22:49:33 -0400'
  content: "<!--%kramer-ref-pre%-->[...] on 20 Mar 2008 at 9:45 am1Peter Murray [...]<!--%kramer-ref-post%-->"
- id: 37976
  author: Ray
  author_email: ray@tradingmetro.com
  author_url: ''
  date: '2009-08-31 18:07:04 -0400'
  date_gmt: '2009-08-31 22:07:04 -0400'
  content: I would like to see this plugin rather than hacking the plugins itself,
    which I have been doing!
- id: 37977
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2009-08-31 19:02:28 -0400'
  date_gmt: '2009-08-31 23:02:28 -0400'
  content: Ray --  Fortunately, the plug-in isn't required anymore...at least for
    the reasons I was originally using it.  I was surprised to see that the PHP code
    for the plugin was no longer included in the text of the post.  I was able to
    find an older version of the post, though, and restore the code.  I hope you find
    it useful.
- id: 38234
  author: WordPress
  author_email: ''
  author_url: http://wordpress.seesaa.net/pages/user/m/article?article_id=100938269&amp;stq=session%3A%3Ablog%3A%3Aa5cab24574e173a959258e29bf98230a
  date: '2009-09-29 00:50:54 -0400'
  date_gmt: '2009-09-29 04:50:54 -0400'
  content: "<!--%kramer-ref-pre%-->[...]  [...]<!--%kramer-ref-post%-->"
- id: 43685
  author: SSL and Cookies in WordPress 2.6 &laquo; Ryan Boren
  author_email: ''
  author_url: http://ryan.boren.me/2008/07/14/ssl-and-cookies-in-wordpress-26/
  date: '2010-02-06 12:18:42 -0500'
  date_gmt: '2010-02-06 17:18:42 -0500'
  content: "<!--%kramer-ref-pre%-->[...] SSL for WordPress Admin and the Problem with
    XMLHttpRequest | Disruptive Library Technology Jester [...]<!--%kramer-ref-post%-->"
---
<div style="border: 2px solid grey; padding: 1.5em;">Note!  The updates to <a href="http://boren.nu/archives/2008/07/14/ssl-and-cookies-in-wordpress-26/" title="&amp;raquo; SSL and Cookies in WordPress 2.6 Ryan Boren">SSL handling in WordPress version 2.6</a> handle the problem of SSL-encrypted admin sessions in a <em>much</em> less hackish sort of way.  It doesn't make any sense to use this plugin with <a href="http://wordpress.org/development/2008/07/wordpress-26-tyner/" title="http://wordpress.org/development/2008/07/wordpress-26-tyner/">WordPress version 2.6</a> when you can simply add <code>define(&rsquo;FORCE_SSL_ADMIN&rsquo;, true);</code> to your wp-config.php file.</div>
<p>The WordPress Codex has documentation for <span class="removed_link" title="http://codex.wordpress.org/Administration_Over_SSL">running the login, registration, and administration interfaces on an SSL server</span>.  There is even a <a href="http://wordpress.org/extend/plugins/admin-ssl-secure-admin/" title="WordPress &#8250; Admin-SSL &laquo; WordPress Plugins">plug-in</a> that will do much of the heavy lifting for you.  I have found both of these methods, by themselves, to be rather unsatisfactory, though, in that admin services that rely on AJAX calls back to WordPress break (such as the periodic saving of drafts).  What happens is this:  </p>
<ol type="1" start="1">
<li>Plugins will use the 'siteurl' and/or 'home' values in the <span class="removed_link" title="http://codex.wordpress.org/General_Options_SubPanel">Options &rarr; General</span> admin page, and that value is typically set to the "http://" rather than "https://" address of the blog.</li>
<li>The URL that plugins construct to talk back to the WordPress installation will go to an "http" address instead of the SSL-encrypted "https" address.</li>
<li>The admin page, loaded in the browser from the "https" address, attempts to talk back to the WordPress installation on a "http" address and triggers a exception.  In Firefox, the error looks like this:  <tt>Error: [Exception... "'Permission denied to call method XMLHttpRequest.open' when calling method: [nsIDOMEventListener::handleEvent]"...]</tt></li>
</ol>
<p>The security model in the browser prevents scripts on a page from using XMLHttpRequest ((See <a href="http://en.wikipedia.org/wiki/XMLHttpRequest" title="XMLHttpRequest - Wikipedia">http://en.wikipedia.org/wiki/XMLHttpRequest</a> for more information on XMLHttpRequest.)) back to any host on the internet <em>except</em> for the host where the script came from.  In this case, the difference between "http://..." and "https://..." is enough to trigger the problem.</p>
<p>So I fixed it with plug-in that uses an undocumented hook in WordPress 2.3.  If a plugin requests the value of 'siteurl' or 'home', a filter is called to check if the requested page is on the SSL server.  If it is, the filter changes the URL from 'http' to 'https'.  In that way, plug-ins will use the proper form of the URL.</p>
{% highlight php %}
< ?php
/*
Plugin Name: Fix Admin SSL
Plugin Script: fix_admin_ssl.php
Plugin URI: http://dltj.org/tag/fix_admin_ssl
Description: Fix the 'siteurl' and 'home' option values to make the protocol 'https' rather than 'http' when the page was requested with SSL.
Version: 1.0
License: GPL
Author: Peter Murray
Author URI: http://dltj.org/about
 
=== RELEASE NOTES ===
2008-02-18 - v1.0 - first version
*/
 
function fix_admin_ssl($url) {
  if ($_SERVER['HTTPS'] == 'on') {
    $url=preg_replace('/^http:\/\//','https://',$url);
  }
  return $url;
}
 
add_action ('option_siteurl', 'fix_admin_ssl', 1);
add_action ('option_home', 'fix_admin_ssl', 1);
 
?>
{% endhighlight %}
<p>One downside to this plug-in, though, is that it will appear to change the values of 'siteurl' and 'home' on the <span class="removed_link" title="http://codex.wordpress.org/General_Options_SubPanel">Options &rarr; General</span> admin page.  The values in the database are still the 'http' ones, but since the Options page is an admin page the filter will run when it pre-loads those form fields.</p>
<p>If there is interest, I can package up the above code into a legitimate plugin and submit it to the <a href="http://wordpress.org/extend/plugins/" title="WordPress &#8250; WordPress Plugins">WordPress plugins list</a>.
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://codex.wordpress.org/Administration_Over_SSL on November 8th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://codex.wordpress.org/General_Options_SubPanel on November 8th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://codex.wordpress.org/General_Options_SubPanel on November 8th, 2012.</p>
