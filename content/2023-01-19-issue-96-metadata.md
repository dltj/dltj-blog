---
title: 'Issue 96: Metadata'
modified: 2023-01-18T21:05:11-05:00
category: Thursday Threads
categories:
- Thursday Threads
tags:
- metadata
- OCLC
mastodon:
- #Libraries love #metadata. This week's issue of the DLTJ Thursday Threads #newsletter gives a glimpse of how much we love it and what librarians go through to make it the best it can be. https://dltj.org/article/issue-96-metadata 1/4
- 12 years ago, #OCLC Research conducted a study on the most common fields in #WorldCat. Everything has a title, of course, but then the number of fields that library records have in common drops off quickly. https://dltj.org/article/issue-96-metadata#most-important 2/4
- Bibliographic metadata is the lifeblood of libraries, and libraries have a long history of cooperating on its creation and maintenance. #ICOLC wants to be sure that tradition continues. https://dltj.org/article/issue-96-metadata#icolc-statement 3/4
- Everyone has a personal name, and personal names are among the most trickiest bits of description that libraries deal with. Last year, @kcoyle@mstdn.social showed us how tricky names can be. https://dltj.org/article/issue-96-metadata#names 4/4
- And the weekly cat. This week, Alan looks back as if to say, "who me?" Yes you, Alan. bonus/4
---
Metadata is at the core of what libraries do. 
("[metadata](https://dltj.org/tag/metadata)" is one of the most common tags on this here library technology blog.)
We gather information about the resources available to patrons, then massage it and slice it and sort it and display it in ways that help patrons find what they need. 
I was thinking about metadata because of a [thread](https://dltj.org/article/thursday-threads-2011w3/#corebibdescr) that ran here in _Thursday Threads_ 12 years ago. 
That is the first thread in this issue, and it is followed by more recent articles about metadata.

- [The Most Important Library Metadata](https://dltj.org/article/issue-96-metadata#most-important)
- [ICOLC Statement on the Metadata Rights of Libraries](https://dltj.org/article/issue-96-metadata#icolc-statement)
- [What's in a name?](https://dltj.org/article/issue-96-metadata#names)

{{ thursday_threads_header() }}

## The Most Important Library Metadata
{: #most-important}
{{ image(div_float="right", width="350", localsrc="2023/2023-01-19-marc-tags.png", caption="Table 2.1—MARC tags occurring in 20% or more of WorldCat records—from 'Implications of MARC Tag Usage on Library Metadata Practices'", alt="Screen capture of a table, which is described in the text below.") }}{{ thursday_threads_quote(href="https://hangingtogether.org/the-core-of-bibliographic-description/",
 blockquote='<p>The outliers in this case are those elements that appear in a large number of records — that is, what might be considered “core” elements that are used to describe the vast majority of library owned material.</p><p>Those “outliers” can be categorized according to three general purposes:</p>
<ul>
<li><i>Provenance and Identity:</i> identifiers (e.g. ISBN, OCLC, etc.) and cataloging source (040)</li>
<li><i>Elements useful for discovery:</i> title statement (245), personal names (100, 700) and subject (650)</li>
<li><i>Elements useful for understanding and evaluation:</i> publication statement (260), physical description (300), and notes (500)</li></ul>
<p>That’s it. In a nutshell you have the very core of bibliographic description as defined by librarians over the last century or so.</p>',
 versiondate="2023-01-18",
 versionurl="https://web.archive.org/web/20230119005635/https://hangingtogether.org/the-core-of-bibliographic-description/",
 anchor="The Core of Bibliographic Description",
 post=', Roy Tennant, OCLC Research&apos;s "Hanging Together" blog, 17-Jan-2011') }}

Back in 2011, Roy Tennant posted a summary of this research on the fields that libraries use most often when describing stuff. 
It pointed to a report from which the above table is taken, _{{ robustlink(href="https://www.oclc.org/content/dam/research/publications/library/2010/2010-06.pdf", versionurl="https://web.archive.org/web/20220924225010/https://www.oclc.org/content/dam/research/publications/library/2010/2010-06.pdf", versiondate="2023-01-18", title="Implications of MARC Tag Usage on Library Metadata Practices | OCLC Research", anchor="Implications of MARC Tag Usage on Library Metadata Practices") }}_. 
WorldCat is the name of a database of records from libraries. 
As the table shows, every record has some mandatory elements: a control number, a set of codes called the "fixed length data elements", a source for where the record came from, and the title. 
Most records also have an imprint (96%) and a physical description (number of pages, etc.—91%). 
In library-speak, the "main entry" is the person or organization responsible for the work, and the research found that 61% of records had a personal "main entry"...what we could commonly call the author.
46% of records have a topical subject and 44% had a descriptive note of some sort. 
Rounding out the last entries in the table, 28% of records had an additional responsible entry—a second author or illustrator or similar—and 23% of records had an ISBN. 

Now library records have hundreds of fields and variations of fields to describe more esoteric aspects of a work, but these are the most common. 
Just a fun fact for your next dinner party.  


## ICOLC Statement on the Metadata Rights of Libraries
{: #icolc-statement}
{{ thursday_threads_quote(href="https://icolc.net/statements/icolc-statement-metadata-rights-libraries",
 blockquote='<p>Metadata and the metadata services that describe library collections are critical in supporting content discovery, knowledge creation, and libraries’ public missions. Metadata describing library collections is not typically copyrightable, and should be considered freely shareable and reusable under most circumstances. However, some industry players restrict libraries’ rights to use such metadata through contractual terms and market influence. Such restrictive activity is out of alignment with libraries’ needs and public, not-for-profit/educational missions.</p><p>The endorsers of this document urge all organizations, whether for-profit or not-for-profit, to uphold libraries’ rights and interests to use, re-use, adapt, aggregate, and share metadata that describes library collections to serve the public interest, without restriction or limitation.</p>',
 versiondate="2022-09-11T13:08:09",
 versionurl="https://web.archive.org/20220911170812/https://icolc.net/statements/icolc-statement-metadata-rights-libraries",
 anchor="ICOLC Statement on the Metadata Rights of Libraries",
 post=", International Coalition of Library Consortia (ICOLC) website, 26-Aug-2022") }}

As you might guess, metadata is really important to libraries. 
And libraries have a natural ethos to cooperate with one another to share the burden of creating and maintaining that metadata. 
Not all of the actors in the metadata world, though, are naturally so cooperative, and this statement from ICOLC emphasizes the need to keep this cooperative ethos going for the benefit of all libraries.


## What's in a name?
{: #names}
{{ thursday_threads_quote(href="https://kcoyle.blogspot.com/2022/01/whats-in-name.html",
 blockquote='Because of both the great variety of name forms and the variability of applications that make use of names, I recommend a metadata vocabulary that follows the principle of minimum semantic commitment. This means a vocabulary that includes broad classes and properties that can be used as is where detailed coding is not needed or desired, but which can be extended to accommodate many different contexts.',
 versiondate="2022-01-27",
 versionurl="https://web.archive.org/web/20220127160437/https://kcoyle.blogspot.com/2022/01/whats-in-name.html",
 anchor="What's in a Name?",
 post=",  Coyle&apos;s InFormation , 26-Jan-2022") }}

This is a great article if you like going down rabbit holes. 
In the Western world (the overwhelmingly large number of _Thursday Threads_ readers), you'll see a form ask you for first name, last name, and sometimes middle name. 
What happens, though, when names are much more complex than that: 

- When you add a birth date and/or death date to disambiguate people with the same name. 
- When you encounter titles ("Sir") or a generational ("Jr.") suffix. 
- What about cultures that by convention put their family name before their given name.

These are the types of things that Karen Coyle explores in this blog post.


## Who me?
{: #alan}
{{ image(div_float="right", width="300", localsrc="2023/2023-01-19-alan-who-me.jpg", alt="Photograph of a white cat with black splotches sitting on a wicker cat tree in front of a sliding door. The cat's body is facing a way but it has its head twisted back towards the camera.") }} 
Ah, the innocence of a cat face. 
Who would believe this cute face could cause any trouble. 

Hopefully Alan is looking healthier now. 
He was on a steady path towards completely rejecting the food we had for him. 
Fortunately, we found some wet food and some kibble that he likes to eat and is good for his sensitive stomach. 
Unfortunately, though, we've had one room-clearing episode of flatulence that may be caused by this new food, so we might be back to the drawing board.