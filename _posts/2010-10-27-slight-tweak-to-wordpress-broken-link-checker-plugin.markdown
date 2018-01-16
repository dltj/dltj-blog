---
layout: wordpress-import
status: publish
published: true
title: Slight Tweak to WordPress Broken Link Checker Plugin
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1805
wordpress_url: http://dltj.org/?p=1805
date: '2010-10-27 22:34:38 -0400'
date_gmt: '2010-10-28 02:34:38 -0400'
categories:
- Raw Technology
tags:
- WordPress
- plugins
comments:
- id: 96285
  author: Ken Varnum
  author_email: rss4lib@gmail.com
  author_url: http://www.rss4lib.com/
  date: '2010-10-28 11:51:04 -0400'
  date_gmt: '2010-10-28 15:51:04 -0400'
  content: As long as you're tweaking...  a date the change was made might be helpful,
    too (for you for diagnostics if suddenly links start getting borked, but also
    for future readers).
- id: 96297
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-10-28 13:25:28 -0400'
  date_gmt: '2010-10-28 17:25:28 -0400'
  content: Ah, that is a good suggestion, and should be simple enough to do.  I'll
    just tack <code>.' on '.date('F jS, Y')</code> on to the end of each line.
---
In a futile effort to fight link rot on _DLTJ_, I installed the [Broken Link Checker](http://wordpress.org/extend/plugins/broken-link-checker)plugin by ["White Shadow"](http://w-shadow.com/blog/2007/08/05/broken-link-checker-for-wordpress/). I like the way it scans the entire content of this blog -- posts, pages, comments, etc. -- looking for pages linked from here that don't respond with an [HTTP 200 "Ok"](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_Success) status code. The dashboard of problem links has a nice interface for updating or deleting these links, including the ability to add a CSS style deleted links to note that they were formerly there. One of the things I wished it did, though, was to add a message to posts/pages that noted a link was changed or deleted. You know -- just to document that something changed since the page was first published. Tonight I hacked into the code to add this function. And with apologies to the original author of this beautifully structured object-oriented PHP code, it is a gruesome hack.  


## The Patch

From the root level of the current version of the broken-link-checker plugin directory, one can apply this patch to `modules/parsers/html_link.php`. There are just two added lines -- one in each of `edit()` and `unlink()` -- that simply appends a paragraph to the end of the content. In my quick hack, there is no internationalization of strings and the CSS styling is inline. See...I told you it was ugly. Still, it meets my needs and it might meet yours too.

{% highlight diff %}
Index: modules/parsers/html_link.php
===================================================================
--- modules/parsers/html_link.php       (revision 304787)
+++ modules/parsers/html_link.php       (working copy)
@@ -127,6 +127,9 @@
                //Find all links and replace those that match $old_url.
                $content = $this->multi_edit($content, array(&$this, 'edit_callback'), $args);  

+               // Append a notation to the end of the HTML that a link was changed
+               $content .= '<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from '.$args['old_url'].' to '.$args['new_url'].'.</p>';
+
                return array(
                        'content' => $content,
                        'raw_url' => $new_url,
@@ -163,6 +166,9 @@
                //Find all links and remove those that match $raw_url.                
                $content = $this->multi_edit($content, array(&$this, 'unlink_callback'), $args);
+               // Append a notation to the end of the HTML that a link was deleted
+               $content .= '<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to '.$args['old_url'].'.</p>';
+
                return $content;
        }
@@ -342,4 +348,4 @@
        }
 }-?>
\ No newline at end of file
+?>
{% endhighlight %}

You can see how this appears to the end-user by looking at the notes added to the bottom of [this post](/article/fedora-plus-sakai-3/).

## Initial Results

I've been blogging for about five years, and in that span of time there have been 4,722 URLs used here. Of those, 748 are now "broken" (return some kind of non-success status code or the server itself is not responding). So far I've fixed or unlinked 50 of them. Whether stay excited about this project to work through the remaining 700 or so remains to be seen.
