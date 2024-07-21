---
layout: wordpress-import
status: publish
published: true
title: 'Fixing a Mac OSX Leopard Login Loop Caused by Launch Services'
modified: 2008-06-03T18:19:49+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 369
wordpress_url: https://dltj.org/?p=369
date: '2008-06-03 14:19:49 -0400'
date_gmt: '2008-06-03 18:19:49 -0400'
categories:
- Raw Technology
tags:
- Mac OS X Operating System
- troubleshooting
comments:
- id: 33393
  author: Mac OS X and iPod Troubleshooting, Support, and Help - MacFixIt
  author_email: ''
  author_url: http://www.macfixit.com/comment.php?mode=display&amp;sid=20080530225515297&amp;title=Another+fix+for+login+window+loop&amp;type=article&amp;order=&amp;pid=32359
  date: '2008-06-04 11:30:16 -0400'
  date_gmt: '2008-06-04 15:30:16 -0400'
  content: "<!--%kramer-ref-pre%-->[...] too, had the login loop problem. In my case,
    it was a corrupted Launch Services file. I've posted details of the symptoms and
    the fix on my blog in case it would be of use to others.[ Reply to This | Parent
    [...]<!--%kramer-ref-post%-->"
- id: 33503
  author: Scott
  author_email: scootklein@gmail.com
  author_url: ''
  date: '2008-06-24 09:10:53 -0400'
  date_gmt: '2008-06-24 13:10:53 -0400'
  content: "beautiful, works like a charm.  better than archive&amp;install as recommended
    by apple\r\n\r\nthanks guys"
- id: 33521
  author: Chris Petty
  author_email: pettycm@talk21.com
  author_url: ''
  date: '2008-06-27 11:16:24 -0400'
  date_gmt: '2008-06-27 15:16:24 -0400'
  content: Great little fix. For me the solutions offered by Apple failed on my Mac
    Mini with wireless keyboard and mouse, unable to login using single user shift
    key and cmd + S. In the end used the install disk, needed a clean first, then
    ran terminal and did as you said. For me login items remained the same but a directory
    I had in the dock lost the hide file extensions that I had set up.
- id: 33525
  author: macgirl
  author_email: shinigamiet@yahoo.com.hk
  author_url: ''
  date: '2008-06-29 17:56:25 -0400'
  date_gmt: '2008-06-29 21:56:25 -0400'
  content: how do you fix it i dont understand >. <" I'm new to mac
- id: 33536
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-07-02 11:17:20 -0400'
  date_gmt: '2008-07-02 15:17:20 -0400'
  content: "macgirl --\r\n\r\nI was intentionally somewhat vague in the solution because
    implementing the solution requires a bit of Unix experience.  To write a new-user
    tutorial for this fix would be beyond my available time and possibly available
    skill.  You might try taking a print-out of this blog post to someone skilled
    in Unix/MacOS and see if they can help you out.\r\n\r\nGood luck!"
- id: 33545
  author: Andrew
  author_email: bunge@ufm.edu
  author_url: ''
  date: '2008-07-07 12:49:56 -0400'
  date_gmt: '2008-07-07 16:49:56 -0400'
  content: You saved my day. I connected the faulty machine to another Mac via FireWire
    and started in Target Mode (hold down the "T" while starting) and proceeded to
    delete the faulty files.
- id: 33546
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-07-07 13:24:29 -0400'
  date_gmt: '2008-07-07 17:24:29 -0400'
  content: A great way to solve the problem of having to understand the Unix command
    line utilities, Andrew!  If you have another (working) Mac around, your suggestion
    is definitely the way to go.
- id: 33654
  author: Chris
  author_email: otherpop@mac.com
  author_url: ''
  date: '2008-07-30 00:20:05 -0400'
  date_gmt: '2008-07-30 04:20:05 -0400'
  content: Thank you! Creating another account with admin rights and deleting the
    offending launch service files fixed this problem. Much appreciated!
- id: 33663
  author: Terri
  author_email: t_n@yahoo.com
  author_url: ''
  date: '2008-08-01 05:55:59 -0400'
  date_gmt: '2008-08-01 09:55:59 -0400'
  content: Thanks a lot, saved my day.
- id: 33795
  author: Francesco
  author_email: makevoid@gmail.com
  author_url: ''
  date: '2008-08-29 10:45:52 -0400'
  date_gmt: '2008-08-29 14:45:52 -0400'
  content: You're Great. Thank you it worked perfectly!
- id: 33812
  author: Manish Gupta
  author_email: manishgupta.mk@gmail.com
  author_url: ''
  date: '2008-09-08 03:38:11 -0400'
  date_gmt: '2008-09-08 07:38:11 -0400'
  content: we see logon looping problem while authenticating to a particualr website,
    could you please suggest if this solution will work for this kind of problem.
    Browsers that I've tried are firefox and safari, after entering my credentials
    the site tries to download an activeX control that is necessary to access this
    site. After this, I fall back on the same logon page? Any clue please? Thanks
- id: 33813
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-09-08 07:53:04 -0400'
  date_gmt: '2008-09-08 11:53:04 -0400'
  content: Manish -- this solution is for login loops at the operating system level
    (e.g. when the computer first starts), not for websites.  Sorry, I don't have
    any suggestions for the problem you are seeing.  Good luck.
- id: 33815
  author: patrick
  author_email: patrick@islandemail.com
  author_url: http://www.islandemail.com
  date: '2008-09-09 02:43:15 -0400'
  date_gmt: '2008-09-09 06:43:15 -0400'
  content: "This fixed the problem for me!!!\r\n\r\nThanks!!!"
- id: 33818
  author: J&oslash;rgen Wahlberg
  author_email: jorgen@jaws.no
  author_url: ''
  date: '2008-09-10 09:14:46 -0400'
  date_gmt: '2008-09-10 13:14:46 -0400'
  content: "You saved my day!\r\n\r\nAfter reading more than 100 blog entries, I finally
    found this one.\r\n\r\nRemoving com.apple.LaunchServices-* in /Library/Caches
    solved my login problem and I can finally log into my usual account.\r\n\r\nThanks!"
- id: 33841
  author: Eric Ridvan Uner
  author_email: eric@uner.com
  author_url: http://www.uner.com
  date: '2008-09-15 19:29:49 -0400'
  date_gmt: '2008-09-15 23:29:49 -0400'
  content: I just installed the 10.5.5. update, was stuck in a login loop, logged
    in as root and saw the launchd crashes in the log. I searched for help and found
    this page, and I just cannot thank you enough for the time you just saved me.  Safe
    boot and disabling login items did not help me, BTW.
- id: 33876
  author: Kev
  author_email: kevmaguire@gmail.com
  author_url: ''
  date: '2008-09-22 16:34:20 -0400'
  date_gmt: '2008-09-22 20:34:20 -0400'
  content: Amazing, worked like a charm. Thank goodness for people who know what they're
    doing!
- id: 34183
  author: rayn
  author_email: ray@obakk.com
  author_url: ''
  date: '2008-11-02 05:17:47 -0500'
  date_gmt: '2008-11-02 10:17:47 -0500'
  content: "These commands can be used by using single user above or by ssh from another
    machine.\r\nfollow these commands (n.b.: dont type \">\" \r\n\r\n> sudo -s (you
    will be asked to type your admin password (unless your root password is different)\r\ntyping
    sudo -s puts you as root, which is a super user that can do everything basically
    so be careful. If you are not asked for your password, you are already root so
    move on.\r\n\r\n> rm /Library/Caches/com.apple.LaunchServices*\r\nrm = remove
    - this will remove a file from the directory/folder Caches in the library folder
    on the root of the harddrive.  The file we want to delete \"com.apple.LaunchServices-023uid.csstore\"
    is the one causing the problem, however, there can be a few of them in the folder
    so we add a wildcard \"*\" to the end of the name to delete everything in that
    folder with \"com.apple.LaunchServices\"\r\n\r\n> reboot\r\nReboots the machine
    and brings you back to the login screen.\r\n\r\nI hope this helps people asking
    for instructions on how to follow the post."
- id: 34210
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-11-03 10:03:50 -0500'
  date_gmt: '2008-11-03 15:03:50 -0500'
  content: Thanks for posting the summary of instructions, Ray.  I edited your comment
    to correct one typo ("om" to "com").
- id: 34219
  author: Michael Rabinovich
  author_email: misha@badmagicnumber.net
  author_url: ''
  date: '2008-11-03 22:16:35 -0500'
  date_gmt: '2008-11-04 03:16:35 -0500'
  content: 'Wow, you really helped a brother out - and I mean Andrew as well.  Single
    user mode loads a read-only file system and deleting files is not allowed even
    with sudo, contrary to what a few people said here.  Andrew was right though -
    target disk mode into another mac is the easiest thing (at least for me).  Apple
    should pay you with a money and praise for giving people what they should be giving
    them: a quick and easy solution instead of reinstalling the OS!!'
- id: 34223
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-11-04 09:11:06 -0500'
  date_gmt: '2008-11-04 14:11:06 -0500'
  content: 'Thanks for the complement, Michael.  You are correct that under normal
    circumstances, a boot into single-user mode does not allow one to make modifications
    to the disk.  (The disk is mounted in read-only mode.)  One can use the following
    command, though, immediately after booting into single user mode to enable read-write
    access to the disk:  mount -uw /'
- id: 34270
  author: Anmibe
  author_email: Software@Anmibe.DE
  author_url: ''
  date: '2008-11-10 15:29:52 -0500'
  date_gmt: '2008-11-10 20:29:52 -0500'
  content: "You described my problem with my day-by-day account on MacOS X Leopard
    10.5.5. I already had the idea of a problem with the launch items, but I overloooked
    the existence of launch services outside of my Account/Library/Caches. With the
    root a account I solved it in few seconds.\r\nThx you made my day."
- id: 34293
  author: Mark C
  author_email: markchow@hotmail.com
  author_url: ''
  date: '2008-11-16 23:22:42 -0500'
  date_gmt: '2008-11-17 04:22:42 -0500'
  content: Thank you, thank you, thank you. Took forever to find this page but glad
    I did. So easy, especially in Target mode.
- id: 34307
  author: andokal
  author_email: avery100@gmail.com
  author_url: ''
  date: '2008-11-20 20:30:28 -0500'
  date_gmt: '2008-11-21 01:30:28 -0500'
  content: "You saved my mac, my user and quite possibly, my job! \r\n\r\nCheers!"
- id: 34314
  author: Daniel
  author_email: daniel.croll@gmx.ch
  author_url: ''
  date: '2008-11-22 13:36:58 -0500'
  date_gmt: '2008-11-22 18:36:58 -0500'
  content: "Wow, great hint!! You saved myself loads of time and hassles this weekend!\r\n\r\nMany
    thanks!\r\n\r\nCheers,\r\nDaniel"
- id: 34316
  author: ippei
  author_email: ippei.ukai@gmail.com
  author_url: ''
  date: '2008-11-22 22:32:15 -0500'
  date_gmt: '2008-11-23 03:32:15 -0500'
  content: "I couldn't login to my account and found you with \"UserEventAgent segmentation
    fault\". Now I'm back in business thanks to your tip.\r\n\r\nThank you thank you
    thank you so much!"
- id: 34354
  author: MAC won't advance to login screen from APPLE logo - macosx.com
  author_email: ''
  author_url: http://macosx.com/forums/mac-os-x-system-mac-software/304161-mac-won-t-advance-login-screen-apple-logo.html
  date: '2008-12-05 20:41:42 -0500'
  date_gmt: '2008-12-06 01:41:42 -0500'
  content: "<!--%kramer-ref-pre%-->[...] startup picture was shown and then the login
    screen came back. I found following url, that helped: Fixing a Mac OSX Leopard
    Login Loop Caused by Launch Services.  The idea is to boot using the installation
    DVD, go to the /Library/Cache directory (using [...]<!--%kramer-ref-post%-->"
- id: 34409
  author: Sumanth
  author_email: k.sumanth@gmail.com
  author_url: ''
  date: '2008-12-25 13:17:22 -0500'
  date_gmt: '2008-12-25 18:17:22 -0500'
  content: "Thanks for the tip. Works like a charm. \r\n\r\n1) Logged into single
    user mode. \r\n2) Gave write permissions to modify the files. mount -uw /\r\n3)
    Removed the files u specified."
- id: 34473
  author: simon
  author_email: simont@gmx.ch
  author_url: ''
  date: '2009-01-05 05:59:27 -0500'
  date_gmt: '2009-01-05 10:59:27 -0500'
  content: "you saved another persons day!!! thanx\r\nsome things were lost, though.
    mail configuration and dock setup"
- id: 34636
  author: Dan Byler
  author_email: dbyler@gmail.com
  author_url: http://bylr.net/
  date: '2009-02-04 14:41:08 -0500'
  date_gmt: '2009-02-04 19:41:08 -0500'
  content: Thanks for posting this--I ran into the login loop this afternoon, and
    removing the caches solved the issue.
- id: 35185
  author: T. Tauri
  author_email: tee.tauri@gmail.com
  author_url: ''
  date: '2009-04-11 12:41:30 -0400'
  date_gmt: '2009-04-11 16:41:30 -0400'
  content: Thank you! Was looking for clues to my own login loop for most of a day
    before I found your page. Worked like a charm!
- id: 35188
  author: Rasmus Groth
  author_email: rasmusgroth@gmail.com
  author_url: ''
  date: '2009-04-11 22:35:00 -0400'
  date_gmt: '2009-04-12 02:35:00 -0400'
  content: "U SAVED MY LIFE!\r\n\r\nThank you soooo much!"
- id: 35320
  author: Steve
  author_email: vondrell@udayton.edu
  author_url: ''
  date: '2009-04-25 14:55:23 -0400'
  date_gmt: '2009-04-25 18:55:23 -0400'
  content: 'Thank you! I had shutdown my MacBook Pro at the office then taken it home
    and powered it up. It never got to the login. I booted into Single User Mode and
    issued fsck -f which found no problem. Hoping the problem was a preference, I
    renamed /Library/Preferences and rebooted but to no avail.  Back in Single User
    Mode, I looked at /var/log/system.log.  Lots of messages contained "com.apple.loginwindow[xx]:
    LaunchServices: bad alias at xxxxxxxxxx". When I googled "com.apple.loginwindow
    launchservices", I found your post. I had also noticed in system.log that lsregister
    had crashed. I reasoned that your solution of getting rid of launch services cache
    files would likely solve my problem and could do no harm. Being perhaps overly
    cautious, I moved the cache files to another directory then restarted.  I was
    rewarded with a login window.  All is well. Thank you so much for publishing this
    article!'
- id: 35340
  author: James
  author_email: jamesram@hawaii.edu
  author_url: ''
  date: '2009-04-27 05:12:09 -0400'
  date_gmt: '2009-04-27 09:12:09 -0400'
  content: You are my savior! This forum really helped out a lot. Thanks!
- id: 35845
  author: Derrick
  author_email: heckcare.der@gmail.com
  author_url: http://www.pbase.com/derrickheng
  date: '2009-05-09 02:13:13 -0400'
  date_gmt: '2009-05-09 06:13:13 -0400'
  content: "Wow! You just saved me day! I thought the OS was a goner already.\r\n\r\nThank
    God I found ur link!!!!\r\n\r\nBRILLIANT!"
- id: 36361
  author: katso viestiketjua - Kaikki kaatuu k&auml;ynnistyksess&auml; - Hopeinen
    Omena
  author_email: ''
  author_url: http://www.hopeinenomena.net/viewtopic.php?f=50&amp;t=126426
  date: '2009-06-06 05:24:45 -0400'
  date_gmt: '2009-06-06 09:24:45 -0400'
  content: "<!--%kramer-ref-pre%-->[...] sycophant p&auml;iv&auml;m&auml;&auml;r&auml;
    6.6.2009 klo 12.24  http://dltj.org/article/macosx-launchse ... -loop-fix/ t&auml;m&auml;
    [...]<!--%kramer-ref-post%-->"
- id: 36766
  author: Hugo
  author_email: hgoeury@hotmail.com
  author_url: ''
  date: '2009-06-22 21:02:47 -0400'
  date_gmt: '2009-06-23 01:02:47 -0400'
  content: "I wish I could say it worked for me too but unfortunately it didn't...
    As it's mounted read only I tried:  mount -uw / and all I got was a \r\n\"HFS:
    Removed 1 orphaned unlinked files or directories\"  what is that supposed to mean
    and what could I do about it?.... I really thought that Mac never crashed :'("
- id: 36774
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2009-06-23 16:37:50 -0400'
  date_gmt: '2009-06-23 20:37:50 -0400'
  content: |-
    What happens after getting "HFS: Removed..." message?  Normally, I wouldn't be concerned about that because it sounds like the system is cleaning up after an abrupt shutdown or restart.  I would think the command line would return and you would be able to continue with the commands in read-write mode.  But, honestly, I haven't encountered this message before, so I'm just guessing.  Macs rarely crash (in my experience) which is why I was so surprised about this particular problem.  (And that the looping login problem still continues to exist by the reports of other comments on this blog post.)

    Good luck!
- id: 38210
  author: Steve K
  author_email: steven@kehlet.cx
  author_url: ''
  date: '2009-09-23 12:59:16 -0400'
  date_gmt: '2009-09-23 16:59:16 -0400'
  content: Thank you!  Saved me.
- id: 38283
  author: Jim
  author_email: post@jmflyer.com
  author_url: ''
  date: '2009-10-06 11:00:27 -0400'
  date_gmt: '2009-10-06 15:00:27 -0400'
  content: Worked like a charm!  I can't thank you enough for posting this!
- id: 38546
  author: 'Mac Corruption: The Login Loop | Tuxrocket'
  author_email: ''
  author_url: http://tuxrocket.com/archives/tinker/53
  date: '2009-11-18 01:02:48 -0500'
  date_gmt: '2009-11-18 06:02:48 -0500'
  content: "<!--%kramer-ref-pre%-->[...] I stumbled upon a post on a third party site
    that solved the problem. Basically my login caches had become corrupt. To fix
    it you have to remove (or move out of the [...]<!--%kramer-ref-post%-->"
- id: 38666
  author: Macforum.ch - Das schweizer Forum f&uuml;r Mac-User - Macbook OSX - blue
    screen - erneute anmeldung - loop
  author_email: ''
  author_url: http://www.macforum.ch/forum/ftopic5977-30.html
  date: '2009-12-04 15:02:58 -0500'
  date_gmt: '2009-12-04 20:02:58 -0500'
  content: "<!--%kramer-ref-pre%-->[...] was eigentlich zu 100% auf meinen Fall zutrifft.
    Leider hat mir aber das Vorgehen nicht geholfen:  http://dltj.org/article/macosx-launchservices-login-loop-fix/
    \  Kann mir jemand sagen wie ich meine Daten am besten von meiner HD rauskriege
    ohne dass ich mich [...]<!--%kramer-ref-post%-->"
- id: 41848
  author: Iain
  author_email: iainforsyth@hotmail.com
  author_url: ''
  date: '2010-01-19 01:35:52 -0500'
  date_gmt: '2010-01-19 06:35:52 -0500'
  content: "I was having this login problem, so I logged into single user mode and
    deleted those -023uid.csstore files. Once I exited single user mode I could log
    in fine.\r\n\r\nHowever, everything seemed to run very slowly, so I restarted.
    But ever since then, if I try to start the computer, it goes to the gray start
    up screen for a little while then shuts itself down. In verbose mode, this shows
    up as \"disk0s2: I/O error\" before it shuts down.\r\n\r\nI can still log in to
    single user mode though. If I try \"/sbin/fsck -fy\", then the first time it says
    \"disk02s: I/O error\", \"Invalid node structure (4, 861)\" and \"volume check
    failed\". The second time I try it, it says \"disk0s2: I/O error\", \"Invalid
    sibling link (4,861)\", \"Rebuilding Catalog B-tree\", and \"The volume Macintosh
    HD could not be repaired\".\r\n\r\nAlso, if I go into single user mode, then log
    out of single user mode, the computer tries to boot and then shuts itself down
    like before. But if I first type \"/sbin/mount -uw /\", which I used before to
    let me delete the LaunchServices files, then if I exit single user mode, the system
    does boot and I can log in. But everything runs super slowly; it takes the computer
    a good 5 seconds to respond to a single click.\r\n\r\nI do have boot camp though,
    and if I start the computer in windows then everything goes perfectly, so I hope
    that means it's just a problem with the OS instead of my hard drive dying.\r\n\r\nAny
    idea what's going on? I don't have an easily obtainable leopard install disk,
    so is there any easy way to fix it or will I have to reinstall the OS?"
- id: 41866
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-01-19 09:22:50 -0500'
  date_gmt: '2010-01-19 14:22:50 -0500'
  content: Iain -- it sure does sound like a hard drive is failing, even though Windows
    boots up fine.  You might want to see if you can get it into an Apple store for
    someone to take a look at it.  Good luck!
- id: 42061
  author: Iain
  author_email: iainforsyth@hotmail.com
  author_url: ''
  date: '2010-01-21 20:45:08 -0500'
  date_gmt: '2010-01-22 01:45:08 -0500'
  content: Wiping the hard drive and reinstalling OS X fixed the problem. Just glad
    the hard drive wasn't broken.
- id: 42656
  author: Won't Login - Mac-Forums.com
  author_email: ''
  author_url: http://www.mac-forums.com/forums/os-x-operating-system/188458-wont-login.html#post989172
  date: '2010-01-28 15:08:46 -0500'
  date_gmt: '2010-01-28 20:08:46 -0500'
  content: "[...] tab of the Account Preference Pane) and had to be reconstructed.
    \   Link to the Article: Fixing a Mac OSX Leopard Login Loop Caused by Launch
    Services | Disruptive Library Technology Jester  [...]"
- id: 43904
  author: What's the cure for endless grey wheel at startup?
  author_email: ''
  author_url: http://forums.macresource.com/read.php?1,885137
  date: '2010-02-09 00:55:24 -0500'
  date_gmt: '2010-02-09 05:55:24 -0500'
  content: "<!--%kramer-ref-pre%-->[...] startup?Posted by: tronnei Date: February
    08, 2010 11:41PM Happened to me too. Here&#39;s the solution:[dltj.org]I used
    target disc mode to go in and delete the corrupted files.Options:&nbsp; Reply&nbsp;&bull;
    [...]<!--%kramer-ref-post%-->"
- id: 47942
  author: bugmatic
  author_email: bugmatic@yahoo.com.au
  author_url: ''
  date: '2010-02-26 22:56:10 -0500'
  date_gmt: '2010-02-27 03:56:10 -0500'
  content: The greatest OSX tip I have found thus far. Saved me from a short stay
    in the psych ward.  Thankyou!!!
- id: 65171
  author: If a user account keeps crashing on login what do you do? &laquo; The Geek
    Interview
  author_email: ''
  author_url: ''
  date: '2010-04-17 22:43:27 -0400'
  date_gmt: '2010-04-18 02:43:27 -0400'
  content: "<!--%kramer-ref-pre%-->[...] http://dltj.org/article/macosx-launchservices-login-loop-fix/
    [...]<!--%kramer-ref-post%-->"
- id: 66500
  author: Mark
  author_email: mcrosbie@mac.com
  author_url: ''
  date: '2010-04-25 20:09:22 -0400'
  date_gmt: '2010-04-26 00:09:22 -0400'
  content: What a great post.   A true lifesaver.  Direct and to the point, only tampering
    with the files needed to resolve.  I wish most folks could be as focused on RCA
    (Root Cause Analysis) vs. the sorry you'll need to totally rebuild your system
    from scratch approach.   THANK YOU!
- id: 71689
  author: Riz Muhammad
  author_email: rizzy63@hotmail.com
  author_url: ''
  date: '2010-05-30 22:30:37 -0400'
  date_gmt: '2010-05-31 02:30:37 -0400'
  content: Dude you are a total total legend. Saved me hours... Cheers mate :)
- id: 72800
  author: ''
  author_email: ''
  author_url: ''
  date: '2010-06-08 16:33:06 -0400'
  date_gmt: '2010-06-08 20:33:06 -0400'
  content: "<!--%kramer-ref-pre%-->[...]  [...]<!--%kramer-ref-post%-->"
- id: 82479
  author: worked perfectly!
  author_email: paintballnaked@gmail.com
  author_url: ''
  date: '2010-08-10 17:17:30 -0400'
  date_gmt: '2010-08-10 21:17:30 -0400'
  content: "This fixed it immediately.  \r\nI was having difficulty at first deleting
    the file from single user mode but then i got it. \r\nI used the following steps
    exactly: (dont type >)\r\n\r\n1. > Sudo -s                 no root password so
    i didnt have to enter mine.\r\n2. > /sbin/mount -uw /\r\n3. > rm /Library/Caches/com.apple.LaunchServices*\r\n4.
    > reboot\r\n\r\nEverything worked right after."
- id: 82558
  author: Launch Services Cache Corruption | My Gorram Frakking Blog
  author_email: ''
  author_url: http://blog.roderickmann.org/2003/05/launch-services-cache-corruption/
  date: '2010-08-11 03:11:40 -0400'
  date_gmt: '2010-08-11 07:11:40 -0400'
  content: "<!--%kramer-ref-pre%-->[...] allowed login to proceed normally. Update
    (2009-03-10): Thanks to this post, I now know that the filenames have changed
    in more recent OS releases. Launch Services caches [...]<!--%kramer-ref-post%-->"
- id: 88920
  author: Wayne Hatch
  author_email: waynehatch42@gmail.com
  author_url: ''
  date: '2010-09-17 21:37:26 -0400'
  date_gmt: '2010-09-18 01:37:26 -0400'
  content: "1 profile out of 4 wouldn't launch and I couldn't fix it. Found which
    which uid was at fault by launching the others and looking at the modification
    date.\r\nDeleted the relevant file and all is good. Thanks SOOO much for your
    post.\r\nRegards Wayne"
- id: 90062
  author: Josh
  author_email: joshgill@gmail.com
  author_url: http://www.newepicmedia.com
  date: '2010-09-24 19:10:50 -0400'
  date_gmt: '2010-09-24 23:10:50 -0400'
  content: Worked like a charm, and saved me another 5 hours of work on a computer
    I had spent all day fixing for a client. I should buy you a beer!
- id: 101286
  author: Sammy
  author_email: samson.kirigua@gmail.com
  author_url: ''
  date: '2010-11-19 05:56:05 -0500'
  date_gmt: '2010-11-19 10:56:05 -0500'
  content: Worked like a charm thanks dude happy i don't have to re-install
- id: 102600
  author: monique
  author_email: monique@dtp-enzo.nl
  author_url: ''
  date: '2010-11-25 13:55:07 -0500'
  date_gmt: '2010-11-25 18:55:07 -0500'
  content: "... and it worked!\r\n\r\nWanna marry me?\r\n(please don't tell my bf
    I asked...)"
