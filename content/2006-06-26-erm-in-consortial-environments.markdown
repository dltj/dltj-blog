---
layout: wordpress-import
status: published
published: true
title: 'Electronic Resource Management Systems in Consortial Environments'
modified: 2006-06-26T17:49:02+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 82
wordpress_url: http://dltj.org/2006/06/erm-in-consortial-environments/
date: '2006-06-26 13:49:02 -0400'
date_gmt: '2006-06-26 18:49:02 -0400'
category: Linking Technologies
categories:
- Linking Technologies
- Economies of Scale
tags:
- ALA Annual Conference 2006
- Library and Information Technology Association
- Digital Library Federation
- ermi
- library consortia
- libraries
comments:
- id: 5578
  author: LITA Blog
  author_email: ''
  author_url: http://litablog.org/2006/06/28/ttt-identifiers-erm-jpeg2000/
  date: '2006-06-28 17:39:13 -0400'
  date_gmt: ''
  content: "<!--%kramer-pre%-->a summary of the discussion of the LITA Library Consortia
    / Automated Systems Interest Group meeting on Monday morning. The meeting consisted
    of a managed discussion of the use of Electronic Resource Management (ERM) systems
    in consortial environments. Read more&hellip; <!--%kramer-post%-->"
---
<p>This is a summary of the discussion of the LITA Library Consortia / Automated Systems Interest Group meeting on Monday morning of the ALA Annual Convention in New Orleans.  The meeting consisted of a managed discussion of the use of Electronic Resource Management (ERM) systems in consortial environments.  In some cases, comments from the two primary speakers and discussion among the commingled and unattributed.  Inaccuracies and comments taken out of context are the responsibility of the author of this posting, and corrections or embellishments are welcome in the form of comments to this post or as private e-mail messages.</p>
<p>The first speaker was from Yale (unfortunately, I arrived late and didn't get her name -- a helpful hint in a comment to this posting would be appreciated).  Yale purchased and "implemented" (actually getting any ERM system up and running is not a trivial task, so it is hard to say when "implemented" is) Verde about 14 months ago when it was in alpha development.  Ex Libris delivered a production version to Yale in September 2005 and from them until two weeks ago Yale has been working through configuration and getting an the electronic journal coverage load into the ERM system to know what they have("took quite a while to get there").  Next they will be migrating information about which databases and e-books they have, followed by data entry for subscription, license, and administrative information for all records in the system.  They will probably set up these data entry projects with three different groups, one for each metadata type, operating concurrently.</p>
<p>Yale's ILS is Endeavor Voyager.  They looked at Endeavor's Meridian and Innovative's ERMS in addition to Verde.  ERMS, although it was in production, was less attractive because it would add third vendor in their automation mix.  A major part of their selection process came down to which of their existing systems needed to be more closely integrated with the ERM, and they decided it was more important to be more closely aligned with their existing SFX and Metalib implementations that with the ILS.  Yale's systems department thinks they will be able to pull read-only acquisitions information from the Voyager system via a custom 'report' function using the purchase order number as a key.  Yale is not putting print serial information into Verde.  (Verde has the capability to create a "print record" for a "work" (e.g. bibliographic record).)  They have an automated lookup from SFX to their ILS that the user can use to find information about print subscriptions.</p>
<p>The second speaker was Diane Carol from the Oregon Health Sciences University (OHSU).  They have an Innovative Interfaces ILS and because of existing consortial arrangements, had no choice but to use ERMS from Innovative.  Prior to implementing an ERM system, they used things like the 856 fields in the ILS to point to electronic journals plus an external SQL/ColdFusion database for public users and spreadsheets for administrative information, license information, and statistics.  At one point they were trying to maintain holdings in five or six systems (above plus Ovid, PubMed, etc.)  In 2003 they decided to integrate the information about electronic products into one place.  This single source of data would be used to upload to other systems and OpenURL resolves, allow wider access to the license data, and centralize the collection development decisions.</p>
<p>Information from their old coverage database (ISSN, URLs, and Holdings) was loaded and attached to a resource records.  ISSN connected it to the existing bibliographic record in the ILS.  Also has a license record that is also attached to the resource record.  Doing things this way created "skeletal records" for resource records -- the minimal of what is needed to start loading the system.  Because OHSU is part of a consortial union catalog, doing this added a lot of brief records in the union catalog; they are now looking at the process needed to clean this up.  OHSU's OpenURL resolver is Innovative's WebBridge, and coverage data is automatically updated.</p>
<h2>Helpful Hints</h2>
<p>Both speakers echoed the need to involve disparate groups of people in the project.  Yale commented that they faced a decision about whether to start with just a small group of people to do a deep load of just the licensing attributes or involve more people with a broad perspective of not just the back-end technical services changes but also the public A-Z list changes.  Yale ended up going with the bigger scope and she was not sure they could have made any other choice.</p>
<p>Yale started by walking through the DLF ERMI data dictionary to determine what fields they wanted to use what values to put in those fields (e.g. establishing standard terminology), but found it very different when they started the data load and thinking about how they would use it.  For instance, does one need to record in the ERM the state of where the license will be adjudicated?  If it isn't part of reporting needs or a public display, then don't bother.  (One can always look it up later out of the paper files.)  In other words, don't create a "high bar" for the initial implementation by thinking that you will fill every field of every record.</p>
<p>If you already have a link resolver and/or a metasearch engine from a vendor other than that of your ILS, decide whether you need tighter integration with the link resolver/metasearch engine or the ILS and have that weight your selection criteria.  For instance, Yale reports that Verde can eliminate some duplicative data entry -- information entered into Verde can be pushed into SFX.  SFX can also be configured to look up permissions, license rights, and technical information in Verde (an "i" information button in SFX).  However, from the same vendor, Metalib is not talking to Verde in any way; it is a concern of Yale for when they start to record database information into Verde.  Yale is seeking from Ex Libris a best practice for data entry now to be prepared for the day when the integration is done.  The general observation of the group was that institutions tend to go with their link resolver product vendor versus their ILS vendor.</p>
<h2>To pay attention</h2>
<p>Know whether you getting a "Knowledge Base" with your product?  If not, that will add on to the ultimate cost.  (Meridian, for instance, doesn't come with a knowledge base.)</p>
<p>Implementation is done for Verde 2.0, documentation done on July 1, early adopters are using the software, public demonstration sites are ready, general release date announcement coming soon.  Verde 2.0 has some new features for consortia.  Although it not available yet, it is still useful to have their 1.1 implementation to start addressing how the consortium will deal with the definition of fields and how they will be used across the consortium.</p>
