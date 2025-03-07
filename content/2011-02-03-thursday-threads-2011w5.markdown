---
layout: wordpress-import
status: published
published: true
title: 'Thursday Threads: So-called "Internet Kill-switch", IP address exhaustion, demographics of P2P piracy'
modified: 2011-02-03T11:53:01+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 2525
wordpress_url: http://dltj.org/?p=2525
date: '2011-02-03 06:53:01 -0500'
date_gmt: '2011-02-03 11:53:01 -0500'
category: Thursday Threads
categories:
- Thursday Threads
tags:
- networking
- legislation
- ipv6
- piracy
- kill switch
- Senate Bill 191 (112th Congress)
- ipv4
- Peer-to-Peer Networks
- BitTorrent
comments:
- id: 160179
  author: Library Feed
  author_email: ''
  author_url: http://twitter.com/libraryfeed/status/33135468023382016
  date: '2011-02-03 12:11:25 -0500'
  date_gmt: '2011-02-03 17:11:25 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Thursday Threads: So-called &ldquo;Internet Kill-switch&rdquo;,
    IP address exhaustion, demographics of P2P piracy http://bit.ly/hJ0hIS</span></span>'
---

<p>This week of <i><a href="/category/thursday-threads/"><acronym title="Disruptive Library Technology Jester">DLTJ</acronym> Thursday Threads</a></i> covers a wide range of topics.  First, from a public policy perspective, is news that the U.S. Senate has a bill proposing the <a href="#p2525-inet-kill-switch">study of an internet "kill-switch"</a> that some are speculating could behave like what happened in Egypt last week.  Next, from a technical perspective, is the fact that we're <a href="#p2525-ipv4-addresses">running out of IP addresses</a>, which is going to make some engineers' lives pretty messy before it is ultimately fixed.  Lastly, from a research perspective, is a paper that characterizes the <a href="#p2525-p2p-piracy">demographics of users using peer-to-peer for piracy</a>.</p>
<p>Continuing last week's sidenote, I think I have found the fundamental problem of why Thursday Threads hasn't been coming out via e-mail on, well, Thursday.  Although the <a href="http://wordpress.org/support/topic/w3-total-cache-prevents-rss-updating" title="WordPress &amp;#8250; Support &amp;raquo; W3 Total Cache Prevents RSS Updating">underlying issue</a> still remains, a workaround has been put in place that will hopefully eliminate the symptomps.</p>
<h2 id="p2525-inet-kill-switch">Internet &lsquo;Kill Switch&rsquo; Legislation Back in Play</h2>
<div class="alignright"><script type="text/javascript"><br />
oc_host_url = "http://www.opencongress.org/";<br />
oc_bill_id = "112-s191";<br />
oc_frame_height = "231";<br />
oc_bgcolor = "ffffff";<br />
oc_textcolor = "333333";<br />
oc_bordercolor = "999999";<br />
</script><br />
<script type="text/javascript" src="http://www.opencongress.org/javascripts/widgets/bill_status.js"></script></div>
<blockquote><p>Legislation granting the president internet-killing powers is to be re-introduced soon to a Senate committee, the proposal&rsquo;s chief sponsor told Wired.com on Friday.</p>
<p>The resurgence of the so-called &ldquo;kill switch&rdquo; legislation came the same day Egyptians <a href="http://www.wired.com/dangerroom/2011/01/egypts-internet-shutdown-cant-stop-mass-protests/" title="Egypt&#8217;s Internet Shutdown Can&#8217;t Stop Mass Protests | Danger Room | Wired.com">faced an internet blackout</a> designed to counter massive demonstrations in that country.</p>
<p>The bill, which has bipartisan support, is being floated by Sen. Susan Collins, the Republican ranking member on the Homeland Security and Governmental Affairs Committee. The proposed legislation, which Collins said would not give the president the same power <a href="http://www.wired.com/threatlevel/2011/01/egypt-isp-shutdown/" title="Egypt Shut Down Its Net With a Series of Phone Calls | Threat Level | Wired.com">Egypt&rsquo;s Hosni Mubarak is exercising</a> to quell dissent, sailed through the Homeland Security Committee in December but expired with the new Congress weeks later.</p>
<p>The bill is designed to protect against &ldquo;significant&rdquo; cyber threats before they cause damage, Collins said.</p>
</blockquote>
<p>Wired.com has <a href="http://www.wired.com/threatlevel/2011/01/kill-switch-legislation" title="Internet &lsquo;Kill Switch&rsquo; Legislation Back in Play | Threat Level | Wired.com">this article</a> about <a href="http://hdl.loc.gov/loc.uscongress/legislation.112s191" title="Bill Summary &amp; Status | 112th Congress (2011 - 2012) | S.191 | THOMAS (Library of Congress)">proposed legislation</a> to "direct the Department of Homeland Security to undertake a study on emergency communications" (the bill's title).   The text of the legislation is not available at this time, but when a similar topic was debated in the <a href="http://hdl.loc.gov/loc.uscongress/legislation.111s3480" title="Bill Summary &amp; Status | 111th Congress (2009 - 2010) | S.3480 | THOMAS (Library of Congress"">last congressional session</a>, the United States Senate Committee on Homeland Security and Governmental Affairs -- chaired by Senator Joseph I. Lieberman with Senator Susan M. Collins as ranking minority member -- issued a four-page <a href="/assets/images/2011/02/111-s3480-Myth-v-Reality.pdf" title="Myth vs. Reality, The Facts About S. 3480, &#039;Protecting Cyberspace as a National Asset Act of 2010&#039;">Myth-v-Reality document</a> [PDF].  That bill also seemed to do more than simply request a study -- it actually established in the Executive Office of the President an Office of Cyberspace Policy.  The bill died before coming up for a vote in the final days of the session.  At the time, the American Library Association joined with dozens of other groups to <a href="http://www.cdt.org/files/pdfs/20100624_joint_cybersec_letter.pdf" title="Civil Liberties Issues in Cybersecurity Bill">send a letter</a> [PDF] to the committee expression concerns with that version. </p>
<p>There is some really wacky stuff going on here.  For instance, the Wired.com article reports on an aide to the Homeland Security committee gave an example when the limited power given to the President would be used:  "An example, the aide said, would require infrastructure connected to 'the system that controls the floodgates to the Hoover dam' to cut its connection to the net if the government detected an imminent cyber attack."  This, of course, begs the question of "Is the system that controls the floodgates of the Hoover Dam connected to the public internet?" followed closely by "If so, why?"  I think this one is going to be worth following to see what happens.</p>
<h2 id="p2525-ipv4-addresses">No more IPv4 addresses</h2>
<blockquote><p>The Internet has run out of IPv4 address space.</p>
<p>The Internet Assigned Numbers Authority (<a href="http://www.iana.org/" title="IANA &mdash; Internet Assigned Numbers Authority">IANA</a>) assigned two of the remaining blocks of IPv4 addresses - each containing 16.7 million addresses - to the Asia Pacific Network Information Centre (<a href="http://www.apnic.net/" title="APNIC - Home">APNIC</a>) on  Tuesday, as predicted.</p>
<p>This action sparks an immediate distribution of the remaining five blocks of IPv4 address space, with one block going to each of the five Regional Internet Registries (RIR).</p>
</blockquote>
<p>Internet Protocol (or "IP") addresses are the unique identifiers that direct traffic from one computer on the network to another.  When the experiment that we now know as the Internet was created -- known as IP version 4 or "IPv4" -- the number of possible unique addresses was set as 4,294,967,296 ((Okay, when one takes out the reserved private addresses and the multicast addresses, the number is somewhere around 4,006,000,000, but who is counting?)).  It was thought that such a number would be sufficient for experimental purposes.  The internet, of course, has taken on a life of its own, and with the assignment of unique addresses to home computers and cell phones, it was only a matter of time before we ran out.</p>
<p>Well, as stated in the <a href="http://www.networkworld.com/news/2011/020111-ipv4-apnic.html" title="No more IPv4 addresses | Network World">article from Network World</a> where the above quote came from, that time is quickly coming.  The very top layer of the IP address bureaucracy assigns addresses in blocks of about 16.8 million to five regional registries that correspond to roughly continental boundaries.  Those registries then assign smaller blocks to various internet services providers to use.  How long it takes for each regional registry to run out of addresses varies from months to years, but with the exhaustion of the top-level registry the internet engineers know that we have reached the first milestone on that path.</p>
<p>There are various techniques that can be used to stretch the number of addresses, but the end-game is going to be the adoption of IP version 6.  IPv6 will give us 340,282,366,920,938,463,463,374,607,431,768,211,456 unique addresses.  That's 340 undecillion, 282 decillion, 366 nonillion, 920 octillion, 938 septillion, 463 sextillion, 463 quintillion, 374 quadrillion, 607 trillion, 431 billion, 768 million, 211 thousand and 456 addresses.  Think that will be enough?</p>
<h2 id="p2525-p2p-piracy">A research study identifies who uploads the majority of the content to the P2P piracy networks</h2>
<blockquote><p>Users who publish contents on BitTorrent dedicate a large part of their own resources (bandwidth, storage capacity) and assume the risks involved in publishing contents that are protected by copyright laws. So, is this altruistic behavior or is there some type of economic incentive at work? "The success of BitTorrent is due to the fact that a few users make a large number of contents available in exchange for receiving economic benefits&rdquo;, explain the authors of a study carried out by the Telematic Engineering Department of the UC3M, Professors Rub&eacute;n Cuevas, Carmen Guerrero and &Aacute;ngel Cuevas. Their analysis demonstrates that a small group of users of these applications (around one hundred) is responsible for 66 percent of the content that is published and 75 percent of the downloads. In other words: the great success of a massively used application like BitTorrent depends on a few users.</p></blockquote>
<p>This quote comes from a <a href="http://www.uc3m.es/portal/page/portal/actualidad_cientifica/noticias/P2P_network" title="A research study identifies who uploads the majority of the content to the P2P piracy networks">summary</a> of a <a href="http://arxiv.org/abs/1007.2327" title="Is Content Publishing in BitTorrent Altruistic or Profit-Driven | arXiv">research study</a> presented at <a href="http://conferences.sigcomm.org/co-next/2010/" title="CoNext 2010 - Welcome - ACM SIGCOMM">6th International Conference on emerging Networking EXperiments and Technologies (CoNEXT)</a> late last year.  It would seem to suggest that if one wanted to shut down piracy on peer-to-peer (P2P) file sharing networks such as BitTorrent that it would only take convincing or eliminating "a few users" to make it happen.  That this hasn't happened perhaps points to the difficulty in locating and stopping those users, but still I thought this made for an interesting read none the less.  [Via <a href="http://technews.acm.org/" title="ACM TechNews">ACM TechNews</a> from <a href="http://technews.acm.org/archives.cfm?fo=2011-01-jan/jan-26-2011.html#503594" title="ACM TechNews for January 26, 2011">January 26, 2011</a>]</p>
