---
layout: wordpress-import
status: published
published: true
title: 'A Catalog for the "Next Generation" or the Current Generation?'
modified: 2008-06-23T19:44:48+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 382
wordpress_url: https://dltj.org/?p=382
date: '2008-06-23 15:44:48 -0400'
date_gmt: '2008-06-23 19:44:48 -0400'
category: Disruption in Libraries
categories:
- Disruption in Libraries
tags:
- opac
- ngc4lib
- rest
- web services
- mashup
comments:
- id: 33502
  author: Dan Scott
  author_email: dan@coffeecode.net
  author_url: http://coffeecode.net
  date: '2008-06-24 00:36:35 -0400'
  date_gmt: '2008-06-24 04:36:35 -0400'
  content: "I agree in principle with the discussion of \"current\" versus \"next\"
    generation catalogs, and most of the conclusions that you've highlighted from
    the report - but the following quote made me chuckle ruefully:\r\n\r\n\"All major
    ILS vendors but III provide their customers a web services or HTTP REST API access
    to their systems, allowing for continued development around the catalog.\"\r\n\r\nWhat?
    It certainly comes as news to me that Unicorn offers either a web services or
    HTTP REST API access to my system. From discussions with other library world developers,
    it doesn't sound like many other \"major ILS vendors\" offer Web services or HTTP
    REST API access either (except, perhaps, in the broadest, most generous definition
    of \"Web service\" where \"you GET or POST to a URL and some mass of poorly formed
    HTML is returned). Methinks the report authors were fed a steady diet of salespeople
    to talk to...\r\n\r\nI don't think the traditional ILS vendors could point to
    something like Evergreen's SuperCat RESTful interface: http://open-ils.org/dokuwiki/doku.php?id=backend-devel:supercat:examples
    - and that's barely scratching the surface of what Evergreen offers today."
- id: 33505
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-06-24 14:43:48 -0400'
  date_gmt: '2008-06-24 18:43:48 -0400'
  content: Dan -- very possible.  It is arguably <em>easier</em> to create an HTTP
    REST API with vendors other than Innovative, but that doesn't necessarily mean
    that the REST API is <em>provided</em> by the vendor.  Still, I hope that excerpting
    that comment from the document as a whole doesn't detract from the fact that we
    <em>need</em> extensible APIs from ILS vendors to do "current generation" and
    "next generation" stuff on our own without relying on said vendors...
- id: 33533
  author: Ian Ibbotson
  author_email: ianibbo@googlemail.com
  author_url: ''
  date: '2008-07-01 08:37:56 -0400'
  date_gmt: '2008-07-01 12:37:56 -0400'
  content: There are certainly a couple of Z3950 -> SRU bridges out there that can
    be used to easily expose Z3950 databases as restful web services. AFAIK Index
    Data have an open source (C based) bridge and JZKit also has an open source (Java)
    bridge. Is the Z3950 problem to do with the semantics of the search mechanism,
    licensing issues with the host systems, or just that these bridges need more exposure?
- id: 33535
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-07-02 11:12:56 -0400'
  date_gmt: '2008-07-02 15:12:56 -0400'
  content: "Ian --\r\n\r\nREST-based (or any API) access to read-only bibliographic
    data is one thing.  It is, unfortunately, quite another to have API access to
    the internals of the item status information, being able to post transaction requests,
    and the like.\r\n\r\nAlthough I haven't tried it, my gut tells me that a Z39.50-to-SRU
    bridge isn't exactly light-weight, either.  One has the overhead of building two
    TCP connections (one into the bridge and one out) plus any Z39.50 connection overhead.
    \ Z39.50 servers are sometimes licensed \"products\" that have to be purchased,
    but I don't think that is the main problem with their non-use."
