---
layout: wordpress-import
status: published
published: true
title: 'Amazon Catalog Updates'
modified: 2010-05-13T02:19:19+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1564
wordpress_url: http://dltj.org/?p=1564
date: '2010-05-12 22:19:19 -0400'
date_gmt: '2010-05-13 02:19:19 -0400'
category: Blue Sky
categories:
- Blue Sky
tags:
- Amazon
- metadata
- Open Library
- crowdsourcing
comments:
- id: 68904
  author: JW
  author_email: john@booksbychance.com
  author_url: ''
  date: '2010-05-12 22:39:08 -0400'
  date_gmt: '2010-05-13 02:39:08 -0400'
  content: "I've never been entirely clear on how Amazon resolves cataloging conflicts,
    such as when two books have the same ISBN. One person says the title is X and
    another says it is Y and then a third says it is X. You get it. I can't recall
    Amazon ever rejecting a change I suggested (out of a few dozen). In my experience
    as a bookseller, the system works well overall.\r\n\r\nAmazon also let's sellers
    create new records. This too works well overall, but contributes to the occurrence
    of many slightly different entries for the same edition, especially for pre-ISBN
    books."
- id: 69009
  author: Jonathan Rochkind
  author_email: rochkind@jhu.edu
  author_url: http://bibwild.wordpress.com
  date: '2010-05-13 11:11:28 -0400'
  date_gmt: '2010-05-13 15:11:28 -0400'
  content: "Very interesting! I think something like this is DEFINITELY what libraries
    should be trying to do. But our broken 'cooperative cataloging' workflow where
    none of us end up sharing local changes with each other would limit it's utility
    until we do that. Just my libraries users, not critical mass. Worldcat, yes critical
    mass. \r\n\r\nMeanwhile on the Amazon front -- does this feature let you correct
    broken ISBNs too?  There are occasionally wrong ISBNs in Amazon, which end up
    causing Umlaut to fetch wrong data when using amazon api calls.  It would be sweet
    if I could fix em myself when encountered."
- id: 69182
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-05-14 09:23:03 -0400'
  date_gmt: '2010-05-14 13:23:03 -0400'
  content: "<p>JW: Its not clear to me how Amazon resolves conflicts either, and unfortunately
    I don't have any inside sources at Amazon to query.  I got a sense of <a href=\"http://dltj.org/article/mashups-of-bib-data/\"
    rel=\"nofollow\">how Google (and Internet Library and OCLC) deal with the same
    problem</a> at an <acronym title=\"American Library Association\">ALA</acronym>
    forum in January.  Google does it with a statistical inference method based on
    a large number of sources of records.  That technique probably doesn't work for
    Amazon's catalog, so I suspect there is an army of cataloger-types that resolve
    conflicts from the product information feeds from its sources as well as these
    one-off reports by individuals through the process described in this post.  Thanks
    for reporting your experiences!</p>\r\n\r\nJonathan: A good question about correcting
    ISBNs.  The metadata correction form does not include a field for suggesting a
    corrected ISBN (see <a href=\"http://dltj.org/wp-content/uploads/2010/05/amazon-catalog-update-form.png\"
    title=\"Full Amazon metadata correction form\" rel=\"nofollow\">the full version
    of the form</a> as an image).  Since that is used as an identifier, I can imagine
    it wrecks a bit more havoc with their systems if it gets changed.  Toss into that
    the fact that ISBNs are representing different manifestations (the hardcover version
    gets one, the softcover one gets another, the Kindle version gets yet a third,
    and the iBookstore one gets a different one, too) that trying to reconcile all
    of this might be more than Amazon wants to take on.  Of course, it is of great
    interest to us in the library community.\r\n\r\nThese are great questions, and
    I'll try to find some answers.  If anyone else has insights, please share them
    here."
- id: 69198
  author: Ron Murray
  author_email: rmur@loc.gov
  author_url: ''
  date: '2010-05-14 11:04:44 -0400'
  date_gmt: '2010-05-14 15:04:44 -0400'
  content: "I agree that \"someone\" like OCLC could (to its benefit to be sure) host
    a \"resource description correction and enhancement\" service, and support community
    coordination of the correction &amp; enhancement process. Things to consider:\r\n\r\n*
    Surveillance - Who is out there discovering erroneous information? What types
    of mistakes are to be attended to?\r\n\r\n* Reportage - Form based reportage &agrave;
    la Amazon is the way to go.\r\n\r\n* Review - The same population doing the surveillance
    - or some subset of stalwarts &ndash; can perform review and verification tasks.
    Review the reviewer reviewing the reviewer...\r\n\r\n* Correction - Up to the
    utilities, but certainly some kind of notification system keyed to unique (enough)
    IDs would be involved.\r\n\r\n* Costs, rights to community provided information
    - I punt...\r\n\r\n* Etc.\r\n\r\nHow to get started on this? Talk it up on the
    Jester!"
