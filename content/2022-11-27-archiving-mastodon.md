---
title: 'With Mastodon on the Rise, Who Archives the Digital Public Square?'
modified: 2022-11-27T19:35:54-05:00
category: Raw Technology
categories:
- Raw Technology
tags:
- Twitter
- Mastodon
- digital preservation
---

{{ image(float="right", width="350", localsrc="2022/2022-11-27-dall-e.png", caption="DALL*E prompt: photorealistic waves of twitter logos and mastodon logos crashing onto a sandy beach", alt="DALL•E generated image", ahref="https://labs.openai.com/s/mycXvF0QGOWiSkQQZ9HllVTK") }} 

Much has been made about the differences between Twitter and Mastodon: the challenge of finding a home for your account (and the corresponding differences between your “local” timeline and your “global” timeline), the intentional antiviral design choices (no quote-tweets and a narrow search system), and the more-empowering block and mute features. 
A recent article in *MIT Technology Review* about {{ robustlink(href="https://www.technologyreview.com/2022/11/11/1063162/twitters-imminent-collapse-could-wipe-out-vast-records-of-recent-human-history/", versionurl="https://web.archive.org/web/20221125215213/https://www.technologyreview.com/2022/11/11/1063162/twitters-imminent-collapse-could-wipe-out-vast-records-of-recent-human-history/", versiondate="2022-11-27", title="Twitter’s potential collapse could wipe out vast records of recent human history | MIT Technology Review", anchor="the potential loss to history if Twitter goes away") }} had me thinking of another one difference: a Mastodon-filled world changes expectations for archiving this kind of primary source material. 

## Think Bigger Than Mastodon
{: bigger-than-mastodon }