- id: 106629
  author: apple.spot.ee &bull; Vaata teemat - Paluks ruttu abi macbookiga !!!
  author_email: ''
  author_url: http://apple.spot.ee/viewtopic?f=50&amp;t=18936
  date: '2010-12-14 18:59:16 -0500'
  date_gmt: '2010-12-14 23:59:16 -0500'
  content: "<!--%kramer-ref-pre%-->[...] &auml;kki on nendest abi:http://dltj.org/article/macosx-launchse
    ... -loop-fix/http://confuseddevelopment.blogspot.com ... -os-x.htmlPS kui ma
    &otilde;igesti m&auml;letan, siis endal kunagi [...]<!--%kramer-ref-post%-->"
- id: 106871
  author: Jon
  author_email: term3186@hotmail.com
  author_url: ''
  date: '2010-12-15 19:23:25 -0500'
  date_gmt: '2010-12-16 00:23:25 -0500'
  content: Haaaa I've been having this problem all afternoon and I need my laptop
    for a final exam tomorrow!  Hooray for Jester and Rayn.  Saved my ass.
- id: 107383
  author: Martin
  author_email: tinorebel@yahoo.it
  author_url: ''
  date: '2010-12-18 05:57:20 -0500'
  date_gmt: '2010-12-18 10:57:20 -0500'
  content: "Thank you so much!\r\nThis post saved my day ..... or the entire week.\r\n
    I was able to fix the problem logging in from another computer connected via wi-fi
    with my username and password. I just moved cache files out of the folder and
    restarted.\r\nThe problem was solved with no other issue."