- id: 69203
  author: Jonathan Rochkind
  author_email: rochkind@jhu.edu
  author_url: http://bibwild.wordpres.com
  date: '2010-05-14 11:56:32 -0400'
  date_gmt: '2010-05-14 15:56:32 -0400'
  content: "Peter, yeah, not surprising that Amazon doesn't let you correct ISBNs
    without intermediation. \r\n\r\nHowever, when I've found a bad ISBN in the past,
    and reported it to Amazon simply using the feedback form, the ISBNs do seem to
    get corrected in a fairly timely manner."
- id: 69844
  author: Jean Small
  author_email: jeans@oldhampl.org
  author_url: ''
  date: '2010-05-18 11:43:27 -0400'
  date_gmt: '2010-05-18 15:43:27 -0400'
  content: does anyone know how you get a z39.50 connection to amazon's catalog?
- id: 69846
  author: Jonathan Rochkind
  author_email: rochkind@jhu.edu
  author_url: http://bibwild.wordpress.com
  date: '2010-05-18 11:52:16 -0400'
  date_gmt: '2010-05-18 15:52:16 -0400'
  content: 'Jean: You can not.'
- id: 69847
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-05-18 11:55:13 -0400'
  date_gmt: '2010-05-18 15:55:13 -0400'
  content: To the best of my knowledge, Amazon doesn't speak z39.50.  [Insert commentary
    here about the isolating nature of library-specific standards.]  They do have
    a machine interface that they call the <a href="https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html"
    rel="nofollow">Product Advertising API</a> which they expect you to use -- as
    the name would suggest -- as a way to drive customers to items in the Amazon catalog.  That
    is probably the closest they come to what we in the library community would think
    of as a catalog connection.
- id: 69850
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-05-18 12:13:49 -0400'
  date_gmt: '2010-05-18 16:13:49 -0400'
  content: By the way -- I'm still trying to make contact with the appropriate people
    at Amazon to see if I can get some insights into their metadata practices and
    discover what we might be able to learn from them.
- id: 84297
  author: NARESH
  author_email: msnareshkumar@yahoo.com
  author_url: http://www.yahoo.com
  date: '2010-08-20 13:00:31 -0400'
  date_gmt: '2010-08-20 17:00:31 -0400'
  content: I want to know more about new technologies
- id: 159785
  author: openinnovation
  author_email: ''
  author_url: http://twitter.com/openinnovation3/status/42658937614516224
  date: '2011-03-01 18:54:17 -0500'
  date_gmt: '2011-03-01 23:54:17 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Amazon Catalog Updates | Disruptive Library Technology
    Jester:  http://bit.ly/hh7Hcw</span></span>'
- id: 161415
  author: Fred Leise
  author_email: ''
  author_url: http://twitter.com/chicagoindexer/status/15707894619
  date: '2010-06-08 13:57:10 -0400'
  date_gmt: '2010-06-08 17:57:10 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Interesting: Amazon lets customers suggest corrections
    to its product metadata. http://tinyurl.com/24u4f67</span></span>'
- id: 161416
  author: Alyssa Briggs
  author_email: ''
  author_url: http://twitter.com/alyssa_briggs/status/15492798753
  date: '2010-06-05 15:12:29 -0400'
  date_gmt: '2010-06-05 19:12:29 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT @OPLIN: For serious catalogers only: http://bit.ly/czuq4a
    Did you know that Amazon offers a facility to make corrections to its catalog?</span></span>'
- id: 161417
  author: OPLIN
  author_email: ''
  author_url: http://twitter.com/oplin/status/15429760396
  date: '2010-06-04 17:06:08 -0400'
  date_gmt: '2010-06-04 21:06:08 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">For serious catalogers only: http://bit.ly/czuq4a
    Did you know that Amazon offers a facility to make corrections to its catalog?</span></span>'
- id: 161418
  author: Karen
  author_email: ''
  author_url: http://twitter.com/karen_from_ohio/status/14250265514
  date: '2010-05-18 21:10:04 -0400'
  date_gmt: '2010-05-19 01:10:04 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Amazon Catalog Updates | Disruptive Library Technology
    Jester - http://ow.ly/1MGJo</span></span>
- id: 161419
  author: Cabot Library
  author_email: ''
  author_url: http://twitter.com/cabotlibrary/status/14167262679
  date: '2010-05-17 15:24:17 -0400'
  date_gmt: '2010-05-17 19:24:17 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">"Amazon Catalog Updates" #corrections #bibliographicdata
    #libraries: http://bit.ly/bJiJqr (shows how readers can correct data in Amazon)</span></span>'
