---
layout: wordpress-import
status: published
published: true
title: 'More About OhioLINK''s Discovery Layer Desires'
modified: 2008-11-24T18:43:41+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 601
wordpress_url: http://dltj.org/?p=601
date: '2008-11-24 13:43:41 -0500'
date_gmt: '2008-11-24 18:43:41 -0500'
category: OhioLINK
categories:
- OhioLINK
tags:
- OhioLINK
comments:
- id: 35108
  author: New Directions for Discovering Information | Disruptive Library Technology
    Jester
  author_email: ''
  author_url: http://dltj.org/article/ohecc-dl/
  date: '2009-03-30 20:54:16 -0400'
  date_gmt: '2009-03-31 00:54:16 -0400'
  content: "[...] OhioLINK project, see this earlier DLTJ posting with a description
    from the solicitation and this follow-up posting with answers to questions from
    potential bidders. (When reading these messages, please note that the time for
    submitting responses to the [...]"
---
<p>On Friday, OhioLINK released an addendum to its <a href="/article/discovery-layer-itn/">inquiry for a comprehensive discovery layer</a> that answers questions submitted from potential bidders.  This is a distilled version of that addendum -- posted here with the desire to reach others that may be interested in submitting a bid.  Please note that this posting is not the official call for proposals nor the official addendum (it isn't even the entire addendum).  Nothing said here binding on the proposal process.  If you are interested in making a proposal for a solution or part of the solution for what we are seeking, please contact Mary Pasquinelli, Sr. Purchasing Agent at Wright State University (OhioLINK's administrative agent), and reference ITN 601908 (Room 301 University Hall, 3640 Colonel Glenn Hwy., Dayton, Ohio 45435, phone 937-775-2411, FAX 937-775-3711, email: mary.pasquinelli@wright.edu).</p>
<ul type="disc">
<li><i>Section 22.2 Specific Features, subsection 1.4.2, Page 24:  Subsection 1.4.2 states: &ldquo;The system supports delivery resolver availability data embedded into facet(s).&rdquo;  Please explain what this means.</i></li>
</ul>
<p>A facet must be generated for broad cross-sections of availability.  For instance:  &ldquo;Online&rdquo; (digital copy available), &ldquo;On-Campus&rdquo; (on-shelf status in the patron&rsquo;s institution/branch), &ldquo;2-3 Day Delivery&rdquo; (as in PCIRC/INN-Reach requesting), &ldquo;2-3 Week Delivery&rdquo; (as in traditional ILL).</p>
<ul type="disc">
<li><i>Could you elaborate on the delivery resolver?  What already exists versus what we envision as being part of the solution?</i></li>
</ul>
<p>OhioLINK is seeking a delivery resolver that will bring together all existing modes of delivery to the user &ndash; what is available now (through digital delivery), what is available today (on campus), what is available in a couple days (through INN-Reach), and what is available in a couple weeks (through Interlibrary Loan).  The delivery resolver must be flexible enough to handle existing modes of delivery as well as enable the addition of new modes of delivery (for example, possibly a subscription to the Google Book Search corpus), and distill all of the complexity of the delivery options into a single link for the user.  </p>
<p>OhioLINK already has a requesting and delivering system for physical items through the INN-Reach software from Innovative Interfaces.  We have a link resolver and a knowledge base for access to electronic articles.  The proposed solution need not replicate/duplicate these existing services.</p>
<ul type="disc">
<li><i>Will the metadata for these databases come directly from the database vendors, in varying formats, or will it come as a single set of data/single format from OhioLINK and the Electronic Journal Center &ndash; in other words, will the data come from the database vendors directly, or will it come out of the Electronic Journal Center as a single set?</i></li>
</ul>
<p>Metadata for the databases listed in section 12.2.1 will come directly from the sources (database vendors as well as other sources such as the Electronic Journal Center, Electronic Book Center, and the Digital Resource Commons) in a variety of formats.</p>
<ul type="disc">
<li><i>P. 11-13, Sections 12.2.1 and 12.2.2 - Regarding the desired content listed:  How will you determine what content is part of your unified index and what is searchable via your federated search engine?</i></li>
</ul>
<p>It is OhioLINK&rsquo;s desire to put as much into the unified index as possible.  To the extent that OhioLINK can get content from the provider, it will be added to the unified index.  The federated search engine will be a fallback for those providers that cannot or will not offer OhioLINK a license to load the data into the unified index.</p>
<ul type="disc">
<li><i>Regarding section 22.2 Specific Features, of the Vendor Response Form, in 2.3: &ldquo;Calculates/resolves a persistent identifier for each record retrieved through the federated search engine&rdquo;.  Please provide further description of what is meant by &ldquo;persistent identifier&rdquo;.</i></li>
</ul>
<p>Views of records obtained through the federated search engine must be repeatable.  This requires the formation of a persistent identifier that can be used in permalink URLs in such a way that enables subsequent users to get back to the same record.  This is needed in order to put URLs for records into course management systems and other locations.</p>
<ul type="disc">
<li><i>What if some of the databases listed as part of the unified index end up being accessed through a federated search (e.g., SportsDiscus) and some databases in your federated search list become part of the unified index?  Can you please discuss how you would handle this?</i></li>
</ul>
<p>OhioLINK expects some fluidity in the mixture of databases in the unified index and federated search components.  Volatility will come in the form of updates/reloads of source data, the addition and removal of licensed databases, additions of new member data (e.g. local institutional repositories, special collections projects, etc.), and capabilities of data sources to start providing (or no longer providing) data to OhioLINK for the unified index.  The candidate solution for the unified index component must be able to load and unload data to match these situations.  It must be possible to add and remove data sources in the federated search component.  The user interface must be capable of mapping its permalinks for records from unified index sources to federated search sources, assuming the existence of common unique identifiers between the unified index source and the federated search source.</p>
<ul type="disc">
<li><i>P. 5, Section 3.1 - This section states: "OhioLINK is evolving its suite of services in the face of changes in user expectations."  Are there predominant user groups you are interested in, and do these groups have unique needs?</i></li>
</ul>
<p>Based on the sheer quantity of users, the predominant user group is undergraduate students.  Studies show that this user group is focused on finding highly relevant answers quickly.  These users also tend to cast a broad search initially, and then refine it as needed.  Students are also likely to be at websites other than the libraries, so there is a strong need to insert the start of the search process in websites such as course management systems, campus portals, and departmental websites.</p>
<ul type="disc">
<li><i>Do you envision that the vendor will take over the responsibility for negotiation of formats and schedules from the data sources or do you see OhioLINK staff still playing a role in acquiring the data and the vendor simply supplying an interface to put the data into the system?</i></li>
</ul>
<p>As originally envisioned, OhioLINK would continue to be involved in receiving the metadata and loading it into the system.  However we would consider a scenario in which the solution provider did that on our behalf &ndash; with the exclusion of the licensing.  Depending on the proposed system, it may also be efficient in terms of cost and effort for the solution provider to negotiate formats and delivery schedules with the data source on OhioLINK&rsquo;s behalf, and OhioLINK staff would be responsible for the ongoing loading of data that meets the agreed upon format and schedule.</p>
<ul type="disc">
<li><i>Once a user executes a search in the membership of OhioLINK, is it anticipated that there will be availability information from each of member institutions?</i></li>
</ul>
<p>Yes.  Whether or not an institution has rolled out the discovery layer interface to its constituency, the proposed system must look for availability of items at that institution.  This information is available now in the form of PCIRC status at the OhioLINK INN-Reach catalog.</p>
<ul type="disc">
<li><i>Can you give a sense of average or peak user searches in OhioLINK?</i></li>
</ul>
<p>OhioLINK cannot currently track use comprehensively across its many resources, so we do not have this data.  We do have high-level statistics, but we do not warrant that this would be representative of actual use.  For the past calendar year, OhioLINK users conducted around 30 million searches.  2.9% of these searches &ndash; approximately 870,000 &ndash; were conducted in the peak month.  19.15% of these searches &ndash; approximately 167,000 &ndash; were conducted on the peak day of the month.</p>
<p>Note that the goal of this ITN is to deploy a system that is more useful to users; thereby drive more traffic to use these library resources.  A proposed solution must be able to scale readily as demand grows and shrinks.  We would anticipate this might entail clusters of servers and requisite load balancers. </p>
<ul type="disc">
<li><i>How do you expect to handle db sources that are subscribed to by member institutions?</i></li>
</ul>
<p>It is OhioLINK&rsquo;s desire to handle as much as possible in the unified index even if not all member institutions have access to all resources.  This requires appropriate authentication (whether by IP address or by login) and access controls for this data loaded into the unified index.  In addition, the federated search must consider authentication when selecting remote databases that receive a broadcasted search.</p>
<ul type="disc">
<li><i>For 3rd party records or vendor records that member institutions do not have the rights to load to OhioLINK, how do you expect those records to be served here?</i></li>
</ul>
<p>These records would be harvested from the local catalog and would be handled as if they were a database for which authentication was required (e.g. a locally-subscribed database).</p>
<ul type="disc">
<li><i>Question 3.10.1 of the vendor response (page 26 of the ITN) says, &ldquo;By default, display federated search results below unified index results.&rdquo;  What does &ldquo;below&rdquo; mean?  At the end of the screen or separate?</i></li>
</ul>
<p>&ldquo;Below&rdquo; is an overly prescriptive word.  It is anticipated that the unified index will return records in orders of magnitude faster than the federated search engine.  What is desired is the results from the unified index are immediately displayed for the user with a portion of the results screen reserved for dynamic updates of summary/progress from the federated search engine.  This requirement says that results from the federated search will be presented on a different screen from the unified index results.  Question 3.10.2 of the vendor response (&ldquo;Upon user request, integrate unified index and federated search results into single display&rdquo;) represents the ideal scenario, where records from the unified index and the federate search engine are combined, de-duped, and re-ranked onto a single display.</p>
<ul type="disc">
<li><i>Regarding integration of federated search with unified index results interface.  Do you want a description of an interface of the federated search separate from unified interface?</i></li>
</ul>
<p>We want to know how the federated search component will integrate with the user interface.  The user interface will handle the higher-level functions &ndash; result set operations, record marking, permalinks, etc. &ndash; and the user interface will get records from the unified index and federated search components.  As such we are not envisioning a separated federated search engine user interface.  A response needs to indicate how the federated search component will integrate into the overall user interface.</p>
<ul type="disc">
<li><i>Will you be requiring library pricing or centralized pricing?</i></li>
</ul>
<p>OhioLINK does not require a specific pricing model.  The model needs to be compatible with our objective to offer a unified discovery layer for all OhioLINK members.  The solution will be purchased as a group. </p>
<ul type="disc">
<li><i>Do you require that the vendor host the solution or OhioLINK host the solution?</i></li>
</ul>
<p>As originally envisioned, OhioLINK would host the system on its own servers.  (See section 12.4 (The OhioLINK systems environment) for details on OhioLINK&rsquo;s requirements for services.)  Notwithstanding that, OhioLINK would consider a solution physically hosted by the vendor.</p>
<ul type="disc">
<li><i>Is there a preferred timeline for deliverables?</i></li>
</ul>
<p>The implementation timetable is a function of the approval timetable and the complexity of the proposals.  Ideally, we would anticipate bringing up the initial discovery layer deliverable for the next school year (starting roughly August 15, 2009).  The implementation at that time might only be some of the eventual components and sources to be included.  We would consider an incremental build-out.</p>
<ul type="disc">
<li><i>Is there a sense that this will be a phased implementation?  Is there a desire to see it all happen at a hard launch?  Is there a sense that the institutions will join gradually or that member institutions will all go live on a single launch date?</i></li>
</ul>
<p>We are interested, of course, with having as complete and robust a system as early as possible.  To the extent that one proposal provides a realistic but more rapid implementation, this will be looked upon favorably.  Without seeing the implementations proposed it is impossible for us to determine how individual libraries will come online- whether all together or in some phasing.  From a data sources perspective, we would anticipate that sources would be added gradually as each is profiled and loaded.</p>
<p>An exception to any phased rollout plan is the display of the availability of a physical item from a member institution.  When the system checks for the availability of physical items, such a check must be comprehensive across all members of OhioLINK that hold an item, not just a subset of sites.</p>
<ul type="disc">
<li><i>Regarding section 22.5 Secondary Evaluation Elements, in item 9.7: &ldquo;Can you provide a full-feature trial using OhioLINK data?&rdquo;  Could you specify what data?</i></li>
</ul>
<p>The data would consist of the candidate solution harvesting MARC records from the ILS, harvesting records from OhioLINK&rsquo;s OAI-PMH servers (dSpace, ETD center), and loading records from index and abstract databases for which OhioLINK already has the data.  </p>
<p>Note, that the full-featured trial is not required in the ITN response due on December 15, 2008.  OhioLINK will work with zero, one or more proposed solutions to build the full-featured trial in the course of evaluating the responses.</p>
<ul type="disc">
<li><i>Section 12. Specifications, subsection 12.2.1, Pages 11-13:  Subsection 12.2.1 describes sources to be included in the Unified Index.  Can you please provide file formats, estimated update frequency, and whether regular (annual) reloads of the datasets will be required for each of the sources listed in this section?</i></li>
</ul>
<p>It is not possible to answer the format and frequency schedule parts of this question because such parameters have not been set for a significant number of sources.  There are sources (at least PSYCinfo and Compendex at present) that require annual reloads.</p>
