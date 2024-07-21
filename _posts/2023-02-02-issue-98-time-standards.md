---
title: Issue 98: Time Standards - leap seconds forwards and backwards, moon time, internet time (then and now), and aliens
modified: 2023-02-01T23:59:05-05:00
categories:
- Thursday Threads
mastodon:
- "Saint Augustine wrote: 'What then is time? If no one asks me, I know: if I wish to explain it to one that asketh, I know not' This week's DLTJ Thursday Threads looks at time standards. https://dltj.org/article/issue-98-time-standards/ 1/7"
- There is a faction of Earthlings that want to eliminate the leap second as a distinct unit of time. Instead, they propose "smearing" that second across an entire day so software developers can avoid having to think about a quirky minute that has 61 seconds. https://dltj.org/article/issue-98-time-standards/#leap-second 2/7
- If you thought adding a second was bad, what are we going to do when we have to remove a second from our clocks to keep solar time in sync with caesium time. https://dltj.org/article/issue-98-time-standards/#backwards-second 3/7
- And what if we leave Earth for the Moon. How are we going to keep track of time there? https://dltj.org/article/issue-98-time-standards/#moon-time 4/7
- Synchronizing time is "black magic" according to one of the pioneers of the internet. Why is it like that? https://dltj.org/article/issue-98-time-standards/#ntp-black-magic 5/7
- Synchronizing clocks to millisecond accuracy isn't good enough for some applications. Read about the move to nanosecond accuracy. https://dltj.org/article/issue-98-time-standards/#ptp 6/7
- Now that we have this time thing sorted out, could we explain it to an alien visitor? Perhaps we don't have time thought through after all. https://dltj.org/article/issue-98-time-standards/#aliens 7/7
- And the weekly addition to #CatsOfMastodon. Mittens invades the groceries looking to rub her face against the strawberry container. bonus/7
---
{% include image.html wpsrc="2023/2023-02-02-confessions.jpg" width="700" alt="Scan of a book page with this quote highlighted: What then is time? If no one asks me, I know: if I wish to explain it to one that asketh, I know not" caption="Augustine, Saint, Bishop of Hippo. <cite>The Confessions of St. Augustine</cite>. New York: Grosset & Dunlap, 1931, <a href='https://babel.hathitrust.org/cgi/pt?id=uc1.b3945012&view=1up&seq=281&q1=what+then+is+time'>page 267</a>. Translation of the Latin original from circa 397 CE."%} 

This week we look at time from a few points of view:

