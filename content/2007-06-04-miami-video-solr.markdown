---
layout: wordpress-import
status: published
published: true
title: 'Solr-ized MARC Record Catalog'
modified: 2007-06-05T03:29:13+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 252
wordpress_url: http://dltj.org/2007/06/miami-video-solr/
date: '2007-06-04 23:29:13 -0400'
date_gmt: '2007-06-05 03:29:13 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- metadata
- opac
- apache
- lucene
- solr
comments: []
---
<p>Rob Casson of Miami University <span class="removed_link" title="http://foam.lib.muohio.edu/blog/?p=13">announced this weekend</span> the <a href="http://beta.lib.muohio.edu/solr/videos/" title="Miami University Video Catalog">beta availability of their video catalog</a>.  In a subsequent posting, Rob <span class="removed_link" title="http://foam.lib.muohio.edu/blog/?p=14">describes the user interface elements</span>.  Rob and the crew at Miami are seeking feedback on the interface, so if you have some <a href="http://beta.lib.muohio.edu/solr/videos/feedback.php" title="Video Catalog Feedback Form">be sure to offer it to them</a>.</p>
<p>A couple of notes on the mechanisms Rob is using.  <a href="http://lucene.apache.org/solr/" title="Apache Solr homepage">Apache Solr</a> is an open source enterprise search server based on the <a href="http://lucene.apache.org/java/" title="Apache Lucene homepage">Lucene Java</a> search library (also an Apache project).  You can think of Lucene as the raw indexing and search engine with Solr layered on top to provide a non-Java interface to a rich feature set.  What Miami has done is extract all of the bibliographic and related item records out of their Innovative Interface system, written programs to transform that data into XML, indexed it with Solr/Lucene and created a search interface.</p>
<p>Now what makes this really interesting is how much useful information is in the MARC record that doesn't currently find its way into the WebPAC interface.  For instance, this snapshot shows the facets where the MARC record has fielded data that can be turned into browsable lists:
<div style="border: 2px solid gray; font-size 90%; padding: .25em;"><img src="/assets/images/2007/06/browse_by_lc_class1.png" alt="Browse Catalog by LC Class" title="Browse Catalog by LC Class" width="623" height="242" style="border-bottom: 1px dashed gray;" />Example from Miami University's video catalog showing the available fielded data.</div>
<p>  The corresponding <a href="http://holmes.lib.muohio.edu/search/X" title="Miami University Libraries:Advanced Keyword Search">WebPAC pre-search limits (for keyword searching)</a> only includes a subset of languages, media formats, locations and does not include topic, genre, LC/SuDoc classes, and coverage date.  In other words, there is a whole lot of information in the MARC record that isn't being exposed in the normal WebPAC interface.  Since Miami is in full control over the data in the Solr-based index, though, they are free to include as much or as little in the end-user interface.</p>
<p>Combined with faceted browsing, this makes for a very simple and quick interface to narrow down a large set of records.  At the time of writing this entry, Miami's video library consisted of 10,538 records.  In three clicks, one can narrow that down to <a href="http://beta.lib.muohio.edu/solr/videos/index.php?query=%5B%2A+TO+%2A%5D&#038;filter_name[]=lang_facet&#038;filter_value[]=fre&#038;filter_name[]=format_facet&#038;filter_value[]=DVD&#038;filter_name[]=topic_facet&#038;filter_value[]=Comedy+films&#038;keep_filters=1" title="http://beta.lib.muohio.edu/solr/videos/index.php?query=%5B%2A+TO+%2A%5D&#038;filter_name[]=lang_facet&#038;filter_value[]=fre&#038;filter_name[]=format_facet&#038;filter_value[]=DVD&#038;filter_name[]=topic_facet&#038;filter_value[]=Comedy+films&#038;keep_filters=1">the 12 French-language comedy films in DVD format</a>:
<div style="border: 2px solid gray; font-size 90%; padding: .25em;"><img src="/assets/images/2007/06/french_dvd_comedy_films1.png" alt="Miami Video Catalog browse for French comedies in DVD" title="Miami Video Catalog browse for French comedies in DVD" width="603" height="71" border="0" style="border-bottom: 1px dashed gray;" />Example from Miami University's video catalog facets after browsing for French-language Comedies on DVD.</div>
<p>  From this screen, to see what is available in all media formats one need just click the red 'X' to the right of "DVD".  Also note the "RSS Feed" symbol on the right side of this interface snapshot.  The results of any search/browse are immediately available as an RSS feed -- a very convenient way to receive notifications of new titles that match this search!</p>
<p>Congratulations, Rob and everyone else at Miami that brought this interface into existence.  It is a nice model and something we all can learn from through your experiences.  Please keep us updated as the project continues.
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://foam.lib.muohio.edu/blog/?p=13 on February 11th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://foam.lib.muohio.edu/blog/?p=14 on February 11th, 2011.</p>