Let's set some common ground. 
"{{ robustlink(href="https://joinmastodon.org/", versionurl="https://web.archive.org/web/20221127085820/https://joinmastodon.org/", versiondate="2022-11-27", title="Mastodon homepage", anchor="Mastodon") }} " is being used here as a shortcut for the growing federation of servers that follow the ActivityPub protocol—the "fediverse".
Most people caught up in the migration away from Twitter are looking for a "Twitter-equivalent", and the option that has caught the popular imagination is Mastodon. 
As we view the fediverse digital public square, we could just as well be talking about Mastodon forks like {{ robustlink(href="https://github.com/hometown-fork/hometown/wiki", versionurl="https://web.archive.org/web/20221108050909/https://github.com/hometown-fork/hometown/wiki", versiondate="2022-11-27", title="Hometown wiki homepag", anchor="Hometown") }}. 
We should also include in the genre-specific ActivityPub software like {{ robustlink(href="https://pixelfed.social/site/about", versionurl="https://web.archive.org/web/20221115012936/https://pixelfed.social/site/about", versiondate="2022-11-27", title="About Pixelfed", anchor="Pixelfed") }} (for photographers, [me there](https://pixelfed.social/dltj)), {{ robustlink(href="https://joinbookwyrm.com/", versionurl="https://web.archive.org/web/20221125055911/https://joinbookwyrm.com/", versiondate="2022-11-27", title="Bookwyrm homepage", anchor="Bookwyrm") }} (for book groups and reader commentary, [me there](https://bookrastinating.com/user/dltj)), [Funkwhale](https://funkwhale.audio/) (for music), and [write.as](https://write.as) (for long-form articles).
Although Mastodon is getting the most traction right now, the question of archiving the digital public square is bigger than just Mastodon...just keep that in mind as you read below. 

## Twitter Archiving Challenges
{: twitter-archiving-challenges }

As the *MIT Technology Review* article points out, there are challenges to archiving Twitter.

> For eight years, the US Library of Congress took it upon itself to maintain a public record of all tweets, but it stopped in 2018, instead selecting only a small number of accounts’ posts to capture.  “It never, ever worked,” says William Kilbride, executive director of the Digital Preservation Coalition. The data the library was expected to store was too vast, the volume coming out of the firehose too great. “Let me put that in context: it’s the Library of Congress. They had some of the best expertise on this topic. If the Library of Congress can’t do it, that tells you something quite important,” he says.

The challenges include that of scale:

> [In January 2013] We now have an archive of approximately 170 billion tweets and growing. The volume of tweets the Library receives each day has grown from 140 million beginning in February 2011 to nearly half a billion tweets each day as of October 2012.
>  - {{ robustlink(href="https://blogs.loc.gov/loc/2013/01/update-on-the-twitter-archive-at-the-library-of-congress/", versionurl="https://web.archive.org/web/20221123093719/https://blogs.loc.gov/loc/2013/01/update-on-the-twitter-archive-at-the-library-of-congress/", versiondate="2022-11-27", title="Update on the Twitter Archive at the Library of Congress | Library of Congress blog", anchor="Update on the Twitter Archive at the Library of Congress") }}, Library of Congress blog, January 2013.

And also of scope—the Library does not receive the multimedia parts of tweets.
As the {{ robustlink(href="https://blogs.loc.gov/loc/files/2017/12/2017dec_twitter_white-paper.pdf", versionurl="https://web.archive.org/web/20221122151051/https://blogs.loc.gov/loc/files/2017/12/2017dec_twitter_white-paper.pdf", versiondate="2022-11-27", title="Update on the Twitter Archive at the Library of Congress, December 2017 whitepaper [PDF]", anchor="whitepaper attached to the Update on the Twitter Archive at the Library of Congress") }} says:

> The Library only receives text. It does not receive images, videos or
linked content. Tweets now are often more visual than textual, limiting the value
of text-only collecting.

Both points speak to the changing nature of Twitter from when its origins as an extension of text messaging geared towards a U.S. audience into a world-wide multimedia platform. 
Michael Zimmer wrote in great detail about these challenges and the issues of processing, privacy, and user consent  for _First Monday_ in 2015. 
The {{ robustlink(href="https://blogs.loc.gov/loc/files/2010/04/LOC-Twitter.pdf", versionurl="https://web.archive.org/web/20220912101153/https://blogs.loc.gov/loc/files/2010/04/LOC-Twitter.pdf", versiondate="2022-11-27", title="Twitter Gift Agreement to the Library of Congress [PDF]", anchor="donor agreement") }} between Twitter and the Library of Congress is silent on the matters of privacy and user consent as well.

On December 26, 2017, the Library of Congress {{ robustlink(href="https://blogs.loc.gov/loc/2017/12/update-on-the-twitter-archive-at-the-library-of-congress-2/", versionurl="https://web.archive.org/web/20221123225408/https://blogs.loc.gov/loc/2017/12/update-on-the-twitter-archive-at-the-library-of-congress-2/", versiondate="2022-11-27", title="Update on the Twitter Archive at the Library of Congress | Library of Congress blog", anchor="announced") }} that it was no longer collecting a comprehensive archive of tweets as of January 1, 2018. 
What is at the Library now has known limitations in its comprehensiveness, and we may not see open access to that archive in our lifetime because of privacy concerns. 

The *MIT Technology Review* article talks about the loss to historians, human rights lawyers, and researchers using "open source intelligence" — that which is openly published in the digital public square. 
Given that we are facing this moment of reckoning as Twitter may be on the brink of disappearing and people are finding community on Mastodon, should we consider an explicit archiving role for the fediverse?

## Mastodon Archiving Challenges
{: mastodon-archiving-challenges }

With Twitter's recent upheaval and the migration to Mastodon, I've seen mentions of how Twitter was unique to its time. 
At Twitter's public unveiling in March 2006, the only way to interact with Twitter was through text messages.
Apple would introduce the iPhone the following year, and it was a year after that when an {{ robustlink(href="https://en.wikipedia.org/wiki/Tweetie", versionurl="https://en.wikipedia.org/w/index.php?title=Tweetie&oldid=1096875704", versiondate="2022-11-27", title="Tweetie | Wikipedia", anchor="app for iPhone would launch") }}. 
Twitter's growth was jumpstarted by the {{ robustlink(href="https://www.wired.com/2007/03/twitter-is-ruling-sxsw/", versionurl="https://web.archive.org/web/20221118041346/https://www.wired.com/2007/03/twitter-is-ruling-sxsw/", versiondate="2022-11-27", title="Twitter is Ruling SXSW | Wired", anchor="influx of users at the 2007 South-by-Southwest (SXSW) conference") }} as attendees publicly shared their experiences in real time in a way they could not have previously. 
The combination of an experience that straddled mobile and desktop devices and the ability of the company to scale to meet the demand made this Twitter's moment. 
A moment that it ran with for the next 15 years. 

Mastodon is different. 
Conceptually, there isn't one "Mastodon" (like there is one "Twitter"); there are many little Mastodons that have a standard way of talking to each other.
(Yes, this is where the "{{ robustlink(href="https://www.w3.org/TR/activitypub/", versionurl="https://web.archive.org/web/20221127093116/https://www.w3.org/TR/activitypub/", versiondate="2022-11-27", title="ActivityPub | W3C Recommendation", anchor="ActivityPub") }}" standard becomes key.) 
And crucially, these many little Mastodons are run by individual users and organizations. 
We witnessed firsthand the difficulties these Mastodons had in scaling to meet the demand from the outflow of Twitter users.
(Many of the larger Mastodon instances halted or greatly limited new user registrations in November 2022.)

Now consider what would be needed to construct a "Mastodon Digital Archive" similar in scope to how Twitter donated its timeline of tweets to the Library of Congress. 
At the very least, it would mean contacting each of these Mastodon instances to get copies of their databases and feeds of ongoing posts. 
And even if there was a mechanism to do that, internet users are more aware about rights to their digital content (or at least more savvy of their digital footprint); some sort of user consent would likely be needed.

Inherent in the structure of independent Mastodon instances is the fact that there isn't a central point of aggregation, and that is seen by the broader community as a good thing.
(The most common reason I've heard is that the lack of a search tool makes finding the discussion of controversial topics harder and decreases the likelihood of bad actors "dogpiling" into a conversation.) 
There have been attempts to aggregate content for a search engine, but Mastodon administrators quickly ban those kinds of ActivityPub peers. 
Creating an archive of Mastodon posts will likely run into the same issues. 

## Do We Want a Digital Public Square Archive?

{: digital-public-square-archive }
Let's step further back: should there be an archive of the digital public square? 
Physical public squares don't have comprehensive archives. 
The fact that a digital public square is made up of ones and zeros in files and databases makes it at least conceivable. 
(Setting aside the technical challenges that the Library of Congress faced with the Twitter archive; with progress in technology and techniques, having such an archive will likely be technically possible at some point.) 
As the MIT Technology Review article points out, there are benefits to such an archive. 
Perhaps archivists and historians can help aim us toward ideas that make sense for this new public space.
