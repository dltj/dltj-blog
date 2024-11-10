---
layout: wordpress-import
status: published
published: true
title: 'Thursday Threads: Web Time Travel, Fake Engine Noise, The Tech Behind Delivering Pictures of Behinds'
modified: 2015-02-05T11:21:11+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 24920
wordpress_url: http://dltj.org/?p=24920
date: '2015-02-05 06:21:11 -0500'
date_gmt: '2015-02-05 11:21:11 -0500'
category: Thursday Threads
categories:
- Thursday Threads
tags:
- web services
- Los Alamos National Laboratory
- Amazon Web Services
- memento
- automotive
comments:
- id: 676772
  author: hvdsomp
  author_email: twitter.90083746@example.com
  author_url: https://twitter.com/hvdsomp
  date: '2015-02-05 07:19:26 -0500'
  date_gmt: '2015-02-05 12:19:26 -0500'
  content: 'RT @DataG: New Thursday Threads blog post: Web Time Travel, Fake Engine
    Noise, The Tech Behind Delivering Pictures of Behinds http://t.co/i&hellip;'
---

<p>In this week's <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym> Thursday Threads</i>: the introduction of a web service that <a href="/article/thursday-threads-2015w05/#p24920-memento">points you to old copies of web pages</a>, dispelling <a href="/article/thursday-threads-2015w05/#p24920-fake-engine-noise">illusions of engine noise</a>, and admiring the <a href="/article/thursday-threads-2015w05/#p24920-aws">technical architecture of Amazon Web Services</a> that gives us <a href="/article/thursday-threads-2015w05/#p24920-web-scale">the power to witness Kim Kardashian&rsquo;s back side</a>.</p>
{{ thursday_threads_header() }}
<h2 id="p24920-memento">Introducing the Memento Web Time Travel Service</h2>
<blockquote><p>The <a href="http://timetravel.mementoweb.org/" title="Time Travel">Time Travel service</a> helps you find versions of a page that existed at some time in the past.  These prior versions of web pages are named Mementos. Mementos can be found in web archives or in systems that support versioning such as wikis and revision control systems. </p>
<p>When you enter the web address of a page and a time in the past, the Time Travel service tries to find a Memento for that page as it existed around the time of your choice. This will work for addresses of pages that currently exist on the web but also for those that have meanwhile vanished.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://timetravel.mementoweb.org/about/" title="About Time Travel">About the Time Travel Service</a>, Last updated: 19-Jan-2015</cite></div>
</blockquote>
<p>The folks at Los Alamos National Laboratory have been working on web-time-travel for years.  What started with <a href="http://www.mementoweb.org/demo/" title="Memento Demos">browser plugins</a> has now become a web service that can be used to find old copies of web pages found in caches throughout the world.  Thought the <a href="https://archive.org/web/">Internet Archive's Wayback Machine</a> was the only game in town?  Check out the <a href="http://timetravel.mementoweb.org/" title="Time Travel">Memento Time Travel service</a>.</p>
<h2 id="p24920-fake-engine-noise">America's best-selling cars and trucks are built on lies: The rise of fake engine noise</h2>
<blockquote><p>Stomp on the gas in a new Ford Mustang or F-150 and you&rsquo;ll hear a meaty, throaty rumble &mdash; the same style of roar that Americans have associated with auto power and performance for decades.</p>
<p>It&rsquo;s a sham. The engine growl in some of America&rsquo;s best-selling cars and trucks is actually a finely tuned bit of lip-syncing, boosted through special pipes or digitally faked altogether. And it&rsquo;s driving car enthusiasts insane.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://www.washingtonpost.com/business/economy/americas-best-selling-cars-and-trucks-are-built-on-lies-the-rise-of-fake-engine-noise/2015/01/21/6db09a10-a0ba-11e4-b146-577832eafcb4_story.html" title="America's best-selling cars and trucks are built on lies: The rise of fake engine noise">America's best-selling cars and trucks are built on lies: The rise of fake engine noise</a>, by <a href="http://www.washingtonpost.com/people/drew-harwell" title="Drew Harwell - The Washington Post">Drew Harwell</a>, The Washington Post, 21-Jan-2014</cite></div>
</blockquote>
<p>I knew they were adding "engine noise" to the all-electric Prius car because it was so quiet that it could startle people, but I didn't know it was happening to so-called "muscle cars".</p>
<h2 id="p24920-aws">A look at Amazon's world-class data-center ecosystem</h2>
<blockquote><p>Amazon VP and Distinguished Engineer James Hamilton shares what makes the company's armada of data centers run smoothly.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://www.techrepublic.com/article/a-look-at-amazons-world-class-data-center-ecosystem/" title="A look at Amazon's world-class data-center ecosystem | TechRepublic">A look at Amazon's world-class data-center ecosystem</a>, by Michael Kassner, TechRepublic, 8-Dec-2014</cite></div>
</blockquote>
<p>Among the geek community, there must be some awe at how Amazon seems to create infinitely big data centers that can be used for everything from powering Netflix to this humble blog.  Amazon is also notoriously secret about how it does things.  This article provides a glimpse into how Amazon Web Services achieves the scale that it does.</p>
<h2 id="p24920-web-scale">How PAPER Magazine's web engineers scaled their back-end for Kim Kardashian</h2>
<blockquote><p>On November 11th 2014, the art-and-nightlife magazine <em>PAPER</em> &ldquo;broke the Internet&rdquo; when it put a Jean-Paul Goude photograph of a well-oiled, mostly-nude Kim Kardashian on its cover and posted the same <a target="_blank" href="http://www.papermag.com/tag/Break%20The%20Internet#" title="PAPERMAG">nude photos of Kim Kardashian to its website</a> (NSFW). It linked together all of these things&mdash;and other articles, too&mdash;under the &ldquo;#breaktheinternet&rdquo; hashtag. There was one part of the Internet that PAPER <em>didn&rsquo;t</em> want to break: The part that was serving up millions of copies of Kardashian&rsquo;s nudes over the web.</p>
<p>Hosting that butt is an impressive feat. You can&rsquo;t just put Kim Kardashian nudes on the Internet and walk away &mdash;that would be like putting up a tent in the middle of a hurricane. Your web server would melt. You need to plan.</p>
<div style="text-align: right; width: 100%;"><cite>- <a href="https://medium.com/message/how-paper-magazines-web-engineers-scaled-kim-kardashians-back-end-sfw-6367f8d37688">How PAPER Magazine's web engineers scaled their back-end for Kim Kardashian (SFW)</a>, by <a href="https://medium.com/@ftrain">Paul Ford</a>, Medium, 21-Jan-2015</cite></div>
</blockquote>
<p>Speaking of how Amazon can seemingly scale to infinite levels, this article tells the story of how one online publisher ramped up their server capacity to meet the demands of users flocking to see Kim Kardashian's rear end.  (And who said the internet wasn't a valuable tool...)</p>
