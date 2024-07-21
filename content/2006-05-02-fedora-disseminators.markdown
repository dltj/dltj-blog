---
layout: wordpress-import
status: published
published: true
title: 'Thinking about Our Fedora Disseminators'
modified: 2006-05-02T18:19:03+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 49
wordpress_url: http://dltj.org/2006/05/fedora-disseminators/
date: '2006-05-02 14:19:03 -0400'
date_gmt: '2006-05-02 19:19:03 -0400'
category: Library Technology
categories:
- DRC
- Fedora
- Unified Content Repository
tags:
- metadata
- asset actions
- Fedora Repository
comments:
- id: 50
  author: "&tau;&epsilon;&chi;&nu;&omicron;&sigma;&omicron;&phi;&iota;&alpha; &raquo;
    The Jester&#8217;s Case for Fedora"
  author_email: ''
  author_url: http://www.lackoftalent.org/michael/blog/2006/05/02/the-jesters-case-for-fedora/
  date: '2006-05-02 16:57:14 -0400'
  date_gmt: '2006-05-02 21:57:14 -0400'
  content: "[...] The third piece, Thinking about Our Fedora Disseminators, highlights
    Fedora as a repository system that&#8217;s put real emphasis on digital preservation.
    \ While other repository systems allow for preservation of an object and its metadata,
    Fedora grants one the ability to preserve the behavior of digital objects and
    the datastreams thereof, a potential approach to the issue of format migration/emulation.
    \ Through a dissemination abstraction (the &#8220;behavior definition&#8221;)
    one might apply the same abstract behaviors to items in different formats, saving
    one the time of defining redundant behaviors.  My explanation is rather vague
    and incomplete, so I would encourage you to read Peter&#8217;s third piece in
    detail.  The point is that &#8220;for each record, the application simply asked
    the repository to deliver a thumbnail of the object. And the repository, regardless
    of media type, delivered one.&#8221;  [...]"
- id: 51
  author: Muriel Foulonneau
  author_email: mfoulonn@uiuc.edu
  author_url: ''
  date: '2006-05-02 18:04:13 -0400'
  date_gmt: '2006-05-02 23:04:13 -0400'
  content: "A sub-group of Fedora adopters and the Digital Library Federation working
    Group has been working on expanding the Fedora disseminator. We have experimented
    [an expression of] those disseminators for images with content harvested through
    OAI. The demonstrator is here http://rama.grainger.uiuc.edu/assetactions/, it
    integrates the Collector tool developed at Virginia on distributed content, whichever
    the system used. I am working on a way of generating those disseminators based
    on OAI records and an application developed by Tom Habing here at UIUC to generate
    thumbnails (same model as Alexa and Thumbshots.org but for OAI records).\r\nAll
    this to say that generally, we are trying to do something like that and any help
    and feedback would be useful."
- id: 53
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-05-03 12:14:36 -0400'
  date_gmt: '2006-05-03 17:14:36 -0400'
  content: Muriel -- very interesting work!  Thanks for passing it along.  I took
    a quick look at the Asset Actions page (it took me a while to figure out that
    I had to search the collection at the top to see any of the enhancements rather
    than use the links to the raw collection websites at the bottom) and then printed
    out the documents to read over lunch.  It sounds like there is a lot of thought
    here about actions that can be applied to objects, so I'm going to dig deeper.
- id: 60
  author: Disruptive Library Technology Jester &raquo; Fedora Disseminators to Enable
    Accessible Repository Content
  author_email: ''
  author_url: http://dltj.org/2006/05/fedora-disseminators-for-accessibility/
  date: '2006-05-05 22:04:30 -0400'
  date_gmt: '2006-05-06 03:04:30 -0400'
  content: "[...] why not? Let&#8217;s look back at the &#8220;presentation&#8221;
    part of the disseminator label: &#182;  A presentation can be oneof: [...]"
- id: 2996
  author: 'Disruptive Library Technology Jester :: Analysis of CDL&#8217;s XTF textIndexer
    to Replace the Local Files with FEDORA Objects'
  author_email: ''
  author_url: http://dltj.org/2006/08/xtf-fedora-2/
  date: '2006-08-22 20:17:35 -0400'
  date_gmt: '2006-08-23 01:17:35 -0400'
  content: '[...] just the XML transformation tool would be needed (as in this snipped
    from SrcTreeProcessor.java): &#182; PLAIN TEXT JAVA:  IndexSource srcFile = null;
    if&#40; format.equalsIgnoreCase&#40;"XML"&#41; &#41;&#123; &nbsp; &nbsp; InputSource
    finalSrc = new InputSource&#40; systemId &#41;; &nbsp; &nbsp; srcFile = new XMLIndexSource&#40;
    finalSrc, srcPath, key,  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;preFilters, displayStyle, lazyStore
    &#41;; &nbsp; &nbsp; if&#40; removeDoctypeDecl &#41; &nbsp; &nbsp; &nbsp; &nbsp;
    &#40;&#40;XMLIndexSource&#41;srcFile&#41;.removeDoctypeDecl&#40; true &#41;; &#125;
    [...]'
