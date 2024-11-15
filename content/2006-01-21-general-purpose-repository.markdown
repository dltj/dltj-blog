---
layout: wordpress-import
status: published
published: true
title: 'On the Need for a General Purpose Digital Object Repository'
modified: 2006-01-21T13:22:45+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 13
wordpress_url: http://dltj.org/2006/01/general-purpose-repository/
date: '2006-01-21 08:22:45 -0500'
date_gmt: '2006-01-21 13:22:45 -0500'
category: Library Technology
categories:
- DRC
- Fedora
- Unified Content Repository
tags:
- DRC
- Fedora Repository
comments:
- id: 10
  author: LibbyTheLibrarian.org &raquo; Blog Archive &raquo; The Need for Convergence,
    part 2
  author_email: ''
  author_url: ''
  date: '2006-02-24 17:17:49 -0500'
  date_gmt: '2006-02-24 22:17:49 -0500'
  content: "[...] For another cogent argument on the need for convergence in the &#8220;digital
    library&#8221; world, check out the Disruptive Library Technology Jester&#8217;s
    post on &#8220;The Need for a General Purpose Digital Object Repository&#8221;
    at http://dltj.org/2006/01/general-purpose-repository. [...]"
- id: 48
  author: "&tau;&epsilon;&chi;&nu;&omicron;&sigma;&omicron;&phi;&iota;&alpha; &raquo;
    The Jester&#8217;s Case for Fedora"
  author_email: ''
  author_url: http://lackoftalent.org/michael/blog/2006/05/02/the-jesters-case-for-fedora/
  date: '2006-05-02 16:39:25 -0400'
  date_gmt: '2006-05-02 20:39:25 -0400'
  content: "[...] In the first piece, On the Need for a General Purpose Digital Object
    Repository, it is argued that having a unified repository simplifies management
    of information systems or &#8220;silos.&#8221;&nbsp; For instance,&nbsp;there
    needn&#8217;t be duplication of workflows or synchronization of content if a number&nbsp;of
    an organization&#8217;s repositories, digital libraries, electronic journals,
    course management systems and so on are all built atop a robust institutional
    repository.&nbsp; A unified repository is useful if one desires a search across
    previously disparate digital projects or collections, if one wishes to eliminate
    redundancies in coding, if one intends to have a particular object, collection
    of objects, or part of an object shared across different systems &#8212; e.g.,
    a journal article repurposed in a course management system and deposited into
    an open archive.&nbsp; With an open,&nbsp;flexible repository,&nbsp;like Fedora,
    such a configuration is possible assuming your organization, unit, or consortium&nbsp;has
    someone to devote to managing and customizing the repository.&nbsp; [...]"
- id: 18409
  author: 'Re: Sakai Fedora Tool'
  author_email: ''
  author_url: http://osdir.com/ml/cms.sakai.devel/2006-04/msg00432.html
  date: '2007-06-22 10:24:42 -0400'
  date_gmt: '2007-06-22 14:24:42 -0400'
  content: <!--%kramer-ref-pre%-->[...] the Fedora repository. (See "On the Need for
    a General Purpose Digital Object Repository" http://dltj.org/2006/01/general-purpose-repository/
    for a more in-depth discussion.) > We've been working on a proof-of-principle
    sakai-fedora-tool. [...]<!--%kramer-ref-post%-->
