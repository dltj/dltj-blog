---
layout: wordpress-import
status: published
published: true
title: 'Long-term Preservation Storage:  OCLC Digital Archive versus Amazon S3'
modified: 2008-05-16T11:55:36+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 361
wordpress_url: https://dltj.org/?p=361
date: '2008-05-16 07:55:36 -0400'
date_gmt: '2008-05-16 11:55:36 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Amazon
- OCLC
- preservation
- Amazon S3
- Amazon EC2
comments:
- id: 33268
  author: K.G. Schneider
  author_email: kgs@freerangelibrarian.com
  author_url: http://freerangelibrarian.com
  date: '2008-05-16 17:13:35 -0400'
  date_gmt: '2008-05-16 21:13:35 -0400'
  content: "This is an outstanding job, Peter.\r\n\r\nMy first question when I read
    about OCLC's archive service was how this compared to LOCKSS. That's not to criticize
    your piece one bit -- just to suggest that someone needs to run those numbers
    as well."
- id: 33271
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-05-16 20:01:36 -0400'
  date_gmt: '2008-05-17 00:01:36 -0400'
  content: "A good point, Karen -- I had not considered comparing it to LOCKSS yet.
    \ My first thought, obviously, was S3 as a raw hosting service.  A comparison
    to LOCKSS would be more appropriate -- and harder given the fuzzier (perhaps better
    described as \"cooperative\" instead) economics.  \r\n\r\nIf anyone else embarks
    on such an effort, be sure to post a comment here that points to your work.  I'm
    sure we'd all be interested."
- id: 33383
  author: s/d
  author_email: ''
  author_url: ''
  date: '2008-06-03 10:05:42 -0400'
  date_gmt: '2008-06-03 14:05:42 -0400'
  content: "<!--%kramer-ref-pre%-->[...]      Enlla&ccedil;os i apunts r&agrave;pids,
    breus, sint&egrave;tics. Flaixos. CENT &szlig;eta: Sturm &#38; Drang.    May 23
    \  Long-term Preservation Storage: OCLC Digital Archive versus Amazon S3     #
    \    &nbsp;   RSS the feed &nbsp;&nbsp; gelato cms the engine &nbsp;&nbsp; Cameron
    the [...]<!--%kramer-ref-post%-->"
- id: 33391
  author: barbara quint
  author_email: bquint@mindspring.com
  author_url: http://www.infotoday.com/newsbreaks
  date: '2008-06-04 06:58:32 -0400'
  date_gmt: '2008-06-04 10:58:32 -0400'
  content: "wow. your analysis is impressive. i feel very proud to have contributed
    to its creation. the original piece also went slightly into the issue of buying
    2 1-terabyte external hard drives for the cost of 1 year's worth of a 10th of
    a terabyte, which oclc sells in chunks. complicated, all these archive choices.\r\nbq"
- id: 33509
  author: Robert McDonald
  author_email: mcdonald@sdsc.edu
  author_url: http://www.sdsc.edu/~mcdonald
  date: '2008-06-25 13:15:40 -0400'
  date_gmt: '2008-06-25 17:15:40 -0400'
  content: One thing that I see missing from your wonderful analysis is the network
    costs associated with S3. This may be figured into Barbara's numbers but if not
    including at least 1 put and 1 get cost factor for networking then you should
    at least include some type of cost for ec2 for checking on the data during the
    course of the year.
- id: 33510
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-06-25 13:35:03 -0400'
  date_gmt: '2008-06-25 17:35:03 -0400'
  content: "Robert -- In retrospect, it isn't entirely clear from the the table of
    cost distributions, but the start-up and ongoing \"ingest costs\" represent the
    network transmission costs.  For data coming into the S3 service, the user is
    charged a flat rate of $0.10/GB.  The rate for returning content out of the S3
    archive varies.  Outputting up to 10TB per month (which would cover outputting
    the entire 2TB prototypical content discussed in the article) costs 17 cents per
    GB; the cost for 2TB would $340/month.  If you tested the content once a month
    by downloading it to a local server, that would be $4,080.\r\n\r\nCosts for using
    a Amazon EC2 virtual machine are harder to calculate, and probably can't be accomplished
    without a little bit of experimentation.  That would involve actually building
    an EC2 machine to do the virus and fixity testing.  \r\n\r\nThanks for the comments."
- id: 33518
  author: barbara quint
  author_email: bquint@mindspring.com
  author_url: http://www.infotoday.com/newsbreaks
  date: '2008-06-26 12:12:38 -0400'
  date_gmt: '2008-06-26 16:12:38 -0400'
  content: "<i>[</i><acronym title=\"\"Disruptive Library Technology Jester\">DLTJ</acronym><i>
    editor's note:  With Barbara Quint's permission, I'm posting a comment received
    as e-mail here along with my reply.]</i>\r\n\r\nboth amazon and oclc had put/get
    costs as i recall, but i didn't compare them. have to suspect that amazon's were
    probably lower.\r\n\r\nabout your analysis, though, you describe oclc's digital
    archive as complete, including end-user access. i don't think so. it's for archival
    copies (hi-res) only and, as far as i know, accessible to archive managers. they
    expect enduser access to come through their contentDM service to which libraries
    subscribe separately. the contentDM subscribers don't even get a special rate
    from oclc for the new digital archive service.\r\n\r\nand as for putting formatting
    issues on the user/subscriber, oclc was quite clear that the archivist sending
    them the files was responsible for any changes in preservation formatting. at
    present, they didn't even have a forum for warning people that their formats are
    getting obsolete, although there was a glimmer of interest when i suggested it
    as a good idea. i got the feeling that it would only happen if the service sold
    big enough to develop its own forum.\r\n\r\nwhat i didn't look into is whether
    other amazon web services could supply tools that would appeal to archivists.
    package together a number of their services and you might get a better deal all
    around and probably still at a lower price."
