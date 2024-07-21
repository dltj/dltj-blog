---
layout: wordpress-import
status: publish
published: true
title: '"Archiving and Preserving the Web" from the Internet Archive perspective'
modified: 2006-04-20T16:03:21+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 44
wordpress_url: http://dltj.org/2006/04/archive-it/
date: '2006-04-20 12:03:21 -0400'
date_gmt: '2006-04-20 17:03:21 -0400'
categories:
- Economies of Scale
- Unified Content Repository
tags: []
comments: []
---
<p>In case you were wondering what some of the back-channel discussion on the #code4lib IRC channel was on Tuesday, Ed Summers and I were watching an EDUCAUSE webcast on the <a href="http://archive.org/" title="302 Found">Internet Archive</a>'s <a href="http://www.archive-it.org/" title="Archive-It.org">Archive-It</a> project.  Archive-It is a subscription service that allows institutions to crawl and search their own web archive through a web application.  On Tuesday, <a href="http://www.educause.edu/library/resources/archiving-and-preserving-web" title="Page Not Found | EDUCAUSE">the EDUCAUSE Live!</a> webcast included the project manager and Senior Crawl Engineer (what a title!) from the Internet Archive to talk about not only the server, but the <a href="http://crawler.archive.org/" title="Heritrix - Home Page">open source web crawler</a> and <a href="http://archive-access.sourceforge.net/" title="nutchwax -<br />
    Home Page">ARC access tools</a> (copied from the project home page):</p>
<ul>
<li>Tom Emerson's <a href="http://libarc.cvs.sourceforge.net/viewvc/libarc/libarc/" class="externalLink" title="External Link">libarc</a>,<br />
           "A C++ library for processing Internet Archive ARC, CDX, and DAT<br />
           files." This project used to reside at<br />
            <a href="http://sourceforge.net/projects/libarc/" class="externalLink" title="External Link">libarc home<br />
            page</a> but was moved here, 09/14/2004.  See the<br />
            <a href="http://libarc.cvs.sourceforge.net/viewvc/libarc/libarc/README?revision=1.5" class="externalLink" title="External Link">README</a>.</li>
<li><a href="http://archive-access.sourceforge.net/projects/nutch" title="301 Moved Permanently">NutchWAX</a> is<br />
              Web Archive Collection Search based on<br />
              <span class="removed_link" title="http://nutch.org">Nutch</span>.
            </li>
<li><a href="http://archive-access.sourceforge.net/projects/infiniteurl" title="301 Moved Permanently">infiniteurl</a> is an<br />
            infinite source of pages used testing crawlers.
            </li>
<li><a href="http://archive-access.cvs.sourceforge.net/viewvc/archive-access/archive-access/projects/hedaern/" class="externalLink" title="External Link">Hedaern</a>, an ARC<br />
            'access' tool, puts up a WebUI that allows URL+timestamp<br />
            lookups and full-text searching of ARCs.  Hedaern is currently<br />
            'alpha' and is LGPL. It is written in python -- it includes python<br />
            ARC reader/writers -- and was donated by Mark Williamson of the<br />
            British Library. To learn more about Hedaern, start with the<br />
            <a href="http://archive-access.cvs.sourceforge.net/viewvc/archive-access/archive-access/projects/hedaern/docs/guide.pdf?revision=1.1" class="externalLink" title="External Link">guide</a>.</li>
<li>
            <a href="http://archive-access.sourceforge.net/projects/wera/" title="wera -<br />
    Home Page">wera</a> is an archive <i>viewer</i></p>
<p>            application that gives an Internet Archive Wayback Machine-like<br />
            access to web archive collections. Wera is a php5 application based<br />
            on -- and replaces --<br />
            the <span class="removed_link" title="http://nwa.nb.no/">NwaToolset</span>. Currently wera<br />
            uses <a href="http://archive-access.sourceforge.net/projects/nutch" title="301 Moved Permanently">NutchWAX</a> as its search engine<br />
            core and the ARCRetriever webpp (included) fetching records from<br />
            ARCs.
            </li>
<li><a href="http://archive-access.sourceforge.net/projects/wayback" title="301 Moved Permanently">wayback</a> is an open-source<br />
            version of the Internet Archive Wayback Machine.  <em>[As an aside, one of the presenters said that this was a pretty old version and that they were looking to update it soon to bring the open source version more in line with the archive.org "live" version.]</em></li>
<li><a href="http://archive-access.sourceforge.net/projects/waxtoolbar" title="301 Moved Permanently">WAXToolbar</a> is a firefox<br />
            extension for browsing Web Archives.</li>
</ul>
<p>The archive of the EDUCAUSE Live! webcast is open to viewing by anyone.  The presenter's PowerPoints and instructions on how to view the webcast archive can be found at <a href="http://www.educause.edu/library/resources/archiving-and-preserving-web" title="Page Not Found | EDUCAUSE">http://www.educause.edu/content.asp?SECTION_ID=201&bhcp=1</a>.  The presentation abstract is included below:</p>
<blockquote><p>
Libraries and archives have long collected information to serve scholars in understanding history, culture, and society. Today, Web pages have replaced newsletters; blogs have supplanted diaries; and many government forms and documents are more readily accessible on the Web than in paper form. As part of an effort to appropriately document and capture today's information for tomorrow's use, institutions must adopt a Web archiving strategy. Fortunately, Archive-It takes much of the burden out of the task. Archive-It is a Web application uniquely designed for the needs of university and government institutions interested in preserving Web content. The application allows organizations with limited infrastructure and technical staff to collect, catalog, search, and manage archived Web content through a Web interface. Built on open source components by the Internet Archive and the International Internet Preservation Consortium, Archive-It creates and stores the ARC files that are the standard format for Web archiving. In this presentation, two representatives from the Internet Archive will discuss the Archive-It project.
</p></blockquote>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://cvs.sourceforge.net/viewcvs.py/archive-access/archive-access/projects/libarc/LOCAL_README.txt?rev=1 to http://libarc.cvs.sourceforge.net/viewvc/libarc/libarc/README?revision=1.5.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://cvs.sourceforge.net/viewcvs.py/archive-access/archive-access/projects/libarc/ to http://libarc.cvs.sourceforge.net/viewvc/libarc/libarc/.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://cvs.sourceforge.net/viewcvs.py/archive-access/archive-access/projects/hedaern/ to http://archive-access.cvs.sourceforge.net/viewvc/archive-access/archive-access/projects/hedaern/.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://cvs.sourceforge.net/viewcvs.py/archive-access/archive-access/projects/hedaern/docs/guide.pdf?rev=1 to http://archive-access.cvs.sourceforge.net/viewvc/archive-access/archive-access/projects/hedaern/docs/guide.pdf?revision=1.1.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://nwa.nb.no/ on December 31st, 2010.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://nutch.org on December 31st, 2010.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.educause.edu/content.asp?SECTION_ID=201&bhcp=1 to http://www.educause.edu/library/resources/archiving-and-preserving-web on August 22nd, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.educause.edu/content.asp?SECTION_ID=201&bhcp=1 to http://www.educause.edu/library/resources/archiving-and-preserving-web on August 22nd, 2012.</p>
