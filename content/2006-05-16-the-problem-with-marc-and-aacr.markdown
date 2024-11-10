---
layout: wordpress-import
status: published
published: true
title: 'The Problem with MARC and AACR: the World Doesn''t Disco Anymore'
modified: 2006-05-16T12:21:17+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 58
wordpress_url: http://dltj.org/2006/05/the-problem-with-marc-and-aacr-the-world-doesnt-know-disco/
date: '2006-05-16 08:21:17 -0400'
date_gmt: '2006-05-16 13:21:17 -0400'
category: Disruption in Libraries
categories:
- Disruption in Libraries
tags:
- MARC
- AACR
comments:
- id: 86
  author: Kevin S. Clarke
  author_email: ksclarke@gmail.com
  author_url: ''
  date: '2006-05-16 09:41:22 -0400'
  date_gmt: '2006-05-16 14:41:22 -0400'
  content: Not your point, I know, but get rid of those colons and semicolons in the
    datafield XML example.  MARC needs them (confusing display with structure), but
    in XML they should be treated as display only (and provided by a stylesheet).  :-)
- id: 87
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-05-16 10:23:13 -0400'
  date_gmt: '2006-05-16 15:23:13 -0400'
  content: "Actually, I lifted the examples straight from <a href=\"http://www.loc.gov/standards/marcxml/Sandburg/sandburg.xml\"
    rel=\"nofollow\">demonstration MARCXML record from LC</a>.  Interestingly enough,
    there is <a href=\"http://www.loc.gov/standards/marcxml/Sandburg/sandburgmods.xml\"
    rel=\"nofollow\">a MODS version of that sample record</a> that can be viewed at
    the directory index, and it has this for the description field:\r\n\r\n<div style=\"margin-left:
    2em; font-family: monospace;\">\r\n<physicalDescription>\r\n&nbsp;&nbsp;<form
    authority=\"marcform\">print</form>\r\n&nbsp;&nbsp;<extent>1 v. (unpaged) : ill.
    (some col.) ; 26 cm.</extent>\r\n</physicalDescription>\r\n</div>\r\n\r\nCan't
    MODS do any better than that?"
- id: 88
  author: K.G. Schneider
  author_email: kgs@bluehighways.com
  author_url: http://freerangelibrarian.com
  date: '2006-05-16 16:22:52 -0400'
  date_gmt: '2006-05-16 21:22:52 -0400'
  content: Dude, this was luminous. Seriously.
- id: 91
  author: caleb t-r
  author_email: caleb@tucker-raymond.net
  author_url: http://www.stealthislibrary.com
  date: '2006-05-16 20:10:24 -0400'
  date_gmt: '2006-05-17 01:10:24 -0400'
  content: "good insight peter. i'm glad to find you blogging.\r\n\r\nrelated, i was
    dabbling in ajax recenently and was completely frustrated at the audacity to iterate
    XML with a language that barely supports arrays.\r\n\r\nwhat i *love* about XML
    is XSLT. i'm sure many transforms are processor hogs, but  the result is elegant
    to me, and i love never even having to wonder whether that semicolon is part of
    the text or part of the format."
- id: 172
  author: This Old Library at ebyblog
  author_email: ''
  author_url: ''
  date: '2006-05-21 10:55:01 -0400'
  date_gmt: '2006-05-21 14:55:01 -0400'
  content: "[...] The Problem with MARC and AACR: the World Doesn&rsquo;t Disco Anymore
    At their creation, MARC and AACR propelled library services to new heights of
    efficiency and usefulness. Here&rsquo;s my problem, though: we no longer live
    in the 1970s, and the fundamental tools of our trade should not be based in nearly
    40-year-old technology. [...]"
- id: 173
  author: kathleen
  author_email: kmccook@tampabay.rr.com
  author_url: ''
  date: '2006-05-21 11:01:27 -0400'
  date_gmt: '2006-05-21 15:01:27 -0400'
  content: "Data archives. Check them out. DATA LIBRARIES FOR THE SOCIAL SCIENCES.
    Library Trends 30 (Winter 1982).See also Aye-Aye.Thanks for the insights.\r\n--Kathleen"
