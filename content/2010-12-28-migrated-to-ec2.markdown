---
layout: wordpress-import
status: published
published: true
title: 'DLTJ In a State of Flux'
modified: 2010-12-28T16:45:54+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1927
wordpress_url: http://50.16.230.151/?p=1927
date: '2010-12-28 11:45:54 -0500'
date_gmt: '2010-12-28 16:45:54 -0500'
category: Meta Category
categories:
- Meta Category
tags:
- Gentoo
- Amazon EC2
comments:
- id: 108852
  author: Peter Murray
  author_email: peter@PandC.org
  author_url: http://dltj.org/
  date: '2010-12-28 12:17:06 -0500'
  date_gmt: '2010-12-28 17:17:06 -0500'
  content: This is a test message.
- id: 108857
  author: TDP
  author_email: timothyparker@gmail.com
  author_url: ''
  date: '2010-12-28 12:41:34 -0500'
  date_gmt: '2010-12-28 17:41:34 -0500'
  content: "\"If this goes well, perhaps I&rsquo;ll leave DLTJ in the cloud&hellip;\"\r\n\r\nConsidering
    the chaos that has surrounded Gentoo in recent years, that might be the best idea."
- id: 108868
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-12-28 14:53:41 -0500'
  date_gmt: '2010-12-28 19:53:41 -0500'
  content: "I find that running a Gentoo system requires a unique state of mind, and
    for the most part that state of mind jells nicely with my roots in System-V and
    early BSD systems. For me, the Gentoo portage system has solidified nicely. In
    the nine year history of the old box, though, is an X11 desktop usage as well
    as various experiments that left lots of crusty old installed packages. (Some
    times a portage update still wants to bring in the entire X11 subsystem.)\n\nThe
    question of what to use on the rebuilt server looms large. Maybe Ubuntu this time?
    Or a straight Debian? Or Fedora or centos?\n\nWhat it might come down to is an
    economic calculation of cost-of-the-cloud versus cost of the co-location facility.
    Time (roughly a month) will tell on that question. "
- id: 109139
  author: Ryan Collins
  author_email: blogs2009@ryancollins.org
  author_url: http://ryancollins.org/
  date: '2010-12-30 15:18:11 -0500'
  date_gmt: '2010-12-30 20:18:11 -0500'
  content: "I've been playing around with a VPS (hosted by chicagovps.net). I get
    512MB instance with 20GB of space and 1TB of transfer. They had a black Friday
    special of $60 for a year, so I couldn't pass that up. I don't know how reliable
    they will be though. Right now I use it as a test bed for little projects (like
    capturing all the tweets from the people I follow) and a VPN using pptp so I can
    use my laptop or iPod Touch securely at public wifi hot spots.\r\n\r\nMy regular
    blog is hosted at Dreamhost. No real complaints, and I've been with them for several
    years.\r\n\r\nI've played around with EC2, but it costs too much for me to run
    an instance 24/7. You probably got in on the free offer for a year?\r\n\r\nI'm
    a big Ubuntu fan, running 10.04 LTS on my VPS. Pretty much headache free to keep
    up."
- id: 109155
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-12-30 17:09:11 -0500'
  date_gmt: '2010-12-30 22:09:11 -0500'
  content: "Thanks for the tips, Ryan.  I did get in on the free year from Amazon,
    but I'm not counting on that in my calculations.  If I reserve a micro instance
    for a year, I think I <a href=\"http://calculator.s3.amazonaws.com/calc5.html?key=calc-85BD1BF9-454C-4224-93DD-957ECA5B273C\"
    rel=\"nofollow\">would pay about $151.44</a> ($54 on-time payment to reserve the
    instance plus $97.44 in monthly usage charges).  That is for 613MB of RAM and
    10GB disk with bursts of 2 <a href=\"http://aws.amazon.com/ec2/faqs/#What_is_an_EC2_Compute_Unit_and_why_did_you_introduce_it\"
    rel=\"nofollow\">ECUs</a>.  I figure as long as I'm on the EC2 instance that I'll
    experiment with offloading static files to the CloudFront distribution network.
    \ That is how <i><acronym title=\"Disruptive Library Technology Jester\">DLTJ</acronym></i>
    is set up now, and I do notice that page load performance is significantly zippier.\r\n\r\nNeedless
    to say, so far I've found Amazon EC2 is a much better way to run a blog that I
    have full control over when compared to renting the co-location space and amortizing
    the cost of the server hardware.\r\n\r\nI've learned a few things along the way
    to moving this blog to EC2.  Hopefully I'll have time at some point to write up
    a report of its configuration and my findings."
- id: 167408
  author: Amy Kirchhoff
  author_email: ''
  author_url: http://twitter.com/lifewiththree/status/19812676989358081
  date: '2010-12-28 17:51:24 -0500'
  date_gmt: '2010-12-28 22:51:24 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">DLTJ In a State of Flux: DLTJ is in a bit of flux
    now. After updating some underlying&hellip; http://goo.gl/fb/DpSIf</span></span>'
- id: 167409
  author: Library Feed
  author_email: ''
  author_url: http://twitter.com/libraryfeed/status/19809595438407680
  date: '2010-12-28 17:39:10 -0500'
  date_gmt: '2010-12-28 22:39:10 -0500'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">DLTJ In a State of Flux http://bit.ly/hBYsxF</span></span>
---
<p><i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym></i> is in a bit of flux now.  After updating some underlying packages on my 9-year-old <a href="http://www.gentoo.org/" title="Gentoo Linux -- Gentoo Linux News">Gentoo</a>-based personal server, I'm finding that I can't start the web server process without the 1-minute load average climbing to roughly 60 in the span of about 5 minutes.  (Translation: the machine is working very hard but getting nowhere fast.)  Increasingly, the server has also been hard to update -- lots of strange errors, etc. -- so after 9 years, it is clearly time to rebuild it.  In the interim, I'm in the process of moving the blog over to an <a href="http://aws.amazon.com/ec2/" title="Amazon Elastic Compute Cloud (Amazon EC2)">Amazon EC2</a> cloud computing instance.  If you see this post, you are reading it on that virtual server.  The DNS entries should catch up with the migration in a couple of hours.</p>
<p>Because this wasn't necessarily planned, you'll see things change a lot.  I'm still working on theme changes, for instance.  But all the content is migrated over.  If this goes well, perhaps I'll leave <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym></i> in the cloud...</p>
