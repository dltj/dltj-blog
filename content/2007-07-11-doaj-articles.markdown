---
layout: wordpress-import
status: published
published: true
title: 'Article-Level OAI-PMH Harvest Available from DOAJ'
modified: 2007-07-11T20:51:54+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 261
wordpress_url: http://dltj.org/2007/07/doaj-articles/
date: '2007-07-11 16:51:54 -0400'
date_gmt: '2007-07-11 20:51:54 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- description
- ejournal
- open access
- oai-pmh
- Directory of Open Access Journals
comments:
- id: 18985
  author: eFoundations
  author_email: ''
  author_url: http://efoundations.typepad.com/efoundations/2007/07/journal-article.html
  date: '2007-07-12 09:09:08 -0400'
  date_gmt: '2007-07-12 13:09:08 -0400'
  content: |-
    <strong>Journal articles, metadata formats and woes...</strong>

    In a post on his Digital Library Technology Jester weblog, Peter Murray of OhioLINK points to an XML format developed by the Directory of Open Access Journals (DOAJ) for representing descriptions of journal articles. First, I think I'd qualify Peter'...
- id: 18986
  author: Eric Lease Morgan
  author_email: emorgan@nd.edu
  author_url: ''
  date: '2007-07-12 09:16:00 -0400'
  date_gmt: '2007-07-12 13:16:00 -0400'
  content: "Yep, kudos to DOAJ.\r\n\r\nI saw this a week or two ago, and while I did
    not take advantage of their article-specific metadata scheme, I did use the Dublin
    Core metadata scheme to harvest about 54,000 of the articles and save them into
    a MyLibrary instance. I then used an indexer called Kinosearch to make them searchable.
    Finally I created a rudimentary searchable/browsable interface to the whole thing.
    See:\r\n\r\n<blockquote><span class=\"removed_link\" title=\"http://dewey.library.nd.edu/mylibrary/demos/article-index/\">http://dewey.library.nd.edu/mylibrary/demos/article-index/</span></blockquote>\r\n\r\nAh,
    the possibilities are almost endless!\r\n\r\n--\r\nEric Lease Morgan\r\nUniversity
    Libraries of Notre Dame\r\n<p style=\"padding:0;margin:0;font-style:italic;\">The
    text was modified to update a link from //dewey.library.nd.edu/mylibrary/demos/article-index/
    to http://dewey.library.nd.edu/mylibrary/demos/article-index/ on December 30th,
    2010.</p><p style=\"padding:0;margin:0;font-style:italic;\" class=\"removed_link\">The
    text was modified to remove a link to http://dewey.library.nd.edu/mylibrary/demos/article-index/
    on May 17th, 2011.</p>"
- id: 19005
  author: Peter Suber, Open Access News
  author_email: ''
  author_url: http://www.earlham.edu/~peters/fos/2007_07_08_fosblogarchive.html
  date: '2007-07-12 19:21:46 -0400'
  date_gmt: '2007-07-12 23:21:46 -0400'
  content: "<!--%kramer-ref-pre%-->[...] articles for local repositories through the
    DOAJ   Article-Level OAI-PMH Harvest Available from DOAJ, Disruptive Technology
    Library Jester,&nbsp;July 11, 2007.&nbsp; [...]<!--%kramer-ref-post%-->"
- id: 19071
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2007-07-13 21:26:34 -0400'
  date_gmt: '2007-07-14 01:26:34 -0400'
  content: Neat, Eric!  Thanks for posting the demo link.  Another great idea for
    the feed...
- id: 19096
  author: K.G. Schneider
  author_email: kgs@freerangelibrarian.com
  author_url: http://freerangelibrarian.com
  date: '2007-07-14 11:36:33 -0400'
  date_gmt: '2007-07-14 15:36:33 -0400'
  content: Is the relationship between two articles in a journal defined by the start
    and end pages of each article?
- id: 19191
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2007-07-16 09:02:20 -0400'
  date_gmt: '2007-07-16 13:02:20 -0400'
  content: "[quote comment=\"19096\"]Is the relationship between two articles in a
    journal defined by the start and end pages of each article?[/quote]\r\n\r\nI suppose
    it would be; I haven't stopped to think about it much.  The order of elements
    matters in XML, so it could be an accurate representation of the way a journal
    issue is put together.  The database in which the citation data is stored would
    need to preserve that order, of course."
- id: 32898
  author: Md. Malek Hossain
  author_email: malek.prc@gmail.com
  author_url: ''
  date: '2008-04-02 09:30:44 -0400'
  date_gmt: '2008-04-02 13:30:44 -0400'
  content: This website is very essential for me and make a helpful guidline.
---
<p>Earlier this year the <a href="http://www.doaj.org/doaj?func=loadTempl&#038;templ=070509" title="Article-level OAI-PMH announcement on DOAJ website"><abbr title="Directory of Open Access Journals">DOAJ</abbr> began offering a new schema for registered articles</a> that significantly improves the value of OAI-PMH harvested article content.  Prior to this addition the only scheme available was Dublin Core, which as a metadata schema for describing article content is woefully inadequate.  (Dublin Core, of course, was never designed to handle the complexity of the description of an average article.)  The <a href="http://www.doaj.org/schemas/doajArticles.xsd" title="doajArticles&#039; XML schema">new schema</a> (graphically represented here<br />
<a href="/assets/images/2007/07/doajArticles_schema_image1.png" rel="lightbox"><img src="/assets/images/2007/07/.doajArticles_schema_image.png" alt="doajArticles schema image" title="doajArticles schema image" align="right" width="112" height="146" border="0" /></a> -- select thumbnail to see a larger version) includes elements for ISSN/eISSN, volume/issue, start/end page numbers, and author affiliation.  There is also a <code><fullTextUrl></code> element that is a link to the article content itself (not the splash page of the article on the publisher's site).</p>
<p>Article content using this schema is harvestable through the DOAJ OAI-PMH provider site (for instance, using a <a href="http://www.doaj.org/oai.article?verb=ListRecords&#038;metadataPrefix=doajArticle" title="XML harvest of the latest articles added to the DOAJ article archive"><code>ListRecords</code> verb with a <code>doajArticle</code> metadata prefix</a> against the PMH URL).  This is, in fact, the same schema journal publishers use to submit article content to the DOAJ article database.  With these pieces in place, it is now conceivable to harvest open access journal article content through the DOAJ and add it to a local journal article repository (such as the <a href="http://journals.ohiolink.edu/ejc/article.cgi?issn=14649055&#038;issue=v25i0002&#038;article=191_etoe" title="Journals: the OhioLINK experience&#039; article record in OhioLINK EJC">Electronic Journal Center</a> in the case of OhioLINK).</p>
<p>Thanks go out to the DOAJ folks for making this available!</p>
