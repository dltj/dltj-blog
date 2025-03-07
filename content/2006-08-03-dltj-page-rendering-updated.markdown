---
layout: wordpress-import
status: published
published: true
title: 'DLTJ page rendering updated (sorry Bloglines users)'
modified: 2006-08-03T16:20:56+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 99
wordpress_url: http://dltj.org/2006/08/dltj-page-rendering-updated/
date: '2006-08-03 12:20:56 -0400'
date_gmt: '2006-08-03 17:20:56 -0400'
category: Meta Category
categories:
- Meta Category
tags:
- ultimatetagwarrior
- WordPress
- Extended Live Archive
comments:
- id: 2608
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-08-03 20:47:25 -0400'
  date_gmt: '2006-08-04 01:47:25 -0400'
  content: "Okay -- well, that didn't go nearly as well as planned.  Lots of CSS mucking
    up that I caused when trying to get the XHTML and the RSS feeds to validate.  Oh,
    they validate fine alright, but now look horrible in MSIE.  (And not much better
    in Firefox.)\r\n\r\nI had to turn of the Extended Live Archive home page and am
    debating whether to revert the rest of the changes or press ahead with a new theme.
    \ At this rate it'll probably be the weekend before anything happens..."
- id: 2725
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-08-08 08:52:48 -0400'
  date_gmt: '2006-08-08 13:52:48 -0400'
  content: 'This has taken longer than I thought to accomplish.  Over the weekend
    I started the work of replacing DLTJ''s ''elegantblue''-based theme with Barthelme.  The
    sidebar, index, and single-post pages are pretty much done, but there is work
    yet to do on the comments template and print style sheets.  If you''d like, you
    can see the work in progress by using this URL to set a cookie in your browser
    to switch to the new theme:  <a href="/index.php?wptheme=Barthelme"
    rel="nofollow">http://dltj.org/index.php?wptheme=Barthelme</a>.  Hopefully in
    a few more evenings, the final version will be ready to go live for everyone.  (And
    yes, Bloglines users, the content of the RSS feed will probably change <i>again.)</i>'
- id: 291679
  author: Peter Murray
  author_email: ''
  author_url: http://twitter.com/datag/status/238418095058862080
  date: '2012-08-22 23:31:18 -0400'
  date_gmt: '2012-08-23 03:31:18 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">DLTJ page rendering updated (sorry Bloglines users)
    http://t.co/jyuLvAZE</span></span>
---
<p>Overnight I made several changes to the layout and rendering of pages on DLTJ -- both in its web presentation and in its RSS presentation.  The changes were really driven by the fact that my tags were not getting picked up in Technorati because the Wordpress <a href="http://www.neato.co.nz/ultimate-tag-warrior">UltimateTagWarrior</a> plugin was not including them as expected in the RSS feed (although it was in the web presentation, which was throwing me off).  And I've heard from some (hi, Karen!) that when I make changes to the RSS rendering that Bloglines makes it look like <em>all</em> of the posts have been updated.  This isn't the case -- just the rendering of them has changed.  You'd think that Bloglines would read the ">pubdate<" tag and figure this out for itself, but it doesn't.  So to all of the Bloglines users, you can ignore all of the "new" posts from DLTJ except for this one -- the content has not changed in those earlier posts.</p>
<p>Knowing that changes were to be made, I also went through a whole bunch of desired changes to the layout of DLTJ that had stacked up as, individually, were not important enough to do.  So some other things that you'll see:</p>
<dl>
<dt>Clearer "Tags" heading<img id="image100" src="/assets/images/2006/08/change_01.gif" alt="Tag table with explanation of graphics" style="float: right; border: 1px solid silver; margin-left: 1em; margin-bottom: 1em;" /></dt>
<dd>I wasn't really pleased with how UltimateTagWarrior was displaying links to the various social tagging services.  Which is to say, if you didn't know what the little 16x16 graphic is, having them strung across the page isn't really going to help you.  So I put them into a table with a header that explains what each graphic means.    I'm not entirely happy with this layout either, but it will stay for a while until I think-of/run-across something better.
</dd>
<dt>No more chronological home page</dt>
<dd>
I've got to agree with Jarrod Trainque in <span class="removed_link" title="http://m.iscellaneo.us/index.php/2005/08/15/turning-wordpress-into-a-tag-based-blogging-application/">his analysis of the typical blog homepage</span>:  "Like most bloggers, I don&rsquo;t get a ton of front-page traffic. My visitor logs show that most of my visitors come via google, and land on a specific page....  The most recent articles appear on the front page, with the newest posts at the top....  How often do you only know when something was posted, and use that as the primary deciding factor when navigating within a site? Rarely, I bet. It&rsquo;s just not useful information to anyone but the weblog author."   So the home page of DLTJ now embeds the <a href="http://www.sonsofskadi.net/extended-live-archive/" title="http://www.sonsofskadi.net/extended-live-archive/">Extended Live Archive</a> on the <a href="/">home page</a> so that if you start from the home page you can more easily find content that may interest you.  (Including chronological, if that is your choice.)
</dd>
<dt>The Funky Feedburner Links Are Gone</dt>
<dd>
When you turn on Feedburner's per-item tracking the links it provides turn out to be really long and ugly.  So long and ugly that I care less about any kind of statistics Feedburner might generate than annoying the rest of you who might try to copy down the URLs and pass them around.  So URLs to all of the posts have changed.  I haven't figured out yet of the old ones will still work.  Probably not.  Sorry 'bout that.
</dd>
</dl>
<p>There were some other tweaks, including a new 'favicon.ico' for those that bookmark DLTJ pages.  If you notice anything strange that seems unresolved, please <a href="/contact">let me know</a>.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://m.iscellaneo.us/index.php/2005/08/15/turning-wordpress-into-a-tag-based-blogging-application/ on August 22nd, 2012.</p>
