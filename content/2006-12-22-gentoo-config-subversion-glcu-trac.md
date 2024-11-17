---
layout: wordpress-import
status: published
published: true
title: Managing a Gentoo Linux Server Configuration with Subversion, GLCU, and Trac
modified: '2018-01-15T22:38:08-05:00'
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 164
wordpress_url: http://dltj.org/2006/12/gentoo-config-subversion-glcu-trac/
date: 2006-12-22 12:49:00 -0500
date_gmt: 2006-12-22 17:49:00 -0500
categories:
- Raw Technology
tags:
- Gentoo
- system administration
- Subversion
comments:
- id: 9448
  author: Ma.gnolia.com - Find Web Sites &amp; Build Community Online
  author_email: ''
  author_url: ''
  date: 2006-12-25 02:48:14 -0500
  date_gmt: 2006-12-25 07:48:14 -0500
  content: <!--%kramer-ref-pre%-->[...] Managing a Gentoo Linux Server Configuration with Subversion, GLCU, and Trac in Disruptive Library Technology Jester [...]<!--%kramer-ref-post%-->
- id: 11092
  author: Server:ServerSetup - Kpautomation.com
  author_email: ''
  author_url: http://www.kpautomation.com/wiki/index.php?title=Server:ServerSetup#Backup_schemes
  date: 2007-01-14 22:56:33 -0500
  date_gmt: 2007-01-15 03:56:33 -0500
  content: <!--%kramer-ref-pre%-->[...] Look at setting up Subversion repository to keep track of Linux conf file changes. [...]<!--%kramer-ref-post%-->
- id: 12360
  author: Stephan Wehner
  author_email: stephanwehner@gmail.com
  author_url: http://stephansmap.org
  date: 2007-02-15 13:35:31 -0500
  date_gmt: 2007-02-15 18:35:31 -0500
  content: "This will add .svn directories under /etc and all others. Wouldn't it be nice to avoid that? Any idea?\r\n\r\nThanks --\r\n\r\nStephan"
- id: 12361
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: 2007-02-15 14:23:55 -0500
  date_gmt: 2007-02-15 19:23:55 -0500
  content: "[quote comment=\"12360\"]This will add .svn directories under /etc and all others. Wouldn't it be nice to avoid that? Any idea?[/quote]\r\n\r\nIt would be nice, but I think it is unavoidable..."
- id: 13661
  author: Andrew Premdas
  author_email: apremdas@yahoo.co.uk
  author_url: ''
  date: 2007-04-03 23:18:07 -0400
  date_gmt: 2007-04-04 03:18:07 -0400
  content: Any thoughts on file permissions and retrieving/merging back files from the repository. My experiments indicate that things comeing back from the repository will lose Group permissions.
- id: 13667
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: 2007-04-04 08:36:24 -0400
  date_gmt: 2007-04-04 12:36:24 -0400
  content: "Andrew --\r\n\r\nThat may be true.  Since Subversion does not store group (nor owner) information, a merged file would take on the ownership of the person doing the merge.  I can't think of a way around that at the moment..."
- id: 14407
  author: Bartosz Brewinski
  author_email: bartosz.brewinski@post.pl
  author_url: ''
  date: 2007-04-24 12:04:50 -0400
  date_gmt: 2007-04-24 16:04:50 -0400
  content: you must remember to use svn commands instead of traditional ones, "svn rm" instead of "rm" for example.
- id: 14415
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: 2007-04-24 16:55:50 -0400
  date_gmt: 2007-04-24 20:55:50 -0400
  content: "[quote comment=\"14407\"]you must remember to use svn commands instead of traditional ones, \"svn rm\" instead of \"rm\" for example.[/quote]\r\n\r\nPerhaps, but if one does an 'svn status' before the 'svn commit' to see what is about to change, the files that were deleted with simply the `rm` command would be marked with exclamation marks.  In such cases, I find that this little shell ditty does the trick to synchronize things.\r\n\r\n<code>svn status | egrep '^!' | cut -c8- | xargs svn rm</code>\r\n\r\nSimilarly, files that were added are marked with a question mark, and this shell pipe will fix that, too:\r\n\r\n<code>svn status | egrep '^?' | cut -c8- | xargs svn add</code>"
