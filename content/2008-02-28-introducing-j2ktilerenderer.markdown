---
layout: wordpress-import
status: published
published: true
title: 'JPEG2000 to Zoomify Shim -- Creating JPEG tiles from JPEG2000 images'
modified: 2008-02-28T12:15:42+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 334
wordpress_url: http://dltj.org/article/introducing-j2ktilerenderer/
date: '2008-02-28 07:15:42 -0500'
date_gmt: '2008-02-28 12:15:42 -0500'
category: JPEG2000
categories:
- JPEG2000
tags:
- jpeg2000
- restlet
- java
- DSpace
- code4lib
- code4lib Conference 2008
- j2ktilerenderer
comments:
- id: 31688
  author: Rob Lancefield
  author_email: rob@lancefield.net
  author_url: ''
  date: '2008-02-28 10:25:32 -0500'
  date_gmt: '2008-02-28 15:25:32 -0500'
  content: Great to know about this, Peter. Thanks for posting!  --Rob
- id: 32080
  author: Chris Freeland
  author_email: chris.freeland@mobot.org
  author_url: http://blog.chrisfreeland.com
  date: '2008-03-06 15:36:47 -0500'
  date_gmt: '2008-03-06 20:36:47 -0500'
  content: Have you looked at <a href="http://www.mojavelinux.com/projects/gsiv/"
    rel="nofollow">GSIV</a> for delivery?  The Biodiversity Heritage Library is also
    delivering JP2 via JPG tiles (see this <a href="http://www.biodiversitylibrary.org/item/13935"
    rel="nofollow">example page</a>), but we're using the proprietary LizardTech ExpressServer
    to decode (we were long-time MrSID users) and the open source GSIV for display
    in the browser.  Worth looking into if you haven't already.<p style="padding:0;margin:0;font-style:italic;">The
    text was modified to update a link from //www.mojavelinux.com/projects/gsiv/ to
    http://www.mojavelinux.com/projects/gsiv/ on December 30th, 2010.</p><p style="padding:0;margin:0;font-style:italic;">The
    text was modified to update a link from //www.biodiversitylibrary.org/item/13935
    to http://www.biodiversitylibrary.org/item/13935 on December 30th, 2010.</p>
- id: 32877
  author: Nick Ruest
  author_email: ruestn@mcmaster.ca
  author_url: ''
  date: '2008-03-31 15:40:15 -0400'
  date_gmt: '2008-03-31 19:40:15 -0400'
  content: "@chris\r\n\r\nWhat version of LizardTech ExpressServer are you running?
    \ We are having a problem with it not rendering in mozilla based browsers, and
    Safari < 3.\r\n\r\nthanks!"
- id: 33257
  author: Etienne Posthumus
  author_email: etienne@pos.thum.us
  author_url: http://blog.pos.thum.us/
  date: '2008-05-14 06:48:30 -0400'
  date_gmt: '2008-05-14 10:48:30 -0400'
  content: "What a great idea.\r\n\r\nWe had similar problems with the disk space
    requirements mushrooming for large collections, and the time required to generate
    the tiles for each new image. My solution was to not Zoomify the images (we use
    plain Jpeg) but make a custom Flash viewer using Actionscript that loads the entire
    file. With networks speeds being so fast it is feasible.\r\n\r\nBut now, you have
    given me an idea that it would be doable to also dynamically dish up Zoomify tiles
    for large Jpeg files server-side. Would need a simple Python script to do. I will
    add this to my TO-DO list... ;-)"
- id: 33263
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-05-15 14:52:00 -0400'
  date_gmt: '2008-05-15 18:52:00 -0400'
  content: "@Etienne --\r\n\r\nThanks for the kind comments.  Some of the files we're
    working with are several 10s' of megabytes in size, so dumping them across the
    net to the browser isn't a great option for us.  I'd be curious to hear about
    how your script to generate the Zoomify tiles using Python works out; let me know!"
