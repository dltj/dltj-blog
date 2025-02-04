---
layout: wordpress-import
status: published
published: true
title: 'Changes to "Emanuel African Methodist Episcopal Church" Wikipedia Page, Visualized'
modified: 2015-06-20T03:06:16+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 25925
wordpress_url: http://dltj.org/?p=25925
date: '2015-06-19 23:06:16 -0400'
date_gmt: '2015-06-20 03:06:16 -0400'
category: Meta Category
categories:
- Meta Category
tags:
- imagemagick
- Wikipedia
- history
comments:
- id: 679757
  author: Procrastine
  author_email: timothee.duhamel@gmail.com
  author_url: ''
  date: '2015-06-20 07:03:51 -0400'
  date_gmt: '2015-06-20 11:03:51 -0400'
  content: "Nice work!\r\nI have taken the liberty to rehost the gif as a webm on
    gfycat.com. Here it is: http://gfycat.com/ParchedInfamousArctichare"
- id: 679821
  author: Slow Knowledge - THE TWELVE
  author_email: ''
  author_url: http://blog.perspectivesjournal.org/2015/06/27/slow-knowledge/
  date: '2015-06-27 09:09:10 -0400'
  date_gmt: '2015-06-27 13:09:10 -0400'
  content: "[&#8230;] hours, 44 different editors made 152 edits to create a &ldquo;solid&rdquo;
    page, according to a fascinating blog post by librarian/blogger Peter Murray.
    Murray created an animation of that Wikipedia page so we can see [&#8230;]"
- id: 680049
  author: Wikipedian
  author_email: none@ofyourbusiness.org
  author_url: https://cosmiclattes.github.io/wikireplay/player.html
  date: '2015-08-05 07:14:29 -0400'
  date_gmt: '2015-08-05 11:14:29 -0400'
  content: 'Nice work, just wanted to point out that Wikireplay has been around for
    some time and does this for every article: https://cosmiclattes.github.io/wikireplay/player.html'
- id: 680050
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2015-08-05 08:56:33 -0400'
  date_gmt: '2015-08-05 12:56:33 -0400'
  content: Nice! Thank you for pointing out that project.
---
<p><i>Edited after initial publication to add:</i>&nbsp;My thoughts are with the people in and around Charleston, South Carolina, this evening. What is making it out of the media fog to me tonight is your compassion for each other. Please be well as you absorb, internalize, and recover from this shocking display of inhumanity.&nbsp;</p>
<p>This afternoon, Ed Summers tweeted:</p>
<blockquote class="twitter-tweet" lang="en">
<p lang="en" dir="ltr">36 hours, 152 edits, 44 editors and now Emanuel AME Church has a solid Wikipedia page <a href="https://t.co/pDLaAzbJLE">https://t.co/pDLaAzbJLE</a> thanks <a href="https://twitter.com/xor">@xor</a> creating it</p>
<p>&mdash; Ed Summers (@edsu) <a href="https://twitter.com/edsu/status/612003700324847616">June 19, 2015</a></p></blockquote>
<p><script async="" src="//platform.twitter.com/widgets.js" charset="utf-8"></script></p>
<p>I wondered what 152 edits -- from stub page to fleshed out -- looked like, so I created this animation of the <a href="https://en.wikipedia.org/wiki/Emanuel_African_Methodist_Episcopal_Church" title="Emanuel African Methodist Episcopal Church | Wikipedia">Emanuel African Methodist Episcopal Church</a> Wikipedia page as it was created:</p>
<p>[caption width="350" id="attachment_animation" align="aligncenter"]<br />
<video width="350" height="970" autoplay="1" loop="1" muted="1"><br />
  <source type="video/mp4"<br />
      src="/assets/images/2015/06/animation.mp4"/><br />
  <source type="video/webm"<br />
      src="/assets/images/2015/06/animation.webm"/><br />
  <img src="/assets/images/2015/06/animation.gif" alt="Animation of edits to the 'Emanuel African Methodist Episcopal Church' Wikipedia Page" width="350" height="970" class="size-full wp-image-animation"/></video> Animation of edits to the "Emanuel African Methodist Episcopal Church" Wikipedia Page (see <a href="/assets/images/2015/06/animation-full.gif" target="_blank">full-sized version</a> [86MB GIF])[/caption]</p>
<p>The page is very long, so in order to get it to scale to something that fits on a normal browser screen, the detail of what is happening is lost.  Still, it is interesting to watch the reference section grow, the infoboxes be added, and the text grow in chunks and occasionally shrink as edits are made.  Of course, watching the length of the page grow as more research is done and edits made.  I echo Ed's kudos to the Wikipedia editors that worked quickly to create a great source of information about the history of this church in a time when many people would be looking for it.</p>
<h2>Process</h2>
<p>There doesn't seem to be a way to programmatically get a list of URLs (or even OIDs) from Wikipedia for one of its pages, so I captured the HTML source of the church's history page and ran a rather hairy regular expression on the unordered list of history entries, replacing:</p>
```regex
^.*<a href="/article/emanuel-african-methodist-episcopal-church-wikipedia-page-visualized/" title="Emanuel African Methodist Episcopal Church" class="mw-changeslist-date">(\d\d):(\d\d), (\d\d) June 2015</a>&lrm; <span class="history-user"><a href="/article/emanuel-african-methodist-episcopal-church-wikipedia-page-visualized/">]*?>(.*?)</a>.*(<span class="comment">(.*)</span>)?.*</span>
```
<p>with</p>
```regex
https://en.wikipedia.org\t201506T\thttps://en.wikipedia.org\t\t\r
```
<p>Then I used the <a href="http://www.paulhammond.org/webkit2png/" title="webkit2png">webkit2png</a> program to grab the full page captures of each version of the wiki page:</p>
```bash
cat page-history.txt | \
 while read line; do \
   IFS=$'\t' read url timestamp editorurl editor < <<"$line"; \
   webkit2png -W 1400 -H 3800 -F -o raw/$timestamp $url; \
   sleep 5; \
 done
 ```
<p>With the full page captures in place, I resized and annotated the top of each with the timestamp and the wiki editor's name using <a href="http://www.imagemagick.org/script/convert.php" title="ImageMagick: Command-line Tools: Convert">Imagemagick <code>convert</code></a>:</p>
```bash
cat page-history.txt | \
 while read line; do \
   IFS=$'\t' read url timestamp editorurl editor < <<"$line"; \
   convert raw/$timestamp-full.png -resize 25% -background '#0008' -splice 0x20 \
   -pointsize 15 -fill white -annotate +10+16 "$timestamp  $editor" \
   labeled/$timestamp-labeled.png; \
 done
 ```
<p>Finally, I also used Imagemagick to create the animated GIF:</p>
```bash
convert -delay 50 -loop 0 labeled/*.png animation.gif
```
