---
layout: wordpress-import
status: published
published: true
title: 'Trip Report of DPLA Chattanooga Appfest: Project Shows Signs of Life'
modified: 2012-12-07T19:18:52+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 4049
wordpress_url: http://dltj.org/?p=4049
date: '2012-12-07 14:18:52 -0500'
date_gmt: '2012-12-07 19:18:52 -0500'
category: Meeting
categories:
- Meeting
tags:
- IMLS
- Digital Public Library of America
comments:
- id: 383377
  author: ThatAndromeda
  author_email: twitter.102080846@example.com
  author_url: http://twitter.com/ThatAndromeda
  date: '2012-12-07 14:23:07 -0500'
  date_gmt: '2012-12-07 19:23:07 -0500'
  content: 'RT @DataG: New blog post: Trip Report of DPLA Chattanooga Appfest: Project
    Shows Signs of Life http://t.co/h8ynfWIx'
- id: 383378
  author: ThatAndromeda
  author_email: twitter.102080846@example.com
  author_url: http://twitter.com/ThatAndromeda
  date: '2012-12-07 14:23:39 -0500'
  date_gmt: '2012-12-07 19:23:39 -0500'
  content: "@DataG yay! I finally got around to drafting my blog post about Appfest
    (for TechConnect) just the other day."
---
<div style="border: 1px solid black; background-color: #DDD; padding: 1em;margin-bottom:1.5em">Below is my report of the DPLA AppFest last month.  This post is the raw input of an <a href="http://blog.imls.gov/?p=2337">article on the IMLS blog</a> that was co-written with Mary Barnett, Social Media Coordinator at the Chattanooga Public Library.  I also attended yesterday's DPLA Audience and Participation workstream meeting at George Mason University, and hope to have a similar trip report posted soon.</div>
<p>The Digital Public Library of America held an <a href="http://dp.la/info/developers/appfest/" title="November 8-9, 2012 DPLA Appfes | Digital Public Library of Americat">AppFest</a> gathering at the <a href="http://www.lib.chattanooga.gov/" title="Chattanooga Public Library homepage">Chattanooga Public Library</a> on November 8-9, 2012 for a full day of designing, developing and discussion.  About 40 people attended from a wide range of backgrounds:</p>
<ul>
<li>Public libraries, academic libraries, companies, library consortia and other groups.</li>
<li>Designers, user experience professions, metadata specialists, coders, and "idea people".</li>
<li>A variety of U.S. states and Canadian provinces.  </li>
</ul>
<p>One of the primary purposes of day was to test the <a href="https://github.com/dpla/platform/wiki">DPLA application programming interface</a> (API) to see if it could answer queries from programs that would do useful tasks.  The quick answer to that challenge would seem to be "yes!" and there were a lot of positive feelings coming out of the meeting.</p>
<p>The goal of the DPLA is a little unusual.  Although there will be a public web-based interface to the DPLA content, the overriding desire is to build the back-end services that will enable DPLA content to be used through local libraries, archives and museums in a variety of interfaces.  In this way, DPLA is like a traditional publisher: it will gather content from a variety of sources (authors), add new value (copyedit, create an index), and send out content through a variety of streams (libraries, local bookstores, internet retailers and other venues like convenience stores and airport shops).  The DPLA will gather content from regional and subject hubs, enhance it, and make it available to websites, mobile applications, and other tools.  So the AppFest was a way to figure out if the early technology designs of the DPLA could meet those goals.</p>
<p>The AppFest started on Thursday evening with a recorded video welcome from John Palfrey and a recording of Emily Gore from DPLA Midwest <a href="https://www.youtube.com/watch?v=YZYf0Li0wlc">introducing the DPLA Digital Hubs Pilot Program</a> followed by a <a href="http://thatandromeda.github.com/appfest/" title="Appfest by thatandromeda">brief introduction to developer productivity tools Git and GitHub</a> by Andromeda Yelton.  The evening ended with people pitching ideas for projects that participants would work on the next day.  The ideas were ones previously recorded on the <a href="http://dp.la/wiki/?title=Appfest&amp;oldid=2441" title="Appfest - Digital Library of America Project">DPLA wiki page</a> or were spontaneously created at the meeting.  </p>
<p>{{ image(
    div_float="center",
    width="600",
    caption='Sign-up sheet for Appfest Projects',
    alt="DPLA Project Sign-up Page",
    localsrc="2012/12/A7RG9HxCIAIOQJM.jpg") }}</p>
<p>Friday morning started with an introduction to the DPLA API by Jeffrey Licht of Pod Consulting and a review of the possible projects.  The project titles were put up on a wall and people self-selected what they wanted to work on for the day.  I picked the project that wanted to create a map interface with pins that corresponded to the position of resources in the repository, and other choices were distributed reference services, visualization techniques to see collection content in context with the whole repository, and a new-content notification service.  The teams presented their work at the end of the day to the other participants and a panel of judges.  We even had a presentation from a remote participant show his work over a Skype video call.  After much deliberation, the judges picked the "DPLA Plus" project as best of the AppFest; that project focused on the need of public users to discover what is in the repository.</p>
<p>I think most would agree that the AppFest was a success.  The API lived up to the challenge, both in terms of robustness of functionality and its technical ability to respond to queries from the projects.  The records returned from the DPLA data set show the challenges of aggregating metadata from disparate sources.  In our project we had problems with nonsensical geo-located records that could be filtered, checked and enhanced by automated routines at the central hub.  We also ran into the classic difficulty of having reasonable thumbnails to display to users.  Web addresses to thumbnail images are not a common part of metadata since they are usually created by the repository system itself.  Having a DPLA service to augment records from hubs with URLs to real thumbnail images would be a very helpful addition.</p>
<p>The AppFest was more evidence that the DPLA is definitely pulling itself up by its bootstraps.  Coming a month after a <a href="http://dp.la/info/get-involved/events/dplamidwest/" title="October 11-12, 2012, DPLA Midwest meeting | Digital Public Library of America">successful Midwest plenary session</a> and two months after formal incorporation and <a href="http://blogs.law.harvard.edu/dplaalpha/2012/09/11/dpla-announces-inaugural-board-of-directors/" title="DPLA Announces Inaugural Board of Directors | Digital Public Library of America">installation of its board of directors</a> plus announcements of new rounds of grant funding from <a href="http://blogs.law.harvard.edu/dplaalpha/2012/09/13/imls-award/" title="IMLS Awards $250,000 to the DPLA for Digital Hubs Pilot Program | Digital Public Library of America">IMLS</a>, <a href="http://blogs.law.harvard.edu/dplaalpha/2012/07/26/national-endowment-for-the-humanities-announces-award-to-support-development-of-dpla/" title="National Endowment for the Humanities announces award to support development of DPLA pilot | Digital Public Library of America">NEH</a>, and the <a href="http://blogs.law.harvard.edu/dplaalpha/2012/10/12/knight-grant/" title="Seven pilot sites join national digital library project with Knight Foundation funding | Digital Public Library of America">Knight Foundation</a>, the DPLA is making steady progress towards fulfilling its mission.  The next major event is slated to be the unveiling of a public interface to the DPLA collection in April 2013.
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://dp.la/get-involved/events/appfest/ to http://dp.la/info/developers/appfest/ on September 26th, 2013.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://dp.la/get-involved/events/dplamidwest/ to http://dp.la/info/get-involved/events/dplamidwest/ on September 26th, 2013.</p>