- id: 129231
  author: Serious mac problem, advice! - Overclockers UK Forums
  author_email: ''
  author_url: http://forums.overclockers.co.uk/showthread.php?t=18255183
  date: '2011-03-23 11:11:55 -0400'
  date_gmt: '2011-03-23 15:11:55 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Sounds like the infamous login loop. Tried
    this?  http://dltj.org/article/macosx-launc...ogin-loop-fix/ [...]<!--%kramer-ref-post%-->"
- id: 148705
  author: V.
  author_email: vschwegman@gmail.com
  author_url: ''
  date: '2011-06-08 22:00:00 -0400'
  date_gmt: '2011-06-09 02:00:00 -0400'
  content: "I never post comments, but I have to say that I can't thank you enough
    for your post! I wouldn't have had enough space on my drive for archive and install.
    I would have had to delete and possibly move files to my external drive via command
    line otherwise. \r\n\r\nI had another admin account that allowed me to log in
    on my Mac so I simply browsed to the system Library folder, followed the path,
    and moved the appropriate three files.  Problem resolved!"
- id: 159724
  author: Guy Hodge
  author_email: ''
  author_url: http://twitter.com/guyhodge/status/47951700484562944
  date: '2011-03-16 09:25:50 -0400'
  date_gmt: '2011-03-16 13:25:50 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">@TheGotting Also this, gotta scroll down on phones:
    http://t.co/cHzLXhn</span></span>'
