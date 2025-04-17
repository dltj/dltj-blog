---
title: 'Issue 115: Public and Private Camera Networks'
posted: 2025-04-10
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- privacy
- law enforcement
summary: "This Thursday Threads issue explores the growth of surveillance camera networks like license plate readers, highlighting privacy concerns despite their law enforcement benefits. It discusses investigations, security flaws, private networks, AI integration, and artistic controversies."
bluesky: "This week's issue of Thursday Threads discusses the rise of surveillance camera networks, focusing on license plate readers and their privacy issues. It highlights investigations, security flaws, and private camera networks, as well as the integration of AI systems and controversial artistic uses of public cameras. Plus, this week I learned about the origin of the word 'scapegoat'...and a cat picture."
---
After [last week's issue on digital privacy]({filename}2025-04-10-issue-114-digital-privacy), I thought I'd focus this week on government-sponsored or -enabled surveillance. 
As I dug through my store of saved articles, though, I realized I had quite a number of a particular kind of surveillance: camera networks. 
These are often municipal-sponsored systems of license plate readers, but there are also networks of private systems—and, of course, attempts to combine the output of all of these networks.
So that is the focus of this week's _Thursday Threads_ issue:

- An investigation by a newspaper editor highlights privacy concerns and legal challenges in rural [Virginia's use of license plate reading cameras]({filename}#va-lpr). (2025)
- Debate over the privacy concerns and legal challenges of license plate readers is nothing new, as [this 2012 article shows]({filename}#lprs).
- What happens when you put equipment not meant for the internet onto the internet? A security flaw in Motorola's automated license-plate-recognition systems [exposes real-time vehicle data and video feeds online]({filename}#motorola). (2025)
- A license plate reader in every tow truck? Privacy concerns of a [private surveillance network of 9 billion license plate scans]({filename}#dnr) enable widespread vehicle tracking. (2019)
- Similar to "the call is coming from inside the house", the surveillance is coming from inside your community. Privacy concerns emerge as [HOAs nationwide install Flock Safety's license plate readers]({filename}#hoa), facilitating police surveillance. (2023)
- How about we network all of these cameras together? [AI-powered surveillance system]({filename}#fusus) spurs privacy concerns as adoption grows in U.S. (2023)
- If we've got to have this tech, we might as well have some fun with it. [Artist's Traffic Cam Photobooth]({filename}#tcp) sparks controversy and cease-and-desist over creative use of NYC traffic cameras. (2024)
- [This Week I Learned]({filename}#twil): The word "scapegoat" was coined in a 1530 translation of the bible.
- [This week's cat]({filename}#cats})

Also on DLTJ since the last newsletter was published:

- [My Public Archive of #TeslaTakedown Protest Signs]({filename}2025-04-11-tesla-takedown-protest-signs). Print one off and take it to <em>your</em> next protest.

{{ thursday_threads_header() }}



## Privacy Concerns and Legal Challenges in Rural Virginia's Use of License Plate Reading Cameras {: #va-lpr}
{{ thursday_threads_quote(href="https://cardinalnews.org/2025/03/28/i-drove-300-miles-in-rural-virginia-then-asked-police-to-send-me-their-public-surveillance-footage-of-my-car-heres-what-i-learned/",
 blockquote='The research for State of Surveillance showed that you can’t drive anywhere without going through a town, city or county that’s using public surveillance of some kind, mostly license plate reading cameras. I wondered how often I might be captured on camera just driving around to meet my reporters. Would the data over time display patterns that would make my behavior predictable to anyone looking at it? So I took a daylong drive across Cardinal Country and asked 15 law enforcement agencies, using Freedom of Information Act requests, to provide me with the Flock LPR footage of my vehicle. My journey took me over 300 miles through slices of the communities those agencies serve, including the nearly 50 cameras they employ. And this journey may take me to one more place: an April Fool’s Day hearing in a courtroom in Roanoke. There, a judge will be asked to rule on a motion to declare the footage of the public to be beyond the reach of the public.',
 versiondate="2025-03-29",
 versionurl="https://web.archive.org/20250329181633/https://cardinalnews.org/2025/03/28/i-drove-300-miles-in-rural-virginia-then-asked-police-to-send-me-their-public-surveillance-footage-of-my-car-heres-what-i-learned/",
 anchor="I drove 300 miles in rural Virginia, then asked police to send me their public surveillance footage of my car. Here's what I learned",
 post=", Cardinal News, 28-Mar-2025") }}

In a detailed exploration of public surveillance, this newspaper editor drove 300 miles across rural Virginia, requesting footage from police of their vehicle captured by license plate reading cameras. 
The investigation aimed to understand how often people are recorded by these cameras and the implications of such surveillance. 
Despite asking 15 law enforcement agencies for footage, only nine complied while others denied the request, leading to a legal challenge regarding public access to this data. 
The editor noted that while driving through various counties, their vehicle was indeed photographed multiple times by {{ robustlink(href="https://www.flocksafety.com/industries/law-enforcement", versionurl="https://web.archive.org/web/20250408172555/https://www.flocksafety.com/industries/law-enforcement", versiondate="2025-04-16", title="Flock Safety for Law Enforcement", anchor="Flock cameras") }}, which capture detailed images of vehicles, including license plates and unique identifiers. 
The editor also reflected on the ease with which police could track movements without a warrant, emphasizing a shift in expectations regarding privacy in public spaces. 



## Debate Grows Over Privacy Concerns and Legal Challenges as License Plate Readers Expand Across the U.S. {: #lprs}
{{ thursday_threads_quote(href="https://arstechnica.com/tech-policy/2012/09/your-car-tracked-the-rapid-rise-of-license-plate-readers/",
 blockquote='The scanners can read 60 license plates per second, then match observed plates against a "hot list" of wanted vehicles, stolen cars, or criminal suspects. LPRs [license plate readers] have increasingly become a mainstay of law enforcement nationwide; many agencies tout them as a highly effective "force multiplier" for catching bad guys, most notably burglars, car thieves, child molesters, kidnappers, terrorists, and—potentially—undocumented immigrants. Today, tens of thousands of LPRs are being used by law enforcement agencies all over the country—practically every week, local media around the country report on some LPR expansion. But the system&apos;s unchecked and largely unmonitored use raises significant privacy concerns. License plates, dates, times, and locations of all cars seen are kept in law enforcement databases for months or even years at a time. In the worst case, the New York State Police keeps all of its LPR data indefinitely. No universal standard governs how long data can or should be retained.',
 versiondate="2012-10-05",
 versionurl="https://web.archive.org/web/20121005031213/arstechnica.com/tech-policy/2012/09/your-car-tracked-the-rapid-rise-of-license-plate-readers/",
 anchor=" Your car, tracked: the rapid rise of license plate readers ",
 post=", WIRED, 27-Sep-2012") }}

This is the earliest article I had bookmarked about license plate readers.
The rise of these cameras had led to significant advancements in law enforcement capabilities, particularly in tracking vehicles linked to criminal activity. 
It described the effect in Tiburon, California, which was among the first towns to implement cameras that allowed police to monitor all cars entering and leaving the area. 
The American Civil Liberties Union raised questions about the lack of regulation surrounding LPR usage and data retention. 
Despite the benefits, such as recovering stolen vehicles and identifying suspects, critics highlighted issues like false positives and potential misuse of data. 
Those criticisms are still valid today as there has been no comprehensive law on the use of such cameras.


## Security Flaw in Motorola's ALPR Systems Exposes Real-Time Vehicle Data and Video Feeds Online {: #motorola}
{{ thursday_threads_quote(href="https://www.wired.com/story/license-plate-reader-live-video-data-exposed/",
 blockquote='This trove of real-time vehicle data, collected by one of Motorola’s ALPR systems, is meant to be accessible by law enforcement. However, a flaw discovered by a security researcher has exposed live video feeds and detailed records of passing vehicles, revealing the staggering scale of surveillance enabled by this widespread technology. More than 150 Motorola ALPR cameras have exposed their video feeds and leaking data in recent months, according to security researcher Matt Brown, who first publicized the issues in a series of YouTube videos after buying an ALPR camera on eBay and reverse engineering it.',
 versiondate="2025-01-07",
 versionurl="https://web.archive.org/20250107230835/https://www.wired.com/story/license-plate-reader-live-video-data-exposed/",
 anchor="License Plate Readers Are Leaking Real-Time Video Feeds and Vehicle Data",
 post=", WIRED, 7-Jan-2025") }}

This article is as much about the surveillance possible with these systems as it is about the risks of connecting misconfigured systems open to the public internet. 
It discusses a significant security flaw in automated license-plate-recognition (ALPR) systems, particularly those manufactured by Motorola, which exposured real-time video feeds and vehicle data. 
On example: in Nashville, an ALPR system captured information from nearly 1,000 vehicles in just 20 minutes. 
A security researcher discovered that ALPR cameras were put on the open internet...something it seems they weren't designed to be. 
This breach does not require any authentication, highlighting the scale of unintended surveillance enabled by these systems. 
The data collected includes photographs, license plate information, and metadata such as location and time. 
 


## Private Surveillance Network of 9 Billion License Plate Scans Enable Widespread Vehicle Tracking {: #dnr}
{{ thursday_threads_quote(href="https://www.vice.com/en/article/i-tracked-someone-with-license-plate-readers-drn/",
 blockquote='In just a few taps and clicks, the tool showed where a car had been seen throughout the U.S. A private investigator source had access to a powerful system used by their industry, repossession agents, and insurance companies. Armed with just a car’s plate number, the tool—fed by a network of private cameras spread across the country—provides users a list of all the times that car has been spotted. I gave the private investigator, who offered to demonstrate the capability, a plate of someone who consented to be tracked. It was a match. The results popped up: dozens of sightings, spanning years. The system could see photos of the car parked outside the owner’s house; the car in another state as its driver went to visit family; and the car parked in other spots in the owner’s city. Each was tagged with the time and GPS coordinates of the car. Some showed the car’s location as recently as a few weeks before. In addition to photos of the vehicle itself, the tool displayed the car’s accurate location on an easy to understand, Google Maps-style interface.',
 versiondate="2019-09-22",
 versionurl="https://web.archive.org/web/20190922032234/https://www.vice.com/en_us/article/ne879z/i-tracked-someone-with-license-plate-readers-drn",
 anchor="This Company Built a Private Surveillance Network. We Tracked Someone With It",
 post=", Vice, 17-Sep-2019") }}
 
The previous articles have talked about public sector cameras for use by police. 
This article discusses the Digital Recognition Network (DRN), a private surveillance system that allows its users to track vehicles via a vast database of license plate scans. 
The system is built from cameras installed by repo men who collect data as they drive. 
Users can access detailed information about a car's location history, including timestamps and GPS coordinates, through a user-friendly interface. 
While DRN markets itself as a tool for industries like insurance and investigations, concerns arise regarding privacy violations, as the data can be accessed by anyone who pays for it, including private investigators. 
(Last week's _Thursday Threads_ include a story about how [freelancers on Fiverr will look up anyone for a price]({filename}2025-04-10-issue-114-digital-privacy#fiverr).)
Critics argue that this system creates a digital dossier of individuals' movements, raising significant privacy issues. 
The technology is legal because it captures publicly visible information, but its widespread use has sparked debates about surveillance and civil liberties. 


## HOAs Nationwide Install Flock Safety's License Plate Readers, Facilitating Police Surveillance {: #hoa}
{{ thursday_threads_quote(href="https://theintercept.com/2023/03/22/hoa-surveillance-license-plate-police-flock/",
 blockquote='Kilgore was referring to a system consisting of eight license plate readers, installed by the private company Flock Safety, that was tracking cars on both private and public roads. Despite being in place for six months, no one had told residents that they were being watched. Kilgore himself had just recently learned of the cameras. “We find ourselves with a surveillance system,” he said, “with no information and no policies, procedures, or protections.” The deal to install the cameras had not been approved by the city government’s executive branch. Instead, the Rough Hollow Homeowners Association, a nongovernment entity, and the Lakeway police chief had signed off on the deal in January 2021, giving police access to residents’ footage. By the time of the June city council meeting, the surveillance system had notified the police department over a dozen times.',
 versiondate="2023-03-23",
 versionurl="https://web.archive.org/20230323130824/https://theintercept.com/2023/03/22/hoa-surveillance-license-plate-police-flock/",
 anchor="License Plate Surveillance, Courtesy of Your Homeowners Association",
 post=", The Intercept, 22-Mar-2023") }}

The first article in this week's _Thursday Threads_ was about Flock's law enforcement division. 
But it isn't just police installing the technology. 
This article describes the collaboration between a private homeowners association (HOA) and police departments to install license plate readers from Flock Safety. 
In Lakeway, Texas, residents were unaware of a surveillance system tracking their vehicles, installed without proper city approval—just an agreement between the HOA and the police chief with no public announcement or comment. 
Flock Safety, valued at the time at approximately $3.5 billion, marketed its cameras to over 200 HOAs nationwide, leveraging their substantial budgets and providing police access to private data. 
The article also points out incidents of wrongful detentions due to erroneous alerts and highlights the risks associated with these systems.


## AI-Powered Fusus Surveillance System Spurs Privacy Concerns as Adoption Grows in U.S. Towns and Cities {: #fusus}
{{ thursday_threads_quote(href="https://www.404media.co/fusus-ai-cameras-took-over-town-america/",
 blockquote='Spread across four computer monitors arranged in a grid, a blue and green interface shows the location of more than 50 different surveillance cameras. Ordinarily, these cameras and others like them might be disparate, their feeds only available to their respective owners: a business, a government building, a resident and their doorbell camera. But the screens, overlooking a pair of long conference tables, bring them all together at once, allowing law enforcement to tap into cameras owned by different entities around the entire town all at once. This is a demonstration of Fusus, an AI-powered system that is rapidly springing up across small town America and major cities alike. Fusus’ product not only funnels live feeds from usually siloed cameras into one central location, but also adds the ability to scan for people wearing certain clothes, carrying a particular bag, or look for a certain vehicle.',
 versiondate="2023-11-04",
 versionurl="https://web.archive.org/20231104000823/https://www.404media.co/fusus-ai-cameras-took-over-town-america/",
 anchor="AI Cameras Took Over One Small American Town. Now They're Everywhere",
 post=", 404 Media, 2-Nov-2023") }}

With the growth of camera networks (public and private), it was only a matter of time before someone tried to link them all together. 
The article explores the rapid adoption of Fusus' AI-powered surveillance system.
Fusus connects various existing security cameras into a central hub, allowing law enforcement to access multiple live feeds simultaneously. 
The technology also enhances existing surveillance systems with new capabilities like enabling the detection of specific clothing, bags, vehicles, and even transforming standard cameras into automatic license plate readers. 
While some communities have embraced Fusus for its potential to improve public safety, others have raised concerns about privacy and the implications of constant surveillance. 
The lack of transparency regarding police access to the system and its data analytics has sparked debate among residents and city councils. 
Fusus has been marketed as a solution to enhance security, but critics argue it could lead to misuse without proper oversight. 


## Artist's Traffic Cam Photobooth Sparks Controversy and Cease-and-Desist Over Creative Use of NYC Traffic Cameras {: #tcp}
{{ thursday_threads_quote(href="https://www.pcmag.com/articles/nyc-wants-you-to-stop-taking-traffic-cam-selfies-but-heres-how-to-do-it",
 blockquote='When it debuted this summer, the Traffic Cam Photobooth (TCP) website offered a new twist on the surveillance state by enabling smartphone users to take selfies with New York traffic cams. By October, it had expanded to Georgia, Maryland, Minnesota, and Ireland. TCP was recently featured in an exhibit at Miami Art Week. But the future of the interactive site is uncertain, at least in New York City, where the Department of Transportation has 900-plus traffic cams accessible through the website. Its Office of Legal Affairs recently sent a cease-and-desist letter to Morry Kolman, the artist behind the project, charging that the TCP "encourages pedestrians to violate NYC traffic rules and engage in dangerous behavior."',
 versiondate="2024-12-15",
 versionurl="https://web.archive.org/20241215055849/https://www.pcmag.com/articles/nyc-wants-you-to-stop-taking-traffic-cam-selfies-but-heres-how-to-do-it",
 anchor="NYC Wants You to Stop Taking Traffic Cam Selfies, But Here's How to Do It Anyway",
 post=", PCMag, 11-Dec-2024") }}

The {{ robustlink(href="https://trafficcamphotobooth.com/", versionurl="https://web.archive.org/web/20250310050848/https://trafficcamphotobooth.com/", versiondate="2025-04-16", title="Traffic Cam Photobooth (TCP) website", anchor="Traffic Cam Photobooth (TCP) website") }}Traffic Cam Photobooth (TCP) website, created by artist Morry Kolman, allows users to take selfies with New York City's traffic cameras.  
The NYC Department of Transportation—being spoilsports—issued a cease-and-desist letter to Kolman, claiming the site encourages unsafe behavior by pedestrians. 
In response, Kolman creatively showcased the cease-and-desist letter using a long pole to photograph it with traffic cameras across Manhattan and Brooklyn. 
Kolman views the project as a way to raise awareness about surveillance technologies and how to navigate living under such systems. 
The [source code](https://github.com/wttdotm/traffic_cam_photobooth) is even on GitHub.



## This Week I Learned: The word "scapegoat" originated in a 1530 bible translation {: #twil}
{{ thursday_threads_quote(href="https://en.wikipedia.org/wiki/Scapegoat#:~:text=Early%20English%20Christian%20Bible%20versions%20follow%20the%20translation",
 blockquote='Early English Christian Bible versions follow the translation of the Septuagint and Latin Vulgate, which interpret azazel as "the goat that departs" (Greek tragos apopompaios, "goat sent out", Latin caper emissarius, "emissary goat"). William Tyndale rendered the Latin as "(e)scape goat" in his 1530 Bible. This translation was followed by subsequent versions up through the King James Version of the Bible in 1611: "And Aaron shall cast lots upon the two goats; one lot for the Lord, and the other lot for the scapegoat."',
 versiondate="2025-03-14",
 versionurl="https://en.wikipedia.org/w/index.php?title=Scapegoat&oldid=1280391718",
 anchor="Scapegoat",
 post=", Wikipedia") }}

{{ image(width="300", localsrc="2025/2025-04-17-scapegoat.png", alt='A close-up of a goat with light brown fur and curved horns is shown next to text. The text reads: "In ancient Syria, the Kingdom of Ebla sends livestock into the desert to symbolically carry away evil. They’re among the first known scapegoats." In the bottom right corner, it says "4 Points."') }} 
Have you stared at a word and suddenly wondered about its origins? 
This entry from the {{ robustlink(href="https://www.nytimes.com/interactive/2025/03/28/upshot/flashback.html", versionurl="https://web.archive.org/web/20250417020656/https://www.nytimes.com/interactive/2025/03/28/upshot/flashback.html", versiondate="2025-04-16", title="Flashback: Your Weekly History Quiz,
March 29, 2025 | New York Times", anchor="New York Times Flashback Quiz") }} had me wondering about "scapegoat". 
"scape" — "goat". 
Why do we say that? 
It comes from a phrase in the bible where a goat sent into the wilderness on the Day of Atonement as a symbolic bearer of the sins of the people — Leviticus 16:22, to be exact. 
The translator coined the term from the interpretation of "the goat that departs" and "emissary goat" in that verse.

What did you learn this week? Let me know on [Mastodon](https://code4lib.social/@dltj/) or [Bluesky](https://bsky.app/profile/dltj.org/).


## Alan Basks in the Window {: #cats}
{{ image(width="600", localsrc="2025/2025-04-17-alan.jpg", alt="A black and white cat lounges on a soft blanket on a windowsill, surrounded by potted green plants. Behind the cat, a view of a street and trees can be seen. Sunlight filters through the window, creating a serene and cozy atmosphere. The cat is looking at the photographer, as if awaken from a nap.") }} 

