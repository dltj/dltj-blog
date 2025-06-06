---
layout: wordpress-import
status: published
published: true
title: 'IPv4 Address Space Disappearing, Here Comes IPv6'
modified: 2011-02-13T02:13:11+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 2546
wordpress_url: http://dltj.org/?p=2546
date: '2011-02-12 21:13:11 -0500'
date_gmt: '2011-02-13 02:13:11 -0500'
category: Raw Technology
categories:
- Raw Technology
tags:
- internet
- networking
- ipv6
- Vint Cerf
- ipv4
comments:
- id: 124443
  author: Bookmarks for February 10th through March 3rd | DarkRepository
  author_email: ''
  author_url: http://darkrepository.net/?p=78
  date: '2011-03-03 17:22:58 -0500'
  date_gmt: '2011-03-03 22:22:58 -0500'
  content: "[...] IPv4 Address Space Disappearing, Here Comes IPv6 &#8211; [...]"
- id: 160084
  author: b0rn2frag
  author_email: ''
  author_url: http://twitter.com/b0rn2frag/status/36716329067089920
  date: '2011-02-13 09:20:29 -0500'
  date_gmt: '2011-02-13 14:20:29 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">IPv4 Address Space Disappearing, Here Comes IPv6
    | Disruptive ...: There are various tricks tha... http://bit.ly/gRBpO0 #ipv4exhaustion</span></span>'
- id: 160085
  author: b0rn2frag
  author_email: ''
  author_url: http://twitter.com/b0rn2frag/status/36716270971785217
  date: '2011-02-13 09:20:15 -0500'
  date_gmt: '2011-02-13 14:20:15 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">IPv4 Address Space Disappearing, Here Comes IPv6
    | Disruptive ...: There are various tricks that... http://bit.ly/hNTgIa #ipv4exhaustion</span></span>'
- id: 160086
  author: sharliethomas
  author_email: ''
  author_url: http://twitter.com/sharliethomas/status/36665966871969792
  date: '2011-02-13 06:00:22 -0500'
  date_gmt: '2011-02-13 11:00:22 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">IPv4 Address Space Disappearing, Here Comes IPv6
    | Disruptive ...: Modering operating systems have support for I... http://bit.ly/eSXLTJ</span></span>'
- id: 160087
  author: Library Feed
  author_email: ''
  author_url: http://twitter.com/libraryfeed/status/36614802566553600
  date: '2011-02-13 02:37:03 -0500'
  date_gmt: '2011-02-13 07:37:03 -0500'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">IPv4 Address Space Disappearing, Here Comes IPv6
    http://bit.ly/dUXiHg</span></span>
- id: 160088
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/36610404234821632
  date: '2011-02-13 02:19:35 -0500'
  date_gmt: '2011-02-13 07:19:35 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: IPv4 Address Space Disappearing,
    Here Comes IPv6 http://bit.ly/geqRRk</span></span>'
---
<p>Last week in <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym> Thursday Threads</i> I posted an entry about <a href="/article/thursday-threads-2011w5/#p2525-ipv4-addresses">running out of IP addresses</a>.  Since I posted that, I've run across a couple of other stories and websites that bring a little more context to the consequences of last week's distribution of the last blocks of IP addresses from the world-wide pool of available addresses.  The short version: channel any panic you might be feeling into making sure your systems are ready to communicate using both the existing network standard (IPv4) and the new network standard (IPv6).</p>
<h2 id="p2546-ifaq">The Imagined Frequently Asked Questions</h2>
<p>I haven't actually been asked questions about this, so these are the Questions that I Imagine are Frequently Asked.<br />
{{ captioned(
    div_float="right",
    width="300",
    caption="What is IPv6? (6 minutes)",
    contents='<iframe title="YouTube video player" width="300" height="199" src="http://www.youtube.com/embed/2wa7y3W2DI0" frameborder="0" allowfullscreen></iframe>') }}</p>
