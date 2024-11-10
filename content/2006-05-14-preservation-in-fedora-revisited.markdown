---
layout: wordpress-import
status: published
published: true
title: 'Fedora, Objects, Datastreams, Filesystems, and a Correction'
modified: 2006-05-14T12:35:00+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 54
wordpress_url: http://dltj.org/2006/05/preservation-in-fedora-revisited/
date: '2006-05-14 08:35:00 -0400'
date_gmt: '2006-05-14 13:35:00 -0400'
category: Library Technology
categories:
- Fedora
tags:
- Fedora Repository
comments:
- id: 79
  author: Ryan
  author_email: rscherle@indiana.edu
  author_url: ''
  date: '2006-05-15 10:09:57 -0400'
  date_gmt: '2006-05-15 15:09:57 -0400'
  content: It's probably too late now, but the 2.1.1 reindex utility should work just
    fine with the files and database structure of a 2.0 system...
- id: 5637
  author: "&tau;&epsilon;&chi;&nu;&omicron;&sigma;&omicron;&phi;&iota;&alpha; &raquo;
    The Jester&#8217;s Case for Fedora"
  author_email: ''
  author_url: http://www.lackoftalent.org/michael/blog/2006/05/02/the-jesters-case-for-fedora/
  date: '2006-10-11 07:27:07 -0400'
  date_gmt: '2006-10-11 11:27:07 -0400'
  content: "<!--%kramer-ref-pre%-->[...] For anyone reading Michael&#8217;s excellent
    summary, in the name of full disclosure I should point out that a piece of &#8220;Why
    Fedora? Because You Don&rsquo;t Need Fedora&#8221; had to be revisited with &#8220;Fedora,
    Objects, Datastreams, Filesystems, and a Correction&#8221;. The correction came
    after Michael posted his summary of the articles. Be sure to read both (the former
    will point you to the latter) to get the full picture. [...]<!--%kramer-ref-post%-->"
- id: 5638
  author: Sergio Berna
  author_email: sberna@gmail.com
  author_url: ''
  date: '2006-10-11 07:57:42 -0400'
  date_gmt: '2006-10-11 11:57:42 -0400'
  content: "Ryan has already pointed to the solution for your problem.\r\n\r\nNevertheless,
    we are currently working in a records preservation project in Spain using fedora
    and one of the features that we will try to implement is that the final AIP written
    to the HDD must be in <a href=\"http://sindbad.gsfc.nasa.gov/xfdu/\" title=\"XFDU
    standard page\" rel=\"nofollow\">XFDU</a> format (user selectable).\r\n\r\nIn
    this way we try to totally eliminate the techonological preservation risk involved
    in using only fedora tools for the archiving.\r\n\r\nAlthought it is true that
    you can rebuild the kowari triplestore index using fedora tools we also find it
    a high technological risk that seriously affects preservation policies.\r\n\r\nAnother
    point we are trying to cope with is the kowari triplestore dependency. Kowari
    is a good enough triplestore but the project is no longer under development. To
    do so we are also going to implement compatibility for both <a href=\"http://www.openrdf.org\"
    rel=\"nofollow\">Sesame</a> and <a href=\"http://jena.sourceforge.net/\" rel=\"nofollow\">Jena</a>."
- id: 5642
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-10-11 09:05:05 -0400'
  date_gmt: '2006-10-11 13:05:05 -0400'
  content: "Thanks, Sergio -- it would have worked...but look at everything I learned
    along the way.  Surely that is a silver lining to that dark cloud.  (I've got
    dark clouds on the brain today -- it is a cold, wet day in Columbus, Ohio.)\r\n\r\nI
    was not aware of the <a href=\"http://sindbad.gsfc.nasa.gov/xfdu/\" title=\"XFDU
    standard page\" rel=\"nofollow\" rel=\"nofollow\">XFDU</a> format until you mentioned
    it -- that looks pretty interesting!  Have you written up any documentation or
    whitepapers about the intersection of FEDORA with XFDU?  Also, I presume you are
    aware of the work of <a href=\"http://dca.tufts.edu/features/nhprc/\" rel=\"nofollow\">Tufts
    University and Yale University on the preservation of university records using
    FEDORA</a>.  I don't know how much that intersects with your work.\r\n\r\n[quote]\r\nIn
    this way we try to totally eliminate the techonological preservation risk involved
    in using only fedora tools for the archiving.\r\n[/quote]\r\n\r\nAgreed!\r\n\r\n[quote]Another
    point we are trying to cope with is the kowari triplestore dependency. Kowari
    is a good enough triplestore but the project is no longer under development. To
    do so we are also going to implement compatibility for both <a href=\"http://www.openrdf.org\"
    rel=\"nofollow\" rel=\"nofollow\">Sesame</a> and <a href=\"http://jena.sourceforge.net/\"
    rel=\"nofollow\" rel=\"nofollow\">Jena</a>.[/quote]\r\n\r\nThere has already been
    some work by Case Western Reserve University to use Oracle for the triplestore.
    \ At the moment, I can't remember it Case's work has been integrated into the
    FEDORA core developer's trunk, but at the very least the could be a level of abstraction
    that you could leverage to use other triplestores.  I've worked with the folks
    up at Case Western -- if you'd like, I could make an introduction."
