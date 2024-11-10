---
layout: wordpress-import
status: published
published: true
title: Does the Google/Bing/Yahoo Schema.org Markup Promote Invalid HTML?
modified: 2018-01-15T17:35:29-05:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 2920
wordpress_url: http://dltj.org/?p=2920
date: '2011-06-03 12:32:10 -0400'
date_gmt: '2011-06-03 16:32:10 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- html
- microformats
- schema.org
- microdata
- html5
comments:
- id: 146919
  author: Karen Coombs
  author_email: librarywebchic@gmail.com
  author_url: ''
  date: '2011-06-03 16:12:54 -0400'
  date_gmt: '2011-06-03 20:12:54 -0400'
  content: "Peter,\r\n\r\nDid you validate it against HTML5? From what I understand
    HTML5 isn't XML so I think that this might be perfectly valid HTML5.\r\n\r\nKaren"
- id: 146929
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-06-03 16:36:00 -0400'
  date_gmt: '2011-06-03 20:36:00 -0400'
  content: "I think the <code><!DOCTYPE html></code> line will trigger the HTML5 parser
    on W3's validation site.  If not, I get the same thing when I remove the DOCTYPE
    line and manually select the experimental HTML5 parser.\r\n\r\nI'm not completely
    familiar with the HTML5 specifications, but I thought there was a XML serialization
    for whatever was being proposed by W3C.  It seems like the schema.org work unnecessarily
    breaks an XML serialization."
- id: 146939
  author: Bruce D'Arcus
  author_email: bdarcus@gmail.com
  author_url: ''
  date: '2011-06-03 17:11:25 -0400'
  date_gmt: '2011-06-03 21:11:25 -0400'
  content: "This is something that drives me absolutely insane about the HTML 5 effort:
    they appear to go out of their way to step on existing, widely used, standards.\r\n\r\nSo
    they introduce an absolutely brain-dead notion of a boolean attribute, whose preferred
    syntax in the non-XML HTML 5 syntax cannot be represented in XML. \r\n\r\nIt would
    be easy enough to have a consistent syntax for both, but they don't.\r\n\r\nThey
    then encourage everyone else to be as casual as they are by posting examples like
    this.\r\n\r\nTo answer your question, I'd call that invalid. They have the namespace
    attribute on the root, and then they post a document which no XML parser will
    parse.\r\n\r\nI wish they'd fix boolean attributes more generally. Absent that,
    they should at least post examples that are the same in XML and non-XML syntaxes.\r\n\r\nEnd
    rant :-)"
- id: 146961
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-06-03 18:39:16 -0400'
  date_gmt: '2011-06-03 22:39:16 -0400'
  content: "To be fair, the example from the schema.org website is only the <code><div
    itemscope itemtype=\"http://schema.org/Event\"></code> block.  I had to add the
    framework, including the <code>xmlns</code> declaration in the <code><html></code>
    tag, to have something to run through the validator.\r\n\r\nYour mention of boolean
    attributes did prompt me to look at the <a href=\"http://dev.w3.org/html5/spec/Overview.html#boolean-attributes\"
    rel=\"nofollow\">HTML5 spec definition for boolean attributes</a>.  If that is
    to be believed, then this should be equivalent, well-formed XML: <blockquote><code><div
    itemscope=\"itemscope\" itemtype=\"http://schema.org/Event\"></code></blockquote>\r\n\r\nNow
    this begs the question as to why a boolean \"itemscope\" attribute is needed at
    all.  The <a href=\"http://schema.org/docs/documents.html\" title=\"schema.org
    - Documentation\" rel=\"nofollow\">documentation on schema.org</a> is really sparse,
    and it doesn't seem to be needed from a modeling perspective.  (Isn't the presence
    of an <code>itemtype</code> attribute good enough?)"
