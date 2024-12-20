---
layout: wordpress-import
status: published
published: true
title: 'Preserving Digital Video'
modified: 2008-04-08T20:22:14+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 348
wordpress_url: https://dltj.org/?p=348
date: '2008-04-08 16:22:14 -0400'
date_gmt: '2008-04-08 20:22:14 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- standards
- video
- accessibility
- preservation
- digitization
comments:
- id: 60219
  author: Michal
  author_email: michelin106@seznam.cz
  author_url: ''
  date: '2010-03-17 09:20:32 -0400'
  date_gmt: '2010-03-17 13:20:32 -0400'
  content: Hi, I found some other informations about <a href="http://www.file-extensions.org/scc-file-extension-scenarist-closed-caption-file"
    rel="nofollow">SCC</a> file format at file-extensions.org. Nice day.
- id: 60227
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-03-17 11:39:47 -0400'
  date_gmt: '2010-03-17 15:39:47 -0400'
  content: Thank you for the link to additional details, Michal.
- id: 163691
  author: Dennis Moser
  author_email: ''
  author_url: http://twitter.com/aldusm/status/69157161917353984
  date: '2011-05-13 21:48:46 -0400'
  date_gmt: '2011-05-14 01:48:46 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT @blefurgy: Preserving Digital Video http://ow.ly/4Ua8j
    @DataG</span></span>'
- id: 163692
  author: bill lefurgy
  author_email: ''
  author_url: http://twitter.com/blefurgy/status/69127374779842560
  date: '2011-05-13 19:50:25 -0400'
  date_gmt: '2011-05-13 23:50:25 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Preserving Digital Video http://ow.ly/4Ua8j @DataG</span></span>
