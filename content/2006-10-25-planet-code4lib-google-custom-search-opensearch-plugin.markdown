---
layout: wordpress-import
status: published
published: true
title: 'Google Custom Search''s Planet Code4Lib as an OpenSearch Plugin'
modified: 2006-10-25T21:21:50+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 139
wordpress_url: http://dltj.org/2006/10/planet-code4lib-google-custom-search-opensearch-plugin/
date: '2006-10-25 17:21:50 -0400'
date_gmt: '2006-10-25 21:21:50 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Google
- code4lib
- opensearch
comments:
- id: 6085
  author: 技术酒徒
  author_email: ''
  author_url: http://kevenlw.blogspot.com/2006/10/blog-post_26.html
  date: '2006-10-26 14:35:42 -0400'
  date_gmt: ''
  content: "<!--%kramer-pre%--> 另外钱涂给了一个厦大的聚合网站，甚好。但能不能弄成这样的模式，还可以集成Google Custom
    Search功能，就方便了。聚合器好是好，但是还没有圈子那样更Portal，加上搜索功能可以弥补一下。大侠们以为如何？ <!--%kramer-post%-->"
- id: 6376
  author: Coin web d&rsquo;Igor
  author_email: ''
  author_url: http://www.igor-web.net
  date: '2006-11-03 22:21:03 -0500'
  date_gmt: ''
  content: "<!--%kramer-pre%--> delicieux  Google Custom Search&rsquo;s Planet Code4Lib
    as an OpenSearch Plugin in Disruptive Library Technology Jester (3 novembre) Cr&eacute;er
    un plugin de recherche Firefox - Shaun { the blog } - Cr&eacute;ation Internet,
    webdesign, tutoriaux PHP, Flash, Photoshop (3 novembre) SPARQL Protocol and Query
    Language: Frequently Asked Questions<!--%kramer-post%-->"
- id: 9060
  author: 数图研究 &raquo; 守望也要有个家
  author_email: ''
  author_url: http://xmulib.net/keven/?p=145
  date: '2006-12-13 10:31:59 -0500'
  date_gmt: '2006-12-13 15:31:59 -0500'
  content: "[...] 另外钱涂给了一个厦大的聚合网站，甚好。但能不能弄成这样的模式，还可以集成Google Custom Search功能，就方便了。聚合器好是好，但是还没有圈子那样更Portal，加上搜索功能可以弥补一下。大侠们以为如何？
    [...]"
- id: 13299
  author: 技术酒徒
  author_email: ''
  author_url: http://kevenlw.blogspot.com
  date: '2007-02-15 08:53:01 -0500'
  date_gmt: '2007-02-15 08:53:01 -0500'
  content: "<!--%kramer-pre%-->又有google后台的强大支撑，包括blogsearch，但是google连自己的访问都朝不保夕，别说blogspot了。
    \ 另外钱涂给了一个厦大的聚合网站，甚好。但能不能弄成这样的模式，还可以集成Google Custom Search功能，就方便了。聚合器好是好，但是还没有圈子那样更Portal，加上搜索功能可以弥补一下。大侠们以为如何？
    \ 厦大现在众望所归，难免人们对她的要求高一些<!--%kramer-post%-->"