- id: 146968
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-06-03 18:56:36 -0400'
  date_gmt: '2011-06-03 22:56:36 -0400'
  content: |-
    Worthy of note now -- if <code>itemscope</code> is turned into <code>itemscope="itemscope"</code> in all three places it appears in the example, it will pass the w3c HTML5 validator.  I was poking around the schema.org discussion group and ran across mention of <a href="http://www.google.com/webmasters/tools/richsnippets" rel="nofollow">Google's rich snippet validator</a>, which seems to be parsing and displaying schema.org entities.  I saved a version of the example above as an online file and ran it through this validator; it <a href="http://www.google.com/webmasters/tools/richsnippets?url=http%3A%2F%2Fdltj.org%2Fwp-content%2Fuploads%2F2011%2F06%2Fschema-event-html5.html&amp;view=" rel="nofollow">checks out fine with the XHTML-style boolean attributes</a>.

    Also of note -- there is a <a href="http://groups.google.com/group/schemaorg-discussion/browse_thread/thread/c9ed20fe53f40210" rel="nofollow">discussion thread about HTML validity</a> in the same group, but mostly concerned about pre-HTML5 validity.
- id: 147169
  author: Kaleb Hornsby
  author_email: thekaleb@gmail.com
  author_url: http://kaleb.hornsby.ws
  date: '2011-06-04 07:31:17 -0400'
  date_gmt: '2011-06-04 11:31:17 -0400'
  content: HTML is **not** XHTML. `` is valid. `` is valid. This **is** a web standard
    and has been for a long time.
- id: 147171
  author: Kaleb Hornsby
  author_email: thekaleb@gmail.com
  author_url: http://kaleb.hornsby.ws
  date: '2011-06-04 07:34:53 -0400'
  date_gmt: '2011-06-04 11:34:53 -0400'
  content: "My element examples were stripped, so I'll try it again. These are both
    valid HTML and meet standards:\r\n\r\n<img src=\"face.gif\" alt=face>\r\n\r\n<input
    type=checkbox checked value=\"hi\" disabled>"
- id: 148100
  author: Chris Graham
  author_email: chris@ocportal.com
  author_url: http://ocportal.com/
  date: '2011-06-06 09:17:32 -0400'
  date_gmt: '2011-06-06 13:17:32 -0400'
  content: "Peter's right, it's perfectly possible to implement in XHTML5 (but not
    any currently-recommended W3C standard, i.e. XHTML 1.1 or HTML4).\r\n\r\nWe've
    released an implementation for ocPortal (http://ocportal.com/) and it's worked
    out very nicely, we're really pleased with the standard."
- id: 148920
  author: skierpage
  author_email: info@skierpage.com
  author_url: ''
  date: '2011-06-10 00:37:25 -0400'
  date_gmt: '2011-06-10 04:37:25 -0400'
  content: "That's not invalid HTML5, and the much better http://validator.nu/ passes
    it.  But as Tantek &Ccedil;elik points out,  http://schema.org/EventVenue example
    of openingHours uses a wildly invalid datetime attribute:\r\n\r\n <time itemprop=\"openingHours\"
    datetime=\"Tu,Th 16:00-20:00\">Tuesdays and Thursdays 4-8pm</time>\r\n\r\nThat
    datetime=\"Tu,Th 16:00-20:00\" is an utter fantasy from this Google-Microsoft
    cabal, it doesn't match even any proposed extension to HTMl5 attributes.\r\n\r\n(I'm
    guessing what markup will get through your site, where's the [Preview comment]
    button?)"
- id: 148990
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-06-10 12:13:39 -0400'
  date_gmt: '2011-06-10 16:13:39 -0400'
  content: Wow -- that datetime pattern is like nothing I've seen before (that would
    be machine-consumable).  That certainly is a problem.  (I fixed up the markup,
    and I'll have to look at getting a "comment preview" plugin for Wordpress.)
- id: 159994
  author: ALA_TechSource
  author_email: ''
  author_url: http://twitter.com/ala_techsource/status/77766880596725760
  date: '2011-06-06 16:00:43 -0400'
  date_gmt: '2011-06-06 20:00:43 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Does the Google/Bing/Yahoo Schema.org Markup Promote
    Invalid HTML? via @DataG http://bit.ly/knmyBu</span></span>
- id: 159996
  author: bdarcus
  author_email: ''
  author_url: http://twitter.com/bdarcus/status/76758994621960192
  date: '2011-06-03 21:15:45 -0400'
  date_gmt: '2011-06-04 01:15:45 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">#HTML5 boolean attributes harmful - http://t.co/ZueBHTs</span></span>
- id: 210208
  author: 'Re: W3C error due to Schema.org tags from Dan Brickley on 2012-01-16 (public-vocabs@w3.org
    from January 2012)'
  author_email: ''
  author_url: http://lists.w3.org/Archives/Public/public-vocabs/2012Jan/0033.html
  date: '2012-01-18 06:17:09 -0500'
  date_gmt: '2012-01-18 11:17:09 -0500'
  content: "<!--%kramer-ref-pre%-->[...] > > > This seems to be a well-known problem;
    see for example the discussion > at <http://dltj.org/article/schema-org-invalid/>.
    Note the follow-up > comments, esp. what Peter Murray says w.r.t. HTML5 boolean
    attributes [...]<!--%kramer-ref-post%-->"
