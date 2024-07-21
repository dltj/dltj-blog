---
layout: wordpress-import
status: publish
published: true
title: 'Processing Raw Fedora Objects'
modified: 2006-05-03T16:08:43+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 50
wordpress_url: http://dltj.org/2006/05/processing-raw-fedora-objects/
date: '2006-05-03 12:08:43 -0400'
date_gmt: '2006-05-03 17:08:43 -0400'
categories:
- DRC
- Fedora
tags:
- mets
- Fedora Repository
comments:
- id: 54
  author: Michael
  author_email: leftwing@alumni.rutgers.edu
  author_url: http://purl.org/net/leftwing/blog
  date: '2006-05-03 12:41:45 -0400'
  date_gmt: '2006-05-03 17:41:45 -0400'
  content: "Thanks for the props, Peter.\r\n\r\nIn fact, Fedora does serialize the
    XML back to the FOXML file on disk for <i>every</i> change, including appropriate
    changes to the administrative metadata section for audit trails.  This was a requirement
    for us at Rutgers as one of our goals for the repository was digital preservation.\r\n\r\nA
    tiny caveat: this <i>used</i> to be the case, at least, under Fedora 1.2 when
    they used Fedora-METS.  I'm 99% confident that this is still the case under Fedora
    2.x w/ FOXML -- it seems to be a core feature of Fedora that the serialized XML
    objects are complete.  Sure, there's stuff in the db and the triplestore, but
    that's all extracted from the XML.  We'd been using Fedora since about 0.9 or
    so, way before much of its advanced functionality started appearing in official
    releases, so we had lots of experience going under the hood of Fedora (esp. for
    searching &amp; repository synchronization).\r\n\r\nThat's part of its beauty
    -- the stuff under the hood is relatively undaunting.  And it's not got the black-boxish
    feel that other information systems do.\r\n\r\nHopefully we'll start to see others
    blog about their Fedora experiences.  Maybe this would be a good topic (for Sandy
    or Thorny?) at the Fedora Users Conference -- building the Fedora community through
    the Wiki, the #fedora-users IRC channel, and through bloggers."
- id: 55
  author: Leslie
  author_email: johnston@virginia.edu
  author_url: ''
  date: '2006-05-03 13:18:22 -0400'
  date_gmt: '2006-05-03 18:18:22 -0400'
  content: Since we keep copies of the xml files for our externally referenced datastreams
    in the file system, we have built our discovery interface at UVA using XPAT outside
    of Fedora, with Cocoon as the middleware.  We have very rich metadata extracted
    from our objects programatically, much richer than what's in Fedora; we also provide
    full text searching of the TEI or EAD that way as well.  As an example, a user
    uses the web interface to search the XPAT index.  He finds an object that he wants
    to see.  When he clicks on it, a parameterized URL is passed through Cocoon that
    formats a call for Fedora to disseminate the object.
- id: 56
  author: Leslie
  author_email: johnston@virginia.edu
  author_url: ''
  date: '2006-05-03 13:20:58 -0400'
  date_gmt: '2006-05-03 18:20:58 -0400'
  content: I should clarify that we don't do this with the raw Fedora XML objects,
    but with the externally managed datastreams.  I think the principle is much the
    same and could work with the raw objects.
---
<p>Michael J. Giarlo <a href="http://lackoftalent.org/michael/blog/2006/05/02/the-jesters-case-for-fedora/" title="Not Found">wrote a very nice summary</a> of <a href="/article/general-purpose-repository/">my</a> <a href="/article/why-fedora-because-you-dont-need-fedora/">FEDORA</a> <a href="/article/fedora-disseminators/">trilogy</a> (only three parts so far -- I think there are more good things to say about FEDORA; and besides, I like <a href="http://www.douglasadams.com/creations/hhgg.html" title="DNA/The Hitchhiker&#039;s Guide to the Galaxy">Douglas Adams' concept of what a trilogy should be</a>), and added a piece that I hadn't considered:</p>
<blockquote>
<ol start="3">
<li>Having one&rsquo;s objects stored as XML on the filesystem also opens up opportunities to see how tools which act thereupon might be glued into the repository infrastructure.  One such example might be for an XML-aware search engine (such as amberfish, Lucene, or Zebra).  Since you&rsquo;ve got low-level access to these files, it would be fairly simple to tack on a search & indexing system that is independent of your choice of repository.</li>
</ol>
</blockquote>
<p>Wow.  Now that is a powerful concept.  Not only do we not need FEDORA in the future to read our digital objects, we don't need FEDORA <i><b>now</b></i> to read our digital objects.  This would take a little digging to see if it is true, but if Fedora really does serialize the XML back to the FOXML file on disk for every change made to it, then one really could use the FOXML files on disk as a surrogate for the FEDORA application itself.  After having conversations with Dan Davis about what it means to live in a Service-Oriented Architecture, I yearn for a time when FEDORA and other OhioLINK applications can send messages to each other.  But for now, simply having another application that looks at the file modification timestamps on files to see if they have changed and should be processed in some way is a very interesting idea.  It make sense, for instance, as a way to feed new/modified objects into an indexing application or a notification application.  Or to 'rsync' a backup hot-spare server with content from the live server.</p>
<p>You hit all of points exactly right in your summary, Michael, and thanks for triggering a new line of thinking about how to exploit FEDORA to its fullest potential.
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://staff.washington.edu/leftwing/wordpress/2006/05/02/the-jesters-case-for-fedora/ to http://lackoftalent.org/michael/blog/2006/05/02/the-jesters-case-for-fedora/.</p>
