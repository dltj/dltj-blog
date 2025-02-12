---
layout: wordpress-import
status: published
published: true
title: 'On the Internet, How Do You Know If You Are Talking to a Dog?'
modified: 2008-07-16T02:51:10+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 387
wordpress_url: https://dltj.org/?p=387
date: '2008-07-15 22:51:10 -0400'
date_gmt: '2008-07-16 02:51:10 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Google
- networking
- domain name service
- opendns
comments:
- id: 33590
  author: PALINET Tech Update - PLN
  author_email: ''
  author_url: ''
  date: '2008-07-18 08:30:44 -0400'
  date_gmt: '2008-07-18 12:30:44 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Tech Update Selected technology-related posts
    from a variety of library blogs On the Internet, How Do You Know If You Are Talking
    to a Dog? 15 July 2008  Think you know Google Search? 15 July 2008  AquaBrowser
    releases reviews and ratings [...]<!--%kramer-ref-post%-->"
- id: 33594
  author: 'PortalEyes: How DNS works'
  author_email: ''
  author_url: http://portaleyes.blogspot.com/2008/07/how-dns-works.html
  date: '2008-07-18 14:03:44 -0400'
  date_gmt: '2008-07-18 18:03:44 -0400'
  content: "<!--%kramer-ref-pre%-->[...] note, 2.) it has an excellent description
    and illustration of how DNS (Domain Name Service) works.On the Internet, How Do
    You Know If You Are Talking to a Dog?      Posted by Sarah Bourne   at 4:59 PM
    \                      Labels: network technology, [...]<!--%kramer-ref-post%-->"
- id: 33595
  author: On the Internet, How Do You Know If You Are Talking to a Dog? | LISNews
  author_email: ''
  author_url: http://lisnews.org/node/30625/
  date: '2008-07-18 15:46:59 -0400'
  date_gmt: '2008-07-18 19:46:59 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Note&rdquo; on Multiple DNS implementations
    vulnerable to cache poisoning. What does that mean? Read on&hellip; Technorati
    Tags: Internet Technology  digg_url = [...]<!--%kramer-ref-post%-->"
- id: 33655
  author: 'Techno-fil (30/07/08) : pintiniblog'
  author_email: ''
  author_url: ''
  date: '2008-07-30 10:36:18 -0400'
  date_gmt: '2008-07-30 14:36:18 -0400'
  content: "<!--%kramer-ref-pre%-->[...]  - 25 Free Stock Photo Sites (source: Digital
    Image Magazine) Des photos en veux-tu en voil&agrave;.  - On the Internet, How
    Do You Know If You Are Talking to a Dog? (source: Disruptive Library Technology
    Jester, 16/07/08) A propos du probl&egrave;me de vuln&eacute;rabilit&eacute; [...]<!--%kramer-ref-post%-->"
