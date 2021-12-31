---
title: "Refactoring DLTJ, Winter 2021 Part 2: Adopt AWS Amplify"
categories:
  - Meta Category
tags:
  -  Amazon Web Services
  -  jekyll
  -  static website
---
Look at that! 
Progress is being made down the list of to-dos for this blog in order to start the new year on a fresh footing. 
As you might recall from the last blog post, I set out to do some upgrades across the calendar year boundary:

* [Ramp up automation for adding reading sources to Obsidian](/article/obsidian-journaling)
* Refactor the process of building this static website on AWS (this post)
* Recreate the ability for readers to get updates by email
* Turn the old DLTJ "Thursday Threads" concept into a newsletter

DLTJ is a "static site" blog, meaning that the page you are reading right now is a straight-up HTML file. 
This page is converted from the simple {% include robustlink.html href="https://www.markdownguide.org/basic-syntax/" versionurl="https://web.archive.org/web/20211229080555/https://www.markdownguide.org/basic-syntax/" versiondate="2021-12-30" title="Basic Syntax | Markdown Guide" anchor="Markdown format" %} to HTML by the {% include robustlink.html href="https://jekyllrb.com/" versionurl="https://web.archive.org/web/20211229202427/https://jekyllrb.com/" versiondate="2021-12-30" title="Jekyll homepage" anchor="Jekyll" %} program. 
The DLTJ blog used to be based on WordPress, which meant a server was always running to dynamically generate each webpage out of a database. 
(If you go back in the DLTJ archives you'll see notes on top of pages that were part of the automatic conversion from WordPress to Markdown.)
That WordPress server was quite costly to have constantly run for a small blog. 
(Yes, it is possible to pay someone a small amount to host your WordPress blog for you, but I'm a do-it-yourself kind of person.)
So [at the end of 2017 I migrated the site](/article/dltj-in-a-newwwyear/) to [Markdown stored in a GitHub repository](https://github.com/dltj/dltj-blog) with the Jekyll conversion and content delivery through Amazon Web Services (AWS). 

Serving up static web pages from AWS S3/CloudFront is really simple. 
Processing the Markdown on GitHub into HTML via Jekyll on AWS is more complicated, and that process was something that I wanted to happen automatically every time I published a change to GitHub.
I ended up hand-crafting about 650 lines of an AWS CloudFormation configuration file plus a few dozen lines of Python in some AWS Lambda functions. 
It worked, but it was fragile and very hard to maintain. 

That was in 2017 and technology marches on; now AWS has a service that does all of the automation for you. 
Called {% include robustlink.html href="https://aws.amazon.com/amplify/" versionurl="" versiondate="2021-12-30" title="AWS Amplify homepage" anchor="Amplify" %}, it bundles together a bunch of other AWS tools to help developers to create "full-stack web and mobile apps." 
The Amplify tools are really quite overkill for a static website, but {% include robustlink.html href="https://aws.amazon.com/getting-started/hands-on/host-static-website/" versionurl="https://web.archive.org/20211230214745/https://aws.amazon.com/getting-started/hands-on/host-static-website/" versiondate="2021-12-30" title="Host a Static Website [using AWS Amplify; tutorial] | Amazon Web Services" anchor="building a static website" %} is one of the hands-on "Getting Started" examples that AWS offers.
For a static website, Amplify handles:

1. creating an S3 bucket and CloudFront distribution to store and serve up the content
1. provisioning a webhook API that notifies AWS to start the content building process and adds that webhook to the GitHub repository 
1. setting up the CodeBuild process for Jekyll to generate the static web pages
1. creating the HTTPS security certificate and adding the appropriate DNS entries to the domain

All of the stuff I was doing in that 650-line CloudFormation file.
(Plus Amplify has a lot more interesting features built into the service.)

{% include image.html 
  wpsrc="2021/AWS-Amplify-Console-Screenshot.svg"
  caption="AWS Amplify Console"
  alt="Screen capture the AWS Console page for the Amplify Service."
  width="99%"
%}

## One Problem: Getting the Correct Version of Ruby
Now for the two-hour detour. 
At least one of the Jekyll Gems I'm using to build this site requires Ruby version 2.6 or higher. 
The AWS CodeBuild container used by Amplify was defaulting to Ruby version 2.4, though, and my initial attempts to configure Amplify to use the higher version (setting an environment variable) didn't work.
One answer that I found seemed to imply that {% include robustlink.html href="https://github.com/aws-amplify/amplify-console/issues/1146#issuecomment-975908831" versionurl="https://web.archive.org/web/20210119205725/https://github.com/aws-amplify/amplify-console/issues/1146" versiondate="2021-12-30" title="'Some applications will not use ruby version specified in Gemfile and fail to build, while others are fine' | GitHub issue on aws-amplify/amplify-console" anchor="I needed to build my own custom Docker image" %}, so I [started to make one](https://github.com/dltj/jekyll-serve-amplify/) using the {% include robustlink.html href="https://docs.aws.amazon.com/amplify/latest/userguide/custom-build-image.html#setup" versionurl="" versiondate="2021-12-30" title="Custom build images and live package updates | AWS Amplify Documentation" anchor="AWS instructions" %}.
I got pretty far down that path before discovering that this blog needs not only the Ruby runtime but also a JavaScript runtime.
(Another one of the Jekyll Gems calls out to a JavaScript function.)
At that point, I went back to searching for an answer that used the AWS-supplied Docker image.

The real solution came in {% include robustlink.html href="https://stackoverflow.com/questions/56444337/how-to-change-node-version-in-provision-step-in-amplify-console/56453511#56453511" versionurl="https://web.archive.org/web/20210119205725/https://github.com/aws-amplify/amplify-console/issues/1146" versiondate="2021-12-30" title="'How to change Node Version in Provision Step in Amplify Console' | Stack Exchange" anchor="an answer about using a different version of Node in Amplify" %}, which was to add a command to the `preBuild` and `build` steps to switch Ruby versions:

```yaml
preBuild:
  commands:
    - rvm use $VERSION_RUBY_2_6
    - bundle install --path vendor/bundle
build:
  commands:
    - rvm use $VERSION_RUBY_2_6
    - bundle exec jekyll build --trace
````

After that, everything built perfectly.

{% include note.html notetext='Jumping in here a day later to say there was another problem...the webmention cache was left behind in the old CodeBuild configuration so <a href="/article/fixing-webmentions">I had to fix it</a>."' %}

## Downsides: Lots of Invisible AWS Services and Poor Pricing Comparison
One problem with using AWS Amplify is that the underlying AWS services—S3 bucket, CloudFront distribution, CodeBuild instance, etc.—are not visible in the AWS Console. 
In other words, you can't go to the CloudFront console page and see the configuration.
More to the point, the cost of the underlying services seems to be aggregated into a relatively flat billing structure; {% include robustlink.html href="https://aws.amazon.com/amplify/pricing/" versionurl="https://web.archive.org/web/20211123052553/https://aws.amazon.com/amplify/pricing/" versiondate="2021-12-30" title="AWS Amplify Pricing" anchor="Amplify's costs" %} are:

* 1¢ per minute it takes to build the site (the blog takes between 2 and 3 minutes to build for each change)
* 2.3¢ per GB of data stored per month (this whole blog is about 300MB)
* 15¢ per GB of data served to readers (it looks like my blog is about 100GB/month)

So all told I think this is going to be $15 to $20 per month, with the biggest piece of that being the outbound bandwidth. 
Under the old system, last month my outbound CloudFront bandwidth cost $0.59, and this month will be zero because {% include robustlink.html href="https://aws.amazon.com/blogs/aws/aws-free-tier-data-transfer-expansion-100-gb-from-regions-and-1-tb-from-amazon-cloudfront-per-month/" versionurl="https://web.archive.org/web/20211219065722/https://aws.amazon.com/blogs/aws/aws-free-tier-data-transfer-expansion-100-gb-from-regions-and-1-tb-from-amazon-cloudfront-per-month/" versiondate="2021-12-30" title="AWS Free Tier Data Transfer Expansion – 100 GB From Regions and 1 TB From Amazon CloudFront Per Month | AWS News Blog" anchor="Amazon announced that the first 1TB of CloudFront data is now free" %}.
Hmmm—now that I'm pricing this out, maybe I'll need to go back to the old way. 
[I asked a question](https://repost.aws/questions/QUyy_CdDAKQ5Giy5ikzA0-0Q/does-amplify-outbound-bandwidth-fall-under-the-new-1-tb-month-free-tier-data-transfer-expansion-announced-for-cloud-front) on AWS' forums to see if this really holds true. 
Of course, I can also just wait a little while and see what my AWS bills look like.

$10 to $15 a month is quite a lot—I'll keep that old 650-line CloudFormation file around to see if I end up reverting to that method. 
Overall, though, I'm pleased with how this turned out.
When I have a better answer on the costs associated with Amplify, I'll try to remember to come back here and update this post.

Tomorrow...with luck...recreating the email notification/delivery service!