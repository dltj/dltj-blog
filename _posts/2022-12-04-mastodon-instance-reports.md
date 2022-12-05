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
notetext=''
%}

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

