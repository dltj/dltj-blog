---
layout: wordpress-import
status: published
published: true
title: 'Thursday Threads: Machine-Meaningful Web Content and Successful IPv6 Test'
modified: 2011-06-09T10:23:07+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 2946
wordpress_url: http://dltj.org/?p=2946
date: '2011-06-09 06:23:07 -0400'
date_gmt: '2011-06-09 10:23:07 -0400'
category: Thursday Threads
categories:
- Thursday Threads
tags:
- ipv6
- linked data
- schema.org
comments:
- id: 148787
  author: mb98115
  author_email: mmbb@sogetthis.com
  author_url: ''
  date: '2011-06-09 07:39:42 -0400'
  date_gmt: '2011-06-09 11:39:42 -0400'
  content: 'Two minor nits: you have a scheme.org typo, you schemer, and ipv6 happens
    at the transport layer and is thus not an issue for >98% of application developers.  OSI
    FTW!'
- id: 148803
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-06-09 08:38:58 -0400'
  date_gmt: '2011-06-09 12:38:58 -0400'
  content: Fixed the typo -- thanks for pointing it out.  And I agree that most application
    developers don't care, but those that keep track of IP addresses -- such as those
    who use IP addresses as a way to limit access to content -- will need to update
    their code in preparation for the point in time when the underlying host operating
    system is using IPv6.  For instance, many content publishers do not rely on usernames/passwords
    to access their services; as a convenience to the reader they instead look at
    the IP address of the client to see if it is coming from a known subscriber range.  That
    code will break when an IPv6 connection comes in.  Much like Y2K, it is easier
    to plan for the change in the size of the address field (and corresponding program
    logic) now rather than have to do it in a panic later.
- id: 148866
  author: Enrico F
  author_email: efrancese@gmail.com
  author_url: http://fraenrico.carcosa.it
  date: '2011-06-09 17:48:39 -0400'
  date_gmt: '2011-06-09 21:48:39 -0400'
  content: Semantic Web is not just about findability of (meta)data, but also about
    their reuse across websites and platforms. Schema.org seems to address only the
    first aspect, but not the second. Am I wrong?
- id: 148906
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-06-09 22:18:49 -0400'
  date_gmt: '2011-06-10 02:18:49 -0400'
  content: I don't think reuse is as much of an issue as long as one can live with
    the expressiveness of the vocabulary.  There has already been work done to create
    <a href="http://schema.rdfs.org/" rel="nofollow">equivalent RDF-based vocabularies</a>
    for the schema.org entities, which should ease translation.  The problem as I
    see it, though, is that schema.org is a take-it-or-leave-it kind of thing.  There
    is an <a href="http://schema.org/docs/extension.html" rel="nofollow">extension
    mechanism</a> but it really only takes you so far when you are describing specialized
    entities.  (Perhaps Google/Microsoft/Yahoo! are intentionally limiting or controlling
    the scope of what they are interested in?)
- id: 160050
  author: ALA_TechSource
  author_email: ''
  author_url: http://twitter.com/ala_techsource/status/78876773361795072
  date: '2011-06-09 17:31:02 -0400'
  date_gmt: '2011-06-09 21:31:02 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Via @DataG Thursday Threads: Machine-Meaningful
    Web Content and Successful IPv6 Test http://bit.ly/iI55Ie</span></span>'
- id: 160051
  author: Marcus P. Zillman
  author_email: ''
  author_url: http://twitter.com/zillman/status/78854577121792000
  date: '2011-06-09 16:02:50 -0400'
  date_gmt: '2011-06-09 20:02:50 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Thursday Threads: Machine-Meaningful Web Content
    and Successful IPv6 Test http://zite.to/j21J0n via @Ziteapp</span></span>'
- id: 160052
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/78775783857991680
  date: '2011-06-09 10:49:45 -0400'
  date_gmt: '2011-06-09 14:49:45 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Thursday Threads: Machine-Meaningful
    Web Content and Successful IPv6 Test http://bit.ly/kLeoAf</span></span>'
---

