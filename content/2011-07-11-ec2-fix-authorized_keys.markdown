---
layout: wordpress-import
status: published
published: true
title: 'Fixing a Bad SSH authorized_keys under Amazon EC2'
modified: 2011-07-12T02:38:29+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 3061
wordpress_url: http://dltj.org/?p=3061
date: '2011-07-11 22:38:29 -0400'
date_gmt: '2011-07-12 02:38:29 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- system administration
- Amazon EC2
comments:
- id: 156019
  author: Stephen Michael Kellat
  author_email: skellat@fastmail.net
  author_url: ''
  date: '2011-07-12 00:11:23 -0400'
  date_gmt: '2011-07-12 04:11:23 -0400'
  content: I am curious.  Would a viable alternate strategy have been to replace your
    local SSH key, log-in with the username/password challenge, then proceed to rebuild
    authorized_keys?
- id: 156104
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-07-12 08:27:30 -0400'
  date_gmt: '2011-07-12 12:27:30 -0400'
  content: "My log files are showing quite a number of ssh login probing attempts,
    so I've disabled password logins on my servers.  In <code>sshd_config</code>:
    <pre lang=\"shell\">PasswordAuthentication no\r\nUsePAM no</pre>So I wouldn't
    be able to move aside the public half of the key and log in with a password."
- id: 159711
  author: ALA_TechSource
  author_email: ''
  author_url: http://twitter.com/ala_techsource/status/92594423522795521
  date: '2011-07-17 14:00:05 -0400'
  date_gmt: '2011-07-17 18:00:05 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Via @DataG Fixing a Bad SSH authorized_keys under
    Amazon EC2 http://bit.ly/nQjggB</span></span>
- id: 159712
  author: ALA_TechSource
  author_email: ''
  author_url: http://twitter.com/ala_techsource/status/91547515538780160
  date: '2011-07-14 16:40:03 -0400'
  date_gmt: '2011-07-14 20:40:03 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Via @DataG Fixing a Bad SSH authorized_keys under
    Amazon EC2  http://bit.ly/nQjggB</span></span>
- id: 159713
  author: Library Feed
  author_email: ''
  author_url: http://twitter.com/libraryfeed/status/90624553662939136
  date: '2011-07-12 03:32:31 -0400'
  date_gmt: '2011-07-12 07:32:31 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Fixing a Bad SSH authorized_keys under Amazon
    EC2 http://bit.ly/mQFiLw</span></span>
- id: 159714
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/90617954957406208
  date: '2011-07-12 03:06:18 -0400'
  date_gmt: '2011-07-12 07:06:18 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Fixing a Bad SSH authorized_keys
    under Amazon EC2 http://bit.ly/plxCE0</span></span>'
- id: 230923
  author: Andrew Eells
  author_email: ''
  author_url: http://twitter.com/agile_cto/status/179201816108609536
  date: '2012-03-12 13:46:57 -0400'
  date_gmt: '2012-03-12 17:46:57 -0400'
  content: "<span class=\"topsy_trackback_comment\"><span class=\"topsy_twitter_username\"><span
    class=\"topsy_trackback_content\">what to do when you inadvertently lock yourself
    out of one of your #aws servers - after shouting \"doh!\" that is \nhttp://t.co/DgCXr5hb</span></span>"
- id: 264818
  author: Stephane Rondal
  author_email: ''
  author_url: http://twitter.com/stephanerondal/status/215796886286778368
  date: '2012-06-21 13:22:41 -0400'
  date_gmt: '2012-06-21 17:22:41 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Locked myself out of my EC2 instance by installing
    gitolite (my stupid). This article saved my life. Thanks to @DataG http://t.co/mGjhj6M2</span></span>
- id: 342008
  author: Ezra
  author_email: ezra.pierce@gmail.com
  author_url: ''
  date: '2012-11-02 17:04:02 -0400'
  date_gmt: '2012-11-02 21:04:02 -0400'
  content: Nice one. This probably saved me half a day :-)
- id: 509059
  author: Keeyai
  author_email: keeyai@gmail.com
  author_url: ''
  date: '2013-04-11 16:58:35 -0400'
  date_gmt: '2013-04-11 20:58:35 -0400'
  content: I somehow allowed group access to my home directory and found myself in
    this situation. Thanks for the walkthrough - you saved me today.
- id: 652454
  author: Sam Bossen
  author_email: sam@richcap.com
  author_url: http://right-handed-monkey.blogspot.com/
  date: '2013-11-22 07:30:58 -0500'
  date_gmt: '2013-11-22 12:30:58 -0500'
  content: Thank you for this.  I wish I had thought of it.  You saved me loads of
    hassle.  You may want to mention to reconnect any elastic ips, since the server
    is being shutdown and restarted.  Just a thought.
- id: 656292
  author: Sourabh kapoor
  author_email: kapoor.utd@gmail.com
  author_url: ''
  date: '2014-03-22 15:19:28 -0400'
  date_gmt: '2014-03-22 19:19:28 -0400'
  content: "hanks for detailed doc. I locked myself out as changed something in ubuntu
    .ssh authorized files permissions.\r\nI Created new instance, detach old volume
    from old instance and attached old volume to new instance and now cant login.
    Am i missing something? I cant login to new instance and it has same problem as
    old one.\r\n\r\nAny advise?"
- id: 656308
  author: Sam
  author_email: rooster@richcap.com
  author_url: ''
  date: '2014-03-23 13:17:25 -0400'
  date_gmt: '2014-03-23 17:17:25 -0400'
  content: You don't want to detach the working drive in your new instance because
    you need to boot to that.  You'll need to have both working and the non-working
    drive mounted but boot to the working drive.  Then change the permissions on the
    file you need.
