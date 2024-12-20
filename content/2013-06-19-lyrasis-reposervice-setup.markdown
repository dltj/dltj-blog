---
layout: wordpress-import
status: published
published: true
title: 'LYRASIS'' "Reposervice" Setup Pushed to GitHub'
modified: 2013-06-19T17:58:26+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 4123
wordpress_url: http://dltj.org/?p=4123
date: '2013-06-19 13:58:26 -0400'
date_gmt: '2013-06-19 17:58:26 -0400'
category: Open Source
categories:
- Open Source
tags:
- Drupal
- LYRASIS
- Islandora
- Fedora Repository
- git
comments:
- id: 620433
  author: Drupal Sun | A Search UI for Drupal Planet Feeds
  author_email: ''
  author_url: http://drupalsun.com/?open=34900&amp;page=0&amp;infinite=1
  date: '2013-06-23 17:15:45 -0400'
  date_gmt: '2013-06-23 21:15:45 -0400'
  content: "<!--%kramer-ref-pre%-->[...] Original Article [...]<!--%kramer-ref-post%-->"
---
<p>Earlier this month published <span class="removed_link" title="https://github.com/lyrasis/reposervice">'reposervice' to GitHub</span>.  Reposervice is a "self-contained" Islandora installation source tree that is intended to smooth the LYRASIS deployment of repository services between development servers, a staging server and production servers.  It is a bit of a work-in-progress at the moment, but others might find it useful as well.</p>
<p>(By the way, if you had looked at Reposervice prior to June 18th, you may have noticed a missing critical element -- the Drupal submodule.  Not because you couldn't add Drupal yourself but because the Reposervice clone has <a href="https://github.com/lyrasis/drupal/tree/lyr-master/sites/all/modules">relative soft symlinks to the Islandora modules</a> positioned in the top level Reposervice directory.)</p>
<p>The goals of this setup are listed in the README file:</p>
<ul>
<li>Put (most) everything in a self-contained directory using relative paths for most components with a configuration script that generates configuration files for absolute paths. </li>
<li>Make it easy to track the upstream Islandora work so that you can bring selected commits into your own environment, if desired [using git submodules]. </li>
<li>Put the configuration of Fedora Commons, FedoraGSearch, SOLR, and other associated components under version control. </li>
<li>Use Drupal Features to store the Drupal configuration and put it under version control. </li>
<li>Support multi-site setups for separate Islandora/Drupal instances using a common Fedora Commons, SOLR, and djatoka installation. </li>
</ul>
<p>The first four bullets are there along with hints of the fifth.  (There is some as-yet unfinished, uncommitted code that automates much of the work of creating multi-site setups under a single Drupal installation.)</p>
<p>When I sent a <a href="https://groups.google.com/d/msg/islandora/mDVDUINXPkk/7P1eTLzWA4gJ">note about this to the islandora community mailing list</a>, I got a helpful reply back from Nick Ruest pointing to some work that Graham Stewart of the University of Toronto had done using <a href="http://www.opscode.com/chef/" title="Chef | Opscode">Chef</a>.</p>
<blockquote><p>Date: Thu, 13 Jun 2013 12:39:50 -0400<br />
From: Nick Ruest<br />
To: islandora@googlegroups.com<br />
Subject: Re: [islandora] A 'DevOps' Configuration for Islandora</p>
<p>I nearly forgot! Graham Steward at UofT has a few recipes up in his<br />
Github account[1] and there is a recording of his presentation from the<br />
2012 Access[2].</p>
<p>-nruest</p>
<p>[1] <span class="removed_link" title="https://github.com/librarychef">https://github.com/librarychef</span><br />
[2] <a href="http://www.youtube.com/watch?v=eTNBmy4ZznA" title="Cooking with Chef: Automated Deployment of Web Apps in a Library Context - Graham Stewart - YouTube">http://www.youtube.com/watch?v=eTNBmy4ZznA</a></p></blockquote>
<p>The recording of the presentation is a great introduction to Chef from a library perspective; Graham builds an Islandora 6.x installation from scratch in 624 seconds.  The Ruby-based <a href="https://github.com/LibraryChef/islandora/blob/master/recipes/islandora12.rb">islandora12.rb recipe</a> indeed has a great deal of resemblance to the bash scripts I was creating to deploy the components into the central directory tree.  I'm going to have to add Chef to my list of things to learn, and Graham's call of cooperation in building library-oriented recipes is a compelling one.</p>
<p>There are a few LYRASIS-specific things in here, but I've tried to make the basic building blocks replicable for others.  This git repo, as it is further developed and documented, will be the foundation of a <a href="http://or2013.net/content/light-weight-devops-approach-islandora" title="A Light-Weight DevOps Approach to Islandora | OR2013">presentation I'm giving at Open Repositories next month.</a>  Comments, questions, observations, and even pull requests (should you find this setup useful in your own work) welcome!</p>
