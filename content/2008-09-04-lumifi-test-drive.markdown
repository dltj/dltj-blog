---
layout: wordpress-import
status: published
published: true
title: 'Test Driving Lumifi'
modified: 2008-09-04T14:09:49+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 444
wordpress_url: http://dltj.org/?p=444
date: '2008-09-04 10:09:49 -0400'
date_gmt: '2008-09-04 14:09:49 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- review
- search engine
comments: []
---
<p>Earlier this week, Lumifi Inc. <span class="removed_link" title="http://lumifinews.com/2008/08/29/lumifi-redefines-research-and-collaboration/">announced a new version of their research platform</span> "to better serve students, professionals and others in dealing with information overload."  Lumifi is a <a href="http://www.vator.tv/pitch/show/lumificom-lumificom---enlighten-your-search" title="lumifi.com company profile on Vator.tv">private corporation</a> based in Maryland, and this is their second major release of their service.  (The first was <a href="http://www.901am.com/2008/lumifi-unveils-research-and-collaboration-portal.html" title="Lumifi unveils research and collaboration portal press release">announced</a> in January 2008.)  I didn't see the first interface so I can't compare it to the earlier effort, but on the whole I am unimpressed.  There may be some new magic happening behind the scenes here, but it is hidden in an awful interface that is very difficult to get past.</p>
<p>This is what Lumifi has to say about itself:</p>
<blockquote><p>Lumifi's contextual analysis system represents a major advancement in web and document research technology.  At the heart of the system is the Synapse engine, a proprietary software technology that analyzes content to find connections and relationships between words using statistical semantic analysis.  By aggregating and analyzing these relationships, Synapse produces highly targeted, contextual insight that is not possible with traditional indexing or search applications.</p>
<p>At its core, Synapse's analysis is the product of two code paths &ndash; a data-mining engine and semantic analysis engine.  They work in concert to find the most statistically significant topics, sentences and paragraphs from unstructured text.  These engines include a number of sophisticated algorithms and components, including a stream-capable sentence and phrase parser, a statistical keyword and keyphrase analyzer, a semantic network optimizer and a real-time context generator.</p></blockquote>
<p>I took it for a test drive, and spent much of my time trying to figure out how the interface works.</p>
<h2>Trying It Out</h2>
<div id="attachment_448" class="wp-caption aligncenter" style="width: 726px;">[flash http://media.dltj.org/Lumifi-testdrive.flv w=720 h=480]
<p class="wp-caption-text">Screencast recording of the Lumifi testdrive (approx. 7 minutes).  Also available for <a href="http://media.dltj.org/Lumifi-testdrive.flv">download</a> in Flash format.</p>
</div>
<p>One needs to register for a free account in order to put Lumifi through its paces.  (There are canned searches on the home page that one can try -- "Global Warming" and "The Origin of Species by Charles Darwin" -- but one can only affect the ranking and weighting of results.)  The interface comes with no documentation, tool tips, or other clues as how to exploit it, so it is entirely possible that I'm missing some of the power of the interface. {{ image(
    div_float="right",
    width="300",
    caption="Sample search for 'pollen allergy' in the Lumifi interface.",
    alt="Sample search for \"pollen allergy\" in the Lumifi interface.",
    localsrc="2008/09/lumifi_example_search-300x255.png",
    localhref="/assets/images/2008/09/lumifi_example_search.png") }}
 After performing a search -- "pollen allergies" in this case -- the screen is broken up into two columns.  On the right is a summary that, based on the poor English constructs, appears to be extracted from the identified web pages; it is followed by web pages entries.  On the left is a "Focus" box with a text input field, a "Best Results" box with 'most relevant titles,' and a "Topics" box.  Selecting one of the topics changes the results display.</p>
