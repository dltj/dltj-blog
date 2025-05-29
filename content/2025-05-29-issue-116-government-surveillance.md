---
title: 'Issue 116: Government Surveillance'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- government surveillance
- digital privacy
- location privacy
summary: "U.S. surveillance is escalating: Trump’s order to scrap inter-agency data silos and Musk’s DOGE unite federal databases; Oracle’s Ellison envisions AI cameras and drones; the Pentagon’s Locomotive tracks phones via app data; and brokers sell personal records to law enforcement. As LexisNexis lobbied for hands-off regulation and Apple battled over data access, pressing issues of oversight, due process, and privacy are emerging."
bluesky: "US surveillance is surging: Trump unites agency data; Musk’s DOGE centralizes federal databases; Ellison backs AI cameras and drones; the Pentagon tracks phones via “Locomotive”; data brokers sell personal records—raising urgent privacy and oversight concerns."
---
After _DTLJ Thursday Threads_  issues on [digital privacy]({filename}2025-04-10-issue-114-digital-privacy) and [surveillance camera systems]({filename}2025-04-17-issue-115-camera-networks), I'm focusing this week on the more general topic of government-sponsored or -enabled surveillance. 
In an era defined by ubiquitous data collection and ever-advancing technologies, the line between public safety and individual privacy is growing alarmingly thin. 
From President Trump’s executive order to dismantle inter-agency “data silos” and Elon Musk’s DOGE initiative weaving federal databases together, to Oracle co-founder Larry Ellison’s vision of AI-powered cameras and drones monitoring citizens, the U.S. surveillance apparatus is expanding at breakneck speed. 
Meanwhile, programs like the Pentagon’s “Locomotive”—which turns innocuous dating-app location pings into real-time tracking tools—and the data broker–driven sharing of driving and personal records with law enforcement underscore how private and public interests have converged to create a modern panopticon.
So that is the focus of this week's _Thursday Threads_ issue:

- Trump’s executive order dismantling government data silos and Musk-led DOGE initiative fuel [fears of a U.S. surveillance state]({filename}#panopticon).
- More details about how [DOGE is building an Immigrant Surveillance Database]({filename}#doge) with Social Security and IRS Data.
- In cases where the government doesn't already have the data, [spy agencies want to centralize commercial data purchases]({filename}#cai) in a new one-stop portal.
- 1984 is here and some people want it: [Oracle’s Larry Ellison]({filename}#ellison) proposes Orwellian AI camera-and-drone surveillance network, stoking privacy fears.
- LexisNexis parent Relx [lobbies against data broker restrictions]({filename}#lexisnexis) amid FISA Section 702 reauthorization clash.
- Dating app location data powers [Pentagon’s “Locomotive” program]({filename}#pentagon) to track phones worldwide
- [Apple sues U.K. government]({filename}#apple) over a secret order for backdoor access to encrypted data on phones, and it removes the Advanced Data Protection from U.K. market rather than giving in.
- [This Week I Learned]({filename}#twil): "Leeroy Jenkins!!!!" was staged



{{ thursday_threads_header() }}


## Trump’s Executive Order and Musk-Led DOGE Initiative Fuel Fears of a U.S. Surveillance State {: #panopticon}

{{ thursday_threads_quote(href="https://www.theatlantic.com/technology/archive/2025/04/american-panopticon/682616/",
 blockquote='In March, President Trump issued an executive order aiming to eliminate the data silos that keep everything separate. Historically, much of the data collected by the government had been heavily compartmentalized and secured; even for those legally authorized to see sensitive data, requesting access for use by another government agency is typically a painful process that requires justifying what you need, why you need it, and proving that it is used for those purposes only. Not so under Trump. This is a perilous moment. Rapid technological advances over the past two decades have made data shedding ubiquitous—whether it comes from the devices everyone carries or the platforms we use to communicate with the world. As a society, we produce unfathomable quantities of information, and that information is easier to collect than ever before.',
 versiondate="2025-04-28",
 versionurl="https://web.archive.org/20250428191603/https://www.theatlantic.com/technology/archive/2025/04/american-panopticon/682616/",
 anchor="American Panopticon",
 post=", The Atlantic, 27-Apr-2025") }}
 
This article examines the growing surveillance capabilities of the U.S. federal government under the Trump administration, particularly through the actions of Elon Musk's DOGE. 
It highlights how various government agencies are pooling vast amounts of data on citizens, which raises concerns about privacy and potential abuses of power. 
The effort starts with an executive order from Trump to eliminate data silos, allowing for easier access and sharing of sensitive information across agencies. 
That is followed up by the web of DOGE-placed staff in various government departments that are weaving the silos together.
Experts warn that this could lead to a surveillance state where personal data is weaponized for political purposes, targeting individuals based on their attributes or actions. 
Hence the title of the article: the American {{ robustlink(href="https://ethics.org.au/ethics-explainer-panopticon-what-is-the-panopticon-effect/", versionurl="https://web.archive.org/web/20250421233421/ethics.org.au/ethics-explainer-panopticon-what-is-the-panopticon-effect/", versiondate="2025-04-27", title="Ethics Explainer: The Panopticon | The Ethics Centre", anchor="Panopticon") }}:

> The panopticon is a disciplinary concept brought to life in the form of a central observation tower placed within a circle of prison cells. From the tower, a guard can see every cell and inmate but the inmates can’t see into the tower. Prisoners will never know whether or not they are being watched.
 

## DOGE Builds DHS Immigrant Surveillance Database with SSA, IRS Data {: #doge}

{{ thursday_threads_quote(href="https://www.wired.com/story/doge-collecting-immigrant-data-surveil-track/",
 blockquote='Operatives from Elon Musk’s so-called Department of Government Efficiency (DOGE) are building a master database at the Department of Homeland Security (DHS) that could track and surveil undocumented immigrants, two sources with direct knowledge tell WIRED. DOGE is knitting together immigration databases from across DHS and uploading data from outside agencies including the Social Security Administration (SSA), as well as voting records, sources say. This, experts tell WIRED, could create a system that could later be searched to identify and surveil immigrants.',
 versiondate="2025-04-19",
 versionurl="https://web.archive.org/web/20250419143655/https://www.wired.com/story/doge-collecting-immigrant-data-surveil-track/",
 anchor="DOGE Is Building a Master Database to Surveil and Track Immigrants",
 post=", WIRED, 18-Apr-2025") }}

This article can be paired with the one above...this one has more details about what DOGE itself is doing.
Under the guise of surveilling and tracking undocumented immigrants, this comprehensive database at the Department of Homeland Security (DHS) is integrating data from various agencies, including the Department of Homeland Security, Social Security Administration, and the IRS. 
They are also reportedly adding other data sources, including biometric information and voting records.
This initiative raises significant privacy concerns, as it may lead to unprecedented surveillance capabilities; although starting with immigrants, what is being built enables real-time tracking of everyone. 
Experts are warning that such data consolidation can increase the risk of misuse and violate privacy rights.


## Spy Agencies to Centralize Commercial Data Purchases in a New One-Stop Portal {: #cai}

{{ thursday_threads_quote(href="https://theintercept.com/2025/05/22/intel-agencies-buying-data-portal-privacy/",
 blockquote='The ever-growing market for personal data has been a boon for American spy agencies. The U.S. intelligence community is now buying up vast volumes of sensitive information that would have previously required a court order, essentially bypassing the Fourth Amendment. But the surveillance state has encountered a problem: There’s simply too much data on sale from too many corporations and brokers. So the government has a plan for a one-stop shop. The Office of the Director of National Intelligence is working on a system to centralize and “streamline” the use of commercially available information, or CAI, like location data derived from mobile ads, by American spy agencies, according to contract documents reviewed by The Intercept.',
 versiondate="2025-05-23",
 versionurl="https://web.archive.org/20250523140839/https://theintercept.com/2025/05/22/intel-agencies-buying-data-portal-privacy/",
 anchor="U.S. Spy Agencies Are Getting a One-Stop Shop to Buy Your Most Sensitive Personal Data",
 post=", The Intercept, 22-May-2025") }}
 
Based on the previous two articles, we learned that the U.S. government is breaking down its data silos and gathering all of its information into a large central pool. 
But that isn't nearly everything that can be known about us. 
Now the U.S. intelligence community is developing a centralized system, the Intelligence Community Data Consortium (ICDC), to streamline the acquisition of commercially available information, including sensitive personal data. 
This initiative aims to address the overwhelming volume of data available from various corporations and brokers, allowing agencies to bypass traditional legal requirements for obtaining such information. 
The ICDC will provide a web-based platform for 18 federal agencies to efficiently purchase access to sensitive data, potentially undermining privacy protections.
Critics express concern that this approach could lead to misuse of sensitive information, as agencies may continue to operate under a "just grab all of it" mentality without sufficient oversight.  
 

## Oracle’s Larry Ellison Proposes Orwellian AI Camera-and-Drone Surveillance Network, Stoking Privacy Fears {: #ellison}

{{ thursday_threads_quote(href="https://arstechnica.com/information-technology/2024/09/omnipresent-ai-cameras-will-ensure-good-behavior-says-larry-ellison/",
 blockquote='Oracle co-founder Larry Ellison shared his vision for an AI-powered surveillance future during a company financial meeting, reports Business Insider. During an investor Q&A, Ellison described a world where artificial intelligence systems would constantly monitor citizens through an extensive network of cameras and drones, stating this would ensure both police and citizens don&apos;t break the law.',
 versiondate="2024-09-17",
 versionurl="https://web.archive.org/20240917061204/https://arstechnica.com/information-technology/2024/09/omnipresent-ai-cameras-will-ensure-good-behavior-says-larry-ellison/",
 anchor="Omnipresent AI cameras will ensure good behavior, says Larry Ellison",
 post=", Ars Technica, 16-Sep-2024") }}

In case you haven't been following along, the dystopian world depicted in George Orwell's 1984 is now quite possible. 
Some even seem to desire it. 
Ellison envisions a future where AI-powered surveillance systems constantly monitor us through a network of cameras and drones. 
Similar automated surveillance systems are already being deployed in places like China, leading to what some call a "road to digital totalitarianism." 

No, thank you.


## LexisNexis Parent Relx Lobbies Amid FISA Section 702 Reauthorization Clash Over Warrant Requirement for Data Brokers {: #lexisnexis}
{{ thursday_threads_quote(href="https://www.theverge.com/2024/4/5/24122079/data-brokers-fisa-extension-nsa-section-702-surveillance-lexis-nexis",
 blockquote='Lawmakers’ negotiations over FISA’s reauthorization became so contentious that House Speaker Mike Johnson withdrew the bill from consideration in February. The biggest source of conflict was an amendment introduced by Rep. Warren Davidson (R-OH) that would prohibit data brokers from selling consumer data to law enforcement and would require a warrant to access Americans’ information, Politico’s Influence newsletter reported in February.',
 versiondate="2024-04-06",
 versionurl="https://web.archive.org/20240407045850/https://www.theverge.com/2024/4/5/24122079/data-brokers-fisa-extension-nsa-section-702-surveillance-lexis-nexis",
 anchor="Data brokers are gearing up to fight privacy bills",
 post=", The Verge, 5-Apr-2025") }}

Section 702 of the Foreign Intelligence Surveillance Act (FISA) is a program that allows the U.S. federal government to conduct targeted surveillance of people outside the U.S. 
Not only is this invading the privacy of non-U.S. citizens, but data about U.S. citizens is also swept into the database. 
LexisNexis became involved in the ongoing debate over privacy and data broker regulations as Congress considered reauthorizing Section 702 last year. 
The company has faced scrutiny for its data collection practices, particularly its partnerships with automakers to sell driving data to insurance companies. 
Needless to say, it wants a part of the government spending on the Section 702 program. 
Former President Biden {{ robustlink(href="https://www.npr.org/2024/04/20/1246076114/senate-passes-reauthorization-surveillance-program-fisa", versionurl="https://web.archive.org/web/20250401185048/https://www.npr.org/2024/04/20/1246076114/senate-passes-reauthorization-surveillance-program-fisa", versiondate="2025-04-01", title="Biden signs reauthorization of surveillance program into law despite privacy concerns | NPR", anchor="signed a two year extension of FISA") }} last April.


## Dating App Location Data Powers Pentagon’s “Locomotive” Program to Track Phones Worldwide {: #pentagon}

{{ thursday_threads_quote(href="https://www.wired.com/story/how-pentagon-learned-targeted-ads-to-find-targets-and-vladimir-putin/",
 blockquote='Working with Grindr data, Yeagley began drawing geofences—creating virtual boundaries in geographical data sets—around buildings belonging to government agencies that do national security work. That allowed Yeagley to see what phones were in certain buildings at certain times, and where they went afterwards. He was looking for phones belonging to Grindr users who spent their daytime hours at government office buildings. If the device spent most workdays at the Pentagon, the FBI headquarters, or the National Geospatial-Intelligence Agency building at Fort Belvoir, for example, there was a good chance its owner worked for one of those agencies. Then he started looking at the movement of those phones through the Grindr data. When they weren’t at their offices, where did they go? A small number of them had lingered at highway rest stops in the DC area at the same time and in proximity to other Grindr users—sometimes during the workday and sometimes while in transit between government facilities. For other Grindr users, he could infer where they lived, see where they traveled, even guess at whom they were dating.',
 versiondate="2024-03-01",
 versionurl="https://web.archive.org/20240301001129/https://www.wired.com/story/how-pentagon-learned-targeted-ads-to-find-targets-and-vladimir-putin/",
 anchor="How the Pentagon Learned to Use Targeted Ads to Find Its Targets—and Vladimir Putin",
 post=", WIRED, 27-Feb-2024") }}

Location data collected from mobile apps is bought and sold by data brokers, and that data is increasingly used by government agencies for surveillance purposes. 
It describes how a man named Mike Yeagley demonstrated to the Pentagon how precisely one could track the movements of government employees through a dating app. 
This led to the creation of a program called Locomotive that could track the location of phones globally in near real-time...including that of world leaders like Vladimir Putin. 
Having that device in our pocket know precisely where it is—and, by extension, where we are—is a very useful tool, but it fuels unprecedented and covert surveillance abilities.


## Apple Sues UK Government Over Secret Order for Backdoor Access to Encrypted Data, Removes Advanced Data Protection from UK Market {: #apple}
{{ thursday_threads_quote(href="https://www.bbc.com/news/articles/c8rkpv50x01o",
 blockquote='Apple is taking legal action to try to overturn a demand made by the UK government to view its customers&apos; private data if required. The BBC understands that the US technology giant has appealed to the Investigatory Powers Tribunal, an independent court with the power to investigate claims against the Security Service.... In January, Apple was issued with a secret order by the Home Office to share encrypted data belonging to Apple users around the world with UK law enforcement in the event of a potential national security threat.',
 versiondate="2025-03-11",
 versionurl="https://web.archive.org/20250311020907/https://www.bbc.com/news/articles/c8rkpv50x01o",
 anchor="Apple takes legal action in UK data privacy row",
 post=", BBC News, 4-Mar-2025") }}
 
Apple is pursuing legal action against the UK government over a demand to access its customers' private data. 
The company appealed to the Investigatory Powers Tribunal after receiving a secret order that requires Apple to share encrypted data with UK law enforcement in cases of national security threats. 
While Apple can still access data protected by its standard encryption with a warrant, its Advanced Data Protection (ADP) feature, which offers stronger privacy, cannot be accessed even by Apple itself. 
In response to the UK order, Apple has removed ADP from the UK market rather than create a "backdoor" for access. 
The situation has sparked tension between Apple and the UK government, with the US administration expressing concern over the UK's actions. 
The Home Office maintains that privacy is only compromised in exceptional cases related to serious crimes. 


## This Week I Learned: "Leeroy Jenkins!!!!" was staged {: #twil}
{{ thursday_threads_quote(href="https://kotaku.com/the-makers-of-leeroy-jenkins-didnt-think-anyone-would-b-1821570730",
 blockquote='It was one of the first memes ever, a viral sensation that went mainstream back when people still used dial-up internet. Yet the cameraman behind “Leeroy Jenkins” still seems stupefied that anyone fell for it.',
 versiondate="2025-04-28",
 versionurl="https://web.archive.org/web/20250429022100/https://kotaku.com/the-makers-of-leeroy-jenkins-didnt-think-anyone-would-b-1821570730",
 anchor="The Makers Of 'Leeroy Jenkins' Didn't Think Anyone Would Believe It Was Real",
 post=", Kotaku, 25-Dec-2017") }}

First posted on May 10, 2005, this month marks the 20th anniversary of {{ robustlink(href="https://www.youtube.com/watch?v=hooKVstzbz0", versionurl="https://web.archive.org/web/20250430025207/", versiondate="2025-04-30", title="Leeroy Jenkins HD | YouTube", anchor="this bit of internet folklore") }}. 
I remember when this first came out, and I totally believed it was real until earlier this year.


What did you learn this week? Let me know on [Mastodon](https://code4lib.social/@dltj/114591093966405498) or [Bluesky](https://bsky.app/profile/dltj.org/post/3lqcpmmgdep2q).


## Another season of outdoor cat activity begins {: #cats}
{{ image(width="600", localsrc="2025/2025-05-29-alan.jpg", alt="White and gray cat with purple collar sitting attentively in a mulched garden bed, surrounded by green lawn and suburban homes in the background. In front of the cat is the dead remnants of last year's catnip patch with new green sprouts shooting up.") }} 

