---
title: 'Issue 117: Local Government Surveillance'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- government surveillance
- law enforcement
summary: "Thursday Threads this week delves into the rise of surveillance tech used by law enforcement, covering topics like Fog Reveal's phone tracking without warrants, suits against Whitepages for exposing officer info, and NYPD's deals with surveillance firms. It also discusses ICE's informal access to local license plate data and the growth of Real-Time Crime Centers. These issues underscore significant privacy concerns and highlight the urgent need for regulatory oversight to safeguard civil liberties."
bluesky: "Thursday Threads this week highlights law enforcement's expanding surveillance use, sparking privacy concerns. It covers phone tracking, data exposure lawsuits, and controversial contracts, emphasizing the urgent need for oversight and regulation."
---
After previous _DTLJ Thursday Threads_ issues on [digital privacy]({filename}2025-04-10-issue-114-digital-privacy), [surveillance camera systems]({filename}2025-04-17-issue-115-camera-networks.md), and [federal government systems]({filename}2025-05-29-issue-116-government-surveillance.md), I'm focusing this week on what is happening at the local level—mainly in policing. 
This closes this loop on surveillance by coming back around to local activity — although it takes an unexpected jump back to the national level with a story published last month.
Law enforcement surveillance has dramatically evolved, influenced by cutting-edge technology and controversial practices. 
This thread of stories highlights the complexities and ethical challenges arising from deploying these advancements. 
From the sophisticated smartphone tracking tools like Fog Reveal to the spidering data collection activities of Flock's AI-powered license plate readers, these stories underscore the growing tensions between public safety objectives and personal privacy rights.
So that is the focus of this week's _Thursday Threads_ issue:

- In 2022, we learned of a [local police surveillance called Fog Reveal]({filename}#fog-reveal-1) that pinpointed mobile phones and de-anonymized users.
- Two years later, [they were still at it]({filename}#fog-reveal-2)—this time asking police to augment Fog Reveal's data to include information about doctor visits. (2024)
- NYPD has [multi-million dollar contracts with controversial surveillance firms]({filename}#nypd) that scrape social media and post fake users to get surveillance engagement. (2023)
- Advances in surveillance technology mean we've seen the unchecked growth of [Real-Time Crime Centers]({filename}#rtcc) across America. (2023)
- Police and other public officials have special protections from data brokers, and [West Virginia officers sue Whitepages]({filename}#wv) over unlawful info disclosure. (2024) 
- Here's the recent national twist on local law enforcement surveillance: [ICE's covert use of Flock's AI camera network]({filename}#ice) for immigration enforcement. (2025)
- [This Week I Learned]({filename}#twil): Ammonium chloride may be the 6th basic taste 

Before we start...it is important to call out what is happening in the United States. 
The Trump administration is using modern-day authoritarian tactics to frighten citizens into accepting a new normal. 
I am more angry at what my national leaders have done than I am frightened, and I hope you will express your outrage, too, at a {{ robustlink(href="https://www.nokings.org/", versionurl="https://web.archive.org/web/20250611012930/https://www.nokings.org/", versiondate="2025-06-11", title="No Kings homepage", anchor="No Kings in America protest this weekend") }}.
These are drafts of the two signs I'll be waving:

{{ image(width="300", div_float="left", localsrc="2025/2025-06-12-three-branches-sign.png", alt="The protest sign emphasizes the roles of the three government branches with phrases: 'Legislative: Investigate!' and 'Executive: Follow the Law!' and 'Judicial: Defend the Bench!' in blue and red lettering. Below, 'Three Co-Equal Branches' is displayed in a mix of blue and red. The background features alternating gray and white stripes, reinforcing the message of balance and cooperation among the branches.") }} 
{{ image(width="300", div_float="left", localsrc="2025/2025-06-12-respect-my-authoritah-sign.png", alt="The protest sign features a cartoon character with the body of Eric Cartman from South Park, dressed in a police uniform, and a face resembling Donald Trump. The character is angrily shouting. Next to the character, the text reads 'RESPECT MY AUTHORITAH!' in bold teal letters. Below, in stylized orange and yellow text, it states 'No Kings in America.' The design humorously critiques authority, blending pop culture with a political message.") }} 

In light of Elon Musk stepping back from a public role in the administration, I'll retitle my [#TeslaTakedown protest sign blog post]({filename}2025-04-11-tesla-takedown-protest-signs) (although, in keeping with cool-URLs-don't-change practice, it is at the same web link) and will be adding these two signs when they are finalized. 
You are welcome to visit that post to download printable versions of these signs or any other ones that I've made. 

{{ thursday_threads_header() }}


## A Deep Dive into Local Police Surveillance Practices Using Fog Reveal {: #fog-reveal-1}
{{ thursday_threads_quote(href="https://www.vice.com/en/article/v7v34a/fog-reveal-local-cops-phone-location-data-manual",
 blockquote='Users can then “tag” a device to mark it as a device of interest, the manual says. From there, they can “query” that particular device and the system will show a 90 day pattern of activity for that device. Some police departments like how quickly they can access this data, according to the Associated Press. Ordinarily, Google might provide information on what devices were present in a particular area at a specific time, but authorities would need to obtain a so-called “reverse location warrant,” which can take time. With Fog Reveal, they can just log in. The Associated Press spoke to a prosecutor in Washington County, Arkansas, who told the outlet that he had used Fog Reveal without a warrant in the past, especially in “exigent circumstances.”',
 versiondate="2022-09-04",
 versionurl="https://web.archive.org/20220904005539/https://www.vice.com/en/article/v7v34a/fog-reveal-local-cops-phone-location-data-manual",
 anchor="Here Is the Manual for the Mass Surveillance Tool Cops Use to Track Phones",
 post=", Motherboard: Tech by Vice, 1-Sep-2022") }}

The article discusses the user manual for Fog Reveal, a mass surveillance tool employed by local police departments in the U.S. to track individuals' phones without warrants. 
A staff technologist at the EFF shared the manual with the article author and {{ robustlink(href="https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police", versionurl="https://web.archive.org/20220904005542/https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police", versiondate="2022-09-04", title="Inside Fog Data Science, the Secretive Company Selling Mass Surveillance to Local Police | Electronic Frontier Foundation", anchor="provided insights about the tool that were found in public record requests") }}.
This technology utilizes data harvested from smartphone apps, allowing law enforcement to access location information quickly and easily. 
The manual reveals that users can search for devices in specific areas using geofencing and tag devices of interest to analyze their activity patterns over 90 days. 
Despite its effectiveness in various investigations, prosecutors rarely disclose the tool's use in court filings, raising concerns about accountability and public awareness. 
The manual emphasizes the sensitivity of the data accessed and notes that surveillance can encompass large numbers of people, potentially overwhelming users with data. 
It highlights the ease of use for law enforcement, who can bypass traditional warrant processes in urgent situations. 
Additionally, the article mentions that Fog Reveal has clients across various jurisdictions, from urban to rural areas.


## How Fog Data Science Enables Police Surveillance on Doctor Visits {: #fog-reveal-2}
{{ thursday_threads_quote(href="https://www.404media.co/location-data-firm-offers-to-help-cops-track-targets-via-doctor-visits/",
 blockquote='The document is a “Project Intake Form” that asks police for information about the person of interest they would like to track, such as biographical information and known locations, including family and friends&apos; addresses and doctors offices they may visit. It shows that, in a time when surveillance of abortion and reproductive health clinics could rise in a post-Roe America, companies providing monitoring tools to the government are prepared to use healthcare information to track down targets.',
 versiondate="2024-12-11",
 versionurl="https://web.archive.org/20241211000842/https://www.404media.co/location-data-firm-offers-to-help-cops-track-targets-via-doctor-visits/",
 anchor="Location Data Firm Offers to Help Cops Track Targets via Doctor Visits",
 post=", 404 Media, 10-Dec-2024") }}

Two years after the above article was published, Fog Data Science was in the news again...still offering services to law enforcement that involve tracking individuals. 
A document obtained by 404 Media reveals that the company seeks specific information from police, including the addresses of doctors and biographical details about persons of interest. 
Fog Data Science uses location data sourced from smartphones through apps and their advertising networks to pinpoint targets. 
The Project Intake Form provided to law enforcement emphasizes the need for detailed information to enhance tracking efficiency. 
It specifically asks for data such as names, aliases, and any links to criminal activity. 
The more data that is in the database, the easier it is to de-anonymize the mobile phone traces.


## NYPD's Multi-Million Dollar Contracts with Controversial Surveillance Firms Raise Privacy Concerns {: #nypd}
{{ thursday_threads_quote(href="https://www.theguardian.com/us-news/2023/sep/08/new-york-police-tracking-voyager-labs-meta-contract",
 blockquote='New York law enforcement agencies have spent millions of dollars to expand their capabilities to track and analyze social media posts, new documents show, including by contracting with a surveillance firm accused of improperly scraping social media platforms for data. Documents obtained by the Surveillance Technology Oversight Project (Stop), a privacy advocacy non-profit and shared with the Guardian, reveal the New York police department in 2018 entered a nearly $9m contract with Voyager Labs, a surveillance company that has been sued by Meta for allegedly using nearly 40,000 fake Facebook accounts to collect data on an estimated 600,000 users.',
 versiondate="2023-09-15",
 versionurl="https://web.archive.org/20230915020840/https://www.theguardian.com/us-news/2023/sep/08/new-york-police-tracking-voyager-labs-meta-contract",
 anchor="NYPD spent millions to contract with firm banned by Meta for fake profiles",
 post=", The Guardian, 8-Sep-2023") }}

The New York Police Department (NYPD) spent millions on a contract with Voyager Labs, a surveillance firm banned by Meta for using fake profiles to scrape social media data. 
Voyager Labs claims its tools can analyze online behavior using artificial intelligence to detect and predict crimes. 
The NYPD's contract allows them to create avatars for data collection.
Of course, the use of such surveillance tools raises ethical and legal concerns, particularly regarding privacy and the collection of personal information without proper warrants. 
While the NYPD stated it uses these tools for public safety and investigative purposes, it did not provide specific details on how they were used. 


## The Unchecked Growth of Real-Time Crime Centers Across America {: #rtcc}
{{ thursday_threads_quote(href="https://www.wired.com/story/real-time-crime-centers-rtcc-us-police/",
 blockquote='Most evidence for [Real-Time Crime Centers (RTCCs)] effectiveness, however, is anecdotal, and there is a real lack of studies into how effective they really are. In Detroit, a National Institute of Justice study concluded that Project Green Light—a part of the Detroit Police Department RTCC that established cameras at more than 550 locations, including schools, churches, private businesses, and health centers—helped decrease property violence in some areas but did nothing to prevent violent and other crimes. But police departments argue they do work.',
 versiondate="2023-07-12",
 versionurl="https://web.archive.org/20230712020934/https://www.wired.com/story/real-time-crime-centers-rtcc-us-police/",
 anchor="The Quiet Rise of Real-Time Crime Centers",
 post=", WIRED, 10-Jul-2023") }}

Originating from concepts like London's "Ring of Steel" in response to Irish Republican Army bombings in the 1990s, the first RTCC was created in New York City in 2005. 
These centers aim to enhance policing efficiency by collecting data from various sources, including CCTV, drones, and social media, often employing facial recognition and predictive policing methods. 
Proponents argue that RTCCs allow for more targeted policing and reduce crime rates. Critics raise concerns about privacy violations and the potential for abuse of surveillance data. 
The lack of public awareness and oversight enables these centers to operate with minimal scrutiny, leading to fears of mass data collection impacting citizens' rights. 
You also have to wonder about the security of this gathered data with the rice of ransomware operations. 
The Electronic Frontier Foundation and others advocate for stricter regulations and community control over surveillance technologies to protect civil liberties. 

Curious about what police-run surveillance products are used in your hometown? 
Check out {{ robustlink(href="https://atlasofsurveillance.org/", versionurl="https://web.archive.org/web/20250612012455/https://atlasofsurveillance.org/", versiondate="2025-06-11", title="Atlas of Surveillance: Documenting Police Tech in Our Communities with Open Source Research", anchor="EFF's Atlas of Surveillance") }}.



## West Virginia Officers Sue Whitepages Over Unlawful Info Disclosure {: #wv}
{{ thursday_threads_quote(href="https://therecord.media/west-virginia-law-enforcement-sues-broker",
 blockquote='Whitepages is the latest data broker to be sued for allegedly flouting laws barring the publication of home addresses and other personal information belonging to judges, police officers, prosecutors and others in law enforcement. A retired West Virginia police officer filed a class action lawsuit against the company late last month for publishing his home address, a violation of a 2021 West Virginia statute known as Daniel’s Law. The West Virginia law is similar to legislation enacted in New Jersey in 2020 following the murder of a federal judge’s son by a disgruntled lawyer who had appeared before her and found her personal information online. That law, also called Daniel’s Law, was enacted following an emotional appeal for reform from U.S. District Court Judge Esther Salas, whose son was killed. In 2022, Congress passed a more limited federal version of the laws, barring the selling or purchasing of judges’ private information online.',
 versiondate="2024-09-11",
 versionurl="https://web.archive.org/20240911021008/https://therecord.media/west-virginia-law-enforcement-sues-broker",
 anchor="West Virginia law enforcement sues data broker for publishing personal information online",
 post=", The Record, 6-Sep-2024") }}

Laws have been enacted at the state and federal levels to protect the privacy of judges, law enforcement, and other public-facing professions following incidents where personal information was used to target them. 
This type of legislation is spreading, and there are calls for it to be expanded to protect other public officials like public health workers and school board members. 
One has to wonder when the increasing demand for average citizens to have similar legal protections against data brokers will pick up steam.


## ICE's Covert Use of AI Camera Network for Immigration Enforcement Through Local Police {: #ice}
{{ thursday_threads_quote(href="https://www.404media.co/ice-taps-into-nationwide-ai-enabled-camera-network-data-shows/",
 blockquote='Data from a license plate-scanning tool that is primarily marketed as a surveillance solution for small towns to combat crimes like car jackings or finding missing people is being used by ICE, according to data reviewed by 404 Media. Local police around the country are performing lookups in Flock’s AI-powered automatic license plate reader (ALPR) system for “immigration” related searches and as part of other ICE investigations, giving federal law enforcement side-door access to a tool that it currently does not have a formal contract for.',
 versiondate="2025-05-28",
 versionurl="https://web.archive.org/20250528130845/https://www.404media.co/ice-taps-into-nationwide-ai-enabled-camera-network-data-shows/",
 anchor="ICE Taps into Nationwide AI-Enabled Camera Network, Data Shows",
 post=", 404 Media") }}

[Issue 115 on surveillance camera systems]({filename}2025-04-17-issue-115-camera-networks.md) had several articles about law enforcement using services from Flock for investigating local crime with the ability to search for cars nationwide.
Now we learn that ICE is asking local police departments to use Flock's automatic license plate reader (ALPR) system for immigration-related purposes, granting ICE access to data without a formal contract or oversight. 
The data indicates that local police must provide justification for their lookups, with many citing immigration or ICE-related reasons. 
Notably, searches mentioning ICE occurred during both the Biden and Trump administrations, but all explicit immigration-related lookups happened after Trump's inauguration. 


## This Week I Learned: Ammonium chloride may be the 6th basic taste {: #twil}
{{ thursday_threads_quote(href="https://web.archive.org/web/20250404201019/https://bigthink.com/health/ammonium-chloride-sixth-basic-taste/",
 blockquote='Ammonium chloride is a slightly toxic chemical most notably found in “salmiak,” a salt licorice candy, which is popular in northern Europe. In a new study, researchers found that the compound triggers a specific proton channel called OTOP1 in sour taste receptor cells, which fulfills one of the key requirements to be considered a primary taste like sweet, salty, sour, bitter, and umami. Ammonium is commonly found in waste products and decaying organic matter and is slightly toxic, so it makes sense that vertebrates evolved a specific taste sensor to recognize it.',
 versiondate="2025-04-25",
 versionurl="https://web.archive.org/web/20250404201019/https://bigthink.com/health/ammonium-chloride-sixth-basic-taste/",
 anchor="Ammonium chloride tastes like nothing else. It may be the sixth basic taste",
 post=", Big Think, 11-Oct-2023") }}

What did you learn this week? Let me know on [Mastodon](https://code4lib.social/@dltj/) or [Bluesky](https://bsky.app/profile/dltj.org/).


## Another season of outdoor cat activity begins, part 2 {: #cats}
{{ image(width="600", localsrc="2025/2025-06-12-mittens.jpg", alt="Black cat wearing a red harness and leash exploring outdoors, nibbling on grass blades in a lush green lawn with shrubs in the background.") }} 
It has finally gotten warm enough to be outside during the workday, and we are taking full advantage of it.