- id: 678752
  author: Omar
  author_email: osteinberg@stand.org
  author_url: ''
  date: '2015-04-03 17:27:55 -0400'
  date_gmt: '2015-04-03 21:27:55 -0400'
  content: Thank you so so so much for this article - it saved my tail!
- id: 686353
  author: Leandro Cosas
  author_email: lecosas@gmail.com
  author_url: ''
  date: '2016-06-24 09:19:30 -0400'
  date_gmt: '2016-06-24 13:19:30 -0400'
  content: "Thanks a lot for sharing this information. You keep me alive! \r\nThank
    God ;)"
---
<p>I was doing some maintenance on the Amazon EC2 instance that underpins <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym></i> and in the process managed to mess up the .ssh/authorized_keys file.  (Specifically, I changed the permissions so it was group- and world-readable, which <a href="https://help.ubuntu.com/community/SSH/OpenSSH/Keys#Permission%20denied%20%28publickey%29">causes `sshd` to not allow users to log in using those private keys</a>.)  Unfortunately, there is only one user on this server, so effectively I just locked myself out of the box.</p>
{% highlight shell %}
$ ssh -i .ssh/EC2-dltj.pem me@dltj.org
Identity added: .ssh/EC2-dltj.pem (.ssh/EC2-dltj.pem)
Permission denied (publickey).
{% endhighlight %}
<p>After browsing the Amazon support forums I managed to puzzle this one out.  Since I didn't see this exact solution written up anywhere, I'm posting it here hoping that someone else will find it useful.  And since you are reading this, you know that they worked.</p>
<h2>Solution Overview</h2>
<p>Basically we've got to get the root filesystem mounted on another EC2 instance so we can get access to it.  I'm using placeholder identifiers like <code>i-target</code>, <code>i-scratch</code>, and <code>vol-rootfs</code> in place of real values.</p>
<ol type="1" start="1">
<li>Stop the target EC2 instance (<code>i-target</code>).</li>
<li>Note the location of and unmount its root filesystem, and detach its EBS volume (<code>vol-rootfs</code>) from the target instance (<code>i-target</code>).</li>
<li>Attach the volume (<code>vol-rootfs</code>) on another EC2 instance (<code>i-scratch</code>) and mount the filesystem.</li>
<li>Change the file permissions (or whatever needs to be done).</li>
<li>Unmount the filesystem and detach the volume (<code>vol-rootfs</code>) from the other EC2 instance (<code>i-scratch</code>).</li>
<li>Attach the volume (<code>vol-rootfs</code>) to the target EC2 instance (<code>i-target</code>) and start it.</li>
</ol>
<p>Assuming you've got all of the environment variables set up with the appropriate AWS credentials, these are the commands:</p>
<h2>Stop the Target Instance</h2>
{% highlight shell %}
$ ec2-stop-instances i-target
{% endhighlight %}
<h2>Detach Root EBS Volume</h2>
<p>A couple of steps here.  We need to remember where the root filesystem is mounted so we can put it back at the end.  So first get a description of the instance.  It will look something like this.</p>
{% highlight shell %}
$ ec2-describe-instances i-instance
INSTANCE	i-instance	ami-xxxxxxxx	ec2-[your-IP].compute-1.amazonaws.com	[...lots of other stuff....]
BLOCKDEVICE	/dev/sdh    vol-datafs      2011-07-12T01:37:21.000Z
BLOCKDEVICE	/dev/sda1   vol-rootfs      2011-07-12T01:37:21.000Z
{% endhighlight %}
<p>In this case we need to remember <code>/dev/sda1</code>.  (Note that we can ignore the <code>vol-datafs</code> -- on my instance it is where the database and other data is stored.  If you don't know which volume is your root volume, you might be facing some trial and error in the steps below until you find it.)  Now we detach it:</p>
{% highlight shell %}
$ ec2-detach-volume vol-rootfs
{% endhighlight %}
<h2>Attach Volume Elsewhere</h2>
<p>This set of instructions assumes that you have another EC2 instance running somewhere else.  If you don't have one, start a micro instance for this purpose then terminate it when you are done.  We're going to attach it as <code>/dev/sdf</code>.</p>
{% highlight shell %}
$ ec2-attach-volume vol-rootfs --instance i-scratch -d /dev/sdf
{% endhighlight %}
<p>Now log into <code>i-scratch</code> and mount the volume.</p>
{% highlight shell %}
$ mount /dev/sdf /mnt
{% endhighlight %}
<h2>Make Changes</h2>
<p>In my case:</p>
{% highlight shell %}
$ chmod 600 /mnt/home/me/.ssh/authorized_keys
{% endhighlight %}
<h2>Unmount/Detach from i-Scratch</h2>
<p>While still on the i-scratch server:</p>
{% highlight shell %}
$ umount /mnt
{% endhighlight %}
<p>Detatch from the scratch server.</p>
{% highlight shell %}
$ ec2-detach-volume vol-rootfs
{% endhighlight %}
<h2>Reattach the Volume and Start the Server</h2>
<p>We're on the home stretch now.  Note that in the first command we're using the mount point we found in the second step.</p>
{% highlight shell %}
$ ec2-attach-volume vol-rootfs --instance i-target -d /dev/sda1
$ ec2-start-instances i-target
{% endhighlight %}
<p>After the instance starts, you should be able to log in.  If not, go through the steps again and read the syslog files in <code>/var/log</code> to figure out what is going on.</p>