- id: 656263
  author: 'PortalEyes: How DNS works'
  author_email: ''
  author_url: http://portaleyes.blog.state.ma.us/2008/07/how-dns-works.html
  date: '2014-03-20 10:08:19 -0400'
  date_gmt: '2014-03-20 14:08:19 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;] note, 2.) it has an excellent description
    and illustration of how DNS (Domain Name Service) works.On the Internet, How Do
    You Know If You Are Talking to a Dog?      Posted by    Sarah Bourne     at  4:59
    [&#8230;]<!--%kramer-ref-post%-->"
---
<div style="width:440px; font-size:85%; float: right; padding: 0 0 1.5em 2em;"><embed type="application/x-shockwave-flash" src="http://www.cartoonbank.com/content/ebiz/cartoonbank/resources/fluidretail/standard/v2/swf/cengage_preloader.swf" style="" id="display_detail_1295491413913_176827" name="display_detail_1295491413913_176827" bgcolor="#ffffff" quality="high" swliveconnect="true" allowscriptaccess="always" wmode="opaque" base="." flashvars="productViewXML=../../../customers/c892/10/61/97/106197_detail/pview_106197_detail.xml&amp;productId=106197&amp;width=440&amp;height=350&amp;bgColor=#ffffff&amp;preloaderBGColor=6710886&amp;preloaderFGColor=13421772&amp;logFunction=handleDisplayLogEvent&amp;onLoadHandler=handleDisplayLoaded&amp;onErrorHandler=handleDisplayError&amp;extraVariables=p_id%3D106197%26p_path%3D10/61/97/&amp;htmlURL=www.cartoonbank.com&amp;zoomWinLCID=_lcid_display_detail_1295491413913_176827" width="440" height="350"/>Published in <i>The New Yorker</i> July 5, 1993.<br />Image from <a href="https://www.condenaststore.com/-sp/On-the-Internet-nobody-knows-you-re-a-dog-New-Yorker-Cartoon-Prints_i8562841_.htm" title="Peter Steiner : &#8220;On the Internet, nobody knows you&#8217;re a dog.&#8221; - Cartoonbank.com">The Cartoon Bank</a></div>
<p>The famous 1993 cartoon from The New Yorker has the caption &ldquo;On the Internet, nobody knows you&rsquo;re a dog.&rdquo;  The question at the moment is:  when you're on the internet, how do you know you are not talking to a dog?  When you ask to connect to a remote service, you expect to connect to that remote service.  You probably don't even think about the possibility that "myspace.com" might not be "myspace.com".  But what if you couldn't rely on that?  How about "mybank.com"?  Believe it or not, you may exist in such a world today.  Last week, US-CERT issued a "Vulnerability Note" on <a href="http://www.kb.cert.org/vuls/id/800113" title="US-CERT Vulnerability Note VU#800113">Multiple DNS implementations vulnerable to cache poisoning</a>.  What does that mean?  Read on...<br />
<!--more--></p>
<h2>DNS:  The Internet's Addressbook</h2>
<p>Your computer (or, in some special cases such as a home network setup, "your entire network" ((This happens with a technique called "Network Address Translation" or NAT.  NAT was created to conserve the internet address space (among other reasons) by putting multiple computers behind a device that makes all of the computers look like one machine to the outside world.  If you connect to the rest of the world via a small hub, you're probably using NAT.  If the IP address of your computer starts with "10" or "192.168" you are definitely using NAT.))) is uniquely defined on the internet by an "IP address".  It is a series of four numbers separated by a period; something like "216.178.38.116".  Every computer on the network has one.  The issue is that these numbers are not as easy to remember as names like "myspace.com".  Enter DNS...</p>
<p>It is the Domain Name System, or DNS, that translates an easily recognizable name to an IP address.  DNS is a distributed database of names-to-numbers (and numbers-to-names and all sorts of other mappings).  A network machine -- say, your desktop computer -- is running a program (a web browser) that needs to connect to a server.  It relies on a DNS client to perform the name-to-number mapping.  This figure shows a simplified relationship between all of the parts.</p>
{{ image(
    div_float="none",
    width="500",
    caption="Sequence Diagram Showing Normal DNS Operation",
    alt="Sequence Diagram Showing Normal DNS Operation",
    localsrc="2008/07/dns-normal.png") }}
<p>On your computer, the web browser makes a request with the local DNS client to one of the DNS servers it knows.  (You'll see this DNS service listed if you look at the network properties on your computer.)  DNS servers can, and typically do, remember the answers to recently asked questions from other DNS clients (a feature called "caching"); if the DNS server can answer the question from its cache, it will.  If not, one of two things can happen:  1) DNS Server 1 can send a message back saying it doesn't know but suggest where it might go to find an answer; or 2) attempt to find the answer itself and send it back to the DNS client.  The latter is what is pictured above and is called "recursive name resolution".  DNS Server 1 can also cache the information so as to answer a subsequent question for the same information without having to go out and ask another DNS server for it.  ((The amount of time a caching DNS server can hold onto information on behalf of an "authoritative" DNS server is specified as part of the DNS protocol, but such consideration is outside the scope of what is being talked about here.))</p>
<h2>When DNS Goes Bad</h2>
<p>So what is the problem?  The United States Computer Emergency Readiness Team (<a href="http://www.us-cert.gov/about-us" title="US-CERT: About Us">US-CERT</a>) <a href="http://www.us-cert.gov/cas/techalerts/TA08-190B.html" title="US-CERT Technical Cyber Security Alert TA08-190B -- Multiple DNS implementations vulnerable to cache poisoning">describes it this way</a>:</p>
<blockquote><p>An attacker with the ability to conduct a successful cache poisoning attack can cause a nameserver's clients to contact the incorrect, and possibly malicious, hosts for particular services. Consequently, web traffic, email, and other important network data can be redirected to systems under the attacker's control.</p></blockquote>
<p>In other words, some rogue agent out on the net tries to inject bad information into a DNS cache by sending specially constructed answers to questions that the caching DNS server never asked.  That looks something like this.</p>
{{ image(
    div_float="none",
    width="500",
    caption="Sequence Diagram Showing the Effect of DNS Cache Poisoning",
    alt="Sequence Diagram Showing the Effect of DNS Cache Poisoning",
    localsrc="2008/07/dns-poison.png") }}
<p>As the US-CERT advisory points out, this is a bad thing.  Many internet services rely on the fact that when they ask to connect to a host with a specified name that they will in fact be talking to a host with that name.  You want to know that you are sending and receiving e-mail from the servers you expect and that the websites you get information from are the true, correct servers.  DNS cache poisoning effectively hides this because the address bar in the browser <em>looks</em> correct.</p>
<h2>Beyond Phishing</h2>
<p>Note that this scheme is different from the "phishing" technique.  In that technique, you might be ask to go to a URL like <code>http://badguys.crimesyndication.org/banking.yourbank.com/</code>, which would look and behave like the "banking.yourbank.com" site that you know, but it is really a website on "badguys.crimesyndication.org" that is simply made to look like your online banking site.  Careful inspection of the URL and the hints supplied by the browser about the security certificate would show that you are connecting to the wrong place.  The "DNS Poisoning" vulnerability is much worse because <em>your computer</em> was fooled into connecting to the wrong site and is passing that tomfoolery back to you.</p>
<h2>One Possible Workaround, One Possible Problem</h2>
<p>One of the possible workarounds is to configure your computer to use a DNS server that is not vulnerable to the problem of DNS cache poisoning.  One such service is called <a href="http://www.opendns.com/" title="OpenDNS homepage">OpenDNS</a>, and they made quite a big point about <a href="http://blog.opendns.com/2008/07/08/opendns-keeping-you-safe/" title="OpenDNS &ndash; Keeping you safe day after day | OpenDNS blog">not being vulnerable to this problem</a>.  At a very basic level, you use OpenDNS by <a href="https://www.opendns.com/start" title="OpenDNS Setup Instructions">setting your DNS servers</a> to 208.67.222.222 and 208.67.220.220.  Of course, they also offer <a href="http://web.archive.org/web/20080725014607/http://www.opendns.com/features/" title="OpenDNS features page">more services</a> layered on top of the basic name-to-address resolution service.</p>
<p><em>However</em>, in the course of writing this posting, I discovered that OpenDNS itself is engaging in something moderately equivalent to DNS cache poisoning itself, and it is doing it with the address of the most popular website:  www.google.com.  The problem seems to stem from issues that OpenDNS users were having with hidden software installed on Dell machines as a result of a Dell/Google agreement.  David Ulevitch, <a href="http://www.opendns.com/about/leadership/david-ulevitch-founder-and-ceo/" title="OpenDNS > About Us > David Ulevitch, Founder and CEO">Founder and CEO of OpenDNS</a>, posted about <a href="http://blog.opendns.com/2007/05/22/google-turns-the-page/" title="Google turns the page... in a bad way. | OpenDNS blog">the impact of Dell/Google's actions and OpenDNS's response</a> on the OpenDNS blog last year.</p>
<blockquote><p>About a year ago Google and Dell announced a partnership to include the Google Toolbar on new Dell computers. At the same time, Google was trying to convince the Department of Justice that changing the default search engine in the (then) new IE7 was too difficult (when in reality it&rsquo;s really simple). Installing the toolbar meant that users would have Google as their default search engine in IE7. It also meant that Dell and Google would share some of the revenue from the advertising clicks that resulted from these installations, much like The Mozilla Foundation does with its Firefox browser. ...</p>
<p>The solution to this problem was to route Google requests through a machine we run to check if the request is a typo or one of your shortcuts. If it is a typo or shortcut then we do what we always do, just fix the typo or launch your shortcut and send you off on your way. If it&rsquo;s not one of those two things, we pass it on to Google for them to give you search results. This solution provides the best of both worlds: OpenDNS users get back the features that they love and Google continues to operate without problems.</p></blockquote>
<p>This is what it looks like in a picture:</p>
{{ image(
    div_float="none",
    width="500",
    caption="Sequence Diagram Showing the OpenDNS Response to Dell/Google",
    alt="Sequence Diagram Showing the OpenDNS Response to Dell/Google",
    localsrc="2008/07/dns-opendns-google.png") }}
<p>Danny Sullivan of Search Engine Land has a more <a href="http://searchengineland.com/070523-083042.php" title="Google &amp; Dell&#039;s Revenue-Generating URL Error Pages Drawing Fire">in-depth analysis of Google's and Dell's actions</a>.  David offers a defense of OpenDNS's response in a comments on <a href="http://yro.slashdot.org/article.pl?sid=07/05/24/0342246" title="OpenDNS Says Google-Dell Browser Tool is Spyware | Slashdot">a post to Slashdot</a> (<a href="http://slashdot.org/comments.pl?sid=235955&amp;cid=19251937" title="Comments on OpenDNS Says Google-Dell Browser Tool is Spyware">this is the sharpest and most poignant</a>).  If offering OpenDNS as a fix for DNS cache poisoning is two steps forward, then OpenDNS's response to the Dell/Google action is, at best, one step back.  I would prefer that Dell not automatically install functionality like this on my PC.  I would also strongly prefer that DNS resolvers not try to be too cute.  Fortunately, it is <a href="http://blowery.org/2008/04/08/opendns-is-proxying-google/" title="OpenDNS is proxying Google?">possible to turn off this behavior in OpenDNS</a>, which I prefer to do.  But, all told, this is just one more lesson about how important the Domain Name Services is to the fundamental operation of the internet, and how easy it is to take for granted.</p>
<h2>Updates</h2>
<p><b>18-Jul-2008</b>:  I exchanged e-mail with David Ulevitch, Founder and CEO of OpenDNS, that focused on the latter part this posting.  He noted that "everything in our service, including the Google proxy, is an option that can be enabled or disabled in a (free, of course) user account."  I implied that by linking to <a href="http://blowery.org/2008/04/08/opendns-is-proxying-google/" title="OpenDNS is proxying Google?">Ben Lowery's posting</a> with instructions on "flipping the 'Enable OpenDNS proxy' toggle".  So I wanted to explicitly call that out.   David also pointed out OpenDNS is working with Google to create favorable peering arrangements at <a href="http://system.opendns.com/" title="OpenDNS &amp;gt; System (also available at http://208.67.219.60/)">their distributed sites</a>; doing so is decreasing the latency introduced by the proxy.</p>
<p>Also, there is a <a href="http://news.cnet.com/8301-10789_3-9989292-57.html?tag=bl" title="The man who changed Internet security | CNet News">C|Net news article</a> talking about how this broad, deep, and important problem was discovered and incrementally disclosed.  It is a very interesting read for those who like to know about how internet security happens.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.cartoonbank.com/item/22230 to https://www.condenaststore.com/-sp/On-the-Internet-nobody-knows-you-re-a-dog-New-Yorker-Cartoon-Prints_i8562841_.htm on November 8th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.us-cert.gov/aboutus.html to http://www.us-cert.gov/about-us on August 22nd, 2013.</p>
