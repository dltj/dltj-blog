---
layout: wordpress-import
status: published
published: true
title: 'OhioLINK Mentors Three Students in the Google Summer of Code'
modified: 2006-05-24T13:03:16+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 61
wordpress_url: http://dltj.org/2006/05/soc-recipients-for-ohiolink/
date: '2006-05-24 09:03:16 -0400'
date_gmt: '2006-05-24 14:03:16 -0400'
category: Google Summer of Code
categories:
- OhioLINK
- JPEG2000
- Google Summer of Code
tags:
- OhioLINK
- jpeg2000
- Google Summer of Code
- Fedora Repository
comments: []
---
<p>OhioLINK is pleased to mentor three students working on projects for Ohio's higher education and libraries around the world during the Google Summer of Code 2006.  The three projects are:</p>
<dl>
<dt>JPIP Browser Applet and Streaming Server</dt>
<dd>JPIP is <a href="http://web.archive.org/web/20060428000000/http://jpeg.org/jpeg2000/j2kpart9.html" title="http://web.archive.org/web/20060428000000/http://jpeg.org/jpeg2000/j2kpart9.html">Part 9</a> of the JPEG 2000 specification and is used to stream image codestream blocks to a client on demand. For instance, a JPIP client on a desktop may ask for a certain quality level and resolution of a region of an image. Using the JPIP protocol, the client makes such requests to a server and the server responds with only the image codestream blocks needed by the client. This saves the overhead of transmitting the entire image file when, say, only a thumbnail version is required.</p>
<p>The server side of the JPIP client/server pair will connect to OhioLINK's existing FEDORA digital object repository.  <a href="http://www.fedora.info/" title="http://www.fedora.info/">FEDORA</a> is the "Flexible Extensible Digital Object Repository Architecture", an open source digital object repository created by Cornell University and the University of Virginia. A key aspect of the Fedora software is its use of "disseminators" to create derivatives on-demand of datastreams stored in the digital object package.</p>
<p>Running in the user's browser, the JPIP applet will request portions of a JPEG2000 image in FEDORA at a specified quality/resolution/clip and the FEDORA/JPIP disseminator will retrieve and return to the applet the requested precincts/packets directly from an archival master in the repository.</p>
</dd>
<dt>Communications System</dt>
<dd>The project consists of a set of two clients, written in Java, on the basis of the Internet Relay Chat (IRC) protocol. One client is targeted at patrons (readers, researchers, scholars, etc.); the other aims at facilitating the needs of librarians and other staff. The server end of the chat system consists of an IRC daemon. The clients, being pure Java, can easily be refitted into a number of embeddable modules, including browser applets, JNLP packages, NetBeans or Eclipse platform modules, etc. Using the ubiquitous and well-developed IRC as the underlying layer provides additional possibilities for sophisticated users and administrators, namely using IRC clients of their choice, using IRC bots when staff are unavailable, etc.</p>
<p>The project consists of two parts: the first being the implementation of a generic IRC client in Java with a GUI, and the second being the addition of advanced functionalities specifically for the purposes of OhioLINK and member libraries:  identity branding; ability to store and send &ldquo;canned&rdquo; messages; ability to transfer patrons among librarians; ability to email transcripts of sessions; ability to automatically email transcripts at the close of a session; a survey for user feedback; and the ability to service / monitor multiple queues.
</dd>
<dt>Video Snapshot Tool</dt>
<dd>This project will provide users with a capability to browse video collections to see 'snapshots' of what each video contains, with index pointers to characteristic frames (scene pointers), equally distant pointers, and user-defined pointers (which are saved within users profile, something like video-browsing history). There will be a timeline with predefined pointers (scene and equally distant pointers) which cannot be changed, and sliding pointers that are user defined (user adds them, deletes them etc.) which can have user comments. Every pointer will have a snapshot that will be shown to the user when he  positions cursor over that pointer.  The user will also be able to play the video from a selected pointer.</dd>
</dl>
<p>With nearly 100 mentoring organizations to choose from, there were 3050 students submitting 6338 proposals to this year's Summer of Code.  OhioLINK received 21 applications.</p>
