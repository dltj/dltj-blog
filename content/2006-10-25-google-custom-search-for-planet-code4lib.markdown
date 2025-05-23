---
layout: wordpress-import
status: published
published: true
title: 'Google Custom Search for Planet Code4Lib'
modified: 2006-10-25T14:18:41+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 137
wordpress_url: http://dltj.org/2006/10/google-custom-search-for-planet-code4lib/
date: '2006-10-25 10:18:41 -0400'
date_gmt: '2006-10-25 14:18:41 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Google
- code4lib
comments:
- id: 6060
  author: 'Disruptive Library Technology Jester :: Google Custom Search&#8217;s Planet
    Code4Lib as an OpenSearch Plugin'
  author_email: ''
  author_url: http://dltj.org/article/planet-code4lib-google-custom-search-opensearch-plugin/
  date: '2006-10-25 17:22:06 -0400'
  date_gmt: '2006-10-25 21:22:06 -0400'
  content: "[...] Earlier I mentioned creating a Google Custom Search for Planet Code4Lib.
    The Google-supplied markup puts a form on your web page that leads to Google's
    server farm. (Alternatively, you can create a custom URL that points to an HTML
    page at Google which contains the form.) Well, that's really neat, but not far
    enough. How about an OpenSearch plugin suitable for Firefox and MSIE7? (Link to
    install in Firefox and MSIE7) Here is the plugin markup:  PLAIN TEXTXML: [...]"
- id: 6286
  author: Lorcan Dempsey's weblog
  author_email: ''
  author_url: http://orweblog.oclc.org/archives/001184.html
  date: '2006-10-26 22:19:06 -0400'
  date_gmt: ''
  content: "<!--%kramer-pre%--> across the contents of the repositories they list.
    As they point out, this search is based on whatever Google has indexed of the
    repository content, which in turn depends on local implementation/configuration
    details. Peter Murray put up a search of Dan Chudnov's Planet Code4Lib blogs.
    Bill Drew has created a Google custom search across his collection of wireless
    resources:I have been working on my Google custom search engine for WLANs and
    Libraries. It is available at <!--%kramer-post%-->"
- id: 33579
  author: kevin
  author_email: info@dynaseo.com
  author_url: http://www.dynaseo.com/sem
  date: '2008-07-15 03:55:06 -0400'
  date_gmt: '2008-07-15 07:55:06 -0400'
  content: "hi,\r\nPlease help me how I can use regular expression in google search
    box. for example i want to find web sites which are like this: www.google*.com\r\nOne
    of the result is www.googlechat.com"
