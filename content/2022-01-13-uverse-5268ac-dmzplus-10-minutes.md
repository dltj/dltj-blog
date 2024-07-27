---
title: 'Router Behind a Uverse/Pace 5268ac Gateway Loses its Mind Every 10 Minutes'
modified: 2022-01-13T20:09:15-05:00
category: Thursday Threads
categories:
  - Raw Technology
tags:
  -  networking
---
Late last year, I had my AT&T Uverse residential gateway replaced. 
For reasons that truly baffle me, AT&T has decided that [they are going to run unsupported equipment on their residential customer network](https://twitter.com/DataG/status/1462819555005374470). 
When the replacement was swapped in, my family noticed that video conference calls—Zoom and Facetime and Slack—would occasionally drop out for about 10 seconds before continuing. 
After much frustration, I started timing the outages and found that they were happening at roughly 10-minute intervals (plus or minus just a few seconds). 

Some internet searching lead to a forum post ({% include robustlink.html href="https://forums.att.com/conversations/att-internet-equipment/pace-5268ac-dmzplus-issue-drops-lan-every-10-minutes/5defc10abad5f2f606c25e99" versionurl="https://forums.att.com/conversations/att-internet-equipment/pace-5268ac-dmzplus-issue-drops-lan-every-10-minutes/5defc10abad5f2f606c25e99" versiondate="2021-11-15" anchor="page 1" %}, {% include robustlink.html href="https://forums.att.com/conversations/att-internet-equipment/pace-5268ac-dmzplus-issue-drops-lan-every-10-minutes/5defc10abad5f2f606c25e99?page=2" versionurl="https://web.archive.org/web/20211214235644/https://forums.att.com/conversations/att-internet-equipment/pace-5268ac-dmzplus-issue-drops-lan-every-10-minutes/5defc10abad5f2f606c25e99?page=2" versiondate="2021-11-15" anchor="page 2" %}) on AT&T's customer site. 
As it turns out, there is a conflict with the DHCP address assignment messages when the residential gateway is in DMZplus mode. [^1]

Forum user "weshunt" had the right solution:

> I'm not a network confguration expert, but it bothered me that the Pace [residential gateway] and the USG both wanted to use 192.168.1.x for DHCP allocations. I noticed that even after putting the USG into the DMZPlus, I could connect a wireless device and it would get an address in the Pace's default 192.168.1.x range, which conflicted with the IP range the USG was trying to manage. And of course the Pace answered to 192.168.1.254, which was also in the default allocation range of the USG.
> 
> So I changed the DHCP settings on the Pace to answer to a different subnet (192.168.100.1 with a DHCP allocation range inside 192.168.100.x as well). Like magic, the USG immediately picked up the DHCP assignment from the Pace and got the public IP exactly like I wanted. Now the networks don't seem to want to fight each other. I can still access the Pace from the wired network via the new gateway IP (192.168.100.1), and also connect to the Pace wirelessly using the old SSID if I need to, though I'm shutting that down to alleviate unnecessary wireless congestion.

Step by step, this is what you need to do.

## Change the LAN DHCP Range
With a web browser, go to your residential gateway advanced device configuration page. 
The link for this will be printed on the bottom of the gateway and is probably http://192.168.1.254. 
You will also need the "Device Access Code" that is printed just below that web address. 
I'm using a hardwired ethernet connection between my desktop and the residential gateway, but this will probably also work over wireless, too.

1. Click on _Settings_
2. ... then _LAN_
3. ... ... then _DHCP_.
3. In the "DHCP  Configuration"→"DHCP Network Range" section, select "Configure manually" and enter these values:
	* Router Address: 192.168.100.1
	* Subnet Mask: 255.255.255.0
	* First DHCP Address: 192.168.100.100
	* Last DHCP Address: 192.168.100.200
	* DHCP Lease Time: 24
1. At the bottom, click "Save".  You'll need your Device Access Code at this point to save your changes.

{{ image(width="846", localsrc="2022/2022-01-13-pace-gateway-dhcp.png", caption="Pace Residential Gateway DHCP Configuration Page", alt="Screen Capture of the DHCP Configuration page of a Pace 5268ac Residential Gateway") }}

The IP address ranges on the LAN side of the residential gateway have now changed, so the browser's computer is going to need a new IP address. 
Unplug the ethernet cable and plug it back in to get a DHCP IP address assignment in the 192.168.100.x block; if using wifi, turn it off and turn it back on. 

## Set DMZplus Mode for Your Router
Connect to the residential gateway advanced device configuration page again. 
Also, make sure your router is plugged into the residential gateway. 
In these examples "SONATA" is the name of my desktop computer, and my home router is called "Gateway".  Yes, I know that is confusing.  Sorry 'bout that.

1. Click on _Settings_
2. ... then _Firewall_
3. ... ... then _Applications, Pinholes and DMZ_.
4. Under "1) Select a computer" pick your router (**not** your desktop computer).
5. Under "2) Edit firewall settings for this computer" pick _Allow all applications (DMZ plus mode)_
6. Click "Save"

{{ image(width="846", localsrc="2022/2022-01-13-pace-gateway-dmzplus.png", caption="Pace Residential Gateway DHCP Configuration Page", alt="Screen Capture of the DHCP Configuration page of a Pace 5268ac Residential Gateway") }}

## Ensure the Router's Network Address is Correct
I think this section is redundant—it should be set this way as a combination of the two changes above—but you can check it to be sure.

1. Click on _Settings_
2. ... then _LAN_
3. ... ... then _LAN IP Address Allocation_.
4. Verify the settings for your router:
	* Current address: your assigned IP address from AT&T
	* Device status: DMZ device
	* Firewall: Disabled
	* Address Assignment: Public (select WAN IP Mapping)
	* WAN IP Mapping: Router WAN IP Address (default)
	* Cascade Router: no
5. Select "Save"

{{ image(width="846", localsrc="2022/2022-01-13-pace-gateway-lan-ip-address-allocation.png", caption="Pace Residential Gateway DHCP Configuration Page", alt="Screen Capture of the DHCP Configuration page of a Pace 5268ac Residential Gateway") }}

[^1]: Aside—my residential gateway is in DMZplus mode because:

	* my home network gear—in particular the wireless access points—are _much_ better than what is in the residential gateway; and
	* I trust AT&T's network about as far as I can throw that residential gateway...apparently for good reason since AT&T thinks it is okay for its customers to have unsupported routers on their networks. 
