---
layout: wordpress-import
status: published
published: true
title: 'Note to Future Self:  Use `ssh -D` to bypass annoying interception proxies'
modified: 2008-02-18T22:12:56+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 329
wordpress_url: https://dltj.org/article/ssh-as-socks-proxy/
date: '2008-02-18 17:12:56 -0500'
date_gmt: '2008-02-18 22:12:56 -0500'
category: Disruption in Libraries
categories:
- Disruption in Libraries
tags:
- proxy
- networking
- system administration
- openssh
comments:
- id: 31364
  author: PALINET Tech Update - PLN
  author_email: ''
  author_url: ''
  date: '2008-02-22 13:32:49 -0500'
  date_gmt: '2008-02-22 18:32:49 -0500'
  content: "<!--%kramer-ref-pre%-->[...] Selected technology-related posts from a
    variety of library blogs DVD Wars Over 18 February 2008  Note to Future Self:
    Use `ssh -D` to bypass annoying interception ... 18 February 2008  A new partnership
    for OpenTranslators 18 February 2008  U.S. eBook sales up 23.6% [...]<!--%kramer-ref-post%-->"
- id: 33464
  author: SonicWALL still hates us - Hack a Day
  author_email: ''
  author_url: http://www.hackaday.com/2008/06/18/sonicwall-still-hates-us/
  date: '2008-06-18 21:25:05 -0400'
  date_gmt: '2008-06-19 01:25:05 -0400'
  content: <!--%kramer-ref-pre%-->[...] any trouble viewing Hack a Day from your school/work?
    What "service" are they using? We use ssh's application level dynamic port forwarding
    to get around most systems when we're on the road.PermalinkEmail thisLinking BlogsComments
    [...]<!--%kramer-ref-post%-->
- id: 33471
  author: tonsofpcs
  author_email: eric.adler@videoproductionsupport.com
  author_url: ''
  date: '2008-06-19 16:11:05 -0400'
  date_gmt: '2008-06-19 20:11:05 -0400'
  content: In Windows, you can set the forward up with PuTTY ("Dynamic Port Forwarding")
    and you can traverse the "SOCKS" proxy by settings in individual applications.
- id: 33472
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-06-19 22:10:40 -0400'
  date_gmt: '2008-06-20 02:10:40 -0400'
  content: '@tonsofpcs : Thanks for the reply.  <a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/"
    rel="nofollow">PuTTY</a> looks like a free telnet/ssh client for windows -- the
    equivalent of opening up a terminal session and running the command line ssh program
    in the directions above.  I was sort of hoping that there would be a system-wide
    SOCKS setting that could be made that well-behaving applications would use (as
    opposed to having to set the SOCKS proxy in each individual one).  Perhaps that
    isn''t the case with Windows.'
- id: 33474
  author: BlogoWogo - The Blog Network | SonicWALL still hates us
  author_email: ''
  author_url: http://www.blogowogo.com/blog_article.php?aid=1518900&amp;t=5
  date: '2008-06-20 02:30:00 -0400'
  date_gmt: '2008-06-20 06:30:00 -0400'
  content: <!--%kramer-ref-pre%-->[...] any trouble viewing Hack a Day from your school/work?
    What "service" are they using? We use ssh's application level dynamic port forwarding
    to get around most systems when we're on the road.Permalink
- id: 33475
  author: Frayed Knots
  author_email: ''
  author_url: ''
  date: '2008-06-20 03:01:53 -0400'
  date_gmt: '2008-06-20 07:01:53 -0400'
  content: <!--%kramer-ref-pre%-->[...] any trouble viewing Hack a Day from your school/work?
    What "service" are they using? We use ssh's application level dynamic port forwarding
    to get around most systems when we're on the road.Permalink&nbsp;|&nbsp;Email
    [...]<!--%kramer-ref-post%-->
- id: 33508
  author: Bookmarks 2008-06-24
  author_email: ''
  author_url: http://sebsauvage.net/favs.html
  date: '2008-06-25 06:27:21 -0400'
  date_gmt: '2008-06-25 10:27:21 -0400'
  content: "<!--%kramer-ref-pre%-->[...] (ACL) sous Linux &agrave; partir de Nautilus.
    (Tags: linux ubuntu system security opensource software) Note to Future Self:
    Use `ssh -D` to bypass annoying interception proxies | Disruptive Library Techn...
    - http://dltj.org/article/ssh-as-socks-proxy/C'est tellement simple d'utiliser
    un client ssh comme [...]<!--%kramer-ref-post%-->"
- id: 33597
  author: jon
  author_email: jon@tfftech.com
  author_url: http://www.jonmadison.com
  date: '2008-07-18 17:05:26 -0400'
  date_gmt: '2008-07-18 21:05:26 -0400'
  content: "helped me. :)\r\n\r\nssh -D + firefox plugin foxyproxy works like a charm
    here."