- id: 317636
  author: krishna bisht
  author_email: krishna.bisth@mitsl.in
  author_url: http://zatse.in
  date: '2012-10-05 05:38:56 -0400'
  date_gmt: '2012-10-05 09:38:56 -0400'
  content: getting same error in w3c validator after validating itemscope" is not
    a member of a group specified for any attribute... any solution for this
- id: 383084
  author: 'Microformats: Google Rich Snippets'
  author_email: ''
  author_url: http://www.commentics.org/forum/showthread.php?tid=172&amp;page=2
  date: '2012-12-07 09:31:55 -0500'
  date_gmt: '2012-12-07 14:31:55 -0500'
  content: "<!--%kramer-ref-pre%-->[...] worked fine.  Note that I have changed itemscope
    to itemscope=&#039;itemscope&#039; to make it valid xHTML. http://dltj.org/article/schema-org-invalid/
    \     Attached File(s)  Thumbnail(s)  [...]<!--%kramer-ref-post%-->"
- id: 577207
  author: mike
  author_email: mikebeilagerung@gmx.de
  author_url: ''
  date: '2013-05-14 15:15:10 -0400'
  date_gmt: '2013-05-14 19:15:10 -0400'
  content: "Hi ... i have the self problem but my english ist not so good.....\r\n\r\nhere
    the wc3 output:\r\n\r\n Line 149, Column 51: \"itemscope\" is not a member of
    a group specified for any attribute\r\n&hellip;ss=\"shopbewertungBox boxgerman\"
    itemscope itemtype=\"http://schema.org/Product\">\r\n✉\r\n Line 149, Column 60:
    there is no attribute \"itemtype\"\r\n&hellip;ss=\"shopbewertungBox boxgerman\"
    itemscope itemtype=\"http://schema.org/Product\">\r\n✉\r\nYou have used the attribute
    named above in your document, but the document type you are using does not support
    that attribute for this element. This error is often caused by incorrect use of
    the \"Strict\" document type with a document that uses frames (e.g. you must use
    the \"Transitional\" document type to get the \"target\" attribute), or by using
    vendor proprietary extensions such as \"marginheight\" (this is usually fixed
    by using CSS to achieve the desired effect instead).\r\n\r\nThis error may also
    result if the element itself is not supported in the document type you are using,
    as an undefined element will have no supported attributes; in this case, see the
    element-undefined error message for further information.\r\n\r\nHow to fix: check
    the spelling and case of the element and attribute, (Remember XHTML is all lower-case)
    and/or check that they are both allowed in the chosen document type, and/or use
    CSS instead of this attribute. If you received this error when using the  element
    to incorporate flash media in a Web page, see the FAQ item on valid flash.\r\n\r\n\r\n\r\nmy
    source is:\r\n\r\n\r\n    \r\n{$BEWERTUNG_GESAMT_DURCHSCHNITT} /\r\n5.00\r\n\r\n\r\n\r\n\r\ni
    have understand that i must make: \r\n\r\n\r\nbut then come :\r\n&hellip;shopbewertungBox
    boxgerman\" itemscope=HERE ERROR\"itemscope\" itemtype=\"http://schema.org/&hellip;\r\n\r\nand
    here the wc3 error output:\r\nYou have used the attribute named above in your
    document, but the document type you are using does not support that attribute
    for this element. This error is often caused by incorrect use of the \"Strict\"
    document type with a document that uses frames (e.g. you must use the \"Transitional\"
    document type to get the \"target\" attribute), or by using vendor proprietary
    extensions such as \"marginheight\" (this is usually fixed by using CSS to achieve
    the desired effect instead).\r\n\r\nThis error may also result if the element
    itself is not supported in the document type you are using, as an undefined element
    will have no supported attributes; in this case, see the element-undefined error
    message for further information.\r\n\r\nHow to fix: check the spelling and case
    of the element and attribute, (Remember XHTML is all lower-case) and/or check
    that they are both allowed in the chosen document type, and/or use CSS instead
    of this attribute. If you received this error when using the  element to incorporate
    flash media in a Web page, see the FAQ item on valid flash.\r\n\r\nWhat is wrong?
    \r\nPlease help me THX"
