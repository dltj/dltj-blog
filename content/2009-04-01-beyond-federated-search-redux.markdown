---
layout: wordpress-import
status: published
published: true
title: 'Beyond Federated Search Redux'
modified: 2009-04-01T21:03:04+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 847
wordpress_url: http://dltj.org/?p=847
date: '2009-04-01 17:03:04 -0400'
date_gmt: '2009-04-01 21:03:04 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- metasearch
- open access
- discovery
comments:
- id: 35121
  author: Jonathan Rochkind
  author_email: rochkind@jhu.edu
  author_url: http://bibwild.wordpress.com
  date: '2009-04-01 18:34:01 -0400'
  date_gmt: '2009-04-01 22:34:01 -0400'
  content: "In fact, I think the Summon approach, which is what Carl originally wrote
    was a marker of our loss of control, _potentially_ provides the _technological_
    means for us to regain control. \r\n\r\nConsider broadcast federated search. We
    are _stuck_ with the search packages that vendors give us. You can offer a federated
    search that combines a particular EBSCO db with a particular Wilson db. But there's
    no good way to provide a search that searches only certain journals accross both
    dbs -- unless EBSCO or Wilson provide packages with those journals. \r\n\r\nWith
    Summon, on the other hand, _technologically_ you could provide a search accross
    only certain journals, perhaps organized in subject sets to YOUR liking. \r\n\r\nOf
    course, realistically, who the heck has time to create and maintain such sets
    of journals, accross the tens of thousands of journals that we have?  But I understand
    that SerSol hopes to create some themselves.  You won't have to search accross
    everything in Summon -- for instance, you can already limit to just things your
    institution has in full text. Something our users really want, and which is nearly
    impossible with broadcast search. \r\n\r\nI still don't understand why Carl or
    Sol think that the Summon approach will lead to less control than we have now.
    We already have not that much control, at the whim of our vendors. That may not
    be a good thing, but what makes Summon a step backwards exactly?   If we need
    to do meta-search somehow (and Carl already argued we did at http://federatedsearchblog.com/2008/10/27/we-don&rsquo;t-really-need-metasearch&hellip;/;
    I agree) ...  what's Carl's suggestion of how to do it with more control?  Current
    broadcast search technology sure isnt' doing it. \r\n\r\n[cross-commented to federated
    search blog]"
- id: 35136
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2009-04-03 12:07:09 -0400'
  date_gmt: '2009-04-03 16:07:09 -0400'
  content: "It is probably that my impressions of Carl's post are colored by the fact
    that OhioLINK is in the process of building/acquiring its own unified index to
    content.  We go into this with the weight of the consortium to demand that the
    unified index be representative and comprehensive of the underlying content that
    we've licensed.  The only exception would come in cases where content providers
    won't give up the data to put into a unified index; those will be searched via
    a metasearch engine.  We'd be prepared to push back, though, and say that the
    content that is searched via the metasearch engine will inherently have a \"second
    class\" status in the user interface.\r\n\r\nYou bring up good points about how
    Summon, in particular, doesn't represent a step backwards.  I wonder if Carl will
    formulate a response on the original blog post."
- id: 35157
  author: Brian Despain
  author_email: brian@deepwebtech.com
  author_url: http://www.deepwebtech.com
  date: '2009-04-07 19:09:05 -0400'
  date_gmt: '2009-04-07 23:09:05 -0400'
  content: A unified index meta data repository like Summon doesn't solve the access
    issue but rather it solves a user experience problem in the speed of broadcast
    searches.  In the end I think it's going to be difficult to get publishers to
    agree to provide their meta data for indexing.  At Deep Web we have been developing
    hybrid solutions like Summon for some time - it really helps speed results and
    helps normalize data across publishers.  I am not sure that treating sources that
    don't want to put their meta data in the repository like second class citizens
    is the way to go, it seems like a harsh stick but it goes with the carrot that
    putting your meta data in the repository allows you to scale your content without
    a huge investment of IT resources.
