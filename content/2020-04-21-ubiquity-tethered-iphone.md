---
title: Tethering a Ubiquity Network to a Mobile Hotspot
modified: 2020-04-21T19:41:48-04:00
categories:
- Raw Technology
tags:
- howto
- networking
- ubiquity
- mobile
- iOS
- system administration
---
I saw it happen. 
{% include image.html
  wpsrc="2020/2020-04-21-ditchwitch.png"
  caption="The cable-chewing device"
%}
The contractor in the neighbor's back yard with the Ditch Witch trencher burying a cable. 
I was working outside at the patio table and just about to go into a Zoom meeting. 
Then the internet dropped out. 
Suddenly, and with a wrenching feeling in my gut, I remembered where the feed line was buried between the house and the cable company's pedestal in the right-of-way between the properties. 
Yup, he had just cut it.

To be fair, the utility locator service did not mark the my cable's location, and he was working for a different cable provider than the one we use. 
(There are three providers in our neighborhood.)
It did mean, though, that our broadband internet would be out until my provider could come and run another line. 
It took an hour of moping about the situation to figure out a solution, then another couple of hours to put it in place:  an iPhone tethered to a Raspberry Pi that acted as a network bridge to my home network's UniFi Security Gateway 3P.
{% include image.html 
  wpsrc="2020/2020-04-21-ubiquity-tethered-iphone.svg"
  caption="Network diagram with tethered iPhone"
%}
A few years ago I was tired of dealing with spotty consumer internet routers and upgraded the house to [UniFi](https://unifi-network.ui.com/) gear from Ubiquity. 
Rob Pickering, a college comrade, had [written about his experience with the gear](https://robpickering.com/ubiquiti-configure-micro-segmentation-for-iot-devices/) and I was impressed. 
It wasn't a cheap upgrade, but it was well worth it.
(Especially now with four people in the household working and schooling from home during the [COVID-19 outbreak](https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic).) 
The UniFi Security Gateway has three network ports, and I was using two: one for the uplink to my cable internet provider (WAN) and one for the local area network (LAN) in the house. 
The third port can be configured as another WAN uplink or as another LAN port. 
And you can tell the Security Gateway to use the second WAN as a failover for the first WAN (or as load balancing the first WAN). 
So that is straight forward enough, but do I get the Personal Hotspot on the iPhone to the second WAN port?
That is where the Raspberry Pi comes in.

The [Raspberry Pi](https://www.raspberrypi.org/) is a small computer with USB, ethernet, HDMI, and audio ports. 
The version I had laying around is a Raspberry Pi 2—an older model, but plenty powerful enough to be the network bridge between the iPhone and the home network.
The toughest part was bootstrapping the operating system packages onto the Pi with only the iPhone Personal Hotspot as the network. 
That is what I'm documenting here for future reference.

## Bootstrapping the Raspberry Pi

The Raspberry Pi runs [its own operating system called Raspbian](https://www.raspberrypi.org/downloads/) (a Debian/Linux derivative) as well as more mainstream operating systems.
I chose to use the [Ubuntu Server for Raspberry Pi](https://ubuntu.com/download/raspberry-pi) instead of Raspbian because I'm more familiar with Ubuntu.
I tethered my MacBook Pro to the iPhone to download the Ubuntu 18.04.4 LTS image and follow the [instructions for copying that disk image to the Pi's microSD card](https://ubuntu.com/tutorials/create-an-ubuntu-image-for-a-raspberry-pi-on-macos#2-on-your-macos-machine). 
That allows me to boot the Pi with Ubuntu and a basic set of operating system packages.

### The Challenge: Getting the required networking packages onto the Pi

It would have been really nice to plug the iPhone into the Pi with a USB-Lightning cable and have it find the tethered network. 
That doesn't work, though. 
Ubuntu needs at least the [`usbmuxd`](https://launchpad.net/ubuntu/+source/usbmuxd) package in order to see the tethered iPhone as a network device. 
That package isn't a part of the disk image download. 
And of course I can't plug my Pi into the home network to download it (see first paragraph of this post).

My only choice was to tether the Pi to the iPhone over WiFi with a USB network adapter. 
And that was a bit of Ubuntu voodoo. 
Fortunately, I found [instructions on configuring Ubuntu to use a WPA-protected wireless network](https://askubuntu.com/a/279333) (like the one that the iPhone Personal Hotspot is providing).
In brief:

{% highlight bash linenos %}
sudo -i
cd /root
wpa_passphrase my_ssid my_ssid_passphrase > wpa.conf
screen -q
wpa_supplicant -Dwext -iwlan0 -c/root/wpa.conf
<control-a> c
dhclient -r
dhclient wlan0
{% endhighlight %}

Explanation of lines:

1. Use `sudo` to get a root shell
1. Change directory to root's home
2. Use the `wpa_passphrase` command to create a `wpa.conf` file.  Replace `my_ssid` with the wireless network name provided by the iPhone (your iPhone's name) and `my_ssid_passphrase` with the wireless network passphrase (see the "Wi-Fi Password" field in _Settings -> Personal Hotspot_).
3. Start the `screen` program (quietly) so we can have multiple pseudo terminals.
4. Run the `wpa_supplicant` command to connect to the iPhone wifi hotspot.  We run this the foreground so we can see the status/error messages; this program must continue running to stay connected to the wifi network.
5. Use the `screen` hotkey to create a new pseudo terminal.  This is control-a followed by a letter c.
6. Use `dhclient` to clear out any DHCP network parameters
7. Use `dhclient` to get an IP address from the iPhone over the wireless network.

_Now_ I was at the point where I could install Ubuntu packages.
(I ran  `ping www.google.com` to verify network connectivity.) 
To install the usbmuxd and network bridge packages (and their prerequisites):

{% highlight bash linenos %}
apt-get install usbmuxd bridge-utils
{% endhighlight %}

If your experience is like mine, you'll get an error back:

```
couldn't get lock /var/lib/dpkg/lock-frontend
```

The Ubuntu Pi machine is now on the network, and the automatic process to install security updates is running.
That locks the Ubuntu package registry until it finishes. 
That took about 30 minutes for me.
(I imagine this varies based on the capacity of your tethered network and the number of security updates that need to be downloaded.)
I monitored the progress of the automated process with the `htop` command and tried the `apt-get` command when it finished.
If you are following along, now would be a good time to skip ahead to _Configuring the UniFi Security Gateway_ if you haven't already set that up.

## Turning the Raspberry Pi into a Network Bridge

With all of the software packages installed, I restarted the Pi to complete the update: `shutdown -r now`
While it was rebooting, I pulled out the USB wireless adapter from the Pi and plugged in the iPhone's USB cable.
The Pi now saw the iPhone as `eth1`, but the network did not start until I went to the iPhone to say that I "Trust" the computer that it is plugged into.
When I did that, I ran these commands on the Ubuntu Pi:

{% highlight bash linenos %}
dhclient eth1
brctl addbr iphonetether
brctl addif iphonetether eth0 eth1
brctl stp iphonetether on
ifconfig iphonetether up
{% endhighlight %}

Explanation of lines:

1. Get an IP address from the iPhone over the USB interface
2. Add a network bridge (the `iphonetether` is an arbitrary string; some instructions simply use `br0` for the zero-ith bridge)
3. Add the two ethernet interfaces to the network bridge
4. Turn on the Spanning Tree Protocol (I don't think this is actually necessary, but it does no harm)
5. Bring up the bridge interface

The bridge is now live!
Thanks to [Amitkumar Pal](https://stackoverflow.com/a/41768606) for the hints about using the Pi as a network bridge. 
[More details about the bridge networking software](https://wiki.debian.org/BridgeNetworkConnections) is on the Debian Wiki.

{% include note.html notetext="I'm using a hardwired keyboard/monitor to set up the Raspbery Pi.  I've heard from someone that was using SSH to run these commands, and the SSH connection would break off at <code>brctl addif iphonetecther eth0 eth1</code>" %}

## Configuring the UniFi Security Gateway

I have a UniFi Cloud Key, so I could change the configuration of the UniFi network with a browser.
(You'll need to know the IP address of the Cloud Key; hopefully you have that somewhere.) 
I connected to my Cloud Key at https://192.168.1.58:8443/ and clicked through the self-signed certificate warning.

First I set up a second Wide Area Network (WAN—your uplink to the internet) for the iPhone Personal Hotspot: _Settings -> Internet -> WAN Networks_.
Select "Create a New Network":

* **Network Name**: Backup WAN
* **IPV4 Connection Type**: Use DHCP
* **IPv6 Connection Types**:  Use DHCPv6
* **DNS Server**: `1.1.1.1` and `1.0.0.1` (CloudFlare's DNS servers)
* **Load Balancing**: `Failover only`

The last selection is key...I wanted the gateway to only use this WAN interfaces as a backup to the main broadband interface.
If the broadband comes back up, I want to stop using the tethered iPhone!

Second, assign the Backup WAN to the LAN2/WAN2 port on the Security Gateway (_Devices -> Gateway -> Ports -> Configure interfaces_):

* **Port WAN2/LAN2 Network**: WAN2
* **Speed/Duplex**: Autonegotiate

Apply the changes to provision the Security Gateway.
After about 45 seconds, the Security Gateway failed over from "WAN iface eth0" (my broadband connection) to "WAN iface eth2" (my tethered iPhone through the Pi bridge).
These showed up as alerts in the UniFi interface.

## Performance and Results

So I'm pretty happy with this setup.
The family has been running simultaneous Zoom calls and web browsing on the home network, and the performance has been mostly normal.
Web pages do take a little longer to load, but whatever Zoom is using to dynamically adjust its bandwidth usage is doing quite well.
This is chewing through the mobile data quota pretty fast, so it isn't something I want to do every day.
Knowing that this is possible, though, is a big relief.
As a bonus, the iPhone is staying charged via the 1 amp power coming through the Pi.
