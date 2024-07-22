---
title: Proxying FeedBurner MyBrand for HTTPS with CloudFront and Lambda at Edge
modified: 2019-01-09T22:07:47-05:00
category: Meta Category
categories:
- Meta Category
tags:
- WordPress
- Amazon Web Services
- rss
- feedburner
---
So I'm paying more attention to the <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym></i> blog now, and one of the things I quickly noticed is that the Atom syndication feed was broken.
Or, at least modern web clients would refuse to retrieve the feed.
The problem turned out to be not with the feed file, but the web client refusing to connect to the server to retrieve it.
The root cause was turning on [`HTTP Strict-Transport-Security` (HSTS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) for the "dltj.org" domain sometime in the middle of the year last year.

I had done the work of moving all of the resources used by the dltj.org blog to HTTPS over the summer, so I turned on the HSTS header:

```plaintext
strict-transport-security: max-age=31536000; includeSubDomains; preload
```

The practical impact of this header is to tell a web client (such as a browser) to use HTTPS only when connecting to this particular domain name.
The `includeSubDomains` attribute tells the web client to apply this rule to _all_ domains under `dltj.org`, which would include the `feeds.dltj.org` domain where the syndication feed lives.
The problem was that `feeds.dltj.org` is an alias for the [FeedBurner service](https://feedburner.google.com/), and the FeedBurner service doesn't have the security key to serve content from that domain name using HTTPS.
We need a way to legitimately serve a file with using HTTPS with the `https://feeds.dltj.org/DisruptiveLibraryTechnologyJester` address.

## About FeedBurner
Back in the day when blog syndication feeds were far more popular when they are now, FeedBurner was a tool that blog authors could use to get statistics about how others used their content as well as providing a way for blog posts to be turned into email-delivered newsletters.
Wikipedia has a [more complete description of FeedBurner](https://en.wikipedia.org/wiki/FeedBurner), including how the company was bought by Google in 2007 -- three years after its founding.
But it didn't last.
After four years at Google, they announced the shutdown of the FeedBurner API, and a year later the discontinuation of AdSense for Feeds.
Still, as a service retrieving syndication feeds from blogs and making them pretty, FeedBurner lives on.
(Aside, last year the Motherboard section of the Vice website had an interesting article about [why Google can't shut down Feedburner](https://motherboard.vice.com/en_us/article/ywqz4x/googles-forgotten-service-how-feedburner-became-a-zombie).)

*_MyBrand_* is a feature of FeedBurner that allowed one to use their own domain name for the syndication feed rather than the FeedBurner-supplied `http://feeds.feedburner.com/`.
With a little bit of extra effort, this gives the blog author the ability to leave FeedBurner at some point without losing all of the users that subscribed to the FeedBurner syndication; you could just use another syndication feed service, or serve the feed yourself.
In my case, I used the domain name `feeds.dltj.org`.

## Fixing the HTTPS and HSTS problem
But now I'm left with the problem that FeedBurner can't securely send my syndication feed using the MyBrand domain name.
And I don't think Google will ever put in the effort to allow that to happen.
Heck, I'm somewhat surprised that FeedBurner is still around as a service, much less being enhanced.
(Read the Motherboard article above for why this is surprising.)
But I don't want to turn off HSTS for the `dltj.org` domain, so what can be done?

This blog is hosted using Amazon Web Services (AWS), and AWS has all of the tools I need to fix this problem:

* [CloudFront](https://aws.amazon.com/cloudfront/): content distribution network
* [Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html): free encryption certificates
* [Lambda@Edge](https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html): snippets of code running on CloudFront

Here is how the pieces fit together:

1. CloudFront is going to retrieve, cache, and serve the FeedBurner-enhanced syndication file.
2. Certificate Manager automatically creates an HTTPS security certificate that CloudFront uses to verify the `feeds.dltj.org` domain name.
3. Lambda@Edge is needed because I don't want to proxy _all_ of the FeedBurner syndication feeds -- just the one that matters to me.

### CloudFront distribution
Here are the screen captures of the setup of the CloudFront distribution in the AWS web console.
{% include image.html
    wpsrc="2019/scaled/20190109-cloudfront-distribution-500px.png"
    wpurl="2019/20190109-cloudfront-distribution.png"
    width="300"
    alt="Screen capture of the AWS CloudFront distribution screen"
    caption="Screen capture of the AWS CloudFront distribution screen. <i>Click image to enlarge.</i>"
%}
Nothing very unusual here, but note that _Alternate Domain Names (CNAME)_ with the `feeds.dltj.org` domain name that I'm publishing to the world and the _SSL Certificate_ with the cert supplied by AWS.

{% include image.html
    wpsrc="2019/scaled/20190109-cloudfront-origin-500px.png"
    wpurl="2019/20190109-cloudfront-origin.png"
    width="300"
    alt="Screen capture of the AWS CloudFront distribution screen"
    caption="Screen capture of the AWS CloudFront distribution screen. <i>Click image to enlarge.</i>"
%}
Nothing unusual here either; note that the origin domain name is `feeds.feedburner.org`.

{% include image.html
    wpsrc="2019/scaled/20190109-cloudfront-behavior-500px.png"
    wpurl="2019/20190109-cloudfront-behavior.png"
    width="300"
    alt="Screen capture of the AWS CloudFront distribution screen"
    caption="Screen capture of the AWS CloudFront distribution screen. <i>Click image to enlarge.</i>"
%}
This one is a little unusual because there is a _"Lambda Function Associations"_ set for the _Viewer Request_ function.
I did not set this Lambda@Edge function on the AWS CloudFront screen; rather set it using the Lambda screen.

### AWS Certificate Services
There isn't anything special about creating the cert using AWS Certificate Services for this CloudFront distribution.
You'll need to verify ownership of the domain name, of course.
Just follow the [instructions in the AWS Certificate Manager documentation](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html).

### Lambda@Edge
If you have followed along this far, you'll note that we set up a CloudFront distribution for all content located at the http://feeds.feedburner.com/ origin server.
I don't want to proxy _all_ of FeedBurner's feeds -- just the one for my blog.
So I have a function running on Lambda@Edge to filter out all CloudFront requests that don't match my blog.
Lambda@Edge uses JavaScript running in Node, so it looks like this:

```javascript
'use strict';

exports.handler = (event, context, callback) => {
    const request = event.Records[0].cf.request;
    const headers = request.headers;

    const mainFeed = "DisruptiveLibraryTechnologyJester";
    
    const passthroughUris = [
        `/${mainFeed}`,
        '/favicon.ico',
        '/fb/images/favicon.ico',
        '/~d/styles/atom10full.xsl',
    ];

    const notFoundResponse =  {
        status: '404',
        statusDescription: 'Not Found',
        headers: {
            'content-type': [{
                key: 'Content-Type',
                value: `text/plain`,
            }],
            'content-encoding': [{
                key: 'Content-Encoding',
                value: 'UTF-8'
            }],
        },
        body: 'The feed you are looking for is not here.',
    };
    
    const redirectResponse = {
        status: '302',
        statusDescription: 'Found',
        headers: {
            location: [{
                key: 'Location',
                value: `https://${headers.host[0].value}/${mainFeed}`,
            }],
        },
    };

    if (request.uri && request.uri == '/') {
        callback(null, redirectResponse);
    }
    if (request.uri && passthroughUris.includes(request.uri)) {
        callback(null, request);
    }

    callback(null, notFoundResponse);
};
```

You can read the [Lambda@Edge documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html) for the specifics of how this code works, but basically:
1. There is a list of partial URLs (just the path portion of the URL) that we are interested in passing through to the origin server (`passthroughUris`).
1. We set up a response variable that tells CloudFront to return a 404-not-found HTTP status code.
1. We set up another response variable that redirects the web client to our syndication feed.
1. We test to see if the requested URL is just the root (`/`), and if so we return the redirect response variable.
1. We test to see if the requested URL is one of the ones we want to pass through, and then pass it through.
1. For everything else we return the not-found response variable.

This Lambda@Edge function is then linked to the _"Viewer Request"_ event of the CloudFront distribution.
The Viewer Request event is the first thing that happens at CloudFront -- before CloudFront looks in its cache of files or tries to get the file from the origin server.
At this event point we determine whether we want to handle the request or return the 404-not-found status code.

## For the future
True be told, this is a stop-gap measure.
I'm not sure I can count on Google continuing to run FeedBurner, and I'm not sure I want to continue to force my readers to use a Google service.
The author of the Motherboard article says:
> I was stuck on FeedBurner for a while myself, and it annoyed me, to be honest. Fortunately, we’re not completely stuck with terrible options anymore. These days, [I use FeedPress](https://feed.press/), which costs money but I recommend, though there are plenty of others, like [Feedity](https://feedity.com/) and [Feedio](http://www.feedio.co/). (You can always go back to your old RSS or Atom feed, of course.)

I'll look at one of these options to enhance the syndication feed.
One of the things I really like about FeedBurner is giving blog readers the option of receiving posts by email.
It seems like most people use services like TinyLetter or similar for this kind of functionality, so I know alternatives exist for blog-post-by-email readers.
It feels at the moment, though, like the <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym></i> blog is getting rebooted, and I want to focus attention on other fixes and enhancements.
This CloudFront-proxied FeedBurner syndication feed will work for now.