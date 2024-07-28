---
title: 'OCLC v. Clarivate: What was MetaDoor? What is an OCLC Record?'
modified: 2022-11-13T21:38:47-05:00
category: Raw Technology
categories:
- Raw Technology
tags:
- OCLC
- Clarivate
- WorldCat record use policy
- MARC record reuse
---
On November 7, 2022, OCLC and Clarivate announced a settlement in their lawsuit about using WorldCat records in the embryonic MetaDoor service.
This ended the latest chapter in the saga of reuse of library metadata with little new clarity.
The settlement terms were not disclosed, but we can learn a little from the proceedings.
First, let's review the press releases from the parties.
Then we'll look at the transcripts of court proceedings to see if we can get closer to answers about some questions this lawsuit raises.

## Clarivate's Statement
{: #clarivate-statement}

Clarivate's statement about the settlement is quite vague:

> Clarivate continues to deny OCLCs allegations of wrong-doing and maintains that the issue lay between OCLC and its customers, who sought to co-create an efficient community platform for sharing of bibliographic records. Clarivate will not develop a record exchange system of MARC records that include records which OCLC has claimed are subject to its policy and contractual limitations. Clarivate will bear its own fees and costs.
>
> Gordon Samson, Chief Product Officer at Clarivate insisted, "Clarivate will continue to support the goals of open research and data exchange - because we believe it is the best way to make the process of research and learning faster, more robust and more transparent. Regardless of business model, when scholarly information is easily accessible and shareable, the dots are easier to join, the connections are explicit, and collaborations are more natural and meaningful. The process of scientific discovery is faster, and it is easier to ensure research integrity and reproducibility. We know that navigating the transition to open research is important to our customers, and we remain committed to helping them make that transition as seamlessly as possible."
>
> _- "{{ robustlink(href="https://ir.clarivate.com/news-events/press-releases/news-details/2022/Clarivate-and-OCLC-Settle-Lawsuit/default.aspx", versionurl="https://web.archive.org/web/20221112042848/https://ir.clarivate.com/news-events/press-releases/news-details/2022/Clarivate-and-OCLC-Settle-Lawsuit/default.aspx", versiondate="2022-11-11", title="Clarivate and OCLC Settle Lawsuit | Clarivate press release ", anchor="Clarivate and OCLC Settle Lawsuit") }}", Clarivate press release issued November 7, 2022_

It isn't clear from this statement whether MetaDoor is done or not.
(We'll answer the "What is/was MetaDoor?" question below.)
The statement, which matches the language in the OCLC statement, only says that a service that includes OCLC records will not be built.
(We'll also try to answer the "What is an OCLC record?" question below.)

## OCLC's Statement
{: #oclc-statement}

OCLC's statement is only a little less vague:

> OCLC is pleased to announce today that it successfully defended WorldCat to protect the collaborative service developed and maintained with and for libraries worldwide.
>
> An agreement has been reached in a lawsuit filed by OCLC in June 2022 against Clarivate and its subsidiaries in the United States District Court, Southern District of Ohio.
>
> Though the settlement document itself is confidential, two significant elements include:
>
>  * **Clarivate, Ex Libris, and ProQuest have ceased the development and marketing of the MetaDoor MARC record exchange system** developed using records that are subject to the WorldCat Rights and Responsibilities Policy.
>  * **Clarivate, Ex Libris, and ProQuest will promptly and permanently delete all MetaDoor work product** that incorporated or was based on records subject to the Policy.
>
> Pursuant to the confidential agreement and elements noted above, OCLC has filed a dismissal of the lawsuit.
>
> Member libraries, publishers, data experts, and OCLC have worked collaboratively for decades to create WorldCat. Protecting this investment and infrastructure ensures innovation for all libraries and sustainability in the future.
>
> _- "{{ robustlink(href="https://www.oclc.org/en/news/announcements/2022/oclc-clarivate-settle-lawsuit.html", versionurl="https://web.archive.org/web/20221107183748/https://www.oclc.org/en/news/announcements/2022/oclc-clarivate-settle-lawsuit.html", versiondate="2022-11-07", title="OCLC and Clarivate settle lawsuit | OCLC press release", anchor="OCLC and Clarivate settle lawsuit") }}", OCLC press release issued November 7, 2022_

We're left with the same questions ("What is/was MetaDoor?" and "What is an OCLC record?").

To dig any further, let's look at some of the court documents.
Many of the documents are available on the CourtListener.com mirror of the federal court PACER system: [OCLC Online Computer Library Center, Inc. v. Clarivate, Plc, 2:22-cv-02470](https://www.courtlistener.com/docket/63381226/oclc-online-computer-library-center-inc-v-clarivate-plc/?order_by=desc).
The most illuminating bits are in the transcripts of conference calls between the court and the lawyers for each side.
(The transcripts are PDF documents, so the Hypothesis service is used to link to specific sections.)

## What was the "MetaDoor MARC record exchange system"?
{: #what-was-metadoor}

Clarivate was pretty cagey on what MetaDoor actually was.
They pretty clearly say that they are not creating a database.
From [page 22 of the transcript of the status conference on June 24, 2022](https://hyp.is/7D7DrkT3Ee2Fc_ea59g-0A/storage.courtlistener.com/recap/gov.uscourts.ohsd.269526/gov.uscourts.ohsd.269526.29.0.pdf):

> THE COURT: All right. In fact, what you are doing, I think, is you are developing a database of information to provide to libraries in competition with OCLC.
>
> MS. RODMAN [counsel for Clarivate]: No, Your Honor, absolutely not.
>
> THE COURT: And you are not doing this for educational purposes. You are doing this for business purposes. You are going to generate some kind of financial benefit by offering this information to others, are you not?
>
> MS. RODMAN: OC -- I'm sorry -- MetaDoor is not, absolutely not, a database. We are not developing a database for libraries. What MetaDoor is is a software solution that lets one library share with another library. No information ever goes into MetaDoor, ever goes to the defendants as a result of MetaDoor. It simply facilitates that library-to-library transfer which is already allowed to happen, and it gives libraries a way to do it that is not a one-by-one clunky way of doing it like they currently do.

"MetaDoor is not, absolutely not, a database"—quite the definitive statement of what it _isn't_, but not very clear about what it _is_.
Marshall Breeding's "{{ robustlink(href="https://librarytechnology.org/document/27423", versionurl="https://web.archive.org/web/20221113213054/https://librarytechnology.org/document/27423", versiondate="2022-11-13", title="MetaDoor: A new bibliographic service for libraries to be offered by Ex Libris", anchor="MetaDoor: A new bibliographic service for libraries to be offered by Ex Libris | Library Technology Guides") }}" from June 2022 has a little more information:

> This new platform will differ from existing bibliographic utilities. Instead of building a massive repository of bibliographic records, the service is based on indexing and artificial intelligence technologies to identify records residing in the integrated library systems or library services platforms of participating institutions that can be shared with other libraries for copy cataloging or record enhancement.

So MetaDoor is not a big repository of metadata records; what might it be?

### My MetaDoor speculation
{: #my-metadoor-speculation}

If MetaDoor wasn't a database of records, then what was it?
At first, I thought it was some sort of metasearch engine where searches are broadcast to an array of library catalogs.
But that isn't any better than the technology we have today; these kinds of broadcast searches are known to be slower than users expect (in the age of instant answers from the web search engines) and notoriously challenging to do good relevance ranking on the fly.

Instead of a database of full records, I think MetaDoor was a database of very brief records and identifiers that facilitated fast full record retrieval from library catalogs.
What follows is complete conjecture...I haven't seen MetaDoor prototypes or talked about its architecture with anyone from Clarivate or development partner libraries.
Instead, this is what I would do if I faced the kinds of design constraints presented in the court filings and was asked to build something.
Let's call it KICReD ("Known Item Cataloging REcord Discovery"), and it would have these parts:

* From participating libraries, a _metadata extract_ of a subset of fields—title, main entry (e.g., author), publisher, ISBN, material type, and dimensions—along with _local catalog identifiers_.
* A _database of facts_ built from the metadata extracts.
* _Z39.50 connection details_ from the participating libraries.
* _Browser-based application_ with a Z39.50 client.

Cataloging a known item with KICReD would use this workflow:

1. The cataloger, starting with the item in hand, would search the _database of facts_ to find records that most closely match the item.
1. The cataloger then selects one or more records from the _database of facts_.
1. The _browser-based application_ gets _Z39.50 connection details_ for the local catalogs of the selected records.
1. The Z39.50 client built into the _browser-based application_ uses the _local catalog identifier_ to retrieve the exact record from the participating library.
1. The _browser-based application_ displays the full MARC record(s) for the user to select for import into the cataloger's library.

A KICReD-like system has several advantages.
First, it would be much faster than broadcast Z39.50 searching.
The _database of facts_ has enough information for the cataloger to select records that most likely match the item in hand.
Searching that database would be fast...the metadata extracts would already have been gathered, clustered, and indexed.
The next step, too, would be relatively fast...known item searching with the local catalog identifier with Z39.50 is a great way to pull up a MARC record.

Second, it would seem to address concerns about WorldCat record reuse.
_Database of Facts_ is a meaningful label in KICReD as facts are not subject to copyright.
Compiling and holding a database of facts would seem to be a defensible position.
And because the Z39.50 search is happening in the user's browser in real-time, the full records are never compiled and so there is never an attempt to build anything that replicates WorldCat.

Third, there are some really neat things that could happen when looking at an array of records about the same item.
It might be possible, for instance, to construct a composite display of all of the fields from all of the selected records...the _browser-based application_ could build a visualization of fields that are most common alongside fields that are unique, and then select the fields that become the record downloaded into the local catalog.

Fourth, one could do some neat automation with this kind of system.
For instance, instead of typing the title and author into a search box, the cataloger could just scan the ISBN barcode from the book jacket and pull up the matching record(s) from the _database of facts_.

If my "KICReD" guess is close to what MetaDoor was, why did Clarivate settle?
The settlement agreement is sealed. so we'll likely never know.
Still, I wonder if they went too far and included the OCLC Record Number in their version of the "database of facts".
Adding that field does make clustering of identical records easier, but (as the OCLC lawyer argued) is demonstrable evidence of the record having come from WorldCat.
Or perhaps there were fields in the _metadata extracts_ touched by OCLC's automated processing that got close to the line between "fact" and "creative effort".
A _main entry_, for instance, could be enhanced with birth and death dates, professional and honorific titles, meeting locations and dates, etc.
One way around that would be to have the participating library send just the subfield "a", which should be enough in the _database of facts_ for the cataloger to select candidate records for full record retrieval from participating libraries.

Side note: if you'd like to have something like KICReD—or just have a better name for it—let me know; it is the type of system that my employer specializes in building.


## What are "records which OCLC has claimed are subject to its policy and contractual limitations"?
{: #what-are-oclc-records}

What is an OCLC Record?
Back to the court documents at [page 18 of the June 24th transcript](https://hyp.is/2nWfwkT2Ee2V3wepwAfZ5w/storage.courtlistener.com/recap/gov.uscourts.ohsd.269526/gov.uscourts.ohsd.269526.29.0.pdf).
The court is asking how (if it had to stop Clarivate from using OCLC records) could it distinguish between OCLC records and non-OCLC records:

> THE COURT: And I'm having trouble with a lack of specificity as to which records your subscribers are free to provide -- because they created them or someone other than OCLC created them and -- and how the Court is going to be able to determine in a -- in a group of data, even with an OCN number attached to it, whether it is something that the -- your subscriber is -- has freedom to release or does not under your subscriber agreement, and I -- go ahead. Answer that.
>
> MS. MARTINEZ [counsel for OCLC]: Yeah. I was going to say maybe this could help. So the libraries will have their initial records prior to the time that they made it to OCLC and -- and before it got into its enhancement process. And so if they want to reach out to a subscriber to see about -- and that's why we -- we redrafted the preliminary injunction order in the manner that we did. This is only related to our member subscribers that currently have their records interacting with the -- the WorldCat database. If they want to reach out to member subscribers and talk to them about their original records before they went into the WorldCat subscriber consortium/network, we're fine with that. If they want to talk to any non -- there are thousands non-WorldCat member libraries or institutions. They are happy to do that. If they want to talk to any of their own New -- SkyRiver subscribers, they are happy to do that. It is just the subset of customers whose records are currently in WorldCat, that those are the ones that we're talking about, and I think the order very specifically relates just to those.
>
> THE COURT: I think you are saying that all of your subscribers, that their current catalogs would -- that all of the information in their current catalogs would be protected from disclosure under your subscriber agreement simply because they -- because they joined up and because they have become a subscriber, that they are not permitted to share information in their catalogs with -- with others.
>
> MS. MARTINEZ: They are WorldCat records. I think that's the difference. It's the WorldCat records that they are not able to share outside of the WorldCat network. They can share it intra-institutional, meaning intra-institutional amongst the other WorldCat subscribers. If they have their records -- their own catalog records that are non-WorldCat records, the records that they had prior to the time that they put those records into WorldCat, they are free to share those, and that's not -- that's not prohibited by the agreement, and it's not -- it's not even talked about in the order. They are free to share non-WorldCat records. That's fine.
>
> THE COURT: Yeah, but everything they have since they have become a WorldCat subscriber is going to be WorldCat records under that definition.
>
> MS. MARTINEZ: No, they would have --
>
> THE COURT: Because you've touched everything they have.
>
> MS. MARTINEZ: No, no, no, no, no, no, no. So like even OCLC -- let's say Ohio State. Let's use that as an example. Ohio State comes to -- to OCLC and becomes a WorldCat subscriber. OCLC could even go back to that point in time before -- you know, with the very limited data that those records had in it prior to the time that it got to OCLC and it enhanced those records, and you could see -- it would look very different. It would be very stripped out. The library similarly could do the same. So if they have their development partners that they are working with that are OCLC WorldCat subscribers, they just can't get their current catalogs as they exist today on the WorldCat system, but they certainly could ask them for the records prior to the time that it went into the WorldCat consortium and OCN number and enhancements occurred and get that from that snapshot in time as well.

OCLC is saying that a library could share with Clarivate the versions of records the library creates before the record is shared with OCLC.
That record wouldn't be an OCLC-enhanced record... a record untouched by OCLC processes.
Once the library downloads and overlays a record from OCLC into its local catalog, it becomes an OCLC/WorldCat record.

The mention of the "OCN number" is interesting.
Could the existence of an OCN in a record be a marker for an "OCLC Record"?
([Transcript page 13](https://hyp.is/yvWDJET1Ee29g1NcZ5_JFw/storage.courtlistener.com/recap/gov.uscourts.ohsd.269526/gov.uscourts.ohsd.269526.29.0.pdf))

> THE COURT: ... Do you assign OCN numbers to all the data that you have, including data created by your subscribers?
>
> MS. MARTINEZ [counsel for OCLC]: We put an OCN number on any record that OCLC enhances. So if it comes into their database and they are going to enhance it by -- kind of similarly to what I talked about on Tuesday to the Court, you know, if they are going to add headnotes or footnotes -- I'm sorry -- head notes, you know, pagination, they are going to change the way that the record is searched.

Perhaps, but counsel from Clarivate takes issue with OCLC "enhancements" ([transcript page 15](https://hyp.is/EaeLyET2Ee2yICPwVcupRQ/storage.courtlistener.com/recap/gov.uscourts.ohsd.269526/gov.uscourts.ohsd.269526.29.0.pdf)):

> MS. RODMAN: ... the term "enhancement" I think is a bit of a misnomer. You have to understand where this data comes from. When OCLC creates a record, it is pulling metadata from other sources, from public sources, from libraries themselves, from the Library of Congress, from publishers. Almost all of the metadata in an OCLC record comes from sources other than OCLC. OCLC pulls that in, and they add an OCN number, which is just a sequential number. [Westlaw example removed.] OCLC assigns that OCN number for purposes of deduplication, but also, Your Honor, so that it can pull in enhancements that its libraries make after it creates the record. So OCLC pulls in metadata. It assigns an OCN number. Then when its members add their own enhancements, further data, the OCN number lets OCLC grab that additional information. So it's a constant cycle of other people, other entities, adding information about a record and OCLC pulling it in, and it uses the OCN number to do that. OCLC has no proprietary interest in this metadata.

The argument from Clarivate's counsel is insightful but incomplete.
Yes, it is true that the metadata OCLC uses to enhance records can come from sources outside of OCLC: publishers, the Library of Congress, and other libraries.
But we've also seen the effort that OCLC puts into records to cluster similar records into works and to eliminate redundant records.
I don't _think_ that effort is subject to copyright as it is seen as mechanical and not creative, but I could be wrong.

So that is the clarity that I and others I've talked to were hoping would come out of this court case...what makes a record an OCLC record, and what proprietary interest does OCLC have in an OCLC record?

## Previous chapters of the OCLC record reuse saga
{: #previous-chapters}

This isn't the first time that questions about the ownership and reuse of WorldCat records have been raised.
In late October 2008, OCLC announced that it was making changes to its <em>{{ robustlink(href="https://web.archive.org/web/20100616212237/http://www.oclc.org/us/en/support/documentation/worldcat/records/guidelines/", originalurl="http://www.oclc.org/us/en/support/documentation/worldcat/records/guidelines/", versiondate="2008-10-30", title="Guidelines for the Use and Transfer of OCLC-Derived Records", anchor="Guidelines for the Use and Transfer of OCLC-Derived Records") }}</em>, which had been in place since 1987.
This touched off a firestorm of controversy that was even visible from outside the library profession (in the form of {{ robustlink(href="https://www.theguardian.com/technology/2009/jan/22/library-search-engines-books", versiondate="2008-11-11", title="Why you can't find a library book in your search engine | The Guardian", anchor="an article in The Guardian newspaper") }}, mentioned in [a 2009 article on this blog](https://dltj.org/article/guardian-correction/)).

In response to the profession's outcry over the new policy, OCLC formed a _Review Board of Shared Data Creation and Stewardship_.
That review board [recommended the withdrawal of the new policy](http://dltj.org/article/oclc-review-board-initial-recommendations/) and the formation of an _OCLC Record Use Policy Council_.
From that, we get the {{ robustlink(href="https://www.oclc.org/en/worldcat/cooperative-quality/policy.html", versionurl="https://web.archive.org/web/20221113225200/https://www.oclc.org/en/worldcat/cooperative-quality/policy.html", versiondate="2022-11-13", title="WorldCat Rights and Responsibilities for the OCLC Cooperative | OCLC", anchor="WorldCat Rights and Responsibilities for the OCLC Cooperative") }} that is in place today.

If you were paying attention earlier, you might have noticed a reference to SkyRiver.
That is a "{{ robustlink(href="https://theskyriver.com/", versionurl="https://web.archive.org/web/20221113225510/https://theskyriver.com/", versiondate="2022-11-13", title="SkyRiver Technologies homepage", anchor="full service bibliographic utility for cataloging") }}" that was [launched in 2009 by the people behind Innovative Interfaces](http://dltj.org/article/skyriver/).
I think SkyRiver is a part of Clarivate now (as part of Ex Libris' purchase of Innovate Interfaces, which was purchased by ProQuest, which was in turn purchased by Clarivate—yes, consolidation in the library automation marketplace is really {{ robustlink(href="https://librarytechnology.org/mergers/proquest/", versionurl="https://web.archive.org/web/20221113230154/https://librarytechnology.org/mergers/proquest/", versiondate="2022-11-13", title="ProQuest: business acquisitions | Library Technology Guides", anchor="that") }} {{ robustlink(href="https://librarytechnology.org/mergers/clarivate/", versionurl="https://web.archive.org/web/20221113230353/https://librarytechnology.org/mergers/clarivate/", versiondate="2022-11-13", title="Clarivate: business acquisitions | Library Technology Guides", anchor="bad") }}).
SkyRiver is nominally a competitor to WorldCat for library cataloging records, but it doesn't have nearly the depth of content and customers.

One last bit.
Over the summer, the International Coalition of Library Consortia (ICOLC) published a statement on {{ robustlink(href="https://icolc.net/statements/icolc-statement-metadata-rights-libraries", versionurl="https://web.archive.org/20220911170812/https://icolc.net/statements/icolc-statement-metadata-rights-libraries", versiondate="2022-11-13", title="Statement on the Metadata Rights of Libraries | ICOLC", anchor="Statement on the Metadata Rights of Libraries") }}.
(I [scribbled some thoughts in the margins](https://via.hypothes.is/https://icolc.net/statements/icolc-statement-metadata-rights-libraries).)
The top of the statement says:

> Metadata and the metadata services that describe library collections are critical in supporting content discovery, knowledge creation, and libraries’ public missions. Metadata describing library collections is not typically copyrightable, and should be considered freely shareable and reusable under most circumstances. However, some industry players restrict libraries’ rights to use such metadata through contractual terms and market influence. Such restrictive activity is out of alignment with libraries’ needs and public, not-for-profit/educational missions.

These questions have been with us for quite a while; it appears they will be with us for quite a bit longer.
