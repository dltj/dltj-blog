---
layout: wordpress-import
status: published
published: true
title: 'JPEG2000 to Zoomify Code4Lib Lightning Talk Video Now Available'
modified: 2008-05-15T19:16:33+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 366
wordpress_url: https://dltj.org/?p=366
date: '2008-05-15 15:16:33 -0400'
date_gmt: '2008-05-15 19:16:33 -0400'
category: JPEG2000
categories:
- JPEG2000
tags:
- video
- jpeg2000
- java
- programming
- code4lib
- code4lib Conference 2008
- j2ktilerenderer
comments: []
---
<p>Thanks, Noel, and everyone else who made the <a href="http://archive.org/search.php?query=subject%3A%22code4lib%2C+2008%22" title="code4lib 2008 videos in Google Video">video editions</a> of <a href="http://code4lib.org/conference/2008/schedule" title="Code4Lib 2008 Meeting Schedule">Code4Lib 2008 presentations</a> possible.  I just had a chance to notice that the <a href="http://archive.org/details/code4lib.conf.2008.lightningtalk.JPEG2000toZoomifyShim" title="Code4Lib 2008 Lightning Talk: JPEG2000 to Zoomify Shim video">video</a> from my <a href="/article/introducing-j2ktilerenderer/">JPEG2000 to Zoomify Shim</a> lightning talk was online:</p>
<div style="width:400px;margin:0px auto;">
<embed id="VideoPlayback" style="width:400px;height:326px" flashvars="" src="http://video.google.com/googleplayer.swf?docid=-425356268115125043&hl=en" type="application/x-shockwave-flash"/>
</div>
<p>Some updates since the post and the presentation were first done.  The code that exists in the source code repository now was refactored to use <a href="http://code.google.com/p/jj2000/" title="JJ2000 Public Homepage">JJ2000</a> as part of the Sun <span class="removed_link" title="https://jai-imageio.dev.java.net/">ImageIO</span> package.  We were seeing non-threadsafe problems with <a href="http://www.kakadusoftware.com/" title="Kakadu JPEG 2000 SDK Home Page">Kakadu</a> and thought that using the multithreaded ImageIO package would help.  Unfortunately, even with extensive caching, it did not.  My next task is to bring Kakadu back into the picture using the threadsafe JNI implementation that is part of the <a href="http://java.net/projects/imageio-ext" title="Imageio-ext &amp;mdash; Java.net">ImageIO-ext</a> project to see if that helps.</p>
<p>Unfortunately, time ran out before this needed to go into initial production with the OhioLINK DRC roll-out, so it isn't in production.  The scheme shows promise, though, so I'm going to keep working with it...
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://jj2000.epfl.ch/ to http://code.google.com/p/jj2000/ on January 28th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to https://jai-imageio.dev.java.net/ on June 9th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from https://imageio-ext.dev.java.net/ to http://java.net/projects/imageio-ext on November 13th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://video.google.com/videosearch?q=code4lib+2008&sitesearch=&num=100 to http://archive.org/search.php?query=subject%3A%22code4lib%2C+2008%22 on August 22nd, 2013.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://video.google.com/videoplay?docid=-425356268115125043 to http://archive.org/details/code4lib.conf.2008.lightningtalk.JPEG2000toZoomifyShim on August 22nd, 2013.</p>
