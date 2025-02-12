---
layout: wordpress-import
status: published
published: true
title: 'Fedora plus Sakai: A view from 30,000 feet'
modified: 2006-04-30T00:55:16+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 48
wordpress_url: http://dltj.org/2006/04/fedora-plus-sakai-3/
date: '2006-04-29 20:55:16 -0400'
date_gmt: '2006-04-30 01:55:16 -0400'
category: Library Technology
categories:
- DRC
- Fedora
- Unified Content Repository
- Sakai
tags: []
comments:
- id: 45
  author: 'Confluence:  5th Sakai Conference, Vancouver, BC, Canada 30 May - 2 June
    2006 (Community Source Week)'
  author_email: ''
  author_url: http://confluence.sakaiproject.org/confluence/display/Conf2006Vancouver/Sakai+Repository+Integration
  date: '2006-04-30 12:24:05 -0400'
  date_gmt: '2006-04-30 16:24:05 -0400'
  content: "<strong>Sakai Repository Integration...</strong>\r\n\r\nThe Sakai Repository
    Integration BOF will look into issues surrounding the use of repository systems
    like Fedora as content storage for Sakai.    Documents   Fedora Plus Sakai: A
    view from 30,000 feet, Edited by Peter Murray..."
- id: 57
  author: 'Confluence: Project: Resources'
  author_email: ''
  author_url: http://confluence.sakaiproject.org/confluence/display/RES/Intersection+between+Sakai+and+Fedora
  date: '2006-05-03 14:23:10 -0400'
  date_gmt: '2006-05-03 18:23:10 -0400'
  content: "<strong>Intersection between Sakai and Fedora...</strong>\r\n\r\nEdited
    by Peter Murray, OhioLINK. This document represents a summary of comments on the
    Sakai Developers mailing list on April 2628, 2006 to a question..."
- id: 96
  author: 'Confluence: bSpace Images'
  author_email: ''
  author_url: http://confluence.media.berkeley.edu/confluence/display/BSPI/Fedora
  date: '2006-05-17 18:19:13 -0400'
  date_gmt: '2006-05-17 23:19:13 -0400'
  content: |-
    <strong>Fedora...</strong>

    Fedora Site Documentation...
- id: 198
  author: 'Confluence:  5th Sakai Conference, Vancouver, BC, Canada 30 May - 2 June
    2006 (Community Source Week)'
  author_email: ''
  author_url: http://confluence.sakaiproject.org/confluence/display/Conf2006Vancouver/Sakai+Repository+Integration+BOF
  date: '2006-05-22 14:13:12 -0400'
  date_gmt: '2006-05-22 18:13:12 -0400'
  content: "<strong>Sakai Repository Integration BOF...</strong>\r\n\r\nThe Sakai
    Repository Integration BOF will look into issues surrounding the use of repository
    systems like Fedora as content storage for Sakai.   A time of 3:30 pm on Thursday
    1 June is preferred.   Documents   Fedora Plus Sakai: A view from 30,......"
- id: 4649
  author: Sakai Repository Integration BOF - 5th Sakai Conference, Vancouver, BC,
    Canada 30 May - 2 June 2006 (Community Source Week) - Confluence
  author_email: ''
  author_url: http://issues.sakaiproject.org/confluence/display/Conf2006Vancouver/Sakai+Repository+Integration+BOF
  date: '2006-09-24 17:28:23 -0400'
  date_gmt: '2006-09-24 21:28:23 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Fedora Plus Sakai: A view from 30,000 feet,
    Edited by Peter Murray [...]<!--%kramer-ref-post%-->"