---
<p>Are we building the "next generation" catalog for us (librarians) or our users?  As a read <a href="http://web.archive.org/web/20081007033935/http://www.orbiscascade.org/staffhome/Next_Generation_Catalog-report.pdf" title="General Recommendations of the Next Generation Summit Search Interface Working Group">a report</a> from the <span class="removed_link" title="http://www.orbiscascade.org/staffhome/SCC-NGSIWG.htm">Next Generation Summit Search Interface Working Group</span> of the Orbis/Cascade Alliance, I have to wonder.  Portions of this report are dated ((Although the report itself does not contain a date, mention of the report appears in <a href="http://www.orbiscascade.org/staffhome/SCC_07mar12-agenda.htm" title="Summit Catalog Committee Agenda -- March 12, 2007">the agenda of a March 2007 meeting</a> of the consortium's Summit Catalog Committee.)) other portions are timeless.  In particular, this section from page 2 (emphasis added):</p>
<blockquote><h2>How do we define &ldquo;next generation&rdquo;?</h2>
<p>The working group has considered what it means to create a "next generation catalog" within the context of the current Summit interface and the current definition of "next generation" as understood within the library community. However, maybe this isn't the right question.  In part, library systems have failed to even keep up with our current generation of users, with neither the library community or vendor community really understanding how a current generation catalog might function.  We have ideas from looking at vendor sites and social software tools that provide tagging, faceted browsing, and user reviews, but are these really "next generation"?  No, they represent current generation functionality that library systems simply have yet to assimilate into their current service offerings.  It's a dangerous confusion of vocabulary.  While these services represent "next generation" services for the library community, they don't for our users.  If a simple makeover of the ILS is to be our aim, then we will continue to fail to provide services for our current generation of users.  Our current library information systems are failing our users and inhibiting our users' attempts to build communities around our services and systems.</p>
<p><strong>Libraries should rectify this problem by seeking to build systems that meet the needs of this current generation, while allowing the library community to plan for and implement functionality that will be necessary within the "next generation".</strong>  In part, this is what some libraries are doing -- some examples are discussed in this report.  North Carolina State University's utilization of Endeca has been lauded far and wide, but in essence, they've simply started to catch up with today&rsquo;s current generation of users.  Yet in just catching up to the current generation, they have distinguished themselves from the rest of the library community.  They have placed themselves in a position to look beyond the needs of the current generation of users and focus on the services and needs of the next.  At this point, few organizations, including the Alliance, can make such a claim.  That, in part, is the challenge facing the Alliance and this working group as it made its assessments.</p></blockquote>
<p>It would seem helpful to shift terminology, because in doing so we can focus more readily on the needs of our users.  They aren't looking for a "Next Generation" interface.  "Next Generation" to us means "Current Generation" to our users.  "Next Generation" for our users is "what have you done for me lately?"  In order to meet that need, we need a platform that is "developer-friendly."  Again, from the report:</p>
<blockquote><p>a platform that supports and encourages interaction with the system.  This can take many shapes, including OAI harvesting, SRU, OpenSearch or a simple web-services-based API to allow the Alliance to take a more proactive role in developing services. </p></blockquote>
<p>And, finally, in the report's recommendations:</p>
<blockquote><p>Additionally, in researching current and in-development solutions, it became clear that if the Alliance is to continue to meet the needs of its users, it will have to demand greater access to the metadata (holdings, items, bibliographic) found within the catalog.  Regardless of who provides the Alliance&rsquo;s next generation OPAC product, one of the deliverables that must be available as part of any solution is API or web services access to the catalog.  Access at this level is important for two reasons:
<ol>
<li>It allows libraries to integrate and share development resources: <br /> The Alliance members are currently hamstrung by the closed nature of the Summit catalog.  The Summit INN- Reach catalog currently only provides two methods of interaction &ndash; Z39.50 and HTML access.  For developers looking to build services around the Summit catalog, the Z39.50 protocol, as implemented, is currently too limiting and expensive for production development services.  All major ILS vendors but III provide their customers a web services or HTTP REST API access to their systems, allowing for continued development around the catalog.  Lacking such access, the Summit catalog will continue to be marginalized within the consortium&rsquo;s academic campuses as tools and services are developed that take advantage of web service friendly applications.</li>
<li>Allows for the development of library-created or user-created mashups: <br /> The Alliance should strive to create a resource that encourages users, libraries, and campuses to develop services around the Summit catalog.  The library community has recognized that our patrons want social tools, which we tend to identify as tagging, commenting, etc.  However, Web 2.0 applications like Flickr are popular because of the API access that they provide to their users as well.  This access has enabled other web services, individuals, and organizations to develop different methods for exporting and utilizing the images placed within the Flickr photo archive.  The Alliance should strive to make the Summit catalog open in this way, so that users and members alike are free to enhance Summit to meet individual, campus, or consortial needs.</li>
</ol>
</blockquote>
<p>If it is possible to sum up what we need in "next generation" systems, I haven't seen more succinctly put than this report.</p>
