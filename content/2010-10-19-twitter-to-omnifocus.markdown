---
layout: wordpress-import
status: published
published: true
title: 'The PERL Way to Add OmniFocus Inbox Entries from Twitter'
modified: 2010-10-20T02:09:16+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1734
wordpress_url: http://dltj.org/?p=1734
date: '2010-10-19 22:09:16 -0400'
date_gmt: '2010-10-20 02:09:16 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- perl
- Getting Things Done
- howto
- Twitter
- applescript
- OmniFocus
- twitter-to-omnifocus
comments:
- id: 94488
  author: Voice -> OmniFocus - Page 2 - The Omni Group Forums
  author_email: ''
  author_url: http://forums.omnigroup.com/showthread.php?p=87755
  date: '2010-10-20 10:25:43 -0400'
  date_gmt: '2010-10-20 14:25:43 -0400'
  content: "<!--%kramer-ref-pre%-->[...] background on the Mac to do the same thing.
    I wrote up the instructions and posted the code here: The PERL Way to Add OmniFocus
    Inbox Entries from Twitter  Thanks to everyone who worked on this problem previously.
    \        Post 12     [...]<!--%kramer-ref-post%-->"
- id: 99310
  author: David Somers
  author_email: jalada@gmail.com
  author_url: https://github.com/jalada/twitter-to-omnifocus
  date: '2010-11-10 09:21:24 -0500'
  date_gmt: '2010-11-10 14:21:24 -0500'
  content: "I forked your repo and changed it to use direct messages sent to the account
    rather than the home timeline, as this means you can use your normal account,
    and just DM the private account.\r\n\r\n(check website link for repo)"
- id: 99313
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-11-10 09:30:05 -0500'
  date_gmt: '2010-11-10 14:30:05 -0500'
  content: Great idea and nice work, David.  Thanks for extending my original work.
- id: 131396
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-03-31 08:41:46 -0400'
  date_gmt: '2011-03-31 12:41:46 -0400'
  content: You're welcome, Chris!  I'm glad you found it useful.
---
<p>Over the weekend I got the bright idea of asking <a href="http://www.omnigroup.com/" title="The Omni Group">OmniGroup</a> to ask an iPhone voice recognition application (like <a href="http://itunes.apple.com/us/app/dragon-dictation/id341446764?mt=8" title="Dragon Dictation for iPhone, iPod touch, and iPad on the iTunes App Store">Dragon Dictation</a>) to add a link to the <a href="http://www.omnigroup.com/products/omnifocus_for_iphone/" title="OmniFocus for iPhone - Products - The Omni Group">OmniFocus iPhone</a> application.  That way I could simply dictate new inbox items on the iPhone rather than laboriously typing them with the on-screen keyboard.  Before making the suggestion, I <a href="http://forums.omnigroup.com/search.php?do=process&amp;quicksearch=1&amp;childforums=1&amp;exactname=1&amp;s=&amp;securitytoken=guest&amp;query=voice+recognition&amp;showposts=0" title="The Omni Group Forums - Search Forums">searched the OmniFocus User Forum for "voice recognition"</a> to see if anyone else had suggested the same thing.  As it turns out, there were <a href="http://forums.omnigroup.com/showthread.php?t=5871" title="Ubiqutious task entry -- anywhere, anytime - The Omni Group Forums">a</a> <a href="http://forums.omnigroup.com/showthread.php?t=11543&amp;highlight=voice+recognition" title="Voice -> OmniFocus - The Omni Group Forums">few</a> <a href="http://forums.omnigroup.com/showthread.php?t=11544&amp;highlight=voice+recognition" title="new solution to speak new inbox tasks - The Omni Group Forums">posts</a> that had instructions from people using Twitter as an intermediary.  Unfortunately, they either required a desktop Twitter client to be running all of the time or <a href="http://ptone.com/dablog/2009/03/voice-to-omnifocus-revisited/" title="Voice to OmniFocus, revisited">used</a> the now deprecated BasicAuth-based Twitter authentication scheme.  So I created my own.<br />
<!--more--></p>
<h2>The Script</h2>
<p>I'm a UNIX command line geek at heart, and an old one at that, so my preferred language is Perl. This program runs as a background command line application using a couple of Perl modules:  <a href="http://search.cpan.org/dist/Net-Twitter-Lite/" title="Marc Mims / Net-Twitter-Lite - search.cpan.org">Net::Twitter::Lite</a> to interact with Twitter and <a href="http://search.cpan.org/~dsugal/Mac-AppleScript/" title="Dan Sugalski / Mac-AppleScript - search.cpan.org">Mac::AppleScript</a> to interact with OmniFocus.  Install those two modules and their depencencies on your Mac if you don't already have them (e.g. <code>cpan install Net::Twitter::Lite</code> and <code>cpan install Mac::AppleScript</code>), then copy <a href="http://github.com/dltj/twitter-to-omnifocus/raw/master/twitter-to-omnifocus" title="twitter-to-omnifocus script">this script</a> and a configuration file based on <a href="http://github.com/dltj/twitter-to-omnifocus/raw/master/tweettoOmniFocus.cfg.example" title="tweettoOmniFocus.cfg example">this sample</a> in a directory off your home directory.  The <a href="http://github.com/dltj/twitter-to-omnifocus" title="dltj's twitter-to-omnifocus at master - GitHub">source code</a> is available on GitHub if you want to fork it and improve it.</p>
<h2>Registering your Application with Twitter</h2>
<p>{{ image(
    div_float="right",
    width="300",
    caption="Tweet Privacy Checkbox",
    alt="Tweet Privacy",
    localsrc="/assets/images/2010/10/Tweet-Privacy-300x71.png",
    localhref="/assets/images/2010/10/Tweet-Privacy.png") }}
