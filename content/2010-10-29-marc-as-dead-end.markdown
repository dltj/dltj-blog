---
layout: wordpress-import
status: published
published: true
title: 'MARC isn''t Dead, but it is a Dead End'
modified: 2010-10-29T16:29:02+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1823
wordpress_url: http://dltj.org/?p=1823
date: '2010-10-29 12:29:02 -0400'
date_gmt: '2010-10-29 16:29:02 -0400'
category: L/IS Profession
categories:
- L/IS Profession
tags:
- metadata
- MARC
- American Library Association
- Functional Requirements for Bibliographic Records
- Resource Description and Access
- semantic web
- Karen Coyle
- linked data
- AACR
comments:
- id: 96532
  author: Diane Hillmann
  author_email: metadata.maven@gmail.com
  author_url: http://managemetadata.com
  date: '2010-10-29 16:10:58 -0400'
  date_gmt: '2010-10-29 20:10:58 -0400'
  content: Peter, we've started to talk about MARC as a 'fairly lossy exchange format',
    with the notion that yeah, it'll be around for a lot more years, but no longer
    at the center of our universe.
- id: 96537
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-10-29 16:34:52 -0400'
  date_gmt: '2010-10-29 20:34:52 -0400'
  content: Ah!  I think that is a good way to think of MARC now -- something that
    you'd want to transform out of, but not something you'd want to go back to because
    you couldn't get the same content fidelity.