- id: 5650
  author: Sergio Berna
  author_email: sberna@gmail.com
  author_url: ''
  date: '2006-10-11 12:25:14 -0400'
  date_gmt: '2006-10-11 16:25:14 -0400'
  content: "Thanks for the offer, it would be great.\r\n\r\nI had already seen the
    wonderful job done by Turfs and Yale university and have found it a valid description
    for the requirements of a trustworthy recordkeeping system. It intersects at some
    point with our work and we will be using several of their conclusions on the final
    system.\r\n\r\nI&rsquo;ll try to introduce the project scope as briefly as I can
    because it will be a very complex and long project.\r\n\r\nThe first thing is
    that it is a public institution funding project. With funding enough for 5 to
    7 senior programmers over a period of 11 months. The final goal of the project
    is to obtain a trustworthy record keeping system to be used in production by all
    the public institutions in a Spanish region named Catalonia.\r\n\r\nAs such the
    main users will be archiving people at public institutions in general such as
    city halls, councils, historical records institutions and so on.\r\n\r\nBriefly
    the main aspects of the project are:\r\n\r\n-Fedora as the core digital object
    repository\r\n-Global Object Identifier through URI\r\n-Digital Object Versioning
    Support\r\n-Support for Digital Objects containing several datastreams\r\n-Full
    text search support through abstraction API first using Google appliance\r\n-Package
    Ingestion support for METS, XFDU, MPEG-21 DIDL, FOXML\r\n-Package Dissemination
    support for METS, XFDU, MPEG-21 DIDL, FOXML\r\n-Full support for SPARQL queries\r\n-Package
    Archiving support for FOXML, XFDU\r\n-Support for Representation information using
    PREMIS [Object/Characteristics, Object/Environment], MIX , AES-X098B\r\n-Support
    for preservation using PREMIS [Event, Agent], Context preservation through RELS-EXT,
    RELS-INT\r\n-Object reference through DCMI\r\n-Security support using PREMIS [Object/Fixity]
    and XML Timestamps\r\n-Rights management through XACML\r\n-Automatic non-RDF ontology
    support through automatic crosswalks [ej. MARCS, MODS,MARCXML, EAD,&hellip;]\r\n-Identity
    federation through liberty alliance tickets\r\n-Ingestion interfaces using WEBDAV/DELTAV,
    SOAP, SFTP\r\n-Automatic validation of Digital Signatures, SIPS, metadata format
    and Antivirus support\r\n-Package dissemination support through WEBDAV, SOAP,
    HTTP REST\r\n-Metadata federation support for several archives (OAI-PMH)\r\n-Storage
    decoupling so that the AIP might be stored in HDD, WORM, etc.\r\n-Digital Signature
    Preservation through automatic evidence recollection at ingestion (CRL, timestamp,
    etc), including re-signing policies\r\n-Integrity support through incremental
    signature policies\r\n-Complete representation knowledge base including algorithms,
    software, operating systems and available emulation software\r\n-Support for automatic
    format migration among several formats, word, pdf, odf, ..\r\n-Support for record
    expiring policies\r\n-Support for offline data\r\n-Auditing support\r\n-Full HTML
    administration and preservation interfaces\r\n\r\nAnd many more that either are
    not important enough or I might have missed. Sorry for not tagging accordingly
    all the references but there are simply too many.\r\n\r\nAs you can see many of
    these features are already supported by fedora. But there are many areas that
    are either out of fedora scope or simply not implemented.\r\n\r\nOur intention
    is to release all the generated code under a compatible license such as the one
    fedora has. And to revert back to fedora community all the code they wish to have
    either in the core or as tools.\r\n\r\nAs such any collaboration is always welcomed."