To put Twitter in the middle between my iPhone voice recognition app and OmniFocus, I set up a new Twitter account just for the purpose of pushing entries into the OmniFocus Inbox.  I marked this new account as <a href="http://support.twitter.com/groups/31-twitter-basics/topics/107-my-profile-account-settings/articles/14016-about-public-and-protected-accounts" title="Twitter Help Center">private in the account settings</a> because I don't want anyone subscribing to the tweets sent through this account.</p>
<p>Because I marked it as private, the script can't read the home timeline of tweets without authentication.  In order to authenticate with Twitter, I need to <a href="http://dev.twitter.com/apps" title="http://dev.twitter.com/apps">register the script</a> with the Twitter API service to get a "Consumer Key" and a "Consumer Secret".  The registration page looks similar to below, but you'll need to pick a different name.  (Application names must be unique across Twitter.)<br />{{ image(
    div_float="center",
    width="795",
    caption="New Twitter Application screen for twitter-to-omnifocus",
    alt="New Twitter Application screen for twitter-to-omnifocus",
    localsrc="/assets/images/2010/10/New-Twitter-Application-dev.twitter.com_1287524992428-795x1024.png",
    localhref="/assets/images/2010/10/New-Twitter-Application-dev.twitter.com_1287524992428.png") }}
</p>
<p>After submitting that form, you'll see a page that will have your key information.  Replace the sample keys in the tweettoOmniFocus.cfg file with the ones from this page.</p>
<p>You'll need to run the twitter-to-omnifocus application once interactively on the command line in order to complete the process of registering the script with Twitter.  First, change the mode of the script so that you can execute it, then run the script:</p>
```bash
chmod u+x twitter-to-omnifocus
./twitter-to-omnifocus
```
<p>You'll be promted to go to a website to get a PIN:</p>
```
Authorize this app at http://twitter.com/oauth/authorize?oauth_token=nnn and enter the PIN#
```
<p>When you get the PIN, paste it into the terminal window and hit return.  Two new security tokens will be added to the configuration file.</p>
<h2>Getting the Script to Run Periodically on the Mac</h2>
<p>The last step is to get the script to run periodically on the Mac.  If one were to stick to UNIX traditions, you would run `crontab -e` to create a cron entry.  I think that would work, but the Mac-way of doing it is to create a launchd entry.  You can create one of these by hand, but I find using <a href="http://sourceforge.net/projects/lingon/" title="Lingon | SourceForge.net">Lingon</a> to be a much more palatable way of doing it.  (Okay -- so I'm not a pure command-line junkie.)<br />{{ image(
    div_float="center",
    width="714",
    caption="Lingon configuration for twitter-to-omnifocus",
    alt="Lingon configuration for twitter-to-omnifocus",
    localsrc="/assets/images/2010/10/Lingon-configuration-for-twitter-to-omnifocus.jpg",
    localhref="/assets/images/2010/10/Lingon-configuration-for-twitter-to-omnifocus.jpg") }}
</p>
<h2>All Done!</h2>
<p>{{ image(
    div_float="right",
    width="200",
    caption="iPhone Dragon Dictation screen",
    alt="",
    localsrc="/assets/images/2010/10/IMG_0054-200x300.png") }}With that set, you can now simply send a tweet to your private Twitter account from any mechanism you might have.  What got me started on this path was using <a href="http://itunes.apple.com/us/app/dragon-dictation/id341446764?mt=8" title="Dragon Dictation for iPhone, iPod touch, and iPad on the iTunes App Store">Dragon Dictation</a> on the iPhone to dictate inbox items.  One person suggested using <a href="http://jott.com/default.aspx" title="Jott.com | Voice-to-Text Notes, To Dos &amp; Reminders.  Voicemail-to-Email and Text Message">Jott</a> for phone-to-Twitter transcribing and another suggested an <a href="http://tweetymail.com/" title="Twitter over Email">e-mail path</a>.</p>
<p>In the end, this is quite an effort and a moderately fragile setup for doing what I want.  In particular, the dictated entries don't immediately appear in my iPhone OmniFocus app database. I'd like some tighter integration between the applications, but I'll settle for this for now.<br />
<br style="clear: both" /></p>