- id: 33519
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-06-26 12:14:48 -0400'
  date_gmt: '2008-06-26 16:14:48 -0400'
  content: "What I had intended to write was that OCLC's Digital Archive service is
    \"complete\" in terms of a traditional dark archive service that may be sought
    by an archivist. &nbsp;(It occurs to me, though, that we don't have much of a
    tradition of dark archive digital services, so that may be a bit of an oxymoron.)
    &nbsp;Amazon S3 could be considered an \"incomplete\" dark archive service (no
    inherent backup or disaster recovery assurance) with a \"light archive\" add-on.\r\n\r\nIt
    is true that OCLC's Digital Archive service does not allow for end- user access
    to content out of the Digital Archive. &nbsp;For archive managers, there is a
    cost associated with retrieving bulk batches of content out of the archive. &nbsp;I
    did not include the latter in the analysis since it was outside the bounds of
    what we had envisioned the Digital Archive could be used for. &nbsp;But I'll agree
    that it is an important aspect to look at.\r\n\r\nI don't think there are other
    Amazon Web Services that by themselves would inherently be appealing to a digital
    archive service, but the ability to build such tools in the Amazon EC2 virtual
    computing cloud is possible, if only theoretical at this point."
- id: 33900
  author: 'Fitzroy Libratech: Digital Archives as Profit'
  author_email: ''
  author_url: http://fitzroylibratech.blogspot.com/2008/09/digital-archives-as-profit.html
  date: '2008-09-27 20:09:14 -0400'
  date_gmt: '2008-09-28 00:09:14 -0400'
  content: "<!--%kramer-ref-pre%-->[...] information in S3! As Peter E. Murray describes
    in his blog Disruptive Library Technology Jester ( http://dltj.org/article/oclc-digital-archive-vs-amazon-s3/
    ), there are important reasons for that price difference. As Murray points out,
    while [...]<!--%kramer-ref-post%-->"
- id: 34545
  author: iNODE &raquo; S3 Storage
  author_email: ''
  author_url: http://timesync.gmu.edu/wordpress/?p=897
  date: '2009-01-18 21:59:04 -0500'
  date_gmt: '2009-01-19 02:59:04 -0500'
  content: "<!--%kramer-ref-pre%-->[...] offered an interesting apples-to-oranges
    comparison of OCLC&#8217;s Digital Archive service and S3 last May that is worth
    reading. His post dug a bit deeper into issues raised by Barbara Quint&#8217;s
    [...]<!--%kramer-ref-post%-->"
