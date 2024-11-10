---
layout: wordpress-import
status: published
published: true
title: 'Downloading the ALA Annual Meeting Planner to Your Mac iCal'
modified: 2008-05-27T14:41:55+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 367
wordpress_url: http://dltj.org/?p=367
date: '2008-05-27 10:41:55 -0400'
date_gmt: '2008-05-27 14:41:55 -0400'
category: Meeting
categories:
- Meeting
tags:
- ALA Annual Conference 2008
- iCalendar
- American Library Association
comments: []
---
<p>First, kudos to the vendor that runs the ALA Meeting Planner website.  They listened to suggestions and now include a way to download your event planner information to your desktop/handheld device using the <a href="http://en.wikipedia.org/wiki/ICalendar" title="iCalendar - Wikipedia">iCalendar</a> <a href="http://tools.ietf.org/html/rfc2445" title="RFC2445 standard for the iCalendar format">standard</a>.  It is available from the "<a href="http://ala.cistems.net/Show_Downloads.php" title="Download and Printing">Downloads and Printing</a>" page of <a href="http://ala.cistems.net/Show_Login.php" title="ALA Event Meeting Planner">your meeting planner homepage</a>.  (You'll need to sign in using the e-mail address listed on your ALA Annual Registration form plus the password "ala".)  Jump down to the end and select the "iCAL" button next to "Personal Itinerary" to download the iCalendar file.</p>
<p>Now comes the unfortunate part -- it doesn't import into <a href="http://www.apple.com/support/ical/" title="iCal support page at Apple">Mac iCal</a>.  Because of a structural error in the file, it may not import into other applications, either.  The problem stems from the fact that the unique identifier ("UID") for each event is not in fact unique -- it is the same for all events.  The fix is pretty simple, though:  open the .ics iCalendar file in a text editor ("<a href="http://docs.info.apple.com/article.html?artnum=304779" title="TextEdit help page at Apple">TextEdit</a>" on the Mac, "<a href="http://windowshelp.microsoft.com/Windows/en-US/Help/5d18d5fb-e737-4a73-b6cc-dccc637202311033.mspx" title="Notepad help page at Microsoft">Notepad</a>" on the PC) and make each UID unique.  In my case, the UID line for each event was:</p>
<blockquote><p><code>UID:EC9439B1-FF65-11D6-9973-003065F99D04</code></p></blockquote>
<p>The text file is somewhat confusing to read (it was meant for a machine to read, after all, not you), but you just have to look for each line that starts with UID.  I changed the last number of each entry to a sequential number, so in the end my file looked something like this:</p>
<blockquote><p>BEGIN:VCALENDAR<br />
PRODID:ALA Personal Itinerary<br />
[...]<br />
BEGIN:VEVENT<br />
CLASS:PUBLIC<br />
CREATED:20080514T021306Z<br />
PRIORITY:5<br />
SEQUENCE:5<br />
DTSTART;TZID=US/Pacific:20080628T103000<br />
DTEND;TZID=US/Pacific:20080628T120000<br />
SUMMARY:Building and Supporting Koha , an open-source ILS<br />
DESCRIPTION: Unit: LITA, Location: Hyatt Regency Orange County, Room: Grand A<br />
<b>UID:EC9439B1-FF65-11D6-9973-003065F99D01</b><br />
TRANSP:OPAQUE<br />
X-MICROSOFT-CDO-BUSYSTATUS:BUSY<br />
X-MICROSOFT-CDO-IMPORTANCE:1<br />
END:VEVENT<br />
BEGIN:VEVENT<br />
CLASS:PUBLIC<br />
CREATED:20080514T021306Z<br />
PRIORITY:5<br />
SEQUENCE:5<br />
DTSTART;TZID=US/Pacific:20080628T133000<br />
DTEND;TZID=US/Pacific:20080628T153000<br />
SUMMARY:There's No Catalog Like No Catalog:  The Ultimate Debate on the future of the Library Catalog<br />
DESCRIPTION: Unit: LITA, Location: Hyatt Regency Orange County, Room: Grand A<br />
<b>UID:EC9439B1-FF65-11D6-9973-003065F99D02</b><br />
TRANSP:OPAQUE<br />
X-MICROSOFT-CDO-BUSYSTATUS:BUSY<br />
X-MICROSOFT-CDO-IMPORTANCE:1<br />
END:VEVENT<br />
CLASS:PUBLIC<br />
CREATED:20080514T021306Z<br />
PRIORITY:5<br />
SEQUENCE:5<br />
DTSTART;TZID=US/Pacific:20080629T080000<br />
DTEND;TZID=US/Pacific:20080629T100000<br />
SUMMARY:Archiving in Practice with JPEG2000<br />
DESCRIPTION: Unit: LITA, Location: Anaheim Convention Center, Room: Ballroom E<br />
<b>UID:EC9439B1-FF65-11D6-9973-003065F99D03</b><br />
TRANSP:OPAQUE<br />
X-MICROSOFT-CDO-BUSYSTATUS:BUSY<br />
X-MICROSOFT-CDO-IMPORTANCE:1<br />
END:VEVENT<br />
END:VCALENDAR</p></blockquote>
<p>See the differences in the bolded lines?  The changes are done; save the file and import it into the Mac iCal program.  All of your entries will show up.  When you do this, also take note of this advice in the site's documentation:</p>
<blockquote><p><img border="0" src="/assets/images/2008/05/warning.jpg" alt="Warning Icon" width="24" height="24" style="float:left; padding-right: 9px; margin-bottom: 25px" /><strong>Dates are relative to the event's location, not the device's.</strong><br />
A meeting at 10am to 11am Pacific Standard Time (PST) will show up in the calendar of an attendee in Washington DC as 1pm to 2pm. When the device's clock is changed from Eastern Standard Time (EST) to PST, the calendar will automatically shift the appointment to the correct local time of 10am to 11am.</p></blockquote>
<p>Hope to see you in Anaheim!</p>