- id: 161180
  author: MacTechHelp
  author_email: ''
  author_url: http://twitter.com/mactechhelp/status/5848489622
  date: '2009-11-19 04:15:03 -0500'
  date_gmt: '2009-11-19 09:15:03 -0500'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">@jackamick for do it yourself, see - http://bit.ly/11UQet</span></span>
- id: 161181
  author: qurgh HoD
  author_email: ''
  author_url: http://twitter.com/qurgh/status/3539899569
  date: '2009-08-25 18:26:02 -0400'
  date_gmt: '2009-08-25 22:26:02 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">@tuftedpuffin What version of Mac OS is it? I
    found this article that seems to describe what you are saying:  http://tr.im/x5qD</span></span>'
- id: 161182
  author: Roshni
  author_email: ''
  author_url: http://twitter.com/roshnimo/status/2235620989
  date: '2009-06-19 08:39:39 -0400'
  date_gmt: '2009-06-19 12:39:39 -0400'
  content: |-
    <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span class="topsy_trackback_content">@aryayush @aalaap This is the link: http://bit.ly/HqODJ
     Thanks a lot. :)</span></span>
- id: 161183
  author: andokal
  author_email: ''
  author_url: http://twitter.com/andokal/status/1015701289
  date: '2008-11-21 00:46:16 -0500'
  date_gmt: '2008-11-21 05:46:16 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">The Jester saved my mac''s life (and quite possibly
    my job): http://tinyurl.com/5n7lwj</span></span>'
