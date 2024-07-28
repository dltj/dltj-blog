---
title: 'Issue 86: Tracking Media Provenance, Digital Classroom Surveillance, Don''t Pixelate to Redact, Android In-App Advertising'
modified: 2022-02-24T09:20:09-05:00
category: Thursday Threads
categories:
- Thursday Threads
tags:
- Android operating system
- privacy
- higher education
- advertising
---
I've deleted what I originally had here as newsletter-opening-banter. These are serious times. I think the world has radically changed overnight, and roughly 7.9 billion of us are not in positions to do anything about it. To those that are in positions to do something about it and to those that are caught up in the effects of one man's decision to impose _his_ will on others: may you be safe, may you succeed, and may you find peace.  For those coming to this after early 2022, yesterday Russia invaded the sovereign country of Ukraine.
{{ robustlink(href="https://en.wikipedia.org/wiki/2022_Russian_invasion_of_Ukraine", versionurl="https://en.wikipedia.org/w/index.php?title=2022_Russian_invasion_of_Ukraine&oldid=1073778722", versiondate="2022-02-24", title="2022 Russian invasion of Ukraine", anchor="Russia invaded the sovern country of Ukraine") }} 

The threads this week:

* [Specification for Media Content Provenance]({filename}/2022-02-24-issue-86-provenance-privacy-pixelation#content-provenance)
* [Encroaching on Digital Privacy in the Classroom]({filename}/2022-02-24-issue-86-provenance-privacy-pixelation#surveillance-university)
* [Pixelation for Redaction → bad]({filename}/2022-02-24-issue-86-provenance-privacy-pixelation#pixelation-redation)
* [Google Changes Up In-App Advertising]({filename}/2022-02-24-issue-86-provenance-privacy-pixelation#android-privacy-sandbox)

{{ thursday_threads_header() }}


## Specification for Media Content Provenance
{: #content-provenance}

{{ thursday_threads_quote(href="https://c2pa.org/post/release_1_pr/",
 blockquote='Today, the Coalition for Content Provenance and Authenticity (C2PA), an organization established to provide publishers, creators, and consumers with opt-in, flexible ways to understand the authenticity and provenance across various media types, released version 1.0 of its technical specification for digital provenance. This specification is the first of its kind and empowers content creators and editors worldwide to create tamper-evident media, by enabling them to selectively disclose information about who created or changed digital content and how it was altered. The C2PA’s work is the result of industry-wide collaborations focused on digital media transparency that will accelerate progress toward global adoption of content provenance.',
 versiondate="2022-02-22 21:28:19+00:00",
 versionurl="https://web.archive.org/20220222220810/https://c2pa.org/post/release_1_pr/",
 anchor="C2PA Releases Specification of World's First Industry Standard for Content Provenance",
 post=", Coalition for Content Provenance and Authenticity, 26-Jan-2022") }}{{ image(div_float="right", width="320", localsrc="2022/2022-02-24-c2pa_visualglossary.png", caption="Elements of the C2PA specification. <a href='https://c2pa.org/specifications/specifications/1.0/specs/C2PA_Specification.html#_overview_2'>[Source]</a>", alt="This image shows how all these various elements come together to represent the C2PA architecture.", ahref="https://c2pa.org/specifications/specifications/1.0/specs/C2PA_Specification.html#_overview_2") }}

This is a fascinating development. 
Although the target audience for this technology is news organizations and citizen journalists to provide a way to establish the creator and editors of media, one could easily envision using this standard to mark images, video, and audio from digital archives. 
As a way of combatting problems like manipulated media and "deep fakes", the specification would allow news organizations to cryptographically "sign" the media in a way that a display tool—via a media tool on your device or a browser plugin—would be able to decode and display to the viewer. 
If the cryptographic signature doesn't match the one published by the news organization, you would know that the media has been changed.
Or, from the perspective of an activist or citizen journalist, the capture device—be it a smartphone or digital camera—could add indelible information to the media file that shows where and when it came from.

The C2PA website has a recording of a 90-minute webinar introducing the specification.  Some quotes from that webinar:

> At the point of recording, typically on a mobile device, when you hit the record button, you grab the date and time, the GPS location, all the pixels, you create a hash or digital compact signature, you cryptographically sign that. And essentially that is a stamp of authenticity put either by the hardware or software at the point of recording. And nobody is in a better place to authenticate content than exactly at this point of recording.

And later:

> If an edit is made in a system without C2PA then the consumer is notified by a missing or incomplete message in the content credentials. C2PA also uses a failsafe for recovery in case of malicious or accidental stripping of providence information. It can always be recovered and matched again with the photo. By comparing the changes made along the way, viewers get a more complete picture of how the content came to be.

There are some serious privacy concerns, but they have accounted for some issues in the specification:

> Privacy is one of the foremost guiding principles of C2PA.  One of the most important principles is privacy.  This is all intended to be opt-in; the guidance documents and the UX task force looked very carefully at ensuring that users of the technology and the producers on the creator side understand what they are doing, when it should be used, and when it shouldn't be used...
> 
> There is a notion of redaction that is baked into the standard that doesn't compromise the cryptographic certainty of what has gone before.

So _that's_ interesting. 
See how it could be used for digital archives? 
I haven't finished reading the specification, but I have made some Hypothesis annotations on the ["explainer"](https://c2pa.org/specifications/specifications/1.0/explainer/Explainer.html) and ["technical specifications"](https://c2pa.org/specifications/specifications/1.0/specs/C2PA_Specification.html). 
Join me there, would you?

## Encroaching on Digital Privacy in the Classroom
{: surveillance-university}

{{ thursday_threads_quote(href="https://georgetownvoice.com/2022/02/19/welcome-to-surveillance-university-where-privacy-no-longer-matters/",
 blockquote='Perusall, for example, gives professors access to the amount of time a student spends on a reading and how many of the assigned pages they&#39;ve viewed. Despite students feeling like their privacy is compromised with this access and the return of most students to in-person learning, schools are still utilizing proctoring and similar invasive technologies.

The use of virtual learning tools has been subject to the fluctuating pandemic and schools&#39; virtual status, with the Omicron variant causing many colleges to move online for final exams and the beginning of the spring semester. As COVID-19 continues, students have been increasingly subject to excessive monitoring technologies—whether proctoring exams or scanning files—such as Proctorio, ProctorU, and Perusall.',
 versiondate="2022-02-20 03:42:02+00:00",
 versionurl="https://web.archive.org/20220220042237/https://georgetownvoice.com/2022/02/19/welcome-to-surveillance-university-where-privacy-no-longer-matters/",
 anchor="Welcome to Surveillance University, where privacy no longer matters",
 post=", The Georgetown Voice, 19-Feb-2022") }}

This article is from the Georgetown University student-run newspaper, and it contains perspectives from students about the invasiveness of the surveillance technology being used in classrooms. 
The emergency measures put in place for at-home learning during pandemic closures are weaving their way into the fabric of college life, and not in a good way. 
This article is a good one to read because it is written by students that are impacted by this technology, but it is just one among many similar articles that describe the technical problems and the cultural impacts. 

## Pixelation for Redaction → bad
{: pixelation-redation}

{{ thursday_threads_quote(href="https://bishopfox.com/blog/unredacter-tool-never-pixelation",
 blockquote='Today, we&#39;re focusing on one such technique – pixelation – and will show you why it&#39;s a no-good, bad, insecure, surefire way to get your sensitive data leaked. To show you why, I wrote a tool called Unredacter that takes redacted pixelized text and reverses it back into its unredacted form. There&#39;s plenty of real-world examples of this in the wild to redact sensitive information, but I won&#39;t name names here. Watch my video for a quick recap of the importance of NEVER using pixelation to redact text, as well as how I unredact Jumpseclabs&#39;s Challenge in real-time.',
 versiondate="2022-02-18 02:27:49+00:00",
 versionurl="https://web.archive.org/web/20220218051725/https://bishopfox.com/blog/unredacter-tool-never-pixelation",
 anchor="Never Use Text Pixelation To Redact Sensitive Information",
 post=", Bishop Fox, 15-Feb-2022") }}

The solution, in retrospect, seems obvious: figure out the font being used, deduce the offset from where the pixelation starts, build a model of letters of the alphabet pixelated to those parameters, and compare with the source material. 
I won't be using pixelation again. 

## Google Changes Up In-App Advertising
{: android-privacy-sandbox}

{{ thursday_threads_quote(href="https://mobiledevmemo.com/rip-gaid-privacy-sandbox-is-coming-to-android-heres-a-summary-of-the-tech/",
 blockquote='it&#39;s a collaborative effort that invites participation from the industry in replacing the existing system for ads targeting on Android with something that is more mindful of consumer privacy. Although Google recently introduced some new privacy initiatives on Android, including the reanimation of its mostly-dormant “Opt Out of Ads Personalization” system setting as an Android-equivalent of Apple&#39;s Limit Ad Tracking setting, it obviously wants to introduce further privacy controls to Android. And it aims to accomplish that with a Privacy Sandbox process for the platform.',
 versiondate="2022-02-18 01:40:16+00:00",
 versionurl="https://web.archive.org/20220218020809/https://mobiledevmemo.com/rip-gaid-privacy-sandbox-is-coming-to-android-heres-a-summary-of-the-tech/",
 anchor="RIP GAID: Privacy Sandbox is coming to Android. What advertisers need to know.",
 post=", Mobile Dev Memo, 16-Feb-2022") }}

This one is mostly for the technical-minded readers. 
I wasn't around at the _start_ of computing, but I've been around long enough to respect the growing sophistication of software development and how layers of the technology stack that are innovative now become assumed-to-exist in just a short while. 
What is fascinating about this technique from Google is that the creators of the Android operating system are abstracting out a whole segment of dynamic code libraries. 
In this case, the advertising tech will be distributed in self-contained blobs that are published by distinct companies. 
At the time an app is installed by the smartphone user, the app code and advertising code are put linked together and sent to the device. 
Once on the device, the ad-tech runs in a separate sandbox from the browser—it is isolated from the app code and has its own permissions structure. 
It is not hard to imagine that this technique will be used for other dynamic parts of an app.

## Close Supervision
{: close-supervision}


{{ image(div_float="right", width="320", localsrc="2022/2022-02-24-supervising-cat.png", caption="Alan lets me know he is watching.", alt="Two photographs in one image. The top picture is of seedlings that have just sprouted in a growing tray under a bright light. In the bottom image, a white cat with a dark fur outline around his face is on an open staircase eye level and is reaching out and reaching out a paw.") }} 

I am the caretaker this week for some newly planted seedlings in the basement. 
Among my tasks is to spray them with water to keep them moist and growing. 
I was doing just that earlier this week when I felt this tap from behind. 
Alan was checking my progress and had a few unsolicited suggestions. 
A couple of scratches behind the ears—well, more than a couple—and all was well again.

Seriously, the darn cat reached through the open stairwell, looked me straight in the eye from his elevated position, and meowed insistently in my face for attention.

The _nerve_ of some beasts!

I should have followed his suggestions, though...I think a couple of the seedlings aren't going to make it.

## Thursday Morning Addition
{: ukrane-colleagues}

After I finished writing Wednesday night but before publishing Thursday morning, Russia's president gave the order to invade Ukraine from the north, east, and south. 
Geopolitics aside (Putin's actions are not warranted and by accounts I've read his interpretation of history is wrong), there are real effects on real people that don't deserve to be caught up in what has happened. 
To FOLIO Project colleagues—notably the EPAM staff located in and around Ukraine—I am thinking about you and praying for your safety and the safety of your family and friends.