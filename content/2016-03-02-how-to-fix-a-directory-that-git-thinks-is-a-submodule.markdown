---
layout: wordpress-import
status: published
published: true
title: 'How to fix a directory that Git thinks is a submodule'
modified: 2016-03-02T21:53:50+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 27155
wordpress_url: http://dltj.org/?p=27155
date: '2016-03-02 16:53:50 -0500'
date_gmt: '2016-03-02 21:53:50 -0500'
category: Raw Technology
categories:
- Raw Technology
tags:
- git
comments: []
---
<p>Nuts.  I added and committed a directory to my Git repository when the directory itself was another separate Git repository.  Now Git thinks it's some sort of submodule, but it doesn't know how to deal with it:</p>
```bash
$ git submodule update
No submodule mapping found in .gitmodules for path 'blah'
```
<p>And worse, Git won't let me remove it:</p>
```bash
$ git rm blah
error: the following submodule (or one of its nested submodules)
uses a .git directory:
    blah
(use 'rm -rf' if you really want to remove it including all of its history)
```
<p>So what to do?  This:</p>
```bash
$ git rm --cached blah
$ git add blah
```
<p>In my case I had a situation where there were several Git repositories-inside-a-repository, so I wanted a way to deal with them all:</p>
```bash
$ for i in `find . -type d -name .git -print | sed 's#/.git##'`; do 
> echo $i
> rm -rf $i/.git
> git rm --cached $i
> git add $i
> done
```
<p>(Be careful not to run this <code>find</code> command at the <em>root</em> of your Git repository, of course, or else you will effectively destroy its usefulness as a git repo. )</p>