- id: 33614
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-07-21 21:59:44 -0400'
  date_gmt: '2008-07-22 01:59:44 -0400'
  content: I use <a href="https://addons.mozilla.org/en-US/firefox/addon/2464" rel="nofollow">FoxyProxy</a>
    as well, Jon, and agree that it makes the Firefox setup very easy. (Firefox is
    one of those Mac programs that doesn't read the standard network parameters, such
    as the SOCKS proxy, out of the operating system configuration.)
- id: 34520
  author: Casey
  author_email: casey.woods@gmail.com
  author_url: http://www.itinfusion.ca
  date: '2009-01-13 00:54:37 -0500'
  date_gmt: '2009-01-13 05:54:37 -0500'
  content: "Are you sure about the SOCKS proxy setting in the Mac network panel proxying
    *everything*?  It doesn't proxy any mozilla products, and it doesn't work on hulu
    flash video.\r\n\r\nFrom what I've read, to proxy all network traffic you have
    to run proxifier.  I haven't found anything else that is all inclusive..."
- id: 34524
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2009-01-14 22:44:23 -0500'
  date_gmt: '2009-01-15 03:44:23 -0500'
  content: "@Casey --\r\n\r\nYes, a good point.  Mozilla does not honor the proxy
    settings set by the underlying operating system; others may not as well.  Generally
    speaking, all of the Apple-supplied applications will.  Others are hit-and-miss.
    \ I also run <a href=\"http://www.obdev.at/products/littlesnitch/index.html\"
    rel=\"nofollow\">Little Snitch</a> (an application that intercepts outgoing connections
    and asks for confirmation before allowing the connection), so I can see if applications
    are not honoring the MacOS SOCKS proxy settings."
- id: 34584
  author: Consolidating Travel Details with TripIt | Disruptive Library Technology
    Jester
  author_email: ''
  author_url: http://dltj.org/article/tripit/
  date: '2009-01-26 20:04:43 -0500'
  date_gmt: '2009-01-27 01:04:43 -0500'
  content: "[...] sitting in the Denver airport (and quite pleased to have remembered
    my note to myself about tunneling through ad-laden interception proxy) with lots
    to think and blog about after this year&#8217;s Midwinter meeting. It was a very
    [...]"
- id: 34985
  author: hudson
  author_email: donkihot@gmail.com
  author_url: ''
  date: '2009-03-08 19:18:10 -0400'
  date_gmt: '2009-03-08 23:18:10 -0400'
  content: I use this <span class="removed_link" title="http://vpnomania.com/proxy-surf.html/">proxy</span>
    and  it makes the  setup very easy<p style="padding:0;margin:0;font-style:italic;"
    class="removed_link">The text was modified to remove a link to http://vpnomania.com/proxy-surf.html/
    on January 19th, 2011.</p>
- id: 38347
  author: "&raquo; SSH Tunneling Examples MaisonBisson.com"
  author_email: ''
  author_url: http://maisonbisson.com/blog/post/14142/ssh-tunneling-example/comment-page-1/
  date: '2009-10-15 19:19:23 -0400'
  date_gmt: '2009-10-15 23:19:23 -0400'
  content: "<!--%kramer-ref-pre%-->[...] forget that you can also create a SOCKS network
    tunnel via ssh as well: http://dltj.org/article/ssh-as-socks-proxy/  [...]<!--%kramer-ref-post%-->"
- id: 38525
  author: Yann Esposito - ssh to Listen 443 on Snow Leopard
  author_email: ''
  author_url: http://yannesposito.com/Scratch/en/blog/08_Configure_ssh_to_listen_the_port_443_on_Snow_Leopard/
  date: '2009-11-13 15:45:19 -0500'
  date_gmt: '2009-11-13 20:45:19 -0500'
  content: "<!--%kramer-ref-pre%-->[...] I get this information from this post. [...]<!--%kramer-ref-post%-->"
- id: 38601
  author: Sashman
  author_email: sashimanu@gmail.com
  author_url: ''
  date: '2009-11-26 17:00:17 -0500'
  date_gmt: '2009-11-26 22:00:17 -0500'
  content: That's nice when you don't have any VPN connectivity.
- id: 44490
  author: What sorts of things can I do with SSH on the iPhone? - Super User
  author_email: ''
  author_url: ''
  date: '2010-02-14 15:27:45 -0500'
  date_gmt: '2010-02-14 20:27:45 -0500'
  content: "<!--%kramer-ref-pre%-->[...] http://dltj.org/article/ssh-as-socks-proxy/
    [...]<!--%kramer-ref-post%-->"
