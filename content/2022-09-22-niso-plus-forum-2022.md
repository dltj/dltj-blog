---
title: 'Trip Report: NISO Plus Forum 2022'
modified: 2022-09-22T22:24:51-04:00
category: L/IS Profession
categories:
- L/IS Profession
tags:
- niso
- NISOplus
---

Earlier this week, NISO held its one-day {{ robustlink(href="https://niso.plus/forum/", versionurl="https://web.archive.org/web/20220923015355/https://niso.plus/forum/", versiondate="2022-09-22",, anchor="NISO Plus Forum for 2022") }}.
{{ image(div_float="right", width="300", localsrc="2022/2022-09-22-niso-plus-forum.webp", alt="NISO Plus Forum 2022 logo") }}
This was an in-person meeting that is intended to feed into the online conference in February 2023.
Around 100 people from NISO's membership groups—libraries, content providers, and service providers—attended to talk about _metadata_.
The meeting was structured in {{ robustlink(href="https://theworldcafe.com/key-concepts-resources/world-cafe-method/", versionurl="https://web.archive.org/web/20220923015409/https://theworldcafe.com/key-concepts-resources/world-cafe-method/", versiondate="2022-09-22",, anchor="_World Café_ style") }} and was moderated by {{ robustlink(href="https://niso.plus/taking-a-hands-on-approach-to-improving-metadata-at-the-niso-plus-forum/", versionurl="https://web.archive.org/web/20220923015711/https://niso.plus/taking-a-hands-on-approach-to-improving-metadata-at-the-niso-plus-forum/", versiondate="2022-09-22",, anchor="Jonathan Clark") }}.
The broad topic of "metadata" was broken down into three parts:

* Identifiers: what identifiers are missing or underutilized
* Exchange: what is the most significant barrier to seamless exchange?
* Structure: what is impossible due to a lack of appropriate structures?

There were small table discussions for each part of no more than six people, with 15 minutes at a table before everyone got up and moved to a new table.
After three rounds of 15 minutes, a scribe that stayed at the same table the whole time reported the major themes to the larger group.
What makes this style interesting is that everyone's experience is different.
We agreed to use the {{ robustlink(href="https://www.chathamhouse.org/about-us/chatham-house-rule", versionurl="https://web.archive.org/web/20220923020029/https://www.chathamhouse.org/about-us/chatham-house-rule", versiondate="2022-09-22",, anchor="Chatham House Rule") }}; what is reported here is my interpretation of my table's discussion and my take on the broader outcomes.

<em>Edited on 5-Oct-2022 to add:</em> NISO published a summary of the in-person meeting in the October issue of NISO I/O — {{ robustlink(href="https://www.niso.org/niso-io/2022/09/are-you-ready-metadata-musical", versionurl="https://web.archive.org/web/20221005203438/https://www.niso.org/niso-io/2022/09/are-you-ready-metadata-musical", versiondate="2022-10-05", title="Are You Ready? Metadata -- The Musical! | NISO I/O", anchor="Are You Ready? Metadata -- The Musical!") }}.

## Identifiers
The most fascinating idea I discovered here was how much the metadata ecosystem relies on "Publication Date".
Not only do several parts use publication date as an anchor, but different understandings of the meaning of "publication date" cause many problems downstream.
There is the online publication date, the physical publication date, and sometimes simply an unlabeled publication date.
Some publishers have a practice of changing an online publication date to the physical issue date when the issue comes out.
(Changing a field that others use as part of metadata to distinguish one item from another is never a good thing.)

"Place of Publication" also has a lot of variability and inconsistency, even within a publisher.
Institution identifiers were also a topic, particularly with the lack of hierarchy in the {{ robustlink(href="https://ror.org/", versionurl="https://web.archive.org/web/20220901085637/https://ror.org/", versiondate="2022-09-22",, anchor="Research Organization Registry") }} (ROR).
Someone reported that ROR is working to address the problem, but right now there is not a good way to relate a department to its encompassing agency or organization.