- id: 577269
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2013-05-14 16:07:41 -0400'
  date_gmt: '2013-05-14 20:07:41 -0400'
  content: Mike -- can you post a URL that contains this markup?  That would be an
    easier way to look at it.
- id: 650766
  author: Tom
  author_email: poeabby@hotmail.com
  author_url: ''
  date: '2013-10-08 10:12:19 -0400'
  date_gmt: '2013-10-08 14:12:19 -0400'
  content: If I change it to itemscope="itemscope" and run it through the Validator,
    I get errors where they were changed. It's really odd.
- id: 678291
  author: Stars and aggregated rating are not shown when using schema.org markup and
    and Review in xhtml page
  author_email: ''
  author_url: http://www.drawbackz.com/stack/465514/stars-and-aggregated-rating-are-not-shown-when-using-schema-org-markup-and-and-review-in-xhtml-page.html
  date: '2015-03-13 11:36:06 -0400'
  date_gmt: '2015-03-13 15:36:06 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;] otherwise my template wouldn&#039;t be
    parsed. I found the solution here [&#8230;]<!--%kramer-ref-post%-->"
---
\[Update on 10-Jun-2011: The answer to the question of the title is "not really" -- see the update at the bottom of this post and the comments for more information.\]

Yesterday [Google][0], [Microsoft Bing][1], and [Yahoo!][2] announced a [project][3] to promote machine-readable markup for structured data on web pages.  

> Many sites are generated from structured data, which is often stored in databases. When this data is formatted into HTML, it becomes very difficult to recover the original structured data. Many applications, especially search engines, can benefit greatly from direct access to this structured data. On-page markup enables search engines to understand the information on web pages and provide richer search results in order to make it easier for users to find relevant information on the web. Markup can also enable new tools and applications that make use of the structure.
> 
> _- [schema.org - Home][4]_
> 

The problem is, I think, that the markup they describe on there site generates invalid HTML. Did they really do this?

Take this example from the [Event][5] description page:

```xml
< !DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Test</title>
</head>
<body>
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
</body>
</html>
```

The problem is in the first &lt;div&gt; line and the attribute 'itemscope' that has no value associated with it. If you copy-and-paste that markup into the [W3 validator][0] (using the "Validate by Direct Input" option and manually removing the space between the less-than sign and the exclamation point in the first line), it comes back with:

> _Line 7, Column 16_: **required character (found i) (expected =)**

A bare attribute may be valid in some forms of HTML, but it certainly isn't valid XML, and I think that will cause all sorts of problems down the line. Does anyone else see this as an issue?

## Update

I heard back from one of the keepers of W3C's validator[6], and the `xmlns="http://www.w3.org/1999/xhtml"` attribute of the `html` tag was triggering the XML version of the validator. The bare `itemscope` attribute is valid HTML but invalid XML (important for the XML serialization of HTML), but can be fixed by making it `itemscope="itemscope"`. See the comments for more information.

[0]: http://googleblog.blogspot.com/2011/06/introducing-schemaorg-search-engines.html "Official Google Blog: Introducing schema.org: Search engines come together for a richer web"
[1]: http://www.bing.com/community/site_blogs/b/search/archive/2011/06/01/bing-google-and-yahoo-unite-to-build-the-web-of-objects.aspx "Bing Introducing Schema.org: Bing, Google and Yahoo Unite to Build the Web of Objects - Search Blog - Site Blogs - Bing Community"
[2]: http://www.ysearchblog.com/2011/06/02/introducing-schema-org-a-collaboration-on-structured-data/ "Introducing schema.org: A Collaboration on Structured Data"
[3]: http://schema.org/ "schema.org - Home"
[4]: http://schema.org/ "schema.org homepage"
[5]: http://schema.org/Event "Event - schema.org"
[6]: http://validator.w3.org/#validate_by_input
