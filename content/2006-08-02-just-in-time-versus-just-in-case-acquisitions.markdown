---
layout: wordpress-import
status: published
published: true
title: 'Just In Time Acquisitions versus Just In Case Acquisitions'
modified: 2006-08-02T13:30:51+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 22
wordpress_url: http://dltj.org/2006/08/just-in-time-versus-just-in-case-acquisitions/
date: '2006-08-02 09:30:51 -0400'
date_gmt: '2006-08-02 14:30:51 -0400'
category: Library Technology
categories:
- Economies of Scale
- Disruption in Libraries
- Library SOA
tags:
- publishing
- Amazon
- library service-oriented architecture
- opac
- ngc4lib
- MARC
- library 2.0
- disruptive innovation
- onix
- book
- libraries
comments:
- id: 2542
  author: jonvw
  author_email: jonvw@jonvw.com
  author_url: ''
  date: '2006-08-02 10:34:23 -0400'
  date_gmt: '2006-08-02 14:34:23 -0400'
  content: "If a library opts for publishers/distributors to do shelf processing,
    would it be possible to develop a workflow in which the book was shipped directly
    to the patron, processed and ready to be returned to the library?\r\n\r\nWhat
    I have in mind is something like this:\r\n\r\nWhen the order is shipped to the
    customer, the vendor sends a MARC record to the library be loaded into the automation
    system.  The automation system generates any relevant holdings data and checks
    the book out to the patron based on the anticipated receipt date of the item.\r\n\r\nMeanwhile,
    the patron receives the item, uses it, and returns it back to the library.  When
    the item is discharged, it's routed to the technical services team for any additional
    processing that might be necessary.\r\n\r\nOur vendors and automation systems
    might not be ready for this just yet, but it seems like something that could be
    just around the corner, especially now that Amazon is in the game."
- id: 2545
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-08-02 11:16:52 -0400'
  date_gmt: '2006-08-02 16:16:52 -0400'
  content: "[quote comment=\"2542\"]If a library opts for publishers/distributors
    to do shelf processing, would it be possible to develop a workflow in which the
    book was shipped directly to the patron, processed and ready to be returned to
    the library?[/quote]\r\n\r\nWow!  Now that is adventurous.  The control freak
    in me would want to be plugged in a little deeper into the publisher/distributor's
    workflow process in order to get the tracking number from the shipment to the
    patron.  Our circulation system can then periodically ask (or get updates from)
    the shipper as to the status of that item, then \"check it out\" when the shipper
    shows it was delivered to the patron.  This is where the Library Service Oriented
    Architecture becomes even more critical.\r\n\r\nThere could be, of course, an
    added cost we (or maybe the patron) would need to bear for the direct delivery
    service.  Presumably more than one item a day would be ordered from the publisher/distributor
    service and we might choose to have them send us in as few shipments as possible
    if the cost of the actual shipping becomes a factor.  If the delivery points get
    spread out to include the patron's own delivery locations, that economy of scale
    would be lost.\r\n\r\nGreat idea, Jon!"
- id: 18599
  author: 'Disruptive Library Technology Jester :: Automating Withdrawn Actions: Maximixing
    the Long Tail of Acquisitions'
  author_email: ''
  author_url: http://dltj.org/2007/07/automated-withdrawn-actions/
  date: '2007-07-05 10:49:37 -0400'
  date_gmt: '2007-07-05 14:49:37 -0400'
  content: "[...] for the first half of this process: approval plans, book jobber
    firm order systems, etc. (See the Just In Time Acquisitions versus Just In Case
    Acquisitions article on DLTJ for another idea about the front end of the process.)
    Not may seem to exist, nor [...]"
- id: 35253
  author: "&#8220;What is a library now?&#8221;: CSU Monterey Bay Opens New Library
    &laquo; E-Research Library"
  author_email: ''
  author_url: http://eresearchlibrary.wordpress.com/2009/04/20/what-is-a-library-now-csu-monterey-bay-opens-new-library/
  date: '2009-04-20 16:01:56 -0400'
  date_gmt: '2009-04-20 20:01:56 -0400'
  content: "[...] CSUMB library did prefer electronic over print delivery of information
    and focused on delivering &ldquo;just in time&rdquo; rather than &ldquo;just in
    case&rdquo; collections.&nbsp; As John Ober wrote in an essay from 2000, &ldquo;While
    [...]"