<p>Two threads this week: the first is an <a href="#p2946-schema-org">announcement from the major search engine on a way they agree to discover machine-processable information in web pages</a>.  The search engines want this so they can do a better job understanding the information web pages, but it stomps on the linked data work that has been a hot topic in libraries recently.  The second is a red-letter day in the history of the internet as <a href="#p2946-ipv6">major services tried out a new way for machines to connect</a>.  The test was successful, and its success means a big hurdle has been crossed as the internet grows up.<br />
<!--more--><br />
{{ thursday_threads_header() }}
<h2 id="p2946-schema-org">Introducing schema.org: Search engines come together for a richer web </h2>
<blockquote><p>Many sites are generated from structured data, which is often stored in databases. When this data is formatted into HTML, it becomes very difficult to recover the original structured data. Many applications, especially search engines, can benefit greatly from direct access to this structured data. On-page markup enables search engines to understand the information on web pages and provide richer search results in order to make it easier for users to find relevant information on the web. Markup can also enable new tools and applications that make use of the structure.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://schema.org/" title="schema.org homepage" rel="homepage">schema.org &ndash; Home</a></cite></div>
</blockquote>
<p>As the quote above suggests, much of the data on the web starts as structured information, but HTML by itself lacks the semantic hooks to easily bring meaning to that information.  Search engine robots and indexing algorithms have to try to infer the meaning of bits of information from surrounding context.  Sometimes they can get really good at it, and sometimes not.  So last week <a href="http://googleblog.blogspot.com/2011/06/introducing-schemaorg-search-engines.html" title="Introducing schema.org: Search engines come together for a richer web | Official Google Blog">Google</a>, <a href="http://www.bing.com/community/site_blogs/b/search/archive/2011/06/01/bing-google-and-yahoo-unite-to-build-the-web-of-objects.aspx" title="Bing Introducing Schema.org: Bing, Google and Yahoo Unite to Build the Web of Objects | Bing Community">Microsoft Bing</a>, and <a href="http://www.ysearchblog.com/2011/06/02/introducing-schema-org-a-collaboration-on-structured-data/" title="Introducing schema.org: A Collaboration on Structured Data">Yahoo!</a> announced a <a href="http://schema.org/" title="schema.org - Home">project</a> to promote machine-readable markup for structured data on web pages.  What does this mean? Take this example from this <a href="http://schema.org/Event" title="Event - schema.org">documentation page on how to describe an event</a>:</p>
```xml
<div itemscope itemtype="http://schema.org/Event">
  <a itemprop="url" href="nba-miami-philidelphia-game3.html">
  NBA Eastern Conference First Round Playoff Tickets:
  Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1)
  </a>
  <time itemprop="startDate" datetime="2011-04-21T20:00">
    Thu, 04/21/11
    8:00 p.m.
  </time>
  <div itemprop="location" itemscope itemtype="http://schema.org/Place">
    <a itemprop="url" href="wells-fargo-center.html">
    Wells Fargo Center
    </a>
    <div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
      <span itemprop="addressLocality">Philadelphia</span>,
      <span itemprop="addressRegion">PA</span>
    </div>
  </div>
  <div itemprop="offers" itemscope itemtype="http://schema.org/AggregateOffer">
    Priced from: <span itemprop="lowPrice">$35</span>
    <span itemprop="offerCount">1,938</span> tickets left
  </div>
</div>
```
<p>There are a number of things going on here.  Line #1 marks the beginning of the description of an event, and that event will have a URL for more information (line 2), a start time (line 6), a location (lines 10 through 19) with an address (lines 14 through 19), and an item for sale -- in this case, a ticket (lines 20 through 24).  With this information, the search engines can more easily understand content on web pages to put them on a map or compare prices.</p>
<p>This, of course, intersects with what libraries have been doing for a long time -- describing things to make them easier for library patrons to find.  The creators behind 'schema.org' have thought about this as well because they have ways of describing <a href="http://schema.org/CreativeWork" title="CreativeWork - schema.org">creative works of various types</a> and the <a href="http://schema.org/Person" title="Person - schema.org">people associated with them</a>.  If you have wondered what the Semantic Web and Linked Data was about, this is <em>sort of</em> an example of what people have been trying to do to bring "more intelligence" to the data encoded on our web pages.</p>
<p>The 'schema.org' announcement, of course, hasn't been without controversy.  In going down the path that they did, Google and Bing and Yahoo appear to have dismissed much of the last decade of work to bring the <a href="http://www.w3.org/DesignIssues/Semantic.html" title="Semantic Web roadmap">semantic web vision</a> to fruition.  (Primarily, using a standard called <a href="http://www.w3.org/TR/xhtml-rdfa-primer/" title="RDFa Primer">RDFa</a> to embed this information in HTML pages.)  <a href="http://weibel-lines.typepad.com/weibelines/2011/06/uncommon-cause.html" title="Uncommon Cause: Schema.org and the Semantic Web | Weibel Lines">Several</a> <a href="http://manu.sporny.org/2011/false-choice/" title="The False Choice of Schema.org | The Beautiful, Tormented Machine">people</a> have commented on the project, and an <a href="http://schema.rdfs.org/about.html" title="schema.rdfs.org - Home">effort was started to unify the 'schema.org' proposal with the semantic web work</a>.  It remains to be seen, though, how what the impacts of this work will be.</p>
<h2 id="p2946-ipv6">World IPv6 Day Happens With Few Problems</h2>
<p><a href="http://www.worldipv6day.org" class="alignright" title="Internet Society - World IPv6 Day"><img src="/assets/images/2011/06/IPv6-badge-blk-128-trans.png" height="128" width="128" title="WORLD IPV6 DAY is 8 June 2011 &ndash; The Future is Forever" alt="WORLD IPV6 DAY is 8 June 2011 &ndash; The Future is Forever"/></a></p>
<blockquote><p>The nation's largest telecom carriers, content providers, hardware suppliers and software vendors will be on the edge of their seats tonight for the start of <a href="http://www.networkworld.com/news/2011/060311-ipv6-day.html" title="Large-scale IPv6 trial set for June 8 | NetworkWorld">World IPv6 Day</a>, which is the most-anticipated 24 hours the tech industry has seen since fears of the Y2K bug dominated New Year's Eve in 1999.  More than 400 organizations are participating in World IPv6 Day, a large-scale experiment aimed at identifying problems associated with <a href="http://www.networkworld.com/newsletters/2010/042810-ipv6-tutorial.html" title="IPv6 tutorial | NetworkWorld">IPv6</a>, an upgrade to the Internet's main communications protocol known as IPv4.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://www.networkworld.com/news/2011/060711-ipv6-expect.html" title="World IPv6 Day: Tech industry's most-watched event since Y2K | NetworkWorld">World IPv6 Day: Tech industry's most-watched event since Y2K</a>, by Carolyn Duffy Marsan, Network World, 7-Jun-2011</cite></div>
</blockquote>
<blockquote><p>Internet administrators were 99.9999% sure that <a href="http://www.zdnet.com/blog/networking/what-is-world-ipv6-day-and-why-it-matters/1148" title="What is World IPv6 Day and why it matters | ZDNet">World IPv6 Day</a> would go by without any real problems. Of course, when you&rsquo;re dealing with something as big as the Internet, even six nines of up-time could mean hundreds of thousands of users with trouble. So far, though, all is well. ...</p>
<p>We now know that the IPv6 Internet can co-exist peacefully with the IPv4 Internet. That&rsquo;s a darn good thing since we can look forward to more than a decade of the two them working side by side as the older IPv4 Internet slowly fades away.</p>
<div style="text-align: right; width: 100%;"><cite>- <a href="http://www.zdnet.com/blog/networking/the-world-ipv6-day-report-card/1158" title="The World IPv6 Day report card | ZDNet">The World IPv6 Day report card</a></cite>, by Steven J. Vaughan-Nichols, ZDNet, 8-Jun-2011</div>
</blockquote>
<p>As <a href="/article/thursday-threads-2011w5/#p2525-ipv4-addresses">noted in a previous <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym> Thursday Thread</i></a>, the internet is <a href="/article/ipv4-ipv6-transition/" title="IPv4 Address Space Disappearing, Here Comes IPv6 | Disruptive Library Technology Jester">running out of addresses for devices on the network</a>.  A decade and a half ago the <a href="http://www.ietf.org/" title="Internet Engineering Task Force">Internet Engineering Task Force</a> realized this and created a next-generation standard called <a href="http://en.wikipedia.org/wiki/IPv6" title="IPv6 | Wikipedia">Internet Protocol version 6</a>, or IPv6, that would solve this problem by dramatically increasing the number of possible addresses (340,282,366,920,938,463,463,374,607,431,768,211,456 versus 4,294,967,296 with IPv4).  Unfortunately, for deep technical reasons, it is not easy to conversion from one to the other; they coexist peacefully but one needs a gateway to translate between the two.  And because IPv4 is embedded in lots of devices like printers and copiers and phones and set-top TV boxes and <a href="http://www.reviewsonline.com/articles/981056056.HTM" title="Reviews OnLine: Internet Washing Machine">washing machines</a> (any other strange internet-connected devices?), IPv4 is going to be with us for a while.</p>
<p>The test on June 8th was to have <a href="https://web.archive.org/web/20110615182443/http://www.worldipv6day.org/participants/index.html" title="Internet Society - World IPv6 Day List of Participants">major internet services and networks</a> such as Google/YouTube, Facebook, and Yahoo! put their servers on IPv4 and IPv6 at the same name (e.g. "www.google.com").  For the most part, the test proved successful.  So the march to IPv6-for-all is on.  Are you a software developer?  And if so have you considered what changes you'll need to make to your code (as in "IP address-based access restrictions")?</p>