- id: 172293
  author: CTS Ltd.
  author_email: ''
  author_url: http://twitter.com/ctsdotnet/status/118952207428239361
  date: '2011-09-28 07:36:30 -0400'
  date_gmt: '2011-09-28 11:36:30 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Logging into a Mac and then logged straight back
    out? We had to create a new account &amp; clear the Launch Services Cache http://t.co/W9dIoYlW</span></span>
- id: 174967
  author: jul
  author_email: juliengrunder@hotmail.com
  author_url: ''
  date: '2011-10-09 14:43:51 -0400'
  date_gmt: '2011-10-09 18:43:51 -0400'
  content: "I love you man!\r\nYou just saved my trip in brazil!\r\nI&acute;m going
    to drink a beer right know."
- id: 179267
  author: Kevin Wood-Friend
  author_email: kevin.wood.friend@gmail.com
  author_url: ''
  date: '2011-10-24 14:18:54 -0400'
  date_gmt: '2011-10-24 18:18:54 -0400'
  content: This worked for me in Snow Leopard. Thanks a lot!
- id: 189473
  author: TechnoBob
  author_email: bob@bobleedom.com
  author_url: ''
  date: '2011-11-30 02:41:02 -0500'
  date_gmt: '2011-11-30 07:41:02 -0500'
  content: "Under 10.6.8, Snow Leopard,\r\nI have this exact problem, but I don't
    see the file \r\nLibrary/Caches/com.apple.LaunchServices\r\n\r\nWhere is it?"
- id: 189647
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-11-30 15:56:29 -0500'
  date_gmt: '2011-11-30 20:56:29 -0500'
  content: "TechnoBob: You won't find it as a file named exactly <code>/Library/Caches/com.apple.LaunchServices</code>
    -- but the file name will start with <code>com.apple.LaunchServices</code>.  These
    two commands should do it:  <ol>\r\n\t<li><code>cd /Library/Caches</code></li>\r\n\t<li><code>rm
    com.apple.LaunchServices*</code></li>\r\n</ol>"
- id: 189649
  author: TechnoBob
  author_email: bob@bobleedom.com
  author_url: ''
  date: '2011-11-30 16:17:08 -0500'
  date_gmt: '2011-11-30 21:17:08 -0500'
  content: "Thanks, Peter, but I wasn't specific enough. More precisely, I am looking
    at the top level of my HD from an administrator (not root) account and I see NO
    files in /Library/Caches or in /System/Library/Caches that begin with (or contain)
    the string\r\ncom.apple.LaunchServices\r\n\r\nHow, or where, should I be looking
    for these files?\r\n\r\nThanks! (I'm losing track of the many hours I've spent
    on this!)"
- id: 189668
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-11-30 17:13:42 -0500'
  date_gmt: '2011-11-30 22:13:42 -0500'
  content: Hmmm -- something must have changed.  I haven't had this problem since
    Leopard (although judging by the comments to this post the problem still exists
    in some form).  I looked in my own <code>/Library/Caches</code> directory under
    Lion and I don't see any files starting with "<code>com.apple.LaunchServices</code>"
    either.  In fact, there are no files matching the pattern "<code>/Library/*/*LaunchServices*</code>"
    at all.  I can only guess that 'lsregister' is reading its values from some other
    cache file (if it is indeed still the same problem).  Unfortunately, I don't know
    where that might be...  Good luck!
- id: 217246
  author: Lucas
  author_email: lucas.draycott@gmail.com
  author_url: ''
  date: '2012-02-03 22:23:24 -0500'
  date_gmt: '2012-02-04 03:23:24 -0500'
  content: "Okay, I know that i've come to the right place, everyone has seemed to
    have resolved the issue. However i'm not a very good with computers and i need
    the exact commands i enter after i enter \"single user mode\". If anyone could
    help me it would be greatly appreciated\r\nthanks"