- id: 18843
  author: "Zupe\u0142nie inna beczka: Ubuntu. Kontrola wersji plik&oacute;w konfiguracyjnych."
  author_email: ''
  author_url: ''
  date: 2007-07-10 02:34:03 -0400
  date_gmt: 2007-07-10 06:34:03 -0400
  content: "<!--%kramer-ref-pre%-->[...] je do kontroli zmian w plikach konfiguracyjnych. Bardzo przyst\u0119pnie zosta\u0142o to opisane w tym blogu. Osobi\u015Bcie wprowadzi\u0142em do powy\u017Cszej procedury troch\u0119 zmian pod k\u0105tem Ubuntu. Przedstawi\u0119 [...]<!--%kramer-ref-post%-->"
- id: 33624
  author: Tom
  author_email: tetra604@gmail.com
  author_url: ''
  date: 2008-07-23 17:17:10 -0400
  date_gmt: 2008-07-23 21:17:10 -0400
  content: For system-wide configuration under version control, try SVK which doesn't leave .svn directories across the hierarchy. All version-control information is held in a single ~/.svk location. Commands are mostly the same as svn, see http://svk.bestpractical.com/ for more information and emerge -uv svk.
- id: 33625
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: 2008-07-23 21:40:39 -0400
  date_gmt: 2008-07-24 01:40:39 -0400
  content: "Tom --\r\n\r\nInteresting concept.  I've heard of 'svk' but only in the context of using it to mirror CVS and SVN revision control trees by manipulating the contents of the depot with its 'smerge' command.  I hadn't considered using it to apply revision control to the /etc directory.  You wouldn't happen to know of someone that has written up a HOWTO on the topic, would you?"
- id: 35438
  author: Morten Lied Johansen
  author_email: mortenjo@ifi.uio.no
  author_url: http://ibidem.homeip.net/
  date: 2009-05-02 19:10:31 -0400
  date_gmt: 2009-05-02 23:10:31 -0400
  content: "I've used this method to get some control over my configuration changes, and it works great except for one thing. The trick to get a sorted version of the portage world file doesn't seem to be working.\r\n\r\nAny clues on why that is? Has something changed in the way portage works perhaps?"
- id: 35440
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: 2009-05-02 19:50:46 -0400
  date_gmt: 2009-05-02 23:50:46 -0400
  content: This still works (although I see reading back through the post that some upgrades to the WordPress database along the way have corrupted some of the shell syntax).  I'll correct the posting.
- id: 77003
  author: "SYSADMINS.BIZ &bull; \u041F\u0440\u043E\u0441\u043C\u043E\u0442\u0440 \u0442\u0435\u043C\u044B - \u0416\u0443\u0440\u043D\u0430\u043B\u0438\u0440\u043E\u0432\u0430\u043D\u0438\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 \u043D\u0435\u0441\u043A\u043E\u043B\u044C\u043A\u0438\u0445 \u0421\u0410 \u043D\u0430 \u0441\u0435\u0440\u0432\u0435\u0440\u0430\u0445 *nix"
  author_email: ''
  author_url: http://sysadmins.biz/viewtopic.php?f=11&amp;t=7561
  date: 2010-07-06 09:24:31 -0400
  date_gmt: 2010-07-06 13:24:31 -0400
  content: "<!--%kramer-ref-pre%-->[...] hanzhin.stas \u043F\u0438\u0441\u0430\u043B(\u0430):\u0425\u043C\u043C\u043C, \u0435\u0441\u043B\u0438 \u0443 \u0432\u0430\u0441 \u043F\u043E\u043B\u0443\u0447\u0438\u0442\u0441\u044F - \u043E\u0442\u043F\u0438\u0448\u0438\u0442\u0435\u0441\u044C \u0437\u0434\u0435\u0441\u044C \u0440\u0435\u0446\u0435\u043F\u0442\u043E\u043C. \u0410 \u0447\u0435\u0433\u043E \u0442\u0443\u0442 \u0434\u0435\u043B\u0438\u0442\u044C\u0441\u044F? \u0412\u0441\u0435 \u0443\u0436\u0435 \u043F\u0440\u0438\u0434\u0443\u043C\u0430\u043D\u043E \u0434\u043E \u043D\u0430\u0441.\u041D\u0430\u043F\u0440\u0438\u043C\u0435\u0440: http://dltj.org/article/gentoo-config-subversion-glcu-trac/ [...]<!--%kramer-ref-post%-->"
