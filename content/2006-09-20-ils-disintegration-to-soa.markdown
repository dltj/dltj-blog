---
layout: wordpress-import
status: published
published: true
title: 'The Dis-integration of the ILS into a SOA Environment'
modified: 2006-09-21T03:29:56+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 125
wordpress_url: http://dltj.org/2006/09/ils-disintegration-to-soa/
date: '2006-09-20 23:29:56 -0400'
date_gmt: '2006-09-21 03:29:56 -0400'
category: Library Technology
categories:
- Library SOA
- Raw Technology
tags:
- service-oriented architecture
- library service-oriented architecture
- ngc4lib
- library 2.0
- libraries
comments:
- id: 4499
  author: panlibus
  author_email: ''
  author_url: http://blogs.capita-libraries.co.uk/panlibus/2006/09/21/this_jester_has/
  date: '2006-09-21 13:31:25 -0400'
  date_gmt: '2006-09-21 17:31:25 -0400'
  content: |-
    <strong>This jester has a serious point to make...</strong>

     Disruptive Library Technology Jester Peter Murray follows up on his earlier post, which Richard blogged about yesterday. In &#8220;The Dis-integration of the ILS into a SOA Environment&#8221;, Peter begins to address the vexed question of; &#8220;what...
- id: 4740
  author: Web services in Libraries &laquo; David, the Blog
  author_email: ''
  author_url: http://davidtheblog.wordpress.com/2006/09/26/web-services-in-libraries/
  date: '2006-09-26 18:58:53 -0400'
  date_gmt: '2006-09-26 22:58:53 -0400'
  content: "[...] The Dis-integration of the ILS into a SOA Environment [...]"
- id: 12852
  author: panlibus
  author_email: ''
  author_url: http://blogs.capita-libraries.co.uk/panlibus/2006/09/22/free_to_sru/
  date: '2006-09-22 14:08:04 -0400'
  date_gmt: '2006-09-22 18:08:04 -0400'
  content: "<!--%kramer-pre%-->When you approach things in a different way things
    just start dropping in to place.    Paul in his post yesterday commenting on Peter
    Murray's latest episode of his excellent series of posts around Service Oriented
    Architecture (SOA), referenced some of the work we are doing here at Talis...
    \   Programmatic access that means the user need only interact with a library
    user interface if they want to?<!--%kramer-post%-->"
- id: 26586
  author: SOA and Library Systems (Digital Library Technologies)
  author_email: ''
  author_url: http://www.personal.psu.edu/mum28/blogs/Mairead/2007/06/soa_and_library_systems.html
  date: '2007-10-16 15:59:31 -0400'
  date_gmt: '2007-10-16 19:59:31 -0400'
  content: |-
    <!--%kramer-ref-pre%-->[...] SOA, then shows how it would work with WorldCat as an
    example, and finally how it would enable the "dis-integration" of
    the hitherto monolithic [...]<!--%kramer-ref-post%-->