- id: 218359
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2012-02-06 21:31:42 -0500'
  date_gmt: '2012-02-07 02:31:42 -0500'
  content: "Lucas -- this solution to the problem seems to only work for some versions
    of Snow Leopard and earlier.  If you have upgraded to Lion and are still seeing
    the login loop problem, then something else is going on.  Once you boot into single
    user mode, the three commands would be:\r\n\r\n<ul>\r\n\t<li>/sbin/mount -uw /</li>\r\n
    \t<li>rm /Library/Caches/com.apple.LaunchServices* </li>\r\n\t<li>reboot</li>\r\n</ul>\r\n\r\n\r\n<p>If
    at the middle step you see \"No such file or directory\" then something else is
    going on. Good luck.</p>"
- id: 218807
  author: Lucas
  author_email: lucas.draycott@gmail.com
  author_url: ''
  date: '2012-02-07 21:54:25 -0500'
  date_gmt: '2012-02-08 02:54:25 -0500'
  content: Thank you peter for your help, unfortunately the "no directory found" is
    showing up. I am currently running Snow Leopard 10.6.8. Do you think upgrading
    to lion would fix the issue?
- id: 219054
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2012-02-08 12:48:39 -0500'
  date_gmt: '2012-02-08 17:48:39 -0500'
  content: I can't guess whether upgrading to Lion will fix it or not.  I haven't
    seen this problem in years, although others have seen it more recently.  If the
    same underlying problem is still there, the file location has clearly moved.  I
    tried looking in some of the obvious places, but I can't find its new location.
- id: 221044
  author: Wombat
  author_email: wombat@octa4.net.au
  author_url: ''
  date: '2012-02-13 19:01:11 -0500'
  date_gmt: '2012-02-14 00:01:11 -0500'
  content: "Similar problem: one user account out of 5 would not load, still running
    Leopard - OSX 10.5.8.\r\nThe account would spend several minutes trying to load
    after login, and then revert to the login screen.\r\nDeleting the files as you
    suggest here worked perfectly.\r\nThank you so much for posting this here (and
    to google who enabled me to find it!)"
- id: 230084
  author: William Gacquer
  author_email: wgacquer@yahoo.fr
  author_url: http://www.amilto.com/
  date: '2012-03-09 04:56:39 -0500'
  date_gmt: '2012-03-09 09:56:39 -0500'
  content: "Same problem, your solution and ... TADAM! it works!\r\nThx"
- id: 250414
  author: DesignatedFlow
  author_email: ''
  author_url: http://twitter.com/designatedflow/status/202031848799477760
  date: '2012-05-14 13:45:20 -0400'
  date_gmt: '2012-05-14 17:45:20 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">This guy just saved me from going crazy: Fixing
    a Mac OSX Login Loop Caused by Launch Services http://t.co/HT8khO8o</span></span>'
- id: 270544
  author: Dw33b
  author_email: paul.osterwald@live.com
  author_url: ''
  date: '2012-07-02 23:58:54 -0400'
  date_gmt: '2012-07-03 03:58:54 -0400'
  content: "Peter,\r\n\r\nI guess I'm screwed because it happened to me in Lion after
    the fix to 10.7.4.  I get the initial boot greyish screen, then the login screen
    and when I login, back to the login screen again.  Have you run into this on Lion
    at all and possibly have an answer to share?\r\n\r\nDa Dw33b"
- id: 270820
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2012-07-03 15:31:14 -0400'
  date_gmt: '2012-07-03 19:31:14 -0400'
  content: Something has changed in the boot process, and this fix no longer seems
    to apply.  It hasn't happened to me again, so I can't tell if the same underlying
    problem is still there in a different form or if your symptoms represent something
    new.  Good luck!
- id: 272972
  author: Upgrade 10.4.11 to 10.5 (Tiger to Leopard)
  author_email: ''
  author_url: http://www.hv20.com/showthread.php?46033-Upgrade-10-4-11-to-10-5-(Tiger-to-Leopard)&amp;p=445165
  date: '2012-07-08 05:30:58 -0400'
  date_gmt: '2012-07-08 09:30:58 -0400'
  content: "<!--%kramer-ref-pre%-->[...] out, unfortunately it works perfectly for
    Leopard. Ut the cache file location is changed in SL  http://dltj.org/article/macosx-launc...ogin-loop-fix/
    \ Glad I read the comments.      Vice President, Team HVFF - http://hvfffollowfocus.webs.com/
    \       [...]<!--%kramer-ref-post%-->"
- id: 290163
  author: applespot.ee &bull; Vaata teemat - Paluks ruttu abi macbookiga !!!
  author_email: ''
  author_url: http://applespot.ee/viewtopic.php?f=50&amp;t=18936
  date: '2012-08-17 07:28:26 -0400'
  date_gmt: '2012-08-17 11:28:26 -0400'
  content: "<!--%kramer-ref-pre%-->[...] &auml;kki on nendest abi:http://dltj.org/article/macosx-launchse
    ... -loop-fix/http://confuseddevelopment.blogspot.com ... -os-x.htmlPS kui ma
    &otilde;igesti m&auml;letan, siis endal kunagi [...]<!--%kramer-ref-post%-->"
- id: 453762
  author: Upgrade 10.4.11 to 10.5 (Tiger to Leopard)
  author_email: ''
  author_url: http://hddv.net/showthread.php?46033-Upgrade-10-4-11-to-10-5-(Tiger-to-Leopard)
  date: '2013-02-28 17:27:26 -0500'
  date_gmt: '2013-02-28 22:27:26 -0500'
  content: "<!--%kramer-ref-pre%-->[...] out, unfortunately it works perfectly for
    Leopard. Ut the cache file location is changed in SL  http://dltj.org/article/macosx-launc...ogin-loop-fix/
    \ Glad I read the comments.      Vice President, Team HVFF - http://hvfffollowfocus.webs.com/
    HV [...]<!--%kramer-ref-post%-->"
- id: 482555
  author: osx - Login loop after OS X 10.8 update (WindowServer problem?) - Ask Different
  author_email: ''
  author_url: http://apple.stackexchange.com/questions/86601/login-loop-after-os-x-10-8-update-windowserver-problem
  date: '2013-03-25 07:46:08 -0400'
  date_gmt: '2013-03-25 11:46:08 -0400'
  content: "<!--%kramer-ref-pre%-->[...] http://dltj.org/article/macosx-launchservices-login-loop-fix/
    [...]<!--%kramer-ref-post%-->"
- id: 518064
  author: Mike Marrotte
  author_email: marrotte@gmail.com
  author_url: ''
  date: '2013-04-16 10:55:18 -0400'
  date_gmt: '2013-04-16 14:55:18 -0400'
  content: Late 2012 model.  Still works like a charm.  Thanks!
