---
layout: wordpress-import
status: publish
published: true
title: 'Advances in OpenSearch Definitions'
modified: 2009-04-21T12:52:15+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 896
wordpress_url: http://dltj.org/?p=896
date: '2009-04-21 08:52:15 -0400'
date_gmt: '2009-04-21 12:52:15 -0400'
categories:
- Raw Technology
tags:
- opensearch
- Ohio State University
comments:
- id: 159739
  author: Peter Murray
  author_email: ''
  author_url: ''
  date: '2009-04-21 12:52:20 -0400'
  date_gmt: '2009-04-21 16:52:20 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">New blog post: Advances in OpenSearch Definitions
    http://tinyurl.com/c3vxye</span></span>'
---
<p>[caption id="osul-opensearch" align="alignright" width="375" caption="Screenshot of adding the OSU Libraries Catalog Search"]<img src="http://library.osu.edu/blogs/labs/files/2.JPG" alt="" width="375" height="250" border="0" />[/caption] Earlier this month, Ohio State University Libraries <a href="http://ericschnell.blogspot.com/2009/04/osu-library-labs-concept-to-production.html" title="The Medium is the Message: OSU Library Labs: Concept to Production in 90 Days">launched</a> the <a href="http://library.osu.edu/blogs/labs/" title="Ohio State Library Labs">OSUL Labs</a> area.  (Congratulations and kudos to Eric Schnell and the others at OSU that have taken this step to "include customers as active participants in the development and/or testing of new products and services.") Their <a href="http://library.osu.edu/blogs/labs/2009/04/09/osu-library-labs-browser-search-extension/" title="OSU Library Labs: Browser Search Extension">first release</a> is an <span class="removed_link" title="http://library.osu.edu/opensearch.xml">OpenSearch definition for the library catalog</span>.  It has been ages since I've messed with OpenSearch, and I didn't remember (or didn't know it was possible) to have the function add the OpenSearch definition right from the OpenSearch menu, as shown in this figure from the OSUL announcement of this feature.  (What I remember is the "<a href="https://developer.mozilla.org/en/Adding_search_engines_from_web_pages">programatic</a>" way of doing this.)  The autodiscovery is done with a special
<link> tag in the head of the HTML:</p>
{% highlight html %}
<link rel="search"
  type="application/opensearchdescription+xml"
  href="http://library.osu.edu/opensearch.xml"
  title="Add OSU Libraries Catalog search" />
{% endhighlight %}
<p>But, in perusing the <a href="https://developer.mozilla.org/en/Creating_OpenSearch_plugins_for_Firefox">documentation for OpenSearch definitions</a>, I did learn that the next version of Firefox (<span class="removed_link" title="https://developer.mozilla.org/index.php?title=En/Firefox_3.1_for_developers&amp;redirect=no">3.1</span>, <a href="https://developer.mozilla.org/en-US/Firefox/Releases/3.5">3.5</a>, whatever) is introducing an <a href="https://developer.mozilla.org/en/Creating_OpenSearch_plugins_for_Firefox#Supporting_automatic_updates_for_OpenSearch_plugins">automatic update function for OpenSearch definitions</a>:</p>
{% highlight html %}
<url type="application/opensearchdescription+xml"
  rel="self"
  template="http://www.foo.com/mysearchdescription.xml"></url>
{% endhighlight %}
<p>Although it isn't clear how this is going to manifest itself in user interface (there are no clues in the <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=467890">Mozilla bug for this feature</a>; does the update happen automatically without the user doing anything? -- that seems dangerous.  Is the user prompted to update like in the Themes/Plug-ins Add-ons listing?), this sounds like something we should be supporting in order to future-proof our OpenSearch definitions.  (It is <a href="http://www.opensearch.org/Specifications/OpenSearch/1.1#The_.22Url.22_element" title="Specifications/OpenSearch/1.1/Draft 4 - OpenSearch">part</a> of the OpenSearch specification.)</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://library.osu.edu/opensearch.xml on January 28th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to https://developer.mozilla.org/index.php?title=En/Firefox_3.1_for_developers&redirect=no on November 13th, 2012.</p>