- id: 35161
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2009-04-08 10:17:18 -0400'
  date_gmt: '2009-04-08 14:17:18 -0400'
  content: Just for clarity, I don't think we can call Summon a hybrid solution.  They
    have stated quite emphatically that they have no intention of binding a federated
    search solution with their metadata index.  Personally, I think that is short-sighted
    because I anticipate there will always be cases where the metadata can't be integrated
    into a unified index.  If an institution desired, though, the Serials Solutions
    business model does seem to offer the opportunity for an institution to subscribe
    to the API version of Summon and build its own interface  that integrates a federated
    search system.
- id: 35162
  author: Jonathan Rochkind
  author_email: rochkind@jhu.edu
  author_url: http://bibwild.wordpress.com
  date: '2009-04-08 10:27:01 -0400'
  date_gmt: '2009-04-08 14:27:01 -0400'
  content: "True, Peter, but they've also stated clearly that the out-of-the-box interface
    will be an open source (PHP I think) app which uses an API to the actual Summon
    functionality -- the same API which will be available to customers too. \n\nSo
    there's nothing to stop customers from writing a front-end that IS a hybrid solution,
    using an external broadcast search solution.  I mean, you would have trouble merging
    the results from both, but you could provide the results in seperate listings,
    which is the only realistic thing to do anyway, I think. \n\nI think it's reasonable
    for Summon to limit the scope of their project to not include broadcast search,
    but provide the hooks for you to easily combine it with broadcast search in your
    own hybrid solution. The scope of Summon is big enough already!\n\nI'm actually
    not sure whether to be optimstic about _publishers_  sharing metadata with Summon.
    I would be pessimistic about an A&I db or aggregator sharing metadata with Summon,
    becuase summon will be seen as a competitor. But if Summon isn't actually providing
    access to human-readable fulltext (as they are not) -- do most publishers make
    much money off search of their content alone? Maybe the biggest ones like Elsevier,
    which are also aggregators. But for a publisher who isn't also an aggregator,
    I'm somewhat optimistic that they'd see it as in their interests to share rather
    than withhold metadata.  Having the technical infrastructure to easily and regularly
    deliver the metadata is another story though. \n\n(And, by the way, I consider
    plain text full text used for matching queries but NOT used to actually deliver
    a human-readable version -- to be 'metadata'.  )"
- id: 35163
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2009-04-08 10:49:56 -0400'
  date_gmt: '2009-04-08 14:49:56 -0400'
  content: |-
    Good point about their intention to release the interface of Summon that we saw at ALA Midwinter into open source.  Time will tell if it can be readily modified.  I've also heard from good sources that there is an active effort to put Aquabrowser Library atop the Summon API.

    Here in Ohio, the intention our project is to merge the unified index data with the federated search data.  My gut tells me it will be possible, and I've seen evidence in some systems that it can happen.  We'll see if it happens at scale, though.

    As we chatted about on the <a href="http://code4lib.org/irc/" rel="nofollow">code4lib IRC channel</a> I'm somewhat optimistic that A&amp;I providers may see benefits from putting their data into Summon.  This is based on the assumption that they are getting paid for their data, so it represents a new revenue stream for them.  (I don't know if this is actually the case.)  Unified indexes like Summon aren't necessarily a threat to their core users because the heavy duty researchers will likely need the advanced indexing and search capabilities that an aggregator like Summon won't be able to provide.  For OhioLINK's project, we are operating under the assumption that the unified discovery layer represents a <em>new</em> interface to the data; it doesn't <em>replace</em> existing interfaces where that advanced functionality will still reside.
- id: 35164
  author: Brian Despain
  author_email: brian@deepwebtech.com
  author_url: http://www.deepwebtech.com
  date: '2009-04-08 11:00:59 -0400'
  date_gmt: '2009-04-08 15:00:59 -0400'
  content: I don't see any reason why merging the unified index and the federated
    search data. We have done that for multi-million document full text document sets
    and federated search results. It can be made fairly seamless to users and offers
    the up to date results of broadcast search and the speed &amp; flexibility of
    an index. I think you are right the unified discovery layer represents another
    way to search and explore underlying data, that will most likely lead to increased
    database usage as users use the unified index as a discovery tool