- id: 96827
  author: Ron Murray
  author_email: rmur@loc.gov
  author_url: ''
  date: '2010-10-31 10:04:35 -0400'
  date_gmt: '2010-10-31 14:04:35 -0400'
  content: "Peter: MARC was very much a child of it's time &ndash; an effort to develop
    a \"practical\" data format for bibliographic information which had resided largely
    on catalog cards. The format was modeled and defined very quickly. As we critique
    MARC's deficits now, we should make sure that we are not doing so from the point
    of view of another \"practical\" resource description approach that will require
    replacement in time as well.\r\n\r\nFRBR &ndash; as a resource description theory
    &ndash; possesses great reach and precision (e.g., this exemplar which connects
    an 8th C. Chinese poem to a 21st C. Sign Language performance of it on a web page
    - https://files.me.com/kandroma1/6r9uhv). This does not mean that \"practical\"
    implementations of FRBR will inevitably realize its full capabilities.\r\n\r\nJust
    as we (can!) critique commercial relational databases from the POV of the Relational
    Model to see how well they implemented useful &amp; powerful ideas in the model,
    we can do the same for FRBR implementations with respect to a well-articulated
    FRBR model."
- id: 97056
  author: George Duimovich
  author_email: parser@rogers.com
  author_url: http://www.parser.ca/z678
  date: '2010-11-01 16:43:08 -0400'
  date_gmt: '2010-11-01 20:43:08 -0400'
  content: "I agree, only I'm surprised and dismayed by the apparent lack of urgency
    with the situation.  There are some real challenges to be sure, but still too
    many in our community don't see anything wrong with duplicating data (e.g. 034
    vs. 255), or in continuing on with the 'rule of three' with regards to, say, authors
    (yes, let's make it even harder for people to find things!). I don't bash tech
    services but we need a greater sense of urgency from all towards having better
    machine-readable data, essential to \"playing ball\" with any modern web infrastructure.
    \ \r\n\r\nIMO, some of the work with institutional repositories offers some glimpse
    into a future out of the MARC/AACR2 prison, one where multiple bibliographic schemas
    can coexist together (e.g. see the Fedora Commons content model). The IR space
    also teaches us that we're no longer the only game in town with regards to bibliographic
    standards. Yep, and some communities won't ever want to come back once they've
    found their own special standard to meet their needs. Who needs MARC when you
    can have FGDC or whatever the flavor is for this or that particular community.
    \r\n\r\nAlso critical to this discussion is the idea of **getting help for moving
    forward.** And recognizing that to change we need to better situate ourselves
    to get the help we need to actually move forward!! And IMHO that means taking
    some incremental but critical steps *ASAP* towards much more developer friendly
    platforms (like open source) and standards (like MARCXML, MODS, etc.).  But even
    those steps need more re-thinking too (e.g. see http://tinyurl.com/2ugmobs)."
- id: 97200
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-11-02 09:37:50 -0400'
  date_gmt: '2010-11-02 13:37:50 -0400'
  content: "Ron: What we face now is somewhat of a unique situation, and I say this
    with some hesitation since the future cannot be predicted.  The monumental task
    before us is to change from a \"machine readable\" format to a \"machine actionable\"
    format.  MARC is machine-readable in the sense that its original mission was to
    automate the process of reproducing cards for a card catalog.  What is needed
    is a machine-actionable format; the leading thought on this appears to be coming
    from the linked data community.\r\n\r\nI don't doubt that the <em>next</em> format
    won't be the <em>last</em> format.  That said, I don't think the next <em>transition</em>
    will be as painful as this one from machine-readable to machine-actionable.  What
    we have now is not only large change of systems and workflow, but also a large
    conceptual change about how bibliographic data is viewed inside the community
    (and potentially how it can be used outside the community)."
- id: 97206
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-11-02 10:06:53 -0400'
  date_gmt: '2010-11-02 14:06:53 -0400'
  content: "George: I'm not surprised as much.  There is a whole lot of momentum behind
    the <i>status quo</i>:  processes, training, documentation, software, contracts,
    service agreements, etc.  That much weight behind a standard makes it hard to
    turn quickly.  But, much like one needs to nudge an asteroid heading on a doomsday
    collision course with Earth by altering its course while it is far off in the
    distance, there are efforts afoot to change this.  (How about that for election
    season hyperbole on how we are all going to die if we don't change <em>right now!</em>)
    \ The three webinars in the \"Using RDA\" series are an example of how the ground
    is shifting.  I also hope highlighting MARC as \"dead end\" rather than simply
    wishing it dead could be considered part of that effort.  (This has certainly
    been the most tweeted and re-tweeted post I've written.)\r\n\r\nI take <a href=\"http://shelterit.blogspot.com/2008/09/marcxml-beast-of-burden.html\"
    rel=\"nofollow\">Alexander's critique of MARCXML</a> (the link you included at
    the end of your comment) with a grain of salt.  MARCXML certainly loses points
    for self-documenting readability, but as a commenter pointed out the roots of
    MARCXML lie in its round-trip nature with binary MARC.  Where I disagree with
    Alexander is that: <pre lang=\"xml\"><datafield tag=\"245\" ind1=\"1\" ind2=\"0\">\r\n
    \ <subfield code=\"a\">Arithmetic /</subfield>\r\n</datafield></pre> is the same
    as: <pre lang=\"xml\"><title>Arithmetic</title></pre> That is the equivalent of
    saying the definition of <a href=\"http://dublincore.org/documents/dces/#title\"
    rel=\"nofollow\">Dublin Core element Title</a> is the same as the <a href=\"http://www.loc.gov/marc/bibliographic/bd245.html\"
    rel=\"nofollow\">MARC 245 tag</a>.  The definition of the former is simply \"A
    name given to the resource.\"  It is possible to say quite a bit more with the
    latter -- titles, subtitles, non-filing characters, dates, etc.  One can quibble
    whether this information really needs to be captured, but it cannot be disputed
    that the MARC 245 tag is more expressive.\r\n\r\nThat the institutional repository
    space takes us out of \"the MARC/AACR2 prison\" is a useful thing to think about.
    \ As you point out, there is software there that can be used to describe resources
    in the most expressive manner necessary for the target community while still having
    ways to pull information back together for cross-community searching.  I'm a <a
    href=\"http://dltj.org/tag/fedora-repository/\" rel=\"nofollow\">big fan of Fedora</a>
    and although I've been on the edges of that community for a while I did give some
    thought half a decade ago on how <a href=\"http://dltj.org/article/description-datastream/\"
    rel=\"nofollow\">desciptions datastreams can best be used</a> in Fedora objects.<p
    style=\"padding:0;margin:0;font-style:italic;\">The text was modified to update
    a link from http://dltj.org/tag/fedora-dr/ to http://dltj.org/tag/fedora/ on January
    19th, 2011.</p>"
- id: 97216
  author: Ron Murray
  author_email: rmur@loc.gov
  author_url: ''
  date: '2010-11-02 10:50:24 -0400'
  date_gmt: '2010-11-02 14:50:24 -0400'
  content: "I agree that *some* of the leading thought comes from the linked data
    community, in the course of addressing data representation issues familiar to
    themselves. This does not mean that the current range of linked data solutions
    satisfies all of *our* needs. This is where attention to FRBR data modeling becomes
    important &ndash; so that we can express our needs in a common language.\r\n\r\nFor
    example, the concept and implementation of a Named Graph (implemented as \"packaged\"
    RDF statements) is perfectly adequate for representing data derived from a single
    point of view on a resource. Except that they did not finish their homework assignment:
    graphs can contain subgraphs &ndash; and so should Named Graphs.\r\n\r\nThis current
    limitation to Named Graph definition impacts a significant data modeling finding
    in our community: FRBR resource descriptions document multiple, complementary,
    points of view on target resources. This characteristic is readily modeled as
    a resource description subgraph for each POV. In the absence of the ability to
    define subgraphs, collapsing data that represents complementary descriptions into
    a single-level graph becomes a lossy process.\r\n\r\nEven though the scientific
    community is well aware of the complementarity of some descriptions of phenomena
    (Neils Bohr, after all...), parties participating in the linked data initiative
    have not (as far as I can tell) engaged that issue. More problematic than myriad
    recognitions and idiosyncratic solutions to the complementarity of description
    issue would be no attention to it at all.\r\n\r\nThe best strategy would be to
    finish the homework assignment and provide a uniform solution for this particular
    issue.\r\n\r\nOf course it's very early in the linked data scheme of things, and
    everyone (me too!) is aglow with the simple *availability* of it all. This also
    means that there is time to examine &ndash; and grow &ndash; the concept of linked
    data to include more sophisticated perspectives on that data."
- id: 98536
  author: Susan Berdinka
  author_email: susgeek@yahoo.com
  author_url: http://susanrb.wordpress.com/
  date: '2010-11-08 19:02:34 -0500'
  date_gmt: '2010-11-09 00:02:34 -0500'
  content: "I addressed this issue in my article \"Some thoughts about FRBR&mdash;It
    is a Beautiful Thing\" (http://susanrb.wordpress.com/2010/10/30/some-thoughts-about-frbr%e2%80%94it-is-a-beautiful-thing/).
    \r\n\r\nThe Marc record itself is an entity&mdash;a specific bibliographic edition.
    Within that entity are other entities. FRBR adds the aspects of work, expression,
    and manifestation. Mathematically speaking, an entity can contain other entities.
    These entitles should be stored outside of the bibliographic entity each in their
    own table, and only REFERENCED from the Marc bibliographic record.\r\n\r\nI don't
    think marc is a dead end - I think it simply needs mathematical normalization."
- id: 98711
  author: Ron Murray
  author_email: rmur@loc.gov
  author_url: ''
  date: '2010-11-09 10:18:05 -0500'
  date_gmt: '2010-11-09 15:18:05 -0500'
  content: "The critical issue from my perspective is that FRBR specifies networks
    of resource descriptions.**\r\n\r\nThe MARC record &ndash; a child of its times,
    IT-wise &ndash; does not readily support the specification of network structures
    (a.) within a single MARC record, or; (b.) across multiple MARC records. For example
    - and even though it is conceivable - I have not yet seen \"zoned\" MARC records.\r\n\r\nA
    zone within a MARC record could host its own unique IDs, which would serve as
    link origins/destinations for whatever purpose. Tags placed within a zone would
    subsequently be reference-able from elsewhere in the same record or from other
    records. One hopes there would be a logical reason for putting tags in the same
    zone. Of course, zoning a MARC record like this would indicate that information
    representing different types/levels of bibliographic description &ndash; FRBR's
    W|E|M|I &ndash; are jammed together into a single storage unit &ndash; and perhaps
    should no longer be.\r\n\r\nNote that networks &ndash; being graph structures
    capable of representation as sets &ndash; could undergo a normalization process.
    Recall though (sorry, Dr. Codd!), that normalization can be taken too far.\r\n\r\n**
    See: http://www.slideshare.net/RonMurray/the-graph-theoretical-library (Slides#
    80-102). If you like the Gardens of Versailles and graph theory, start at the
    beginning."
- id: 99092
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-11-09 13:41:48 -0500'
  date_gmt: '2010-11-09 18:41:48 -0500'
  content: "Susan -- thank you for responding to my tweet and linking to your post
    in a comment.  I would agree that normalization is one issue with MARC and its
    current usage today.  If authorities in bibliographic records were defined as
    identifiers (say, a URI) to an authority record, we would start to eliminate the
    issues of findability, and you talk about in your blog.  As Ron Murray points
    out in his comment, when normalizing what we use as bibliographic records now,
    it isn't long before we get into graphs of entities linked by meaningful predicates.
    \ Unfortunately, I haven't seen evidence that MARC -- as a communications format
    -- can effectively transmit graphs of entities.\r\n\r\nBeyond that issue, though,
    is that MARC is used by no one but libraries, and as such will always be an inwardly-facing
    format.  If we only want library systems to talk with other library systems, that
    would be okay.  I don't think such an inwardly-facing focus is good for the health
    of our profession.  The rest of the information world won't come to us; we will
    need to meet it more than half-way by using more commonly accepted data formats."
- id: 160741
  author: Sergi Montes
  author_email: ''
  author_url: http://twitter.com/sergi_montes/status/1604633285885952
  date: '2010-11-08 11:59:09 -0500'
  date_gmt: '2010-11-08 16:59:09 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT @ALA_TechSource: MARC isn&rsquo;t Dead, but
    it is a Dead End @DataG post #lldata http://bit.ly/a0CWtK</span></span>'
- id: 160742
  author: heather pena
  author_email: ''
  author_url: http://twitter.com/hpena310/status/1079641502650368
  date: '2010-11-07 01:13:01 -0500'
  date_gmt: '2010-11-07 05:13:01 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT @ALA_TechSource: MARC isn&rsquo;t Dead, but
    it is a Dead End @DataG post #lldata http://bit.ly/a0CWtK</span></span>'
- id: 160743
  author: ALA_TechSource
  author_email: ''
  author_url: http://twitter.com/ala_techsource/status/1031104605724672
  date: '2010-11-06 22:00:09 -0400'
  date_gmt: '2010-11-07 02:00:09 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">MARC isn&rsquo;t Dead, but it is a Dead End @DataG
    post #lldata http://bit.ly/a0CWtK</span></span>'
- id: 160744
  author: Celine Carty
  author_email: ''
  author_url: http://twitter.com/cjclib/status/29455063264
  date: '2010-11-02 09:42:12 -0400'
  date_gmt: '2010-11-02 13:42:12 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Wish I had attended these webinars -good read
    on MARC "not dead, but a dead end" from @DataG http://dltj.org/article/marc-as-dead-end/</span></span>
- id: 160745
  author: Ana C. Griebler
  author_email: ''
  author_url: http://twitter.com/agrieble/status/29414764858
  date: '2010-11-01 23:03:33 -0400'
  date_gmt: '2010-11-02 03:03:33 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT @ALA_TechSource: RT: MARC isn&rsquo;t Dead,
    but it is a Dead End @DataG post #lldata http://bit.ly/a0CWtK</span></span>'
- id: 160748
  author: ALA_TechSource
  author_email: ''
  author_url: http://twitter.com/ala_techsource/status/29397998875
  date: '2010-11-01 19:05:05 -0400'
  date_gmt: '2010-11-01 23:05:05 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">RT: MARC isn&rsquo;t Dead, but it is a Dead End
    @DataG post #lldata http://bit.ly/a0CWtK</span></span>'
- id: 160749
  author: Suzuki Takao
  author_email: ''
  author_url: http://twitter.com/suzuki_takao/status/29261288744
  date: '2010-10-31 09:05:23 -0400'
  date_gmt: '2010-10-31 13:05:23 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">MARC isn&rsquo;t Dead, but it is a Dead End (Disruptive
    Library Technology Jester) http://bit.ly/9erW9f</span></span>
- id: 160750
  author: nathalie  vielleuse
  author_email: ''
  author_url: http://twitter.com/vielleuse/status/29208189036
  date: '2010-10-30 18:41:26 -0400'
  date_gmt: '2010-10-30 22:41:26 -0400'
  content: "<span class=\"topsy_trackback_comment\"><span class=\"topsy_twitter_username\"><span
    class=\"topsy_trackback_content\">marc is dead ??? \nhttp://dltj.org/article/marc-as-dead-end/</span></span>"
- id: 230260
  author: What ... in scope &mdash; Council on Library and Information Resources
  author_email: ''
  author_url: http://www.clir.org/pubs/reports/pub152/linked-data-survey/part02_a_environ.html
  date: '2012-03-09 18:52:52 -0500'
  date_gmt: '2012-03-09 23:52:52 -0500'
  content: "<!--%kramer-ref-pre%-->[...] Peter Murray adds this note about constraints
    embedded in the mental model that evolved alongside library metadata practice
    [...]<!--%kramer-ref-post%-->"
---
<p>This week I sat in on the first of the three "<a href="http://www.alastore.ala.org/detail.aspx?ID=3125" title="Using RDA: Moving into the Metadata Future (A Three-part ALA TechSource Workshop)">Using RDA: Moving into the Metadata Future</a>" webinars being hosted by <acronym title="American Library Association">ALA</acronym>.  This one was hosted by <a href="http://kcoyle.net/" title="Karen Coyle's home page" rel="homepage">Karen Coyle</a> with the title <a href="http://www.alatechsource.org/blog/2010/10/continuing-the-conversation-new-models-of-metadata.html" title="Continuing the Conversation: New Models of Metadata | ALA TechSource">New Models of Metadata</a> where she talked about library-specific efforts such as<acronym title="Resource Description and Access"><a href="http://www.rdatoolkit.org/" title="RDA Toolkit">RDA</a></acronym> and <acronym title="Functional Requirement for Bibliographic Records"><a href="http://www.ifla.org/en/publications/functional-requirements-for-bibliographic-records" title="Functional Requirements for Bibliographic Records | IFLA">FRBR</a></acronym> as well as the <a href="http://linkeddata.org/" title="Linked Data - Connect Distributed Data across the Web">linked data</a> effort in the wider world of information.  There was a great deal of concern expressed in the chat window by participants about the future of cataloging, of cataloguers, and of <acronym title="MAchine-Readable Cataloging"><a href="http://www.loc.gov/marc/" title="MARC STANDARDS (Network Development and MARC Standards Office, Library of Congress)">MARC</a></acronym>.  The latter brought up memories of <a href="http://roytennant.com/professional.html" title="Roy Tennant: Professional Life">Roy Tennant</a>'s "<a href="http://www.libraryjournal.com/article/CA250046.html" title="MARC Must Die | Library Journal">MARC Must Die</a>" declaration.  My take away, though, isn't that MARC is dead as much as MARC is a dead end.<br />
<!--more--><br />
{{ image(
    div_float="right",
    width="180",
    caption="Cover art from \'Library of the Dead\' audio book",
    alt="&#039;Library of the Dead&#039; cover art",
    localsrc="2010/10/Library-of-the-Dead-cover-art-180x300.jpg",
    ahref="http://www.wfhowes.co.uk/catalogue/titles.php?&amp;t=4401") }} </p>
<h2>MARC, not dead yet?</h2>
<p>We know that MARC isn't dead; the communications format, along with its <acronym title="Anglo-American Cataloguing Rules, Second Edition"><a href="http://www.aacr2.org/" title="AACR2">AACR2</a></acronym> companion rules for describing bibliographic resources, are deeply and daily ingrained in our systems and processes.  For the same reasons, I think it is fair to say that MARC isn't dying.  (The fate of AACR2 with respect to RDA may be a little closer to the edge.)  What I propose, though, is that MARC is a dead end.  Karen makes a comment -- <a href="http://www.alatechsource.org/blog/2010/10/continuing-the-conversation-new-models-of-metadata.html#comment-2803" title="Continuing the Conversation: New Models of Metadata | ALA TechSource">On the brokenness of MARC</a> -- that starts to enumerate some of the basic issues with the MARC format.  (Karen's <a href="http://www.kcoyle.net/marcdead.html" title="Is MARC Dead? by Karen Coyle">writings from 10 years ago</a> lists even more details.)  Also, as Karen pointed out in her presentation (and many others have done before her), MARC is a format that is only used in the library community.  As a communications format, it is cumbersome -- requiring those outside the library community to use custom code toolkits to read and write the format.  That is a pretty high barrier for the wider world to want to use library bibliographic data encoded in MARC.</p>
<p>What trips up our community even more, I think, is that we have a tendency to equate this communications format with mental model of how we describe things from a bibliographic point of view.  We think of discrete records that describe these things rather than a network (or, more accurately, a <a href="http://en.wikipedia.org/wiki/Graph_theory" title="Graph theory - Wikipedia">graph</a>) of interrelated nodes.  This forces us to focus on the textual content of fields and not on the relationships between things.  And in doing so, we are not making the best use of our limited efforts to describe the things in our curatorial care.</p>
<p>MARC may not be dead, but it is a dead end.</p>
