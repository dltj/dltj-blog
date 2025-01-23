---
title: 'Issue 104: Long Term Digital Storage'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- digital storage
mastodon:

---
This week's _Thursday Threads_ looks at digital storage from the past and the future.
There are articles about the mechanics of massive data storage systems in tech giants like Google and Amazon, the still existing use of floppy disks in certain industries, and the herculean efforts of digital archivists to access stored data from outdated mediums. 

This week:

- Hard drives seem indestructible, especially compared to previous forms of storage. So we went all in on digitizing and converting and storing on hard drives. But what if the [hard drives start failing]({filename}#iron-mountain)?
- You've been tasked with storing data. You don't know what the data is or how important it is, but you have to give it back when asked. When your goal is [outliving the heat death of the universe]({filename}#s3).
- It is the rare company that reaches the size of Google, Amazon, or Facebook. These companies have a lot of data, and they want to make sure it is findable and usable anywhere in the company. What [distributed storage]({filename}#distributed-storage) looks like.
- When was the last time you used a floppy disk? There are some industries that [still use them every day]({filename}#still-using-floppies).
- Archives everywhere have stacks of old floppy disks. Read about the techniques that archivists use to [recover what is on them]({filename}#reading-old-floppy).
- Your job is to store data that outlasts your career. What medium do you use? How do you distribute it? How to think about [century-scale storage]({filename}#century-scale-storage).
- This Week I Learned: [In Ethiopia, time follows the sun like nowhere else]({filename}#twil).
- Obligatory Cat Photo: [Alan and Mittens squabble at the cat tree]({filename}#cats)

{{ thursday_threads_header() }}



## Hard Drives Go Bad {: #iron-mountain}

{{ thursday_threads_quote(href="https://www.mixonline.com/business/inside-iron-mountain-its-time-to-talk-about-hard-drives",
 blockquote='A few years ago, archiving specialist Iron Mountain Media and Archive Services did a survey of its vaults and discovered an alarming trend: Of the thousands and thousands of archived hard disk drives from the 1990s that clients ask the company to work on, around one-fifth are unreadable. Iron Mountain has a broad customer base, but if you focus strictly on the music business, says Robert Koszela, Global Director Studio Growth and Strategic Initiatives, “That means there are historic sessions from the early to mid-’90s that are dying.”',
 versiondate="2024-09-11",
 versionurl="https://web.archive.org/20240911130910/https://www.mixonline.com/business/inside-iron-mountain-its-time-to-talk-about-hard-drives",
 anchor="Inside Iron Mountain: It’s Time to Talk About Hard Drives",
 post=", Mix Magazine, 19-Aug-2024") }}

This article focuses on the music industry, but its story is applicable across all fields. 
Music production once used multi-track analog tape (where splicing was done with physical cuts and tape); when the process was done, the analog tape went into storage. 
Alarms went up in the field about media deterioration and a lot of effort was made to digitize the source materials.
Those digitized artifacts were stored on hard drives, and everyone assumed they were now safe. 
But preservation of digital media is an active process — one can't assume that the disks will spin and that the software to read the files still runs.


## When your goal is out living the heat death of the universe {: #s3}

{{ thursday_threads_quote(href="https://www.lastweekinaws.com/blog/s3-as-an-eternal-service/",
 blockquote='I sometimes think about the fact that Amazon S3 effectively has to exist until the heat death of the universe. Many millennia from now, our highly-evolved descendants will probably be making use of an equally highly evolved descendant of S3. It is fun to think about how this would be portrayed in science fiction form, where developers pore through change logs and design documents that predate their great-great-great-great grandparents, and users inherit ancient (yet still useful) S3 buckets, curate the content with great care, and then ensure that their progeny will be equally good stewards for all of the precious data stored within.',
 versiondate="2023-04-01",
 versionurl="https://web.archive.org/20230402004520/https://www.lastweekinaws.com/blog/s3-as-an-eternal-service/",
 anchor="S3 as an Eternal Service",
 post=", Last Week in AWS, 29-Mar-2023") }}
 
The idea that struck me in this article is that as service provider like Amazon can't distinguish between what is important and what is not: if a customer asked Amazon to store it, it will do its best to make sure it retrievable.
How much storage is in use — multiple copies on multiple drives in multiple servers and multiple locations — for files that have zero value?


## Distributed Storage Systems {: #distributed-storage}

{{ thursday_threads_quote(href="https://arstechnica.com/information-technology/2012/01/the-big-disk-drive-in-the-sky-how-the-giants-of-the-web-store-big-data/",
 blockquote='The impact of these distributed file systems extends far beyond the walls of the hyper-scale data centers they were built for— they have a direct impact on how those who use public cloud services such as Amazon&apos;s EC2, Google&apos;s AppEngine, and Microsoft&apos;s Azure develop and deploy applications. And companies, universities, and government agencies looking for a way to rapidly store and provide access to huge volumes of data are increasingly turning to a whole new class of data storage systems inspired by the systems built by cloud giants. So it&apos;s worth understanding the history of their development, and the engineering compromises that were made in the process.',
 versiondate="2012-01-28",
 anchor="The Great Disk Drive in the Sky: How Web giants store big—and we mean big—data",
 post=", Ars Technica, 25-Jan-2012") }}

This 13-year-old article explores the massive data storage systems utilized by major tech companies like Google, Amazon, and Facebook to manage their vast information stores. 
Traditional methods of scaling storage, such as increasing disk capacity or adding more servers, fall short at the size of in cloud computing environments. 
While you may not ever operate at the scale of these companies, it is interesting to read about how the tech giants do data storage and management. 
(The article's subtitle also refers to "big data" — a phrase that was fashionable in the previous decade but one which we don't hear much about anymore.)


## Industries are still using floppy disks {: #still-using-floppies}

{{ thursday_threads_quote(href="https://www.wired.com/story/why-the-floppy-disk-just-wont-die/",
 blockquote='A surprising number of industries, from embroidery to aviation, still use floppy disks. But the supply is finally running out.',
 versiondate="2023-03-07",
 versionurl="https://web.archive.org/20230307145317/https://www.wired.com/story/why-the-floppy-disk-just-wont-die/",
 anchor="Why the Floppy Disk Just Won’t Die",
 post=", Wired, 6-Mar-2023") }}

8-inch floppy disks were invented in the early 1970s; they could store a megabyte a piece.
5.25-inch floppy disks were introduced in late 1970s; while obviously smaller, its high density capacity could also store about a megabyte and a quarter per disk. 
3.5-inch disks (no longer called "floppy" because they were in a hard plastic case) came to the market in the early 1980s and could store a megabyte and a half. 
Each of these formats are still used today. 
(Maybe not the 8-inch floppies; those were {{ robustlink(href="https://www.cnet.com/science/us-military-retires-floppy-disks-used-by-nuclear-weapons-system/", versionurl="https://web.archive.org/web/20220829034438/https://www.cnet.com/science/us-military-retires-floppy-disks-used-by-nuclear-weapons-system/", versiondate="2022-08-29", title="US military retires floppy disks used by nuclear weapons system | CNET", anchor="retired from nuclear weapons silos in 2019") }}.)


## Reading old floppy disks {: #reading-old-floppy}

{{ thursday_threads_quote(href="https://digitalpreservation-blog.lib.cam.ac.uk/raw-flux-streams-and-obscure-formats-further-work-around-imaging-5-25-inch-floppy-disks-5a2cf2e5f0d1",
 blockquote='',
 versiondate="2024-04-21",
 versionurl="https://web.archive.org/20240421171052/https://digitalpreservation-blog.lib.cam.ac.uk/raw-flux-streams-and-obscure-formats-further-work-around-imaging-5-25-inch-floppy-disks-5a2cf2e5f0d1?gi=ab265ce08372",
 anchor="Raw flux streams and obscure formats: Further work around imaging 5.25-inch floppy disks",
 post=", Digital Preservation at Cambridge University Libraries, 19-Apr-2024") }}

Speaking of floppy disks, digital archivists from Cambridge University Library and Churchill Archives Centre detail their efforts to create copies of 5.25-inch floppy disks. 
Remember 5.25-inch floppy disks? 
From soliciting donations of old floppy disk drives to the hardware and software required to access these old disks on new hardware, the report is a fascinating look at the past (and maybe a preview of what future generations will need to do to read today's digital storage media).


## Century-scale Storage {: #century-scale-storage}

{{ thursday_threads_quote(href="https://lil.law.harvard.edu/century-scale-storage/",
 blockquote='This piece looks at a single question. If you, right now, had the goal of digitally storing something for 100 years, how should you even begin to think about making that happen? How should the bits in your stewardship be stored with such a target in mind? How do our methods and platforms look when considered under the harsh unknowns of a century? There are plenty of worthy related subjects and discourses that this piece does not touch at all. This is not a piece about the sheer volume of data we are creating each day, and how we might store all of it. Nor is it a piece about the extremely tough curatorial process of deciding what is and isn’t worth preserving and storing. It is about longevity, about the potential methods of preserving what we make for future generations, about how we make bits endure. If you had to store something for 100 years, how would you do it? That’s it.',
 versiondate="2024-12-15",
 versionurl="https://web.archive.org/web/20241215173726/https://lil.law.harvard.edu/century-scale-storage/",
 anchor="Century-Scale Storage: If you had to store something for 100 years, how would you do it?",
 post=", Harvard Law School Library Innovation Lab, undated") }}

This 15,000-word essay looks at digital storage from the earliest hard drives (including restoring data from a 1960s-era IBM hard disk prototype) to the cloud to old fashion print-on-paper. 
There are discussions of the reliability and longevity of different storage methods, such as RAID systems, cloud storage, and physical media like vinyl records and tape drives. 
But it isn't just the physical medium...the article also highlights the importance of institutional commitment, funding, and cultural values in ensuring the preservation of data. 
Ultimately, the writers suggest that successful century-scale storage requires a combination of methods, a culture of vigilance, and a commitment to preserving human cultural memory.


## This Week I Learned: In Ethiopia, time follows the sun like nowhere else {: #twil}

{{ thursday_threads_quote(href="https://theworld.org/stories/2015/01/30/ethiopian-time",
 blockquote='Because Ethiopia is close to the Equator, daylight is pretty consistent throughout the year. So many Ethiopians use a 12-hour clock, with one cycle of 1 to 12 — from dawn to dusk — and the other cycle from dusk to dawn. Most countries start the day at midnight. So 7:00 a.m. in East Africa Time, Ethiopia&apos;s time zone, is 1:00 in daylight hours in local Ethiopian time. At 7:00 p.m., East Africa Time, Ethiopians start over again, so it&apos;s 1:00 on their 12-hour clock.',
 versiondate="2025-01-23",
 versionurl="https://web.archive.org/web/20250123033849/https://theworld.org/stories/2015/01/30/ethiopian-time",
 anchor="If you have a meeting in Ethiopia, you'd better double check the time",
 post=", The World from PRX, 30-Jan-2015") }}
 
This could have easily gone in [last week's _Thursday Threads_ on time standards]({filename}2025-01-16-issue-103-time-standards). 
There are 12 hours of daylight, numbered 1 through 12.
Then 12 hours of night, numbered 1 through 12.
What could be easier?


## Alan and Mittens squabble in the cat tree {: #cats}

{{ image(width="400", localsrc="2025/2025-01-23-alan-and-mittens.jpg", alt="Two cats on a cat tree by a window; one above, white with black spots, and one below, black with a white chest. The one on the bottom is looking up with a 'hiss' in its mouth; the one on top looks down unconcerned.") }} 

These two troublemakers. 
Alan is the cat on top, looking down on Mittens below.
In this cozy sunlit room with a cat tree by an open window, you'd think these two would get along.
Not so.
Alan's typical perch is on top of the cat tree, so it is Mittens that is intruding (if you could call it that.)