- id: 161420
  author: Cammie
  author_email: ''
  author_url: http://twitter.com/cammiesthoughts/status/14058919613
  date: '2010-05-15 21:15:25 -0400'
  date_gmt: '2010-05-16 01:15:25 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">"Did you know that Amazon offers a facility to
    make corrections to its catalog?" via Dltj http://bit.ly/aSnbBD</span></span>
- id: 161421
  author: Garrett Eastman
  author_email: ''
  author_url: http://twitter.com/notinmy/status/14015730371
  date: '2010-05-15 03:32:39 -0400'
  date_gmt: '2010-05-15 07:32:39 -0400'
  content: |-
    <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span class="topsy_trackback_content">"    *

    Amazon Catalog Updates" #corrections #bibliographicdata #libraries: http://bit.ly/bJiJqr</span></span>
- id: 161422
  author: Suzuki Takao
  author_email: ''
  author_url: http://twitter.com/suzuki_takao/status/13925576491
  date: '2010-05-13 17:34:24 -0400'
  date_gmt: '2010-05-13 21:34:24 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Amazon Catalog Updates | Disruptive Library Technology
    Jester http://bit.ly/bLaaqJ</span></span>
- id: 230247
  author: Crowdsourcing &mdash; Council on Library and Information Resources
  author_email: ''
  author_url: http://www.clir.org/pubs/reports/pub152/linked-data-survey/part11_c_tools.html
  date: '2012-03-09 18:24:44 -0500'
  date_gmt: '2012-03-09 23:24:44 -0500'
  content: "<!--%kramer-ref-pre%-->[...] j. Peter Murray Amazon catalog updates [...]<!--%kramer-ref-post%-->"
