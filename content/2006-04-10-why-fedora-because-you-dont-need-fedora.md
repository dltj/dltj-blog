---
status: published
published: true
title: 'Why Fedora?  Because You Don''t Need Fedora'
modified: 2021-06-23T21:15:00-04:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 38
wordpress_url: http://dltj.org/2006/04/why-fedora-because-you-dont-need-fedora/
date: '2006-04-10 20:39:17 -0400'
date_gmt: '2006-04-11 01:39:17 -0400'
category: Library Technology
categories:
- DRC
- Fedora
- Unified Content Repository
tags:
- DRC
- Fedora Repository
comments:
- id: 49
  author: "&tau;&epsilon;&chi;&nu;&omicron;&sigma;&omicron;&phi;&iota;&alpha; &raquo;
    The Jester&#8217;s Case for Fedora"
  author_email: ''
  author_url: http://www.lackoftalent.org/michael/blog/2006/05/02/the-jesters-case-for-fedora/
  date: '2006-05-02 16:54:13 -0400'
  date_gmt: '2006-05-02 21:54:13 -0400'
  content: "[...] An advantage of using the Fedora system, as outlined in Why Fedora?
    Because You Don&#8217;t Need Fedora, is that due to modular design and adherence
    to more or less open standards, one is not necessarily wedded to Fedora for the
    foreseeable future.  Items in a Fedora repository are serialized as XML objects,
    either in the Fedora-METS or FOXML format.  While some of this information is
    copied into a relational database system and an RDF triplestore for speed and
    convenience, it is all intact within the serialized XML objects which reside in
    a predictable directory hierarchy on the local filesystem.  There are at least
    two advantages to this design: [...]"
- id: 77
  author: Fedora, Objects, Datastreams, Filesystems, and a Correction in Disruptive
    Library Technology Jester
  author_email: ''
  author_url: http://dltj.org/2006/05/preservation-in-fedora-revisited/
  date: '2006-05-14 16:02:27 -0400'
  date_gmt: '2006-05-14 21:02:27 -0400'
  content: "[...] In an earlier post, I extolled the virtues of Fedora as an ideal
    candidate for digital preservation because &#8220;[a]ll of the metadata (descriptive,
    preservation, and relationship to other objects) and managed datastreams that
    make up a digital object are &#8217;serialized&#8217; to a single XML file on
    a file system.&#8221; Well, as I found out last week, it isn&#8217;t quite that
    straight forward. &#182; [...]"
---
I'm often asked "Why is OhioLINK using FEDORA?" (Just to eliminate any confusion at the start, I'm referring to the {% include robustlink.html href="http://fedora.info/" versiondate="2006-04-10" title="Fedora" anchor="FEDORA Digital Object Repository" %}, a project of Cornell's computer science department and the University of Virginia Libraries, and not the Linux operating system distribution by Redhat.)
There are many reasons, but I was reminded of one recently while reading through the {% include robustlink.html href="http://web.archive.org/web/20140328025312/http://fedora.info/download/2.1.1/userdocs/distribution/migration.html" versiondate="2006-04-10" title="Fedora Upgrade and Migration Guide" anchor="migration documentation" %} for the 2.1.1 release that came out today.

<blockquote><p>In case of corruption or failure of the repository, the Fedora Rebuild utility can completely rebuild the repository by crawling the digital object XML source files that are stored on disk.</p>
<p>The fedora-rebuild command launches the interactive Fedora Rebuild utility that restores the repository if it somehow became corrupted.&nbsp;&nbsp; Symptoms of repository corruption include underlying indexes or registries becoming unusable, or the server refusing to start.&nbsp;&nbsp; The components of the repository that can become corrupted are the SQL relational database and the RDF triplestore that underlie the Fedora repository service.&nbsp;&nbsp; The SQL database (e.g., MySQL, McKoi, or Oracle) contains a set of registries, as well as metadata to enable simple searching of the repository,&nbsp; and a cache of digital object profiles to speed up API-A access to the repository.&nbsp; The triplestore contains RDF triples for key properties of digital objects, datastreams, disseminations, and relationships to create an RDF-based index of the repository (used for more advanced RDF-based searching).</p>
<p>{% include robustlink.html href="http://web.archive.org/web/20090205021214/http://fedora.info:80/download/2.1.1/userdocs/server/cmd-line/index.html" versiondate="2006-04-10" title="Fedora Server Command-Line Utilities" anchor="http://www.fedora.info/download/2.1.1/userdocs/server/cmd-line/index.html#rebuild" %}</p></blockquote>

Translation?
If your Fedora system blows up -- software glitch, disk failure, or heaven forbid a logic bomb -- you can restore the entire thing by simply reading files off the disk.
Yep -- that's right.
That large and complex software package only optimizes access to the objects.
The digital objects themselves are stored in {% include robustlink.html href="http://web.archive.org/web/20080522153921/http://www.fedora.info:80/download/2.1.1/userdocs/digitalobjects/introFOXML.html" versiondate="2006-04-10" title="Introduction to Fedora Object XML (FOXML)" anchor="a METS-like package called Fedora Object XML" %} (FOXML).
All of the metadata (descriptive, preservation, and relationship to other objects) and managed datastreams that make up a digital object are "serialized" to a single XML file on a file system.
Backup those XML files, and you've just created a preservation copy of your entire system.
Don't like Fedora -- or in five years something better comes along -- just program the new system to read these METS-like packages, load them into your new system, and away you go.
And, as the above quote from the documentation suggests, if something bad happens to the repository software or database, don't fret -- your worse case scenario is to wipe the system clean, restore the FOXML packages from backup, run the rebuild script, and away you go.

From a preservation perspective, what could be better for the long-term health of your content than a digital object repository system that doesn't <i>require </i>that you ever use that system at all?

<p style="padding:0;margin:0;font-style:italic;">The text was modified to remove a link to http://comm.nsdl.org/pipermail/fedora-users/2006-April/001505.html.</p>
