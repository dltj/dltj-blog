---
layout: wordpress-import
status: published
published: true
title: 'Thursday Threads: Payment Card Security, Crap Detection, VoIP in your Hand'
modified: 2014-08-14T10:56:09+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 19098
wordpress_url: http://dltj.org/?p=19098
date: '2014-08-14 06:56:09 -0400'
date_gmt: '2014-08-14 10:56:09 -0400'
category: Thursday Threads
categories:
- Thursday Threads
tags:
- VoIP
- security
- mobile
- information literacy
- EMV
- Payment card
comments: []
---

<p>Welcome to the revival of <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym> Thursday Threads</i>.  With the summer over and the feeling of renewal towards this blog and its topics, I'm happy to be back sharing tidbits of technology that I hope you will find interesting.  Today's set of threads covers the <a href="#p19098-emv-hacking">gnarly security issues</a> behind the bright-and-shiny chip-on-payment card systems being rolled out by banks and retailers in the U.S., a <a href="#p19098-crap-detection">list of resources</a> for checking things that you read about online, and a heads-up on <a href="#p19098-cellphone-voip">changes to how your phone will work</a> in the near future.</p>
{{ thursday_threads_header() }}
<h2 id="p19098-emv-hacking">That Chip in your Credit Card May Not Be as Secure as Your Bank Hopes</h2>
<blockquote><p>According to new research, chip-based &ldquo;Smartcard&rdquo; credit and debit cards&mdash;the next-generation replacement for magnetic stripe cards&mdash;are vulnerable to unanticipated hacks and financial fraud. Stricter security measures are needed, the researchers say, as well as increased awareness of changing terms-of-service that could make consumers bear more of the financial brunt for their hacked cards.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://www.computerworld.com/s/article/9250275/Update_Payment_cards_with_chips_aren_39_t_perfect_so_encrypt_everything_experts_say" title="Black Hat 2014: A New Smartcard Hack | IEEE Spectrum">Black Hat 2014: A New Smartcard Hack</a>, by Mark Anderson, IEEE Spectrum, August 7, 2014</cite></div>
</blockquote>
<blockquote><p>Although U.S. banks are issuing EMV cards now, it will be some time before they start to see a reduction in fraud.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://www.cl.cam.ac.uk/~sjm217/papers/cacm14emv.pdf" title="EMV: Why Payment Systems Fail | Communications of the ACM">EMV: Why Payment Systems Fail [postprint, pdf]</a> by Ross Anderson and Steven J. Murdoch, Communications of the ACM, June 2014</cite></div>
</blockquote>
<p>The first quote comes from an article that covers a <a href="https://www.blackhat.com/us-14/briefings.html#how-smartcard-payment-systems-fail">presentation</a> made at this year's Black Hat security conference in Las Vegas.  The presenter at Black Hat is also a co-author of the Communications article.  The first article gives an overview of some of the problems with the EMV system (an acronym for "Europay-Mastercard-Visa" -- the three companies promoting the chip-on-payment-card system).  For the real gory details, read the second article.</p>
<p>The bottom line is this, though -- payment cards with chips are coming to U.S.  The big Target data breach from last year only accelerated plans already in place to bring this technology to U.S. consumers.  Banks may try to say that you, the consumer, are responsible for any charges made with your card and your PIN because this whole system has been set up to make sure only someone with the card and the PIN could have authorized the charge.  As with many things dealing with computer security, reality is not quite so clear cut, so I recommend keeping an eye on this topic as the EMV system rolls out in the U.S.</p>
<h2 id="p19098-crap-detection">A Recourse for Information Literacy</h2>
<blockquote><p>This document is a resource for assessing the accuracy or veracity of online information, organized under a number of headings. The objective of the resource is to improve the digital lives of individuals and to improve the quality of the online commons by increasing the number of people who know how to separate good info from bad info. It began as a chapter for my 2012 book, <a href="http://rheingold.com/books/net-smart/" title="Net Smart | Howard Rheingold">Net Smart: How to Thrive Online</a>.
<div style="text-align: right; width: 100%;"><cite>- <a href="https://docs.google.com/document/d/163G79vq-mFWjIqMb9AzYGbr5Y8YMGcpbSzJRutO8tpw/edit">A Guide to Crap Detection Resources</a>, by Howard Rheingold</cite></div>
</blockquote>
<p>This one crossed my Twitter stream as a retweet from someone else.  Author Howard Rheingold has put together a list of places to go to, well, exercise your crap detection skills.  With headings for "Political" and "Urban Legends, Hoaxes, and Emails" and "Journalism", it is a resource that you may want to keep close-at-hand for checking into those things that sound too good to be true.  The author also takes comments from others in the document, so it is a living document of contributions from others.</p>
<h2 id="p19098-cellphone-voip">The Subsumption of Voice into IP Networks Continues</h2>
<blockquote><p>What in fact is really going on...is that this is the iceberg tip of a massive paradigm shift away from analog calling, at every level across the board. It&rsquo;s not just a shift from PSTN, or Public Switched Telephone Network, in favor of IP-based calling, either. PSTN is the old-school wireline circuit that uses copper wires for analog voice. Half of residential U.S. wireline service is VoIP, according to a <a href="http://transition.fcc.gov/Daily_Releases/Daily_Business/2014/db0625/DOC-327830A1.pdf" target="new" title="http://transition.fcc.gov/Daily_Releases/Daily_Business/2014/db0625/DOC-327830A1.pdf">recent FCC report.</a>But all calling, including mobile, is going IP.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://www.networkworld.com/article/2459515/voip/how-cellphone-calling-is-going-all-internet.html" title="How cellphone calling is going all Internet | Network World">How cellphone calling is going all Internet</a>, by <a href="http://www.networkworld.com/author/Patrick-Nelson/" title="Articles by Patrick Nelson | Network World">Patrick Nelson</a>, Network World, August 1, 2014</cite></div>
</blockquote>
<p>Sure, we have Skype and FaceTime and some have VoIP (Voice-over-IP) phones on our desks.  But the world just now getting to the point where VoIP is <em>the</em> way voice calls are made.  In this opinion piece, the author outlines the many ways that voice calls are switching from circuit-switched to packet-switched right down to the devices we hold in our hands.  (On medium- and long-haul phone circuits, that changeover happened long ago.)  If done the right way, you won't notice the change -- except that your calls may be <a href="http://www.wired.com/2013/04/how-hd-voice-works-to-make-your-calls-clearer/" title="How HD Voice Works to Make Your Calls Sound Drastically Better | WIRED Gadget Lab">clearer and higher quality</a>.</p>