---
<p>Did you know that Amazon offers a facility to make corrections to its catalog?  Somewhere in the past few months someone mentioned this to me and I tried it out.  (<del datetime="2010-05-14T13:34:39+00:00">Unfortunately, it has been long enough now that I've forgotten who told me; if you are the one, please fess up in <a href="/article/amazon-catalog-updates/#respond">this post's comments section</a>.</del> <ins datetime="2010-05-14T13:34:39+00:00">It was Ron Murray from the Library of Congress.  Thanks, Ron!</ins>)  And it works!  Is this a model for crowdsourced corrections to library data?<br />
<!--more--><br />
Here is how it looks from a user's perspective.</p>
<h2>Step 1. Finding something to correct</h2>
<p>Amazon has a pretty good catalog, so for the purposes of demonstrating this feature it took a while to find a record to correct.  I used the suggestions from <a href="http://librarytypos.blogspot.com/" title="Typo of the day for librarians">Typo of the Day for Librarians</a> for ideas of errors to look for in the Amazon catalog.  One of the suggested typos was <a href="http://librarytypos.blogspot.com/2010/03/sucess-etc-for-success-etc.html" title="Typo of the day for librarians: Sucess*, etc. (for Success, etc.)">Sucess*, etc. (for Success , etc.)</a>, and I found a record for <a href="http://www.amazon.com/How-Talk-Anyone-Success-Relationships/dp/1593160267/" title="Amazon product page for &#039;How to Talk to Anyone&#039;">How to Talk to Anyone: 62 Little Tricks for Big Success in Relationships</a> in audio CD format with this misspelling.  As this image shows, the original title was "How to Talk to Anyone: 62 Little Tricks for Big <em>Sucess</em> in Relationships"<br />
[caption id="attachment_1583" align="aligncenter" width="672" caption="Amazon page for \'How to Talk to Anyone\' with typo"]<a href="/wp-content/uploads/2010/05/amazon-page-with-typo.png"><img src="/wp-content/uploads/2010/05/amazon-page-with-typo-cropped.png" alt="" title="Amazon page for &#039;How to Talk to Anyone&#039; with typo" class="size-full wp-image-1583" width="672" height="396"/></a>[/caption]</p>
<h2>Step 2. Making the Correction</h2>
<p>In the "Product Details" section of the Amazon catalog page is a link to "update product info"<br />
[caption id="attachment_1586" align="aligncenter" width="672" caption="Excerpt of Amazon product information page with the \'update product info\' link highlighted"]<a href="/wp-content/uploads/2010/05/amazon-page-with-typo.png"><img src="/wp-content/uploads/2010/05/amazon-page-with-typo-cropped-2.png" alt="" title="Excerpt of Amazon product information page with the &#039;update product info&#039; link highlighted" class="size-full wp-image-1586" width="672" height="328"/></a>[/caption]<br />
Following that link takes you to a form that is prefilled with all of the information from the Amazon catalog.  You can make your corrections here and provide citation URLs to reference the source of the correct information.  (In the excerpt of the form on this page only the Title and Reference sections are show.  Click through the image to see the full version of the form.)<br />
[caption id="attachment_1587" align="aligncenter" width="820" caption="Excerpt of Amazon Catalog Update Form"]<a href="/wp-content/uploads/2010/05/amazon-catalog-update-form.png"><img src="/wp-content/uploads/2010/05/amazon-catalog-update-form-cropped.png" alt="" title="Excerpt of Amazon Catalog Update Form" class="size-full wp-image-1587" width="820" height="573"/></a>[/caption]<br />
You are given a chance to preview your changes before submitting them.  Note in this case that the reference URL I'm using is actually a link to the cover image for this item at Amazon.  A bit of neat symmetry there, I figure.<br />
[caption id="attachment_1589" align="aligncenter" width="820" caption="Preview of Amazon Catalog Updates"]<a href="/wp-content/uploads/2010/05/amazon-catalog-update-preview.png"><img src="/wp-content/uploads/2010/05/amazon-catalog-update-preview-cropped.png" alt="" title="Preview of Amazon Catalog Updates" class="size-full wp-image-1589" width="820" height="400"/></a>[/caption]<br />
After submitting the changes, you get a nice "thank you" from Amazon for making their service better.<br />
[caption id="attachment_1590" align="aligncenter" width="820" caption="Submission confirmation page from Amazon Catalog Update service"]<a href="/wp-content/uploads/2010/05/amazon-catalog-update-submitted.png"><img src="/wp-content/uploads/2010/05/amazon-catalog-update-submitted-cropped.png" alt="" title="Submission confirmation page from Amazon Catalog Update service" class="size-full wp-image-1590" width="820" height="145"/></a>[/caption]</p>
<h2>Step 3. Getting Confirmation from Amazon</h2>
<p>After a bit -- mere hours in my case -- Amazon will send you a confirmation back that the correction has been accepted.</p>
<blockquote><p>From: "gfix-noreply@amazon.com" <gfix -noreply@amazon.com><br />
To: "peter@OhioLINK.edu"
<peter @OhioLINK.edu>
Subject: Your Amazon.com Catalog Update Request</p>
<p>==== This is an automated response message - please do not reply ====</p>
<p>Thank you for using the Catalog Update Form to send suggestions for</p>
<p>How to Talk to Anyone: 62 Little Tricks for Big Sucess in Relationships (ASIN 1593160267)</p>
<p>Your update has been accepted and processed. It will appear online within the next two to three business days.<br />
Attribute: Title<br />
Current value:<br />
How to Talk to Anyone: 62 Little Tricks for Big Sucess in Relationships </p>
<p>Your suggestion:<br />
How to Talk to Anyone: 62 Little Tricks for Big Success in Relationships </p>
<p>Data accuracy is highly important to us. We appreciate the time you have taken to submit your updates to us.</p>
<p>Best regards,</p>
<p>Catalog Department<br />
www.amazon.com</p></blockquote>
<p>And if you go to this <a href="http://www.amazon.com/How-Talk-Anyone-Success-Relationships/dp/1593160267/" title="http://www.amazon.com/How-Talk-Anyone-Success-Relationships/dp/1593160267/">product page now</a> you'll see the title has been corrected.</p>
<h2>Would this Work for Libraries?</h2>
<p>Now Amazon must have some resources backing up this service to do the verification of submissions.  And it makes sense for them because corrected metadata makes it easier for their products to be found and purchased.  If libraries were to consider providing an equivalent service for our metadata, could we justify the costs?  Is this a good use of our time and effort?</p>
<p>If we were to do it, I think it might have to be done by a bibliographic utility like OCLC who has ways to push the updated records to member libraries.  Otherwise we run the risk of diluting the corrections across many individual library catalogs.  Interestingly, this sort of user-generated correction facility one that the <a href="http://openlibrary.org/" title="Open Library homepage" rel="homepage">Open Library</a> already provides. (Open Library is a wiki-like service that offers the ability for anyone to make changes to its records, much like how <a href="http://en.wikipedia.org/wiki/Welcome_to_Wikipedia" title="http://en.wikipedia.org/wiki/Welcome_to_Wikipedia">anyone can edit articles on Wikipedia</a>.)  So between Amazon and Open Library there is a continuum of workflows of mediated corrections to unmediated corrections for us to consider.  This scheme, of course, begs us to consider the notion of <a href="http://journal.code4lib.org/articles/86" title="The Code4Lib Journal &amp;#8211; Distributed Version Control and Library Metadata">distributed version control systems for handling our bibliographic data</a> so that changes can be merged across many sources.</p>
<p>Lots to think about...</peter></gfix></p></blockquote>
