---
title: DLTJ in another #NEWWWYEAR
modified: 2018-12-31T19:49:51-05:00
category: Meta Category
categories:
- Meta Category
tags:
- WordPress
- Amazon Web Services
- jekyll
---
Well, we have reached the end of another arbitrary orbit around our small unregarded yellow sun[^1], and this primitive ape-descended life form[^2] is looking back on this blog's past twelve months.  Not much to show for it -- this'll be just the third blog post this year.

[^1]: With apologies to Douglas Adams for mangling his [opening paragraph](https://www.goodreads.com/quotes/54481-far-out-in-the-uncharted-backwaters-of-the-unfashionable-end).
[^2]: _Ibid_

And yet it started with [so much excitement](https://dltj.org/article/dltj-in-a-newwwyear/) over a refresh of the technology behind DLTJ. 
This was my plan:

> 1. I'll start January 1.
> 1. I'll convert 'dltj.org' from WordPress to a static site generator (probably Jekyll) with a new theme.
> 1. My deadline is January 13 (with a conference presentation in between the start and the end dates).
> 
> Along the way, I'll probably package up a stack of Amazon Web Services components that mimic the behavior of GitHub pages with some added bonuses (standing temporary versions of the site based on branches, supporting HTTPS for custom domains, integration with GitHub pull request statuses).  I'll probably even learn some Ruby along the way.

So the blog did get converted from WordPress to Jekyll, and all of the old posts were brought over as HTML-looking things with significant YAML headers at the top of each file.
That was good. [^3]

There were some pieces left missing, notably the short URLs that were based on the WordPress post number were never recreated into redirects.
That was bad. [^4]

I also did a lot of work on an Amazon Web Services CloudFormation setup that uses a GitHub commit hook to fire off a process of automatically rebuilding the website for every commit.
That was ugly; 653 lines of CloudFormation YAML ugly. [^5]

[^3]: Now apologizing to Sergio Leone for twisting [his spaghetti western film title](https://www.imdb.com/title/tt0060196/).
[^4]: _Ibid_
[^5]: _Ibid_

So what do I want to do with DLTJ this year?  Sort of like a list of New Year's resolutions?  Well, this is what I'm thinking:

1. Write more blog posts.
1. Do some enhancements to the underlying code -- like address the old short URL redirects.  I'd also like to build in some diff displays for posts based on the underlying Git files, and maybe even implement a [Memento](http://mementoweb.org/about/) TimeMap based on the Git history.  Anyone done something like that yet.
1. Learn [Serverless](https://serverless.com/) and reimplement the ugly CloudFormation template.

Check back with me in a year and see how I did!
