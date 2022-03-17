---
title: "Sanctioning Governments on the Internet"
categories:
- Meta Category
tags:
- internet governance
- internet
- governance
---

What a strange article title to type: _Sanctioning Governments on the Internet._ 
What does that even mean? 
Who would decide? 
Who would implement the decision? 
To say nothing of the consequences of trying to impose an Internet Sanction on a government or a country. 

{% include image.html wpsrc="2022/2022-03-10-woodyatpch-tweet.png" float="right" width="320" url="https://twitter.com/woodyatpch/status/1501820133227974656" alt="Screen capture of Bill Woodcock's tweet: 'Ten days and dozens of authors working together, we now have a document that describes the Internet infrastructure governance community's position on sanctions: what's appropriate, and a multistakeholder governance method for their imposition'" %} 

The internet as we know it is a quirky beast. 
It is called "inter-net" because it is formed as the interconnection of independent networks plus a healthy dose of human capital (and independent streams of monetary capital), reliance on openly-published and open-ended standards, interpersonal trust, and—quite frankly—quite a bit of luck. 

You might think of "the internet" as one big thing, but in reality it is many smaller things hooked together by common agreement. 
The internet connection at my house comes from an Internet Service Provider (ISP). 
My ISP connects to one or more (likely many more than one) other ISPs and transit providers. 
Through those interconnections, a message I'm typing here will be sent to a computer across town, across the country, and across the world. 

It works like this because many decades ago, a bunch of people got together to agree on the methods and rules computers would use to communicate with each other. 
A guiding philosophy was to make those methods and rules simple and easy to implement. 
Another guiding principle was to build up layers of complexity that relied on the functionality of the layers below it. 

1. At the bottom-most layer, the network equipment moves messages along a path from a sending computer to a receiving computer. That equipment doesn't understand or care what was in the messages...it just knows how to get the message one hop closer to its destination. 
1. On top of that is a set of rules (a "protocol") for ensuring all messages get from the sender to the receiver and describing how to retransmit if something is missing. 
1. On top of that is a protocol for translating human-readable names into computer-understandable addresses.
1. On top of that, a protocol for requesting and receiving a file. 
1. Then a specification for how to arrange text on a page. 
1. Lastly, a web browser that understands that specification and knows how to ask the layer below it to retrieve an HTML file from a faraway server.

The network layer at the bottom doesn't know the difference between an HTML file and a snippet of voice on a Zoom call, and the browser at the top doesn't know how the file got to it. 
It is the common agreement on the protocols and specifications across decades of work that put this page in front of your eyes. 

So about those key components of the "inter-net":

* **human capital**: coming to agreement takes time, and humans need to bring their priorities, their experiences, their knowledge, and their biases to the table to work to a common agreement.
* **monetary capital**: every network that is a part of the "inter-net" is paying for its piece to connect its users to is neighboring networks; there isn't one singular budget of internet money.
* **openly-published standards**: all of the core internet standards—the rules by which computers talk to each other and programs on those computers talk to each other—are free to examine and implement by anyone.
* **open-ended standards**: each of the internet standards handles a concise piece of the puzzle and makes as few assumptions as possible about how things will work outside of its well-defined control.
* **interpersonal trust**: there are very few central internet authorities (more on this in a moment); when an ISP connects to its neighbor, it trusts that the neighbor will follow the rules set out in the standards and the guidance from the central authorities.
* **quite a bit of luck**: the internet didn't have to be formed this way; in fact, there were schemes that were considerably more centralized, prescriptive, and tightly controlled.

That is the *multistakeholder* nature of the inter-net. 
To disrupt any of that would require the coordination of a whole lot of people at many companies. 
If there are any central internet authorities at all, they are the few organizations that assign network addresses, run the systems that translate human-readable names ("dltj.org") to computer-recognizable network addresses ("143.204.39.101" and "2600:9000:2177:8a00:13:fcdc:19c0:93a1"), and operate the central network traffic exchange points around the world. 
And this brings us back to the subject of Bill Woodcock's tweet. 

