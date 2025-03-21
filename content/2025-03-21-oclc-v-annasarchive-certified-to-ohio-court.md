---
title: "In OCLC v Anna's Archive, New/Novel Issues Sent to State Court"
modified: 
category: Library Technology
categories:
- Library Technology
tags:
- OCLC
- OCLC v Anna's Archive
- metadata
- web scraping
summary: "The case of OCLC against Anna's Archive, accused of &ldquo;data scraping&rdquo; from OCLC's WorldCat, takes a turn as the U.S. District Court for the Southern District of Ohio decides to certify several &ldquo;novel and unsettled&rdquo; legal questions to the Supreme Court of Ohio."
mastodon: ""
---

The U.S. District Court for the Southern District of Ohio released an {{ robustlink(href="https://storage.courtlistener.com/recap/gov.uscourts.ohsd.287709/gov.uscourts.ohsd.287709.47.0.pdf", versionurl="https://web.archive.org/20250321133418/https://storage.courtlistener.com/recap/gov.uscourts.ohsd.287709/gov.uscourts.ohsd.287709.47.0.pdf", versiondate="2025-03-21", title="Opinion, OCLC v. Anna's Archive | U.S. District Court for the Southern District of Ohio", anchor="opinion") }} in the case of [OCLC v. Anna's Archive](https://www.courtlistener.com/docket/68157923/oclc-online-computer-library-center-inc-v-annas-archive/?order_by=desc). 
As you may recall, the case stems from an accusation that Anna's Archive—{{ robustlink(href="https://en.wikipedia.org/wiki/Anna%27s_Archive", versionurl="https://en.wikipedia.org/w/index.php?title=Anna%27s_Archive&oldid=1280995287", versiondate="2025-03-21", title="Anna's Archive | Wikipedia", anchor="a search engine for 'shadow libraries'") }}—scraped the content of OCLC's WorldCat. 
Anna's Archive itself is an anonymous effort, and OCLC named one person in the lawsuit—Maria Matienzo—with a weak and dubious connection to Anna's Archive. 

Here are bits of the court's order from its introduction (the start of the order) and conclusion (at the end):

> This case is about data scraping. Plaintiff Online Computer Library Center, Inc. ("OCLC") is a non-profit organization that helps libraries organize and share resources. In collaboration with its member libraries, OCLC created and maintains WorldCat-the most comprehensive database of library collections worldwide. OCLC alleges that a "pirate library" named Anna's Archive along with Maria Matienzo, and other unknown individuals (collectively, "Defendants") scraped WorldCat's data. OCLC claims that, in doing so, Defendants violated Ohio law. Specifically, OCLC invokes causes of action arising under the Ohio common law of tort, contract, and property, as well as a provision of the Ohio criminal code.
> 
> But whether Ohio law prohibits the data scraping alleged here poses "novel and unsettled" issues. No Ohio court has ever applied its law as OCLC would have this Court do (as far as the Court is aware). Nor have courts uniformly applied analogous laws of other jurisdictions that way. So, to resolve this case, the Court would need to answer "novel and unsettled" questions about Ohio law.
> 
> When that is true-when a federal court faces "novel and unsettled" state-law issues-the federal court may certify those issues to the state's high court. Unwilling to sleepwalk into a drastic expansion of Ohio law, this Court thus resolves to certify the issues presented here.
> 
> [...]
>
> The Court is sympathetic to OCLC's situation: a band of copyright scofflaws cloned WorldCat's hard-earned data, gave it away for free, and then ignored OCLC when it sued them in this Court. But mindful that bad facts sometimes make bad law, the Court requests that an Ohio court intervene before this Court makes any new state tort, contract, property, or criminal law.
> 
> The Court resolves to CERTIFY the novel Ohio-law issues identified above to the Supreme Court of Ohio. Plaintiff's counsel and Matienzo's counsel are ORDERED to propose an order containing all the information Ohio Supreme Court Practice Rule 9. 02 requires by April 11, 2025. The parties may file their proposed orders separately, or, if they so choose, they may file one joint proposed order. The Court will finalize a certification order afterward.
> 
> OCLC's motion for default judgment is DENIED without prejudice. _See Lammert v. Auto-Owners (Mut. ) Ins.,_ 286 F. Supp. 3d 919, 928-29 (M. D. Tenn. 2017) (adopting this same disposition). Because the answers to the certified questions may also determine Matienzo's motion to dismiss under Federal Rule of Civil Procedure 12(b)(6), ECF No. 21, the Court DENIES without prejudice that motion too. _See id._ The Court invites the parties to reraise their motions after the certification proceeding. _See id._
> 
> The Court also grants OCLC leave to amend its Complaint to correct any of the above-identified pleading deficiencies.

OCLC has brought twelve claims against the defendants, including breach of contract, unjust enrichment, tortious interference, criminal violations under Ohio law, trespass to chattels (a fancy way of saying "breaking and entering", I think), and conversion of property to deny benefits to OCLC. 
Almost every claim raises novel legal questions that have not been definitively addressed by Ohio courts. 
As is the practice of federal courts in such cases, the judge decides to certify several "novel and unsettled" legal questions to the Supreme Court of Ohio, given the absence of clear precedent in state case law. 
Interestingly, this includes a question about the enforceability of "browserwrap" contracts—or terms of service that appear as links on the bottom of web pages. 
(This is contrasted with "clickwrap" contracts where the user must affirmatively click an "I agree" button or link.)
Other questions include the definition of unjust enrichment in the context of data scraping and the interpretation of Ohio Revised Code § 2913.04 regarding unauthorized access to computer systems.
If it were only that simple, though...the order also discusses potential preemption by federal copyright law, suggesting that OCLC’s claims may conflict with federal statutes, which complicates the legal landscape further.

There is a curious footnote at the end that makes me wonder if the judge is signalling to Matienzo's lawyers that there may be a way to get their client out of this sticky mess (legal citations removed):

> As an aside, the Court also wonders whether the intracorporate conspiracy doctrine bars OCLC's conspiracy claims. Under that doctrine, an agreement between agents of the same legal entity is not an unlawful conspiracy. OCLC's conspiracy counts allege, in effect, that Matienzo is an agent of Anna's Archive who conspired with other agents of Anna's Archive to scrape WorldCat's data. If Anna's Archive is a legal entity, then OCLC may have alleged an intracorporate conspiracy. The Court pulls this thread no further (because it decides to certify). But, after the certification proceeding, the Court expects the parties will brief whether the intracorporate conspiracy doctrine applies here.

So it would seem that this case is not done, and the focus now shifts to Ohio's top state court. 
I don't know what the odds are that Ohio's court system will take up these questions or what happens if it declines to do so.