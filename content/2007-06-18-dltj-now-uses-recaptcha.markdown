---
layout: wordpress-import
status: published
published: true
title: 'DLTJ Now Uses reCAPTCHA'
modified: 2007-06-19T03:05:44+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 255
wordpress_url: http://dltj.org/2007/06/dltj-now-uses-recaptcha/
date: '2007-06-18 23:05:44 -0400'
date_gmt: '2007-06-19 03:05:44 -0400'
category: Meta Category
categories:
- Meta Category
tags:
- web design
- Disruptive Library Technology Jester
comments:
- id: 34687
  author: Leto A.
  author_email: leto@arrakis.org
  author_url: ''
  date: '2009-02-12 07:02:13 -0500'
  date_gmt: '2009-02-12 12:02:13 -0500'
  content: This is great, thanks for the heads up.
- id: 69715
  author: me
  author_email: me_again@yahoo.com
  author_url: ''
  date: '2010-05-17 17:04:03 -0400'
  date_gmt: '2010-05-17 21:04:03 -0400'
  content: "not sure that reCAPTCHA is so secure\r\nJust as i figured...hmm.."
- id: 69835
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-05-18 10:15:33 -0400'
  date_gmt: '2010-05-18 14:15:33 -0400'
  content: Is reCAPTCHA ultimately secure?  I'm not under any illusion that it is
    ("<a href="http://www.zdnet.com/blog/security/inside-indias-captcha-solving-economy/1835"
    rel="nofollow">No CAPTCHA can survive a human that&rsquo;s receiving financial
    incentives for solving it...</a>").  Does it raise the bar high enough that I'm
    not dealing with cleaning up a lot of comment spam after the fact? It seems to
    be working for me.  reCAPTCHA is, of course, not the only defense I use on <i>DLTJ</i>,
    but it is the most visible one.
- id: 287466
  author: jamie
  author_email: jhf1621@yahoo.com
  author_url: ''
  date: '2012-08-08 15:40:35 -0400'
  date_gmt: '2012-08-08 19:40:35 -0400'
  content: I hate recaptcha !!
- id: 288136
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2012-08-10 14:12:35 -0400'
  date_gmt: '2012-08-10 18:12:35 -0400'
  content: When I redesigned DLTJ a few months ago, I took out the reCAPTCHA requirement.  I've
    actually been quite please using just Akismet.
---
<p><acronym title="Disruptive Library Technology Jester"><i>DLTJ</i></acronym> now uses <a href="http://recaptcha.net/" title="reCAPTCHA homepage">reCAPTCHA</a> on comment forms.  reCAPTCHA is an enhanced version of CAPTCHA (an acronym for "completely automated public Turing test to tell computers and humans apart") and like the original it is a type of challenge-response test used to determine whether there is a human user at the other end of the browser or if it is a software agent (such as a SPAM robot).  And like the original it asks the user to type in recognized words from an image or a set of numbers from an audio clip.</p>
<p><img src="/assets/images/2007/06/reCAPTCHA_text.png" alt="reCAPTCHA example with text" title="reCAPTCHA example with text" width="313" height="123" border="0" /><img src="/assets/images/2007/06/reCAPTCHA_audio.png" alt="reCAPTCHA audio example" title="reCAPTCHA audio example" style="padding-left: 1em;" width="314" height="123" border="0" /></p>
<h2>Help with reCAPTCHA</h2>
<p>The reCAPTCHA box contains three buttons to help use the service:</p>
<table style="margin-left: 2em;">
<tr>
<td align="right" valign="top"><img src="/assets/images/2007/06/refresh.gif" width="25" height="17" alt="Refresh button" /></td>
<td><em>Refresh the word images.</em>  If you are unsure what the two words are, select this button to receive a new pair of words.  (Alternatively, just try to guess what the two words are; if you are wrong, you'll get a new pair of words automatically.)</td>
</tr>
<tr>
<td align="right" valign="top" style="white-space: nowrap;"><img src="/assets/images/2007/06/audio.gif" width="25" height="17" alt="Audio button" />&nbsp;/&nbsp;<img src="/assets/images/2007/06/text.gif" width="25" height="17" alt="Text button" /></td>
<td><em>Alternate between the Audio- and Text-based challenges.</em>  If you cannot see the word images, select this audio button to hear a set of digits among random noise that can be entered instead of the visual challenge.</td>
</tr>
<tr>
<td align="right" valign="top"><img src="/assets/images/2007/06/help.gif" width="25" height="17" alt="Help button" /></td>
<td><em>Get <span class="removed_link" title="http://recaptcha.net/popuphelp/">help from the reCAPTCHA site</span> about this human detection scheme.</em>  Also includes introductory information about the reCAPTCHA service itself.</td>
</tr>
</table>
<h2>What's Special About reCAPTCHA</h2>
<p><img src="/assets/images/2007/06/reCAPTCHA_example.png" alt="Example words from a reCAPTCHA challenge" title="Example words from a reCAPTCHA challenge" style="float: left; border: 1px solid gray; margin: 0 1.5em 1em 0;" width="263" height="47" border="0" /> The human mind is still a more powerful computer than any silicon circuitry in place now or in the foreseeable future.  With just a glance our brains can recognize the patterns among the noise &mdash; something that is computationally very expensive or impossible to do.  reCAPTCHA researchers at Carnegie Mellon University, also the home of the original CAPTCHA concept, estimate that 60 million CAPTCHAs are solved by humans around the world every day with roughly ten seconds of human time are being spent in each instance. That is not a lot of time per person, but in aggregate it adds up to more than 150,000 hours of work each day.</p>
<p>In the original CAPTCHA scheme, that work is wasted on deciphering random strings of letters and numbers.  The researchers at Carnegie Mellon realized that they could harness that work to resolve ambiguities in deciphering scanned text from books.  As with the original CAPTCHA system, there are some blocks of scanned text that computers cannot decipher yet are easily readable by humans.  reCAPTCHA pairs a known word with one of these unknown blocks of text.  If the human types the known word correctly, the reCAPTCHA system tells the <acronym title="Disruptive Library Technology Jester"><i>DLTJ</i></acronym> system that the comment is coming from a human.  And if enough humans type the same response for the unknown block of text, the reCAPTCHA system can be pretty sure the word has been deciphered.</p>
<p>So by commenting here on <acronym title="Disruptive Library Technology Jester"><i>DLTJ</i></acronym> you are helping make the world a better place by aiding in the digital conversion of texts from the Internet Archive.  This is a bit of an experiment, so if it is not working out, please let me know.
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://recaptcha.net/popuphelp/ on November 8th, 2012.</p>
