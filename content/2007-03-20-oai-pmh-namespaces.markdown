---
layout: wordpress-import
status: published
published: true
title: 'A Report on Namespaces Used by OAI-PMH Repositories'
modified: 2007-03-20T20:00:43+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 197
wordpress_url: http://dltj.org/2007/03/oai-pmh-namespaces/
date: '2007-03-20 16:00:43 -0400'
date_gmt: '2007-03-20 21:00:43 -0400'
category: Raw Technology
categories:
- Linking Technologies
- Raw Technology
tags:
- standards
- metadata
- MARC
- digital libraries
- Dublin Core
- oai-pmh
- libraries
comments:
- id: 13278
  author: Sarah Shreeves
  author_email: sshreeve@uiuc.edu
  author_url: ''
  date: '2007-03-20 17:45:24 -0400'
  date_gmt: '2007-03-20 22:45:24 -0400'
  content: "Have you seen the work that Tom Habing has done at the University of Illinois
    on a Registry of OAI data providers? He's added all sorts of interesting reports
    on OAI data providers and has probably the biggest list of OAI data providers
    since he pulls in data providers that are not registered at openarchives.org.\r\n\r\nSee
    http://gita.grainger.uiuc.edu/registry/.\r\n\r\nsarah"
- id: 13283
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2007-03-20 21:16:07 -0400'
  date_gmt: '2007-03-21 02:16:07 -0400'
  content: Thank you, Sarah!  Tom's <a href="http://gita.grainger.uiuc.edu/registry/ListSchemas.asp"
    rel="nofollow">Distinct Metadata Schemas</a> is much more comprehensive, and more
    useful, than my quick scripting.  I'm grateful for the pointer to his work.
---
<p>I had a need for a survey of the metadata namespaces used by <a href="http://www.openarchives.org/pmh/" title="Open Archives Initiative Protocol for Metadata Harvesting homepage">OAI-PMH</a> repositories, so I wrote up a quick shell script and XSLT style sheet to parse through the list of <a href="http://www.openarchives.org/Register/BrowseSites" title="Registered OAI-PMH Data Providers">Registered Data Providers</a> at the OpenArchives.org website.  The <span class="removed_link" title="http://dltj.org/misc/oai-pmh-namespace-report.html">results of this effort</span> are pretty interesting.  Some of them:</p>
<ul>
<li>Dublin Core is, as you would expect, the highest-used descriptive metadata standard.  Every service &mdash; or at least those that reported using any namespace at all &mdash; reported Dublin Core as a record harvesting option.  For some, it was the <em>only</em> option (which I find rather sad).  One problem, though, comes in with the variety of namespace URIs declared that all appear to be semantically the same thing:  <tt>http://www.openarchives.org/OAI/2.0/oai_dc/</tt>, <tt>http://www.openarchives.org/OAI/2.0/oai_dc</tt> (note the missing trailing slash), <tt>http://purl.org/dc/elements/2.0/</tt> (used exclusively by the <span class="removed_link" title="http://www.umi.com/umi/digitalcommons/">ProQuest Digital Commons product</span>, it would seem), and <tt>http://purl.org/dc/elements/1.1/</tt> (the difference between 2.0 and 1.1 is not clear to me).  In order to be processable, there must be an exact string match of the namespace URI -- so even that missing trailing slash is significant!</li>
<li>The next most popular namespace URI is <tt>http://info.internet.isi.edu:80/in-notes/rfc/files/rfc1807.txt</tt>, which semantically would seem to identify the <a href="http://www.faqs.org/rfcs/rfc1807.html" title="RFC 1807 (rfc1807) - A Format for Bibliographic Records">IETF RFC 1807 on a Format for Bibliographic Records</a>.  You can <a href="http://etd.library.pitt.edu/ETD-db/NDLTD-OAI2/oai.pl?verb=GetRecord&#038;metadataPrefix=oai_rfc1807&#038;identifier=oai%3APITETD%3Aetd-11272006-155805" title="">see what one of these things looks like</a> -- although RFC1807 predates XML (it was approved by the IETF in mid-1995), it looks like someone turned the metadata format into XML along the way.  Very interesting...</li>
<li>The next most popular is <tt>http://www.ndltd.org/standards/metadata/etdms/1.0/</tt> &mdash; corresponding to the <a href="http://web.archive.org/web/20130905212055/http://www.ndltd.org/standards/metadata/etd-ms-v1.00-rev2.html/" title="Networked Digital Library of Theses and Dissertations Metadata Standard">Interoperability Metadata Standard for Electronic Theses and Dissertations</a> &mdash; followed closely by <tt>http://www.openarchives.org/OAI/1.1/oai_marc</tt> &mdash; which <a href="http://www.openarchives.org/OAI/2.0/guidelines-marcxml.htm" title="OAI-PMH Implementation Guidelines: A recommended XML Schema to represent MARC21 records">fell out of favor years ago</a> with the publication of <a href="http://www.loc.gov/standards/marcxml/" title="MARC 21 XML Schema">MARC21</a> by the Library of Congress (which goes by the namespace <tt>http://www.loc.gov/MARC21/slim</tt>).  Unfortunately, it doesn't seem to have been picked up by the majority of OAI-PMH data providers that used the older oai_marc schema.</li>
<li>As you get towards the bottom of the first list, there are all sorts of interesting variants on qualified Dublin Core and other one-off schemas.</li>
</ul>
<p>Your thoughts and observations?  I've filed away the UNIX script and XSLT style sheet.  If there is interest in seeing something like this in the future, let me know and I can dig them out.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://dltj.org/misc/oai-pmh-namespace-report.html on December 30th, 2010.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.umi.com/umi/digitalcommons/ on January 19th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.ndltd.org/standards/metadata/current.html to http://www.ndltd.org/standards/metadata/etd-ms-v1.00-rev2.html/ on January 19th, 2011.</p>
