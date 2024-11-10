---
layout: wordpress-import
status: published
published: true
title: 'Presentation Summary: "MPTStore: Implementing a fast, scalable, and stable RDBMS-backed triplestore for Fedora and the NSDL"'
modified: 2007-01-29T19:03:09+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 176
wordpress_url: http://dltj.org/2007/01/fedora-mptstore/
date: '2007-01-29 14:03:09 -0500'
date_gmt: '2007-01-29 19:03:09 -0500'
category: Library Technology
categories:
- Fedora
- Meeting
- Raw Technology
tags:
- National Science Digital Library
- icor2007
- RDF
- programming
- semantic web
- Fedora Repository
comments:
- id: 11958
  author: NSDL Road Reports &raquo; Blog Archive &raquo; NSDL Presentations at Open
    Repositories 2007
  author_email: ''
  author_url: ''
  date: '2007-02-01 14:32:50 -0500'
  date_gmt: '2007-02-01 19:32:50 -0500'
  content: "[...] Wilper, Birkland, MPT Store: A Fast, Scalable, and Stable Resource
    Index http://dltj.org/2007/01/fedora-mptstore/ [...]"
- id: 13534
  author: Kingsley Idehen
  author_email: kidehen@openlinksw.com
  author_url: http://www.openlinksw.com/blog/~kidehen
  date: '2007-03-29 10:09:02 -0400'
  date_gmt: '2007-03-29 15:09:02 -0400'
  content: "Hi There, \r\n\r\nWould you be happy to repeat these experiments using
    Virtuoso (see: http://sourceforge.net/projects/virtuoso ). \r\n\r\nNote: Virtuoso
    is a High-Performance DBMS for both SQL and RDF (in-built Quad Store). It also
    has its own in-built Full Text Indexing. It is optimized at all levels. We also
    control the SQL compiler so we are able to optimize specifically for SPARQL inside
    the SQL Compiler.\r\n\r\nVirtuoso current hosts: http://dbpedia.org amongst other
    large Triple Store projects.\r\n\r\nLet's do some testing etc.."
- id: 13536
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2007-03-29 10:55:32 -0400'
  date_gmt: '2007-03-29 15:55:32 -0400'
  content: "Kingsley &mdash;\r\n\r\nIn this case, I'm just the reporter of someone
    else's work.  I don't know if the Fedora core developers or the NSDL development
    team considered Virtuoso, but I will pass along your comment to them in case you
    have not contacted them directly."
- id: 13541
  author: More News
  author_email: ''
  author_url: http://morenews.blogspot.com/2007/03/mptstore.html
  date: '2007-03-29 13:14:34 -0400'
  date_gmt: '2007-03-29 18:14:34 -0400'
  content: "<!--%kramer-ref-pre%-->[...] MPTStore  Presentation Summary on MPTStore.
    A summary of an interesting approach by the Fedora guys to storing lots of triples,
    fast.The real motivation behind experimenting with a new triplestore, however,
    was the NSDL use case. The National Science Digital Library5 (NSDL) is a moderately
    large repository (4.7 million objects, 250 million triples) with a lot of write
    activity (driven by periodic OAI harvests; primarily mixed ingests and datastream
    modifications). The NSDL data model also includes existential/referential integrity
    constraints that must be enforced. Querying the RI to determine correct repository
    state proved to be difficult: Kowari is aggressively buffering triple, sometimes
    on the order of seconds, before writing them to disk. Flushing the buffer after
    every write is also computationally expensive (hence the drive to use buffers
    in the first place).Based on this observation, their solution, called &ldquo;Mapped
    Predicate Tables,&rdquo; creates a table for every predicate in the triplestore.
    This has several advantages: a low computational cost for triple adds and deletes,
    queries for known predicates are fast, complex queries benefit from the relatively
    mature RDBMS planner having finer-granularity statistics and query plans, and
    flexible data partitioning to help address scalability. This solution comes with
    several disadvantages, however: one needs to manage predicate to table mapping,
    complex queries crossing many predicates require more effort to formulate, and
    with a naive approach simple unbound queries scale linearly with the number of
    predicates.They achieved basically the same performance either asynchronous or
    synchronous modification.The project is available on Sourceforge, including slides
    and javadoc (which has a similar design to JRDF except no blank nodes).Labels:
    rdf, triple store [...]<!--%kramer-ref-post%-->"
---
<p>Chris Wilper gave this presentation on behalf of the work that he and Aaron Birkland did to improve the performance of the Fedora Resource Index.  </p>
<div style="margin-left: 5em;">
<object type="application/x-shockwave-flash" data="https://s3.amazonaws.com:443/slideshare/ssplayer.swf?id=20618&#038;doc=mptstore-a-fast-scalable-and-stable-resource-index-1484" width="425" height="348"><param name="movie" value="https://s3.amazonaws.com:443/slideshare/ssplayer.swf?id=20618&#038;doc=mptstore-a-fast-scalable-and-stable-resource-index-1484" /></object><br />
<span style="font-size: 85%"><a href="http://www.slideshare.net/cwilper/mptstore-a-fast-scalable-and-stable-resource-index" title="MPTStore: A Fast, Scalable, and Stable Resource Index &amp;raquo; Slideshare">Presentation slides via SlideShare</a></span>
</div>
<p>Version 2.0 of the <a href="http://www.fedora.info/" title="Fedora">Fedora digital object repository software</a> added a feature called the Resource Index (RI).  Based on <a href="http://www.w3.org/RDF/" title="http://www.w3.org/RDF/">Resource Description Framework</a> (RDF) triples, the RI provided quick access to relationships between objects as well as to the descriptive elements of the object itself.  After about two years of use using the <a href="http://www.kowari.org/" title="kowari">Kowari software</a>, the RI has pointed to a number of challenges for "triplestores":  scalability (few triplestores are designed for greater than 100 million triples); performance; and stability (frequent "rebuilds").</p>
<p>The real motivation behind experimenting with a new triplestore, however, was the NSDL use case.  The <a href="http://nsdl.org/" title="The National Science Digital Library">National Science Digital Library</a> (NSDL) is a moderately large repository (4.7 million objects, 250 million triples) with a lot of write activity (driven by periodic OAI harvests; primarily mixed ingests and datastream modifications).  The NSDL data model also includes existential/referential integrity constraints that must be enforced.  Querying the RI to determine correct repository state proved to be difficult:  Kowari is aggressively buffering triple, sometimes on the order of seconds, before writing them to disk.  Flushing the buffer after every write is also computationally expensive (hence the drive to use buffers in the first place).</p>
<p>The NSDL team also encountered corruption under concurrent use and with abnormal shutdowns, forcing the rebuild of the triplestore.  And the solution was not scaling well; performance was becoming notably worse.  In looking for solutions other triplestores were considered but rejected.  Using a RDBMS seemed attractive --  efficient transactions, very stable, generally speedy -- but a "one big table" paradigm to store all of the relations did not seem to give them a desired scalability.</p>
<p>NSDL developers observed that total number of distinct predicates is much lower than the number of predicates or objects;  NSDL has about 50 distinct predicates.  Based on this observation, their solution, called "Mapped Predicate Tables," creates a table for every predicate in the triplestore.  This has several advantages:  a low computational cost for triple adds and deletes, queries for known predicates are fast, complex queries benefit from the relatively mature RDBMS planner having finer-granularity statistics and query plans, and flexible data partitioning to help address scalability.  This solution comes with several disadvantages, however:  one needs to manage predicate to table mapping, complex queries crossing many predicates require more effort to formulate, and with a naive approach simple unbound queries scale linearly with the number of predicates.</p>
<p>So the NSDL team created the <a href="http://mptstore.sourceforge.net/" title="MPTStore 0.9.1 Documentation">MPTStore triplestore</a> and contributed it back to the Fedora core developers for use by the community.  MPTStore is a Java library that handles all of the predicate mapping and accounting behind the scenes.  The basic API remains the same as for other triplestores, performing triple writes and queries, and the library hides all of the implementation details of translating queries from a particular language (SPO, SPARQL) into SQL statements.  The library is also designed to expose transaction/connection semantics should the developer wish to have direct access to the predicate tables.</p>
<p>A solution like MPTStore is well suited for NSDL use case.  The NSDL team was very familiar with the operations of RDBMS administration: performance tuning, backups, etc.  The stored triplestore data is transparent and "hackable" -- adhoc SQL queries and analysis are relatively simple.  In fact, the RDBMS triplestore helped track down Fedora middleware bugs that resulted in an inconsistent state.  Fixing these bugs also improved the performance of the Kowari-based RI.</p>
<p>[Updated 20070129T1447 to include links to Chris' presentation on SlideShare.]</p>