---
<div style="width: 100%; border: 1px solid black; background: #EEE; color: black; padding: 1em;">Please note:  the living, editable version of this document is now on <a href="http://confluence.sakaiproject.org//x/bYD9" title="http://confluence.sakaiproject.org//x/bYD9">Sakai's Confluence</a> in the "Resources" project area.
</div>
<p>Edited by Peter Murray, OhioLINK.  This document represents a summary of comments on the Sakai Developers mailing list on April 26-28, 2006 to <a href="http://article.gmane.org/gmane.comp.cms.sakai.devel/2779" target="_blank" title="Gmane -- Mail To News And Back Again">a question</a> posted by this document's editor regarding possible integration points between <a href="http://fedora.info/" title="301 Moved Permanently">Fedora</a> and <a href="https://www.sakaiproject.org/" title="Sakai Project - an Open Source suite of learning, portfolio, library and project tools | Sakai Project">Sakai</a>.  The resulting threads were:</p>
<ul>
<li><a href="http://thread.gmane.org/gmane.comp.cms.sakai.devel/2779/" title="Gmane Loom">Seeking status of 'Rep API' and 'JSR-170' shim from "Sakai Repository API Design"</a></li>
<li><a href="http://thread.gmane.org/gmane.comp.cms.sakai.devel/2813/" title="Gmane Loom">Repository integration with Sakai</a></li>
<li><a href="http://thread.gmane.org/gmane.comp.cms.sakai.devel/2870/" title="Gmane Loom">Fedora in Content Hosting - An Alternative</a></li>
</ul>
<p>The editor is indebted to the public and private responses of:  Ben Brophy, Ian Dolphin, Glenn Golden, Adam Hochman, Jeffrey Kahn, Beth Kirschner, Peter Knoop, Anoop Kumar, Jim Martino, Mark Norton, and Charles Severance.  Information from these individuals is supplemented by additional research by the editor, and the whole should not be viewed as a coherent or even advisable strategy.  Direct quotes in this summary are not attributed to individuals, and the editor alone is responsible for omissions and quotes-out-of-context errors.</p>
<p>The editor's question related to the integration of Sakai and Fedora.  OhioLINK's desire with the <a href="http://info.drc.ohiolink.edu/" title="DRC Home">Digital Resource Commons</a> is to build a unified content repository by meeting Sakai (and other tools such as OJS/DpubS for electronic journals, etc.) right where they store the data.  In doing so, it is our expectation that allowing data to flow across applications will be much easier because there is one underlying repository.</p>
<h2>Sakai Infrastructure</h2>
<h3>Description of ContentHostingService interface</h3>
<p>ContentHostingService is one of the "backbones" of Sakai.  To make Fedora the content repository (i.e. the attachment helper and resources tool, presentation tool, and any other tool using "content" in Sakai) then one must implement the ContentHostingService API.  The API is found in <a href="https://source.sakaiproject.org/svn/content/">https://source.sakaiproject.org/svn/content/</a> as <span class="removed_link" title="https://source.sakaiproject.org/svn/content/trunk/content-api/api/src/java/org/sakaiproject/content/api/ContentHostingService.java">org.sakaiproject.content.api.ContentHostingService </span> (<a href="http://source.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/service/legacy/content/ContentHostingService.html" title="http://cvs.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/service/legacy/content/ContentHostingService.html">JavaDoc</a>) and the baseline implementation can be found as <a href="http://source.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/component/legacy/content/BaseContentService.html" title="http://cvs.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/component/legacy/content/BaseContentService.html">BaseContentService</a>.</p>
<p>The ContentHostingService API supports WebDav, the AccessServlet, the WebServlet, Resources Tool, Presentation Tool, interoperates closely with Sakai's Authorization model, generates well-formed Sakai notifications, and real-time events, and is cluster aware and on and on.  This is a key API used heavily by Sakai; an alternative implementation probably needs to implement it completely to be of any use.</p>
<h3>Plugin Pattern</h3>
<p>Most current open-source repository systems cannot handle the on-line performance demands of a large-scale Sakai installation.  As an example, a Sakai installation supporting 500 users could easily store all of its resources in a separate repository.  But a system supporting 100,000 users may not be able to "outsource" all of its storage.</p>
<p>What is needed is a sophisticated set of plug-ins that allow great flexibility for different Sakai installations.  Instead of a complete re-write of the ContentHostingService interface, a plugin pattern that allows ContentHosting to precisely outsource things like blob storage and metadata storage with simpler APIs than ContentHosting and a very clean and simple API contract.  Then one can write plugins for things like Fedora, JSR-170, DSpace, iTunes, etc.</p>
<h3>Extend ContentCollection</h3>
<p>Suppose one were to extend the existing ContentHostingService, specifically the ContentCollection class (<a href="http://source.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/service/legacy/content/ContentCollection.html" title="ContentCollection">JavaDoc</a>) such that it serves as a gateway to a repository. It would need to represent the protocol to be used (Fedora, SRA, JSTOR, whatever) and likely include at least some support for digital rights management.</p>
<p>A simple idea with a lot of consequences, both easy and hard. On the plus side, repository-based collections could either be tied to a search pattern on the repository,or tied to a specific remote collection (including the root). Done right, it would integrate seamlessly into existing Sakai tools, such as the ResourceTool, etc. On the minus side, ContentResource might also be affected, since the tools would list content that is no longer directly accesible via the current implementation. WebDAV integration might also be challenging.</p>
<p>In the intial stages, this would have to be an optional feature that could be enabled or disabled since complete integration may not come quickly. Still, one could have an instance of the ResourceTool tied to a specific repository (not mixed) that could be billed as not supporting WebDAV or other regular content hosting features.</p>
<h3>ContentHostingService refactoring</h3>
<p>Ian Boston of Cambridge University reports development of a plugin into ContentHostingService that enables an implementing class, once it has registered itself with the ContentHostingService to be consulted if it 'owns' a node in the content hosting tree. Once it 'owns' the node, it takes responsibility for providing ContentResources for that node and all child nodes.</p>
<p>Cambridge has used this to implement an IMS Global Learning Consortium Content Packaging specification (<a href="http://www.imsglobal.org/content/packaging/" title="http://www.imsglobal.org/content/packaging/">IMS-CP</a>) plugin, that 'plays' IMS-CP files but one could just as easily use it to 'mount' a repository inside the ContentHostingService at an arbitrary position.</p>
<p>If the resource is read-only, or can't be accessed via DAV, then it is the responsibility of the plugin to act accordingly (ie, not return the content).<br />
Cambridge is also looking to write a plugin that 'interprets' an XML file loaded into resources to invoke a UI.  With Fedora, that XML file might be the connection settings to the repository.</p>
<p>Since the plugin patch is small (<50 lines), and the plugins can be implemented inside webapps (ie reloadable), Ian is hoping that it will be useful and can be included in the BaseContentService (<a href="http://source.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/component/legacy/content/BaseContentService.html" title="http://cvs.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/component/legacy/content/BaseContentService.html">JavaDoc</a>) for 2.2.  If it isn't, Cambridge will maintain it as a patch as it as they are going to be running it in production in July.  See <a href="http://bugs.sakaiproject.org/jira/browse/SAK-4457" title="302 Found">SAK-4457</a>.</p>
<h3>JSR-170 interface</h3>
<p><a href="http://www.jcp.org/en/jsr/detail?id=170" title="The Java Community Process(SM) Program - JSRs: Java Specification Requests - detail JSR# 170">JSR 170</a> is the Content Repository API for Java.  It specifies a standard API to access content repositories in Java independent of implementation.  (See also its follow-on: <a href="http://www.jcp.org/en/jsr/detail?id=283" title="The Java Community Process(SM) Program - JSRs: Java Specification Requests - detail JSR# 283">JSR 283</a> Content Repository API version 2.0).  Neither Fedora nor Sakai have JSR-170 interfaces, although if they did it could be a point of integration.  Implementation of JSR-170/283 would be a new implementation of the Sakai ContentHostingService API.</p>
<h3>AFS interface</h3>
<p>UC Davis people have home directories in AFS space, and their course management system also utilizes this space.  UC Davis has a <a href="https://ucdavis.jira.com/wiki/display/UCDSAKAI/Sakai+Data+Storage+-+Campus+Installations" title="http://webby.ucdavis.edu:8080/confluence/pages/viewpage.action?pageId=4549">problem statement</a> for integrating the user home directory AFS space into Sakai.</p>
<h2>Alternate Integration Points</h2>
<h3>OKI Repository OSID as a Sakai Tool/Service</h3>
<p>Sakai offers Repository integration through the O.K.I. Repository OSID.   The Repository OSID is used in a small (but perhaps growing) number of places in Sakai as a secondary interface to external repositories -- it does not go through the main ContentHostingService interface.  If this bridge were wide enough to include all the functionality Sakai needed, these calls could go through OKI.  (Additional information is on <a href="http://bugs.sakaiproject.org/confluence/pages/viewpage.action?spaceKey=SLIB&amp;title=O.K.I.+Repository+OSID" title="302 Found">confluence</a>, implementation is tracked as <a href="http://bugs.sakaiproject.org/jira/browse/SAK-2327" title="302 Found">SAK-2327</a>, and an example application is <span class="removed_link" title="https://twinpeaks.dev.java.net/">Twin Peaks</span>.)</p>
<p>One implements a set of interface methods that talk to your repository and then applications (one of which is Sakai) can search, retrieve, and upload content to your repository, subject to permissions.  Since the interface is standard (maintained by the IMS Global Learning Consortium), the calling application can use the same approach for all repositories. The caller is also insulated from connection, protocol, and some data format specifics.</p>
<p>The Fedora OKI Bridge under development by Anoop Kumar of Tufts for VUE release 1.5 (expected June 1, 2006) will support following:</p>
<ul>
<li>It will work with Fedora 2.0</li>
<li>It will provide read-only support.</li>
<li>It provides ability to perform simple and advanced search.</li>
<li>It will support three types of RecordStructure(OSID).</li>
<li>Dissemination RecordStructure holds all disseminations of object as its parts.</li>
<li>Image Record Structure will provide thumbnail, medium and high res images.</li>
<li>VUE Default Record Structure will provide a default view for digital object and dublin core metadata.</li>
</ul>
<p>Sakai may be able to use the bridge as is or we can add additional record structures to support Sakai's needs.</p>
<p>Sakai's Repository OSID is being considered as an <a href="http://wiki.dspace.org/SakaiIntegration" title="301 Moved Permanently">integration point with the DSpace</a> Institutional Repository application.</p>
<h3>UMichigan Fedora Tool</h3>
<p>Beth Kirschner at the University of Michigan is developing a Fedora repository interface for XSLT-driven CRUD operations against Fedora objects.  The current implementation is a prototype, supporting browse, search and editing capabilities. Authorization is not yet integrated with Sakai.  For more information, see: <a href="/assets/images/2006/04/README.txt">source.sakaiproject.org&mdash;README.txt</a>.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://bugs.sakaiproject.org/confluence/x/ikE to http://confluence.sakaiproject.org//x/bYD9.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to https://source.sakaiproject.org/svn/content/trunk/content-api/api/src/java/org/sakaiproject/content/api/ContentHostingService.java.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://webby.ucdavis.edu:8080/confluence/pages/viewpage.action?pageId=4549 to https://confluence.ucdavis.edu/confluence/pages/viewpage.action?pageId=4549.</p>
<p><</p>
<p>p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to https://twinpeaks.dev.java.net/ on June 9th, 2011.</p>
