---
layout: wordpress-import
status: published
published: true
title: 'Thursday Threads: Unprotected Social Media Sites, Value of Free, and Real Life Net Neutrality'
modified: 2010-10-28T19:41:20+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1813
wordpress_url: http://dltj.org/?p=1813
date: '2010-10-28 15:41:20 -0400'
date_gmt: '2010-10-28 19:41:20 -0400'
category: Thursday Threads
categories:
- Thursday Threads
tags:
- digital rights management
- ssl
- encryption
- security
- network neutrality
- Cory Doctorow
- session hijacking
- Firesheep
comments:
- id: 96347
  author: Jodi Schneider
  author_email: jodi.a.schneider@gmail.com
  author_url: http://jodischneider.com/
  date: '2010-10-28 17:19:12 -0400'
  date_gmt: '2010-10-28 21:19:12 -0400'
  content: I've always enjoyed your blog, Peter, but I enjoy it even more with the
    bite-sized content you're adding on Thursdays now. Thanks for the tips!
- id: 96485
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-10-29 09:03:48 -0400'
  date_gmt: '2010-10-29 13:03:48 -0400'
  content: Thanks, Jodi!  It has been useful for me to put the Thursday Threads posts
    together, too.  I'm finding I think about things at one level when initially posting
    them to FriendFeed and then at another level when putting together the weekly
    post.  That second level of thought has been helpful.
- id: 159982
  author: SocialMediaDigest
  author_email: ''
  author_url: http://twitter.com/socmediadigest/status/29062210599
  date: '2010-10-29 06:13:20 -0400'
  date_gmt: '2010-10-29 10:13:20 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">#RT #SM #SocialMedia Thursday Threads: Unprotected
    Social Media Sites, Value of Free ...: Receive DL... http://bit.ly/94nqbe #social
    #media</span></span>'
- id: 159983
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/29018481666
  date: '2010-10-28 19:54:52 -0400'
  date_gmt: '2010-10-28 23:54:52 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Thursday Threads: http://bit.ly/dlKhx5</span></span>'
---
<p>This week's  <a href="/category/thursday-threads/">Thursday Threads</a> looks at a big hole in the security model of most internet sites that require you to log into them with a username and password plus a pair of stories about "big media" battles.</p>
{{ thursday_threads_header() }}
<h2>Users of Non-SSL Sites are Prone to Hijacking</h2>
<blockquote><p>When logging into a website you usually start by submitting your username and password. The server then checks to see if an account matching this information exists and if so, replies back to you with a "cookie" which is used by your browser for all subsequent requests.</p>
<p>It's extremely common for websites to protect your password by encrypting the initial login, but surprisingly uncommon for websites to encrypt everything else. This leaves the cookie (and the user) vulnerable. HTTP session hijacking (sometimes called "sidejacking") is when an attacker gets a hold of a user's cookie, allowing them to do anything the user can do on a particular website. On an open wireless network, cookies are basically shouted through the air, making these attacks extremely easy.</p>
<p>{{ image(
    div_float="right",
    width="300",
    caption="Screenshot of Firesheep in action, from codebutler.com",
    alt="Firesheep exploit in action",
    localsrc="2010/10/Firesheep-exploit-in-action-300x181.png",
    ahref="http://codebutler.com/firesheep") }}