- id: 33581
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-07-16 14:51:01 -0400'
  date_gmt: '2008-07-16 18:51:01 -0400'
  content: "Kevin --\r\n\r\nIt sounds to me like what you want is to search the DNS
    records (see my recent post about <a href=\"http://dltj.org/article/dns-vulnerabilities/\"
    rel=\"nofollow\">DNS vulnerabilities</a> for an overview of DNS).  I used to have
    a link to a site that searched DNS entries, but it looks like it was taken over
    by a spam site.  I can't find another one -- perhaps <acronym title=\"Disruptive
    Library Technology Jester\"><i>DLTJ</i></acronym> readers will be able to help
    out."
- id: 161569
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/25395305331560448
  date: '2011-01-13 03:34:47 -0500'
  date_gmt: '2011-01-13 08:34:47 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">del.icio.us: Google Custom Search for Planet Code4Lib
    http://bit.ly/enqzuL</span></span>'
---
<p>I wanted to mess around with Google's new <a href="http://www.google.com/cse/" title="Google Co-op - Custom Search Engine">Custom Search Engine</a> feature and in casting about for a list of URLs to feed it I thought I'd try the list of blogs at <a href="http://planet.code4lib.org" title="planet code4lib">Planet Code4Lib</a>.  As it turns out, this might be a modestly useful search if you remember reading something from one of the code4lib bloggers but can't remember which one.  The exercise was pretty fun and here is the result:</p>
<p><!-- Google CSE Search Box Begins --></p>
<form id="searchbox_017716194421589436379:zdoxzpetaxk" action="http://www.google.com/cse">
  <input type="hidden" name="cx" value="017716194421589436379:zdoxzpetaxk" /><br />
  <input name="q" type="text" size="40" /><br />
  <input type="submit" name="sa" value="Search" /><br />
  <input type="hidden" name="cof" value="FORID:0" /><br />
</form>
<p><!-- Google CSE Search Box Ends --></p>
<p>To build it, I started with the <a href="http://planet.code4lib.org/opml.xml" title="planet code4lib">Planet Code4Lib OPML feed</a> and ran some regular expression transformations against it, replacing these matches with empty strings (I used BBEdit on the Mac for this one-off, but it could probably be automated with a PERL script to a certain degree):</p>
```text
/feed/?(rss|atom)?/?$
(\?|<pre wp-pre-tag-0></pre>|<pre wp-pre-tag-0></pre>amp;)feed=(atom|rss2)$
(\?|<pre wp-pre-tag-0></pre>(amp;)?)feed=(atom|rss2)(<pre wp-pre-tag-0></pre>(amp;)?)
/?(wp-rss2.php|rss|index.*|atom.*|rdf)[^/\r]*$
```

<p>After a minimal amount of manual cleanup, I ended up with this list:</p>
```text
catalogablog.blogspot.com/*
www.wallandbinkley.com/quaedam*
maisonbisson.com/blog*
www.blyberg.net/*
use.perl.org/~LTjake/journal*
foam.lib.muohio.edu/blog/*
schenizzle.wordpress.com/*
onebiglibrary.net/node*
weblog.kevinclarke.info/*
feeds.feedburner.com/DanCohen*
www.librarywebchic.net/wordpress*
www.ecorrado.us/*
beta.blogger.com/feeds/3338174527262061848/posts/full*
textsfornothing.com/blog/*
orweblog.oclc.org/*
feeds.feedburner.com/hublog*
blog.ryaneby.com/*
meredith.wolfwater.com/wordpress*
fawcett.blogspot.com/*
kados.org/cgi-bin/blosxom.cgi*
lisletters.blogspot.com/*
digitallibrarian.org/*
www.patronizing.org/*
www.lackoftalent.org/*
www.kentongood.com/?cat=26*
www.epistemographer.com/*
blogdriverswaltz.com/*
outgoing.typepad.com/outgoing*
shelter.nu/blog*
interoperating.info/mark/blog/1*
www.tomkeays.com/blog*
lxming.blogspot.com/*
john.mignault.net/blog*
infomotions.com/musings/musings*
dltj.org/*
benostrowsky.wordpress.com/*
www.daveyp.com/blog*
efoundations.typepad.com/efoundations*
oregonstate.edu/~reeset/blog*
librarycog.uwindsor.ca:8087/artblog/librarycog*
inquiringlibrarian.blogspot.com/*
www.ibiblio.org/bess/*
thedil.wordpress.com/*
cavlec.yarinareth.net/archives/category/computers*
cavlec.yarinareth.net/archives/category/librariana*
coffeecode.net/feeds/categories/16-Coding*
dilettantes.code4lib.org/*
umlaut.library.gatech.edu/blog/*
www.inkdroid.org/journal*
techessence.info/node*
techessence.info/blog/1*
roytennant.com/*
vielmetti.typepad.com/vacuum*
dystmesis.com:8081/*
weibel-lines.typepad.com/weibelines*
dataunbound.wordpress.com/*
q6.oclc.org/*
del.icio.us/rss/tag/code4lib*
www.frbr.org/*
libdev.plymouth.edu/*
makinglinks.uwindsor.ca:8087/mitas/sfxblog*
open-ils.org/blog/*
oss4lib.org/node*
blogs.talis.com/panlibus*
feeds.technorati.com/feed/posts/tag/code4lib*
unalog.com/group/code4lib*
```

<p>...and fed that into the Google Custom Search control panel.</p>
<h2>Items of note in the Terms of Service</h2>
<p>Along the way I found some curious bits in the <a href="http://www.google.com/coop/docs/cse/tos.html" title="Google Co-op - Custom Search Engine">Google Custom Search Terms of Service</a>.  In particular:</p>
<blockquote><p>
<b>1.5 Exclusivity.</b> You agree that, during the Term, Google will be the exclusive provider of Internet search services on the Site. You further understand that Google will provide the Service on a nonexclusive basis, and that Google will continue to customize and provide its services to other parties for use in connection with a variety of applications, including search engine applications.
</p></blockquote>
<p>Section 1.1 defines <em>Site</em> this way:</p>
<blockquote><p>
For purposes of the Terms of Use, "<b>Site</b>" shall mean the Web site or sites on which You place JavaScript or similar programming ("<b>Code</b>") which renders the Google search box (or other means used by users of the Site ("<b>End Users</b>") to enter a search query ("<b>Query</b>")) on the Site ("<b>Search Box</b>").
</p></blockquote>
<p>One suspects what Google meant was that if you put up a Custom Search Box on your Site, then you must also use Google for any general internet search you might have -- you can't have a Google Custom Search Box and a Yahoo search box on the same Site, for instance.  I imagine that this also effectively locks out other internet search engine providers from offering the same service.  Since Google is the first-to-market, if Yahoo were to come up with a similar service you couldn't put a Google Custom Search and a Yahoo custom search pointing to each providers indexes with the same subset of URLs.  Since we know that each index contains different stuff and ranks results with different algorithms, one might imagine that the same custom search segments over a multiplicity of indexes could be a useful thing.</p>
<p>Ah, well -- it is still useful.  Just go in with your eyes open...
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.google.com/coop/cse/overview to http://www.google.com/cse/ on January 13th, 2011.</p>
