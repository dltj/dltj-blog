---
layout: wordpress-import
status: published
published: true
title: 'Using Twitter For Service Outage Awareness'
modified: 2010-09-01T00:20:32+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1661
wordpress_url: http://dltj.org/?p=1661
date: '2010-08-31 20:20:32 -0400'
date_gmt: '2010-09-01 00:20:32 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Twitter
- javascript
- dynamic HTML
comments:
- id: 163038
  author: Jill Hurst-Wahl
  author_email: ''
  author_url: http://twitter.com/jill_hw/status/25073161577
  date: '2010-09-21 00:40:10 -0400'
  date_gmt: '2010-09-21 04:40:10 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Using Twitter For Service Outage Awareness (in
    libraries), http://dltj.org/article/twitter-for-outages/ Interesting implementation</span></span>
- id: 163039
  author: Outage Tracker
  author_email: ''
  author_url: http://twitter.com/outagetracker/status/23977924766
  date: '2010-09-09 04:03:54 -0400'
  date_gmt: '2010-09-09 08:03:54 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT @aarontay Using Twitter For Service Outage
    Awareness http://bit.ly/cfwAmw</span></span>
- id: 163040
  author: Aaron Tay
  author_email: ''
  author_url: http://twitter.com/aarontay/status/23975795402
  date: '2010-09-09 03:34:16 -0400'
  date_gmt: '2010-09-09 07:34:16 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Using Twitter For Service Outage Awareness http://bit.ly/cfwAmw</span></span>
- id: 163041
  author: Fabrizio Tinti
  author_email: ''
  author_url: http://twitter.com/pintini/status/22783199755
  date: '2010-09-02 08:58:34 -0400'
  date_gmt: '2010-09-02 12:58:34 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Twitter dans l&#39;OPAC (et messages "de service")...
    http://bit.ly/dzL9pl</span></span>
- id: 163042
  author: lioneldujol
  author_email: ''
  author_url: http://twitter.com/lioneldujol/status/22691913858
  date: '2010-09-01 09:04:41 -0400'
  date_gmt: '2010-09-01 13:04:41 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">[veille] Using Twitter For Service Outage Awareness
    http://dlvr.it/4Xdz9</span></span>
- id: 163043
  author: Outage Tracker
  author_email: ''
  author_url: http://twitter.com/outagetracker/status/22665627232
  date: '2010-09-01 01:07:04 -0400'
  date_gmt: '2010-09-01 05:07:04 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT @infopeep Murray, Peter: Using Twitter For
    Service Outage Awareness http://bit.ly/c1HpQn</span></span>'
- id: 163044
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/22664592806
  date: '2010-09-01 00:53:38 -0400'
  date_gmt: '2010-09-01 04:53:38 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Using Twitter For Service Outage
    Awareness http://bit.ly/c1HpQn</span></span>'