- id: 33264
  author: JPEG2000 to Zoomify Code4Lib Lightning Talk Video Now Available | Disruptive
    Library Technology Jester
  author_email: ''
  author_url: http://dltj.org/article/jpeg2000-to-zoomify-lightning-talk-video/
  date: '2008-05-15 15:16:56 -0400'
  date_gmt: '2008-05-15 19:16:56 -0400'
  content: "[...] of Code4Lib 2008 presentations possible. I just had a chance to
    notice that the video from my JPEG2000 to Zoomify Shim lightning talk was [...]"
- id: 33386
  author: OpenLayers Zoomify Example
  author_email: ''
  author_url: http://oldmapsonline.googlecode.com/svn/trunk/openlayers/examples/zoomify.html
  date: '2008-06-03 18:51:22 -0400'
  date_gmt: '2008-06-03 22:51:22 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Zoomify tiles can be also served dynamically
    on the server side from JPEG2000 masters using J2KTileRender with available integration
    for DSpace and soon for Fedora Digital Repository. IIPImage server can [...]<!--%kramer-ref-post%-->"
- id: 33470
  author: Museums - Zitgist Wiki
  author_email: ''
  author_url: ''
  date: '2008-06-19 15:57:32 -0400'
  date_gmt: '2008-06-19 19:57:32 -0400'
  content: "<!--%kramer-ref-pre%-->[...]  Here are a few museum blogs that are pretty
    decent: http://culturalsemanticweb.wordpress.com/ , http://dltj.org/article/introducing-j2ktilerenderer/
    , http://www.code4lib.org/ , http://www.powerhousemuseum.com/dmsblog/  Also, see
    Second Story? [...]<!--%kramer-ref-post%-->"
- id: 33506
  author: 'Old Maps Online: ImageServer IIPImage now supports Zoomify'
  author_email: ''
  author_url: http://blog.oldmapsonline.org/2008/06/imageserver-iipimage-now-supports.html
  date: '2008-06-24 19:28:07 -0400'
  date_gmt: '2008-06-24 23:28:07 -0400'
  content: "<!--%kramer-ref-pre%-->[...] and developer of the IIPImage and scientist
    in Laboratories of Louvre Gallery.Note: a project j2ktilerenderer is also generating
    Zoomify tiles - from JPEG2000.      Vystavil Klokan Petr Přidal   v 1:05        [...]<!--%kramer-ref-post%-->"
- id: 33839
  author: 'Introducing djatoka: A Reuse Friendly, Open Source JPEG 2000 Image Server'
  author_email: ''
  author_url: http://www.dlib.org/dlib/september08/chute/09chute.html
  date: '2008-09-15 14:10:43 -0400'
  date_gmt: '2008-09-15 18:10:43 -0400'
  content: "<!--%kramer-ref-pre%-->[...] [5] Murray, P. (2008, February 28). JPEG2000
    to Zoomify Shim &#150; Creating JPEG tiles from JPEG2000 images. Disruptive Library
    Technology Jester. <http://dltj.org/article/introducing-j2ktilerenderer/>. [...]<!--%kramer-ref-post%-->"
- id: 36522
  author: 'Re: [Dspace-tech] Zooming software for Dspace'
  author_email: ''
  author_url: http://www.mail-archive.com/dspace-tech@lists.sourceforge.net/msg07714.html
  date: '2009-06-11 07:19:18 -0400'
  date_gmt: '2009-06-11 11:19:18 -0400'
  content: "<!--%kramer-ref-pre%-->[...] it has already been done (for DSpace) by
    the OhioLINK developers using on-the-fly tile creation: http://dltj.org/article/introducing-j2ktilerenderer/
    Thanks, Stuart Lewis Digital Services Programmer Te Tumu Herenga The University
    of Auckland Library [...]<!--%kramer-ref-post%-->"
