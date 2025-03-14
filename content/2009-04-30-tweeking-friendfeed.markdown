---
layout: wordpress-import
status: published
published: true
title: 'Tweaking the New FriendFeed Interface'
modified: 2009-04-30T20:15:59+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 912
wordpress_url: http://dltj.org/?p=912
date: '2009-04-30 16:15:59 -0400'
date_gmt: '2009-04-30 20:15:59 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Firefox
- usability
- CSS
- greasemonkey
- FriendFeed
comments:
- id: 162611
  author: yamasas
  author_email: ''
  author_url: http://twitter.com/yamasas/status/1678381826
  date: '2009-05-02 13:31:23 -0400'
  date_gmt: '2009-05-02 17:31:23 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">[useful] Tweaking the New FriendFeed Interface
    | Disruptive Library Technology Jester http://tinyurl.com/cxzgpw</span></span>
- id: 162612
  author: Mike Chelen
  author_email: ''
  author_url: http://twitter.com/mikechelen/status/1673640362
  date: '2009-05-01 22:36:29 -0400'
  date_gmt: '2009-05-02 02:36:29 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT @DataG New blog post: Tweaking the New FriendFeed
    Interface http://tinyurl.com/cxzgpw</span></span>'
- id: 162614
  author: Eric Schnell
  author_email: ''
  author_url: http://twitter.com/ericschnell/status/1664852176
  date: '2009-05-01 01:10:12 -0400'
  date_gmt: '2009-05-01 05:10:12 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">blogroll: Tweaking the New FriendFeed Interface
    http://tinyurl.com/cxzgpw</span></span>'
- id: 162615
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/1662700647
  date: '2009-04-30 20:49:58 -0400'
  date_gmt: '2009-05-01 00:49:58 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Tweaking the New FriendFeed Interface
    http://snipurl.com/h3yyq</span></span>'
- id: 162616
  author: Peter Murray
  author_email: ''
  author_url: http://twitter.com/datag/status/1662404389
  date: '2009-04-30 20:16:04 -0400'
  date_gmt: '2009-05-01 00:16:04 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">New blog post: Tweaking the New FriendFeed Interface
    http://tinyurl.com/cxzgpw</span></span>'
---
<p><a href="http://friendfeed.com/" title="FriendFeed homepage">FriendFeed</a> went live yesterday with <a href="http://blog.friendfeed.com/2009/04/whole-new-friendfeed.html" title="Announcement of A whole new FriendFeed">changes to the user interface and back-end systems</a>.  The changes were moderately positive, taken as a whole, but there are aspects of the new user interface that I don't like -- the color scheme, the removal of the service icons, and the (over)-use of whitespace.  Fortunately, with Firefox plus a few extensions as my primary browser, I'm able to tweak the interface to be closer to my liking.  If your tastes resemble mine, I both feel sorry for you and want to help you improve your view of FriendFeed.<br />
<!--more--><br />
{{ image(
    div_float="right",
    width="300",
    caption="FriendFeed interface before changes via Greasemonkey and Stylish",
    alt="FriendFeed interface before Greasemonkey/Stylish changes",
    localsrc="/assets/images/2009/04/friendfeed-before-300x191.png",
    localhref="/assets/images/2009/04/friendfeed-before.png") }}
<br />
{{ image(
    div_float="right",
    width="300",
    caption="FriendFeed interface after changes via Greasemonkey and Stylish",
    alt="FriendFeed anterface after Greasemonkey/Stylish changes",
    localsrc="/assets/images/2009/04/friendfeed-after-300x186.png",
    localhref="/assets/images/2009/04/friendfeed-after.png") }}
</p>
<p>The primary tool to help with the user interface changes, in addition to using <a href="http://www.mozilla.com/firefox/" title="Get the Firefox Browser">Firefox</a>, is the <a href="http://www.greasespot.net/" title="Greasemonkey homepage">Greasemonkey</a> extension.  After <a href="https://addons.mozilla.org/en-US/firefox/addon/748">installing this extension</a>, <a href="http://web.archive.org/web/20090430204322/http://userscripts.org/about/installing" title="Installing Greasemonkey Scripts">you can use "scripts"</a> to tell the browser to change the HTML markup of any arbitrary web page as it is being loaded.  A secondary tool is the <a href="https://addons.mozilla.org/firefox/addon/2108">Stylish extension</a>.  Stylish does to a pages CSS code what Greasemonkey does to the HTML -- it <a href="http://userstyles.org/help" title="User styles explained | userstyles.org">overrides the page author's styles and substitutes your own</a>.  Stylish is actually optional because you can use Greasemonkey to load a form of Stylish scripts to accomplish the same outcome.  (<a href="http://web.archive.org/web/20090530/http://www.opera.com/browser/tutorials/userjs/examples/#greasemonkey" title="Opera: Tutorial - User Javascript">Some</a> Greasemonkey scripts also <a href="http://web.archive.org/web/20090530/http://www.opera.com/browser/tutorials/userjs/" title="Opera: Tutorial - User javascript">work</a> in the <a href="http://www.opera.com/browser/" title="Opera Web Browser">Opera browser</a>; I haven't tried the scripts listed here, so your mileage may vary.)</p>
<p>The first thing we want to do is bring back the service icons.  These are the 16x16 pixel graphics that show the source of the entry in the FriendFeed stream.  I haven't heard a good explanation from the FriendFeed developers as to why they took this out, but I find it to be a key factor in how I scan through the FriendFeed stream.  Fortunately, <a href="http://chrispeoples.com/" title="Chris Peoples' homepage">Chris Peoples</a> wrote a <a href="http://web.archive.org/web/20090430204322/http://userscripts.org/scripts/show/46187" title="FriendFeed Service Icons for Greasemonkey">Greasemonkey script</a> to bring them back.  Simply <a href="http://web.archive.org/web/20090430204322/http://userscripts.org/scripts/source/46187.user.js" title="Greasemonkey script">install the script</a> and reload the FriendFeed page; the service icons will be back for public entries.  (As Chris notes, it doesn't work on private feed entries.)</p>
<p>The second thing we want to do is clean up the color scheme:  remove the grey background, de-emphasis the functional areas on the right, and rebalance the font sizes.  AJ Batac wrote a <a href="http://userstyles.org/styles/17424" title="Cleaner FriendFeed">Stylish script</a> that does that and more.  You can load this script into Stylish or apply the Greasemonkey version; as far as I know, they are equivalent.  In addition to the color schemes, this script adds new functionality:  highlighting friend comments in a light yellow background and highlighting your comments with a light blue background.  The latter is particularly useful for rescanning a conversation where you have made a comment; the light blue background tells you exactly where your comment is in the conversation and the new comments that followed.</p>
<p>There is a third script that removes the large avatars that came with the new interface design.  Personally, the avatar graphics don't bother me, but if you want to remove those, <a href="http://userstyles.org/styles/16763" title="Remove avatars from Friendfeed">you have that option</a>, too.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.opera.com/browser/tutorials/userjs/examples/#greasemonkey to http://web.archive.org/web/20090530/http://www.opera.com/browser/tutorials/userjs/examples/#greasemonkey on August 22nd, 2013.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.opera.com/browser/tutorials/userjs/ to http://web.archive.org/web/20090530/http://www.opera.com/browser/tutorials/userjs/ on August 22nd, 2013.</p>