Bill is the chief executive officer of an organization called {% include robustlink.html href="https://www.pch.net/" versionurl="https://web.archive.org/web/20220311020858/https://www.pch.net/" versiondate="2022-03-10" title="Packet Clearing House homepage" anchor="Packet Clearing House (PCH)" %}. 
It is one of those organizations that you've never heard of because it does its job behind the scenes so well. 
PCH runs Internet Exchange Points—those places where various ISPs come together to exchange traffic with their neighbors. 
It also runs many top-level name-to-number translation servers (called Domain Name Service, or DNS). 
If PCH stopped working, you would know it. 
Or, perhaps more accurately, you wouldn't know PCH stopped working because your computer probably wouldn't be able to talk to anyone else. 

The document that Bill tweeted about is called _{% include robustlink.html href="https://www.pch.net/resources/Papers/Multistakeholder-Imposition-of-Internet-Sanctions.pdf" versionurl="https://web.archive.org/20220311010844/https://www.pch.net/resources/Papers/Multistakeholder-Imposition-of-Internet-Sanctions.pdf" versiondate="2022-03-11 00:22:56+00:00" title="Multistakeholder Imposition of Internet Sanctions (PDF)" anchor="Multistakeholder Imposition of Internet Sanctions" %}_. 
***Multistakeholder*** is key here because, as I described above, there isn't one company, one government, or one person who can decide what happens on the inter-net. 
Yes, within a country, a government can dictate what the ISPs in that country can do. 
Most famous is the "great firewall of China" that heavily regulates what happens on the Chinese portion of the inter-net. 
But as a matter of fact, no one has that much control over the inter-net as a whole. 
Not the United States. 
Not the United Nations. 
Not the International Telecommunication Union (as much as they try to get such control). 

This document was put together in response to a {% include robustlink.html href="https://www.wired.com/story/ukrainian-official-digital-front/" versionurl="https://web.archive.org/web/20220311030548/https://www.wired.com/story/ukrainian-official-digital-front/" versiondate="2022-03-10" title="I’m a Ukrainian Official. We Need More Help on the Digital Front | Wired" anchor="request from the Ukrainian Ministry of Digital Transformation to sanction Russia" %} over its government's war on Ukraine. 
Ukraine wants to cut off Russian networks from the rest of the internet, disable its top-level domain names, and revoke its web server security certificates. 
There are technical problems with those requests that border on the impossible, and the _Multistakeholder_ document says why. 

{% include image.html wpsrc="2022/2022-03-10-Multistakeholder-Imposition-of-Internet-Sanctions.png" float="right" width="320" url="https://www.pch.net/resources/Papers/Multistakeholder-Imposition-of-Internet-Sanctions.pdf" alt="Image of the first page of the linked document, Multistakeholder Imposition of Internet Sanctions" %} 

The executive summary of the document is:

>The invasion of Ukraine poses a new challenge for multistakeholder Internet infrastructure governance. In this statement, we discuss possible sanctions and their ramifications, lay out principles that we believe should guide Internet sanctions, and propose a multistakeholder governance mechanism to facilitate decision-making and implementation.

I encourage you to read the whole thing. 
The core part of it is just over two pages long with an introduction (that paired with the discussion above will hopefully emphasize how important it is that the people of the inter-net get this right), a series of principles that could guide a policy on internet sanctions, and recommendations for moving the multistakeholder deliberation forward. 
Past the signatories on the second page is an additional four-page appendix on why what the Ministry of Digital Transformation was asking for is ill-advised and/or impossible. 

My heart cries out for the Ukrainian people. 
The Russian government must be persuaded to stop its actions. 
The internet's **human capital** and **interpersonal trust** will move slowly (mainly because this is precedent-setting) to bring about a consensus on Internet Sanctions—much too slowly to help with the immediate concerns. 
But it is the historically correct and appropriate route to take. 