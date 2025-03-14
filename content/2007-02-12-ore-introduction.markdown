---
layout: wordpress-import
status: published
published: true
title: 'Introducing the OAI Object Reuse and Exchange Initiative'
modified: 2007-02-13T03:49:20+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 181
wordpress_url: http://dltj.org/2007/02/ore-introduction/
date: '2007-02-12 22:49:20 -0500'
date_gmt: '2007-02-13 03:49:20 -0500'
category: Linking Technologies
categories:
- Linking Technologies
tags:
- standards
- digital libraries
- Object Reuse and Exchange
comments:
- id: 12396
  author: 'Disruptive Library Technology Jester :: The Intersection of the Web Architecture
    with Scholarly Communication'
  author_email: ''
  author_url: http://dltj.org/2007/02/ore-model-services/
  date: '2007-02-16 15:01:44 -0500'
  date_gmt: '2007-02-16 20:01:44 -0500'
  content: "[...] Two previous posts on dltj.org have described the OAI Object Reuse
    and Exchange (ORE) project and the theory behind what has become known as the
    &#8216;Web Architecture&#8217;. These two areas meet up now in this post which
    describes the issues surrounding the raw Web Architecture as applied to a web
    of scholarly communication and a basic outline of what the ORE project hopes to
    accomplish. [...]"
- id: 12448
  author: pintiniblog
  author_email: ''
  author_url: ''
  date: '2007-02-18 07:38:40 -0500'
  date_gmt: '2007-02-18 12:38:40 -0500'
  content: "<strong>OAI-ORE, architecture web et information acad&eacute;mique...</strong>\n\nToujours
    dans le cadre de Open Repositories 2007, voici la pr&eacute;sentation de C. Lagoze
    et H. Van de Sompel sur le projet OAI-ORE.\r\n\r\nRep&eacute;r&eacute;e sur Disruptive
    Library Technology Jester dans une s&eacute;rie de posts &agrave; propos de l'architecture
    web et de l'in..."
- id: 79132
  author: Disruptive Library Technology - Close Encounters With Learning Objects of
    a Digital Kind - LibGuides at Auraria Library (UCD, MSCD, CCD)
  author_email: ''
  author_url: http://guides.auraria.edu/aecontent.php?pid=129320&amp;sid=1111272
  date: '2010-07-20 14:34:40 -0400'
  date_gmt: '2010-07-20 18:34:40 -0400'
  content: '<!--%kramer-ref-pre%-->[...] "...Digital objects &mdash; we&rsquo;ve all
    got &lsquo;em, billions and billions of them. And we put them in individual content
    silos, stratified along such unhelpful lines as media type, owning entity, and
    other equally meaningless categories. At least meaningless to the end user. So,
    let&rsquo;s ask ourselves: what is the job the user is trying to get done? And
    how can we structure our digital object repositories to help them out?..." - the
    Disruptive Library Techology Jester [...]<!--%kramer-ref-post%-->'