---
<p>Emily Clasper of the Suffolk County Library <span class="removed_link" title="http://libraryrevolution.com/?p=202">posted about some work she had done to embed status messages in the catalog using Twitter</span>.  This sounded like a really great idea because it is an out-of-band (e.g. something that doesn't rely on OhioLINK infrastructure for reporting downtimes) way to get messages to member staff and users.  But I didn't get a chance to work on my implementation for a while, so for over a year ideas have bubbled around in my head about ways to apply this technique and improve on it.  I finally carved out some spare time to actually work on it, and came up with my take on the concept.  The result is the OhioLINK Status-Via-Twitter service.{{ image(
    div_float="right",
    width="300",
    caption="A demo of the TwitterJS implementation using a copy of the OhioLINK homepage.",
    alt="Demo of TwitterJS",
    localsrc="/assets/images/2010/08/ohiolink_homepage_with_message-300x242.png",
    localhref="/assets/images/2010/08/ohiolink_homepage_with_message.png") }}
</p>
<p>In Emily's approach to putting messages on public pages, the staff would first post a message to the public status Twitter account which would then be turned into a block of HTML inserted into the public catalog page via JavaScript.  The JavaScript would query the feed for the public status Twitter account and insert any tweets found there into the page.  When the information in the tweet is no longer needed, the library staff would delete the tweet.</p>
<p>In my conceptualization of this service, there would be individuals or agents other than the catalog JavaScript code that would be looking to the tweet stream for updates on services.  Those individuals and agents won't know when a tweet is deleted, so an "all-clear" message needs to be posted to the tweet stream for those consumers.  And, of course, we wouldn't want an "all-clear" tweet to be posted <i>ad infinitum</i> (or at least until the next service message) on public web pages.</p>
<p>I would also like to include the tweeted service messages on all pages on our site, not just the homepage.  But if we do that, then every page hit for one of our users would hit the Twitter API to get the tweets from the public status Twitter account...with possible privacy and capacity overloading concerns.  So there would need to be a way to cache messages from Twitter for a period of time.</p>
<p>In bulleted-point form, what I was looking for was:</p>
<ul>
<li>A bit of JavaScript that would dynamically insert HTML into a
<div> tag that contains the text of tweets.</li>
<li>The script would not display tweets that contain a set phrase (e.g. "returned to normal") or were older than a pre-defined period.</li>
<li>The script would cache messages as cookies and only read new messages from Twitter after a pre-defined period of time.</li>
<li>The script had to be compact and self-contained (e.g. not rely on external JavaScript libraries) for speed and simplicity.</li>
</ul>
<h2>The Implementation</h2>
<p>What I ended up doing was <a href="http://github.com/dltj/twitterjs" title="dltj's twitterjs at master - GitHub">adapting</a> JavaScript code by <a href="http://remysharp.com/2007/05/18/add-twitter-to-your-blog-step-by-step/" title="Add Twitter to your blog (step-by-step)">Remy Sharp</a> from his <a href="http://code.google.com/p/twitterjs/" title="twitterjs - Project Hosting on Google Code">twitterjs</a> project.  Modifications include the ability to pass a parameter to limit the number of hours a tweet will be shown before it is ignored (the <strong>ignoreOlderThan</strong> parameter) and to truncate the display of tweets if a particular string is used (the <strong>stopIfSeen</strong> parameter) as well as the caching function.  The code is posted on GitHub at <a href="http://github.com/dltj/twitterjs" title="dltj's twitterjs at master - GitHub">http://github.com/dltj/twitterjs</a>.</p>
<p>The <a href="http://github.com/dltj/twitterjs/blob/OhioLINK-Prod/src/twitter.js#L472" title="Line 472 of twitter.js on the OhioLINK-Prod branch of twitterjs">bottom of 'twitter.js' in the <em>OhioLINK-Prod</em> branch</a> of the twitterjs project has an example of how to configure the JavaScript function.  It looks like this:</p>
```JavaScript
getTwitters('ohiolinkstatus', {       // <div> to insert text
  id: 'OhioLINKstatus',               // Twitter id
  count: 20,                          // Maximum number of tweets to show
  ignoreReplies: true,                // Ignore @-replies (true or false)
  ignoreOlderThan: 36*60*60,          // Ignore tweets older than this (in minutes)
  stopIfSeen: 'returned to normal',   // Stop display tweets if this text is in tweet
  cookiePrefix: 'TwitterJS',          // Preface cookies with this prefix
  cookieDomain: 'dltj.org',           // Cookies stored for this domain
  cookieRefresh: 5                    // How often to check tweets (in minutes)
});</div>
```
<p>To make this work on your pages, you'd need to follow these steps:</p>
<ol>
<li>Download the <a href="http://github.com/dltj/twitterjs/raw/master/src/twitter.js" title="twitter.js">twitter.js file</a> from GitHub.  At the end of this file, add the configuration to match your needs.  At a minimum, change <code>cookieDomain</code> to match the domain of your website, or this won't work.  You probably also want to change the <code>id</code> unless you want to monitor OhioLINK services.  ((Note that at the time this is being posted, OhioLINK is not using this in production so don't rely on this Twitter ID for actual outage messages.))</li>
<li>Download the <a href="http://github.com/dltj/twitterjs/raw/master/test/twitter.css" title="twitter.css">CSS file for twitterjs</a> and modify to your tastes.</li>
<li>(Optional Step) Run your JavaScript through <a href="http://jscompress.com/" title="Minify Javascript Online / Online JavaScript Packer">JSMinify</a> to reduce its size to increase website performance.  Do <a href="http://refresh-sf.com/yui/" title="Online YUI Compressor">the same</a> for the CSS file.</li>
<li>Upload the JavaScript and CSS files to your website.</li>
<li>Add these lines to the <head> section of any page you want to use this:
```html
<link rel="stylesheet" href="http://your.host.name/your.directory/twitter.css" type="text/css" media="screen" charset="utf-8" />
<script src="http://your.host.name/your.directory/twitter.js" type="text/javascript" charset="utf-8"></script>
```
</li>
<li>Add this line to the <body> section of the document where you want the tweets to appear:
```html
<div class="twitters" id="ohiolinkstatus"></div>
```
<p>  <em>Be sure</em> the <code>id</code> attribute value matches the first parameter of the <code>getTwitters()</code> function call in the first step.</li>
</ol>
<p><code>getTwitters()</code> will run the main body of code after the page is finished loading.  If it finds a twitterjs cookie for the current domain, it replaces whatever is inside the
<div> with that information.  If it doesn't find a twitterjs cookie or the cookie has expired, it pulls the feed of tweets, parses them, stashes the value into a domain cookie (even if the value is the empty string), and replaces whatever is inside the
<div>.</p>
<p>For extra credit, note that you can do a lot of styling with the CSS file.  For instance, the version of this I'm demoing at OhioLINK has an GIF encoded as Base64 data in the background of the unordered list of tweets.  (We do the Base64 encoding like this to avoid the overhead of another round-trip back to the webserver to get the small graphic.)  You can create your own graphic, translate it using <a href="http://www.google.com/search?q=base64+encoder" title="base64 encoder - Google Search">a Base64 encoder</a>, and replace that value.</p>
<p>If you end up using this, please let me know in the comments.
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://libraryrevolution.com/?p=202 on January 8th, 2013.</p>
