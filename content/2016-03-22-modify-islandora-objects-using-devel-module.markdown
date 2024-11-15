---
layout: wordpress-import
status: published
published: true
title: 'Modify Islandora objects on-the-fly using Devel "Execute PHP Code"'
modified: 2016-03-22T15:45:10+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 27171
wordpress_url: http://dltj.org/?p=27171
date: '2016-03-22 11:45:10 -0400'
date_gmt: '2016-03-22 15:45:10 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Drupal
- web development
- Islandora
comments:
- id: 685804
  author: islandora
  author_email: twitter.901783298@example.com
  author_url: https://twitter.com/islandora
  date: '2016-03-22 12:12:50 -0400'
  date_gmt: '2016-03-22 16:12:50 -0400'
  content: 'RT @DataG: New blog post: Modify #Islandora objects on-the-fly using Devel
    "Execute PHP Code" https://t.co/7b2rlfncPZ'
---
<p><a href="http://islandora.ca/content/meet-your-developer-alan-stanley" title="Meet Your Developer: Alan Stanley | Islandora Website">Alan Stanley</a> taught me this trick at an Islandora Camp a few years ago, and when trying to remember it this morning I messed up one critical piece.  So I'll post it here so I have something to refer back to when I need to do this again.</p>
<p>The <a href="https://www.drupal.org/project/devel">Drupal Devel module</a> includes a menu item for executing arbitrary PHP code on the server.  (This is, of course, something you want to set permissions on very tightly because it can seriously wreck havoc on your day if someone uses it to do bad things.)  Navigate to <code>/devel/php</code> on your Islandora website (with the Devel module enabled), and you'll get a nice, big <code>&lg;textarea></code> and an "Execute" button:</p>
<p>{{ image(
    div_float="none",
    width="584",
    caption='Execute arbitrary PHP using Drupal Devel module.',
    alt="Execute arbitrary PHP using Drupal Devel module.",
    localsrc="2016/03/devel-execute-php-1024x794.png",
    localhref="2016/03/devel-execute-php.png") }}</p>
<p>In this case, I'm generating the TECHMD datastream using the FITS module and displaying the results of the function call on the HTML page using the Devel module's <a href="https://api.drupal.org/api/devel/devel.module/function/dpm/7">dpm()</a> function:</p>
```php
include drupal_get_path('module', 'islandora_fits') . '/includes/derivatives.inc';
$object= islandora_object_load('demo:6');
$results = islandora_fits_create_techmd($object, False, array('source_dsid' => 'OBJ'));
dpm($results);
```
<p>Works like a charm!</p>
