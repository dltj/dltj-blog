---
title: 'Issue 92: Privacy Stories From 2014 Still Echo Today'
modified: 2022-12-07T22:10:45-05:00
category: Thursday Threads
categories:
- Thursday Threads
tags:
- privacy
- algorithmic creulty
- geo-privacy
- cloud encryption
- Facebook
- gdpr
---

Back again. 
Thanks for the comments on the return of the newsletter. 
I've heard that Microsoft Outlook isn't playing nice with my email theme. 
(It also isn't playing fair...someone forwarded the newsletter back to me, and when I replied that person said the view of the newsletter in the reply looked fine in that same Microsoft Outlook.) 
Until I get that fixed, remember that you can read the newsletter online — just follow one of the bullet point links below to get to it. 

This week we're going to pull through some privacy threads to the current day. 
Eight years ago this week, I published a whole <i>DLTJ Thursday Threads</i> issue on privacy.
This was the lead paragraph:

> Are you paranoid yet? Are you worried that [the secret you shared anonymously might come right back to you](https://dltj.org/article/thursday-threads-2014w49/#p24188-gizmodo)? Or wondering why [advertisements seem to follow you around from web page to web page](https://dltj.org/article/thursday-threads-2014w49/#p24188-guardian)? Or just creeped out by [internet-enabled services tracking your every move](https://dltj.org/article/thursday-threads-2014w49/#p24188-nyt-oped)? Or angry that [mobile carriers made it very easy for anyone to track every page you visited from your smartphone](https://dltj.org/article/thursday-threads-2014w49/#p24188-propublica-phone)? Or maybe you will [simply give up any personal information for a delicious cookie](https://dltj.org/article/thursday-threads-2014w49/#p24188-propublica-cookie)? (Are you paranoid now?) 

The first was about how posts on apps like YikYak, Secret, Whisper, and Snapchat weren't really anonymous. 
The second was about the kinds of data that apps collect and aggregate about us. 
The third was an opinion piece about how Uber was tracking your every move as part of its experiments, and also contained a nugget about how Facebook was updating its terms of service to say explicitly that the app will now track your location. 
The fourth was how AT&T and Verizon got caught invisibly rewriting web pages passing through their network to include their own tracking tokens.
And the fifth was a person-on-the-street test to see how much personal information passers-by would give up for a cookie (a tasty treat, not the browser cookie kind).

So with all that attention on privacy in 2014, you'd figure we'd have it all solved by now, right? 
Let's see what some of the latest stories are.

* [Algorithmic Creulty](https://dltj.org/article/issue-92-privacy/#algorithmic-cruelty)
* [Ditching CAPTCHAs _and_ Improving Privacy](https://dltj.org/article/issue-92-privacy/#privacy-access-tokens)
* [When Privacy is a National Security Concern](https://dltj.org/article/issue-92-privacy/#geolocation-privacy)
* [A Privacy-in-the-Cloud Good News Story](https://dltj.org/article/issue-92-privacy/#icloud-encryption)
* [Facebook's Luck Running Out in the European Union](https://dltj.org/article/issue-92-privacy/#facebook-eu)

{{ thursday_threads_header() }}

## Algorithmic Cruelty {: #algorithmic-cruelty}
{{ thursday_threads_quote(href="https://www.theatlantic.com/ideas/archive/2022/10/can-you-hide-your-pregnancy-era-big-data/671692/",
 blockquote='<p>When I became pregnant, my partner and I, like many expectant individuals, opted not to tell our friends until after the first trimester. But I had an additional goal: for my friends to learn of my pregnancy before advertisers did. I&rsquo;m a health-privacy scholar, so I know that pregnant individuals are of particular interest to retailers because their purchasing habits change during pregnancy and after birth. Companies are eager to send targeted ads and capture a new customer base. In an attempt to avoid this spamming and, frankly, to see if it was possible, I endeavored to hide my private health status from the advertising ecosystem....</p><p>Yet, because of the lack of data privacy in the U.S., the day finally came when I lost my battle to keep my reproductive information private. I was sitting on my couch scrolling through social media when I saw it: an advertisement for diapers. It appeared the same week that we lost the pregnancy.</p>',
 versiondate="2022-10-18",
 versionurl="https://web.archive.org/20221019000813/https://www.theatlantic.com/ideas/archive/2022/10/can-you-hide-your-pregnancy-era-big-data/671692/",
 anchor="I Tried to Keep My Pregnancy Secret",
 post=", Anya E. R. Prince, The Atlantic, 10-Oct-2022") }}

Algorithms are cruel. 
In this article, the data miners and advertising conglomerates got to this person at precisely the wrong time. 
Eight years ago this month, my friend Eric Meyer {{ robustlink(href="https://meyerweb.com/eric/thoughts/2014/12/24/inadvertent-algorithmic-cruelty/", versionurl="https://web.archive.org/web/20141224215848/https://meyerweb.com/eric/thoughts/2014/12/24/inadvertent-algorithmic-cruelty/", versiondate="2014-12-24", title="Inadvertent Algorithmic Cruelty | Eric's Archived Thoughts", anchor="found the same thing") }} when Facebook posted a year-end memory video that prominently featured pictures of his daughter who died six months earlier. 
(Eric went on to {{ robustlink(href="https://web.archive.org/web/20160505192736/https://abookapart.com/products/design-for-real-life", versionurl="https://web.archive.org/web/20160505192736/https://abookapart.com/products/design-for-real-life", versiondate="2016-05-05", title="Design for Real Life | A Book Apart", anchor="write a book") }} with [Sara Wachter-Boettcher](https://www.sarawb.com/) about designing with compassion.) 
Data about us is being gathered up, aggregated, parsed, mischaracterized, and pulled out of context by systems we can't see or control, and it is still as true today as it was eight years ago.

## Ditching CAPTCHAs _and_ Improving Privacy {: #privacy-access-tokens}
{{ thursday_threads_quote(href="https://www.fastly.com/blog/private-access-tokens-stepping-into-the-privacy-respecting-captcha-less",
 blockquote='Earlier today at WWDC, Apple presented a demo of a new technology that allows users to leverage Fastly to seamlessly access content at FT.com with zero CAPTCHAs, all while respecting end-user privacy. At its core, Private Access Tokens present a privacy-respecting, anti-fraud and authorization framework. This blog post provides an overview of what it does and how developers can try it out with Fastly and Apple today.',
 versiondate="2022-07-22",
 versionurl="https://web.archive.org/web/20220627012029/https://www.fastly.com/blog/private-access-tokens-stepping-into-the-privacy-respecting-captcha-less",
 anchor="Private Access Tokens:",
 post=" stepping into the privacy-respecting, CAPTCHA-less future we were promised, Fastly blog, 8-Jun-2022") }}

We have the classic _"On the internet, nobody knows you're a dog"_ (or maybe a bot). 
Websites use CAPTCHAs—those click-all-the-stoplight widgets—to separate bots from humans. 
Not only are CAPtCHAs difficult for some to solve, the biggest is also run by an advertising-data-heavy company (Google). 
With some clever cryptography, there seems to be a privacy-aware way out of this problem.

## When Privacy is a National Security Concern {: #geolocation-privacy}
{{ thursday_threads_quote(href="https://www.bbc.com/news/world-middle-east-61879383",
 blockquote='A security vulnerability in the fitness app Strava allowed suspicious figures to identify and track security personnel working at secretive bases in Israel, a disinformation watchdog says. FakeReporter found that by uploading fake running "segments" a user could learn the identities and past routes of others active in the area, even if they had the strongest privacy settings.',
 versiondate="2022-07-22",
 versionurl="https://web.archive.org/web/20220627012026/https://www.bbc.com/news/world-middle-east-61879383",
 anchor="Strava app flaw revealed runs of Israeli officials at secret bases",
 post=", BBC, 21-Jun-2022") }}

One of the _Thursday Threads_ from 2014 was about [the emerging concern of mobile device apps reporting our movements to data aggregators](https://dltj.org/article/thursday-threads-2014w49/#p24188-nyt-oped). 
That is still a concern and one with far-reaching consequences. 
If the _military_ is having problems keeping this stuff secret, I'm not sure we civilians have much hope.
And the misuse of geo-location information goes beyond privacy; there is an {{ robustlink(href="https://arstechnica.com/tech-policy/2022/12/grandmother-sues-cop-who-wrongly-targeted-her-home-using-find-my-app/", versionurl="https://web.archive.org/web/20221207124747/https://arstechnica.com/tech-policy/2022/12/grandmother-sues-cop-who-wrongly-targeted-her-home-using-find-my-app/", versiondate="2022-12-07", title="Grandmother sues cop who wrongly targeted her home using &lquo;Find My&rquo; app | Ars Technica", anchor="article in Ars Technica this week") }} about police not understanding the limitations of geo-location data and terrorizing a retired woman in her home.

## A Privacy-in-the-Cloud Good News Story {: #icloud-encryption}
{{ thursday_threads_quote(href="https://www.washingtonpost.com/technology/2022/12/07/icloud-apple-encryption/",
 blockquote='After years of delay under government pressure, Apple said Wednesday that it will offer fully encrypted backups of photos, chat histories and most other sensitive user data in its cloud storage system worldwide, putting them out of reach of most hackers, spies and law enforcement.',
 versiondate="2022-12-07",
 versionurl="https://web.archive.org/20221208003147/https://www.washingtonpost.com/technology/2022/12/07/icloud-apple-encryption/",
 anchor="Apple says it will allow iCloud backups to be fully encrypted",
 post=", Washington Post, 7-Dec-2022") }}

Just yesterday, Apple announced that it will start encrypting the iCloud backups from mobile devices. 
This has long been a loophole in the privacy of Apple's mobile devices; while activities like chat messages may be encrypted end-to-end, they are available in the clear in backups on Apple's servers. 
Not everything will be encrypted in the backup, though; {{ robustlink(href="https://www.apple.com/newsroom/2022/12/apple-advances-user-security-with-powerful-new-data-protections/", versionurl="https://web.archive.org/web/20221208010102/https://www.apple.com/newsroom/2022/12/apple-advances-user-security-with-powerful-new-data-protections/", versiondate="2022-12-07", title="Apple advances user security with powerful new data protections | Apple", anchor="Apple says") }} that email, calendars, and contacts won't be encrypted so those tools can interoperate with third parties. 
That should be plenty for law enforcement to use (when they have the duly authorized search warrant).

## Facebook's Luck Running Out in the European Union {: #facebook-eu}
{{ thursday_threads_quote(href="https://pluralistic.net/2022/12/07/luck-of-the-irish/",
 blockquote='A leak from the European Data Protection Board reveals that the EU&rsquo;s top privacy regulator is about to overrule the Irish Data Protection Commission and declare Facebook&rsquo;s business model illegal, banning surveillance-based ads without explicit consent.',
 versiondate="2022-12-07",
 versionurl="https://web.archive.org/web/20221207175554/https://pluralistic.net/2022/12/07/luck-of-the-irish/",
 anchor="EU to Facebook, 'Drop Dead'",
 post=", Pluralistic, 7-Dec-2022") }}

Also yesterday is this essay from Cory Doctorow about a serious threat to Facebook from the European Union. 
Although Facebook has had favorable court rulings in the past from the Irish government's data protection board, those may be overruled by the continent-wide oversight body. 
Cory notes that GDPR, as envisioned, does not consider top-level checkboxes and approval-as-click-through-fine-print to be sufficient consent. 
"These uses have to be individually enumerated, and the user has to actively opt into giving up each piece of data and into each use of that data. That means that if you're planning to steal 700 pieces of information from me and then use it in 700 ways, you need to ask me 1,400 questions and get a 'Yes' to each of them."
Will Meta pull Facebook out of the EU? Or will it modify its data practices to conform to a court ruling that puts more power into the hands of the end users? (And what is the fine amount going to look like?)
Cory talks about this and the potential impacts beyond Facebook of such a ruling.

## Mittens' Calendar {: #mittens-calendar}
{{ image(width="700", localsrc="2022/2022-12-08-mittens-calendar.jpeg", alt="Photograph of a black cat in the arms of its owner. Held next to the cat is a page-a-day calendar with the title 'texts from mittens'. The picture of the cat on the calendar box resembles the cat being held.") }} 

For Christmas last year, the family got a page-a-day calendar with text messages between a cat named Mittens and its owner. 
Our Mittens had a striking resemblance, so we had to take this picture.

Let me know what privacy stories you recently encountered or remember from 2014. 
Just reply to this email (if you got it in newsletter form) or see my contact information to the left (if you are reading it on the website)