---
<p>My place of work is looking to acquire educational videos in a digital form with an eye towards long-term preservation.  At this point we receive a physical form (preferably DVD, but sometimes VHS) and digitize it to a very lossy access format (RealMedia, in this case).  With this change, we would get a preservation-worthy digital copy from the producer/distributor and forego the physical version.</p>
<p>There is quite a lot written on preserving video, but I wanted to distill the requirements down into statements that vendors could reasonably provide today.  I think these are pretty sound requirements, but I'm looking for feedback.  In particular, I'm not quite sure how to handle the transfer of closed caption text from the publisher/distributor; suggestions are welcome.<br />
<!--more--><br />
[Jester's note:  I just realized that an earlier version of this posting went out to the net about two hours before this "final" version.  Sorry about publishing the work-in-progress early; I must have hit the wrong button in the new version of WordPress...]</p>
<h2>File Formats</h2>
<p>Some of the clearest guidance on file formats comes from this short excerpt from the Moving Image section of the <a href="http://www.ahds.ac.uk/" title="The Arts and Humanities Data Service homepage">U.K. Arts and Humanities Data Service</a> <a href="http://www.ahds.ac.uk/preservation/ahds-preservation-documents.htm" title="AHDS Repository Policies and Procedures">Preservation Handbook</a>:</p>
<blockquote><p>Guidance on the preservation of digital video should, by necessity, change over time. [...] The MPEG-2 and MPEG-4 formats are better suited to high-quality digital video. MPEG-2 is better known for its use as a format for DVD-Video, which encourages confidence when considering the likelihood that the format will be readable in the long-term. The format has an average transfer rate of 2-5 megabits per second, but there may be disk space restraints and the software tools necessary to convert and store this format are costly. MPEG-4 has a lower transfer rate of 1-2 megabits per second and is intended for streaming video. Other codecs, such as QuickTime, Windows Media, Real Video and Open DIVX, are useful for specific purposes, but not suitable for preservation.  ((Knight, G., &amp; McHugh, J. (2005). <span style="font-style:italic;"><a href="http://www.ahds.ac.uk/preservation/video-preservation-handbook.pdf" title="http://ahds.ac.uk/preservation/video-preservation-handbook.pdf">Preservation Handbook: Moving Image</a></span>.  p. 3.))</p></blockquote>
<p>The Library of Congress Sustainability of Digital Formats site has <a href="http://www.digitalpreservation.gov/formats/fdd/fdd000028.shtml" title="http://www.digitalpreservation.gov/formats/fdd/fdd000028.shtml">an entry for MPEG-2</a> (also known as H.262) and <a href="http://www.digitalpreservation.gov/formats/fdd/fdd000155.shtml" title="MPEG-4 File Format, Version 2">an entry for MPEG-4</a> (more completely, MPEG-4 file format version #2) that give the nitty-gritty details for the file formats.</p>
<p>The preservation master copies we want to store has a frame size of 720 pixels by 480 pixels.  (That size is for NTSC format videos, common in USA, Canada and Japan.  Master copies of PAL-format videos, common in Australia, New Zealand, the United Kingdom and most of Europe, is 720 x 576.)  This is the standard resolution used in MPEG-2-compressed commercially distributed DVD movies. ((<a href="http://www.nyu.edu/its/humanities/ninchguide/VII/" title="Audio/Video Capture and Management chapter of NINCH Guide to Good Practice">Audio/Video Capture and Management</a> (2002).))  These frame sizes are appropriate for analog video signals.  ("As defined by ITU-R Recommendation BT.601, more commonly know by the abbreviations Rec. 601 or BT.601 or its former name, CCIR 601. [It is] a standard published by the CCIR (now ITU-R) for encoding interlaced analogue video signals in digital form." (("Rec. 601" (2008).)) )  The audio is 48KHz stereo at 224 kb/s or better.</p>
<h2>Captioning Text</h2>
<p>There appears to be two primary schemes for binding closed captioned text with video files.  One from the W3C is <a href="http://www.w3.org/AudioVideo/" title="http://www.w3.org/AudioVideo/">Synchronized Multimedia Integration Language</a> (or SMIL) is an XML format and is used by many media players.  The other is Microsoft's <a href="http://msdn2.microsoft.com/en-us/library/ms971327.aspx" title="Object moved">Synchronized Accessible Media Interchange</a> (or SAMI), a pseudo-HTML format that is only read by Windows Media player.</p>
<p>To make matters more complicated, a whole set of different schemes are used for DVDs.  (On VHS recordings, closed caption text was encoded in one of the non-visible lines that make up the video signal.  Since the DVD format only included visible lines, other schemes were required.)  The most popular seems to be the <a href="http://www.fileinfo.net/extension/scc" title="SCC File Extension - Open .SCC files">Scenarist Closed Caption (SCC) format</a>.  This is a binary file that exists on the DVD along side the video files.</p>
<h2>Resources Consulted</h2>
<div style="line-height:1.1em;margin-left:0.5in;text-indent:-0.5in;margin-top:1.5em;">
<p style="margin:0">Arms, C. R., &amp; Fleischhauer, C. Sustainability of Digital Formats: Planning for Library of Congress Collections. <span style="font-style:italic;">National Digital Information Infrastructure and Preservation Program</span>. Retrieved April 8, 2008, from <a href="http://www.digitalpreservation.gov/formats/" title="Sustainability of Digital Formats: Planning for Library of Congress Collections">http://www.digitalpreservation.gov/formats/</a>.</p>
<p style="margin:0"><span style="font-style:italic;">Audio/Video Capture and Management</span>. (2002).In <span style="font-style:italic;">NINCH Guide to Good Practice</span> (1st). Retrieved April 8, 2008, from <a href="http://www.nyu.edu/its/humanities/ninchguide/VII/" title="NINCH Guide to Good Practice">http://www.nyu.edu/its/humanities/ninchguide/VII/</a>. </p>
<p style="margin:0">Guideline H: Provide access to multimedia presentations for users with sensory disabilities. <span style="font-style:italic;">Accessible Digital Media: Design Guidelines for Electronic Publications, Multimedia and the Web</span>.  Retrieved 14-Apr-2008 from <a href="http://ncam.wgbh.org/invent_build/web_multimedia/accessible-digital-media-guide/guideline-h-multimedia" title="Accessible Digital Media: Guideline H: Multimedia">http://ncam.wgbh.org/publications/adm/guideline_h.html</a>.</p>
<p style="margin:0">Knight, G., &amp; McHugh, J. (2005). <span style="font-style:italic;">Preservation Handbook: Moving Image</span>. AHDS Preservation Handbook. 8 p. Arts and Humanities Data Service. Retrieved April 8, 2008, from <a href="http://www.ahds.ac.uk/preservation/video-preservation-handbook.pdf" title="AHDS&#039;s Preservation Handbook: Moving Image">http://ahds.ac.uk/preservation/video-preservation-handbook.pdf</a>.</p>
<p style="margin:0">Rec. 601. (2008, April 8).<span style="font-style:italic;">Wikipedia, the free encyclopedia</span>. Retrieved April 8, 2008, from <a href="http://en.wikipedia.org/wiki/Rec._601" title="http://en.wikipedia.org/wiki/Rec._601">http://en.wikipedia.org/wiki/Rec._601</a> (<a href="http://en.wikipedia.org/wiki/Rec._601?oldid=204278564" title="http://en.wikipedia.org/wiki/Rec._601?oldid=204278564">version at time of citation</a>).</p>
</div>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://ahds.ac.uk/ to http://www.ahds.ac.uk/ on January 28th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://ahds.ac.uk/preservation/ahds-preservation-documents.htm to http://www.ahds.ac.uk/preservation/ahds-preservation-documents.htm on January 28th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://ahds.ac.uk/preservation/video-preservation-handbook.pdf to http://www.ahds.ac.uk/preservation/video-preservation-handbook.pdf on January 28th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://ahds.ac.uk/preservation/video-preservation-handbook.pdf to http://www.ahds.ac.uk/preservation/video-preservation-handbook.pdf on January 28th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://ncam.wgbh.org/publications/adm/guideline_h.html to http://ncam.wgbh.org/invent_build/web_multimedia/accessible-digital-media-guide/guideline-h-multimedia on January 28th, 2011.</p>