- id: 35165
  author: Jonathan Rochkind
  author_email: rochkind@jhu.edu
  author_url: http://bibwild.wordpress.com
  date: '2009-04-08 11:04:27 -0400'
  date_gmt: '2009-04-08 15:04:27 -0400'
  content: "Brian, how can you present a merged result set without waiting for the
    broadcast search to complete, thus bringing everything down the slowest common
    denominator and NOT offering the speed of an index?\r\n\r\nOh, you're presenting
    incremental results?\r\n\r\nThat's a whole different UI challenge that I've basically
    given up on. I can't figure out any way to have incremental results that are not
    REALLY confusing to users."
- id: 35166
  author: Brian Despain
  author_email: brian@deepwebtech.com
  author_url: http://www.deepwebtech.com
  date: '2009-04-08 11:10:47 -0400'
  date_gmt: '2009-04-08 15:10:47 -0400'
  content: We have also discussed giving users sliders to indicate their preference
    for newer results or more complete results.  The point in the UI is to be seamless
    to users where possible and let users make their choice based on their research
    needs.  If Summon offers a robust enough API, it might be possible to integrate
    outside federated search results. I think it's a bit short sighted as well since
    there always going need to bring some data outside the index.
- id: 73472
  author: Beyond Federated Search &ndash; Winning the Battle and Losing the War? &raquo;
    Federated Search Blog
  author_email: ''
  author_url: http://federatedsearchblog.com/2009/03/30/beyond-federated-search-%e2%80%93-winning-the-battle-and-losing-the-war/
  date: '2010-06-13 12:06:04 -0400'
  date_gmt: '2010-06-13 16:06:04 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Beyond Federated Search Redux | Disruptive
    Library Technology Jester April 1st, 2009 at 2:03 pm&nbsp;&nbsp; [...] started
    with a post by Carl Grant on the Federated [...]<!--%kramer-ref-post%-->"
- id: 160851
  author: Peter Murray
  author_email: ''
  author_url: ''
  date: '2009-04-01 21:03:13 -0400'
  date_gmt: '2009-04-02 01:03:13 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">New blog post: Beyond Federated Search Redux http://dltj.org/article/beyond-federated-search-redux/</span></span>'
- id: 161043
  author: Fed Search Blog
  author_email: ''
  author_url: http://twitter.com/fedsearchblog/status/1449899865
  date: '2009-04-04 04:10:24 -0400'
  date_gmt: '2009-04-04 08:10:24 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Beyond Federated Search Redux. It started with
    a post by Carl Grant on the Federated Search Blog ... http://bit.ly/jEcpg</span></span>
- id: 161044
  author: Fed Search Blog
  author_email: ''
  author_url: http://twitter.com/fedsearchblog/status/1448842911
  date: '2009-04-04 00:24:46 -0400'
  date_gmt: '2009-04-04 04:24:46 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Dirsruptive Library Technology Jester - Beyond
    Federated Search -  http://bit.ly/jEcpg</span></span>
- id: 161045
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/1434360703
  date: '2009-04-01 21:52:00 -0400'
  date_gmt: '2009-04-02 01:52:00 -0400'
  content: "<span class=\"topsy_trackback_comment\"><span class=\"topsy_twitter_username\"><span
    class=\"topsy_trackback_content\">Murray, Peter: Beyond Federated Search Redux:
    \nIt started with a post by Carl Grant on the Federated Search Blog.. http://snipurl.com/f16il</span></span>"
