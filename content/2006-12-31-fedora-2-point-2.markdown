---
layout: wordpress-import
status: published
published: true
title: 'Looking Forward to Version 2.2 of FEDORA'
modified: 2007-01-01T01:46:39+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 165
wordpress_url: http://dltj.org/2006/12/fedora-2-point-2/
date: '2006-12-31 20:46:39 -0500'
date_gmt: '2007-01-01 01:46:39 -0500'
category: Library Technology
categories:
- DRC
- Fedora
tags:
- DRC
- library service-oriented architecture
- icor2007
- java
- jboss
- open source
- Fedora Repository
comments:
- id: 10196
  author: John Fink
  author_email: jbfink@lib.muohio.edu
  author_url: http://libgrunt.blogspot.com
  date: '2006-12-31 21:59:02 -0500'
  date_gmt: '2007-01-01 02:59:02 -0500'
  content: Wow, sounds great.  I have a very little experience with DSpace but have
    never messed about with Fedora -- I've had terrible luck with Java-based apps
    but maybe I'll fool around with this to see if anything happens.
- id: 11159
  author: pintiniblog
  author_email: ''
  author_url: http://pintini.blogspirit.com
  date: '2007-01-04 18:54:40 -0500'
  date_gmt: '2007-01-04 18:54:40 -0500'
  content: "<!--%kramer-pre%--> Fedora v2.2   S. Payette a annonc&eacute; la version
    2.2 de Fedora pour la mi-janvier.    Plus de d&eacute;tails sur Disruptive Library
    Technology Jester   12:12 Publi&eacute; dans D&eacute;p&ocirc;ts institutionnels
    | <!--%kramer-post%-->"
