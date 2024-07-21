---
title: 'Refactoring DLTJ, Winter 2021 Part 3: "Serverless" Newsletter System'
modified: 2022-01-05T21:09:02-05:00
category: Linking Technologies
categories:
  - Meta Category
tags:
  - Amazon Web Services
---
So it has been quiet here for a couple of days.
Rest assured: the quietness comes from heads-down work, not from giving up.
Here are the refactor-DLTJ activities so far:

* [Ramp up automation for adding reading sources to Obsidian]({% post_url 2021-12-29-obsidian-journaling %})
* [Refactor the process of building this static website on AWS]({% post_url  2021-12-30-aws-amplify-jekyll %})
	* [Fix the webmentions cache, an unanticipated diversion]({% post_url 2021-12-31-fixing-webmentions %})
* Recreate the ability for readers to get updates by email (this post)
* [Turn the old DLTJ “Thursday Threads” concept into a newsletter]({% post_url 2022-01-06-refactoring-complete %})

Since New Years Day, I've been working on a way to send the contents of blog posts by email...commonly known nowadays as a newsletter. 
Years ago, I was using the Feedburner service to do that. 
Then Feedburner was bought by Google, and things were mostly okay for a while. 
Which is to say that most everything was working, and the things that weren't—[like HTTPS for custom RSS domain names]({% post_url 2019-01-09-proxy-feedburner-mybrand-cloudfront-edge-lambda %})—had workarounds. 
But last summer {% include robustlink.html href="https://developers.google.com/search/blog/2021/04/changes-to-feedburner" versionurl="https://web.archive.org/web/20220106013340/https://developers.google.com/search/blog/2021/04/changes-to-feedburner" versiondate="2022-01-05" title="" anchor="Feedburner-Google discontinued the distribution of blog posts by email" %}, which necessitated the need to buy or build my own email distribution system.

There are certainly "buy" options.
For instance, one might use {% include robustlink.html href="https://medium.com/creators" versionurl="ttps://archive.li/wip/ZXEYM" versiondate="2022-01-05" title="" anchor="Medium" %} for writing and distribution. 
But I've seen too many services come and go to come to rely on a business to be a good steward of my content. 
The {% include robustlink.html href="https://substack.com/for-bloggers" versionurl="https://web.archive.org/web/20220106013105/https://substack.com/for-bloggers" versiondate="2022-01-05" title="" anchor="Substack service" %}  has the same problem.
For a while I considered the {% include robustlink.html href="https://follow.it/intro" versionurl="https://archive.li/wip/8Upc2" versiondate="2022-01-05" title="" anchor="follow.it service" %}  as an alternative to Feedburner that included a newsletter-like add-on, but its "white label" service inserts the "follow.it" domain name in critical places where I would lose control over my list of subscribers.
(After all, I'm only able to do this cleanly because I kept control over my RSS feed by using "feeds.dltj.org" as a hostname.)

So I'm running it myself. 
I briefly considered {% include robustlink.html href="https://victoria.dev/blog/build-your-own-serverless-subscriber-list-with-go-and-aws/" versionurl="https://web.archive.org/web/20220105234454/https://github.com/knadh/listmonk" versiondate="2022-01-05"  anchor="listmonk" %}, but I don't know the Go programming language so that make troubleshooting and enhancing more of a challenge. 
Not readily spotting other alternatives, I created my own system using AWS tools, the {% include robustlink.html href="https://www.serverless.com/framework/docs" versionurl="https://web.archive.org/web/20220106014902/https://www.serverless.com/framework/docs" versiondate="2022-01-05" title="" anchor="Serverless.com framework" %}, and the Python programming language.
Thanks to a {% include robustlink.html href="https://www.marcolancini.it/2020/blog-serverless-mailing-list/" versionurl="https://web.archive.org/web/20211029010808/https://www.marcolancini.it/2020/blog-serverless-mailing-list/" versiondate="2021-10-29" title="Building a Serverless Mailing List in AWS | Marco Lancini" anchor="great outline by Marco Lancini" %} and {% include robustlink.html href="https://victoria.dev/blog/build-your-own-serverless-subscriber-list-with-go-and-aws/" versionurl="https://web.archive.org/20220105232949/https://victoria.dev/blog/build-your-own-serverless-subscriber-list-with-go-and-aws/" versiondate="2022-01-05" title="Build your own serverless subscriber list with Go and AWS | Victoria Drake" anchor="ideas from Victoria Drake" %}.

The [newsletter infrastructure software is on GitHub](https://github.com/dltj/serverless-mailing-list). 
It deserves a decent README file and some documentation to help others use it if they are so inclined. 
There are also a number of hard-coded areas that would need to be made more general. 
(See, for instance, [these couple of lines](https://github.com/dltj/serverless-mailing-list/blob/main/create_issue.py#L92-L94) that are used to pull out the body of the blog post for inclusion into the newsletter email.)

## But Why

I've been asked, {% include robustlink.html href="https://twitter.com/MikeTaylor/status/1476977509942104069" versionurl="https://web.archive.org/web/20211231181028/https://twitter.com/MikeTaylor/status/1476977509942104069" versiondate="2022-01-05" anchor="why do you go through all of this work instead of just hosting your blog on Wordpress.com" %}?
That is a reasonable question and it deserves a thoughtful response.

1. *I like control of my content.* My writings have always been stored on devices that I have a moderate amount of control over—first WordPress on a personal server in a co-location space, then WordPress on an Amazon Web Services (AWS) server, then as static files created by the Jekyll program and served up by AWS. (Side note, AWS isn't the only place my stuff lives—I've always kept a copy on my local machine with backups held off-site.)
1. *To keep my tech skills sharp.*  With a computer science undergrad degree and self-described, old-school hacker, I'd like to think I could dive into any system and figure out how to run it.  I've about given up on physical and data link layers (there was a time I made my own cables and configured building network equipment) and skills in the network and transport layers are getting quite stale (heard of the new {% include robustlink.html href="https://en.wikipedia.org/wiki/QUIC" versionurl="https://archive.li/wip/0RQbQ" versiondate="2022-01-05" anchor="QUIC protocol" %}?).  In my day job, the newish always-on, internet-grade infrastructure tools are becoming ever more mysterious.  I want to learn a few new things just to keep up the practice of learning.
1. *Privacy and the Common Good still matter.*  My blog and this newsletter technology use no tracking technology.  Aside from comments, I can't tell who or how many are reading my blog.  With the newsletter system, there are no tracking pixels or link shorteners that are detecting what you read.  And this content is offered for free.  Beyond the technical expertise, the technology running the blog and newsletter is really cheap.  The blog looks to be about 50¢ a day—much lower than expected; we'll see about the newsletter, but I don't expect it to be more than a couple of dollars a month.

So that's my thinking at this point. 
The technology surrounding DLTJ has certainly changed over the years, and I don't expect it will remain static for decades on end. 
Time, technology advancement, and life choices can certainly change the calculus in the future.

Keep an eye out for the newsletter tomorrow, posted here on DLTJ and sent by email. 
If you'd like to subscribe to _DLTJ Thursday Threads_ by email, head on over to [newsletter.dltj.org](https://newsletter.dltj.org/).