- id: 30981
  author: links for 2008-02-16 &laquo; Talkabout
  author_email: ''
  author_url: http://talkabout.wordpress.com/2008/02/16/links-for-2008-02-16/
  date: '2008-02-15 22:25:27 -0500'
  date_gmt: '2008-02-16 03:25:27 -0500'
  content: "[...] The Problem with MARC and AACR: the World Doesn&rsquo;t Disco Anymore
    (Disruptive Library Technology Jes... &#8220;And more to the point, let&rsquo;s
    not forget AACR where every colon, period, and dash carries meaning versus the
    explicit description of attributes in XML. Example? Look at 300 |a1 v. (unpaged)
    : |bill. (some col.) ;|c26 cm. [...]"
---
<p>My undergraduate background is in computer science, and from that perspective I have a great deal of admiration for MARC and AACR as well as their creators and proponents: Henriette Avram and Michael Gorman.  At their creation, MARC and AACR propelled library services to new heights of efficiency and usefulness.  Here's my problem, though: we no longer live in the 1970s, and the fundamental tools of our trade should not be based in nearly 40-year-old technology.</p>
<p>This post started out as a comment to <a href="http://lisnews.org/node/26973" title="Gorman and Fischerspooner | LISNews:">an LISnews thread</a> by <span class="removed_link" title="http://librarian.lishost.org/">Kathleen</span> <a href="http://unionlibrarian.blogspot.com/" title="Union Librarian">de</a> <a href="http://justicelibraries.blogspot.com/" title="Librarians for Human Rights">la</a> <a href="http://justicelibraries.blogspot.com/" title="Librarians for Human Rights">Pe&ntilde;a</a> <a href="http://librarianoutreach.blogspot.com/" title="A LIBRARIAN AT THE KITCHEN TABLE">McCook</a> that pointed back to a posting with the title <span class="removed_link" title="http://librarian.lishost.org/?p=382">Michael Gorman, Fischerspooner, Amnesty International and Hamlet</span>.  The more I thought about it, though, the more the comment went beyond a criticism of my perception of <span class="removed_link" title="http://mg.csufresno.edu/">Michael Gorman's</span> <a href="http://www.libraryjournal.com/article/CA502009.html" title="BackTalk: Revenge of the Blog People!">world view</a>.  I must admit that I was also influenced by the <a href="http://www.i-am-bored.com/bored_link.cfm?link_id=17295" title="Evolution of Dance | I Am Bored">Evolution of Dance</a> video that is making the rounds on the net (thanks, Thomas!) &mdash; hence the byline to this post.  So I've edited the comment and posted it here (with comments and trackbacks open, I might add) for posterity.</p>
<p>I noted this statement in the <a href="http://www.libraryjournal.com/article/CA6331810.html" title="MARC Creator Henriette Avram Dies at 86">announcement of Henriette Avram passing</a>: "Though Avram was a systems analyst by training, not a librarian, her work ... revolutionized access to library materials."  Right on the mark.  With that background in computer science I'd like to think I have a somewhat unique (or at least minority) perspective on Avram's and Gorman's work.  They did what they did in a world with the twin challenges of expensive computing cycles and scarce storage.  MARC and AACR were created when punch cards and 9-track tapes ruled the world and computers took up rooms.  (Wanted one for your desk? Hah!)</p>
<p>Fast forward to today.  Computer cycles are so cheap that we stack CPUs in huge racks to collectively work on solving a problem. Storage is so cheap that we consider a verbose, ASCII-based markup language (a.k.a. "XML") as the state of the art in the transmission of data. Compare the information density of 1000 characters of MARC versus 1000 characters of XML. And more to the point, let's not forget AACR where every colon, period, and dash carries meaning versus the explicit description of attributes in XML. Example? Look at</p>
```
300    |a1 v. (unpaged) : |bill. (some col.) ;|c26 cm.
```
<p>versus</p>
```xml
<datafield tag="300" ind1=" " ind2=" ">
  <subfield code="a">1 v. (unpaged) :</subfield>
  <subfield code="b">ill. (some col.) ;</subfield>
  <subfield code="c">26 cm.</subfield>
</datafield>
```
<p>See what I mean? The first is 51 characters, more or less, and the second is 185 characters. Now I'd argue that the second is not much more expressive than the first. (The second is MARCXML -- a raw translation of the MARC record format to XML.) But take a look at this more mainstream XML format (from MODS):</p>
```xml
<subject authority="lcsh">
  <geographic>United States</geographic>
  <topic>Politics and government</topic>
  <temporal>20th century.</temporal>
</subject>
```
<p>A human can read and understand that as well as being parsable by a computer.</p>
<p>Now anyone that would have proposed the second or third of these examples in the 1960s or 1970s would have been laughed out of the machine room and told never to come back. Sure, you could write a computer program back then to read and write those XML-based formats, but it would have been so computationally- and storage-expensive that it would never have been taken seriously, much less actually contribute to the spread of machine-based cataloging tools.</p>
<p>So back to this decade, when storage is cheap and computer processing power even cheaper. Interoperability with other systems outside the library domain is more and more important. There is a computer on every desk...and one in your pocket. The user is empowered with a combination of better human/machine interfaces (we've exchanged punch cards for keyboards, mice and graphical user interfaces) and inexpensive communication mechanisms (that make machine-aided tagging and recommendation engines possible).</p>
<p>I've never met Ms. Avram, nor have I followed her work (and in fact I didn't know of her connection to MARC until this announcement), but I wonder what she would think of the MARC/AACR combination now.  Given her training in systems analysis, would she say we are making the best use of computing technology today?</p>
<p>Is this the death knell for the librarian? Not necessarily. If the profession continues to train and promote the librarian of the 1960s, 70s and 80s, then yes. If that librarian is one that recognizes the shift to user-empowered technology in the past decade, nebulously characterized as "Library 2.0", then we have a valuable value-added role to play in the information-seeking and -use activities of citizens in this new world.  Are our users disco dancing?  If not, we'd better figure out how they are dancing now...</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://lisnews.org/article.pl?sid=06/05/13/1719246 to http://lisnews.org/node/26973 on January 13th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://librarian.lishost.org/ on August 22nd, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://librarian.lishost.org/?p=382 on August 22nd, 2012.</p>
