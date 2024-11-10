---
layout: wordpress-import
status: published
published: true
title: 'HOWTO Deal With Spam as a Mailman List Owner'
modified: 2008-07-17T01:47:05+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 398
wordpress_url: http://dltj.org/?p=398
date: '2008-07-16 21:47:05 -0400'
date_gmt: '2008-07-17 01:47:05 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- howto
- email
- mailman
comments:
- id: 34355
  author: terry
  author_email: terrymzo@ggmail.com
  author_url: http://corlive.com
  date: '2008-12-06 09:39:37 -0500'
  date_gmt: '2008-12-06 14:39:37 -0500'
  content: "\"Dealing with SPAM e-mail is a real hassle\"\r\n\r\nYes, it is, that's
    why you should use http://corlive.com !"
---
<p>Dealing with SPAM e-mail is a real hassle.  Dealing with SPAM e-mail as a mailing list owner is an even bigger hassle.  Here are some tips for dealing with SPAM e-mail on mailing lists using the <a href="http://www.list.org/" title="Mailman, the GNU Mailing List Manager">Mailman</a> software package.</p>
<h2>The Symptoms</h2>
<p>Unless you are making your users as well as yourself miserable, you've probably set the "Action to take for postings from non-members for which no explicit action is defined" to "Hold".  I believe this is the default setting for new lists.</p>
{{ image(
    div_float="none",
    width="500",
    caption="Hold Nonmember setting in Mailing list administration,  Privacy Options, Sender filters",
    alt="\"Hold Nonmember\" Setting in Mailing list administration -> Privacy Options -> Sender filters",
    localsrc="2008/07/hold-nonmember.png") }}
{: #genericNonmemberActionLink}
<p>This will hold all of the messages sent by non-members -- all of those spamy e-mail addresses -- to a queue on the Mailman server.  You'll receive a notification that a message is being held for you:<br />
<blockquote><code>As list administrator, your authorization is requested for the following mailing list posting:<br />
&nbsp;<br />
&nbsp;&nbsp;List:&nbsp;&nbsp;&nbsp;&nbsp;<i>mailingListName</i>@<i>mailingListHost</i><br />
&nbsp;&nbsp;From:&nbsp;&nbsp;&nbsp;&nbsp;<i>spam-email-address</i><br />
&nbsp;&nbsp;Subject:&nbsp;:)<br />
&nbsp;&nbsp;Reason:&nbsp;&nbsp;Post by non-member to a members-only list<br />
&nbsp;<br />
At your convenience, visit:<br />
&nbsp;<br />
&nbsp;&nbsp;http://<i>mailingListHost</i>/mailman/admindb/<i>mailingListName</i><br />
&nbsp;<br />
to approve or deny the request.<br /></code></p></blockquote>
<p>You'll also get a message once a day telling you that these messages are being held and insisting that you do something about it.<br />
<blockquote><code>The <i>mailingListName</i>@<i>mailingListHost</i> mailing list has 3 request(s) waiting for your consideration at:<br />
&nbsp;<br />
&nbsp;&nbsp;http://<i>mailingListHost</i>/mailman/admindb/<i>mailingListName</i><br />
&nbsp;<br />
Please attend to this at your earliest convenience. &nbsp;This notice of pending requests, if any, will be sent out daily.<br /></code></p></blockquote>
<h2>A Solution</h2>
<p>This isn't an ideal solution, but it at least lets you ignore the vast majority of these messages confidently knowing that -- unless your mailing list is unlucky enough to be hit daily by spam -- eventually the daily prodding messages will go away.  The key is to set the "Discard held messages older than this number of days" to some reasonable number:</p>
{{ image(
    div_float="none",
    width="500",
    caption="Discard Messages setting in Mailing list options, General options",
    alt="\"Discard Messages\" setting in Mailing list options -> General options",
    localsrc="2008/07/discard-messages.png") }}
{: #maxDaysOnHoldLink}
<p>I use "4" in that field:  two days to cover weekends plus a two day grace period.  For a message that is errantly caught in the queue (because it was too large, was sent by a subscriber who's email address changed, or other reason), I now have four days to release it.  If I do nothing, the message disappears from the hold queue after that time, and I get this final e-mail message:</p>
<blockquote><p><code>From:&nbsp;&nbsp;&nbsp;&nbsp;<i>mailingListName</i>-bounces@<i>mailingListHost</i><br />
Subject:&nbsp;<i>mailingListName</i> moderator request check result<br />
Date:&nbsp;&nbsp;&nbsp;&nbsp;July 16, 2008 8:00:08 AM EDT<br />
To:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>mailingListName</i>-owner@<i>mailingListHost</i><br />
&nbsp;<br />
Notice: 1 old request(s) automatically expired.<br /></code></p></blockquote>
<h2>Customize these instructions</h2>
<p>This posting contains a fragment of JavaScript that allows you to customize the instructions above.  If you are the owner of a Mailman mailing list, enter in the hostname of your Mailman host and the name of the list below, select Customize, and links will appear under the two images above that will take you to that setting on your list.</p>
<form action="." onsubmit="return replaceLinks(this)">
<table cellspacing="10">
<tr valign="bottom">
<td><label for="listName">Name of List</label>:&nbsp;<input name="listName" id="listName" type="text" />
</td>
<td><label for="listHost">Mailman Host</label>:&nbsp;<input name="listHost" id="listHost" type="text" value="ohiolink.edu" /></td>
<td><input type="submit" value="Customize" /></td>
</tr>
</table>
</form>
<p><span id="sampleLink">Note that this JavaScript probably doesn't work in feed readers, but you can make it work by <a href="/article/mailman-spam-howto/">viewing this post on the <acronym title="Disruptive Library Technology Jester"><i>DLTJ</i></acronym> site</a>.</span></p>
<p><script type="text/javascript" language="javascript1.3"><br />
function replaceLinks(formdata) {<br />
  var lHost;<br />
  var lName;<br />
  with (formdata) {<br />
    lHost = listHost.value;<br />
    lName = listName.value;<br />
  }<br />
  var listAdminAddr = "http://" + lHost + "/mailman/admin/" +lName;<br />
  var gnaLink = document.getElementById('genericNonmemberActionLink');<br />
  var newGNAanchor = document.createElement('a');<br />
  var newGNAhref = document.createAttribute('href');<br />
  newGNAhref.nodeValue = listAdminAddr + "/?VARHELP=privacy/sender/generic_nonmember_action";<br />
  newGNAanchor.setAttributeNode(newGNAhref);<br />
  var newGNAid = document.createAttribute('id');<br />
  newGNAid.nodeValue = 'genericNonmemberActionLink';<br />
  newGNAanchor.setAttributeNode(newGNAid);<br />
  newGNAanchor.appendChild(document.createTextNode("Set the Generic Nonmember Action parameter for list " + lName + " on " + lHost + "."));<br />
  var newGNAfrag = document.createDocumentFragment();<br />
  newGNAfrag.appendChild(newGNAanchor);<br />
  gnaLink.parentNode.replaceChild(newGNAfrag, gnaLink);<br />
  var maxDaysOnHoldLink = document.getElementById('maxDaysOnHoldLink');<br />
  var newMDOHanchor = document.createElement('a');<br />
  var newMDOHhref = document.createAttribute('href');<br />
  newMDOHhref.nodeValue = listAdminAddr + "/?VARHELP=general/max_days_to_hold";<br />
  newMDOHanchor.setAttributeNode(newMDOHhref);<br />
  var newMDOHid = document.createAttribute('id');<br />
  newMDOHid.nodeValue = 'maxDaysOnHoldLink';<br />
  newMDOHanchor.setAttributeNode(newMDOHid);<br />
  newMDOHanchor.appendChild(document.createTextNode("Set the Max Days to Hold parameter for list " + lName + " on " + lHost + "."));<br />
  var newMDOHfrag = document.createDocumentFragment();<br />
  newMDOHfrag.appendChild(newMDOHanchor);<br />
  maxDaysOnHoldLink.parentNode.replaceChild(newMDOHfrag, maxDaysOnHoldLink);<br />
  var sampleLink = document.getElementById('sampleLink');<br />
  var newSanchor = document.createElement('a');<br />
  var newShref = document.createAttribute('href');<br />
  newShref.nodeValue = listAdminAddr;<br />
  newSanchor.setAttributeNode(newShref);<br />
  var newSid = document.createAttribute('id');<br />
  newSid.nodeValue = 'sampleLink';<br />
  newSanchor.setAttributeNode(newSid);<br />
  newSanchor.appendChild(document.createTextNode("Links in this document are now customized to " + listAdminAddr + "."));<br />
  var newSfrag = document.createDocumentFragment();<br />
  newSfrag.appendChild(newSanchor);<br />
  sampleLink.parentNode.replaceChild(newSfrag, sampleLink);<br />
  return false;<br />
}<br />
</script></p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://dltj.org/article/mailman-spam-howtomailman-spam-howto/ to http://dltj.org/article/mailman-spam-howto/ on December 30th, 2010.</p>