---
Keeping track of configuration changes to servers is a tough job made tougher when some of the sysadmins work from home. Questions of who did what when and why can be exacerbated by the lack of physical proximity --- in other words, I can't simply yell over the cubical wall to the colleague down the hall to ask him about the new package installed on the server. Besides, that oral history tradition is difficult to maintain and harder to sustain as the number of machines grows. This essay describes a practice for maintaining a [Gentoo Linux distribution][0] using GLCU, Subversion, and Trac that is lightweight (doesn't impose a large burden on the sysadmin staff), effective (although it is lightweight it better documents and makes accessible the state of our systems over the oral history tradition), and cheap (no operating budget dollars were harmed in the creation of this process --- only staff time overhead).

## Create an All-Encompassing Configurations Directory

The first step is to put the system configuration files into a revision control system (RCS). An RCS allows us to track the history of files by storing information about changes such as the date/time a change was made, what the change was, who made it, and a free-text field explaining why the change was made. RCS systems are common for software development shops as a way to track changes to source code. In this circumstance we are tracking changes to the text configuration files that make up the operating system and its components. We are using the [Subversion][1] RCS, but the same concepts apply whether you are using other systems (such as CVS or Arch).

The RCS will want to act on a single directory tree, but in most cases our configuration files are spread out over the file system. Most are in /etc, but others exist elsewhere. (The portage "world" file, a record of everything installed on your system, for instance, is in /var/lib/portage.) What we do is create a directory called /server-rcs that will be managed by the RCS, and in that directory is copies or links to all of the configuration files on the system.

### Putting /etc (or any other directory) Under Version Control

One of the things we're going to want to do, obviously, is put the entire /etc directory into the RCS. Ideally, we would simply put a link to /etc in /server-rcs. Unfortunately, we can't use the simple filesystem-based linking methods (soft links and hard links) because a) our RCS is smart enough to see the soft link and [records it as a soft link in the revision control database][2] rather than following the link to the contents of that directory; and b) one cannot make a hard link to a directory:

```shell
/server-rcs # ln ../etc .
ln: `../etc': hard link not allowed for directory
```

What we need to do instead is a trick using the 'mount' command to _bind_ one portion of the file system to another part. From the mount MAN page:

> Since Linux 2.4.0 it is possible to remount part of the file hierarchy somewhere else. The call is
> 
>     mount --bind olddir newdir
> 
> After this call the same contents is accessible in two places. One can also remount a single file (on a single file).
> 

So we can bind the entire /etc directory into our RCS space with this command:

```bash
mount --bind /etc /server-rcs/etc
```

Better yet, we put this in our /etc/fstab file (also adding the /var/spool/cron directory as well):

```text
/etc                            /system-rcs/etc                         none    bind
/var/spool/cron/crontabs        /system-rcs/var-spool-cron-crontabs     none    bind
```

Since the /etc directory (and other directories) already exist, we're going to have to play some games to get them into the repository. For the trick do to this with Subversion, see [the FAQ entry on in-place imports][3].

### Handling Individual Files Under Version Control

Not everything we want to track is in /etc or neatly packaged into directories. Some application-specific configuration files, most notably web applications, exist somewhere else in the directory structure. We want to track things like the 'phpmyadmin' configuration file, for instance.

We could use the mount 'bind' trick to put individual files into the /server-rcs space, but that seems overly complicated. Our servers are generally configured with few filesystems, so in many cases the files we need to track in the RCS are within the same filesystem and we can use hard links to put them into the /server-rcs directory. Another alternative is to write a cron job to copy configuration files into the /server-rcs directory, but then realize that this kind of revision control is one way --- if we restore a previous version of a file from the RCS, we need to manually copy it back to the original location.

(On the other hand, using the mount 'bind' method is a form of self-documenting the otherwise invisible hard links to files in the same filesystem. For that reason, it might be worth considering that option.)

### Special Case: /var/lib/portage/world

One special case is the portage 'world' file. This file records all of the user-specified (e.g. non-profile) packages that have been installed on your Gentoo system. Unfortunately, each time 'emerge' runs, the world file is rewritten and the order of package names is seemingly random. This wrecks havoc with the 'diff' function of the RCS --- it seems like a lot more has changed than just the addition or removal of a package or two.

What we do instead is patch into a hook of the 'emerge' command that will save a sorted copy of the world file into /server-rcs. This patch goes into `/etc/portage/profile/profile.bashrc`:

```bash
if [ "${EBUILD_PHASE}" == "setup" ]
then
        sort /var/lib/portage/world > /server-rcs/misc/var-lib-portage-world