<p>One can input in a "Focus" term (also interchangeably called a "Skewing Term" it would appear) and the search results on the right side change.  The Summary, Best Results, and Topics don't change, though.  This seems to be a weak form of limiting, but the results are not very satisfying because it only affects one portion of the results.</p>
<p>There are options in the Summary box to "Copy summary", "Copy website(s)," and "Copy note(s)" but the options don't appear to do anything.  They certainly don't put data on the computer's clipboard that can be pasted into another application.  In fact, many of the functions assume that Lumifi will be the center of the universe.  One can upload documents to the site, but that seems to have limited value other than just storing them in Lumifi.</p>
<h2>Lumify - The Technology</h2>
<p>Quoting several paragraphs from the "Lumifi Technology" panel of the flash applet:</p>
<blockquote><p>Utilizing an advanced service-oriented architecture (SOA), Lumifi is both scalable and easily extendable.  Lumifi is developed in accordance with industry best practices and leverages standards and open source software from across the computing platform.  These include: XML for the API, JAAS for authentication, J2EE for scaleability and portability, SQL for universal database support, JMS for activity monitoring, and Adobe Flex for the rich user interface.  The adherence to standards allows Lumifi to be effortlessly installed in the enterprise, either using the open source components that Lumifi currently leverages or using other standards-supporting technologies that the enterprise may currently license.</p></blockquote>
<p>This all sounds good.  J2EE is a Java-based standard for deploying server applications across many computing environments.  JAAS and JMS are standards within the Java community for J2EE applications.  SQL is the standard language for relational databases, so it sounds like the Lumifi application will use everything from the freely available MySQL and Postgresql databases up to the proprietary Oracle and DB2.</p>
<blockquote><p>Although, Lumifi contains a rich, brandable, user interface based on the Adobe Flex technology, Lumifi's XML/REST-based architecture allows Lumifi services to be embedded in any internet-aware technology. Lumifi implements a simple yet powerful security model that allows for user authentication, document sharing and intuitive access controls.</p></blockquote>
<p>I'm going to take Lumifi to task below for its use of Flex/Flash as the primary demonstration interface to the technology.  In short, Flex/Flash results in a clunky, if glitzy, user interface.  The mention of "XML/REST-base architecture", though, gives one hope that the Lumifi-supplied interface can be thrown out entirely and embedded in more traditional interface designs.  There isn't any documentation or other examples, though, of the XML/REST interface.</p>
<blockquote><p>Lumifi's unique architecture allows features to be easily added and extended; any feature can be provisioned based on any aspect of a user's profile.  This permits Lumifi to enable features on an individual basis, on a class basis, or even on a demographic basis.  Accordingly, Lumifi can target features to users according to virtually any criteria.</p></blockquote>
<p>With limited information about <em>how</em> it could be extended, it is difficult to judge <em>how easily</em> it could be extended.</p>
<h2>Lumifi - The User Experience</h2>
<p>Although the underlying technology may be based on sound principles of an open architecture, the way they decided to show it off is anything but open from a technological perspective.  That is, the user interface is based entirely on a 1MB Flash applet downloaded to the browser that is scaled to fit the entire screen.  This is wrong on so many levels it is hard to know where to start:</p>
<ul type="disc">
<li><strong>It violates the principles of the Web Architecture.</strong>  You know how you usually can bookmark a page and return to that exact spot of your discovery process later?  Or how you can share a URL with someone and know that they are seeing exactly what you are seeing?  That is how the web works -- how it is architected.  The web architecture is based on the notion that the context embodied in a URL is all you need to get back a page.  Lumifi has chosen to go outside the web architecture by embedding all of the context in the flash applet.  They appear to be exploiting some Flash tricks to change the URL somewhat (after searching for "pollen allergies" above the URL change to <span class="removed_link" title="http://www.lumifi.com/lumifi/index.jsp#app=252c&amp;55e1-selectedIndex=2&amp;57ec-selectedIndex=0&amp;8ba-selectedIndex=0&amp;9c53-selectedIndex=0&amp;dadc-selectedIndex=0&amp;e0fb-selectedIndex=0">http://www.lumifi.com/lumifi/index.jsp#app=252c&amp;55e1-selectedIndex=2&amp;57ec-selectedIndex=0&amp;8ba-selectedIndex=0&amp;9c53-selectedIndex=0&amp;dadc-selectedIndex=0&amp;e0fb-selectedIndex=0</span>).  The changes are in the <a href="http://tools.ietf.org/html/rfc3986#section-3.5" title="URI standard">fragment</a> portion of the URL, but this doesn't seem to be an appropriate place to put server-side state.  In particular, the URLs don't work if you aren't actually signed into the Lumifi system.  (You just see the front page with no indication as to the special nature of the URL.)</li>
<li><strong>The applet assumes a large window size.</strong>  {{ image(
    div_float="right",
    width="150",
    caption="Example of a Lumifi window that is cropped because the browser window is not large enough.",
    alt="Example of a Lumifi window that is cropped because the browser window is not large enough.",
    localsrc="2008/09/cropped_lumifi_window-150x150.png",
    localhref="/assets/images/2008/09/cropped_lumifi_window.png") }}
 I was initially hampered by the fact that my browser window size was not set to the maximum.  There were parts of the flash applet that I could not see because my window wasn't large enough.  Based on some experimentation, it looks like the applet assumes that your browser window will be taller than about 680 pixels and wider than about 762.  If it isn't, you'll not only loose information (such as the bottom-most links in the left navigation panel), but you also get dueling scroll-bars, as in the middle and right panels.</li>
<li><strong>The applet is huge.</strong>  There is no real indication as to what is going on while it is loading, and a number of times I've thought the site itself was down because the only thing I was seeing was a blank screen.  1MB, even in today's predominantly broadband internet days, is still quite big.</li>
</ul>
<p>The interface itself is very confusing.  I found that options are hidden behind nondescript icons and that the site design deviates enough from user interface conventions that it makes the service hard to use.  Other parts of it seem to be broken, like the fact that it remembered I had set a focus/skewing term of trees even after I had cleared it.  Or that adding a focus/skewing term didn't change the topics listed in the left column of the display.</p>
<p>In addition to all of that, the Flash applet seems to needlessly command the attention of the computer's processor -- even when it isn't doing anything.  (There is no network activity that I can determine when idle -- it just forces the browser to consume about 40% of an otherwise idle CPU.)  This is true at least on a Mac PowerBook using the Safari browser.</p>
<h2>Some Conclusions</h2>
<p>At this point, I think it is "Please Move On; Nothing to See Here."  From an OhioLINK perspective, it may be possible to use this as an enhanced search engine that is inferring relationships between journal articles in our Electronic Journal Center, book chapters in our Electronic Book Center, and items in the Digital Resource Commons.  There is no mention of the capacity limits of the system, however, and to cover all of that OhioLINK content would require an engine capable of handling several tens of millions of objects.  A Google search for "pollen allergies" returns 1.7 million hits; the Lumifi search returns 39 "most relevant".  It is impossible to know whether the smaller number is due to a more advanced relevance ranking or simply a limited pool of possible results.</p>
<p>More to the point, I can't envision keeping my research in Lumifi -- especially given that I can't edit documents, build bibliographies, or perform other necessary research options.  On the search screen, the "Topics" may be semantically derived based on the results of the initial search, but there are other engines that do the same.  There might be good technology here, but it is very hard to find it given their choice to use a full-window Flash applet as its delivery mechanism.  It would certainly take more follow-up with them, and more information other than flowery phrases in the service itself ("wow professors with the depth and substance of your knowledge" and "add credibility to your paper or project with citable resources").  At this point I don't believe it would be worth the effort.</p>
<p>If anyone else tries out Lumifi and comes to different conclusions, please let me know.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.lumifi.com/lumifi/index.jsp#app=252c&55e1-selectedIndex=2&57ec-selectedIndex=0&8ba-selectedIndex=0&9c53-selectedIndex=0&dadc-selectedIndex=0&e0fb-selectedIndex=0 on February 11th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://gbiv.com/protocols/uri/rfc/rfc3986.html#fragment to http://tools.ietf.org/html/rfc3986#section-3.5 on November 13th, 2012.</p>