---
<p>Digital objects -- we've all got 'em.  Billions and billions of them.  And we put them in individual content silos, stratified along such unhelpful lines as media type, owning entity, and other equally meaningless categories.  At least meaningless to the end user.  So, let's ask ourselves:  what is the <em>job</em> the <em>user</em> is trying to get <em>done</em>?  And how can we structure our digital object repositories to help them out?</p>
<h2>What is a Digital Object?</h2>
<p>Kahn and Wilensky ((Kahn, Robert and Wilensky, Robert. 1995. "A Framework for Distributed Digital Object Services." <a href="http://www.cnri.reston.va.us/home/cstr/arch/k-w.html" title="Kahn/Wilensky Architecture">http://www.cnri.reston.va.us/home/cstr/arch/k-w.html</a>)) define a digital object as "a data structure whose principal components are digital material, or data, plus a unique identifier for this material, called a handle (and, perhaps, other material)." Lagoze, <em>et al</em>, further define 'other material' to include "terms and conditions &hellip; an encapsulation of access rules on use of the object" ((Lagoze, Carl. 1995. A Secure Repository Design for Digital Libraries. D-Lib Magazine. <a href="http://www.dlib.org/dlib/december95/12lagoze.html" title="A Secure Repository Design for Digital Libraries">http://www.dlib.org/dlib/december95/12lagoze.html</a>)) and metadata ("data about data" ((Daniel, Ron, Jr.; Lagoze, Carl; and Payette, Sandra D. A Metadata Architecture for Digital Libraries. <a href="http://web.archive.org/web/20120617040554/http://www.cs.cornell.edu/lagoze/papers/ADL98/dar-adl.html" title="A Metadata Architecture for Digital Libraries">http://www.cs.cornell.edu/lagoze/papers/ADL98/dar-adl.html</a>)) ).</p>
<p>Furthermore, Daniel, Lagoze and Payette distill the principles of a digital object repository within a model they call "Distributed Active Relationships":</p>
<ul>
<li>There is no essential distinction between data and metadata. We can only make such a distinction in terms of a particular "about" relationship. As a result, what is metadata in the context of one "about" relationship may be data in another.</li>
<li>There is no single "about" relationship. There are many different and important relationships between data resources.</li>
<li>Resources can be related without regard for their location. The connectivity in networked information architectures makes it possible to have data in one repository describe data in another repository.</li>
<li>The computational power of the networked information environment makes it possible to consider active or dynamic relationships between data sets. This adds considerable power to the "data about data" definition. First, data about another data set may not physically exist, but may be automatically derived. Second, the "about" relationship may be an executable object -- in a sense interpretable metadata.</li>
</ul>
<p>Within such a general framework, it is possible to refer to digital objects, their metadata, and the services/operations/transformations applied to them as distinct entities.</p>
<h2>Where Digital Objects Reside Today</h2>
<p>Many systems have been and are being deployed on college campuses that contain, in part, the concept or a subsystem for storing digital objects as reflected by this general definition.</p>
<p><strong>Digital Library</strong> systems (examples of specific instances are <a href="http://www.greenstone.org/" title="302 Found">Greenstone</a> and <a href="http://www.oclc.org/en-US/contentdm.html" title="CONTENTdm Digital Collection Management Software by DiMeMa, Inc.">ContentDM</a>) store and present the bitstreams along with their associated, typically very rich metadata. The library, archive, or museum staff play an important, and sometimes sole, role in ingesting content into the system. Content is presented as in an online exhibition or a search/retrieve interface. Digital library systems usually also have the goal of preserving bitstreams, metadata, and context for scholars in the distant future.</p>
<p><strong>Institutional Repositories</strong> (IRs - <a href="http://dspace.org/" title="DSpace Federation">DSpace</a>, <span class="removed_link" title="http://www.umi.com/proquest/digitalcommons/">Digital Commons</span> and <a href="http://www.iii.com/products/symposia.shtml" title="Innovative Interfaces: Millennium: Digital Collections">Symposia</a>) offer a web-based interface to those that perform the content ingestion process (in most use cases their roles are faculty, instructor, researcher, or the administrative assistant of one of these). There is a hierarchical representation of communities within communities, into which digital objects are placed. Presentation of content reflects the same organization of communities within communities. Like digital library systems, the design and implementation of subsystems within an IR are guided by best practices for preserving information in a digital form.</p>
<p><strong>Electronic Journals</strong> (ejournals - <a href="http://www.eprints.org/uk/" title="302 Found">eprints</a>, <span class="removed_link" title="http://dpubs.org/">DpubS</span> and <a href="http://www.bepress.com/" title="302 Found">BEPress</a>) require specialized handling and presentation of content. Authors submit digital objects to editors; editors in turn use a machine-mediated workflow to farm out, track, and collate comments from reviewers. Revised digital objects are packaged together in "issues" and "volumes" for presentation on the website. There is usually a commitment to ongoing preservation of ejournal digital objects.</p>
<p><strong>Collaborative Learning Environments</strong> (CLEs - <a href="http://sakaiproject.org/" title="sakaiproject.org</p>
<p>sakaiproject.org">Sakai, <a href="https://moodle.org/" title="http://moodle.org/">Moodle</a>, <span class="removed_link" title="http://webct.com/">WebCT</span>, <a href="http://blackboard.com/" title="Object moved">Blackboard</a>, <a href="http://www.angellearning.com/" title="http://www.angellearning.com/">Angel</a> and <a href="http://Desire2Learn.com/" title="Document Moved">Desire2Learn</a>) ingest and present content in the course of teaching and learning. Digital objects come into the system, are combined and manipulated into packages of learning objects by instructors, and presented to learners as part of taking a course. Learners, in turn, create and ingest their own digital objects into the CLE as evidence of learning and are manipulated by instructors by annotation and/or grading.</p>
<p><strong>Electronic Portfolios</strong> (ePortfolio - <a href="http://www.osportfolio.org/" title="Home of Open Source Portfolio (OSP) - Home">OSPI</a> plus just about all of the CLE vendors) hold digital objects on behalf of learners and scholars that demonstrate that individual's competency for a particular field or skill. The digital objects can be a result from a learning experience in a CLE, a paper published in an ejournal, a research report submitted to an IR community, or come from a source not identified in this whitepaper. The portfolio's owner creates a presentation context for a selection of objects and grants access to selected groups.</p>
<h2>The Case for a Unified Repository</h2>
<p>Each of these systems - digital libraries, institutional repositories, electronic journals, collaborative learning environments, and electronic portfolios - is, at least in part, a repository of digital objects. Content (a digital object in the form of data and metadata) is added to the repository through a variety of ingestion workflows, manipulated by a variety of business tools, and expressed to repository users through a variety of presentation mechanisms. Internally to each system, metadata is usually distantly linked to its underlying object through numerous relational database tables or other schemes.</p>
<p>The content repository of each system can be viewed as a silo; content resident in the system is not easily accessible to other systems. In some cases, the content repository is closely linked to the ingestion and presentation functions of the system. In other systems, the linkage is not tightly bound making it possible to substitute alternate repository systems. In almost all cases, sharing content between silos usually involves words like "export/import" or "copy" or "migrate" - signaling a practice of content stored in multiple, unsynchronized locations in order to meet the needs of the workflow and presentation of the system surrounding each content silo.</p>
<p>But what if, beneath the facade of workflows, interfaces and business rules for each of these tasks, there was a single unified repository of all digital objects.</p>
<h2>Shared Objects</h2>
<p>At a fundamental level, objects placed in the repository via one system are visible to all of the other systems that use the same unified repository. An article ingested through the e-journal interface is available as evidence of a competency in an e-portfolio. From a video imported through the digital library interface a segment is described and annotated (and inserted back into the repository as a new object) for use as part of a learning object through the collaborative learning environment. A student submits a paper for evaluation to an instructor through a collaborative learning environment course and immediately that paper, and the resulting grading and commentary, is immediately visible as an object in the student's portfolio.</p>
<p>The recent unification of Sakai as a CLE and OSP as an ePortfolio platform is evidence of the evolution of thinking for single-repository/multiple-service systems.</p>
<h2>Shared Workflow</h2>
<p>Another immediate benefit of the unified repository concept is the generalization of tasks that promote efficiency through automation. For example, the process by which a paper submitted to a journal is reviewed by peers is similar to processes in dissertation defenses and promotion/tenure boards. An object - or a collection of objects in a portfolio combined into a single object following the Daniel <em>et al</em> model of "Distributed Active Relationships" - follows a process whereby reviewers submit comments and annotations on "an object" to a central point for aggregation, processing and reporting. In the case of a journal article, it is peer reviewers submitting comments to an editor. In the case of dissertation defenses and promotion/tenure boards, it is automation of the review of a candidates work by internal committee members and external referees. In all cases, the underlying digital objects remain immutable and are augmented by relationships to other objects representing annotations and other actions (subsequent publications, acceptance by defense committee, award of promotion or tenure).</p>
<h2>Preconditions to Ensure Success</h2>
<p>Such a unified repository model presupposes a number of factors. First, that it is possible to uniquely identify individuals and their roles in relationship to objects through the numerous interfaces atop the object repository. The foundation for this precondition exists with the Shibboleth federated identity management system.</p>
<p>Second, that it is possible to decouple the existing repository function from the workflow, business rule, and presentation layers of the underlying system (e.g. CLE, IR, ePortfolio). In most cases, it may be necessary for the unified repository to emulate the repository store and retrieve functions of the incumbent system.</p>
<h2>Conclusion</h2>
<p>Digital Objects are at the heart of the systems emerging on higher education campuses. These systems each employ repositories to hold objects used in accomplishing the goals of the system, but these repository silos are not efficient use of storage space and promulgate the problems of copying objects from system to system. A unified repository, on the other hand, promotes a single universe of digital objects enabled by a multifaceted network of relationships and metadata that allow each system to use any digital object to fulfill its needs. The end result is a seamless, efficient presentation of content available to learners and researchers through the system that best meets the users' needs.</p>
<p style="padding:0;margin:0">Modified to remove a link to http://www.umi.com/proquest/digitalcommons/.</p>
<p><</p>
<p>p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.cs.cornell.edu/lagoze/papers/ADL98/dar-adl.html to http://web.archive.org/web/20120617040554/http://www.cs.cornell.edu/lagoze/papers/ADL98/dar-adl.html on October 21st, 2013.</p>