- id: 69195
  author: Sad news &laquo; Dropbox Forums
  author_email: ''
  author_url: http://forums.dropbox.com/topic.php?page=2&amp;id=19835&amp;replies=33
  date: '2010-05-14 10:56:05 -0400'
  date_gmt: '2010-05-14 14:56:05 -0400'
  content: "<!--%kramer-ref-pre%-->[...] SSH SOCKS howto here: http://dltj.org/article/ssh-as-socks-proxy/
    \ Posted 24 minutes ago #       &laquo; Previous 1 [...]<!--%kramer-ref-post%-->"
- id: 69510
  author: Tunneling
  author_email: alex1990o@yahoo.com
  author_url: http://www.interwap.ro
  date: '2010-05-16 08:36:13 -0400'
  date_gmt: '2010-05-16 12:36:13 -0400'
  content: You can use the software from http://www.interwap.ro . They have free access
    at 384kbps and low prices for up to 50mbps high speeds.
- id: 72646
  author: nice ssh option for tunneling
  author_email: ''
  author_url: http://pascal-schwarz.ch/blog/index.php/2010/06/07/nice-ssh-option-for-tunneling/
  date: '2010-06-07 13:39:43 -0400'
  date_gmt: '2010-06-07 17:39:43 -0400'
  content: "[...] see here: http://dltj.org/article/ssh-as-socks-proxy/ [...]"
- id: 108921
  author: Linux Notes Blog, Using an ssh tunnel
  author_email: ''
  author_url: http://linuxnotes.tumblr.com/post/2441263086/using-an-ssh-tunnel
  date: '2010-12-28 22:19:33 -0500'
  date_gmt: '2010-12-29 03:19:33 -0500'
  content: "<!--%kramer-ref-pre%-->[...] Mac [...]<!--%kramer-ref-post%-->"
- id: 161297
  author: Tristan
  author_email: ''
  author_url: http://twitter.com/trisweb/status/4836598746
  date: '2009-10-13 15:00:54 -0400'
  date_gmt: '2009-10-13 19:00:54 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">ssh -D is saving my ass right now at a car dealership
    that has a web filter. http://bit.ly/HOs5Z if you have access to any ssh server!
    Sweet</span></span>
- id: 161298
  author: 流水弦歌
  author_email: ''
  author_url: http://twitter.com/xiange/status/2682391119
  date: '2009-07-17 04:00:30 -0400'
  date_gmt: '2009-07-17 08:00:30 -0400'
  content: |-
    <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span class="topsy_trackback_content">@linkinpark1106 http://bit.ly/1MLdQ
      这篇文章怎么样，我觉得 Mac 也可以用吧</span></span>
- id: 170672
  author: Enable SSH Tunneling in OpenSuse Server - webdevRefinery Forum
  author_email: ''
  author_url: http://webdevrefinery.com/forums/topic/8929-enable-ssh-tunneling-in-opensuse-server/
  date: '2011-09-19 13:00:17 -0400'
  date_gmt: '2011-09-19 17:00:17 -0400'
  content: "<!--%kramer-ref-pre%-->[...] connect, then set your browser&#039;s proxy
    server to a SOCKS proxy of localhost port 9999.  Edit: http://dltj.org/arti...as-socks-proxy/
    explains it a bit better. Uses port 9050, but it&#039;s the exact same thing (you
    can choose [...]<!--%kramer-ref-post%-->"
- id: 212028
  author: A very inexpensive way to get access to BBC iplayer from France - SURVIVE
    FRANCE NETWORK
  author_email: ''
  author_url: http://www.survivefrance.com/group/computercorner/forum/topics/a-very-inexpensive-way-to-get?commentId=3339392%3AComment%3A81839&amp;groupId=3339392%3AGroup%3A6295
  date: '2012-01-23 11:53:36 -0500'
  date_gmt: '2012-01-23 16:53:36 -0500'
  content: "<!--%kramer-ref-pre%-->[...] an addendum, here is a link to a blog post
    on how to set up OSX to use a socks proxy.  setup socks proxy in OSX  regards
    \ [...]<!--%kramer-ref-post%-->"
- id: 230804
  author: Gary Larizza
  author_email: ''
  author_url: http://twitter.com/glarizza/status/179044614882332672
  date: '2012-03-12 03:22:17 -0400'
  date_gmt: '2012-03-12 07:22:17 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">@ryanycoleman @stahnma Basically, ssh -D http://t.co/qDdw51ib</span></span>
- id: 463256
  author: C&oacute;mo crear un proxy p&uacute;blico a trav&eacute;s de ssh. | Demonios
    y pinguinos.
  author_email: ''
  author_url: http://demoniosypinguinos.wordpress.com/2011/02/10/como-crear-un-proxy-publico-a-traves-de-ssh/
  date: '2013-03-10 22:56:08 -0400'
  date_gmt: '2013-03-11 02:56:08 -0400'
  content: "<!--%kramer-ref-pre%-->[...] M&aacute;s info: http://dltj.org/article/ssh-as-socks-proxy/
    [...]<!--%kramer-ref-post%-->"
