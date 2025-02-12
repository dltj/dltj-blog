---
layout: wordpress-import
status: published
published: true
title: 'Analysis of Google Scholar and Google Books'
modified: 2007-08-15T20:34:29+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 275
wordpress_url: http://dltj.org/2007/08/google-scholar-and-books/
date: '2007-08-15 16:34:29 -0400'
date_gmt: '2007-08-15 20:34:29 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- publishing
- ejournal
- Google
- Directory of Open Access Journals
- Google Book Search
- Google Scholar
comments:
- id: 20990
  author: New Basement Tapes
  author_email: ''
  author_url: http://new-basement-tapes.blogspot.com/2007/08/analysis-of-google-scholar-and-google.html
  date: '2007-08-19 09:21:00 -0400'
  date_gmt: '2007-08-19 13:21:00 -0400'
  content: "<!--%kramer-pre%--> Analysis of Google Scholar and Google Books in Disruptive
    Library Technology Jester <!--%kramer-post%-->"
- id: 21103
  author: David F. Flanders
  author_email: dff1978@gmail.com
  author_url: http://dfflanders.wordpress.com
  date: '2007-08-21 13:03:54 -0400'
  date_gmt: '2007-08-21 17:03:54 -0400'
  content: 'And yet Google Books takes that value-added step that keeps students/researchers
    coming back: http://scilib.typepad.com/science_library_pad/2007/08/google-earth-bo.html'
- id: 21108
  author: Informatoin Retrieval 2.0 &laquo; David F. Flanders
  author_email: ''
  author_url: http://dfflanders.wordpress.com/2007/08/21/informatoin-retrieval-20/
  date: '2007-08-21 13:56:47 -0400'
  date_gmt: '2007-08-21 17:56:47 -0400'
  content: "[...] 2.0. (IR=Information Retrieval).&nbsp; In the first case it is Peter
    Murray&#8217;s blog on the &#8216;Analysis of Google Scholar and Google Books&#8216;
    which points out -rightly so- that Google Scholar / Books are not comprehensive
    in their [...]"
- id: 22015
  author: 数图研究 &raquo; Blog Archive &raquo; 情报检索2.0
  author_email: ''
  author_url: http://xmulib.net/keven/archives/439
  date: '2007-09-03 21:22:35 -0400'
  date_gmt: '2007-09-04 01:22:35 -0400'
  content: '[...] <a href="http://translate.google.com/translate?u=http://www.dlresearch.cn/keven/index.php/archives/465"
    title="Translation to English provided by Google" rel="nofollow">[English Translation]</a>
    David比较了&#8217;Analysis of Google Scholar and Google Books&#8216;和&#8221;Google
    Earth Book Search&#8220;，认为后者才是比较地道的情报检索2.0。 [...]'
