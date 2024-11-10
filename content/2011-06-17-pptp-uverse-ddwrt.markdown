---
layout: wordpress-import
status: published
published: true
title: 'PPTP VPN for iOS with AT&T Uverse and DD-WRT'
modified: 2011-06-17T16:41:33+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 3025
wordpress_url: http://dltj.org/?p=3025
date: '2011-06-17 12:41:33 -0400'
date_gmt: '2011-06-17 16:41:33 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- networking
- security
- iOS
- vpn
- pptp
comments:
- id: 151979
  author: Ryan Collins
  author_email: blogs2009@ryancollins.org
  author_url: http://ryancollins.org/
  date: '2011-06-22 22:57:21 -0400'
  date_gmt: '2011-06-23 02:57:21 -0400'
  content: "I setup this up on a VPS, that way I get higher throughput than on my
    Road Runner connection.\r\n\r\nMy only problem is that there are public wifi hotspots
    that I can't connect to my PPTP server. On my MacBook this isn't a problem because
    I then use SOCKS tunneled over SSH (with SSH running on port 443, which seems
    to never be blocked. :) But that doesn't work on my iPhone, so I just don't use
    the public wifi on it for those situations."
- id: 152054
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-06-23 06:45:16 -0400'
  date_gmt: '2011-06-23 10:45:16 -0400'
  content: "Hey, Ryan. Do you have a recipe to set up a PPTP tunnel using a VPS service?
    \ The documentation I found out there is a mess. \n\nI, too, have a separate IP
    address on my personal server that has an ssh daemon listening on port 443. I
    can use that for my laptop, but it doesn't work with (non-jail broken) iOS devices.
    If your going the tunneled ssh route, take a look at sshuttle &mdash; it allows
    you to go deeper in the routing level than SOCKS."
- id: 153249
  author: Ryan Collins
  author_email: blogs2009@ryancollins.org
  author_url: http://ryancollins.org/
  date: '2011-06-29 19:16:20 -0400'
  date_gmt: '2011-06-29 23:16:20 -0400'
  content: "Here's the tutorial I used:\r\nhttp://www.ubuntugeek.com/howto-pptp-vpn-server-with-ubuntu-10-04-lucid-lynx.html"
- id: 153491
  author: Ryan Collins
  author_email: blogs2009@ryancollins.org
  author_url: http://ryancollins.org/
  date: '2011-06-30 23:35:29 -0400'
  date_gmt: '2011-07-01 03:35:29 -0400'
  content: "Ok, sshuttle is very, very cool. Especially with this app:\r\nhttp://apenwarr.ca/log/?m=201102#04\r\n\r\nThanks!"
- id: 153566
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-07-01 08:55:51 -0400'
  date_gmt: '2011-07-01 12:55:51 -0400'
  content: Ah, a GUI for sshuttle?  Thanks for the pointer to that, and you're welcome.
- id: 159826
  author: Library Feed
  author_email: ''
  author_url: http://twitter.com/libraryfeed/status/81769940599848961
  date: '2011-06-17 17:07:27 -0400'
  date_gmt: '2011-06-17 21:07:27 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">PPTP VPN for iOS with AT&amp;T Uverse and DD-WRT
    http://bit.ly/iGEdh1</span></span>
- id: 159827
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/81769837319303168
  date: '2011-06-17 17:07:03 -0400'
  date_gmt: '2011-06-17 21:07:03 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: PPTP VPN for iOS with AT&amp;T
    Uverse and DD-WRT http://bit.ly/knsO8T</span></span>'
- id: 168918
  author: '瘋 iDevice: iOS 4.3.3 does not work with PPTP 無法連接PPTP VPN'
  author_email: ''
  author_url: http://www.funidevice.com/2011/07/ios-433-does-not-work-with-pptp-pptp.html
  date: '2011-09-08 09:29:31 -0400'
  date_gmt: '2011-09-08 13:29:31 -0400'
  content: "<!--%kramer-ref-pre%-->[...] PPTP VPN for iOS with AT&amp;T Uverse and
    DD-WRT [...]<!--%kramer-ref-post%-->"
- id: 649959
  author: anthony
  author_email: zerberk@yahoo.com
  author_url: ''
  date: '2013-09-10 07:29:30 -0400'
  date_gmt: '2013-09-10 11:29:30 -0400'
  content: i have the same connection problem too on iphone and ipad when connecting
    to pptp on dd-wrt (tested on starbucks wifi and alike). i also avail to paid vpn
    services and tried pptp feature on ios hardwares and sadly had the same results.
    i guess its apple' ios is the one breakin pptp connection.imho.
- id: 656279
  author: aMakUzr
  author_email: user33@derman.com
  author_url: ''
  date: '2014-03-21 18:06:34 -0400'
  date_gmt: '2014-03-21 22:06:34 -0400'
  content: "----------------------------------------------------------------------\r\n\r\nI've
    put up an article on this topic that I hope will help others:\r\n\r\nsee Setting
    Up an iOS 7 On-Demand VPN:\r\nhttp://www.derman.com/blogs/Setting-Up-iOS-OnDemand-VPN\r\n\r\n----------------------------------------------------------------------"