- id: 3793
  author: OhioLINK Disseminators - FedoraWiki
  author_email: ''
  author_url: ''
  date: '2006-09-11 16:42:25 -0400'
  date_gmt: '2006-09-11 20:42:25 -0400'
  content: "<!--%kramer-ref-pre%-->[...] There is [some background material] leading
    up to this perspective that may be useful to review. (It also has a general discussion
    about what disseminators are and why they are important.) Keep in mind that OhioLINK&rsquo;s
    Fedora repository vision doesn&rsquo;t expect to have one front end; rather we
    anticipate getting to the repository data from a number of genre-, topic-, or
    technology-specific interfaces. In doing so, a lot of the intelligence about how
    to handle media types needs to go into the disseminators. With this perspective,
    one thinks about how an object can present itself in generic ways to a wide variety
    of interfaces. The name/label of a disseminator in the repository has three parts:
    \  action  presentation  optional sizing parameters [...]<!--%kramer-ref-post%-->"
- id: 11285
  author: 'Disruptive Library Technology Jester :: Building an Institutional Repository
    Interface Using EJB3 and JBoss Seam'
  author_email: ''
  author_url: http://dltj.org/2007/01/drc-ir-ejb3-seam/
  date: '2007-01-18 23:01:33 -0500'
  date_gmt: '2007-01-19 04:01:33 -0500'
  content: "[...] The paradigm of handling different media types within the DRC application
    is guided in large part by the notion of disseminators for FEDORA objects and
    the Digital Library Federation Aquifer Asset Actions experiments. The underlying
    concept is to push the media-specific content handling into the digital object
    repository and to have the presentation interface consume those content handlers
    as it is preparing the end-user presentation. [...]"