fi
```

Every time 'emerge' goes through the 'setup' mode when installing a package, it will run this sort command. Note that there is no file locking going on here, so there is a remote chance that the /server-rcs version (but not the /var/lib/portage version) could get corrupted. Such a problem is minor, though, and easily fixed.

### Importing into Subversion

With the /server-rcs directory prepared, we now just need to get it into the RCS. These are Subversion commands:

```bash
svn add --force /server-rcs
svn checkin --message "Importing the configuration files for the server" /server-rcs https://svn.repository.url/svn/configurations/server
```

Because of the in-place import problem for pre-existing directories (described earlier), we likely had to create some of the repository directory structure already. (In this example, we would have executed a `svn mkdir https://svn.repository.url/svn/configurations/server/etc` command already to "prime the pump" for adding /etc to the repository.) In line \#1, the --force option makes the 'svn add' command continue the recursive directory parse to add files and directories to the RCS structure even if some component of those paths were already in the RCS structure. Line \#2 checks in our completed /server-rcs directory.

## Daily Usage

With all of this setup done, it is finally time to make use of this configuration management infrastructure. Doing so is pretty easy --- work as you normally do when installing packages and making changes to configuration files. (As you do so, you also have the added safety net of `svn revert _filename_` should you make a mistake and want to go back to the previous version of a file.) When you've done a defined chunk of work, simply run this command:

```bash
svn status /server-rcs
svn checkin /server-rcs -m "Free-text description of why you made the changes."
```

The first line will show you the files modified since the last check-in &mdash hopefully only the files you intended to modify, although this is a good point to check to make sure an inadvertent change didn't happen. The second line will copy changes to the /server-rcs directory into the RCS along with the free-text note describing why you made the change.