---
<p>Wandering into public or semi-public wireless networks makes me nervous because I know how my network traffic can be easily watched, and because I'm a geek with control issues I'm even more nervous when using devices that I can't get to the insides of (like phones and tablets).  One way to tamp down my concerns is to use a Virtual Private Network (VPN) to tunnel the device's network connection through the public wireless network to a trusted end-point, but most of those options require a subscription to a VPN service or a VPN installed in a corporate network.  I thought about using one of the open source VPN implementations with an Amazon EC2 instance, but it isn't possible with the EC2 network configuration judging from the comments on the Amazon Web Services support forums.  (Besides, installing one of the open source VPN software implementations looks far from turnkey.)  Just before I lost hope, though, I saw a reference to using the open source DD-WRT consumer router firmware to do this.  After plugging away at it for an hour or so, I made it work with my home router, a AT&amp;T U-verse internet connection, and iOS devices.  It wasn't easy, so I'm documenting the steps here in case I need to set this up again.</p>
<h2>Prerequisites</h2>
<p>To make this happen, I'm using a <a href="http://web.archive.org/web/20110617000000/http://www.dlink.com:80/DIR-825" title="D-Link Xtreme N Dual Band Gigabit Router">D-Link DIR-825</a> that has been flashed with "v24-sp2 (04/23/10) std" of the <a href="http://www.dd-wrt.com/wiki/index.php/What_is_DD-WRT%3F" title="What is DD-WRT? - DD-WRT Wiki">DD-WRT firmware</a>.  For my internet connection I have a <a href="http://www.att.com/u-verse/explore/residential-gateway.jsp" title="AT&amp;T Residential Gateway">AT&amp;T U-verse residential gateway</a> and a "Max Turbo" plan (I work from home so I need the 3 Mbps uplink speed that is only available with "Max Turbo", although that added uplink capacity is certainly helpful for this road-warrior VPN use).  I also have a pair of iOS version 4.3.3 devices; this setup might work for other handheld operating systems (e.g. Android or Windows Mobile), but I don't have any of those to test with.</p>
<p>DD-WRT comes with support for a point-to-point-tunneling-protocol (PPTP) server.  I know <a href="http://pptpclient.sourceforge.net/protocol-security.phtml" title="PPTP Protocol Security">PPTP has some inherent security risks</a>.  At this point I'm just aiming to be harder for someone passively listening on the public wireless network to eavesdrop on my connections.  I'm not doing anything ultra-sensitive that I need advanced encryption; I just don't want to make it easy to watch what my devices are doing.</p>
<h2>Setting up the AT&T U-verse Residential Gateway</h2>
<p>Since the D-Link router is behind the U-verse residential gateway, we need to punch a couple holes through its firewall to allow downstream connections from the iOS devices to reach the D-Link router.  Specifically, one needs to forward ports 1723/TCP and 1723/UDP through the residential gateway firewall to the internal D-Link router.  To do this:</p>
<ol type="1" start="1">
<li>Connect to the web interface of the residential gateway, select the <em>Settings</em> tab followed by the <em>Firewall</em> tab then the <em>Applications, Pinholes and DMZ</em> tab.</li>
<li>This screen has two steps:  1) Select a computer; then 2) Edit firewall settings for this computer.  Click on the link to "Choose" the DIR-825 router (by name).</li>
<li>In the second step choose the "Add a new user-defined application" link.  Use "PPTP" for the <em>Application Profile Name</em>.</li>
<li>Select "TCP" and put "1723" in the <em>From</em> text box, under <em>Application Type</em> select <em>PPTP virtual private network server</em> and leave the rest of the boxes blank for the defaults; click on <em>Add to List</em>.</li>
<li>Repeat everything in the last step except choose <em>UDP</em> in place of <em>TCP</em>.</li>
<li>Click on the <em>Back</em> button to return to the <em>Allow device application traffic to pass through firewall</em> screen.</li>
<li>Select the <em>Allow individual application(s)</em> radio button, click on the <em>User-defined</em> applications list, pick "PPTP" from the Application List, and click on <em>Add</em>.</li>
<li>Click <em>Save</em>.</li>
</ol>
<p>The U-verse residential gateway will now pass everything inbound on ports 1723/TCP and 1723/UDP to the D-Link router.  You're done with the residential gateway setup now.</p>
<h2>Setting up the PPTP Service on DD-WRT</h2>
<p>Now we need to set up the DD-WRT PPTP service.  This is harder than it probably should be, but given the geeky focus of the DD-WRT effort (in my humble opinion), features seem to come before user interface and documentation niceties.  This works for me, but it isn't entirely clear or easy, and I can't offer troubleshooting insights if it doesn't work for you.  It has two main steps -- first, turn on and configure the PPTP server; and second, patch the PPTP server configuration with a start-up script so that it actually works.  First, the PPTP server configuration:</p>
<ol type="1" start="1">
<li>Log onto the DD-WRT web interface, select the <em>Services</em> tab then the <em>VPN</em> tab.</li>
<li>Enable <em>PPTP Server</em>, <em>Broadcast support</em>, and <em>Force MPPE Encryption</em>.</li>
<li>Put in the WAN IP (listed in the upper right corner of the web page) in the <em>Server IP</em> box.  (Some instructions I have seen said that this can be left blank and the firmware will automatically pick it up.  That didn't work for me.)</li>
<li>For Client IPs, put in a range of LAN-side IPs that aren't being used by the DHCP server.  In my case I'm using "192.168.68.200-210".</li>
<li>Put in one or more <em>CHAP-Secrets</em>.  These are the username and passwords used on the PPTP client to connect to this server, and they follow a weird form:  username-space-asterisk-space-password-space-asterisk.  For example:
```
username * password *
```
</li>
<li>Leave <em>Radius</em> disabled.</li>
<li>At the bottom of the screen, pick <em>Apply Settings</em>.</li>
</ol>
<p>The second step is the startup script:</p>
<ol type="1" start="1">
<li>Select the <em>Administration</em> tab then the <em>Commands</em> tab.</li>
<li>Put this in the <em>Commands</em> text box, then select <em>Save Startup</em>:
```bash
#!/bin/sh
sed -i -e 's/mppe .*/mppe required,stateless/' /tmp/pptpd/options.pptpd
echo "nopcomp" >> /tmp/pptpd/options.pptpd
echo "noaccomp" >> /tmp/pptpd/options.pptpd
kill `ps | grep pptp | cut -d ' ' -f 1`
pptpd -c /tmp/pptpd/pptpd.conf -o /tmp/pptpd/options.pptpd
```
</li>
<li>Go to the <em>Management</em> subtab of <em>Administration</em> and at the bottom select <em>Reboot Router</em>.</li>
</ol>
<p>This script comes from the <a href="http://www.dd-wrt.com/wiki/index.php/PPTP_Server_Configuration" title="PPTP Server Configuration | DD-WRT Wiki">PPTP Server Configuration</a> page.  The bulk of it is from the <a href="http://www.dd-wrt.com/wiki/index.php/PPTP_Server_Configuration#iOS_4.3" title="PPTP Server Configuration | DD-WRT Wiki">iOS 4.3</a> heading with the addition of the <code>sed</code> line to <a href="http://www.dd-wrt.com/wiki/index.php/PPTP_Server_Configuration#Force_Encryption" title="PPTP Server Configuration | DD-WRT Wiki">force encryption</a>.</p>
<h2>Configuring the iOS Device</h2>
<p>{{ image(
    div_float="right",
    width="320",
    caption="iOS PPTP VPN Configuration",
    alt="iOS PPTP VPN Configuration",
    localsrc="2011/06/IMG_0267.png") }}
The iOS device was pretty straight forward (particularly compared to the previous steps):</p>
<ol type="1" start="1">
<li>In the <em>Settings</em> app, choose <em>General</em> then <em>Network</em> then <em>VPN</em>.</li>
<li>Select <em>Add VPN Configuration...</em></li>
<li>At the top choose <em>PPTP</em> and give this configuration a descriptive label.</li>
<li>For <em>Server</em> put in the IP address of your U-verse residential gateway.  (Setting up something like Dynamic DNS with DD-WRT is left as an exercise to the reader.)</li>
<li>For <em>Account</em> put in the username field from the CHAP-Secrets text box above.</li>
<li>Leave <em>RSA SecurID</em> off and put in the password field from the CHAP-Secrets text box.</li>
<li>Under <em>Encryption Level</em> select <em>Maximum</em>.</li>
<li>Select <em>Save</em> in the upper right hand corner.</li>
</ol>
<p>Now when you connect to a public network, before starting any applications that will access the internet, go into the <em>Settings</em> app and near the top will be a choice to turn on the VPN.  Give it about five or six seconds to make the connection, and you'll then see a blue VPN icon in the status bar at the top next to the WiFi icon.</p>
<h2>Acknowledgements</h2>
<p>The <a href="http://www.dd-wrt.com/wiki/index.php/PPTP_Server_Configuration" title="PPTP Server Configuration | DD-WRT Wiki">PPTP Server Configuration</a> was much more helpful than the built in documentation for figuring out what was needed to make this work.  A series of posts on the Whirlpool Forums starting with <a href="http://forums.whirlpool.net.au/forum-replies.cfm?t=1260916&p=2&#r28" title="DD-WRT VPN / PPTP Server - Networking - Whirlpool Forums">this reply</a> and continuing through a half-dozen more had the final pieces.</p>
