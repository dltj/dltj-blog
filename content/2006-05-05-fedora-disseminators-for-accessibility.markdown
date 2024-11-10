---
layout: wordpress-import
status: published
published: true
title: 'Fedora Disseminators to Enable Accessible Repository Content'
modified: 2006-05-06T02:04:19+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 51
wordpress_url: http://dltj.org/2006/05/fedora-disseminators-for-accessibility/
date: '2006-05-05 22:04:19 -0400'
date_gmt: '2006-05-06 03:04:19 -0400'
category: Library Technology
categories:
- DRC
- Fedora
tags:
- asset actions
- section508
- Fedora Repository
comments:
- id: 61
  author: Michael
  author_email: leftwing@alumni.rutgers.edu
  author_url: http://purl.org/net/leftwing/blog
  date: '2006-05-05 23:27:50 -0400'
  date_gmt: '2006-05-06 04:27:50 -0400'
  content: Yet another advantage borne of the flexibility of Fedora!  You're on a
    roll, Peter.
- id: 72
  author: Michael
  author_email: leftwing@alumni.rutgers.edu
  author_url: http://purl.org/net/leftwing/blog
  date: '2006-05-12 23:46:13 -0400'
  date_gmt: '2006-05-13 04:46:13 -0400'
  content: "Hey Peter,\r\n\r\nSince Red Hat doesn't seem likely to give up on the
    name \"Fedora,\" and it'd be nice to have a tag for our Fedora that doesn't bring
    up a bunch of articles about the Linux kernel, I was thinking it'd be good for
    us Fedora bloggers to come up with a tag solely for our Fedora.  Then we can make
    smarter searches on technorati, del.icio.us, and so forth.\r\n\r\nI'm thinking
    something along the lines of \"fedora-repository\" currently, but that's not too
    spectacular.  Any ideas?  If we come up with a tag before the Fedora conference,
    it can even be shared with other potential Fedora bloggers."
- id: 75
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-05-13 21:05:28 -0400'
  date_gmt: '2006-05-14 02:05:28 -0400'
  content: "Hmmm -- if it was case sensitive, we could call it FEDORA.  :-)\r\n\r\nGood
    question, though.  \"The-Fedora\"?  \"Fedora-DOR\"?  Should we refer to it by
    the domain name (\"fedora-info\" -- I'm not sure if \"fedora.info\" is legal in
    many cases)?"
- id: 81
  author: Michael
  author_email: leftwing@alumni.rutgers.edu
  author_url: http://purl.org/net/leftwing/blog
  date: '2006-05-15 17:39:58 -0400'
  date_gmt: '2006-05-15 22:39:58 -0400'
  content: "It's a tough one, isn't it?  \r\n\r\nI think I'm leaning towards fedora-repository
    or fedorarepository, though both are terribly long.  The popular tags for fedora.info
    at del.icio.us aren't terribly great, either.\r\n\r\nDo you know any other Fedora
    bloggers who might have suggestions?"
- id: 83
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-05-15 19:54:35 -0400'
  date_gmt: '2006-05-16 00:54:35 -0400'
  content: I don't know of anyone else the blogs, but there are some that are reading
    this blog and some others that hang out on the IRC channel.  I'll try posting
    a message here specifically on the topic (to catch those that are not reading
    the comments) and query the IRC channel participants tomorrow.
- id: 10832
  author: 'Walt at Random &raquo; Blog Archive &raquo; Printability: It&#8217;s not
    just for Firefox anymore'
  author_email: ''
  author_url: http://walt.lishost.org/?p=397
  date: '2007-01-11 01:22:38 -0500'
  date_gmt: '2007-01-11 06:22:38 -0500'
  content: "<!--%kramer-ref-pre%-->[...] I tried your site and was pleased to find
    a nice print media CSS declaration. (Or, in the case of WaR, I think what is happening
    when the page is printed is the absence of a CSS declaration because you are using
    media=&#8221;screen&#8221; attribute.) How your page appears when printed (and
    given your typography interest, this comes as no surprise to you) is very important.
    I worked for a number of hours to make sure it came out right on DLTJ as well.
    Try printing a random posting on DLTJ and you&#8217;ll see what I mean. [...]<!--%kramer-ref-post%-->"
---
<p>Calling all accessibility technology experts!  What follows is a line of thinking about using characteristics of the <a href="http://www.fedora.info/" title="Fedora">FEDORA digital object repository</a> to enable access to content through non-graphical interfaces.  Thanks to Linda Newman from the University of Cincinnati and others on the Friday morning DRC Developers conference call for triggering this line of thinking.</p>
<p>In a recent post defining <a href="/article/fedora-disseminators/">universal disseminators for every object in our repository</a> (if the last dozen words didn't make sense, please read the linked article and come back), I hinted at having an auditory derivative of each object, at least at the preview level.  During today's conference call, Linda asked if such a disseminator could be used to offer different access points for non-GUI users.  Well, why not?  Let's look back at the "presentation" part of the disseminator label:</p>
<blockquote><p>
A presentation can be one of:</p>
<ul>
<li>"preview" - a small/short version of the datastream returned in the datastream's original format</li>
<li>"screen" - a roughly GUI-screen-sized version of the datastream returned in the datastream's original format</li>
<li>"thumb" - a small, static image derivative of the datastream</li>
<li>"audio" - an auditory derivative of the datastream</li>
<li>"description" - a Dublin Core description of the item marked up in an HTML table</li>
<li>"record" - HTML markup of Thumb plus Description (suitable, for instance, as a representation of the object in a browse list)</li>
</ul>
</blockquote>
<p>Specifically, we talked about the <em>audio</em> presentation for non-audio objects (digital objects where audio is not the fundamental focus of the object).</p>
<ul>
<li>There could be a descriptive audio track, similar in concept to <a href="http://www.afb.org/section.asp?SectionID=3&#038;TopicID=140" title="Public Policy - American Foundation for the Blind">video description</a>, that would be returned to the calling application.  Perhaps, for instance, the audio of a commentary found on the <a href="http://web.archive.org/web/20060109104203/http://www.ices.utexas.edu:80/~natacha/CATTt/hearing.html" title="Exhibition Design Guidelines: Hearing Impairements">handheld audio tour devices in art museums</a>.</li>
<li>In the absence of other audio description, the disseminator could run a text-to-speech algorithm against the title, creator, and description fields and return that to the calling application.</li>
</ul>
<p>This brings to mind another transformation we could apply to give a preview of an object.  (No, I haven't moved into the odor or tactile senses -- yet.)  Would it be useful to have a disseminator return a text summary and/or metadata aggregation of an object on demand?</p>
<p>And, of course, the critical question:  is it the job of a repository to build in access methods like this to be used by applications designed with alternate accessibility in mind?  Should it be up to the application to create the derivatives necessary?  I took a brief look at <a href="http://www.section508.gov/" title="Section 508: The Road to Accessibility">Section 508</a> requirements, but couldn't find any real guidance about serving up accessible forms of content.  (There is a great deal of information about how to create accessible web pages, but very little I could find about making assets in those pages accessible.)  But I only know enough about this area to have it on my radar...and certainly not enough to formulate any answers.</p>
<p>The original goal of defining these universal disseminators was to assure a base level of functionality for every object in the system -- a contract, if you will, between the repository and any consuming application that it could ask an object to return itself or a derivative of itself in all of these forms.  What do you think?  Should that contract be consciously extended to include universal accessibility?</p>
