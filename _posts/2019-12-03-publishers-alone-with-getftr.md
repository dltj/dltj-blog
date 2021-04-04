---
title: 'Publishers going-it-alone (for now?) with GetFTR'
categories: linking-technologies
tags:
- openurl
- discovery
- ra21
- SeamlessAccess
- niso
- GetFTR
---
In early December 2019, a group of publishers announced [Get-Full-Text-Research](https://www.getfulltextresearch.com/), or GetFTR for short.
I read about this first in Roger Schonfeld's "[Publishers Announce a Major New Service to Plug Leakage](https://scholarlykitchen.sspnet.org/2019/12/03/publishers-announce-plug-leakage/)" piece in _The Scholarly Kitchen_ via Jeff Pooley's [Twitter thread](https://twitter.com/jeffersonpooley/status/1201867300229517313) and [blog post](https://www.jeffpooley.com/2019/12/publishers-announce-a-major-new-service-to-plug-leakage/).
[Details about how this works are thin](https://www.getfulltextresearch.com/how-getftr-works/), so I'm leaning heavily on Roger's description.
I'm not as negative about this as Jeff, and I'm probably a little more opinionated than Roger.
This is an interesting move by publishers, and—as the title of this post suggests—I am critical of the publisher's "go-it-alone" approach.

First, some disclosure might be in order.
My background has me thinking of this in the context of how it impacts libraries and library consortia.
For the past four years, I've been co-chair of the [NISO Information Discovery and Interchange topic committee](https://www.niso.org/topic-committees/information-discovery-interchange) (and its predecessor, the "Discovery to Delivery" topic committee), so this is squarely in what I've been thinking about in the broader library-publisher professional space.
I also traced the early development of RA21 and more recently am volunteering on the SeamlessAccess Entity Category and Attribute Bundles Working Group; that'll become more important a little further down this post.

I was nodding along with Roger's narrative until I stopped short here:

> The five major publishing houses that are the driving forces behind GetFTR are not pursuing this initiative through one of the major industry collaborative bodies. All five are leading members of the STM Association, NISO, ORCID, Crossref, and CHORUS, to name several major industry groups. But rather than working through one of these existing groups, the houses plan instead to launch a new legal entity. 

> While [Vice President of Product Strategy & Partnerships for Wiley Todd] Toler and [Senior Director, Technology Strategy & Partnerships for the American Chemical Society Ralph] Youngen were too politic to go deeply into the details of why this might be, it is clear that the leadership of the large houses have felt a major sense of mismatch between their business priorities on the one hand and the capabilities of these existing industry bodies. At recent industry events, publishing house CEOs have voiced extensive concerns about the lack of cooperation-driven innovation in the sector. For example, [Judy Verses from Wiley spoke to this issue in spring 2018](https://twitter.com/rschon/status/989137191094939649), and [several executives did so at Frankfurt this fall](https://twitter.com/acochran12733/status/1184105258986815489). In both cases, long standing members of the scholarly publishing sector questioned if these executives perhaps did not realize the extensive collaborations driven through Crossref and ORCID, among others. It is now clear to me that the issue is not a lack of knowledge but rather a concern at the executive level about the perceived inability of existing collaborative vehicles to enable the new strategic directions that publishers feel they must pursue. 

This is the publishers going-it-alone.
To see Roger describe it, they are going to create this web service that allows publishers to determine the appropriate copy for a patron and do it without input from the libraries.
Librarians will just be expected to put this web service widget into their discovery services to get "colored buttons indicating that the link will take [patrons] to the version of record, an alternative pathway, or (presumably in rare cases) no access at all."
(Let's set aside for the moment the privacy implications of having a fourth-party web service recording all of the individual articles that come up in a patron's search results.)
Librarians will not get to decide the "alternative pathway" that is appropriate for the patron: "Some publishers might choose to provide access to a preprint or a read-only version, perhaps in some cases on some kind of metered basis."
(Roger goes on to say that he "expect[s] publishers will typically enable some alternative version for their content, in which case the vast majority of scholarly content will be freely available through publishers even if it is not open access in terms of licensing."  I'm not so confident.)

No, thank you.
If publishers want to engage in technical work to enable libraries and others to build web services that determine the direct link to an article based on a DOI, then great.
Libraries can build a tool that consumes that information as well as takes into account information about preprint services, open access versions, interlibrary loan and other methods of access.
But to ask libraries to accept this publisher-controlled access button in their discovery layers, their learning management systems, their scholarly profile services, and their other tools?
That sounds destined for disappointment.

I am only somewhat encouraged by the fact that RA21 started out as a small, isolated collaboration of publishers before they brought in NISO and invited libraries to join the discussion.
Did it mean that it slowed down deployment of RA21? Undoubtedly yes.
Did persnickety librarians demand transparent discussions and decisions about privacy-related concerns like what attributes the publisher would get about the patron in the Shibboleth-powered backchannel? Yes, but because the patrons weren't there to advocate for themselves.
Will it likely mean wider adoption? I'd like to think so.

Have publishers learned that forcing these kinds of technologies onto users without consultation is a bad idea?  At the moment it would appear not.
Some of what publishers are seeking with GetFTR can be implemented with straight-up OpenURL or—at the very least—limited-scope additions to OpenURL (the [Z39.88](https://www.niso.org/publications/z3988-2004-r2010) open standard!).
So that they didn't start with OpenURL, a robust existing standard, is both concerning and annoying.
I'll be watching and listening for points of engagement, so I remain hopeful.

A few words about Jeff Pooley's five-step "laughably creaky and friction-filled effort" that is SeamlessAccess.
Many of the steps Jeff describes are invisible and well-established technical protocols.
What Jeff fails to take into account is the very visible and friction-filled effect of patrons accessing content beyond the boundaries of campus-recognized internet network addresses.
Those patrons get stopped at step two with a "pay $35 please" message.
I'm all for removing that barrier entirely by making all published content "open access".
It is folly to think, though, that researchers and readers can enforce an open access business model on all publishers, so solutions like SeamlessAccess will have a place.
(Which is to say nothing of the benefit of inter-institutional resource collaboration opened up by a more widely deployed Shibboleth infrastructure powered by SeamlessAccess.)