- id: 34953
  author: Can We Outsource the Preservation of Digital Bits? | Disruptive Library
    Technology Jester
  author_email: ''
  author_url: http://dltj.org/article/outsource-digital-bits/
  date: '2009-03-05 14:55:51 -0500'
  date_gmt: '2009-03-05 19:55:51 -0500'
  content: "[...] companies that do the same thing? (I know of OCLC&#8217;s Digital
    Archive service &mdash; I did a comparison of it with Amazon S3 last [...]"
- id: 34993
  author: John Wang
  author_email: zhengwang@library.ucla.edu
  author_url: http://www.library.ucla.edu
  date: '2009-03-09 16:37:56 -0400'
  date_gmt: '2009-03-09 20:37:56 -0400'
  content: "It is a very interesting post. A larger picture born in my mind is the
    access to those preserved content. Is it a black box only for preservation purposes?
    Or it should offer users access to those content as well? \r\n\r\nIf users don't
    have access, libraries have to host at least a set of copy of the entire collection
    elsewhere - What is the total cost (hardware, software, labor, physical space,
    Power, etc)? If we add the cost of the \"access copy/copies,\" it appears to me
    that it is going to cost libraries much more. \r\n\r\nIt is critical and practical
    to look at cloud computing solutions coving the whole library value chain (from
    acquisition, cataloging, access, preservation, etc) instead of looking at it for
    a part of the value chain. The saving on one part of the chain does not translate
    to saving on other parts, and it may be likely to spike the costs on other part
    of the chain. Amazon appears to be the vendor for the overarching picture from
    its various web services (storage, cloud computing, rented IT expertise, etc).\r\n\r\nOne
    element is missing from the post is that the technical infrastructure that Amazon
    and OCLC run those services - it is really the key to data recovery, backup, management,
    and security, regardless what's says on the terms. The terms have to be written
    for \"minimal business liability\" and \"protection from law suits.\" If we look
    at \"economy of scale\" here: Amazon has\r\n\r\nFar larger Grid/Server Farm, and
    thus much more stable, distributed, faster, and high availability;\r\nMuch more
    years of experience running cloud computing and hosted storage;\r\nMuch experienced
    staff manage cloud computing.\r\n\r\nI have no idea what infrastructure OCLC is
    running for its Digital Archive and who is manage it from reading the post. I
    don't know how OCLC can compete with Amazon on the rules of the \"economy of scale.\"
    \r\n\r\nThe added values from OCLC are not really added values to me anyway: for
    most of the libraries have set up processes and applications to manage them, which
    can be run on our local infrastructures or elsewhere, such as Amazon infrastructure.\"\r\n\r\nIn
    my humble opinion, OCLC got to consider investing in other larger Cloud Computing
    Providers as its infrastructure instead of investing on hardware to reinvent a
    much \"smaller wheel,\" and focus the investment on software solutions on preservation
    and access services for libraries - a strategy to lower costs and concentration
    on core values."
- id: 36357
  author: 'Re: [AMIA-L] personal digital archiving; was "Future of Video"'
  author_email: ''
  author_url: ''
  date: '2009-06-06 01:59:20 -0400'
  date_gmt: '2009-06-06 05:59:20 -0400'
  content: "<!--%kramer-ref-pre%-->[...] OCLC's Digital Archive Service, and in the
    process provides a nice illustration of the difference:  http://dltj.org/article/oclc-digital-archive-vs-amazon-s3/
    \ Once the Audiovisual Archive Network (AVAN) is up and running, it will offer
    a Digital Repository [...]<!--%kramer-ref-post%-->"
- id: 99320
  author: blog.ecorrado.us &raquo; S3 for Backup, Is It Worth It?
  author_email: ''
  author_url: http://blog.ecorrado.us/2010/06/14/s3-for-backup-is-it-worth-it/?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+ecorradorss2+(ecorrado.us)
  date: '2010-11-10 10:29:38 -0500'
  date_gmt: '2010-11-10 15:29:38 -0500'
  content: "<!--%kramer-ref-pre%-->[...] about the availability of the service, but
    not of the files themselves. A while back I did a comparison of Amazon&#8217;s
    S3 and OCLC&#8217;s &#8220;Digital Archive&#8221; service that goes into these
    details and a little bit [...]<!--%kramer-ref-post%-->"