I showed my professional age a bit by mentioning {{ robustlink(href="https://en.wikipedia.org/wiki/Serial_Item_and_Contribution_Identifier", versionurl="https://web.archive.org/web/20220923020033/https://en.wikipedia.org/wiki/Serial_Item_and_Contribution_Identifier", versiondate="2022-09-22",, anchor="SICI") }}—the Serial Item and Contribution Identifier.
This is a compound identifier developed in the 1990s. Given a citation, you could construct a SICI that was a kind of key to the article. For instance,

Lynch, Clifford A. "The Integrity of Digital Information; Mechanics and Definitional Issues." JASIS 45:10 (Dec. 1994) p. 737-44

...could be condensed into...

0002-8231(199412)45:10<737:TIODIM>2.3.TX;2-M

This standard didn't last past the early 2000s, although a few people at my table mentioned that they saw examples of this identifier in their backfile as the publisher-specific suffix of a DOI.

## Exchange
Among the metadata exchange topics, the one I found the most interesting was diversity-equity-inclusion data points in an authoring workflow.
With a desire to address inequity in a field, these data points would be gathered from many sources.
This is sensitive data, so how can it be kept secure while ensuring the integrity of the data (for instance, catching when false data is dumped into the system).

## Structure
As we know, metadata is gathered, aggregated, mixed, and disseminated in ways that the originator can't predict.
A big problem when this happens is having ways to assert confidence in a data element.
Take, for instance, the ORCID field for an author. Was that ORCID obtained when the author logged in with the {{ robustlink(href="https://info.orcid.org/documentation/api-tutorials/api-tutorial-get-and-authenticated-orcid-id/", versionurl="https://web.archive.org/web/20220923020205/https://info.orcid.org/documentation/api-tutorials/api-tutorial-get-and-authenticated-orcid-id/", versiondate="2022-09-22",, anchor="Authenticated ORCID ID workflow") }}? Was it manually keyed by an author (and subject to typos)? Did the software guess the ORCID based on name and institution affiliation?
There can be a range of certainty that an ORCID ID is correct for a particular author.
And—related to "Exchange"—how can this certainty be expressed to subsequent users of the metadata record.

## The Top-Level Topics
One goal of the NISO Plus Forum was to gather topics for sessions at next February's NISO Plus Conference.
At the end of the day, there was one final table session where we were asked to propose a session for the conference: what is the topic? what questions would the session answer? who should attend and who should speak?

Reflecting the observation that metadata is much more than technical specifications, the proposed conference topics tended to want to explain to an organization's management and end-users why carefully curated metadata is essential.
The session would answer questions like "why is it important to fund robust metadata systems?" and "how do we measure return-on-investment for our metadata systems?"
One person said that metadata needs its own public relations manager.
Another sought accessible messaging on the importance of metadata to send to the people making decisions.
Relatedly, how can researchers be convinced of the importance of identifiers like ORCID and ROR as they input data on grant applications and institutional repository deposit forms?

## My Takeaways
Honestly, those were not the outcomes I expected as the top-level ideas from the Forum.
As you can tell from my summary above, I thought we'd focus on discussions of a collective understanding of a set of "publication date" fields.
Or think about how the producers and consumers of metadata can agree on a range of confidence for a particular metadata field.
The end-of-the-day outcomes were very high-level and not focused on making the exchange and use of metadata better across the field.

That aside, it was a wonderfully engaging conversation all day long.
NISO is on the right track to having focused meetings like this that put a value on activities that are best done in person.
This was not an event full of prepared presentations or passive panel sessions.
It made the best use of precious face-to-face time and gathered topics that would feed into the online conference.

Thank you to the American Geophysical Union in Washington, DC, for the use of their meeting space, Silverchair for their significant sponsorship, and all of the other event sponsors.
I ended up with seven pages of dense notes to think about, so thank you, too, to all of the participants.