---
<p><a href="http://www.cs.cornell.edu/payette" title="Sandy Payette&#039;s homepage">Sandy Payette</a>, Co-Director of the Fedora Project and Researcher in the Cornell Information Science department, <a href="http://article.gmane.org/gmane.comp.cms.fedora-commons.user/2330/" title="Posting to the Fedora-Users mailing list by Sandy Payette with the subject &#039;Release Date for Fedora 2.2&#039; dated Fri, Dec 22, 2006 at 15:25:56 EST"> announced a tentative date for the release 2.2 of the FEDORA</a> digital object repository.</p>
<blockquote><p>
The Fedora development team would like to announce that Fedora 2.2 will be released on Friday, January 19, 2007.   </p>
<p>This new release will contain many significant new features and enhancements, including <i>[numbers added to the original for the sake of subsequent commentary]</i>:</p>
<ol>
<li>Fedora repository is now a web application (.war) that can be installed in any container</li>
<li>Fedora authentication has been refactored to use servlet filters (no longer Tomcat realms)</li>
<li>A new Fedora installer makes it easy to get started with Fedora (with both "quick" and "custom" install options)</li>
<li>GSearch service (backed by Lucene or Zebra) - flexible, configurable, indexes any datastream</li>
<li>Journaling service to create a backup/mirror repository</li>
<li>New checksum features for datastreams</li>
<li>Support for Postgres database configuration</li>
<li>Standard system logging with Log4J</li>
<li>Over 40 bug fixes</li>
<li>Many other enhancements</li>
</ol>
<p>Be on the lookout for the release announcement the new year!   Also, there will be opportunities to talk with the Fedora development team at Open Repositories 2007 (<a href="http://openrepositories.org/" title="Open Repositories 2007 homepage">http://openrepositories.org/</a>).
</p></blockquote>
<p>This is great news and a major step forward for the project.  Here are some reasons why I think this is true.</p>
<h2>1. Fedora repository is now a web application (.war)</h2>
<p>To this point, the FEDORA repository application distribution has been pre-bundled inside a Tomcat Java servlet container.  The binding has been pretty tight with certain dependencies written into the Tomcat configuration itself.  That made it very difficult to install FEDORA into an organization's existing servlet container (be it another installation of Tomcat or Jetty/JBoss/Glassfish, etc.).  Even more problematic, there were reports of problems trying to get JSP-based applications to work inside the FEDORA-supplied container (we ran into this ourselves) meaning that organizations wanting to run both FEDORA and another servlet-based application needed to run <i>two</i> servlet containers; pretty inefficient.  (OhioLINK was in this position in its early implementations of the <a href="http://info.drc.ohiolink.edu/" title="Ohio Digital Resource Commons home page">Ohio DRC</a> project.)</p>
<p>With release 2.2, the core developers have effectively turned the software distribution inside out.  The primary output of the new build process is a standard <b>W</b>eb <b>AR</b>chive (or <b>WAR</b>) file that can be put inside any servlet container.  The new installation program (see #3 below) comes with a Tomcat distribution, should a new installation need it, but it is no longer required.  There have been reports that the new WAR-based distribution works inside the Jetty servlet container; we're hoping it will work in the JBoss Application Server as well (<a href="/article/java-framework/">since that is what we're using to build our next generation interface</a>).</p>
<h2>2. Fedora authentication has been refactored to use servlet filters</h2>
<p>I'm not quite sure what this means, but I have hopes that it will make integration with <a href="http://shibboleth.internet2.edu/" title="Project Shibboleth home page">Shibboleth</a> easier.  Can anyone else see the path between FEDORA and Shibboleth and comment on it?</p>
<h2>3. A new Fedora installer makes it easy to get started with Fedora</h2>
<p>From the start, FEDORA required a Java servlet container in order to run.  To make the installation job easier for those that are not familiar with Java servlet containers, the FEDORA installation process did everything for you.  Now that the relationship between the FEDORA application and the servlet container have been flipped around (see #1 above), the core developers devised an easy-to-use installation application that mimics the simplicity of the previous installation style while allowing others to make use of FEDORA as an integrated application within an existing servlet container.</p>
<h2>4. GSearch service</h2>
<p>The original FEDORA search service, the appropriately-named "basic search," indexes only the Dublin Core (DC) datastream of each object.  As has been mentioned on the Fedora-Users mailing list several times, the DC datastream is really meant as an administrative metadata datastream and not necessarily the full description of the object; <a href="/article/description-datastream/">that full description can be stored in other datastreams of a FEDORA object</a>.  Not only did basic search not index these other descriptive metadata streams, but it also wouldn't index the full text of PDF, text, and other indexable datastreams.</p>
<p><span class="removed_link" title="http://defxws2006.cvt.dk/fedoragsearch/">GSearch</span> &mdash; where "G" stands for "General" but could equally well stand for "Gert" Schmeltz Pedersen, its lead developer from the Technical University of Denmark &mdash; does all of the above as a new component in the FEDORA Service Framework.  We extend our gratitude to Gert and his colleagues for contributing their work to the general FEDORA distribution as well as to <a href="http://www.deff.dk/" title="Danmarks Elektroniske Fag- og Forskningsbibliotek">DEFF, Denmark's Electronic Research Library</a>, which funded the GSearch project.</p>
<h2>5. Journaling service</h2>
<p>Like a journaling file system or a journaling database, this capability allows one to capture all of the transactions applied to the repository and replay them against a secondary repository instance or to restore a repository from backup.</p>
<h2>6. Datastream checksums</h2>
<p>As part of its ingestion and maintenance functions, the FEDORA software can now calculate, store, and verify checksums of datastreams.  This helps ensure the integrity of the repository content, or at least detect when something goes wrong.</p>
<h2>7. Support for PostgreSQL</h2>
<p>In the battle between which relational database engine is best, FEDORA now supports most of the big ones out-of-the-box:  Oracle, MySQL, and new PostgreSQL.  Here at OhioLINK, we've started with MySQL but are considering a migration to PostgreSQL as our in-house, preferred RDBMS, so the timing of this announcement is great.</p>
<h2>8. Standard system logging with Log4J</h2>
<p>Put this one in the category of "playing nicely with others."  We've already reaped the benefit of the refactored logging code in the client JAR file in a pre-release version of the code.</p>
<h2>9 and 10.  Bug fixes and many other enhancements</h2>
<p>The core code is evolving along a nice trajectory.  This is good to see for the health of the overall project!</p>
<p>Version 2.2 represents another monumental step towards the vision of a <b>F</b>lexible, <b>E</b>xtensible <b>D</b>igital <b>O</b>bject <b>R</b>epository <b>A</b>rchitecture.  Congratulations to the core developers for what sounds like is going to be a great release.
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://comm.nsdl.org/pipermail/fedora-users/2006-December/002330.html to http://article.gmane.org/gmane.comp.cms.fedora-commons.user/2330/ on January 19th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://defxws2006.cvt.dk/fedoragsearch/ on January 19th, 2011.</p>