- id: 520358
  author: cosmicstresshead
  author_email: bensmylie@gmail.com
  author_url: http://defendersofthemirth.com
  date: '2013-04-17 14:15:10 -0400'
  date_gmt: '2013-04-17 18:15:10 -0400'
  content: "I think I just solved my login loop issue by logging into the affected
    account in safe mode, going into the accounts control panel and removing all the
    login items from there.  Seems to have worked.  Worth a try before potentially
    cocking something up in the terminal!\r\n\r\nNote: At the same time as removing
    the login items, I set the account to log in automatically.  This was not the
    most scientific of approaches, as I'm now not sure which one worked.  But something
    worked and I am now past the login loop.  Hoorah!"
- id: 520361
  author: cosmicstresshead
  author_email: bensmylie@gmail.com
  author_url: http://defendersofthemirth.com
  date: '2013-04-17 14:17:19 -0400'
  date_gmt: '2013-04-17 18:17:19 -0400'
  content: 'Re: above, I am running Snow Leopard (10.6.6)'
- id: 520365
  author: cosmicstresshead
  author_email: bensmylie@gmail.com
  author_url: http://defendersofthemirth.com
  date: '2013-04-17 14:20:49 -0400'
  date_gmt: '2013-04-17 18:20:49 -0400'
  content: Apologies, I just re-read through the thread and I see this doesn't work
    for everyone.
- id: 625303
  author: philalonso
  author_email: philalonso@gmail.com
  author_url: ''
  date: '2013-06-30 19:37:39 -0400'
  date_gmt: '2013-06-30 23:37:39 -0400'
  content: "I'm able to look at the system.log file, but I don't see anything like
    this. There are a number of additional system.log files with appendages, like
    system.log.0.bz2 through system.log.7.bz2. \r\nAny ideas?"
- id: 625320
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2013-06-30 20:46:35 -0400'
  date_gmt: '2013-07-01 00:46:35 -0400'
  content: "The system.log.?.bz2 are just the rotated and compressed versions of the
    log files.  I'd be willing to bet that if the same problem I was having was occurring
    for you, you'd see the messages in the most recent system.log file.\r\n\r\nIf
    the underlying problem I saw and corrected back in OSX 10.5 is still there, then
    location of the cache files that would need to be cleared has changed and so my
    instructions no longer work.  A few months ago cosmicstresshead posted above a
    solution that involves logging into the system in safe mode and removing all the
    login items.  That is something that is certainly worth a try, but I don't have
    direct experience with that solution."
- id: 627059
  author: Josh
  author_email: joshuajlee@gmail.com
  author_url: ''
  date: '2013-07-04 09:49:51 -0400'
  date_gmt: '2013-07-04 13:49:51 -0400'
  content: 'Hi, I was in the camp of having this issue in Snow Leopard and therefore
    being unable to apply the posted, outdated fix. Here is a more current version
    of the fix which solved my problem: http://junkheap.net/blog/2011/09/22/solving-a-login-loop-in-mac-os-x-lion-due-to-corrupt/'
- id: 627075
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2013-07-04 10:32:44 -0400'
  date_gmt: '2013-07-04 14:32:44 -0400'
  content: Ah! That's where the file went.  Thanks for the link to your post, Josh.
- id: 627198
  author: Josh
  author_email: joshuajlee@gmail.com
  author_url: ''
  date: '2013-07-04 16:19:49 -0400'
  date_gmt: '2013-07-04 20:19:49 -0400'
  content: not my post, just passin it along :)
- id: 630455
  author: Antonio
  author_email: schjeldedafonseca@gmail.com
  author_url: ''
  date: '2013-07-10 12:43:20 -0400'
  date_gmt: '2013-07-10 16:43:20 -0400'
  content: "For those who couldn't get it to work with this solution (no such file)
    is there any other way?  \r\nI'm using leopard and stuck with a useless computer.
    Have no extra mac nor a multi-user login set up."
- id: 630460
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2013-07-10 12:54:55 -0400'
  date_gmt: '2013-07-10 16:54:55 -0400'
  content: 'You''ll need to boot to single user mode (<a href="http://support.apple.com/kb/ht1492"
    rel="nofollow">Mac OS X: How to start up in single-user or verbose mode</a>),
    then run the command `<code>mount -uw /</code>` to be able to write to the file
    system.  Then you should be able to follow the commands here or in the <a href="http://junkheap.net/blog/2011/09/22/solving-a-login-loop-in-mac-os-x-lion-due-to-corrupt/"
    rel="nofollow">follow up for later operating systems</a>.'
- id: 630496
  author: Antonio
  author_email: schjeldedafonseca@gmail.com
  author_url: ''
  date: '2013-07-10 14:02:02 -0400'
  date_gmt: '2013-07-10 18:02:02 -0400'
  content: "Thanks for the quick reply. \r\nI did manage to start in single user mode,
    did all the commands, after a few times i get the \"everything appeara to be ok\"
    (or similar) message and reboot. And then cry again because i'm still stuck. \r\nI
    dont have another user account, neither can I set up one before it goes back to
    the login screen... \r\nAnd i'm no super nerd, that latest tutorial i didn't really
    follow..."
- id: 630531
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2013-07-10 15:19:22 -0400'
  date_gmt: '2013-07-10 19:19:22 -0400'
  content: As one gets to single user mode and the command line, it is very easy to
    mess up your system worse than the problem you have now.  If the command line
    is something that isn't familiar to you, I'd suggest getting in touch with someone
    that is; that person can sit at the machine and run through the suggestions here
    and elsewhere to try to fix the problem.  Good luck!