- id: 38120
  author: Kemp Watson
  author_email: kemp@objectivepathology.com
  author_url: http://www.objectivepathology.com
  date: '2009-09-13 11:24:34 -0400'
  date_gmt: '2009-09-13 15:24:34 -0400'
  content: Take a look at http://images.objectivepathology.com - we're delivering
    JPEG tiles from JPEG 2000 source images in many cases, transcoding on the fly
    as required from our own image server.
- id: 174747
  author: JPEG2000 software and toolkits - JP2K Working Group - Confluence
  author_email: ''
  author_url: http://wiki.opf-labs.org/display/JP2/JPEG2000+software+and+toolkits
  date: '2011-10-08 13:52:27 -0400'
  date_gmt: '2011-10-08 17:52:27 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Disruptive Library Technology Jester JPEG2000
    to Zoomify Shim [...]<!--%kramer-ref-post%-->"
- id: 305148
  author: 1905 SF Sanborn Maps, Now in Color &laquo; Burrito Justice
  author_email: ''
  author_url: http://burritojustice.com/2011/06/27/1905-sf-sanborn-maps-now-in-color/
  date: '2012-09-19 15:25:18 -0400'
  date_gmt: '2012-09-19 19:25:18 -0400'
  content: "<!--%kramer-ref-pre%-->[...] http://dltj.org/article/introducing-j2ktilerenderer/
    [...]<!--%kramer-ref-post%-->"
