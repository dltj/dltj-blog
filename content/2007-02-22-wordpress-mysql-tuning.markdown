---
layout: wordpress-import
status: published
published: true
title: 'WordPress/MySQL Tuning'
modified: 2007-02-22T18:56:45+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 188
wordpress_url: http://dltj.org/2007/02/wordpress-mysql-tuning/
date: '2007-02-22 13:56:45 -0500'
date_gmt: '2007-02-22 18:56:45 -0500'
category: Raw Technology
categories:
- Meta Category
- Raw Technology
tags:
- WordPress
- Gentoo
- system administration
- MySQL
comments:
- id: 12586
  author: ebyblog
  author_email: ''
  author_url: ''
  date: '2007-02-24 06:58:20 -0500'
  date_gmt: '2007-02-24 11:58:20 -0500'
  content: "<!--%kramer-pre%--> My Ma.gnolia Links  WordPress/MySQL Tuning in Disruptive
    Library Technology Jester  Tweaking some configs. Toothpaste For Dinner blog -
    Second Life  You could transform yourself into a giant penis for 200 fakebucks,
    but one could argue that you do that anyway by spending time in Second Life.<!--%kramer-post%-->"
- id: 12619
  author: 'Disruptive Library Technology Jester :: Killing Off Runaway Apache Processes'
  author_email: ''
  author_url: http://dltj.org/2007/02/die-apache-die/
  date: '2007-02-26 17:04:07 -0500'
  date_gmt: '2007-02-26 22:04:07 -0500'
  content: "[...] Well, something is still going wrong on dltj.org &mdash; despite
    previous performance tuning efforts, I&#8217;m still running into cases where
    machine performance grinds to a halt. In debugging it a bit further, I&#8217;ve
    found that the root cause is an apache httpd process which wants to consume nearly
    all of real memory which then causes the rest of the machine to thrash horribly.
    The problem is that I haven&#8217;t figured out what is causing that one thread
    to want to consume so much RAM &mdash; nothing unusual appears in either the access
    or the error logs and I haven&#8217;t figured out a way to debug a running apache
    thread. (Suggestions anyone?) [...]"
- id: 18283
  author: The Rule of Tech
  author_email: ''
  author_url: http://ruleoftech.wordpress.com/2007/06/17/tuning-apache-php-and-mysql/
  date: '2007-06-17 00:00:00 -0400'
  date_gmt: '2007-06-17 04:00:00 -0400'
  content: "<!--%kramer-pre%-->, second article concentrates on &ldquo;Optimizing
    Apache and PHP&rdquo; and final part is for &ldquo;Tuning your MySQL server&rdquo;.
    \ More practical example is on Disruptive Library Technology Jester -blog which
    writes about WordPress/MySQL Tuning on a Pentium III with 512M RAM box which runs
    a mail server (IMAP, ClamScan, Spam) and an Apache (WordPress and stuff).  Article
    contains setting up Alternative PHP Cache and some options for database tuning
    focusing on memory management. About MySQL<!--%kramer-post%-->"
- id: 29367
  author: se on kiva sillo &raquo; Blog Archive &raquo; Apachen ja MySQL:n optimointia
    v&auml;hille resursseille
  author_email: ''
  author_url: http://verteksi.net/soks/2007/07/08/apachen-ja-mysqln-optimointia-vahille-resursseille/
  date: '2008-01-15 03:30:50 -0500'
  date_gmt: '2008-01-15 07:30:50 -0500'
  content: |-
    <!--%kramer-ref-pre%-->[...] osa k&auml;sittelee Apachen asetuksia ja vastaavasti toinen osa
    keskittyy MySQL:n asetuksiin. My&ouml;s dltj-blogin vinkit ovat
    tarkistamisen [...]<!--%kramer-ref-post%-->
- id: 38465
  author: eli
  author_email: eli.g.anthony@gmail.com
  author_url: ''
  date: '2009-11-06 11:29:10 -0500'
  date_gmt: '2009-11-06 16:29:10 -0500'
  content: Thanks for the tips. I hadn't thought about managing this aspect of my
    wordpress install, so I'm sure this will help.
- id: 159955
  author: NaiTan  | ✔ Verified
  author_email: ''
  author_url: ''
  date: '2010-04-19 01:42:53 -0400'
  date_gmt: '2010-04-19 05:42:53 -0400'
  content: |-
    <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span class="topsy_trackback_content">WordPress/MySQL Tuning
    http://dltj.org/article/wordpress-mysql-tuning/</span></span>
- id: 173817
  author: MySQL Quick Review &mdash; Leocornus Plone XP
  author_email: ''
  author_url: http://plonexp.leocorn.com/xp/open-source-software-review/xps11
  date: '2011-10-04 10:04:53 -0400'
  date_gmt: '2011-10-04 14:04:53 -0400'
  content: "<!--%kramer-ref-pre%-->[...] WordPress MySQL Tunning:&nbsp;http://dltj.org/article/wordpress-mysql-tuning/
    [...]<!--%kramer-ref-post%-->"
- id: 290041
  author: NaiTan  |  Verified
  author_email: ''
  author_url: http://twitter.com/9tan/status/12430202649
  date: '2010-04-19 01:42:53 -0400'
  date_gmt: '2010-04-19 05:42:53 -0400'
  content: |-
    <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span class="topsy_trackback_content">WordPress/MySQL Tuning
    http://dltj.org/article/wordpress-mysql-tuning/</span></span>
