---
layout: wordpress-import
status: published
published: true
title: 'Fedora plus Sakai &mdash; a marriage made in heaven?'
modified: 2006-04-13T01:24:10+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 39
wordpress_url: http://dltj.org/2006/04/fedora-plus-sakai/
date: '2006-04-12 21:24:10 -0400'
date_gmt: '2006-04-13 02:24:10 -0400'
category: Library Technology
categories:
- DRC
- Fedora
- Unified Content Repository
tags:
- DRC
- Sakai
- Fedora Repository
comments:
- id: 30
  author: Ben Brophy
  author_email: benbr@mit.edu
  author_url: http://benbrophy.com/
  date: '2006-04-16 19:03:09 -0400'
  date_gmt: '2006-04-17 00:03:09 -0400'
  content: 'At MIT we''re doing a little mixing of Sakai and Fedora (plus sprinkle
    of O.K.I. a lot of our own stuff) in Stellar images, a project that revolves around
    gathering images from repositories, mixing them with your own and building slide
    lectures. Some info here: https://confab.mit.edu/confluence/display/STLR/Images'
- id: 32
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-04-17 14:30:34 -0400'
  date_gmt: '2006-04-17 19:30:34 -0400'
  content: Thanks, Ben.  I'm not all that familiar with OKI (except to know that I
    should get more familiar with it) -- could it be a good glue between a resource
    consumer like Sakai and a resource provider like Fedora?
- id: 33
  author: Adam Hochman
  author_email: adam@media.berkeley.edu
  author_url: http://confluence.media.berkeley.edu/confluence/display/BSPI/Home
  date: '2006-04-17 14:45:41 -0400'
  date_gmt: '2006-04-17 19:45:41 -0400'
  content: In the near future, for the bSpace Images, we will explore authorization/authentication
    issues/approaches between bSpace and Fedora.  Essentially Fedora will be our "image
    repository" within Sakai.  Our level of integration with Sakai's default Resource
    Tool may be limited to a means for users to add content from the Resources tool
    to their image personal collections.
- id: 20070
  author: Anand Subramanian
  author_email: anands@tatainteractive.com
  author_url: ''
  date: '2007-08-07 03:10:54 -0400'
  date_gmt: '2007-08-07 07:10:54 -0400'
  content: "[quote comment=\"30\"]At MIT we're doing a little mixing of Sakai and
    Fedora (plus sprinkle of O.K.I. a lot of our own stuff) in Stellar images, a project
    that revolves around gathering images from repositories, mixing them with your
    own and building slide lectures. Some info here: https://confab.mit.edu/confluence/display/STLR/Images[/quote]\r\n\r\nHello
    Ben, would you be able to share more details on Sakai integration with Fedora?"
- id: 33950
  author: DSpace 2.0/Modelling Services - DSpace Wiki
  author_email: ''
  author_url: https://wiki.duraspace.org/display/DSPACE/DSpace+2.0+Modelling+Services
  date: '2008-10-05 16:43:55 -0400'
  date_gmt: '2008-10-05 20:43:55 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Digital Library Technology Jester... http://dltj.org/article/fedora-plus-sakai/trackback/
    http://dltj.org/article/fedora-plus-sakai-3/trackback/ [...]<!--%kramer-ref-post%-->"
---
<div style="border: 1px solid gray;">Note -- there was a <a href="/article/fedora-plus-sakai-2/">follow-up to this post</a>.</div>
<p>What happens when you mix two <a href="http://www.mellon.org/" title="About the Foundation &amp;mdash; The Andrew W. Mellon Foundation">Mellon</a>-funded projects?  Perhaps a nice bit of what they call <a href="http://www.google.com/search?q=define%3A+synergy" title="http://www.google.com/search?q=define%3A+synergy">synergy</a>.  The thinking goes something like this...</p>
<h2>Sakai</h2>
<p>"The Sakai Project is a community source software development effort to design, build and deploy a new Collaboration and Learning Environment (CLE) for higher education. ... The Sakai Project's primary goal is to deliver the Sakai application framework and associated CMS tools and components that are designed to work together.  These components are for course management, and, as an augmentation of the original CMS model, they also support research collaboration.  The software is being designed to be competitive with the best CMSs available." ((See <a href="http://sakaiproject.org/index.php?option=com_content&#038;task=view&#038;id=103&#038;Itemid=208" title="Home | Sakai">http://sakaiproject.org/index.php?option=com_content&amp;task=view&amp;id=103&amp;Itemid=208</a>))</p>
<p>Written in the Java language for a servlet container, it is an example of some of the best thinking and work in the creation of a course management system (CMS) or a learning management system (LMS) [that plus "CLE" -- how many acronyms do we need?] in the open source arena.  It is truly an example of how <a href="/article/our-destiny/">higher education can take command of its destiny</a>.</p>
<h2>Fedora</h2>
<p>"Fedora open source software gives organizations a flexible service-oriented architecture for managing and delivering their digital content. At its core is a powerful digital object model that supports multiple views of each digital object and the relationships among digital objects." ((See <a href="http://fedora.info/" title="Fedora Repository | Fedora is a general-purpose, open-source digital object repository system.">http://fedora.info/</a>))</p>
<p>Also written in Java to run in a servlet container, it is the best of the basic research of the general characteristics of a digital object implemented in an easily approachable (and again -- open source) application.</p>
<h2>Mix Together with a Glob of Glue</h2>
<p>Our latest thinking about <a href="http://info.drc.ohiolink.edu/" title="DRC Home">Ohio's general purpose digital object repository</a> (based in Fedora) has a potentially interesting intersection point with Sakai.  In looking at<br />
the latest releases of the Sakai framework, it appears that the developers have consolidated all of the repository functions into one tidy unit they call "<a href="http://web.archive.org/web/20081122102007/http://cvs.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/service/legacy/entity/Entity.html" title="Entity">Entity</a>".</p>
<p>The methods for the Sakai Entity interface are:</p>
<ul>
<li> getId: Access the id of the entity.</li>
<li> getProperties: Access the entity's properties.</li>
<li> getReference: Access the internal reference which can be used to access the entity from within the system.</li>
<li> getReference: Access the alternate internal reference which can be used to access the entity from within the system.</li>
<li> getUrl: Access the URL which can be used to access the entity.</li>
<li> getUrl: Access the alternate URL which can be used to access the entity.</li>
<li> toXml: Serialize the entity into XML, adding an element to the doc under the top of the stack element.</li>
</ul>
<p>If this pans out, it should be relatively straight forward to swap out Sakai's built-in repository infrastructure with that of Fedora.  At the very least we'll need some new content models and disseminators.  So we'd have some more work to do on the Fedora end of the equation (and the Sakai end is a bit of an unknown to us at the moment), but on the surface it seems possible.</p>
