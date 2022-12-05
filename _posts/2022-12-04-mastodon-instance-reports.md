---
title: "Mastodon Instance Operators Report on the Impact of the #TwitterMigration"
categories:
- Raw Technology
tags:
- Mastodon
---

A number of Mastodon operators have started to report the impact of the #TwitterMigration on their instances. 
I started gathering these because I was curious about what it takes to run a public or semi-public Mastodon instance. 
These reports are full of those kinds of details, but they also describe evolutions of policy and operations that are just as interesting. 
If you see other reports (or have posted a report of your own Mastodon instance), please tag me at [@dltj@code4lib.social](https://code4lib.social/@dltj) and I'll add it to this list.

{% include note.html 
notetext='There is now a <a href="https://github.com/dltj/dltj-blog/pull/14">branch and pull request</a> on GitHub where you can suggest changes to this list and/or subscribe to notifications for updates. <a href="https://rss-bridge.bb8.fun/?action=display&bridge=GithubIssueBridge&context=Issue+comments&i=14&u=dltj&p=dltj-blog&format=Html">Updates to the page</a> are also available via <a href="https://rss-bridge.bb8.fun/">RSS-Bridge</a>.'
%}

## mindly.social
{: #mindly}

{% include thursday-threads-quote.html
blockquote='Since April of this year I&lsquo;ve been running my own Mastodon server and 3 days ago we hit 100 users which was a huge milestone for my tiny little server... and then all of a sudden something happened, the other Mastodon servers started to get full and new users were looking for homes. Less than 72 hours after being excited for hitting 100 users we hit 10,000 users.'
href="https://kujoe.blog/2022/11/running-a-mastodon-server-part-1"
versionurl="https://web.archive.org/web/20221205152349/https://kujoe.blog/2022/11/running-a-mastodon-server-part-1"
versiondate="2022-12-05"
anchor="Running a Mastodon server - Part 1?"
post=', KuJoe&lsquo;s blog, 29-Nov-2022'
%}

Includes sections for:

- Statistics for activity growth
- Process for managing growth (technical)

## chaos.social
{: #chaos}

{% include thursday-threads-quote.html
blockquote='The past month has changed the Fediverse, and, by extension, our instance. We&lsquo;ve continued as normal (apart from limiting sign-ups) to give ourselves time to figure out which changes were only temporary, what seems to be changed for good, and how to react. A month seems ample time, and here we are with a set of changes in how chaos.social will work in the future.'
href="https://blog.chaos.social/2022/11/29/changes"
versionurl="https://web.archive.org/web/20221205150718/https://blog.chaos.social/2022/11/29/changes"
versiondate="2022-12-05"
anchor="Rule changes, closed sign-ups, and more"
post=', chaos.social blog, 29-Nov-2022'
%}

Includes sections for:

- Statistics for activity growth
- Process for managing growth (new user moderation, instance rules)

{% include thursday-threads-quote.html
blockquote='I was going to write an article for a while now, but there was too much work to do with the latest influx. Together with my co-admin @rixx we run the chaos.social instance. As of writing this, we are one of the biggest and most active instances on the fediverse and one of the oldest mastodon instances, starting mid of April 2017. For the last 5 years everything was simple, one VM with 10 cores, 500GB NVMe SSD Storage and 32GB RAM. This VM did everything from the database to the webserving. Then Musk happened.'
href="https://leah.is/posts/scaling-the-mastodon/"
versionurl="https://web.archive.org/web/20221204201002/https://leah.is/posts/scaling-the-mastodon/"
versiondate="2022-12-05"
anchor="Scaling the Mastodon"
post=', Leahs Gedanken&lsquo; blog, 2-Dec-2022'
%}

Includes sections for:

- Infrastructure, including breakout of server functions
- Process for managing growth (technical)


## Scaling Mastodon
{: #scaling-mastodon}

{% include thursday-threads-quote.html
blockquote='This is honestly a very hastily written selection of various snippets, with text extracted, and notes. No real editing thought was put into this, so I hope it&lsquo;s not too confusing. This blog post will be kept up to date as I find out more information and publish my findings. It&lsquo;s currently organized in no particular order with a bunch of micro fragment thoughts split out in a row.'
href="https://hazelweakly.me/blog/scaling-mastodon/"
versionurl="https://web.archive.org/web/20221204181502/https://hazelweakly.me/blog/scaling-mastodon/"
versiondate="2022-12-05"
anchor="Scaling Mastodon: The Compendium"
post=', Hazel Weakly'
%}

Includes sections for:

- Process for managing growth (technical)


## Metalhead.club
{: #metalhead}

{% include thursday-threads-quote.html
blockquote='Mastodon has recently gained popularity amongst tech-savvy users after Elon Musk has bought Twitter. With November&lsquo;s wave of new Mastodon users, many servers experienced mayor problems with their performance - so did metalhead.club, the Mastodon instance that I&lsquo;m hosting myself. Here&lsquo;s how I tackled performance issues on metalhead.club.'
href="https://thomas-leister.de/en/scaling-up-mastodon/"
versionurl="https://web.archive.org/web/20221205145841/https://thomas-leister.de/en/scaling-up-mastodon/"
versiondate="2022-12-05"
anchor="Scaling up your Mastodon Sidekiq workers for better performance"
post=', Thomas Leister&lsquo;s blog, 6-Nov-2022'
%}

Includes sections for:

- Process for managing growth (technical)


## Mastodon.ART
{: #art}

{% include thursday-threads-quote.html
blockquote='The steep line itself is when I realised that doing it that way actually gave us less control over new user numbers, so we went back to &lsquo;anyone can request an account but accounts need to be approved by a mod&rsquo;. This was about the time that big news sites had started reporting people were leaving Twitter for Mastodon, and they were all linking to joinmastodon.org, where we were one of three art instances listed and the biggest one by far... We had 2000 new user accounts placed in the approval queue that day. These weren&lsquo;t approved accounts, so they weren&lsquo;t logged on and using .art - so they weren&lsquo;t contributing much (aside from the verification emails being sent out) to server activity. Still, server activity skyrocketed.'
href="https://www.patreon.com/posts/update-on-costs-74379258"
versiondate="2022-12-05"
anchor="Update on costs & expansion plans"
post=', Masto Art on Patreon, WelshPixie, 8-Nov-2022'
%}

Includes sections for:

- Statistics for activity growth
- Process for managing growth (new user moderation)
- Financials/fundraising
- Governance changes (new moderators, etc)

See also:

- [26-Apr-2022](https://www.patreon.com/posts/after-wave-65616461): Statistics for activity growth
- [9-Nov-2022](https://www.patreon.com/posts/on-our-policy-74436103), [10-Nov-2022](https://www.patreon.com/posts/silencing-social-74474015), [10-Nov-2022](https://www.patreon.com/posts/oh-well-74495239): Federation policy
- [22-Nov-2022](https://www.patreon.com/posts/server-status-74989836): Financials/fundraising

## Fosstodon (April 2022)
{: #fosstodon-april}

{% include thursday-threads-quote.html
blockquote='If you haven&lsquo;t heard, Elon Musk recently agreed a deal to buy Twitter for a whopping $44bn. That cause a little turmoil over in Twitter land, which resulted in expats coming over to Mastodon in their droves. Because we&lsquo;re one of the biggest technology focussed instances on the Fediverse, a lot of people requested an account on Fosstodon. As you can see from the graphs below, the spike in users from Twitter made our usual activity almost flat line. This effectively resulted in a sustained DDoS that lasted for around 36 hours. As you can imagine, that was a lot of fun for myself and the team. Here&lsquo;s the details of what happened during those 36 hours…'
href="https://hub.fosstodon.org/elon-twitter-post-mortem/"
versionurl="https://web.archive.org/web/20221205142534/https://hub.fosstodon.org/elon-twitter-post-mortem/"
versiondate="2022-12-05"
anchor="Twitter, Elon & Fosstodon - A Post-Mortem"
post=', Fosstodon Hub, Kev Quirk, 29-Apr-2022'
%}

Includes sections for:

- Statistics of activity growth
- Process for managing growth
- Financials/fundraising


## Fosstodon (November 2022)
{: #fosstodon-november}

{% include thursday-threads-quote.html
blockquote='Woooooh! It&lsquo;s been a crazy few weeks at Fosstodon HQ. If you&lsquo;ve been living under a rock (or are just not interested) Elon Musk, or better known as Melon Tusk on the fediverse, has taken over Twitter and looks to be on a mission to ruin the platform even more. Because of this, people have been flocking to Mastodon in their droves, and since Fosstodon is one of the biggest tech-focussed instances on the fediverse, we&lsquo;ve seen A LOT of that traffic.'
href="https://hub.fosstodon.org/fosstodon-vs-twitter-round-2/"
versionurl="https://web.archive.org/web/20221205143403/https://hub.fosstodon.org/fosstodon-vs-twitter-round-2/"
versiondate="2022-12-05"
anchor="Fosstodon vs Twitter - Round 2"
post=', Fosstodon Hub, Kev Quirk, 13-Nov-2022'
%}

Includes sections for:

- Statistics of activity growth
- Financials/fundraising


## Mastodon Canada
{: #mastodon-canada}

{% include thursday-threads-quote.html
blockquote='The instance grew from less than 60 users to what is now 24 500 users in the span of just two weeks. It went from an experiment to a service demanding significant infrastructure, moderation, and governance. I want to offer a warm welcome to everyone and thanks for their patience as I bolstered Mastodon Canada with the necessary server capacity to handle the load.'
href="https://news.mstdn.ca/state-of-the-instance-nov-2022/"
versionurl="https://web.archive.org/20221205023822/https://news.mstdn.ca/state-of-the-instance-nov-2022/"
versiondate="2022-12-04"
anchor="State of the Instance - Nov 2022"
post=', Mastodon Canada, Chad Ohman, 3-Dec-2022'
%}

Includes sections for:

- Infrastructure (Digital Ocean), including breakout of server functions
- Process for managing growth
- Governance changes (new moderators, etc)
- Financials/fundraising
- Future plans

## Hachyderm
{: #hachyderm}

{% include thursday-threads-quote.html
blockquote='Hachyderm has reached 30,000 users. A ‘small sized’ service in regard to scale. However, in the process we have hit very familiar ‘medium sized’ scale problems which caused us to migrate our services out of my basement. This is the outage report, post mortem, and high level overview of the process of migrating to Hetzner in Germany. From observation to production fixes. This is the story.'
href="https://community.hachyderm.io/blog/2022/12/03/leaving-the-basement/"
versionurl="https://web.archive.org/20221205023756/https://community.hachyderm.io/blog/2022/12/03/leaving-the-basement/"
versiondate="2022-12-04T21:37:54"
anchor="Leaving the Basement"
post=', Hachyderm Community, Kris Nóva, 3-Dec-2022'
%}

Includes sections for:

- Infrastructure (was: basement; now: Hetzner)
- Process for managing growth
- Postmortem(s) on outages caused by growth

## Cloud Island (New Zealand)
{: #cloud-island}

{% include thursday-threads-quote.html
blockquote='November was a heck of a time for Cloud Island, and the Fediverse as a whole. With the Twitter purchase, the Fediverse as a whole saw a massive increase in use and traffic. Cloud Island is seeing a 15x sustained increase in traffic on Sidekiq, which is the behind-the-scenes processing layer that interacts with the rest of the Fediverse. Cloud Island is seeing 1700% more interactions through November than in October. And, finally a 12.5x increase in the amount of bandwidth being used from October to November. In October, we used about 100GB of bandwidth. In November, we used 1.25TB of bandwidth.'
href="https://www.patreon.com/posts/cloud-island-75379795"
versiondate="2022-12-04"
anchor="Cloud Island November"
post=', Cloud Island on Patreon, Aurynn Shaw, 1-Dec-2022'
%}

Includes sections for:

- Infrastructure (Catalyst Cloud), including breakout of server functions
- Financials

