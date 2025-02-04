---
layout: wordpress-import
status: published
published: true
title: 'Automating Withdrawn Actions: Maximixing the Long Tail of Acquisitions'
modified: 2007-07-05T14:49:22+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 37
wordpress_url: http://dltj.org/2007/07/automated-withdrawn-actions/
date: '2007-07-05 10:49:22 -0400'
date_gmt: '2007-07-05 14:49:22 -0400'
category: Economies of Scale
categories:
- Economies of Scale
tags:
- OhioLINK
- library consortia
- disruptive innovation
- long tail
- libraries
comments: []
---
<p>Libraries place a good deal of emphasis on collection development policies -- a written statement of a library's intentions for building its collection.  It describes the collection's strengths and weaknesses and provides guidelines for the purchase ("acquisition") and disposition ("weeding") of content.  This is an activity that sets libraries apart from other organizations.</p>
<p>A number of automated systems exist for the first half of this process:  approval plans, book jobber firm order systems, etc.  (See the <a href="/article/just-in-time-versus-just-in-case-acquisitions/">Just In Time Acquisitions versus Just In Case Acquisitions</a> article on DLTJ for another idea about the front end of the process.) Not may seem to exist, nor are they as widely used, at the end of the process -- deciding when an item needs to drop off the shelf to make way for something new.  The <a href="http://www.oclc.org/collectionanalysis/" title="OCLC WorldCat Collection Analysis homepage">OCLC WorldCat Collection Analysis</a> is one such tool; this posting describes another -- a way a consortia can maximize the array of content held collectively by optimizing the deaccessioning of material.<br />
<!--break--></p>
<h2>Existing Practice</h2>
<p>Cooperative collection development is nothing new to OhioLINK.  Its <a href="http://web.archive.org/web/20060906101222/http://www.ohiolink.edu/ostaff/policyhbk/cirm/1.assumption.html" title="OhioLINK Policy Handbook">Cooperative collection development document objectives and assumptions</a> policy is a foundational document that describes the consortium's intent to build a collection that is collectively stronger than the individual parts.  More specifically, the <a href="http://platinum.ohiolink.edu/cbtf/lastcopy.pdf">CIRM Guidelines for Last Copy</a> describes actions "the library should take in order to keep at least one copy [of a title] in Ohio."  To that end, a "discards" list is maintained where libraries can post information about titles being removed from a collection, with special emphasis on last-copy announcements.</p>
<p>The 'discards' list is a shot-gun approach to handling deaccessioned items -- everyone on the list receives the same broad spectrum of announcements.  If a subject specialist subscribed to the list, he or she would receive a lot of "noise" from announcements in unrelated subject areas.  Conversely, an acquisitions coordinator may not appreciate the value of an item from a specialized field.  Also, as the policy guidelines dictate, checking to see if special handling is needed on a title-by-title basis because it might be the last copy in Ohio adds a time consuming step to the discard process.  This proposed "Automated Withdrawn Actions" system seeks to address the issues of targeted notification of deaccessioned items and streamlining the consortial aspects of collection weeding.</p>
<h2>Overview of Proposed System</h2>
<p>The Automated Withdrawn Actions (AWA) system starts with a web page where the local catalog's bibliographic record number or item barcode is entered into a database at OhioLINK.  Software at OhioLINK pulls the MARC record from the local system using on the bib record number or the barcode and reads the LC class and/or Dewey call number.  A rough subject categorization is determined based on the LC class or Dewey call number.  The software uses the subject categorization to send an announcement of the item (either via e-mail, RSS feed, or some other mechanism) to selectors across the state that have signed up to receive notifications for that subject area.  If another library wants the item, the system will notify the holding library and a PCIRC transmittal slip is generated for the physical delivery of the item to the requesting library.</p>
<p>The AWA system can also look up the item in the OhioLINK central catalog to determine the number of libraries that hold the same title.  If removing the copy in question would trigger a "last copy" situation, the software can send the same notification to the 'discards' mailing list with the "LAST COPY OFFER" notation.  If seven days pass and no other library accepts the item, the system can generate a PCIRC transmittal slip to send the item to Ohio State University -- Ohio's academic library of last resort.</p>
<h2>Technical Requirements</h2>
<p>The Automated Withdrawn Actions software would run on OhioLINK's servers on behalf of its members.  Staff at member institutions would notify the system of items being withdrawn via a record-by-record web form or by uploading a file of records.  Bibliographic item numbers are the unique key for titles both in the local system and in the central catalog.  In order to use barcodes (or item record numbers), a member library would need to export a list of barcodes (and item record numbers) with matching bibliographic record numbers and upload that to the AWA software.  Requesting libraries would use a URL embedded in the e-mail or RSS message to request the item for their library.</p>
<h2>Possible Extensions</h2>
<p>Once the basic AWA system is automated, one can envision several extensions that would streamline the process or provide additional avenues for withdrawn items.</p>
<h3>Transfer of MARC Record</h3>
<p>As long as the item is being transferred, the system could offer a file containing the MARC record from the withdrawing library that could be used as the basis of cataloging the item in the receiving library.  Since the bibliographic record is a match for the item, little if any copy cataloging would be needed.</p>
<h3>OCLC Holdings Update</h3>
<p>If the MARC record is copied from the withdrawing library to the receiving library, there may be no corresponding OCLC copy cataloging activity to register the receipt of the new item.  Additionally, removing the withdrawing library's OCLC symbol from the Worldcat record is yet another task to be done by the withdrawing library.  The AWA system could queue up the "withdrawn" and "attach" messages to Worldcat on behalf of the member libraries.  (Assuming the original MARC record contained an OCLC record number.)</p>
<h3>Offering Withdrawn Items to Libraries Outside Ohio</h3>
<p>If an item is being withdrawn is not desired by another OhioLINK member and it is not the last copy in the state, the AWA system could be opened up to participation by other libraries.  For the cost of shipping, another library may request an item withdrawn from the collection of a member library.</p>
<h3>Other Automated Transfers of Deaccessed Items</h3>
<p>In addition to other libraries, other transfer systems could be tied into AWA.  For instance, there could be a function that would list the item for sale on e-bay, or offer it to <a href="http://www.alibris.com/" title="Alibris: Used Books, Used Textbooks, Rare &amp;amp; Out-of-Print Books">Alibris</a> or another used book seller.</p>
<h2>Conclusion</h2>
<p>Chris Anderson, Editor of Wired magazine and author of <a href="http://www.thelongtail.com/" title="The Long Tail&#039; homepage">The Long Tail</a>, describes a phenomenon where a large number of items each used a small number of times collectively make up a large body of usage, given an enabling framework.  Amazon is one such framework where more books than could possibly be held at a physical bricks-and-mortar store are offered, and every title is purchased by at least some small number of individuals.</p>
<p>By automating the actions that occur when an item is withdrawn from a member library, the long tail of library item usage can be pulled out a little further.  Once unused items can find a new home and a new stream of usage via the software and workflow described here.</p>