---
<p>Another reason to consider the FEDORA digital object repository system, if <a href="/article/general-purpose-repository/">having the ability to put all of your content in one place</a> and <a href="/article/why-fedora-because-you-dont-need-fedora/">reducing the complexity of digital preservation</a> aren't enough, is the capability to create and define behaviors that the content can perform.  In the <a href="http://www.fedora.info/" title="Fedora">FEDORA</a> world, these behaviors are called disseminators.</p>
<p>By way of example -- say you have a digital object that is an image that you want to display to users.  Furthermore, you want to create at the time of the user's request a smaller "thumbnail" version on search results lists and so forth.  (Let's set aside for a moment that the system could create thumbnail derivatives in batch and simply deliver that to the user.  Someday I'll propose that dynamic derivatives from a JPEG2000 master are a better way to go, but not now.  Stick with me...it'll be worth it.)  From a system architecture point of view, the resize operation can happen in at least two places:  as a function of the content repository or as a function of the interface application.  In this simple example, one might argue that the best place is in the interface application.</p>
<p>Now let's say that your content repository has not only still images but moving image files.  Uh, oh.  That means the application now has to be smart enough to know whether a particular search results hit is a still image or a moving image datastream.  And the application is going to have to know how to transform a large image to a thumbnail <i>and</i> know how to extract a key frame from a sequence of moving images.  And if you have more than one interface to the object repository (say, one that presents a digital library interface and one that integrates objects into your learning environment) then you're going to have to replicate that still image and moving image capability in more than one application.</p>
<p>So instead, what if we put the "smarts" of the object into the repository and create some well-defined expectations for what every object in the repository has to do.  That "smarts" in the repository are the <i>Disseminators</i> and the well-defined expectations is the <i>Content Model</i>.  The "dumb" application (relatively speaking) gets a list of record identifiers that are the results of a search and asks the repository to give it a thumbnail images for each one.  The first record is a still image, so the repository resizes the image and delivers the result to the application.  The second record is a moving image file, so the repository extracts one frame, resizes it, and delivers it back to the application.  The third record is that of a book -- want to guess what happens?  Perhaps the repository returns a thumbnail-sized image of the book jacket?  Or maybe an image rendering of the title page?  Okay, now so the fourth record is of a dataset -- how do we get a thumbnail of a dataset?  Maybe a reduced size of visualization of the image?  What if the fifth was of a website?  Have you seen "thumbnail" sizes of websites, such as through <span class="removed_link" title="http://pages.alexa.com/exec/faqsidos/help/index.html?index=126">Alexa</span> or <a href="http://www.thumbshots.org/" title="Open Thumbshots - Free Web thumbnail preview image. Visualize sites in directory, search engine. View visual screenshot picture link. See snapshot graphics of Web page. Thumbnails screenshots snapshots thumbshot pictures images. Whether you&#039;re searching for a car, flower, photo or girafa, thumbshots will help you find it quickly and accurately.">Thumbshots.org</a>?</p>
<p>This is the key point:  for each record, <i>the application simply asked the repository to deliver a thumbnail of the object.</i>  And the repository, regardless of media type, delivered one.</p>
<p>Okay, enough background.  Also keep in mind that OhioLINK's Fedora repository vision doesn't expect to have one front end; rather we anticipate getting to the repository data from a number of genre-, topic-, or technology-specific interfaces.  In doing so, I think a lot of the intelligence about how to handle media types needs to go into the disseminators.  So I'm thinking about how an object can present itself in generic ways to a wide variety of interfaces.</p>
<p>So in my current line of thinking, the name of a disseminator in the repository has three parts:</p>
<ul>
<li>action</li>
<li>presentation</li>
<li>optional sizing parameters</li>
</ul>
<p>An action can be one of:</p>
<ul>
<li>"get" - raw stream of bits from the datastream</li>
<li>"view" - HTML-wrapped version of the stream of bits plus activities that can be applied to the datastream intended for access by a GUI or to be transformed via XSLT</li>
</ul>
<p>I tried to combine the GUI and XSLT actions into "view" on the theory<br />
that the HTML wrapper would have sufficient CSS "id" and "class" values<br />
to make it possible to style it with CSS or transform it with XSLT.<br />
This may not be a practical theory once we get to implementation.</p>
<p>A presentation can be one of:</p>
<ul>
<li>"preview" - a small/short version of the datastream returned in the datastream's original format</li>
<li>"screen" - a roughly GUI-screen-sized version of the datastream returned in the datastream's original format</li>
<li>"thumb" - a small, static image derivative of the datastream</li>
<li>"audio" - an auditory derivative of the datastream</li>
<li>"description" - a Dublin Core description of the item marked up in an HTML table</li>
<li>"record" - HTML markup of Thumb plus Description (suitable, for instance, as a representation of the object in a browse list)</li>
</ul>
<p>The final piece of the name is "Sized" which can be used to pass parameters that override the dimensions of the "preview" and "thumb" presentations.</p>
<p>So these would get put together like this (with examples based on still images):</p>
<ul>
<li>"getPreview" - return an x-by-y derivative of the datastream</li>
<li>"getThumb" - in the case of still images, same as "getPreview"</li>
<li>"viewThumb" - the same derivative as "getThumb" wrapped in an HTML div such as:
<pre>

<div class="viewThumb" id="viewThumb[PID][DS]">

  <div class="getThumb" id="getThumb[PID][DS]">

    <img class="getThumbImg" id="getThumb[PID][DS]Img" alt="Thumbnail of [DS]" src="..." />

  </div>

  <div class="getThumbOptions" id="getThumbOptions[PID][DS]">

    <span class="getThumbOptionScreen" id="getThumbOptionScreen[PID][DS]">

      <a href="[URL to getScreen]">View Screen-sized</a>

    </span>

    <span class="getThumbOptionDescription"

id="getThumbOptionDescription[PID][DS]">

      <a href="[URL to getDescription">View Description</a>

    </span>

    ....

  </div>

</div>

</pre>
<p>   (where [PID] is the Fedora PID and [DS] is the datastream label)</li>
</ul>
<p>For non-static images, it gets a little more interesting because:</p>
<ul>
<li>"getPreview" of a video would return a short video segment defined as the 'preview' of the larger video where as "getThumb" of that same video datastream would return just a single frame from the video.</li>
<li>"getPreview" of a journal article could return a block of text that is the abstract of the article while "getThumb" of that same journal article could return an image rendering of the first page of the article</li>
<li>"getScreen" of a journal article could return an HTML fragment of the article itself while "getAudio" might return a prerecorded or computer-synthesized rendition of the article</li>
</ul>
<p>That's the basic plan, open for comments before we get too far with the coding part of the project.  Thoughts?
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://pages.alexa.com/exec/faqsidos/help/index.html?index=126.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.thumbshots.org/freethumbshots.pxf to http://www.thumbshots.org/.</p>