Isn't this great? It is sort of self-documenting. Not only to you have your brief description of what you did but you also have the exact changes made to the configuration files. If a change doesn't work out, you have easy access to past configurations that allow you to revert back to a previous state. (Note, though, that we're not saving actual applications in the RCS --- you may have to recompile and install older versions of applications to get back to the previous state.)

### Portage Updates with GLCU

We can make our system management lives even easier by using the semi-automated tool [Gentoo Linux Cron Update][4] (GLCU). This script breaks up the process of updating packages into two pieces. The first that runs in the off-hours via cron that syncs the local portage copy, download and compiles updated packages, and stages ready-to-install binary distributions of those updates. The second piece has the human interface: seeing the list of updated packages in the staging area, selecting which to install, and prompting the sysadmin to install any updates as a result of Gentoo Linux Security Announcements (GLSAs). 

See the [project on SourceForge][4] for all of the details on installing, configuring and running GLCU. We make one tweak to the GLCU configuration to prompt the sysadmin to complete all of the housekeeping chores: running `dispatch-conf` to merge changes to configuration files and `revdep-rebuild` to make sure all of the applications using updated linked libraries are properly recompiled. To do this, add a line to `/etc/conf.d/glcu`:

```shell
updatetc: dispatch-conf && revdep-rebuild -X -pv
```

A typical update for us looks like:

```text
# glcu /tmp/glcuUpdate-23112

****************************************
>> Welcome to glcu's easy update feature

Prebuilt packages:
------------------
(  1 ) [binary     U ] app-editors/nano-2.0.1 [1.3.12-r1] USE="ncurses nls spell unicode
  -debug -justify -minimal -slang"
(  2 ) [binary     U ] media-libs/libsdl-1.2.11 [1.2.8-r1] USE="X esd* -aalib -alsa -arts
  -dga -directfb -fbcon -ggi -libcaca -nas -noaudio -noflagstrip -nojoystick -novideo 
  -opengl -oss -svga -xinerama -xv (-pic%)" 

Do you want to install the prebuilt package(s) [Y/n]    
   (or you can either install only specified package number(s) #,
     or NOT install package with -# and use i# for injecting)

> y
[...pre-compiled packages are installed...]

>>> Auto-cleaning packages...

>>> No outdated packages were found on your system. 

* GNU info directory index is up-to-date. 
* IMPORTANT: 1 config files in /etc need updating. 
* Type emerge --help config to learn how to update config files.

glsa's:  ['200612-03']
(  1 ) 200612-03 [N] GnuPG: Multiple vulnerabilities ( app-crypt/gnupg )

 Do you want to fix all glsa's now? [Y/n]
    (or you can either install only specified glsa number(s) #,
     or NOT install glsa with -# and use i# for injecting)

> y
[...packages related to the GLSA are downloaded, compiled and installed...]

 Do you want to run dispatch-conf && revdep-rebuild -X -pv now? [Y/n]
 > y
[...dispatch-conf and revdep-rebuild are run...]
```

With the system nicely updated, we can check in all of the changes to the RCS with a note about what we did:

```bash
svn ci -m "After running 'glcu' to update app-editors/nano, media-libs/libsdl, and GLSA for app-crypt/gnupg"
```
### Tracking Configuration Changesets and Trouble Tickets with Trac

So far we've done quite a lot to document changes to the configuration of our server. What we're missing is a nice way to view and track those changes over time. Since everything is in the Subversion RCS, one way to accomplish this is to put a web interface (like ) on top of Subversion repository. For just a little bit more effort and complexity, though, we can have a very nice documentation and issue tracking system bundled with the display of our configuration changes repository by using [Trac][5]. 

Trac is an open source wiki and issue tracking system for software development projects. Its stated mission is to "help developers write great software while staying out of the way." In this case we'll be using it to help sysadmins manage complex systems while staying out of the way. Trac is a web-based tool that "allow wiki markup in issue descriptions and commit messages, creating links and seamless references between bugs, tasks, changesets, files and wiki pages. A timeline shows all ... events in order, making the acquisition of an overview of the \[state of the system\] and tracking progress very easy."

Trac is synchronized with our Subversion source code repository, so the [timeline of changes][6] ([demo][7]) shows each [check in to the Subversion RCS][8] ([demo][9]), which can be tied to an [issue ticket][10] (demo) for a problem or task that is requested, worked on, then closed via simple wiki-like markup. One can also [browse through the stored changes][11] ([demo][12]) and look at a [graphical difference between any two revisions of a file][13] (demo) but also review the [log of check in messages][14] ([demo][15]) associated with that file over time.

## Conclusion

With a few tools and some modest changes to current system maintenance practices, the history of the configuration of machines can be documented and the changes viewed over time. The changes in practices are designed to be very minimal and simple yet return a large payoff over time if consistently followed. The practices also enhance communication between geographically dispersed staff tasked with managing the same platforms by regularly creating snapshots of the configuration state and documenting who did what changes and why.

The text was modified to remove a link to Demonstration of Trac Issue Tickets on December 30th, 2010\.

The text was modified to remove a link to http://gentoo-wiki.com/MAN\_emerge\_1 on January 19th, 2011\.

The text was modified to remove a link to http://gentoo-wiki.com/MAN\_mount\_8 on January 19th, 2011\.

The text was modified to remove a link to http://gentoo-wiki.com/MAN\_emerge\#lbAN on January 19th, 2011\.

The text was modified to remove a link to http://trac.edgewall.org/changeset?new=trunk%2Fhtdocs%2Fcss%2Ftrac.css%404501&old=trunk%2Fhtdocs%2Fcss%2Ftrac.css%404390 on January 19th, 2011\.

[0]: http://www.gentoo.org/ "Gentoo Linux distribution homepage"
[1]: http://subversion.tigris.org/ "Subversion RCS homepage"
[2]: http://subversion.tigris.org/faq.html#symlinks "Subversion FAQ"
[3]: http://subversion.tigris.org/faq.html#in-place-import "Subversion FAQ"
[4]: http://glcu.sourceforge.net/ "Gentoo Linux Cron Update (GLCU) hompage"
[5]: http://trac.edgewall.org/ "The Trac Project - Trac"
[6]: http://trac.edgewall.org/wiki/TracTimeline "TracTimeline help page from the Trac project"
[7]: http://trac.edgewall.org/timeline "Timeline help page from the Trac project"
[8]: http://trac.edgewall.org/wiki/TracChangeset "TracChangeset help page from the Trac project"
[9]: http://trac.edgewall.org/changeset/4501 "Demonstration of Trac Changesets"
[10]: http://trac.edgewall.org/wiki/TracTickets "TracTickets help page from the Trac project"
[11]: http://trac.edgewall.org/wiki/TracBrowser "TracBrowser help page from the Trac project"
[12]: http://trac.edgewall.org/browser/trunk/htdocs/css/trac.css?rev=4501 "Demonstration of Trac RCS Browser"
[13]: http://trac.edgewall.org/wiki/TracRevisionLog#InspectingChangesBetweenRevisions "TracRevisionLog - The Trac Project - Trac"
[14]: http://trac.edgewall.org/wiki/TracRevisionLog "TracRevisionLog help page from the Trac project"
[15]: http://trac.edgewall.org/log/trunk/htdocs/css/trac.css?rev=4501 "Demonstration of Trac Revision Logs"