---
title: "This Was News: a time capsule of yesterday's headlines"
summary: 
categories:
- Personal
tags:
- This Was News
---
Earlier this month, I added a [post here about Five Thank Yous]({filename}2026-09-13-five-thank-yous)...this year's summer vacation project. 
This weekend I was working on last summer's vacation project and realized I hadn't posted about it here.
That project is **[This Was News](https://thiswas.news)**, a website and social media bot that encourages people to reflect on the news that was. 
It seems (to me, at least) that the news cycle is winding faster and faster, which makes it easy to forget what the most important story of the day when it happened. 
One reasonable reaction to this is to tune out the news entirely. 
Another reaction would be to get periodic reminders of those stories, then be able to think about their impact after time has passed.

{{ image(width="600", abssrc="https://thiswas.news/image/social-banner.png", alt="This Was News logo featuring a calendar icon with rewind arrows, alongside the text 'THIS WAS NEWS' in a serif font, with 'WAS' highlighted in orange-red and 'NEWS' in bold black.") }} 

Although this site first debuted in 2025, its origins go back to February 2024 when a collision at DC's National Airport between a military helicopter and a commercial jet was the biggest news. 
This was, of course, a big deal, but I wondered how soon it would fall off the front page and eventually be forgotten. 
(Do you remember the around-the-clock reporting on that tragedy?) 

It wasn't long after that before I wrote the "gatherer" stage of the project: an automated process to save lead article titles and URLs from the home pages of the Associated Press wire service, NPR, and the New York Times. 
It ran for several months while I occasionally worked on other parts of the project. 
(Eventually, I wrote a "back-fill" script that pulled the headlines from the Washington Examiner and Center Square websites to round out the political biases.)

The "Gather" script runs twice daily: 6:30am and 6:30pm Eastern U.S. Time. 
That felt like the right time to capture the important news of the day: early morning East Coast time to get the important news from the previous day, then half a day later to see what happened in the first part of the current day. 
The Gather script marks the "top" story from each site, then saves the next two to four stories in the order in which they appear in the HTML code of the page. 
I'm using the order of appearance as a proxy for how important each news organization thinks the stories are. 
The [Editorial Policy](https://thiswas.news/editorial-policy/) page describes how I pick the news organizations and which stories are used from each site.

The way I envisioned using this was to get periodic posts in my social media feed, then replying to the post saying "remind me in 30 days". 
Then a month later the bot would send me a personal message reminding me about the event. 
As it turns out, that "remind me" function isn't as useful as I thought (and people haven't been using it) but it is still there. 
A good number of people are subscribed to the Bluesky and Mastodon accounts, a few have subscribed to the daily email, and an unknown number use the RSS feeds.  
(All of these methods are described on the "[Get Reminded](https://thiswas.news/reminders/)" page.)
The site's BlueSky and Mastodon bots will also record comments, likes, and reposts on each day's page to create a running commentary on the news.

Last summer's vacation project was a push to get all of the pieces functioning as a system. 
I tried a "quiet launch" for ThisWas.News...I was curious to see how far it would go on its own without me pushing it with my existing (meager) social media presence. 
For the first six months or so, it got a couple dozen people following the site's bots and reposting its content, which I thought was an interesting organic spread.
Since then I've posted about it a few times with my Bluesky and Mastodon accounts, and reshared some of its content, so the project is quite firmly tied to me now.

## Fall 2026 Update

The site has been gathering news for about two and a half years and has been publicly available for about a year. 
Over that time, I found that one of the news sources wasn't very useful, so I dropped Center Square and added the Wall Street Journal's news page. 
(I had initially rejected the WSJ as mainly a finance news source, but reconsidered this year.)
I also added The Guardian from the U.K. and National Post from Canada as news sources with a bit of an outside-U.S. perspective. 

The difficulty has come with the anti-webscraper features that news sites are putting in place now. 
I'm not going any deeper than the front page of each news site to get the title and link to the article, but even that was too much for the New York Times and Associated Press. 
I reluctantly switched to parsing the New York Times' RSS feed. 
This isn't great because the RSS feed doesn't accurately reflect the order of articles in the page's HTML, so it feels like a derivative source instead of what the NYT editors think is really important. 
There isn't an alternative for the Associated Press at the moment — they don't have a public RSS feed, and it seems like they are pushing people toward their developer API.
Needless to say, I'm not willing to pay for a developer API key for a solo, spare-time project like this, so I might drop the Associated Press. 
(If anyone has another way to get the lead stories from the Associated Press, please let me know!)

A few months ago, I also added "tags" to the data model for each story, and those get output as linkable tags in the social media feeds. 
That has helped with discovery of the posts in the social media feeds quite a bit.

The core idea still holds: the news moves fast, and it's worth having something that slows it back down. 
Two and a half years in, the earliest stories the Gather script saved are now old enough to be genuinely surprising to me to look back on — which is really the whole point. 
If you'd like a periodic nudge of your own, the [Get Reminded](https://thiswas.news/reminders/) page has the Bluesky and Mastodon bots, the daily email, and the RSS feeds — pick whichever fits how you already read. 
If you have ideas on how the concepts of this site could be extended, let me know! 
...those ideas might work their way into next year's summer vacation project.
