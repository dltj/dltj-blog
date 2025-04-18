---
layout: wordpress-import
status: published
published: true
title: 'Modifications to FreePress Recent Comments Plugin'
modified: 2006-08-23T15:10:37+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 107
wordpress_url: http://dltj.org/2006/08/modified-freepress-recent-comments-plugin/
date: '2006-08-23 11:10:37 -0400'
date_gmt: '2006-08-23 16:10:37 -0400'
category: Meta Category
category: Meta Category
category: Meta Category
category: Meta Category
category: Meta Category
categories:
- Meta Category
tags:
- WordPress
comments: []
---
<p>For others that may find it useful, I've made two modifications to the <a href="http://freepressblog.org/wordpress-plugins-2/wordpress-recent-comments-plugin-widget/" title="FreePress Blog   &amp;raquo; WordPress Recent Comments Plugin / Widget">FreePress Recent Coments</a> plugin on <a href="/">DLTJ</a>:  one to <strong>strip out quoted material when using the <a href="http://www.damagedgoods.it/wp-plugins/quoter/" title="Quoter - DamagedGoods.it">Quoter</a> plugin</strong> and a second to <strong>suppress pingback entries that result from links to material within the blog</strong>.</p>
<p>Code from the first came from a <span class="removed_link" title="http://www.damagedgoods.it/wp-plugins/quoter/tutorial-integration-with-get-recent-comments/">blog posting</span> about how to get Quoter to work with a different recent comments plugin.  It is slightly modified, though, with the use non-greedy wildcard (<code>*?</code>) in the middle.  (It is possible to have more than one quoted section in a comment, and the original code would leave just the text beyond the final [/quote] tag.)  The context-sensitive diff is:</p>
```diff
*** recentCommentsWidget.php.dist	Wed Aug 23 09:52:11 2006
--- recentCommentsWidget.php	Wed Aug 23 11:22:14 2006
***************
*** 135,140 ****
--- 143,149 ----
  				// Comment Content -> Excerpt
  				$comment_content = strip_tags($comment->comment_content);
  				$comment_content = stripslashes($comment_content);
+ 				$comment_content = preg_replace('/\[quote(.|\s)*?\[\/quote\]/i', '', $comment_content); // remove quote tags and quoted text
  				$words=split(" ",$comment_content); 
  				
  				if($max_letters_per_word!=0) 
{
```
<p>The second is a modification to the SQL statement that pulls up records from the wp_comments table.  There is an additional <code>AND</code> conditional clause that eliminates the pingback where the URL of the pingback begins with the URL of the blog.  The context-sensitive diff:</p>
```diff
*** recentCommentsWidget.php.dist	Wed Aug 23 09:52:11 2006
--- recentCommentsWidget.php	Wed Aug 23 11:22:14 2006
***************
*** 221,227 ****
  	if (get_option('WPTagboardPostID')) {
  		$request .= "AND ID <> " . get_option('WPTagboardPostID') . " ";
  	}
! 
  	$request .= "AND comment_approved = '1' ORDER BY comment_ID DESC LIMIT $limit";
  	$comments = $wpdb->get_results($request);
--- 228,235 ----
  	if (get_option('WPTagboardPostID')) {
  		$request .= "AND ID <> " . get_option('WPTagboardPostID') . " ";
  	}
!     // Eliminate pingbacks/tracebacks by registered authors to posts on this blog
! 	$request .= "AND (comment_type = '' OR comment_author_url NOT LIKE \"".get_bloginfo('url')."%\") ";
  	$request .= "AND comment_approved = '1' ORDER BY comment_ID DESC LIMIT $limit";
  	$comments = $wpdb->get_results($request);
```
<p><a href="http://en.wikipedia.org/wiki/Notable_phrases_from_The_Hitchhiker&#039;s_Guide_to_the_Galaxy#Share_and_Enjoy" title="Notable phrases from The Hitchhiker&#039;s Guide to the Galaxy : Wikipedia">Share and Enjoy!</a>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.damagedgoods.it/wp-plugins/quoter/tutorial-integration-with-get-recent-comments/ on November 13th, 2012.</p>