<p>This is a widely known problem that has been talked about to death, yet very popular websites continue to fail at protecting their users. The only effective fix for this problem is full end-to-end encryption, known on the web as HTTPS or SSL. Facebook is constantly rolling out new "privacy" features in an endless attempt to quell the screams of unhappy users, but what's the point when someone can just take over an account entirely? Twitter forced all third party developers to use OAuth then immediately released (and promoted) a new version of their insecure website. When it comes to user privacy, SSL is the elephant in the room.</p>
<p> Today at <a href="http://sandiego.toorcon.org/" title="ToorCon - Home">Toorcon 12</a> I announced the release of <a href="http://codebutler.github.com/firesheep/" title="Firesheep plugin distribution site">Firesheep</a>, a Firefox extension designed to demonstrate just how serious this problem is.</p>
</blockquote>
<p>Most of the <a href="http://news.google.com/news/search?pz=1&amp;cf=all&amp;ned=us&amp;hl=en&amp;as_q=firesheep&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_scoring=o&amp;btnG=Search&amp;as_qdr=a&amp;as_drrb=b&amp;as_minm=10&amp;as_mind=20&amp;as_maxm=10&amp;as_maxd=28&amp;as_nsrc=&amp;as_nloc=&amp;geo=&amp;as_author=&amp;as_occt=any" title="Google News/Blog search for 'Firesheep'">coverage</a> of <a href="http://codebutler.com/firesheep" title="Firesheep announcement">Firesheep</a> this week focused on the fact that using Facebook on an open wi-fi network in a coffee shop makes you prone to having your account broken into.  That is true, and perhaps most the most common scenario, but the problem goes deeper than that.  This can occur at any point where a third-party can intercept the communication between your browser and the web server:  your home wireless router, your internet service provider, or even some types of local area networks.  The real answer is to have the entire session -- from the point when you log in to when you log out -- encrypted.  Google recently made this the <a href="http://gmailblog.blogspot.com/2010/01/default-https-access-for-gmail.html" title="Default https access for Gmail - Official Gmail Blog">default for GMail sessions</a>, and some of the engineers involved in the effort <a href="http://www.imperialviolet.org/2010/06/25/overclocking-ssl.html" title="Overclocking SSL - ImperialViolet">published findings about how the SSL encryption overhead isn't that bad</a>.  In the meantime, Network World has some options to consider to <a href="http://www.networkworld.com/news/2010/102610-how-to-protect-against-firesheep.html" title="How to protect against Firesheep attacks  | Network World">protect yourself a little bit</a> from this kind of attack. (Hat tip to Dan Scott on Code4Lib IRC.)</p>
<h2>Cory Doctorow on the Role of "Free"</h2>
<blockquote><p>The topic I leave my family and my desk to talk to people all over the world about is the risks to freedom arising from the failure of copyright giants to adapt to a world where it's impossible to prevent copying. Because it <em>is</em> impossible. Despite 15 long years of the copyright wars, despite draconian laws and savage penalties, despite secret treaties and widespread censorship, despite millions spent on ill-advised copy-prevention tools, more copying takes place today than ever before.</p>
<p>As <a href="http://www.guardian.co.uk/technology/2007/sep/18/informationeconomy" title="I've written here before">I've written here before</a>, copying isn't going to get harder, ever. Hard drives won't magically get bulkier but hold fewer bits and cost more.</p>
<p>Networks won't be harder to use. PCs won't be slower. People won't stop learning to type "Toy Story 3 bittorrent" into Google. Anyone who claims otherwise is selling something &ndash; generally some kind of unworkable magic anti-copying beans that they swear, this time, will really work.</p>
</blockquote>
<p>Cory writes <a href="http://www.guardian.co.uk/technology/blog/2010/oct/05/free-online-content-cory-doctorow" title="The real cost of free | Cory Doctorow | Guardian technology blog">this piece in the U.K. Guardian</a> in response to a column from a fellow Guardian writer on how creative people can control their own intellectual property and some media companies' demands for digital rights management are actually stifling creativity.  It starts as a rant and moves quickly into a powerful summary of what is at stake in the "copyright wars."  (Hat tip to <a href="http://www.oclc.org/research/publications/newsletters/abovethefold/default.htm" title="Above the Fold">OCLC's Above the Fold</a>.)</p>
<h2>What Network Neutrality Really Means</h2>
<blockquote><p>In its continuing contract showdown with <a href="http://topics.nytimes.com/top/news/business/companies/cablevision_systems_corporation/index.html" title="More information about Cablevision Systems Corp">Cablevision</a>, the <a href="http://topics.nytimes.com/top/news/business/companies/news_corporation/index.html" title="More information about News Corporation">News Corporation</a> tried to extend its blackout of the Fox Broadcasting network to Fox.com and to Hulu, the popular Web site for free TV viewing, on Saturday. Angry Cablevision customers reported being unable to watch episodes of &ldquo;Glee&rdquo; and &ldquo;House&rdquo; on Hulu.        </p>
<p>The blackout caused shock waves because it had not been done before by a programmer. Though the shutdown was brief, the message was unmistakable: do not expect to be able to watch Fox online unless you are paying for Fox on TV.        </p>
<p>The attempted Web blockade was leverage for Fox in its contract negotiations, but more important, it was the latest evidence that entrenched media companies hope to replicate their walled gardens in a new medium, the Internet.</p>
</blockquote>
<p>Broadcast and cable companies in the New York City area are locked in a dispute over what the latter needs to pay the former for the right to retransmit the content on cable TV.  The dispute <a href="http://www.nytimes.com/2010/10/20/business/media/20hulu.html" title="Internet Is a Weapon in Cable Fight | New York Times">spilled over into the internet</a> when the cable company started blocking internet subscribers from reaching the broadcast company's shows on its website and on Hulu.  This could be seen as a litmus test for <a href="http://en.wikipedia.org/wiki/Network_neutrality" title="Network Neutrality | Wikipedia">net neutrality</a>:  should an internet service provider be able to decide what content it sends to end-users -- either by giving preferential treatment to some content or by blocking other content?  The dispute, by the way, continues...even <a href="http://www.nytimes.com/2010/10/27/sports/baseball/27sandomir.html" title="Rabbit Ears Redux | New York Times">impacting those who want to watch baseball's World Series</a>.</p>