---
<p>In the past few months a new group has formed to tackle the problem of representing and exchanging complex digital objects in a web-based environment.  I am proud to serve on the technical committee for this group and over the next few postings I'm aiming to introduce the library community to the work of the Open Archives Initiative Object Exchange and Reuse group and seek the feedback of the wisdom of this crowd.</p>
<h2>Vision and Scope</h2>
<p><a href="http://www.openarchives.org/ore/" title="Open Archives Initiative - Object Exchange and Reuse home page">OAI Object Reuse and Exchange</a> (ORE) is a new effort conducted under the umbrella of the Open Archives Initiative.  The summary vision statement is to develop, identify, and profile extensible standards and protocols to allow repositories, agents, and services to interoperate in the context of use and reuse of compound digital objects beyond the boundaries of the holding repositories.  A key aspect of this statement is that it refers to working with objects, not about metadata only.  In that way, the ORE work is set apart from the previous OAI work, the <a href="http://www.openarchives.org/pmh/" title="Open Archives Initiative Protocol for Metadata Harvesting home page">Protocol for Metadata Harvesting</a> (PMH).</p>
<p>The aim of the ORE effort is to promote (through creation or endorsement) effective and consistent mechanisms:</p>
<ul>
<li>to facilitate discovery of compound digital objects;</li>
<li>to reference (or 'link to') these objects (as well as parts thereof);</li>
<li>to obtain a variety of disseminations of these objects;</li>
<li>to aggregate and disaggregate objects; and</li>
<li>to enable processing of objects by automated agents.</li>
</ul>
<p>Although these mechanisms may apply to more general web activities, the use cases we are working from are firmly bounded to the needs of the academic community.  Generally speaking, those use cases seek to establish the basis for a digital scholarly communication system composed of two types of systems:  a) applications that manage content (such as institutional repositories); and b) applications that leverage managed content (such as search engines, personal productivity tools, and data and text analysis services).  Of course, other application domains are possible, but like the initial OAI-PMH, the intent is to start with a domain with which we are familiar with an eye towards more general applications as appropriate.</p>
<h2>Compound Digital Objects</h2>
<p>Key to understanding the ORE vision and scope is a definition of the phrase "compound digital object."  In the case, a compound digital object is content with multiple components that vary on:</p>
<ul>
<li>Content, or semantic, types (including: text, datasets, simulations, software, dynamic knowledge representations, machine readable chemical structures, bibliographic and other types of metadata); </li>
<li>Media types (including IANA registered MIME types and other type/format registries such as GDFR);</li>
<li>Network locations (including content from institutional repositories, scientific data repositories, social networking sites and the general web); and</li>
<li>Relationships (where the digital object is part of a complex graph of objects related by lineage, versions, and derivations).</li>
</ul>
<p>In the abstract, this definition is understandably hard to grasp.  There are some conceptual examples the technical committee uses to keep focus on the task at hand.  One example is a paper in the arXiv repository with different disseminations.  Although the primary artifact in this example might be simply the paper itself, in even this case there is a compound digital object surrounding that artifact with components that represent the paper in PDF and Postscript formats, Dublin Core descriptive metadata, and an HTML "splash page" for the paper.  Another example is that of an issue of an overlay journal built from distributed ePrints from different repositories.  The nature of "the paper" itself is changing: in e-science the text of the paper is combined with data sets and simulations; in e-humanities, the text of the paper is combined with primary content (such as scanned items) and the scholar's derived content.</p>
<h2>Description of Work</h2>
<p>So an accurate perspective on the OAI-ORE work is that it seeks to enrich the content sharing landscape.  ORE is about enabling digital objects to float between systems that manage content and systems that leverage managed content.  In the first category are applications such as institutional repositories, research-group and managed personal (ePortfolio) repositories, discipline-oriented repositories, publisher repositories, dataset repositories, cultural heritage repositories, learning object repositories, and digitized book and manuscript collections.  In the second category are applications such as search engines, authoring tools, citation management, collaborative environments, social network applications, data/text mining applications, relationship graph analysis tools, preservation services, workflow tools, and report generation tools.</p>
<p>A key point to remember is that OAI-ORE is not necessarily about transferring the digital assets from one system to another.  It is the goal of the technical work to enable new, complex objects to be built without necessarily transferring all of the component parts from disparate content repositories to a single system.  (Reflect for a moment on the overlay journal concept -- the papers that make up the issue of the overlay journal could certainly remain dispersed in the repositories where they are originally located; the overlay journal pulls together the contents in a virtual construct that represents an issue of that overlay journal.)  In some use cases, transfer of the digital object content is required; preservation mirroring is one such example.  In many cases, however, full transfer is not permitted (by terms of use), impractical (as in a dataset that is terabytes in size) or simply superfluous.</p>
<p>At its first meeting, the technical committee identified some motivating use cases to guide our work.  At this point they are little more than general statements of the activities that can be done better with an ORE framework in place.  Over the course of the next few weeks the technical committee will elaborate on these general statements and turn them into stories.</p>
<ul>
<li>Find, collect, analyze, relate, and publish data-oriented scholarly objects</li>
<li>Preserve compound digital objects</li>
<li>Remote submission of compound digital objects</li>
<li>Citation management</li>
<li>Object equivalence recognition (de-duping) to aid resource discovery</li>
<li>Graph-based quality assessment of data-centric scholarship</li>
</ul>
<h2>OAI-ORE Project Organization</h2>
<p>The character of the project organization is similar to that of the Protocol for Metadata Harvesting effort.  Carl Lagoze (Cornell University) and Herbert Van de Sompel (Los Alamos National Laboratory) are the principle investigators on the project.  They coordinate the efforts of an international group of volunteers that form an Advisory Committee, a Technical Committee (of which I am a member) and a Liaison Committee.  The membership lists for these committees are available on the <a href="http://www.openarchives.org/ore/" title="Open Archives Initiative Protocol - Object Exchange and Reuse">OAI-ORE website</a>.  It is worth noting that the participants are not exclusively from the library domain.  In particular, there is an emphasis not just on text/image/video objects but also scientific data objects.  The <a href="http://www.openarchives.org/ore/documents/ORE-Announcement.html" title="For immediate release October 13">Andrew W. Mellon Foundation is funding the work</a> for a 24-month period that began in October 2006 with additional support from the National Science Foundation.</p>
<p>The impetus behind the OAI-ORE effort was a meeting in April 2006 of representatives from institutional repository projects, scholarly content repositories, registry projects, and various other projects that touch on interoperability.  See <a href="http://msc.mellon.org/Meetings/Interop/" title="http://msc.mellon.org/Meetings/Interop/">http://msc.mellon.org/Meetings/Interop/</a> or more information.</p>
<p>The ORE work does not imply that the OAI-PMH specification is being dropped or replaced.  OAI-PMH will continue to exist as one approach to interoperability.  OAI-ORE will complement OAI-PMH when richer functionality is desired as part of a multi-level interoperability stack. In fact, one might consider OAI-ORE to be resource centric in contrast to OAI-PMH's metadata-centric approach.</p>
<p>The technical committee has met once (the <a href="http://www.openarchives.org/ore/documents/OAI-ORE-TC-Meeting-200701.pdf" title="http://www.openarchives.org/ore/documents/OAI-ORE-TC-Meeting-200701.pdf">report of the meeting</a> is available from the ORE website) and will be conducting a conference call this week leading up to a second face-to-face meeting in May.  Right now we are fleshing out the use cases as a tool for testing models that we create or adapt from other uses.  We want to make sure what we're specifying will really work in our application domain.  Once we have a good sense of what a model of the ORE scope of work entails, we'll review existing related technologies with the intent of adapting what is currently available to meet the needs of the ORE model and only creating new specifications and protocols when it is really necessary.  Some early candidates of related technologies are OAI-PMH, RSS/ATOM, OpenURL, and METS/DIDL.</p>
<p>The technical committee has agreed amongst itself to use a tag of 'oaiore' in the various social web tools (<span class="removed_link" title="http://technorati.com/tag/oaiore">Technorati</span>, <a href="http://www.connotea.org/tag/oaiore" title="Pages tagged with &amp;quot;oaiore&amp;quot; on Connotea">Connotea</a>, and <a href="http://del.icio.us/tag/oaiore" title="Pages tagged with &amp;quot;oaiore&amp;quot; on del.icio.us">del.icio.us</a> for example) as a way to co-locate material on this topic.  Others are encouraged to do the same.  Fellow technical committee member <a href="http://efoundations.typepad.com/efoundations/2007/01/ore.html" title="eFoundations: Prospecting for ORE">Pete Johnson</a> (with <a href="http://efoundations.typepad.com/efoundations/2007/01/more_ore.html" title="eFoundations: More ORE">follow up</a>) has already started a conversation, and you can listen to <a href="http://www.educause.edu/blogs/mpasiewicz/interview-herbert-van-de-sompel" title="An Interview with Herbert van de Sompel via EDUCAUSE CONNECT">an interview with Herbert van de Sompel</a> via EDUCAUSE.</p>
<p>In a subsequent postings, I'll go into some detail about the <a href="/article/web-architecture/">inner workings of "The Web Architecture"</a> and how it is both <a href="/article/ore-model-services">a help and a hindrance to the interaction of compound digital objects in our domain</a>, and how it is a force too powerful to be ignored in either case.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://technorati.com/tag/oaiore on January 19th, 2011.</p>