---
<p>This is part three of a continuing series on the application of the Service Oriented Architecture (SOA) design pattern to library systems.  In the first part, the <a href="/article/defining-soa-by-analogy/">SOA concept was compared to a transportation network</a> and the basic foundation for defining SOA was set down.  The second part <a href="/article/services-in-soa/">described what a "service" in SOA could be</a> and proposed an example using OCLC's WorldCat interface with item status information being pulled from a library catalog system.  That part also left off with a teaser about the juxtaposition of "inventory control system" with "local catalog system" &mdash; a foreshadowing of the topic of this post:  what to do about the <span style="text-decoration: line-through;">Monolithic</span> (<i>er...</i> "Integrated") Library System.</p>
<h2>How did we get where we are today?</h2>
<p>Wikipedia has the most concise description of the state of library automation today:</p>
<blockquote><p>
Before the advent of computers, libraries frequently used a card catalog to index its holdings. Computers were used to automate the card catalog, thus the term <em>automation system</em>.  Since the late 1980s, multi-tasking modules allowed business functions to be integrated. Instead of having to open up separate applications, library staff could now use a single application with multiple functional modules. <footnote>Adapted from "Integrated library system." Wikipedia, The Free Encyclopedia. 20 Sep 2006, 19:29 UTC. Wikimedia Foundation, Inc. 20 Sep 2006 <a href="http://en.wikipedia.org/wiki/Integrated_library_system?oldid=76840266#History" title="Integrated Library System">http://en.wikipedia.org/wiki/Integrated_library_system&oldid=76840266#History</a>.</footnote>
</p></blockquote>
<p>As this article points out, libraries have a grand tradition of applying technology to its business problems.  These "integrated library systems" (ILS) &mdash; so named for their unified functions of public search, circulation (check-in/check-out), acquisitions, and cataloging (description) &mdash; propelled library staff productivity to magnitudes not seen before. "Those systems," notes Marshall Breeding, "came quite close to delivering comprehensive automation for libraries."<footnote>Breeding, Marshall. "Re-Integrating the integrated library system." Computers in Libraries. 25(25): Jan 2005.  20-Sep-2006 <a href="http://www.librarytechnology.org/ltg-displaytext.pl?RC=11340" title="Library Technology Guides:  Re-Integrating the integrated library system -- Breeding, Marshall">http://www.librarytechnology.org/ltg-displaytext.pl?RC=11340</a>.</footnote>  </p>
<p>So why change?  Marshall goes on to say, "the ILS remains shackled to the antiquated print-based paradigm for library automation."  Today's integrated library system is ill-equipped to handle the desired integration of formats (audio, video, journal article) and delivery mechanisms (online versus on-site) of our users.  It is also not a nimble platform; as a single, all-encompassing application, bug fixes and new functionality across the entire must be wrapped in a software distribution to be released to users.</p>
<p>This post is not intended to be an exhaustive examination of the problems with the software design model of current ILS applications; there is a growing body of analysis and commentary on that point.  Rather, the rest of this post seeks to point a way forward &mdash; a path that involves the dis-integration ("un-integration"? or, as Marshall put it, "re-integration"?) of the integrated library system.</p>
<h2>What <em>is</em> the Integrated library System?</h2>
<p>What I propose is that we think back to a time before we had the luxury of an integrated library system, and remember the pieces that over the past few decades we have worked so hard to bring together. <footnote>A note out to those of you outside the library community who still seem to be reading this series, if the blog statistics are to be any guide:  you can help us out with your ideas here &mdash; many of us have had our heads buried in ILS systems for so long (my entire career, for instance) that it is difficult to think outside that box.  Let me know in the comments if I've missed anything.</footnote>  As we start to pull things apart, it will be helpful to think of actions and activities that we and our users do and not on the outcomes or the objects that the actions are performed upon.  It might be tempting to call these actions and activities "Services", but I would like to reserve that word for the SOA notion of services; instead, I'll call these things "Tools."  Keep in mind one of the things that we've already learned:  a single page on Amazon can call on more than 100 services to build up the contents of the page <footnote>"A Conversation with Werner Vogels."  ACM Queue. 4(4): May 2006. 19-Sep-2006 <a href="http://www.acmqueue.com/modules.php?name=Content&#038;pa=showpage&#038;pid=388">http://www.acmqueue.com/modules.php?name=Content&pa=showpage&pid=388</a></footnote> &mdash; by their nature these calls need to be very quick and light-weight.  This is what I've come up with so far as the actions and activities of an ILS:</p>
<h3>Discovery Tool / Indexing Tool</h3>
<p>Sometimes called a "search engine", the term "Discovery" more accurately describes the activity of our users.  There is more here, though, then just splitting off the public interface of the existing ILS.  A true SOA Discovery Tool is more akin to Roy Tennant's <a href="http://roytennant.com/presentations/older/2005niso/" title="PowerPoint Presentation  -  Only Librarians Like to Search, Everyone Else Likes to Find : MARC, Metasearching, &amp;  Marginalization">"Only Librarians Like to Search, Everyone Else Likes to Find"</a> mantra &mdash; there should be one Discovery Tool for the user that, <i>a la</i> Google or Amazon, searches across the entire content space to bring the best information results back to the user.  Maybe it helps to think of the Discovery Tool as a portal through which the user finds any nugget of information available in the library's sphere of content; that nugget may be a book, a journal article, a web page, a video, a dissertation, or any other piece of content.</p>
<p>Speaking of Roy's mantra, I may be showing a bit of a bias here towards one particular solution by pairing the Discovery Tool with an Indexing Tool.  The underlying presumption here is that there will be One Common Index for all library content.  Given the issues surrounding metasearch (particularly the speed at which a metasearch query can be executed), getting a zippy response for a SOA interaction really requires that an index already exist that is used to answer the query.  This bias is fueled, admittedly, by OhioLINK's fortunate position of storing and serving much of the content under license from publishers/producers from our own servers.  When you actually have access to the content and underlying metadata, you can think about creating One Common Index for all of that content.  So use of the Discovery Tool is inexorably linked to the Indexing Tool.</p>
<h3>Inventory Control Tool</h3>
<p>Based on the previous posting, you could probably guess that this tool was coming.  What else would you call an activity that keeps track of what items are located where in, if you'll pardon the analogy, a warehouse full of books?  Inventory Control is a problem that has been solved time and time again with greater and greater efficiency by industries other than libraries, and I think it is about time that we start to be able to take advantage of some of those efficiencies.  (Interestingly enough, I've noticed an increase of "global logistics" companies on the ALA exhibitor floor.  I stopped and talked with one of them, and he mentioned some of the work that his company was doing &mdash; fascinating stuff for perhaps another blog post someday.)  </p>
<p>A library's inventory control challenge is modestly similar to that of a video rental store:  we need to track what is within our confines and what has been "rented."  That leads us right into the next tool.</p>
<h3>Point-of-Sale (<i>a la</i> video rental) Tool / User Directory Tool</h3>
<p>If our inventory control is similar to that of a video rental store, our "check out" is their "rental" and our "check in" is their "return."  If we can make that analogy, our circulation system is a kind of Point-of-Sale system. <footnote>For a definition and description of Point-of-Sale systems, I recommend <a href="http://en.wikipedia.org/wiki/Point_of_sale" title="Point of Sale -- Wikipedia">this Wikipedia article</a>.</footnote></p>
<p>If that analogy holds, then their customer database is like out patron database.  In any case, we will need a User Directory Tool where demographic information is kept as well as information about users' "rentals."  The User Directory Tool can also be a source of authentication and authorization as well as other functions such as storing recommendations and annotations.  (More on this topic to come at a later time.)</p>
<h3>Ordering and Receiving Tool</h3>
<p>This, quite frankly, has to be the least "library" of all of the components that make up an ILS.  After all, doesn't just about every business have some sort of acquisitions, receiving, and accounts payable workflow?  Is there anything about an Ordering and Receiving Tool that is unique to the libraries?  From a broad perspective, what is being "bought" is a description of an item &mdash; a record number, if you will, coming out of the Description Tool (see below).</p>
<h3>Description Tool</h3>
<p>If ordering and receiving is the least "library-like" aspect of the ILS, item description has to be the most uniquely library activity.  Who else gets as passionate about how items are described?  Large parts of our professional training are devoted to the creation and use of descriptive metadata.  (For the outsiders peeking into the library profession through these postings:  yes, it's true...this is what most librarians, at some level, get really excited about.)</p>
<p>Unlike the integrated library systems in use today, however, our next generation Description Tool must be multi-lingual:  MARC <footnote><a href="http://en.wikipedia.org/wiki/MARC_standards" title="MARC Standards">Machine Readable Cataloging</a></footnote>, while very expressive to the point of obsessive, cannot capture all of the information about every object.  If metadata is going to truly encapsulate the descriptive fidelity of the object, we need to look at standards other than MARC.  For example, OhioLINK's current media content repository has object that are digitized bird calls; the description of those audio files includes elements such as genus and species, the type of microphone used to record the bird call, and a notation of whether the bird was seen or not seen.  Odds are those elements will never find their way into MARC, so the Description Tool must be able to pull together schema such as the <a href="http://services.natureserve.org/technical2/species_schema.jsp" title="NatureServices: Acknowledgements">Nature Services Species Schema</a>, some other schema that describes recording devices, and something that we'll likely have to make up to represent whether the bird was observed.  (See, I told you we were obsessive about description.)  In addition, a really good Description Tool would pull in authority files and ontologies of various sorts, beyond the Name Authority File and Library of Congress Subject Headings that enable similar topics to be grouped together.  Above all, this tool needs to be easy to use to promote a quick workflow and response SOA Service requests.</p>
<h2>What's Next</h2>
<p>There is more to come in our exploration of general Tools and specific Services that we might find in a Library Service Oriented Architecture environment.  The next posting in this series, however, will explore the important distinction between SOA and another buzz-phrase making the rounds:  "Web Services".</p>
<p>Thanks go out to <a href="http://blogs.capita-libraries.co.uk/panlibus/2006/09/20/a_library_soa_e/" title="panlibus">Richard Wallis at Talis</a> and <a href="http://orweblog.oclc.org/archives/001148.html" title="Lorcan Dempsey&#039;s weblog: D2D in Ohio">Lorcan Dempsey at OCLC</a> for their comments so far.  I'm on the home stretch towards a plateau in this series and which point I'll take a step back, absorb your observations, and reflect them back out in subsequent postings.  Everyone else, please feel free to join in on the conversation as well, whether it be through comments here or commentary elsewhere.</p>
<p>[20060921T0820 Missed the "p" in Lorcan's last name -- my humble apologies, Lorcan.]
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://en.wikipedia.org/wiki/Integrated_library_system&oldid=76840266#History to http://en.wikipedia.org/wiki/Integrated_library_system?oldid=76840266#History on January 13th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://blogs.talis.com/panlibus/archives/2006/09/a_library_soa_e.php to http://blogs.capita-libraries.co.uk/panlibus/2006/09/20/a_library_soa_e/ on August 27th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.cdlib.org/inside/news/presentations/rtennant/2005niso/ to http://roytennant.com/presentations/older/2005niso/ on November 13th, 2012.</p>
