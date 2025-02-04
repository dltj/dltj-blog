---
layout: wordpress-import
status: published
published: true
title: Idea for an NPR Twitter bot -- Tweet me about that story I just heard
modified: '2018-01-15T17:35:29-05:00'
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 27145
wordpress_url: http://dltj.org/?p=27145
date: 2016-02-17 21:07:51 -0500
date_gmt: 2016-02-18 02:07:51 -0500
category: Raw Technology
categories:
- Raw Technology
tags:
- National Public Radio
- Twitter
- Amazon Web Services
- bot
comments: []
---
So I had an idea for a Twitter bot I would like to see. Occasionally I'll be listening to a story on NPR and I'll want to know more about it. Sometimes the host will say something like: "come to npr.org for more information and click on..." Other times it will be because I missed a crucial bit of the story and I'll want to know more about it. So why not have a Twitter bot that I can call upon to say "Tell me more about that story":

https://twitter.com/DataG/status/700138826472140802

https://twitter.com/NPRnow/status/700138909154545664

The workflow for such a system doesn't seem that hard. The bot would have to know my current location, and from that guess which NPR station(s) I'm listening to. (If I didn't have geolocated tweets turn on, the bot could engage in a direct message conversation with me to ask which radio station I was listening to.) It would know the time of my tweet, so it know which segment I was listening to. Sure, there is variation in local program listings, but for the most part it could probably rely on the national program segment lineups.

The technology isn't all that hard either. [Amazon Kinesis][0] could be used for tapping into [Twitter's streaming API][1]. Kinesis would fire off [AWS Lambda][2] events in response to tweets to the bot, and the Lambda function could do the work of figuring out how to respond to the user. There is already some [nice sample code from AWS][3] for how to put this together.

I'd do this, but there is one piece missing that I can't find -- the NPR segment lineup. A time-stamped listing of when the segments appear in the national audio stream. There is some nice semantic markup in the program listing page ([today's Morning Edition show][4], for example):

```html
<article class="story clearfix">
  <p class="segment-num"><b>1</b></p>
  <div class="storyinfo noimg">
    <h2 class="slug"><a href="http://www.npr.org/sections/race/" title="Race : NPR">Race</a></h2>
    <h1><a href="http://www.npr.org/2016/02/17/467036605/qualified-diverse-candidates-must-be-considered-for-supreme-court-vacancy" title="Supreme Court Short List Must Include Diverse Candidates, Author Says : NPR">Supreme Court Short List Must Include Diverse Candidates, Author Says</a></h1>
    <input type="hidden" id="title467036605" value="Supreme Court Short List Must Include Diverse Candidates, Author Says"/>
    <input type="hidden" id="modelShortUrl467036605" value="http://n.pr/1R7CT0l"/>
    <input type="hidden" id="modelFullUrl467036605" value="http://www.npr.org/2016/02/17/467036605/qualified-diverse-candidates-must-be-considered-for-supreme-court-vacancy"/>
  </div>

  <div class="audio-player ">
    <a href="#" data-audio="/npr/me/2016/02/20160217_me_qualified_diverse_candidates_must_be_considered_for_supreme_court_vacancy" data-audio-desktop="[467036605, 467036606, null, 1, 1, 1]">
      <b class="icn-media"></b>
      <b class="call-to-action">Listen</b>
      <b class="loading">Loading&hellip;</b>
      <b class="audio-info">
        </b><b class="time-elapsed"></b>
        <b class="time-total">5:30</b>
      
      <b class="media-time-total">
        </b><b class="media-time-current"></b>
        <b class="scrubber"></b>
      
    </a>
    
    <ul class="aux has-embed">
      <li class="playlist"><a href="#" data-audio="/npr/me/2016/02/20160217_me_qualified_diverse_candidates_must_be_considered_for_supreme_court_vacancy" data-audio-desktop="[467036605, 467036606, null, 2, 1, 1]" title="Playlist">Playlist</a></li>

      <li class="download"><a href="http://pd.npr.org/anon.npr-mp3/npr/me/2016/02/20160217_me_qualified_diverse_candidates_must_be_considered_for_supreme_court_vacancy.mp3?dl=1" title="Download">Download</a></li>

      <li class="embed">
        <a href="#" title="Embed">Embed</a>
        <div class="audio-embed-modal">
          <label class="embed-label">Embed<input class="embed-url embed-url-no-touch" readonly="" value="<iframe src="http://www.npr.org/player/embed/467036605/467036606" width="100%" height="290" frameborder="0" scrolling="no" title="NPR embedded audio player"/>"></label>
          <button class="embed-close" aria-label="close embed overlay">Close embed overlay</button>
          <b class="embed-url embed-url-touch"><code><b class="punctuation"><</b>iframe src="http://www.npr.org/player/embed/467036605/467036606" width="100%" height="290" frameborder="0" scrolling="no" title="NPR embedded audio player"></code></b>
        </div>
      </li>
    </ul>
  </div>
</article>
```

But it doesn't have the time-stamped rundown of when the segments occur in the show.  I've done some moderately intense Google searches, but I haven't turned up anything.  This kind of thing is probably on the dark web since it is intended just for station managers.  Does anyone know how I might get ahold of it?

[0]: https://aws.amazon.com/kinesis/
[1]: https://dev.twitter.com/streaming/overview/messages-types
[2]: https://aws.amazon.com/lambda/
[3]: https://github.com/awslabs/lambda-refarch-streamprocessing
[4]: http://www.npr.org/programs/morning-edition/?prgDate=02-17-2016 "Morning Edition : NPR"