---
<p>In an <a href="/article/why-fedora-because-you-dont-need-fedora/">earlier post</a>, I extolled the virtues of Fedora as an ideal candidate for digital preservation because "[a]ll of the metadata (descriptive, preservation, and relationship to other objects) and managed datastreams that make up a digital object are 'serialized' to a single XML file on a file system."  Well, as I found out last week, it isn't quite that straight forward.</p>
<p>Last week we had a problem with Fedora running on our production server -- it had locked up tight in a wait-state for some sort of disk I/O and not even a `kill -9` could get rid of it.  So I rebooted the server.  Then the Fedora service wouldn't start again -- it complained about corruption in the Kowari triplestore.  Okay, so we'd have to blow away the Kowari database and the MySQL database and reload.</p>
<p>Now I can only imagine that readers who are familiar with the Fedora software are yelling "what version of Fedora were you using?!?"  Well, unfortunately it was 2.0.  (And those that know are probably groaning.)  For everyone else &mdash; and I used to be in that category &mdash; the consensus might be, "well, simply reload the objects off the disk," right?  So here's the kicker:</p>
<div style="margin-left: 2em; font-variant: small-caps;">
the storage format of the objects on disk isn't really a single serialized XML file.
</div>
<p><i>Gasp!</i>  Yep, that's right.  As it turns out, the framework of the object is stored as a single XML (METS-like..."FOXML" to be exact) file in the "objects" directory and each of that object's datastreams is stored as a single binary file in the "datastreams" directory.  (Or, to be completely accurate, the "objects" and "datastreams" directories are further subdivided in to a year, month-day, hour and minute directory structure.)  The FOXML markup refers to a file with type "reference":</p>
```xml
    <foxml:datastream ID="DS1" STATE="A" CONTROL_GROUP="M" VERSIONABLE="true">
        <foxml:datastreamVersion ID="DS1.0" LABEL="DSCN0349" CREATED="2006-03-20T20:58:54.352Z" MIMETYPE="image/jpeg" SIZE="0">
            <foxml:contentLocation TYPE="INTERNAL_ID" REF="peter:4+DS1+DS1.0" />
        </foxml:datastreamVersion>
    </foxml:datastream>
```
<p>This is a sample piece of a FOXML file for a digital object in FEDORA.  In summary, this snippet defines a datastream called "DS1" with the label "DSCN0349" that is a JPEG file managed by the FEDORA server.  The inner-most tag is a contentLocation with the type "INTERNAL_ID" and a reference attribute of "peter:4+DS1+DS1.0".  That reference corresponds exactly to a file name in the "datastreams" directory (with the exact subdivided directory structure as the "objects" directory) that is the datastream itself.</p>
<p>So what happened with the server restore?  I thought I could just point the automated ingestion utility at the 'objects' directory and have them all sucked back into the repository.  What happened, though, was a whole bunch of errors like "invalid location" and "no objects loaded" because, of course, the batch loader couldn't resolve the datastream locations.</p>
<p>(By the way, the reason this isn't so much an issue in v2.1b and beyond is that the core developers added a reindexing tool that can walk the 'objects' and 'datastreams' hierarchies in order to rebuild the triplestore and SQL databases.  The FEDORA process itself, of course, must be stopped while this kind of bulk rebuild is happening.  What we ended up doing was jumping to version 2.1.1 faster than we had planned so we could make use of the reindexing tool.)</p>
<p>This division between the 'objects' and 'datastreams' directories means the preservation benefits are not as straight forward as I had originally thought.  There isn't one XML file that represents the entire object &mdash; rather there is an XML file that has structure, some metadata and opaque (albeit easily decoded) references to files elsewhere in the file system.  This makes me think about changing our backup scheme to use a utility that will put together the XML framework with the datastream file(s) before that whole combination is written to off-line storage.  Doing so would make me much more comfortable about the prospects for recovery at a later date.</p>