- id: 604065
  author: OSGeo Discuss - fastest option of serving huge imagery on web map on the
    fly
  author_email: ''
  author_url: http://osgeo-org.1560.x6.nabble.com/fastest-option-of-serving-huge-imagery-on-web-map-on-the-fly-td3850467.html
  date: '2013-06-05 05:23:54 -0400'
  date_gmt: '2013-06-05 09:23:54 -0400'
  content: "<!--%kramer-ref-pre%-->[...] > and the J2K Tiler Renderer: > http://dltj.org/article/introducing-j2ktilerenderer/.
    > None of the above seem to enable output as WMS (correct me if I&#039;m > wrong).
    One draw back [...]<!--%kramer-ref-post%-->"
- id: 661198
  author: OpenLayers Zoomify Example
  author_email: ''
  author_url: http://dev.openlayers.org/examples/zoomify.html
  date: '2014-09-21 09:42:33 -0400'
  date_gmt: '2014-09-21 13:42:33 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;] Zoomify tiles can be also served dynamically
    on the server side from JPEG2000 masters using J2KTileRender with available integration
    for DSpace and soon for Fedora Digital Repository. IIPImage server can [&#8230;]<!--%kramer-ref-post%-->"
---
<p>This is a textual representation of a lightning talk done on Feb 26th at <a href="http://code4lib.org/conference/2008" title="Code4Lib 2008 Conference Homepage">Code4Lib 2008</a>.  <del datetime="2008-05-15T19:17:08+00:00">When the video of the talk is up (thanks, Noel!) I'll link it here, too.</del>  The video is <a href="/article/jpeg2000-to-zoomify-lightning-talk-video/">now available</a>, and that article includes an update on progress since the this article was posted.</p>
<p>OhioLINK has a collection of JPEG2000 images as an access format that were generated for use in our <a href="http://dlxs.org/" title="Digital Library eXtension Service homepage">DLXS</a>-based content system.  We are in the process of migrating those collections to DSpace and were looking for a mechanism to leverage the existing JPEG2000 files and not have to generate new derivatives.  We are also considering the use of JPEG2000 as a preservation format, and would find it attractive to use the same image format for both access copies and preservation copies.  We looked at Zoomify, but to perform its scaling function it generates JPEG tiles at several resolutions and storing those tiles can triple or quadruple disk space requirements.  Or, one could use the 'enterprise' version of Zoomify and its proprietary PFF format or the equally proprietary MrSID format.  We didn't want to be locked into either of these scenarios.  Our solution is to create a web application that mimics the directory-of-JPEG-tiles solution, but to dynamically generate the tiles our of a JPEG2000 master.</p>
<p>The free version of Zoomify reads JPEG tiles out of a directory structure that looks like this:</p>
<table cellpadding="3">
    </table>
<tr>
<td style="white-space: nowrap;" valign="top">/ImageProperties.xml</td>
<td>Includes descriptive elements of the source image like height, width, and tile size.</td>
</tr>
<tr>
<td style="white-space: nowrap" valign="top">/TileGroup0/0-0-0.jpg</td>
<td>The highest power-of-2 zoom out level that creates an image with dimensions less than 256x256</td>
</tr>
<tr>
<td style="white-space: nowrap" valign="top">/TileGroup0/1-0-0.jpg</td>
<td>The tile at the upper left corner at the first power-of-2 zoom level</td>
</tr>
<tr>
<td style="white-space: nowrap" valign="top">/TileGroup0/1-1-0.jpg</td>
<td>The tile to the left of 1-0-0.jpg</td>
</tr>
<p>The shim mimics that directory structure.  It parses the URL of the request and dynamically creates the appropriate JPEG tile (or metadata file) out of the JPEG2000 image.</p>
<h2>The Code</h2>
<p>The JPEG2000 for Zoomify shim requires <a href="http://java.sun.com/javase/downloads/" title="Java Download page">Java</a> 1.5 or greater.  It does not require a servlet engine; rather, it uses the <a href="http://www.restlet.org/" title="Restlet project homepage">Restlet</a> library to perform as a stand-alone application.  The <a href="http://one-jar.sourceforge.net/" title="OneJar project homepage">OneJar</a> library allows the Java classes and required dependencies to be bundled into a single JAR file.  We're using the <a href="http://www.kakadusoftware.com/" title="Kakadu Software homepage">Kakadu Software JPEG2000 library</a> to perform the on-the-fly decoding of JPEG2000 images.  Kakadu is a commercial JPEG2000 codec, although <a href="http://www.kakadusoftware.com/index.php?option=com_virtuemart&amp;Itemid=19&amp;vmcchk=1&amp;Itemid=19" title="Kakadu Software purchasing and licensing guidelines">inexpensive licenses are available</a> for not-for-profit activity.  We are using the Enterprise version of <a href="http://www.zoomify.com/" title="Zoomify homepage">Zoomify</a>, a Flash-based image viewer, although I believe the free version will work as well.  (You'll need the Enterprise version to be able to modify and adapt the appearance of the Zoomify applet.)  The same techniques can also be used for other Flash applets and probably even JavaScript-based viewers (<i>a la</i> Google Maps).</p>
<p>The source code is available from the <span class="removed_link" title="https://drc-dev.ohiolink.edu/browser/j2kTileRenderer/trunk">OhioLINK DRC source code repository</span> (<span class="removed_link" title="https://drc-dev.ohiolink.edu/svn/j2kTileRenderer/trunk">Subversion access</span>).  We plan to integrate it into DSpace 1.5 as part of the <a href="http://info.drc.ohiolink.edu/" title="Ohio Digital Resource Commons | Save, Discover, and Share Your Resources and the Resources of the World">Ohio Digital Resource Commons</a>, and I may create a Fedora disseminator to serve up the tiles as well.</p>
<p>Thanks go out to Keith Gilbertson and John Davison on the OhioLINK staff for their help in making this work as well as Stu Hicks and Fran&ccedil;ois d'Erneville for being a sounding board for these ideas.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to https://drc-dev.ohiolink.edu/browser/j2kTileRenderer/trunk on January 13th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://code4lib/conference/2008 to http://code4lib.org/conference/2008 on January 28th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.kakadusoftware.com/Purchasing.html to http://www.kakadusoftware.com/index.php?option=com_virtuemart&Itemid=19&vmcchk=1&Itemid=19 on January 28th, 2011.</p>
