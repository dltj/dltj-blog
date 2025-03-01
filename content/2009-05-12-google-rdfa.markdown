---
layout: wordpress-import
status: published
published: true
title: 'Google Search Engine Adds Support for RDFa, Or Do They?'
modified: 2009-05-13T02:38:27+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 934
wordpress_url: http://dltj.org/?p=934
date: '2009-05-12 22:38:27 -0400'
date_gmt: '2009-05-13 02:38:27 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Google
- microformats
- RDFa
- semantic web
comments:
- id: 35913
  author: Google поддерживает семантическую разметку (RDFa)!!! | SHCHERBAK.NET
  author_email: ''
  author_url: http://shcherbak.net/2009/05/google-podderzhivaet-semanticheskuyu-razmetku-rdfa/
  date: '2009-05-15 19:09:21 -0400'
  date_gmt: '2009-05-15 23:09:21 -0400'
  content: "<!--%kramer-ref-pre%-->[...] http://www.google.com/support/webmasters/bin/answer.py?hl=en&amp;answer=146898
    http://dltj.org/article/google-rdfa/ Как я написал в одном [...]<!--%kramer-ref-post%-->"
- id: 61142
  author: "&raquo; Google Recommends Microformats and RDFa MaisonBisson.com"
  author_email: ''
  author_url: http://maisonbisson.com/blog/post/13988/google-recommends-microformats-and-rdfa/
  date: '2010-03-25 16:39:59 -0400'
  date_gmt: '2010-03-25 20:39:59 -0400'
  content: "<!--%kramer-ref-pre%-->[...] that they are going beyond their made-up
    vocabulary rooted at http://rdf.data-vocabulary.org/. See this blog post for more
    info.  [...]<!--%kramer-ref-post%-->"
- id: 159721
  author: Peter Murray
  author_email: ''
  author_url: ''
  date: '2009-05-13 02:38:30 -0400'
  date_gmt: '2009-05-13 06:38:30 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">New blog post: Google Search Engine Adds Support
    for RDFa, Or Do They? http://dltj.org/article/google-rdfa/</span></span>'
- id: 163721
  author: SemanticBot
  author_email: ''
  author_url: http://twitter.com/semanticbot/status/12971050201
  date: '2010-04-27 23:11:04 -0400'
  date_gmt: '2010-04-28 03:11:04 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">#SemNews : Google Search Engine Adds Support for
    RDFa, Or Do They? http://bit.ly/cGcCkk</span></span>'
- id: 163722
  author: Barbara Gordon
  author_email: ''
  author_url: http://twitter.com/barbaragordon/status/1804380281
  date: '2009-05-15 08:59:31 -0400'
  date_gmt: '2009-05-15 12:59:31 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">@jimmy1712 re: hot topics in semantic web, here''s
    a new twist: http://dltj.org/article/google-rdfa/ - RDF and reusing existing vocab</span></span>'
- id: 163724
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/1781444156
  date: '2009-05-13 04:40:43 -0400'
  date_gmt: '2009-05-13 08:40:43 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Google Search Engine Adds Support
    for RDFa, Or Do They? http://snipurl.com/hx3ue</span></span>'
- id: 678758
  author: Google - BC$ MobileTV Wiki
  author_email: ''
  author_url: http://wiki.bcmoney-mobiletv.com/index.php?title=Google
  date: '2015-04-04 14:28:26 -0400'
  date_gmt: '2015-04-04 18:28:26 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;] &uarr; Google Search Engine Adds Support
    for RDFa, Or Do They?: http://dltj.org/article/google-rdfa/ [&#8230;]<!--%kramer-ref-post%-->"
---
<p>Via a <a href="http://radar.oreilly.com/2009/05/google-announces-support-for-m.html" title="Google Announces Support for Microformats and RDFa - O'Reilly Radar">post</a> and an <a href="http://radar.oreilly.com/2009/05/google-adds-microformat-parsin.html" title="Google Engineering Explains Microformat Support in Searches - O'Reilly Radar">interview</a> on the O'Reilly Radar blog, Google <a href="http://googleblog.blogspot.com/2009/05/more-search-options-and-other-updates.html" title="Official Google Blog: More Search Options and other updates from our Searchology event">announced</a> limited support for <a href="http://www.google.com/support/webmasters/bin/topic.py?topic=21997" title="Structured data (rich snippets) - Webmasters/Site owners Help">parsing RDFa statements and microformat properties</a> in web page HTML coding and using those statements to enhance the relevance of search results as so-called "rich snippets".  In looking at the example review markup outlined in the O'Reilly post, though, I was struck by some unusual and unexpected markup.  Specifically, that the namespace was this <code>http://rdf.data-vocabulary.org/</code> thing that I had never seen before, and the "rating" property didn't have any corresponding range that would make that numeric value useful in a computational sense.<br />
<!--more--></p>
<blockquote style="font-family: monospace;"><div <b>xmlns:v="http://rdf.data-vocabulary.org" typeof="v:review"</b>></p>
<div>
    79 of 98 people found the following review helpful:
  </div>