---
<p>
Earlier I mentioned creating a <a href="/article/google-custom-search-for-planet-code4lib/">Google Custom Search for Planet Code4Lib</a>.  The Google-supplied markup puts a form on your web page that leads to Google's server farm.  (Alternatively, you can create a custom URL that points to an HTML page at Google which contains the form.)  Well, that's really neat, but not far enough.  How about an <a href="/assets/images/2006/10/planet-code4lib-search.xml" title="OpenSearch Description of Planet Code4Lib Search via Google Custom Search">OpenSearch plugin</a> suitable for Firefox and MSIE7?  Here is the plugin markup:</p>
```xml
< ?xml version="1.0" encoding="UTF-8"?>
 <opensearchdescription xmlns="http://a9.com/-/spec/opensearch/1.1/" xmlns:moz="http://www.mozilla.org/2006/browser/search/">
   <shortname>Planet Code4Lib</shortname>
   <description>Search the bloggers of Planet Code4Lib using Google Custom Search.</description>
   <inputencoding>UTF-8</inputencoding>
   <tags>code4lib library</tags>
   <contact>peter@OhioLINK.edu</contact>
   <url type="text/html" template="http://www.google.com/cse?q={searchTerms}&amp;cx=017716194421589436379:zdoxzpetaxk&amp;sa=Search&amp;cof=FORID:0">
      <image height="16" width="16" type="image/png">
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAwBQTFRF////s7OzNDQ0SkpKioqKbGxsoaGhe3t7KSkp6enpWFhYHR0dzMzMl5eXYmJivr6+8/PzPj4+2traAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVWdikQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAI1JREFUKFNVTlsCwyAIE0SMLdSV+x92WLuP5SvmISnlgQLgTTcui/gTMGLi52oSDKMUzFbagQ/CXDqO4zEjwMMO0AihImJmQWEUYdOlwEhpLpC6a80KX04JlV75fC4Za8LvFu9hELmotva+TyfvK/RO5ZZ1Zkplb00q1b2pyI50lpafc9bW8ATdy2l1+1/rhQUihcZntwAAAABJRU5ErkJggg==</image>
      <adultcontent>false</adultcontent>
      <moz :searchform>http://dltj.org/2006/10/google-custom-search-for-planet-code4lib/
   </moz></url>
</opensearchdescription>
```
<p>Pretty neat, eh?  This link will <a href="javascript:window.external.AddSearchProvider(&#039;http://dltj.org/wp-content/uploads/2006/10/planet-code4lib-search.xml&#039;);">install the search definition in Firefox and MSIE7.</a></p>
<h2>Is this going too far?</h2>
<p>One can't help but to wonder whether this violates the <a href="http://google.com/coop/docs/cse/tos.html" title="Google Co-op - Custom Search Engine">Google Custom Search Terms of Service</a>.  Here is a piece of <b>1.1 Description of Service.</b></p>
<blockquote><p>
For purposes of the Terms of Use, "Site" shall mean the Web site or sites on which You place JavaScript or similar programming ("Code") which renders the Google search box (or other means used by users of the Site ("End Users") to enter a search query ("Query")) on the Site ("Search Box"). All Queries sent from the Site to Google shall comply with the technical specifications that Google may provide from time to time, and and must originate from the Site.
</p></blockquote>
<p>So I'm not really using JavaScript, but I am using XML markup.  Can "Site" mean the user's web browser interface?  Further on in the ToS:</p>
<blockquote><p>
<b>1.3 Your Obligations.</b><br />
You shall receive a Query from the End User and shall forward that Query<br />
to Google. You may not in any way frame or cache the Results produced<br />
by Google, except as otherwise agreed to between You and Google. Google<br />
will not be responsible for receiving Queries from End Users or for<br />
transmission of data between You and Google's network interface. You<br />
shall be responsible for providing all hardware and software required<br />
to perform Your obligations under the Terms of Use, including but not<br />
limited to the following: (a) implementing and maintaining the Site,<br />
(b) implementing and maintaining the interface between the Site and<br />
the Service, and (c) receiving a Query from an End User and transmitting<br />
the Query to Google.
</p></blockquote>
<p>So with the search plugin, I'm not receiving the query &mdash; rather I'm facilitating the process of forwarding the query from the user's browser to Google.  So far, so good, I think.  The search plugin doesn't frame or cache the results; I'm okay with that clause.  With regard to my obligations, I'll maintain DLTJ as the source of the OpenSearch XML configuration file (unless someone wants to put it directly on code4lib.org somewhere), but again DLTJ is not sitting between the end user and Google so I don't think points (b) and (c) apply.</p>
<p>Too much legalese.  In the spirit of <a href="http://en.wikipedia.org/wiki/Mashup_%28web_application_hybrid%29" title="Mashup (web application hybrid)">mashups</a> everywhere, I'll put this out and ask for forgiveness if it violates Google's sensibilities rather than asking for permission first.</p>