<h3 id="p2546-stop-working">Will the internet stop working?</h3>
<p>It is highly unlikely that the internet will stop working.  There are various tricks that can be used to maximize the usage of the IPv4 addresses.  (Massive deployment of Network Address Translation, or NAT, for one.)  And the deployment of IPv6 is going to happen gradually over time and space.  ((Adapted from the SANS Internet Storm Center entry <a href="http://isc.sans.edu/diary.html?storyid=10342" title="The End Of IP As We Know It | SANS Internet Storm Center">The End Of IP As We Know It</a>.  Check it out for more techie questions and answers.))</p>
<p>There will not be a so-called "flag day" when everyone's computers switch from IPv4 to IPv6.  (There wasn't the last time the internet went through a similar upheaval in the 1980s -- see the "<a href="#p2546-history">History</a>" section below.)  IPv6 will coexist with IPv4 for probably most of this decade, based on what I'm reading, as computers at the edges will communicate over both IPv4 and IPv6.  Some <a href="http://www.tcpipguide.com/free/t_DNSChangesToSupportIPVersion6.htm" title="http://www.tcpipguide.com/free/t_DNSChangesToSupportIPVersion6.htm">magic in the Domain Name Service (DNS)</a> will enable this to happen.  There will come a day, though, when IPv4 addresses are truly exhausted and new services will only be reachable via IPv6.  Whether we get there before IPv6 is widely deployed is a topic of much debate.</p>
<h3 id="p2546-ready">Am I ready now?</h3>
<p>Maybe, but probably not.  There is a website that tests <a href="http://test-ipv6.com/" title="Test your IPv6">IPv6 connectivity</a>.  This website gives to general responses -- can your computer access resources that are offered on both IPv4 and IPv6, and can your computer access resources that are only offered on IPv6.</p>
<p>The Internet Society is calling for a <a href="http://isoc.org/wp/worldipv6day/" title="World IPv6 Day | Internet Society">World IPv6 Day</a> on June 8, 2011. "<a href="http://googleblog.blogspot.com/2011/01/world-ipv6-day-firing-up-engines-on-new.html" title="World IPv6 Day: firing up the engines on the new Internet protocol | Official Google Blog">Google</a>, <a href="http://www.facebook.com/notes/facebook-engineering/world-ipv6-day-solving-the-ip-address-chicken-and-egg-challenge/484445583919" title="World IPv6 Day: Solving the IP Address Chicken-and-Egg Challenge | Facebook">Facebook</a>, <a href="http://www.yahoo.com" title="Yahoo!">Yahoo!</a>, <a href="http://www.akamai.com/ipv6" title="IPv6 | Akamai">Akamai</a> and <a href="http://web.archive.org/web/20110212000000/http://blog.llnw.com/2011/01/ready-to-celebrate-world-ipv6-day-we-are/" title="Ready to Celebrate World IPv6 Day? We Are. | In the Limelight">Limelight Networks</a> will be amongst some of the <a href="http://web.archive.org/web/20110212000000/http://isoc.org:80/wp/worldipv6day/participants/" title="World IPv6 Day participants | Internet Society">major organisations</a> that will offer their content over IPv6 for a 24-hour 'test flight'. The goal of the Test Flight Day is to motivate organizations across the industry &ndash; Internet service providers, hardware makers, operating system vendors and web companies &ndash; to prepare their services for IPv6 to ensure a successful transition as IPv4 addresses run out."</p>
<h3 id="p2546-networks">I manage networks.  Should I care?</h3>
<p>Dude!  This is all about you.  It is your chance to get new network gear that will support IPv6!</p>
<p>Okay, that probably won't happen.  Your gear either supports IPv6 addressing and routing (perhaps with a software upgrade), or as you phase in new gear it will support IPv6.  You do have a lot of work ahead of you, though, to get your network ready.  The <a href="http://www.ipv6actnow.org/info/how-to/" title="How To Act Now | IPv6 Act Now">IPv6 Act Now</a> has suggestions and links.</p>
<h3 id="p2546-hardware">I manage hardware.  Should I care?</h3>
<p>Modern operating systems have support for IPv6 as part of the operating system, and you won't need new hardware (unless you also manage the network, see above).  You'll also need to work with the folks that make you software (see below) to coordinate the transition.  DSLreports.com has <a href="http://www.dslreports.com/faq/ipvsix" title="IPv6 FAQ | DSLReports.com, ISP Information">information about enabling IPv6 for various operating systems</a>.</p>
<h3 id="p2546-software">I write software.  Should I care?</h3>
<p>Remember the year-2000 problem?  Did you scoff at the short-sightedness of those older developers for only using two digits to represent the year?  You are about to get your due.  The move to IPv6 means a change to the size of IP addresses from 48-bits to 128-bits.  Code that is storing, comparing, or outputting addresses is going to have to be reviewed and probably changed to handle <em>both</em> IPv4 and IPv6 addresses.  Hurricane Electric has some <a href="http://web.archive.org/web/20110212000000/http://owend.corp.he.net:80/ipv6/" title="IPv6 Porting Information">information on porting code to IPv6</a>.</p>
<h3 id="p2546-help">How can I help?</h3>
<p>Reddit notes that "There has been no strong business case for the cost of moving to IPv6, as up until now there have been enough IP addresses available", and it also answers the question <a href="http://web.archive.org/web/20130120172543/http://code.reddit.com/wiki/help/faqs/ipv6" title="Reddit IPv6 FAQ">How can I help the adoption of IPv6?</a>.</p>
<h2 id="p2546-history">Bits of History</h2>
<p>The last time the internet faced a major restructuring like this was when IPv4 replace the ARPANET Network Control Protocol (NCP).  In November 1981, Jon Postel published <a href="http://tools.ietf.org/html/rfc801" title="RFC 801 - NCP/TCP transition plan">RFC 801 on the transition plan from NCP to TCP</a>.  In the introduction to that document, Dr. Postel wrote:</p>
<blockquote><p>ARPA sponsored research on computer networks led to the development of the ARPANET.  The installation of the ARPANET began in September 1969, and regular operational use was underway by 1971.  The ARPANET has been an operational service for at least 10 years.  Even while it has provided a reliable service in support of a variety of computer research activities, it has itself been a subject of continuing research, and has evolved significantly during that time.</p>
<p>In the past several years ARPA has sponsored additional research on computer networks, principally networks based on different underlying communication techniques, in particular, digital packet broadcast radio and satellite networks.  Also, in the ARPA community there has been significant work on local networks.</p>
<p>It was clear from the start of this research on other networks that the base host-to-host protocol used in the ARPANET was inadequate for use in these networks.  In 1973 work was initiated on a host-to-host protocol for use across all these networks.  The result of this long effort is the Internet Protocol (IP) and the Transmission Control Protocol (TCP).</p>
<p>These protocols allow all hosts in the interconnected set of these networks to share a common interprocess communication environment. The collection of interconnected networks is called the ARPA Internet (sometimes called the "Catenet").</p>
<p>The Department of Defense has recently adopted the internet concept and the IP and TCP protocols in particular as DoD wide standards for all DoD packet networks, and will be transitioning to this architecture over the next several years.  All new DoD packet networks will be using these protocols exclusively.</p>
<p>The time has come to put these protocols into use in the operational ARPANET, and extend the logical connectivity of the ARPANET hosts to include hosts in other networks participating in the ARPA Internet.</p>
<p>As with all new systems, there will be some aspects which are not as robust and efficient as we would like (just as with the initial ARPANET).  But with your help, these problems can be solved and we can move into an environment with significantly broader communication services.</p></blockquote>
<p>The transition plan for NCP to TCP called for roughly a year-long process in 1982 to transition hosts from one network stack to the other.  There were gateways between the two networks during that time.  In January 1983 all the gateways between the NCP-based hosts and the IP-based hosts were turned off.</p>
<p>Vint Cerf, one of the parents of what we call the "Internet", reflected on IPv4 addressing at the <a href="http://www.youtube.com/watch?v=mZo69JQoLb8" title="YouTube - Google IPv6 Conference 2008:  What will the IPv6 Internet look like?">2008 IPv6 conference</a>.  A <a href="/article/vint-cerf-ip-addressing/"><i><acronym title="Vint Cerf on the Origins of 32-bit IP Addressing | Disruptive Library Technology Jester">DLTJ</acronym></i> post from 2008 has a transcript</a> of Dr. Cerf's comments.</p>