- id: 64162
  author: bookpublisher
  author_email: jacob.peters@townsend.com
  author_url: http://www.publish-book.com/
  date: '2010-04-12 11:46:16 -0400'
  date_gmt: '2010-04-12 15:46:16 -0400'
  content: If it's true that it will work like a business-to-business transaction,
    and be a RTIB would trigger the purchase of the item to be expedited to the patron&rsquo;s
    library. It's simple and great.
---
<p>What of a service existed where the patrons selected an item they needed out of our library catalog and that item was delivered to the patron <em>even when the library did not yet own the item?</em>  Would that be useful?  With the growth of online bookstores, our users do have the expectation of finding something they need on the web, clicking a few buttons and having it delivered.  When such expectations of what is possible exist, where is the first place a patron would go to find recently published items -- the online bookstore or their local library catalog?  Does your gut tell you it is the online bookstore?  Would it be desirable if the patron's instinct were to be the local library catalog?</p>
<p>A savvy patron looking for a recently published item will likely try the local library catalog to see if the item has been selected, purchased, received, cataloged, processed, and shelved (hereafter "SPRCPS") by the staff &mdash; in other words, gone through the traditional process libraries use for acquiring items.  If not, the patron has one of three choices (that I can think of):</p>
<ol>
<li>make a request for the item to be SPRCPS'd with a hold placed on the item so that the patron is notified when it is ready;</li>
<li>start an Interlibrary Loan process to try to get the item from another site that has SPRCPS'd the item faster than your library; or</li>
<li>pay a cost premium &mdash; buy the book themselves and have it delivered.</li>
</ol>
<p>Looking at this from the perspective of elapsed time, #1 is likely many weeks, #2 is likely a few weeks, and #3 is likely a few days.  Looking at this from the perspective of direct cost to the patron, #1 is the cheapest, #2 may be free or some nominal ILL transaction cost (depending on local policy), and #3 is the most expensive.  All-in-all, reasonable tradeoffs.</p>
<p>But what if our libraries offered a service that had the speed of #3 and the cost of #1?  Do you think that would be an appropriate service to our users?</p>
<h2>Local Catalog Display</h2>
<p>In my mind, such a system would be predicated on four factors.  First, our local catalog would need to display some record of <em>items that are not yet held but could be acquired on an expedited basis.</em>  If the savvy patron is going to start at the library catalog to determine if we already have the item, thereby executing the cheapest (no direct cost to the patron) and likely fastest (hop down to your local branch and pick it up) path to getting the item in hand, there needs to be a way to show patrons that the item <em>could</em> be added to the library's collection on an expedited basis.  Here in OhioLINK and with other similar consortial catalog systems, that expectation is already being set.  "Can't find the item in your local catalog?  Push this button and see if it is available from one of our consortial members.  If so, push this other button and we'll transport it from that library to here for you."</p>
<p>In terms of the mechanics of getting these records into our systems, it seems that we need a new form of MARC record loads into our systems.  The most likely source?  How about what booksellers use now -- the <a href="http://web.archive.org/web/20060802154431/http://www.bisg.org:80/activities-programs/activity.php?n=d&amp;id=15&amp;cid=2" title="Book Industry Study Group">ONIX format</a> "that publishers can use to distribute electronic information about their books to wholesale, e-tail and retail booksellers, other publishers, and anyone else involved in the sale of books."  A feed of ONIX records from publishers, filtered through a selection criteria, <a href="http://www.loc.gov/marc/onix2marc.html" title="ONIX to MARC 21 Mapping">converted into MARC21</a>, and loaded into our local catalogs would do the trick.</p>
<h2>Automated "Request This Item" Function</h2>
<p>Second factor -- a highly automated process to get the requested book to the library.  Again, those familiar with OhioLINK and other similar consortial borrowing/lending systems know that there is a ubiquitous "Request This Item" button ("RTIB" hereafter) for objects that are not in the patron's own library but can be requested from a consortial partner.  In this new Just-In-Time acquisition based on the ONIX record in our catalog, that RTIB would need the addition a second workflow:  the buy-this-item-and-deliver-it-to-my-library workflow.  Like a business-to-business transaction, the RTIB would trigger the purchase of the item to be expedited to the patron's library.</p>
<h2>Speedy Copy Cataloging and Shelf Prep</h2>
<p>Third factor -- the item must get through copy cataloging and shelf prep quickly.  When a RTIB item reaches the library loading dock, there must be a workflow and a commitment by copy catalogers and shelf prep staff to turn the item around in four hours for patron pick up.  If the RTIB immediately buys the item from the distributor, the distributor turns it around for same-business-day shipping, and the item arrives on our doorstep via an expedited courier (no "library rate postage" here, please), then the only place where we have an influence on the time it takes to get the item into the hands of the user is right here -- in our own technical services processes.  And there are a number of short-cuts that can be made here as well,</p>
<ul>
<li>Use "on the fly" circulation procedures to lend the book out immediately.  When it is returned route the item through technical services for formal copy cataloging (or decide that the Onyx data is acceptable as is for the copy cataloging).</li>
<li>Use a distributor that will delivery the item shelf-ready.  Just yesterday, through an <a href="http://lisnews.org/node/19233" title="LISNews.org | Amazon Introduces End-to-End Library Processing">LISnews posting</a>, I learned that <a href="http://www.amazon.com/gp/help/customer/display.html?nodeId=51533011" title="http://www.amazon.com/gp/help/customer/display.html?nodeId=51533011">Amazon is now one such distributor</a>:<br />
<blockquote><p>
Amazon offers a wide array of library processing options. In addition to mylar jackets on hard-cover books, Amazon also offers MARC records, spine labels, and barcodes. By partnering with leading cataloging companies and organizations, Amazon is also able to offer you highly customized MARC records, spine labels, and barcodes that meet your specific needs.
</p></blockquote>
</li>
</ul>
<h2>New Roles for Staff</h2>
<p>The fourth factor is the hardest -- the humans involved in the process.  And I don't think it is the patrons that would have as big of an issue with this Just-In-Time acquisitions process.  Here in Ohio a user expectation exists to tolerate receipt of an item in 24 to 48 hours via consortial borrowing services.  I think it will be the library staff who would need first convincing then time to adjust to this new way of selecting and purchasing items.  Some initial thoughts on new roles:</p>
<ul>
<li>Selectors/bibliographers still have front-end work to do.  They are the ones to tune the profile of "items that could be purchased" records (informed by the requesting patterns from users) that are loaded into the system and to buy items not yet requested that round out a collection.  This is modestly akin to the approval plan systems we use now.</li>
<li>Copy cataloging staff may have a reduced workload for items that come in through the RTIB process &mdash; particularly if the distributor selected does much of the shelf prep and copy cataloging work already.  This, too, is nothing new:  we have been outsourcing more of our technical services work and assigning the copy cataloging and shelf prep staff to work on other areas of the collection.</li>
</ul>
<h2>Summary</h2>
<p>Let's take one more look at the traditional SPRCPS process and see how things would change under a Just-In-Time acquisitions model.</p>
<dl>
<dt>Selected</dt>
<dd>An initial round of selection is done by the bibliographers and collection managers.  They decide which broad categories of ONIX records from publishers/distributors will be represented as "items-to-be-acquired" in the local catalog.  Patrons, then vote with their fingers and mice clicks as to which items meet their needs.</dd>
<dt>Purchased</dt>
<dd>An entirely automated business-to-business transaction.  Once the user decides the item is what they need, our library computer talks directly to the publisher/distributor computer and buys the item.</dd>
<dt>Received</dt>
<dd>The publisher/distributor doesn't dally -- they ship the item to us for next-day or second day delivery.  When it arrives in our mail room, we need to act fast.</dd>
<dt>Cataloged</dt>
<dd>Copy cataloging could be done by us, we could receive copy catalog records from the publisher/distributor, or we could decide that &mdash; at least for now &mdash; that the ONIX data is good enough and that like an "on-the-fly" transaction the formal copy cataloging will happen after the item is returned.</dd>
<dt>Processed</dt>
<dd>Choices here, too.  Will our staff do the shelf-prep work or is that something we contract with the publisher/distributor?  In any case quick processing here, too because...</dd>
<dt>Shelved</dt>
<dd>...we want to get the item in the hands of the user who requested it.  "Shelved" in this case could be the hold-pickup shelf, or it could be a local physical delivery service that sends the item to the patron.</dd>
</dl>
<p>Can we do this as fast as it would take the patron to get the item directly from the online bookseller?  Maybe not -- we do have some necessary processing steps that a direct patron purchase process does not have.  Can we make that delay short enough so that the patron considers it acceptable as compared to the direct price premium of ordering it themselves?</p>
<p>Do we want to?</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.bisg.org/onix/index.html to http://www.bisg.org/activities-programs/activity.php?n=d&id=15&cid=2.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://lisnews.org/article.pl?sid=06/08/01/023238 to http://lisnews.org/node/19233 on January 13th, 2011.</p>