---
<p>Two papers were published recently exploring the quality of <a href="http://scholar.google.com/" title="Google Scholar homepage">Google Scholar</a> and <a href="http://books.google.com/" title="Google Book Search homepage">Google Books</a>.</p>
<p><br clear="all" /><br />
<h2>Google Scholar</h2>
<p>Philipp Mayr and Anne-Kathrin Walter, both of GESIS / Social Science Information Center in Bonn, Germany, uploaded an article to arXiv called "<a href="http://arxiv.org/abs/0707.3575" title="arXiv abstract page for &#039;An exploratory study of Google Scholar&#039;">An exploratory study of Google Scholar</a>."  ((Judging from the citation listed on <span class="removed_link" title="http://www.gesis.org/IZ/Mayr/">Philipp Mayr's homepage</span>, the article will appear in an upcoming issue of Online Information Review from Emerald Group Publishing.))  Originally created as a presentation for a 2005 conference, it was updated in January 2007 to reflect new findings and published as a paper.  Excerpts from the abstract include:<br />
<blockquote>The study shows deficiencies in the coverage and up-to-dateness of the [Google Scholar] index. Furthermore, the study points up which web servers are the most important data providers for this search service and which information sources are highly represented. We can show that there is a relatively large gap in Google Scholar&rsquo;s coverage of German literature as well as weaknesses in the accessibility of Open Access content. Major commercial academic publishers are currently the main data providers. </p>
<p>We conclude that Google Scholar has some interesting pros (such as citation analysis and free materials) but the service can not be seen as a substitute for the use of special abstracting and indexing databases and library catalogues due to various weaknesses (such as transparency, coverage and up-to-dateness).</p></blockquote>
<p>The authors performed a "brute force analysis" (their words) of the coverage of Google Scholar by comparing search results by journal title with five journal lists:  ISI Arts & Humanities Citation Index, ISI Social Science Citation Index, ISI Science Citation Index, open access journals listed by <abbr title="Directory of Open Access Journals">DOAJ</abbr>, and journals from the SOLIS database (mainly German-language journals from sociological disciplines).  They queried Google Scholar using the "Return articles published in..." limiter on the advanced search screen, downloaded the first 100 records for each title, then parsed and analyzed each of the records.  In total, 621,000 records from Google Scholar search results were analyzed.</p>
<p><img src="/assets/images/2007/08/IdentificationOfJournals.png" alt="Number of Articles Found in Google Scholar by Title List" title="Number of Articles Found in Google Scholar by Title List" align="right" width="431" height="291" border="0" style="padding: 0 0 1.5em 2em;" />The authors first determined the coverage of titles in the five journal lists in the Google Scholar database.  The authors note surprise at the relative lack of coverage for open access titles listed in the DOAJ.  I think this can be explained by the fact that many open access publishers are not using a systematic application to put their content on the internet.  Of the 2,804 journals in the DOAJ directory, only 846 are searchable via DOAJ's own article-level indexing service. ((Numbers from the <a href="http://www.doaj.org/" title="Directory of Open Access Journals homepage">DOAJ home page</a>, as of 15-Aug-2007.))  If the journals can't be easily harvested at the article level, then they Google can't add them to the Scholar article index.</p>
<p><br clear="all" /><img src="/assets/images/2007/08/DistributionOfDocumentTypes.png" alt="Distribution of Document Types Among the Lists Queried" title="Distribution of Document Types Among the Lists Queried" align="right" width="430" height="291" border="0" style="padding: 0 0 1.5em 2em;" />Based on the semantics provided in each record, the authors divided the results into three categories (referred to in the paper as "document types"):  links to complete descriptive records on an external (publisher's or aggregator's) site, citation-only records (no full-text and no link to more complete information at an external site), and direct access links to full text.  The distribution of results is shown in the table to the right.</p>
<p>The paper also includes an analysis of the various publisher and portal sites that supply information to Google Scholar's index.  </p>
<h2>Google Books</h2>
<p>The August issue of First Monday contains an article by Paul Duguid called "<a href="http://www.firstmonday.org/issues/issue12_8/duguid/index.html" title="First Monday article: &#039;Inheritance and loss? A brief survey of Google Books&#039;">Inheritance and loss?  A brief survey of Google Books</a>".  The article is a somewhat contrived exploration of the Google Books Library Project through his lens of quality assurance derived "through innovation or through 'inheritance.'"  His thesis seems to be that users expect the reputations of the libraries participating in the project (Harvard, University of Michigan, New York Public, Stanford, and Oxford among the <a href="http://books.google.com/googlebooks/partners.html" title="Google Book Search Library Partners">other partners</a> are arguably a reputable group) convey a level of quality to the results of the digitization process in the Google Books Library Project.  Duguid then goes on to pick what arguably has to be the hardest book artifact to capture digitally (various editions of Laurence Sterne's "<a href="http://andromeda.rutgers.edu/~jlynch/Biblio/shandy.html" title="Tristram Shandy: An Annotated Bibliography by Jack Lynch"><i>The Life and Opinions of Tristram Shandy, Gentleman</i></a>") as an example of everything that is wrong with Google Books.  </p>
<p>I don't subscribe to that notion at all, but it is perhaps because I've been around enough technology and innovation to know that each new service needs to stand on its own.  <i>Tristram Shandy</i> is in part an experiment in typography and layout by the author, as Duguid describes in detail in this article, that is unusual and atypical to the extreme, so I think many of the characterizations of the Google Books project, based on this one artifact, are unfair and short-sighted.  When you strip away the false dichotomy of innovative-or-inherited-quality, the oddities surrounding the <i>Tristram Shandy</i> artifact, and various unnecessary pot-shots (("A quick look at the online catalogue for Stanford&rsquo;s library shows that the Stanford volume presented as your second choice by Google Books is actually tucked away in the Stanford Auxiliary library along with &ldquo;infrequently&ndash;used&rdquo; texts.")) Duguid's analysis does point to some apparent problems with Google's scheme for digitizing and indexing books.  The quality of some of the scans pointed out in the <i>Tristram Shandy</i> artifact and others are sources of concern.  Substandard metadata is another:<br />
<blockquote>Not a word is mentioned about multiple volumes or volume number. Indeed, a quick survey of the Google Book Project suggests that Google doesn&rsquo;t recognize volume numbers. Not only are the different editions (Harvard&rsquo;s from 1896, Stanford&rsquo;s from 1904) given exactly the same name, but also the different volumes of this Stanford&rsquo;s multivolume edition are labeled identically. Consequently, whatever algorithm Google uses to find the book, it is quite likely, as in this case, to offer volume II first.</p></blockquote>
<p>Reservations aside, it is a good review the some of the problematic outcomes of the Google Books Library Project.
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.gesis.org/IZ/Mayr/ on November 6th, 2012.</p>
