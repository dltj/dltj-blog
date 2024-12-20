---
layout: wordpress-import
status: published
published: true
title: 'Client JAR for FEDORA Server Access'
modified: 2006-06-02T17:23:30+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 62
wordpress_url: http://dltj.org/2006/06/fedora-client-jar/
date: '2006-06-02 13:23:30 -0400'
date_gmt: '2006-06-02 18:23:30 -0400'
category: Library Technology
categories:
- Fedora
tags:
- Fedora Repository
comments:
- id: 33007
  author: Ian Ibbotson
  author_email: ianibbo@googlemail.com
  author_url: ''
  date: '2008-04-14 12:32:07 -0400'
  date_gmt: '2008-04-14 16:32:07 -0400'
  content: "Thanks for this, it looks like exactly what I need in terms of code...
    I don't suppose it's available as a maven2 dependency anywhere?\r\n\r\nCheers
    again!\r\nIan."
- id: 33011
  author: the Jester
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2008-04-14 14:24:23 -0400'
  date_gmt: '2008-04-14 18:24:23 -0400'
  content: No, sorry.  I haven't gotten into Maven yet.
---
<p>At OhioLINK we've reached the conclusion that coding would be easier if we created a modestly robust JAR file that is an implementation of the AXIS-based web services interface to a FEDORA server.  Our initial effort is ready for public consumption; you can check it out of our Subversion repository at:</p>
<p><span class="removed_link" title="http://drc-dev.ohiolink.edu/svn/FedoraClientJar/trunk">http://drc-dev.ohiolink.edu/svn/FedoraClientJar/trunk</span></p>
<p>The JavaDocs are available at:</p>
<p><span class="removed_link" title="http://drc-dev.ohiolink.edu/svn/FedoraClientJar/trunk">http://drc-dev.ohiolink.edu/javadoc/FedoraClientJar/</span></p>
<p>If you ask the OhioLINK team, they'll tell you that the API has undergone significant changes in its young life, but I think it will settle down now.  Some features:</p>
<ul>
<li>The client library and nothing but the client library (distinguished from the core developer's client library in that there is no Swing presentation code mixed in).</li>
<li>Good embedded JavaDocs for all packages, classes and methods. (Some of the descriptive and proscriptive elements could be better, and will probably improve with age.)</li>
<li>A single class that contains both API-A and API-M remote methods.</li>
<li>A class that helps with searching the Resource Index through the REST interface.  (It only implements the "find tuples" returning results as a CSV stream at the moment.)</li>
<li>A factory-based method for instantiating classes that hopefully will be extensible and easy to use.</li>
</ul>
<p>To Dos:</p>
<ul>
<li>Implementing mock interfaces for the methods to enable unit testing of client application code without needed to start a FEDORA server.  (The stubs for this are already in the packages.)</li>
<li>JUnit tests of the "Live" interfaces against a pre-configured FEDORA server.</li>
<li>Adding a class to help with searching the native FEDORA index (and probably Gert's General Fedora Search Plug-in as well).</li>
<li>Adding more helper methods (such as use of the file-upload servlet).</li>
</ul>
<p>I'm also toying with adding JavaBeans and DAO pattern classes as well.  If someone already has these in a client-side implementation and would be willing to offer them to this code library, our team (and probably many others) would appreciate it.</p>
<p>Comments and code contributions are welcome.</p>