---
<p>It started with a post by <a href="http://www.exlibrisgroup.com/?catid=%7B795BD8B6-47DE-4722-8D5D-B664EEEFB34C%7D" title="Carl Grant's Page at Ex Libris">Carl Grant</a> on the Federated Search Blog:  <a href="http://federatedsearchblog.com/2009/03/30/beyond-federated-search-%E2%80%93-winning-the-battle-and-losing-the-war/" title="Beyond Federated Search blog post">Beyond Federated Search &ndash; Winning the Battle and Losing the War?</a>.  I <a href="http://delicious.com/url/ad53db29e7b7b6df758579af5173aa33" title="Beyond Federated Search at Delicious">bookmarked this in Delicious</a> and copied this extended quote from the text into the bookmark:</p>
<blockquote><p>I&rsquo;ve long argued that librarianship on top of digital information is about the authority/authenticity/appropriateness of the information provided to the user, as opposed to the overwhelming amounts of information available via other search tools that don&rsquo;t provide that differentiation. In order to meet those tests, one thing that is clear is that libraries and librarians should never cede control to other organizations over the content they offer to their end-users. It doesn&rsquo;t matter if that happens because the content providers fail to provide access via federated search, or whether the library has allowed third party organizations to determine what content they can access via a local index discovery tool. Ceding this control cripples the ability of a library to build unique and precise informational offerings that target the needs of their end-users.</p></blockquote>
<p>This in turn got pulled into <a href="http://friendfeed.com/dltj" title="Peter Murray - FriendFeed">my FriendFeed stream</a> and the <a href="http://friendfeed.com/e/463ad9b9-5aa4-dee7-27c5-89b6462578dd/Beyond-Federated-Search-Winning-the-Battle-and/" title="FriendFeed discussion surrounding Beyond Federated Search posting">ensuing discussion</a> seemed too valuable to let sit there, so I'm creating this post with those replies and adding a little bit more of my own thoughts.  (Since all of these were public comments, I believe it is good nettiquete to reproduce them here with attribution.  If not, please let me know...particularly if you are one of the people quoted!)<br />
<!--more--><br />
<span class="removed_link" title="http://friendfeed.com/cavlec">Dorothea Salo</span> was the first to post a comment:</p>
<blockquote><p>1) We HAVE ceded control. So what do we do about that? 2) Authority/authenticity doesn't mean jack to the satisficing patron. Which is IMO most of them. </p></blockquote>
<p>This was followed shortly by <a href="http://friendfeed.com/mndoci" title="http://friendfeed/mndoci">Deepak Singh</a>:</p>
<blockquote><p>That control is long gone.  I think people do care about authority, but IMO, that will come from outside the library community, at least on the technology side.</p></blockquote>
<p>Does everyone really think we have ceded control?  I think we still have it; we just don't market it as an asset to the user like we should/could.  It is "the discovery layer problem" that we are all trying to tackle.  My take on it is that we should put all of the information we can into a unified index with a user interface as simple as Google but with the added advantage of improving relevance of results via fielded data and librarian vetting for authority/authenticity/appropriateness.  I subscribe to the notion that federated search can't take us far enough ... that there is benefit in bringing together metadata for our vetted resources and expanding/enhancing the metadata.  This added-value metadata comes in computing relationships and relevancy between records, attempting to apply uniform headings on records based on machine heuristics, and other tricks that can't be done in real time with small subsets of data that we get back through federated search interfaces.</p>
<p><a href="http://friendfeed.com/scilib" title="Richard Akerman - FriendFeed">Richard Ackerman</a> then jumped into the conversation with an excellent point about misplacing focus on the user interface itself:</p>
<blockquote><p>I think to some extent it doesn't matter if we've ceded control or not - we've been having this discussion/argument at my office - the tech architects' side being that, if we want to add value at all, we have to build a discovery layer anyway - which we will expose in many different places, including browser extensions - but once you build it, the cost to also show it as a searchbox on your website is low.  In other words, it doesn't matter that "they won't come" - the website is free anyway since you need to build the underlying infrastructure if you ever want to have a hope of delivering enhanced services around content and metadata.  I also think "search in this box, and discover far more of the millions of dollars of content that we license for you than if you search in THAT box (e.g. google)" has got to be a compelling argument... surely?  Researchers, what do you think?</p></blockquote>
<p>In a FriendFeed comment, I thanked Richard for reminding me about how this concept is more than the user interface.  I "know" that -- it is the cornerstone of OhioLINK's discovery layer strategy -- but I haven't internalized it in my thinking very well.</p>
<p>And a follow-up from Dorothea:</p>
<blockquote><p>Yes, we have ceded control. We cannot insist that any given vendor support either an API or a data-provision protocol. Until we CAN, we have ceded control of discovery. Yet one more reason to dump the vendors in favor of OA. </radical></p></blockquote>
<p>I think Dorothea's argument is stronger for supporting open source software than open access content.  With an open source software solution, we can see the innards of the data and create the APIs we need to make extended use of that data.  Richard also followed up on Dorothea's comment:</p>
<blockquote><p>Dorothea, I keep hearing that story internally too - "oh won't it will be great when all the publishers are gone and the library can be the Temple of OA".  The whole point of OA is that anyone can have it, anywhere.  Considering we do a terrible job of helping our users find content that is licensed from a few huge publishers, we're going to do better when content is scattered all over the place?  Since it's OA, what's to stop a thousand startups from loading it all on their local harddrives?  Doesn't OA just take the problem from libraries (who pay millions of dollars to license content) doing a terrible job even though they have a perfect right to intermediate access, to libraries (who pay nothing for OA content) trying to out do *every other web search engine on the entire web, a battle which we were never in and lost long ago*?  OA doesn't make things better, it make them much, much worse for libraries.  (and as always, I mean pure special/research libraries, not public libraries or unis)</p></blockquote>
<p><a href="http://friendfeed.com/mrgunn" title="Mr. Gunn - FriendFeed">William Gunn</a> posted a comment:</p>
<blockquote><p>It's a compelling argument, but I haven't seen an implementation that lives up to the promise. Pubmed's "searching pubmed for X will give Y results" message that it shows people arriving there via google search is the closest thing I've seen that actually shows more value in searching using their interface than using Google. Most in-library search functions I've seen (admittedly not many) are woefully bad, but they are probably the third-party things Dorothea is railing about.</p></blockquote>
<p>I didn't post this comment to FriendFeed, but I agree with William's assessment.  In fact most of the innovation in end-user interfaces is coming out of the libraries themselves, public and academic, and not coming from the traditional vendor community.  I'm thinking of projects like <a href="http://vufind.org/" title="VuFind: Home">VuFind</a>, <a href="http://www.hathitrust.org/" title="Welcome to the Shared Digital Future | www.hathitrust.org">Haithi Trust</a>, the <a href="http://oleproject.org/" title="The OLE Project">OLE Project</a>, and others.  There are some notable exceptions to this -- the demonstration of <a href="http://www.proquest.com/products-services/The-Summon-Service.html" title="Summon<br />
            | Serials Solutions">Serials Solutions Summon</a>, for instance, at ALA Midwinter is one example.  But on the whole I think libraries are putting sweat equity into evolving or recreating their digital presence.</p>