- [Eliminating the leap second](https://dltj.org/article/issue-98-time-standards/#leap-second)
- [If adding a second causes problems, imagine removing a second](https://dltj.org/article/issue-98-time-standards/#backwards-second)
- [What time is it on the Moon?](https://dltj.org/article/issue-98-time-standards/#moon-time)
- [Internet time is "black magic"](https://dltj.org/article/issue-98-time-standards/#ntp-black-magic)
- [From millisecond precision to nanosecond precision](https://dltj.org/article/issue-98-time-standards/#ptp)
- [Explaining our concept of time to aliens](https://dltj.org/article/issue-98-time-standards/#aliens)
- [Mittens in the Groceries](https://dltj.org/article/issue-98-time-standards/#mittens)

{% include thursday-threads-header.html %}


## Eliminating the leap second
{: #leap-second}
{% include thursday-threads-quote.html
blockquote='The leap second change triggered a massive Reddit outage in 2012, as well as related problems at Mozilla, LinkedIn, Yelp and airline booking service Amadeus. In 2017, a leap second glitch at Cloudflare knocked a fraction of the network infrastructure company&apos;s customers&apos; servers offline. Cloudflare&apos;s software, comparing two clocks, calculated that time had gone backward but couldn&apos;t properly handle that result.'
href="https://www.cnet.com/tech/computing/its-time-to-ditch-the-leap-second-the-devastating-effect-of-adding-just-one-second/"
versionurl="https://web.archive.org/web/20220809072523/https://www.cnet.com/tech/computing/its-time-to-ditch-the-leap-second-the-devastating-effect-of-adding-just-one-second/"
versiondate="2022-07-26T01:17:25"
anchor="It's Time to Ditch the Leap Second: The Devastating Effect of Adding Just One Second"
post=', CNET, 8-Aug-2022'
%}

Programmers can be forgiven for assuming that every minute has 60 seconds. 
But sometimes they have 61. 
And when that sometimes happens, you get unexpected results. 
Google proposes using a "leap smear", where computer clocks spread the extra second across all of the 86,400 seconds that make up a day. 


## If adding a second causes problems, imagine removing a second
{: #backwards-second}
{% include thursday-threads-quote.html
blockquote='<p>If the Earth speeds up enough, we might find ourselves pondering over the possibility of a negative leap second. According to the Time and Date folks, a day in 2021 is averaging about 0.2ms faster than the 84600 atomic seconds per day, ~70ms/year, so at most 14 years of this would put us over the threshold (super unlikely). In reality, we don’t have to speed up a full 1000ms of rotation speed because there was always a fractional difference in UT1-UTC.</p><p>The time specs involving leap seconds always included the possibility that a negative leap second could happen, but I don’t think anyone really expected it actually happen. In more practical terms, Either July 31 or December 31 23:59:59 would just… disappear from existence, with clocks ticking from 23:59:58 seconds to 00:00:00.</p>'
href="https://counting.substack.com/p/hate-leap-seconds-imagine-a-negative"
versionurl="https://web.archive.org/web/20220119004844/https://counting.substack.com/p/hate-leap-seconds-imagine-a-negative"
versiondate="2022-07-22T16:38:28"
anchor="Hate leap seconds? Imagine a negative one"
post=', Counting Stuff, 10-Aug-2021'
%}

Add this to the list of things that are possible in our corner of the universe.


## What time is it on the Moon?
{: #moon-time}
{% include thursday-threads-quote.html
blockquote='The Moon doesn’t currently have an independent time. Each lunar mission uses its own timescale that is linked, through its handlers on Earth, to coordinated universal time, or utc — the standard against which the planet’s clocks are set. But this method is relatively imprecise and spacecraft exploring the Moon don’t synchronize the time with each other. The approach works when the Moon hosts a handful of independent missions, but it will be a problem when there are multiple craft working together. Space agencies will also want to track them using satellite navigation, which relies on precise timing signals.'
href="https://www.nature.com/articles/d41586-023-00185-z"
versionurl="https://web.archive.org/20230131010828/https://www.nature.com/articles/d41586-023-00185-z"
versiondate="2023-01-30T20:08:17"
anchor="What time is it on the Moon?"
post=', Nature News, 24-Jan-2023'
%}

Robust, accurate time is a given here on Earth. 
(There are undoubtedly applications where "robust" and "accurate" aren't good enough, but most humans aren't faced with those challenges.) 
Everyone has a sense of the importance of a common understanding of time. 
But what if you are setting up a homestead on another celestial body? 
You might want to sort out your time standards before you build and ship the equipment to your new location. 
For instance, "The Moon’s gravitational pull is weaker than Earth’s, meaning that, to an observer on Earth, a lunar clock would run faster than an Earth one."
So you are not only synchronizing clocks on the Moon, but you also need to deal with the skew of time compared to the Earth.


## Internet time is "black magic"
{: #ntp-black-magic}
{% include thursday-threads-quote.html
blockquote='By 1988, Mills had refined N.T.P. to the point where it could synchronize the clocks of connected computers that had been telling vastly differing times to within tens of milliseconds—a fraction of a blink of an eye. “I always thought that was sort of black magic,” Vint Cerf, a pioneer of Internet infrastructure, told me.'
href="https://www.newyorker.com/tech/annals-of-technology/the-thorny-problem-of-keeping-the-internets-time"
versionurl="https://web.archive.org/20221002182008/https://www.newyorker.com/tech/annals-of-technology/the-thorny-problem-of-keeping-the-internets-time"
versiondate="2022-10-02T14:20:06"
anchor="The Thorny Problem of Keeping the Internet’s Time"
post=', The New Yorker, 30-Sep-2022'
%}

When Vint Cerf, a {% include robustlink.html href="https://en.wikipedia.org/wiki/Vint_Cerf" versionurl="https://en.wikipedia.org/w/index.php?title=Vint_Cerf&oldid=1136158594" versiondate="2023-02-01" title="Vinton Cerf | Wikipedia" anchor="co-developer of TCP/IP" %}, thinks something is black magic, you can wager that it is intense technology.
This article peels back some of the mystique of one of the oldest internet standards: Network Time Protocol (NTP). 
NTP has been under the care of mostly one person since it was first developed in the late 1980s. 
This is a story about honoring an unsung—if prickly—hero of the common good of the internet and how the community is advancing the state of the art beyond what a 40-year-old standard can support. 

I remember getting into the bowels of NTP configurations in the early 1990s when I was helping configure a cluster of NeXT cubes at my university. 
(I also remember longing for an excuse to get the hardware for a stratum 1 server so we could put our mark on the net.) 


## From millisecond precision to nanosecond precision
{: #ptp}
{% include thursday-threads-quote.html
blockquote='Implementing Precision Time Protocol (PTP) at Meta allows us to synchronize the systems that drive our products and services down to nanosecond precision. PTP’s predecessor, Network Time Protocol (NTP), provided us with millisecond precision, but as we scale to more advanced systems on our way to building the next computing platform, the metaverse and AI, we need to ensure that our servers are keeping time as accurately and precisely as possible. With PTP in place, we’ll be able to enhance Meta’s technologies and programs — from communications and productivity to entertainment, privacy, and security — for everyone, across time zones and around the world.'
href="https://engineering.fb.com/2022/11/21/production-engineering/precision-time-protocol-at-meta/"
versionurl="https://web.archive.org/web/20221125192255/https://engineering.fb.com/2022/11/21/production-engineering/precision-time-protocol-at-meta/"
versiondate="2022-11-25T14:22:29"
anchor="How Precision Time Protocol is being deployed at Meta"
post=', Engineering at Meta, 21-Nov-2022'
%}

And this is the advancement of network time from the 1980's NTP (millisecond precision) to today's PTP (nanosecond precision). 
This article's first part discusses the importance of very precise time at internet-scale companies. 
Even if you don't care about the time standards, it is interesting to read about how Facebook structures its databases in its highly distributed architecture.


## Explaining our concept of time to aliens
{: #aliens}
{% include thursday-threads-quote.html
blockquote='<replay-web-page replayBase="/assets/js/replayweb/" source="https://dltj.org/wp-content/uploads/2023/2023-02-02-tweet-1572260363764400129.wacz" url="https://oembed.link/https://twitter.com/foone/status/1572260363764400129" embed="replay-with-info" newwindowbase="https://dev.replayweb.page/" style="width: 30rem;  height: 20rem;"></replay-web-page><noscript><img src="https://dltj.org/wp-content/uploads/2023/2023-02-02-tweet-1572260363764400129.png"></noscript>'
href="https://twitter.com/foone/status/1572260363764400129"
versionurl="https://web.archive.org/20221002135008/https://threadreaderapp.com/thread/1572260363764400129.html"
versiondate="2022-10-02T09:50:05"
anchor="@Foone on Twitter"
post=', 20-Sep-2022'
%}
<script src="/assets/js/replayweb/ui.js"></script>

An imaginary conversation in 68 tweets, including bits like:

- "YOUR CALENDAR IS BASED ON A RELIGIOUS LEADER THAT NOT EVERYONE BELIEVES IN?" ... "well, on his birth. And yeah, we got it wrong by a couple years."
- "yep! Our 9th month is named after the number 7, and so on for 10, 11, and 12."
- "yeah so cultures before then had a 12 month system, because of the moon. But they had been using a 10 month system, before switching to 12 and giving them the modern names"


## Mittens in the Groceries
{: #mittens}
{% include image.html wpsrc="2023/2023-02-02-mittens.jpg" width="700" alt="Two pictures of a black cat with a white bib. In the top picture, the cat has her head through the handles of a canvas bag full of groceries. In the bottom picture, she is rubbing her face against the edges of a plastic container of strawberries." %} 

This is one of Mittens' quirks. 
She waits for the groceries to come in from the car, then starts nosing through them. 
She is looking for the pack of strawberries so she can rub her face on the rough edges of the plastic container.
Other plastic containers of strawberries will do in a pinch, but her clear favorite is strawberries.
