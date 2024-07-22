---
layout: wordpress-import
status: published
published: true
title: Getting a Hyperlink of the Last Sent Message from Mail.app using Applescript
modified: 2018-01-15T22:38:08-05:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 363
wordpress_url: https://dltj.org/?p=363
date: '2008-05-15 12:15:15 -0400'
date_gmt: '2008-05-15 16:15:15 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Mac OS X Operating System
- Getting Things Done
- email
- applescript
- OmniFocus
comments:
- id: 33290
  author: Getting a Hyperlink of the Last Sent Message from Mail.app using Applescript
    - The Omni Group Forums
  author_email: ''
  author_url: http://forums.omnigroup.com/showthread.php?goto=lastpost&amp;t=8028
  date: '2008-05-21 18:45:36 -0400'
  date_gmt: '2008-05-21 22:45:36 -0400'
  content: "<!--%kramer-ref-pre%-->[...] I can easily refer back to the e-mail I sent
    that is waiting for a reply.  Details can be found at http://dltj.org/article/copy-last-se...e-as-rtf-link/.
    \        Post 1     [...]<!--%kramer-ref-post%-->"
- id: 33628
  author: Applescript Forums | MacScripter / convert link in HTML to link in RTF
  author_email: ''
  author_url: ''
  date: '2008-07-24 13:16:03 -0400'
  date_gmt: '2008-07-24 17:16:03 -0400'
  content: "<!--%kramer-ref-pre%-->[...] to see if I could find an answer to. I located
    something close to what you were trying to do from http://dltj.org/article/copy-last-sent-
    &hellip; -rtf-link/ but needed to modify it a bit.Re-creating the .sh file that
    Brett Terpstra had written was easy [...]<!--%kramer-ref-post%-->"
- id: 36379
  author: Alfred Fazio
  author_email: alfred.fazio@gmail.com
  author_url: ''
  date: '2009-06-09 22:35:26 -0400'
  date_gmt: '2009-06-10 02:35:26 -0400'
  content: "This is fucking AMAZING.\r\n\r\nAfter hours of pulling my hair out trying
    to find a way to create a hyperlink in Numbers 09, this was the ONLY way I could
    get it to work.  Absolutely perfect.  Can't thank you enough!"
- id: 173684
  author: MacScripter / convert link in HTML to link in RTF
  author_email: ''
  author_url: http://macscripter.net/viewtopic.php?id=26498
  date: '2011-10-03 18:25:11 -0400'
  date_gmt: '2011-10-03 22:25:11 -0400'
  content: "<!--%kramer-ref-pre%-->[...] to see if I could find an answer to. I located
    something close to what you were trying to do from http://dltj.org/article/copy-last-sent-
    &hellip; -rtf-link/ but needed to modify it a bit.Re-creating the .sh file that
    Brett Terpstra had written was easy [...]<!--%kramer-ref-post%-->"
---
I've been a fan of [Getting Things Done](http://en.wikipedia.org/wiki/Getting_Things_Done) as a technique for managing projects, but it was only recently that I settled on OmniFocus as the "trusted system" collecting all of my next actions. One of the things I like about [OmniFocus](http://www.omnigroup.com/applications/omnifocus/) -- as a rich, Mac-only application -- is its ability to hold links to messages from Mail.app as notes for each action. This occurs, for instance, when you use the "Clippings" function of OmniFocus to create a new action based on the message that you are currently viewing in Mail.app. (There are other ways to do it, such as the method described by [Adam Sneller](http://www.earth2adam.com/omnifocus-gtd-actions-from-mail-redux/).)

One of the things I find myself doing is creating actions in a "Waiting" context based on e-mail messages I've just sent. Initially, I'd just create the action via the OmniFocus Quick Entry window. But I found myself needing to refer back to the message I sent when the person I'm waiting on doesn't come through. So I started clicking and dragging the message from the Sent mailbox to the action. But to do that I'd have to click into the Sent mailbox and have the Mail.app and the OmniFocus windows set up just right. Or I'd have to follow a select-sent-mailbox, select-message, OmniFocus-quick-entry-with-clipping, select-Inbox, select-next-message workflow. And that took time and effort. So I've created an AppleScript ditty that does the work of creating a hyperlink on the clipboard of the last sent message. The results can then be pasted into any RTF-aware application, including OmniFocus.  
  
