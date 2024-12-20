---
layout: wordpress-import
status: published
published: true
title: 'Child Rearing Through HTTP Status Codes'
modified: 2006-12-15T21:24:10+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 152
wordpress_url: http://dltj.org/2006/12/child-rearing-through-http-status-codes/
date: '2006-12-15 16:24:10 -0500'
date_gmt: '2006-12-15 21:24:10 -0500'
category: Personal
categories:
- Personal
tags:
- standards
- rest
- humor
comments: []
---
<p>Long time readers of DLTJ know that I rarely post commentary outside the realm of disruptive library technology to this blog, much less reflections of personal, non-work life.  This will be an exception, though, because it straddles that boundary between technology and family.  It is called <a href="http://web.archive.org/web/20110607150329/http://diveintomark.org/archives/2006/12/07/rest-for-toddlers" title="REST for toddlers [dive into mark]">REST for toddlers</a> and it comes to us from the "dive into mark" blog.  By way of explanation, REST (as a technology term, not as used in the sentence "parents with young children often which they had a chance to <em>rest</em>.") is an acronym for <a href="http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm" title="Architectural Styles and the Design of Network-based Software Architectures">Representational State Transfer</a>, a way of constructing URLs so that they are useful outside the context of your current web browsing session (e.g. bookmarkable and/or e-mailable to someone else).  REST rides atop the HTTP protocol, of which <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html" title="HTTP/1.1: Status Code Definitions">section 10 of the specification</a> talks about response codes from clients to servers.  What Mark has done is offer a real-life explanation of some of those response codes in the context of child-rearing.  A sample:</p>
<blockquote>
<dl>
<dt id="http200"><samp>200 OK</samp></dt>
<dd>&ldquo;OK.&rdquo;</dd>
<dt id="http201"><samp>201 Created</samp></dt>
<dd>&ldquo;You went pee-pee in the potty!&rdquo;</dd>
<dt id="http202"><samp>202 Accepted</samp></dt>
<dd>&ldquo;Daddy will do it in a minute.&rdquo;</dd>
<dt id="http204"><samp>204 No Content</samp></dt>
<dd>&ldquo;&hellip;&rdquo;</dd>
<dt id="http300"><samp>300 Multiple Choices</samp></dt>
<dd>&ldquo;Do you want apple juice or do you want milk?&rdquo;</dd>
</dl>
</blockquote>
<p>So, it would seem to me, that I just need to teach my daughter the HTTP protocol, at which point I can make our challenge/response dialog much more efficient:</p>
<ul>
<li><b>Her:</b> Can I go outside?</li>
<li><b>Me:</b>Sure!  200</li>
</ul>
<ul>
<li><b>Her:</b> Do you know where my bouncy ball is?</li>
<li><b>Me:</b> Sorry, 404. 302.</li>
</ul>
<ul>
<li><b>Her:</b> Well, then can I have that bucket and shovel?</li>
<li><b>Me:</b> 409.</li>
<li><b>Her:</b> Ple-e-e-s-e?!?</li>
<li><b>Me:</b> 304, and if you keep asking, 403!</li>
</ul>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://diveintomark.org/archives/2006/12/07/rest-for-toddlers to http://web.archive.org/web/20110607150329/http://diveintomark.org/archives/2006/12/07/rest-for-toddlers on November 6th, 2012.</p>
