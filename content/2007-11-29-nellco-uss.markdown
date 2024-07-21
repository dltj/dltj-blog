---
layout: wordpress-import
status: publish
published: true
title: 'NELLCO's Universal Search Solution Project'
modified: 2007-11-29T18:59:15+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 298
wordpress_url: http://dltj.org/2007/11/nellco-uss/
date: '2007-11-29 13:59:15 -0500'
date_gmt: '2007-11-29 17:59:15 -0500'
categories:
- Raw Technology
tags:
- metadata
- metasearch
- unified index
- NELLCO
- Index Data
- IMLS
comments:
- id: 671566
  author: The problem with discovery tools and law firm libraries &#8211; Slaw
  author_email: ''
  author_url: http://www.slaw.ca/2013/11/06/the-problem-with-discovery-tools-and-law-firm-libraries/
  date: '2014-12-10 14:14:16 -0500'
  date_gmt: '2014-12-10 19:14:16 -0500'
  content: "<!--%kramer-ref-pre%-->[&#8230;] for this post, Susannah. In 2007 NELLCO
    received an IMLS grant to fund the development of the Universal Search Solution
    (USS) for law libraries. At that time, we [&#8230;]<!--%kramer-ref-post%-->"
---
<blockquote>Boundaries are being blurred between the academic and commercial Web, between library resources, between the citation and the item itself. Students have no patience with these arbitrary boundaries; they want information, and they want it now, wherever it may be located. ((<span class="removed_link" title="http://www.uwec.edu/library/aboutUs/who/cox.htm">Cox, Christopher</span>.  <a href="http://journals.ohiolink.edu/ejc/article.cgi?issn=15307131&amp;issue=v06i0003&amp;article=253_aaotioliutas" title="Link to article on OhioLINK EJC">An Analysis of the Impact of Federated Search Products on Library Instruction Using the ACRL Standards</a>.  <a href="http://www.press.jhu.edu/journals/portal_libraries_and_the_academy/" title="journal homepage">portal: Libraries and the Academy</a>.  6(3), July 2006, pp. 253-267.))</p></blockquote>
<p>Earlier this year, the New England Law Library Consortium (<a href="http://www.nellco.org/" title="New England Law Library Consortium homepage">NELLCO</a>) <a href="http://www.librarytechnology.org/ltg-displaytext.pl?RC=13319" title="NELLCO&#039;s IMLS press release">announced</a> that they had <span class="removed_link" title="http://www.imls.gov/results.asp?program=-1&amp;inst=+New+England+Law+Library+Consortium&amp;city=&amp;State=0&amp;year=12&amp;keyword=&amp;description=on&amp;sort=year&amp;imageField.x=0&amp;imageField.y=0">received a grant</span> from the <a href="http://www.imls.gov/about/about.shtm" title="About IMLS">Institute of Museum and Library Services</a> to build a "Universal Search Solution" -- a 'one-box' search into a unified index of a range of electronic resources.  Indexed databases include <abbr title="Online Public Access Catalog">OPAC</abbr>s, subscription-based resources, and selected free web resources.  It is a two year grant to build and implement the tool for NELLCO members and release the code into open source.  <a href="http://www.indexdata.dk/news/#2007-09-26" title="News">Index Data</a> will be contracted to build the tool.</p>
<p>The tool "will be based on open standards and open source software, and will result in the creation of a ... master index of material, including participating library catalogs, as well as subscription-based databases and open content, special collections, and other resources that a participating library wishes to make discoverable to its patrons."  ((From the <a href="http://www.librarytechnology.org/ltg-displaytext.pl?RC=13319" title="NELLCO&#039;s IMLS press release">NELLCO press release</a>.))  The project specifications include the concept of differentiating search results based on the user's institutional affiliation -- search results from the user's OPAC and hits from commercial data sources in the unified index that are limited by license to just that user's institution.  "Technologically, the Universal Search Solution will combine multiple technologies (consolidated indexing and data storage; metadata harvesting; and metasearching) to put together a single window to disparate resources." ((From the <a href="http://www.indexdata.dk/news/#2007-09-26" title="News">Index Data press release</a>.))</p>
<p>I spoke with <a href="http://www.nellco.org/general/?type=CONTACT" title="Contact information for Tracy Thompson">Tracy Thompson</a> earlier this week about the project.  The concept is an out-growth of an earlier pilot to use a <a href="http://www.google.com/enterprise/gsa/" title="Google Enterprise: Google Search Appliance">Google Search Appliance</a> (GSA) to create the unified index.  The pilot was technologically successful, but ran into problems in the business model for the GSA because the pricing was based on the number of "documents" and from the GSA perspective each record indexed in a database was a document.  (To give a perspective, the GSA page says the base model "starts at $30,000 to search up to 500,000 documents" ((This figure is on the GSA page at the time this posting is being published, but it is also on the <a href="http://web.archive.org/web/20070808095050/http://www.google.com/enterprise/gsa/" title="403 Forbidden">8-Aug-2007 copy of the page in the Internet Archive</a>.)) -- and how many bibliographic records are in our OPACs, just as a baseline for costing out a GSA?)</p>
<h2>Current Status</h2>
<p>Tracy said the IMLS grant period starts on December 1st, and they are in the process of hiring a project coordinator (the search has not yet been announced).  There will be a kick-off meeting for NELLCO participants in early December.</p>
<p>In broad strokes, the first year is geared mainly towards building the tool.  In the second year, the IMLS grant will fund the implementation of the tool for interested NELLCO members.  After the grant period, NELLCO expects they will be able to sustain the implementation by subscription fee from the members.  As described earlier, this is a consortial product/service, so there are already some economies of scale to be gained by not implementing redundant hardware/support at many local institutions.</p>
<h2>A Different Model for Open Source Development</h2>
<p>The Index Data press release goes on to say:</p>
<blockquote><p>The grant also offers a new model for libraries to obtain affordable software services that are under their control. It combines the powerful financial leverage of IMLS and the organizational capabilities of NELLCO and its membership with the software development expertise of Index Data to bring cutting edge open source software and services to all types and sizes of libraries -- affordable and with commercial support -- but without vendor lock-in.</p></blockquote>
<p>The <a href="/article/clashing-values/">tension between the inherent values of commercial, closed-source software vendors and higher education institutions</a> (with an <a href="/article/aligning-clashing-values/">acknowledging nod towards commercial support for open source solutions</a>) has been discussed on <acronym title="Disruptive Library Technology Jester"><i>DLTJ</i></acronym> before.  The IMLS/NELLCO/Index Data collaboration suggests a new way for software tools to be built:  a granting agency funds the initial hurdle of software development, and then the project transitions to self-supporting either through subscription charges that are in the self-interest of participants or through the sweat equity of participant-developers.
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.nellco.org/IMLS/Press%20Release.pdf to http://www.nellco.org/index.cfm?fuseaction=Feature.showFeature&featureid=21&pageid=4 on January 20th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.nellco.org/IMLS/Press%20Release.pdf to http://www.nellco.org/index.cfm?fuseaction=Feature.showFeature&featureid=21&pageid=4 on January 20th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.uwec.edu/library/aboutUs/who/cox.htm on January 20th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.nellco.org/index.cfm?page=contact to http://www.nellco.org/general/?type=CONTACT on November 13th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.imls.gov/results.asp?program=-1&inst=+New+England+Law+Library+Consortium&city=&State=0&year=12&keyword=&description=on&sort=year&imageField.x=0&imageField.y=0 on November 13th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.nellco.org/index.cfm?fuseaction=Feature.showFeature&featureid=21&pageid=4 to http://www.librarytechnology.org/ltg-displaytext.pl?RC=13319 on November 21st, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.nellco.org/index.cfm?fuseaction=Feature.showFeature&featureid=21&pageid=4 to http://www.librarytechnology.org/ltg-displaytext.pl?RC=13319 on November 21st, 2012.</p>
