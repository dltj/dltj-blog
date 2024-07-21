---
layout: wordpress-import
status: published
published: true
title: 'Adding Islandora Viewers Capability to Basic Image Solution Pack'
modified: 2017-08-29T01:15:58+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 27716
wordpress_url: http://dltj.org/?p=27716
date: '2017-08-28 21:15:58 -0400'
date_gmt: '2017-08-29 01:15:58 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- programming
- Drupal
- Islandora
- php
comments: []
---
<p>Putting this here because I didn't see it mentioned elsewhere and it might be useful for others.  Thinking about the history of the <a href="https://islandora.ca/">Islandora</a> solution packs for different media types, the <a href="https://github.com/Islandora/islandora_solution_pack_image">Basic Image Solution Pack</a> was probably the first one written.  Displaying a JPEG image, after all, is -- well -- pretty basic.  I'm working on an Islandora project where I wanted to add a viewer to Basic Image objects, but I found that the solution pack code didn't use them.  Fortunately, Drupal has some nice ways for me to intercede to add that capability!</p>
<h2>Step 1: Alter the <tt>/admin/islandora/solution_pack_config/basic_image</tt> form</h2>
<p>The first step is to alter the solution pack admin form to add the Viewers panel.  Drupal gives me a nice way to alter forms with <a href="https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_form_FORM_ID_alter/7.x"><tt>hook_form_FORM_ID_alter()</tt></a>.</p>
{% highlight php %}
/**
 * Implements hook_form_FORM_ID_alter().
 *
 * Add a viewers panel to the basic image solution pack admin page
 */
function islandora_ia_viewers_form_islandora_basic_image_admin_alter(&$form, &$form_state, $form_id) {
  module_load_include('inc', 'islandora', 'includes/solution_packs');
  $form += islandora_viewers_form('islandora_image_viewers', 'image/jpeg', 'islandora:sp_basic_image');
}
{% endhighlight %}

<h2>Step 2: Insert ourselves into the theme preprocess flow</h2>
<p>The second step is a little trickier, and I'm not entirely sure it is legal.  We're going to set a basic image preprocess hook and in it override the contents of <tt>$variables['islandora_content']</tt>.  We need to do this because that is where the viewer sets its output.</p>
{% highlight php %}
/**
 * Implements hook_preprocess_HOOK(&$variables)
 * 
 * Inject ourselves into the islandora_basic_image theme preprocess flow. 
 */
function islandora_ia_viewers_preprocess_islandora_basic_image(array &$variables) {
  $islandora_object = $variables['islandora_object'];
  module_load_include('inc', 'islandora', 'includes/solution_packs');
  $params = array();
  $viewer = islandora_get_viewer($params, 'islandora_image_viewers', $islandora_object);
  if ($viewer) {
    $variables['islandora_content'] = $viewer;
  }
}
{% endhighlight %}
<p>I have a sneaking suspicion that the hooks are called in alphabetical order, and since <tt>islandora_ia_viewers</tt> comes after <tt>islandora_basic_image</tt> it all works out.  (We need our function to be called <em>after</em> the Solution Pack's <tt>preprocess</tt> function so our <tt>'islandora_content'</tt> value is the one that is ultimately passed to the theming function.  Still, it works!</p>