<p></p>
<div>
    <span><b><span property="v:rating">5.0</span></b> out of 5 stars</span><br />
    <span><b>American Biographer: Jon Meacham</b>/span>
  </div>
<p></p>
<div><a href="http://www.amazon.com/gp/pdp/profile/A2G8PQ9HNUY6NA/"><br />
       <span property="v:reviewer"<br />
                 about="http://www.amazon.com/gp/pdp/profile/A2G8PQ9HNUY6NA/">Marian the Librarian</span></a> (NY, NY)  - <br />
       <span property="v:dtreviewed">1st April 2009</span>
  </div>
<p></p>
<div>
    <b>This review is from: <br />
      <a property="v:itemreviewed" <br />
           about="http://www.amazon.com/American-Lion-Andrew-Jackson-White/dp/1400063256/"<br />
           href="http://www.amazon.com/American-Lion-Andrew-Jackson-White/dp/1400063256/"><br />
      American Lion: Andrew Jackson in the White House (Hardcover)</a></b></p></div>
<p></p>
<div class="review" property="v:description">
    American Lion is a wonderfully crafted biography about an incredibly interesting <br />
    and oft-overlooked American who helped shaped this country...
  </div>
<p>
</div>
</blockquote>
<p>I didn't think much of it, but this evening I came across a <a href="http://iandavis.com/blog/2009/05/googles-rdfa-a-damp-squib" title="Internet Alchemy &amp;raquo; Google&amp;#8217;s RDFa a Damp Squib">post by Ian Davis</a> that confirmed my odd feelings:<br />
<blockquote>However, a closer look reveals that Google have basically missed the point of RDFa. The RDFa support is limited to the properties and classes defined on a hastily thrown together site called <a href="http://data-vocabulary.org/" title="Data Vocabulary homepage">data-vocabulary.org</a>. There you will find classes for Person and Organization and properties for names and addresses, completely ignoring the millions of pieces of data using well established terms from <a href="http://xmlns.com/foaf/0.1/" title="FOAF vocabulary">FOAF</a> and the like.</p></blockquote>
<p>  That's when I figured out why the rating property looked weird.  Rather than using the <a href="http://vocab.org/review/terms.html" title="Review vocabulary">http://vocab.org/review/review.rdf</a> vocabulary, which defines a <code>http://purl.org/stuff/rev#minRating</code> and a <code>http://purl.org/stuff/rev#minRating</code>, the geeks at Google invented something new.  Ian's <a href="http://iandavis.com/blog/2009/05/googles-rdfa-a-damp-squib" title="Internet Alchemy &amp;raquo; Google&amp;#8217;s RDFa a Damp Squib">post</a> goes into greater detail about why this goes against the typical trend of reusing vocabularies.  I share Ian's hope that this is an error that will be corrected shortly, and his fear that this could be an example of a market leader trying to bend the rest of the world to its own ways.</p>
<h2>Update</h2>
<p><i>13-May-2009:</i>  For those seeking more information, there is a <a href="http://googlewebmastercentral.blogspot.com/2009/05/introducing-rich-snippets.html" title="Official Google Webmaster Central Blog: Introducing Rich Snippets">detailed posting</a> on the Google Webmaster Central Blog on the Rich Snippets.  And the question of the day seems to be whether <a href="http://googlewebmastercentral.blogspot.com/2009/05/introducing-rich-snippets.html?showComment=1242206220000#c2041139679460323259" title="Official Google Webmaster Central Blog: Introducing Rich Snippets">Google will support vocabularies other than their own</a>.
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://vocab.org/review/review.rdf to http://vocab.org/review/terms.html on January 28th, 2011.</p>