- id: 650110
  author: Double logon screen
  author_email: ''
  author_url: http://www.tonymacx86.com/general-help/104492-double-logon-screen.html#post662758
  date: '2013-09-14 11:27:02 -0400'
  date_gmt: '2013-09-14 15:27:02 -0400'
  content: "[&#8230;] day, finally solved my own problem. From this article:  http://dltj.org/article/macosx-launc...ogin-loop-fix/
    \ Led me to this:  http://apple.stackexchange.com/quest...the-apps-twice  Simply
    open Terminal and [&#8230;]"
- id: 655866
  author: Login impossible (Leopard) - Forum Mac
  author_email: ''
  author_url: http://forums.macg.co/mac-os-x/login-impossible-leopard-270731.html
  date: '2014-02-22 02:05:47 -0500'
  date_gmt: '2014-02-22 07:05:47 -0500'
  content: "<!--%kramer-ref-pre%-->[&#8230;]  [&#8230;]<!--%kramer-ref-post%-->"
- id: 656238
  author: 'Mac Corruption: The Login Loop | Tuxrocket'
  author_email: ''
  author_url: http://dave.lyonmania.com/2008/10/31/mac-corruption-the-login-loop/
  date: '2014-03-18 13:01:43 -0400'
  date_gmt: '2014-03-18 17:01:43 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;] I stumbled upon a post on a third party
    site that solved the problem. Basically my login caches had become corrupt. To
    fix it you have to remove (or move out of the [&#8230;]<!--%kramer-ref-post%-->"
- id: 656668
  author: pierre
  author_email: couleaud.pierre@gmail.com
  author_url: ''
  date: '2014-04-14 05:41:09 -0400'
  date_gmt: '2014-04-14 09:41:09 -0400'
  content: "Hey,\r\nIt seems that I have the same kind of problem but i don't have
    those same files to delete. but other type of com.apple.LaunchServices&hellip;\r\nCan
    it be named in another way ?\r\n\r\nThanks for helping me&hellip;."
- id: 658245
  author: kingsley
  author_email: kingsleyihiaso@yahoo.com
  author_url: http://oracool11@blogspot.com
  date: '2014-07-03 09:20:55 -0400'
  date_gmt: '2014-07-03 13:20:55 -0400'
  content: I am having d same issue with my mbp late 08, when I try ur method it pops
    permission denied pls help.
- id: 658644
  author: ''
  author_email: ''
  author_url: http://www.macuser.de/forum/thema/532886-10-5-8-h%C3%A4ngt-nur-noch
  date: '2014-08-04 17:11:26 -0400'
  date_gmt: '2014-08-04 21:11:26 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;]  [&#8230;]<!--%kramer-ref-post%-->"
- id: 679595
  author: boots to log in screen, Blue screen, back to login | MacRumors Forums
  author_email: ''
  author_url: http://forums.macrumors.com/threads/boots-to-log-in-screen-blue-screen-back-to-login.522680/
  date: '2015-06-02 22:32:49 -0400'
  date_gmt: '2015-06-03 02:32:49 -0400'
  content: "<!--%kramer-ref-pre%-->[&#8230;] hunting around I discovered this post
    and solved a similar problem without having to reinstall: http://dltj.org/article/macosx-launchservices-login-loop-fix/
    \ Probably a bit late for daboogymahn but hopefully of use to others who might
    strike this issue. [&#8230;]<!--%kramer-ref-post%-->"
- id: 682096
  author: Sion
  author_email: smartgraphics@freenetname.co.uk
  author_url: ''
  date: '2015-11-02 11:09:35 -0500'
  date_gmt: '2015-11-02 16:09:35 -0500'
  content: "Its years later, but today you are the God of our office\r\nThanks so
    much for sharing"
- id: 686230
  author: Softlay
  author_email: sofr@gmail.com
  author_url: http://softlay.net
  date: '2016-05-19 15:18:55 -0400'
  date_gmt: '2016-05-19 19:18:55 -0400'
  content: I am having d same issue with my mbp late 08, when I try ur method it pops
    permission denied pls help.
- id: 688559
  author: softfiler
  author_email: auspeciousborn@gmail.com
  author_url: https://www.softfiler.com
  date: '2017-10-28 15:11:27 -0400'
  date_gmt: '2017-10-28 19:11:27 -0400'
  content: I am having same headache. Is there any verified solution available for
    this?
- id: 688570
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2017-10-31 12:20:23 -0400'
  date_gmt: '2017-10-31 16:20:23 -0400'
  content: I haven't seen this situation since Leopard, and the underlying pieces
    of the MacOS operating system have undoubtedly changed.  If you find an updated
    solution, feel free to post it in a comment.
---
<p>After the release of the latest update to the Macintosh operating system (<a href="http://support.apple.com/kb/HT1141" title="About the Mac OS X 10.5.3 Update">10.5.3</a>), <a href="http://www.macfixit.com/article.php?story=20080530225515297" title="Mac OS X 10.5.3 (#3): serious proxy .pac problems; random application crashes; login window loop; more (MacFixIt.com)">some users were reporting a "login loop"</a> to MacFixIt.com.  I followed the always helpful advice on MacFixIt for updating the operating system, and after the first reboot everything came back fine on my PowerBook G4 I thought I was in the clear.  With the second reboot, though, I started seeing the login loop:  the machine boots fine, but when you put the username and password in, the system hangs for about 20 seconds before displaying the login window again.  Clearly something is hosed, and fortunately I was able to fix it.</p>
<p>I tried the suggested solutions -- booting in safe mode and logging in (still had the same problem); running a file system check in single user mode (no errors reported); deleting the login window plists; and changing the password -- but they had no effect.  I could log into the temporary admin account I give to Apple when the machine is sent in for service, so I knew it was something specific to my day-to-day account.  I was able to get into single user mode (hold down Command-S right after the startup twang) and examine the /var/log/system.log file.  This is part of the underlying UNIX nature of MacOSX, and was the only place I found that gave clues to what was going on.  Here is a portion of the log file that occurs right after hitting return at the login screen:</p>
<blockquote><p><code>loginwindow[23]: USER_PROCESS: 23 console<br />
com.apple.launchd[1] (com.apple.UserEventAgent-LoginWindow[86]): Exited: Terminated<br />
<b>ReportCrash[106]: Formulating crash report for process lsregister[104]</b><br />
ReportCrash[106]: Saved crashreport to /Library/Logs/CrashReporter/lsregister_<i>timestamp</i>.crash using uid: 0 gid: 0, euid: 0 egid: 0<br />
kernel[0]: SetCryptoKey R: len 32, idx 1<br />
ReportCrash[111]: Formulating crash report for process ReportCrash[105]<br />
ReportCrash[111]: Saved crashreport to /Users/<i>userid</i>/Library/Logs/CrashReporter/ReportCrash_<i>timestamp</i>.crash using uid: <i>uid</i> gid: <i>gid</i>, euid: <i>uid</i> egid: <i>gid</i><br />
com.apple.launchd[92] (com.apple.ReportCrash[105]): Exited abnormally: Bus error<br />
ReportCrash[112]: Too many crashes in rapid succession! No crash report being written for pid 113<br />
com.apple.launchd[1] (com.apple.UserNotificationCenter[113]): Exited abnormally: Segmentation fault<br />
com.apple.launchd[1] (com.apple.UserNotificationCenter): Throttling respawn: Will start in 10 seconds<br />
ReportCrash[112]: Too many crashes in rapid succession! No crash report being written for pid 114</code></p></blockquote>
<p>The key clue is bolded -- the <span class="removed_link" title="http://www.carbondev.com/site/?page=lsregister">lsregister</span> process is crashing.  I found a clue to the fix in <a href="http://web.archive.org/web/20090516050839/http://roderickmann.org:80/log/archives/2003/05/launch_services.html" title="log: Launch Services Cache Corruption">a 2003 blog posting by a guy named Rick</a> when he said <q>After a couple hours of snooping, and some luck (I was able to ssh in from another machine and watch the system log report the crashes), I discovered that Launch Services&rsquo; cache was corrupted, and was causing lsregister to seg fault.</q>  His posting was related to MacOSX 10.2.6, and since then the name of the Launch Services cache file has morphed.  I found it in the same place (the <code>/Library/Caches</code> directory), but now there is more than one and they take the form of "<code>com.apple.LaunchServices-023<i>uid</i>.csstore</code>" where <i>uid</i> varies depending on the appropriate userid number.  I removed all of the Launch Services files from <code>/Library/Caches</code>, restarted, and was able to log in fine.  The only side effect was that the applications-to-launch-at-login list was gone (the "Login Items" tab of the Account Preference Pane) and had to be reconstructed.</p>
<p>So I'm productive again, and I didn't have to reinstall the operating system or transfer all my old files and settings to a newly-generated account.  I hope this message helps someone else, too.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.carbondev.com/site/?page=lsregister on November 13th, 2012.</p>
