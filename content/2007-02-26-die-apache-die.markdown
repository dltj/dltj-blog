---
layout: wordpress-import
status: published
published: true
title: 'Killing Off Runaway Apache Processes'
modified: 2007-02-26T22:03:10+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 191
wordpress_url: http://dltj.org/2007/02/die-apache-die/
date: '2007-02-26 17:03:10 -0500'
date_gmt: '2007-02-26 22:03:10 -0500'
category: Raw Technology
categories:
- Meta Category
- Raw Technology
tags:
- WordPress
- Gentoo
- system administration
- apache
comments:
- id: 12850
  author: Jonathan Rochkind
  author_email: rochkind@jhu.edu
  author_url: http://bibwild.wordpress.com
  date: '2007-03-06 15:36:48 -0500'
  date_gmt: '2007-03-06 20:36:48 -0500'
  content: "Are you going to tell us how you tracked down the problem?\r\n\r\nI too
    have an occasional runaway Apache instance, although in a completely different
    environment (we don't even run PHP. But we do run Perl for a certain vendor's
    application)."
- id: 12988
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2007-03-08 14:37:27 -0500'
  date_gmt: '2007-03-08 19:37:27 -0500'
  content: "[quote comment=\"12850\"]Are you going to tell us how you tracked down
    the problem?[/quote]\r\n\r\nPure chance, actually.  I was making a run through
    the WordPress plug-ins that I use looking for updated versions and I ran across
    the comment on the blog page for the footnote plug-in.  Sorry to report that I
    have no generally useful suggestions for tracking down such problems."
- id: 82114
  author: Apache Getting Bogged Down By Certain Script (Wp-Cron.php) - How To Kill
    Process Automatically - Server Fault
  author_email: ''
  author_url: http://serverfault.com/questions/166538/apache-getting-bogged-down-by-certain-script-wp-cron-php-how-to-kill-process
  date: '2010-08-08 17:58:03 -0400'
  date_gmt: '2010-08-08 21:58:03 -0400'
  content: "<!--%kramer-ref-pre%-->[...] have seen various other scripts such as :
    http://dltj.org/article/die-apache-die/ . I took a look at the stat of /proc.
    But I was boggled at which delimited part was the time [...]<!--%kramer-ref-post%-->"
---
<p>Well, something is still going wrong on <i>dltj.org</i> &mdash; despite <a href="/article/wordpress-mysql-tuning/">previous performance tuning efforts</a>, I'm still running into cases where machine performance grinds to a halt.  In debugging it a bit further, I've found that the root cause is an apache httpd process which wants to consume nearly all of real memory which then causes the rest of the machine to <a href="http://en.wikipedia.org/wiki/Thrash_%28computer_science%29" title="Wikipedia: Thrash">thrash</a> horribly.  The problem is that I haven't figured out what is causing that one thread to want to consume so much RAM &mdash; nothing unusual appears in either the access or the error logs and I haven't figured out a way to debug a running apache thread.  (Suggestions anyone?)</p>
<div style="border: 1px solid black; color black; background: #EEE">
<strong>Found it!</strong>  It was a WordPress plug-in plus a change to the PHP configuration that was causing the problem.  The fix for the fundamental cause of the problem came from a comment timestamped February 8th, 2007 at 3:55 pm on the <a href="http://www.elvery.net/drzax/2006/02/10/footnotes-0-9-plugin-for-wordpress-2-0-x/" title="http://www.elvery.net/drzax/2006/02/10/footnotes-0-9-plugin-for-wordpress-2-0-x/">Footnotes 0.9 Plugin for WordPress 2.0.x</a> page.  An infinite loop was consuming both CPU cycles and RAM, and this was exacerbated by a change I made to the maximum CPU execution time for PHP scripts that was required in order to play with the <a href="http://wordpress.org/plugins/ipccp/" title="WordPress &rsaquo; Error">IP City Cluster plug-in</a>.  With the patch to the Footnotes plug-in, <i>dltj.org</i> has gone 12 hours without a run-away apache process.
</div>
<p>In any case, I whipped up this little ditty that is running every five minutes in cron as a way to gloss over the problem for the moment.  Running as root, it looks into all of the processes in the <a href="http://en.wikipedia.org/wiki/Procfs" title="Wikipedia: procfs">virtual /proc file system</a>, specifically in the 'stat' file, and using <a href="http://en.wikipedia.org/wiki/AWK_%28programming_language%29" title="Wikipedia: AWK">awk</a> looks to see if the second space-delimited value is the name of the httpd process (this is the <a href="http://www.gentoo.org/" title="Gentoo Linux -- Gentoo Linux News">Gentoo Linux</a> distribution, so the name of the process is <tt>apache2</tt>) and the 23rd space-delimited value (the virtual size of the process) is bigger than 800MB.  If so, it prints out the PID of the process (the first value in the <tt>stat</tt> file) at which the bash script unceremoniously sends it a <tt>kill</tt> ('-9') signal.  The script looks like this:</p>
```bash
#!/bin/bash
for i in `/bin/ls -d /proc/[0-9]*`; do
        if [ -f $i/stat ]; then
                pid=`/bin/awk '{ if ($2 == "(apache2)" &amp;&amp; $23 > 800000000) print $1}' $i/stat`
                if [ "$pid" != "" ]; then
                        echo "Killing $pid because of load average: `awk '{print $1}' /proc/loadavg`"
                        kill -9 $pid
                fi
        fi
done
```
<p>If anyone has any suggestions as to how to narrow down what the problem might be, I'd appreciate hearing from you.  I've tried eliminating Wordpress plugins, recompiling Wordpress and Apache, and attempted to catch the behavior with a network traffic sniffer, but have come up empty so far.
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://blog.vimagic.de/ip-city-cluster-wordpress-plugin/ to http://wordpress.org/plugins/ipccp/ on August 22nd, 2013.</p>