- id: 656537
  author: Using ssh as proxy/tunnel between Mac OS and Linux | Blog Inventic.eu
  author_email: ''
  author_url: http://blog.inventic.eu/2014/02/using-ssh-as-proxy-tunnel-between-mac-os-and-linux/
  date: '2014-04-06 07:09:39 -0400'
  date_gmt: '2014-04-06 11:09:39 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;] ssh -D as SOCKS proxy [&#8230;]<!--%kramer-ref-post%-->"
---
<p>Dear future self,</p>
<p>If you are reading this, you are remembering a time when you ran into a really nasty <a href="http://en.wikipedia.org/wiki/Proxy_server#Intercepting_proxy_server" title="Proxy server - Wikipedia">interception proxy</a> ((Version of the <a href="http://en.wikipedia.org/wiki/Proxy_server?oldid=192282546#Intercepting_proxy_server">"Proxy Server" Wikipedia page when this posting was written</a>)) and you are looking for a way around it.  Do you remember when you were sitting in the Denver International Airport using their free wireless service?  And remember how it inserted advertising banners in HTML frames at the top of random web pages as you surfed?</p>
<p>After about a half an hour of this, you started looking for solutions and found that the secure shell client can act as a <a href="http://en.wikipedia.org/wiki/SOCKS" title="SOCKS - Wikipedia">SOCKS proxy</a> ((Version of the <a href="http://en.wikipedia.org/wiki/SOCKS?oldid=192280146">SOCKS Wikipedia page when this posting was written</a>)).  Using 'ssh', you set up a tunnel between your laptop and a server in the office that encrypted and effectively hid all of your network communications from the interception proxy.  And if you are reading this again you want to remember how you did it.</p>
<h2>Set up the SOCKS proxy</h2>
<p>SOCKS is a client protocol that can be used to tunnel all of your traffic to a remote host before it fans out across the internet.  The <a href="http://www.openssh.com/" title="OpenSSH homepage">OpenSSH client</a> can set up a local SOCKS proxy that uses an 'ssh' session as the network tunnel.  To set up the tunnel, use the <code>-D</code> option followed by a local port number: </p>
{% highlight bash %}
ssh -D 9050 [username]@[remote.server.name]
{% endhighlight %}
<p>To refresh your memory, here is an extract from the 'ssh' manual page for the -D option:<br />
<blockquote>
<dl>
<dt>-D [<code>bind_address</code>:]<code>port</code></dt>
<dd>Specifies a local "dynamic'' application-level port forwarding. This works by allocating a socket to listen to <code>port</code> on the local side, optionally bound to the specified <code>bind_address</code>.  Whenever a connection is made to this port, the connection is forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine.  Currently the SOCKS4 and SOCKS5 protocols are supported, and ssh will act as a SOCKS server.  Only root can forward privileged ports. Dynamic port forwardings can also be specified in the configuration file.</dd>
</dl>
</blockquote>
<h2>Using the SOCKS proxy</h2>
<div style="float:right;border:1px solid #CCC; margin:0 0 1.5em 2.5em; padding: .75em; width:35%;"><a href="/wp-content/uploads/2008/02/airport-advanced-settings-proxy.png" title="MacOSX 10.5 Proxy screen"><img src="/wp-content/uploads/2008/02/airport-advanced-settings-proxy.png" alt="MacOSX 10.5 Proxy screen" /></a></div>
<p>Next you need to tell the applications to use the SOCKS proxy.  If you are still using a Mac when you are reading this, you'll probably have it pretty easy.  Mac OSX lets you set a proxy system-wide that all well-written Mac applications will use to get their parameters.  It is in the "Proxies" tab of the Advanced... network settings.  On Mac OSX version 10.5 (Leopard), it looks like the graphic to the right.</p>
<p>If you're using some sort of UNIX variant, the application may have a setting to use a SOCKS client, or you may need to use the '<a href="http://tsocks.sourceforge.net/" title="tsocks - Transparent SOCKS Proxying Library">tsocks</a>' <a href="http://www.linux.com/articles/54894" title="&#039;Creating virtual private networks with tsocks and VTun&#039; from Linux.com">shim</a> that intercepts the network calls of the application.  And, future self, if you are using a Microsoft Windows box right now, please remember how much simpler life was when you used a Mac or Linux desktop.  If you find yourself in such a spot, some reader of this blog posting may have left a comment for you below that will help you use a SOCKS proxy with a Windows platform.</p>
<p>Hope this helps.  Sincerely,</p>
<p>Self, circa February 2008</p>