- id: 218167
  author: 'Eifl-OA: Georgia'
  author_email: ''
  author_url: ''
  date: '2012-02-06 13:31:22 -0500'
  date_gmt: '2012-02-06 18:31:22 -0500'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">http://t.co/w0AFALo2</span></span></span>
---
<p>Last month <a href="http://www.oclc.org/us/en/news/releases/200810.htm" title="Press Release: OCLC offers Digital Archive service for long-term digital storage">OCLC announced a new service offering for long-term storage of libraries' digital collections</a>.  Called <a href="http://www.oclc.org/us/en/digitalarchive/" title="OCLC Digital Archive homepage">Digital Archive&trade;</a>, it provides "a secure storage environment for you to easily manage and monitor the health of your master files and digital originals."  Barbara Quint has an article in Information Today called "<a href="http://newsbreaks.infotoday.com/nbReader.asp?ArticleId=49018" title="Information Today Article: OCLC Introduces High-Priced Digital Archive Service">OCLC Introduces High-Priced Digital Archive Service</a>" in which she makes a comparison to <a href="http://www.amazon.com/S3-AWS-home-page-Money/b/ref=sc_fe_l_2?ie=UTF8&amp;node=16427261" title="Amazon S3 product description">Amazon's Simple Storage Service</a> (or "S3") from primarily a cost perspective: "The price for S3 storage at Amazon Web Services is 15 cents a gigabyte a month or $1.80 a year, in comparison to OCLC&rsquo;s $7.50 a gig."  Barbara also goes into some of the technical differences, but I think it might be worthwhile to go a little more into depth on them.</p>
<h2>OCLC's Digital Archive</h2>
<p>According to the <a href="http://web.archive.org/web/20081012181719/http://www.oclc.org/us/en/digitalarchive/overview/" title="OCLC Digital Archive Service Overview">service overview</a>, Digital Archive is a content hosting service that provides:</p>
<ul type="square">
<li>Systems management</li>
<li>Physical security</li>
<li>Data security</li>
<li>Data backups</li>
<li>Disaster recovery</li>
<li>ISO 9001 certification</li>
<li>Manifest verification</li>
<li>Virus check</li>
<li>Format verification</li>
<li>Fixity check</li>
</ul>
<p>It is targeted towards the preservation of digital masters.  There is a document on the Digital Archive website called <a href="http://web.archive.org/web/20110830065826/http://www.oclc.org/us/en/digitalarchive/about/commitment/default.htm" title="&#039;Our commitment&#039; page on OCLC Digital Archive product site">Our commitment</a> that describes other aspects of a digital preservation program:  "OCLC is actively developing processes for full preservation of digital assets to ensure complete renderability, regardless of technology changes. This preservation system will likely involve a combination of migration and emulation."  But it is not clear whether these services, beyond "bit preservation" activities, is part of the Digital Archive service or will be part of an add-on service to be developed later.</p>
<p>This "Digital Archive" is a revamping of an older product from OCLC, also called "Digital Archive" but one that included a web harvesting tools component.  The service and support documentation on the OCLC website still refers to the former version of Digital Archive, so there is little information about how the service works beyond what one can infer from the sales information.</p>
<h2>Amazon's S3</h2>
<p>Amazon describes S3 as "a simple web services interface that can be used to store and retrieve any amount of data, at any time, from anywhere on the web. It gives any developer access to the same highly scalable, reliable, fast, inexpensive data storage infrastructure that Amazon uses to run its own global network of web sites."  Files are transfered across the internet to Amazon's services and stored in multiple data centers.  Files can be retrieved using standard HTTP mechanisms (the same protocol that powers the web) and are protected by an optional access control mechanism.  S3 does have a <a href="http://www.amazon.com/gp/browse.html?node=379654011" title="Amazon Web Services S3 Service Level Agreement">Service Level Agreement</a> (SLA) that offers guarantees on performance.</p>
<p>SLA seems to extend only to availability of the service, not to a long term commitment to keeping track of files on the service.<br />
<blockquote>AWS [Amazon Web Services, LLC] will use commercially reasonable efforts to make Amazon S3 available with a Monthly Uptime Percentage (defined below) of at least 99.9% during any monthly billing cycle (the "Service Commitment"). In the event Amazon S3 does not meet the Service Commitment, you will be eligible to receive a Service Credit as described below.</p></blockquote>
<p>  There is no mention specifically in the S3 SLA about permanence of file storage.  In leu of that, one seems to be covered by the overarching <a href="http://www.amazon.com/AWS-License-home-page-Money/b/ref=sc_fe_c_0_16427261_10?ie=UTF8&#038;node=3440661" title="Amazon Web Services Customer Service Agreement">Amazon Web Services Customer Agreement</a>, which has several points of interest from a preservation use perspective:<br />
<blockquote>3.3. Termination or Suspension by Us Other Than for Cause.<br />3.3.2. <i>Paid Services...</i>. We may suspend your right and license to use any or all Paid Services (and any associated Amazon Properties)..., or terminate this Agreement in its entirety (and, accordingly, cease providing all Services to you), for any reason or for no reason, at our discretion at any time by providing you sixty (60) days' advance notice in accordance with the notice provisions set forth in Section 15 below. </p></blockquote>
<p>  So if they desire to terminate a library's use of the service (assuming there was no specific cause -- such as a violation of the terms of use -- to do so), they have to give 60 days notice.  That's when the "Data Preservation in the Event of Suspension or Termination" clause kicks in:<br />
<blockquote>3.7.2. In the Event of Termination Other Than for Cause. In the event of any termination by us of any Service or any set of Services, or termination of this Agreement in its entirety, other than a for cause termination under Section 3.4.1, (i) we will not take any action to intentionally erase any of your data stored on the Services for a period of thirty (30) days after the effective date of termination; and (ii) your post termination retrieval of data stored on the Services will be conditioned on your payment of Service data storage charges for the period following termination, payment in full of any other amounts due us, and your compliance with terms and conditions we may establish with respect to such data retrieval.</p></blockquote>
<p>  The customer agreement then goes on to say:<br />
<blockquote>3.8. Post-Termination Assistance.Following the suspension or termination of your right to use the Services by us or by you for any reason other than a for cause termination (i.e., a termination under Section 3.2 or under Section 3.3), you shall be entitled to take advantage of any post-termination assistance we may generally make available with respect to the Services, such as data retrieval arrangements we may elect to make available. We may also endeavor to provide you unique post-suspension or post-termination assistance, but we shall be under no obligation to do so. Your right to take advantage of any such assistance, whether generally made available with respect to the Services or made available uniquely to you, shall be conditioned upon your acceptance of and compliance with any fees and terms we specify for such assistance.</p></blockquote>
<p>Perhaps the most troubling aspect, from a preservation point-of-view, deals with data security and backups.  Specifically, Amazon says that data security and backups are the responsibility of the customer.  The Amazon Web Services Customer Agreement says (emphasis added):<br />
<blockquote>7.2. Security. We strive to keep Your Content secure, but cannot guarantee that we will be successful at doing so, given the nature of the Internet. Accordingly, without limitation to Section 4.3 above and Section 11.5 below, <strong>you acknowledge that you bear sole responsibility for adequate security, protection and backup of Your Content.</strong> We strongly encourage you, where available and appropriate, to use encryption technology to protect Your Content from unauthorized access and to routinely archive Your Content. We will have no liability to you for any unauthorized access or use, corruption, deletion, destruction or loss of any of Your Content.</p></blockquote>
<p>  That kind of security and data backup is something you'd want in a preservation service.  Since activities against S3 storage is limited only by a knowing a private "key" ((S3 uses secret keys -- a 40-character password -- to verify the identify of the client making the request.  If the private key becomes known, anyone on the internet can perform operations actions as the content owner.)) (as opposed to limiting to particular IP addresses or not allowing deletes/modifications from the web at all), it is a real possibility that the archive can be harmed if the private key is disclosed.  Furthermore, S3 does not have a backup/restore service for retrieving files that were accidentally or maliciously deleted.</p>
<h2>Feature Comparison</h2>
<p>It is useful to compare Amazon's S3 on a point-by-point basis OCLC's Digital Archive service to try to put some meaning behind the cost numbers.</p>
<table>
<tr>
<th></th>
<th style="padding: .25em 1.5em;">OCLC Digital Archive</th>
<th>Amazon S3</th>
</tr>
<tr>
<td>Systems management</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Physical security</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Data security</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Data backups</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Disaster recovery</td>
<td>Yes</td>
<td>unclear</td>
</tr>
<tr>
<td>ISO 9001 certification</td>
<td colspan="2">whatever the heck that might mean in this context</td>
</tr>
<tr>
<td>Manifest verification</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Format verification</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Virus check</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Fixity check</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>"Light archive" capability</td>
<td>No</td>
<td>Yes</td>
</tr>
</table>
<p>This is a useful comparison because it would indicate what one would have to layer on top of S3 to reach the level of service provided by Digital Archive.  For instance, it would be possible to create an application that would perform the manifest and format verifications as well as the periodic virus and fixity checks against the files in S3.  It would even be possible to run that application in <a href="http://www.amazon.com/EC2-AWS-Service-Pricing/b/ref=sc_fe_l_2?ie=UTF8&amp;node=201590011&amp;" title="Amazon Web Services EC2 homepage">Amazon's Elastic Compute Cloud</a> (EC2) -- a "virtual computing environment" that allows developers to easily create and deploy software on the internet.  Since data transferred between Amazon EC2 and Amazon S3 is free of charge, there wouldn't be the S3 cost of periodically downloading the data to perform the virus and fixity checks.  </p>
<p>One advantage to note about the S3 solution is that it can perform as a "light archive" -- meaning the data is available to users in addition to being part of the content repository.  In contrast to the OCLC Digital Archive service -- a "dark archive" -- access to the data is highly or completely restricted.  Still, the lack of automated backups and a robust data security infrastructure in the S3 infrastructure are notable from a preservation data service perspective.</p>
<h2>Cost Comparison</h2>
<p>To examine the similarities and differences in costs, let's use the OhioLINK Satellite Image collection as a prototypical example.  It consists of about 2 terabytes (2TB) of high-quality images in TIFF format, with about 7.5GB of data going into the repository each month.  In the interest of exploring everything that S3 can do, there is an assumption that approximately 4GB of data will be transfered out of the archive each month; OCLC's Digital Archive does not have a end-user dissemination component.</p>
<table>
<tr>
<th></th>
<th colspan="2" style="text-align:center;padding: .25em 1.5em; border-bottom: 1px solid black;">OCLC Digital Archive</th>
<th colspan="2" style="text-align:center; border-bottom: 1px solid black;">Amazon S3</th>
</tr>
<tr>
<th></th>
<th>Rate</th>
<th>Cost</th>
<th>Rate</th>
<th>Cost</th>
</tr>
<tr>
<td>Setup Cost</td>
<td colspan="2" style="text-align:center;"><i>- - - redacted - - -</i></td>
<td colspan="2" style="text-align:center;"><i>- - - none - - -</i></td>
</tr>
<tr>
<td>Startup Ingest Cost</td>
<td colspan="2" style="text-align:center;"><i>- - - redacted - - -</i></td>
<td style="padding-right: 1.25em;">$0.10/GB into S3 [#1]</td>
<td>$200</td>
</tr>
<tr>
<td>Initial Storage Cost</td>
<td style="padding-right: 1.25em;">$750/100GB/year [#2]</td>
<td>$15,000/year</td>
<td>$0.15/GB/month</td>
<td>$3,600/year</td>
</tr>
<tr>
<td colspan="5">
<hr style="width: 85%;" /></td>
</tr>
<tr>
<td>Ongoing Ingest Cost</td>
<td colspan="2" style="text-align:center;"><i>- - - redacted - - -</i></td>
<td>$0.10/GB into S3 [#1]</td>
<td>$9/year</td>
</tr>
<tr>
<td valign="top" style="padding-right: 1.25em;">Ongoing Storage Cost</td>
<td valign="top">$750/100GB/year [#2]</td>
<td style="margin-right: 1.25em;">previous year<br />plus $750/year [#3]</td>
<td valign="top">$0.15/GB/month</td>
<td>previous year<br />plus $10.80/year [#3]</td>
</tr>
<tr>
<td colspan="5">
<hr style="width: 85%;" /></td>
</tr>
<tr>
<td>Ongoing Access Cost</td>
<td colspan="2" style="text-align:center;"><em>Not available</em></td>
<td>varies [#1, #4]</td>
<td>$8.16/year</td>
</tr>
</table>
<div style="font-size: 85%; margin-left: 2em; margin-top: 1em;">
Note #1: Amazon S3 also adds charges by HTTP request, but those are considered negligible for the data load and the ongoing accesses.</p>
<p>Note #2: As listed in <a href="http://newsbreaks.infotoday.com/nbReader.asp?ArticleId=49018" title="Information Today Article: OCLC Introduces High-Priced Digital Archive Service">Barbara Quint's article</a>.  Charge is for any part of 100GB used.</p>
<p>Note #3: Additions each year factor in the assumption of adding 90GB/year to the collection.</p>
<p>Note #4: Costs for transfers out of S3 is:  $0.17/GB for the first 10TB/month; $0.13/GB for the next 40TB/month; $0.11/GB for the next 100TB/month; and $0.10/GB for outflowing data over 150TB/month.
</p></div>
<p>For this prototypical example, S3 would cost $3,800 in the first year and roughly $3,615 per year after that, with the added benefit that end-users could access the content without using our infrastructure.  There are costs associated with the OCLC Digital Archive service that had to be redacted from the public version of this table due to a confidentiality clause, but the costs that are assumed for ongoing storage based on Barbara Quint's article are comparable to the quote I got from OCLC and represent a large portion of the total yearly costs.</p>
<p>By way of comparison, we are planning the purchase of 50TB of storage this summer for roughly $250K; that is about $5,000/TB.  Amortize the cost of the hardware over five years and assume 150% of the purchase price represents maintenance, personnel support, and other factors, and we get $2,500/TB/year.  This doesn't include software costs, so it is comparable to S3 in the functions table above; software would have to be written to verify the manifest and file formats on ingest as well as the monthly fixity and virus scanning.  It also represents only one copy of the data; it does not include the duplication across data centers that both Digital Archive and S3 provide.</p>
<h2>Conclusions</h2>
<p>OCLC's Digital Archive product goes pretty far down the path of a preservation-worthy archive of digital files.  The value-added services, in addition to simply storing and retrieving files, make it as close to a one-stop shop as I've seen so far.  Whether outsourced digital preservation services makes sense -- particularly at this price point -- remains to be seen, especially since is hard to make a comparison since I'm betting that most of us aren't (yet) doing all of the ongoing activities with digital preservation masters that Digital Archive is doing.</p>
<p>Amazon's S3 is an inexpensive, network-oriented file hosting service, and as such it doesn't have many of the features built into it that we would want to see in a preservation archive service.  Beyond raw file service, one would need to add layers of software and human activities to perform the functions that Digital Archive provides now.</p>
<p>Looking at OCLC's Digital Archive and Amazon S3 is almost an apples-to-oranges comparison, both in price and in functionality.  Comparing functionality first, S3 is missing critical components of a preservation storage system -- namely, rigorous access control and a content backup/restore facility.  Comparing costs, though, S3 is dramatically cheaper...and has the benefit of serving up large files to end-users using Amazon's distributed infrastructure.</p>
<p>It is possible to level the functionality playing field a bit by taking responsibility for the ongoing maintenance of files in the S3 archive -- those things that Digital Archive offers as value-added services over raw file storage.  An EC2 virtual machine running in Amazon's infrastructure can perform the virus and fixity scanning.  And with good key maintenance (as with passwords, regularly changing the private key and securing it appropriately), S3 could conceivably offsite copies of content stored offline (e.g. burned to preservation quality optical media).  Again, in this scenario one has to take responsibility for refreshing the offline media and occasionally running comparisons against the S3 offsite copy.
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.oclc.org/us/en/digitalarchive/overview/ to http://web.archive.org/web/20081012181719/http://www.oclc.org/us/en/digitalarchive/overview/ on November 13th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.oclc.org/us/en/digitalarchive/about/commitment/default.htm to http://web.archive.org/web/20110830065826/http://www.oclc.org/us/en/digitalarchive/about/commitment/default.htm on August 22nd, 2013.</p>
