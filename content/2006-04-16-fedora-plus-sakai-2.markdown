---
layout: wordpress-import
status: published
published: true
title: 'Fedora plus Sakai &mdash; not quite that easy'
modified: 2006-04-16T12:08:57+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 42
wordpress_url: http://dltj.org/2006/04/fedora-plus-sakai-2/
date: '2006-04-16 08:08:57 -0400'
date_gmt: '2006-04-16 13:08:57 -0400'
category: Library Technology
categories:
- DRC
- Fedora
- Unified Content Repository
tags: []
comments: []
---
<p>In <a href="/article/fedora-plus-sakai/">previous post</a> I described to how easy it would be for Fedora to be integrated into Sakai and offered as reference the <a href="http://web.archive.org/web/20081122102007/http://cvs.sakaiproject.org/release/2.1.2/javadoc/org/sakaiproject/service/legacy/entity/Entity.html" title="Entity">Entity.java</a> interface as evidence.  Well, it isn't quite that easy.  Two big clues:</p>
<ol>
<li>It is in the "legacy" part of the source code tree; and</li>
<li>The interface has only getters (no setters).</li>
</ol>
<p>Pretty damning evidence.</p>
<p>I still haven't figured it all out yet, but there is this commentary in a document from last month with the title "<span class="removed_link" title="http://collab.sakaiproject.org/access/content/group/1118328820812-113628/Proposals/sakai_framework_proposal_reorg.pdf">The Sakai Framework: Proposal for Reorganization</span>":</p>
<blockquote>
<p>Entity Bus</p>
<p>This module provides support for treating the end-user-created data objects in Sakai, across all Sakai applications, as uniform "entities", for other applications to process them without API dependencies on the specific "entity producing" application.  An entity is an object with properties; property names come from a well know vocabulary; property values are either simple strings or references to other entities. </p>
<p>An Entity, and the service which produces them, the EntityProducer, can also declare that they have common characteristics, other than the ability to produce entities as objects with properties.  These are: </p>
<ul>
<li>URL able - the entity has a URL and will respond with an access request </li>
<li>... </li>
</ul>
</blockquote>
<p>All may not be lost -- there is mention in the document of a JDBC package:</p>
<blockquote>
<p>JDBC</p>
<p>This module adds support for direct and Hibernate access to back-end databases.  Connection pooling.  Hibernate stuff </p>
</blockquote>
<p>Certainly much harder to interface with, but I'm also appreciating more how powerful and complex the Sakai system is.  Perhaps Fedora integration would have to happen at the "module" level (whatever module would be dealing with digital objects -- I haven't found it yet).</p>
<p><</p>
<p>p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://collab.sakaiproject.org/access/content/group/1118328820812-113628/Proposals/sakai_framework_proposal_reorg.pdf.</p>