The script is based heavily on [Speedy creation of rich text links to Mail messages](http://www.tuaw.com/2008/04/14/speedy-creation-of-rich-text-links-to-mail-messages/) by [Brett Terpstra](http://www.tuaw.com/bloggers/brett-terpstra/). In particular, he had the missing link about creating RTF hyperlinks on the clipboard using a bash shell script. The meat of the AppleScript is:

```AppleScript
tell application "Mail"

	-- Ask the user which account to use
	set _accts to get accounts
	set _enabledAccounts to {}
	repeat with eachAccount in _accts
		-- Only offer the enabled accounts for the user to choose
		if enabled of eachAccount then
			set the end of _enabledAccounts to name of eachAccount as string
		end if
	end repeat
	set _selectedAccount to (choose from list _enabledAccounts with title "Select Account" with prompt "Select the account from which to copy a link of the last sent message..." default items (item 1 of _enabledAccounts))
	
	-- Quit script if the user selected "cancel"
	if _selectedAccount is false then
		return
	end if
	set _selectedAccountName to _selectedAccount as string
	
	-- Get the "last" message of the Sent mailbox of the selected account
	set _msg to first message of mailbox "Sent" of account _selectedAccountName
	
	-- Get various properties of the message
	set _date to _msg's date sent
	
	try
		set _recipient to name of first recipient of _msg
		set _test to _recipient
	on error
		-- if the Recipient's name property was blank, use the e-mail address instead
		set _recipient to address of first recipient of _msg
	end try
	
	set _sub to _msg's subject
	if _sub starts with "Re:" then
		-- Remove the "Re:" prefix from messages
		set _sub to text 5 through (length of _sub) of _sub
	end if
	
	set _msgid to _msg's message id
	
	-- Create the URL to the message
	set _msglnk to "message://%3C" & my urlencode(_msgid) & "%3E"
	
	-- Create the anchor text for the link
	set _anchorText to "Message sent " & _date & " to " & _recipient & " regarding '" & _sub & "'"

	-- Execute the external script to generate the RTF hyperlink on the clipboard
	do shell script "/bin/bash -c \"" & _script & " \\"" & _anchorText & "\\" \\"" & _msglnk & "\\"\""
end tell
```

It first prompts the user for which account to use based on the list of active accounts. Then it gets the last message in the Sent mailbox of that account, gets various metadata properties, and sends the results to the bash shell script. The shell script comes from Brett; it creates the RTF snippet and pipes it into '[pbcopy](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/pbcopy.1.html)' to put it on the clipboard:

```bash
#!/bin/bash
# Places a rich text link on the clipboard
# usage: rtflink.sh "Title of link" "URL to link to"
#
# This will paste *nothing* into applications that don't recognize rich text

echo "{\rtf1\ansi\ansicpg1252\cocoartf949\cocoasubrtf270
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww9000\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\ql\qnatural\pardirnatural
{\field{\*\fldinst{HYPERLINK \"$2\"}}{\fldrslt 
\f0\fs24 \cf0 $1}}}" | pbcopy -Prefer rtf
```

The end result is a hyperlink with an anchor that looks something like:

<pre>    Message sent Thursday, May 15, 2008 8:36:33 AM to Jane Partner regarding 'Can you pick up milk?'</pre>

...waiting on the clipboard to be pasted into an action note. With that bound to a keyboard trigger via QuickSilver, copying a link to a message is now a simple matter of keystrokes.

If you are interested, you can [download the "Copy last sent message as RTF link" AppleScript bundle](/wp-content/uploads/2008/05/copy-last-sent-message-as-rtf-link.zip) and try it yourself. Let me know what you think.

Update 20080516T1219 : I had to modify the part of the code that gets the recipient name or (for recipients without name parts) the e-mail address. The downloaded version has been updated.

Update 20110405T1946 : The script has been improved! See this [thread on the Omni Group forums](http://forums.omnigroup.com/showthread.php?t=20397) for the update. Thanks to [whpalmer4](http://forums.omnigroup.com/member.php?u=5000) for the modifications.

The text was modified to remove a link to http://docs.blacktree.com/quicksilver/triggers on January 28th, 2011.