<p>Dorothea followed up on Richard's comment:</p>
<blockquote><p>I guess it depends on where the money turns out to be. I'm actually not all that troubled about libraries getting pushed out of the discovery business; if it can be done better and cheaper elsewhere, fine and dandy. If games start being played, libraries can get back in and compete as long as everything's still OA. We libraries suck enough at this that I think it's something we should stop doing.</p></blockquote>
<p>I replied to Dorothea that I think we need to stick with the discovery end of the trade until the context sensitive linking -- e.g., get the user to the appropriate copy -- is better.  What I don't want to end up with is giving up on the discovery layer to the point where users aren't coming to content that we have paid for on their behalf.  Perhaps that will be the day when everything is open access, but can't hold my breath that long.</p>
<p>The last word at the moment goes to Dorothea:</p>
<blockquote><p>Understood and agreed, Peter. Though I have days where I wish we'd just tell 'em "if I can't get my patrons easily and quickly to your stuff, it is WORTHLESS, ergo I will no longer pay for it." That doesn't necessarily have to mean OA, of course.</p></blockquote>
<p>That is the conversation so far.  Do you have any thoughts?  Please add them here or on the original FriendFeed post.  I should note that the WordPress plug-in I was using to shuttle comments between <acronym title="Disruptive Library Technology Jester"><i>DLTJ</i></acronym> posts and FriendFeed isn't working at the moment, so I may need to edit this post with interesting comments that come from FriendFeed (and vice versa).</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://friendfeed/mndoci to http://friendfeed.com/mndoci on January 28th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://friendfeed.com/cavlec on February 11th, 2011.</p>