- id: 654535
  author: David
  author_email: davidrapos@gmail.com
  author_url: ''
  date: '2014-01-09 05:58:25 -0500'
  date_gmt: '2014-01-09 10:58:25 -0500'
  content: "Nice Post.\r\nI got some good tips from http://www.techflirt.com/blog/wordpres/wordpress-performance-tuning.html
    also to improve overall wordpress performace"
---
<p><i>dltj.org</i> runs on a relatively tiny box &mdash; a Pentium III with 512MB of RAM.  I'm running a <a href="http://www.gentoo.org/" title="Gentoo Linux homepage">Gentoo</a> Linux distribution, so I actually have a prayer of getting useful work out of the machine (it server is actually a recycled Windows desktop), but the performance just wasn't great.  As it turns out, there are several easy things one can do to dramatically improve life.</p>
<h2>The Configuration</h2>
<p>The box is both a mail server (IMAP) and a WordPress server.  A rough eyeball at the process accounting on the server shows that it spends about 40% of the time doing mail (mostly taken up by Clamscan virus scanning and spam checking) and another 40% doing MySQL and web stuff.  Since there isn't much dynamic content on the box and nothing else using the database but WordPress, I'm fairly confident that blog traffic is almost all of that 40%.  I'm using MySQL 5.0.x, Apache 2.0.x and WordPress 2.0.x with about two dozen plugins.</p>
<h2>Taking PHP Up A Notch</h2>
<p>PHP is an interpreted programming language, meaning that each time a script runs it needs to be translated into something closer to machine code (called the 'opcode').  (As opposed to compiler languages like C and Java where you compile the source code into an executable in one step and then run that executable in a second step.)  For an application like WordPress, where the source code is not changing, this translation causes a lot of overhead.  Fortunately, there is a PHP plug-in called the <a href="http://php.net/apc" title="Alternative PHP Cache home page">Alternative PHP Cache</a> that will saved the translated opcode the first time the script runs and use it for subsequent invocations.  Getting this set up is pretty easy (these are Gentoo-specific commands, your Linux distribution will vary and I am glossing over a number of distribution-specific details like how to install packages and where the configuration files will reside):</p>
<ol>
<li><code>emerge -aDNtuv pecl-apc</code> will download and install PHP APC and its dependencies (yep -- that easy...I <em>love</em> Gentoo)</li>
<li>Change the configuration defaults in <code>/etc/php/apache2-php5/ext/apc.ini</code>.  I've found that one shared segment of 20MB is enough, so I set <code>apc.shm_size="20"</code>.  The rest of the settings are as they came in the distribution.</li>
<li>Restart your web server:  <code>/etc/init.d/apache2 restart</code></li>
</ol>
<p>APC comes with a nifty PHP page that will give you cache statistics and details.  If you copy <code>/usr/share/php5/apc/apc.php</code> into your 'htdocs' somewhere and execute that page from a browser, you'll see what I mean.  (This is how I learned that 20MB of opcode cache space was fine for my application.)</p>
<h2>Kicking MySQL Into Gear</h2>
<p>Database tuning focuses a great deal on memory management.  Your RAM will always be an order of magnitude faster than reading blocks off a disk.  RAM, of course, costs more per MB than disk, though, so you have to select memory management strategies carefully.  WordPress is, of course, a read-intensive operation.  In other words, the majority of SQL statements are SELECTs rather than INSERTs, UPDATEs, or DELETEs.  With that in mind, we tune MySQL with a read-intensive strategy.  I found some of the best guidance in <a href="http://www.mysqlperformanceblog.com/2006/09/29/what-to-tune-in-mysql-server-after-installation/" title="What to tune in MySQL Server after installation from MySQL Performance Blog"> Peter Zaitsev's "What to tune in MySQL Server after installation"</a> and the ez.no documentation on <a href="http://ez.no/community/articles/tuning_mysql_for_ez_publish/optimizing_for_read_performance">Optimizing for read performance</a>.</p>
<p>The changes I made to my MySQL configuration file, in the <code>[mysqld]</code> section are:</p>
```
key_buffer = 6M ; (Actually, a decrease from the default since I didn't seem to need as much)
table_cache = 512
max_connections = 25
thread_cache = 16
query_cache_type = 1
query_cache_limit = 1M
query_cache_size = 20M
```
<p>The 20MB query cache limit seems to be just about the right size for me.  I seem to get very close to the edge of that buffer, but never seem to go over.</p>
<h2>Finishing Up with a WordPress Plug-in</h2>
<p>One more thing is needed to make this all come together: Mark Jaquith's <a href="http://txfx.net/code/wordpress/post-query-accelerator/" title="Post Query Accelerator WordPress Plug-in Homepage">Post Query Accelerator</a>.  As Mark points out on his blog, WordPress "always ask[s] for posts with post_date_gmt <= '$now' where $now is set to the current time, to prevent posts in the future from showing up."  If one turns on cache querying as described above, the "problem with $now is that it changes [with each query], so the query is never exactly the same again and the cache doesn&rsquo;t help."  Mark's plug-in "freezes" the value of $now to 15 minute increments or to whenever a post is added/updated, which ever comes first.  That makes the query cache useful again and all is well.  </p>
<p>Simply download the plug-in from Mark's page and enable it in WordPress.  Note that this plug-in is not needed for WordPress 2.1 and higher as the core developers have solved the "$now" problem with the "future" post status.</p>
