---
title: 'Issue 94: Controlled Digital Lending'
modified: 2022-12-28T16:16:06-05:00
category: Thursday Threads
categories:
- Thursday Threads
tags:
- ebooks
- controlled digital lending
mastodon:
- 
---
E-books are a prominent theme looking back at a couple of year-end issues of _DLTJ Thursday Threads_. 
In [2010](https://dltj.org/article/thursday-threads-2010w52/#books_after_amazon), a writer in _Boston Review_ wondered about "books after Amazon."
In [2011](https://dltj.org/article/thursday-threads-2011w52/#p3560-publishing), an author  for O'Reilly Media's _Radar_ blog wrote that "readers sure to like ebooks" and "DRM is full of unintended consequences." 
(That person also noted that "publishers aren’t necessary to publishing" in predicting that self-publishing on platforms like Amazon's would take off, as it has.) 
Also [in 2011](https://dltj.org/article/thursday-threads-2011w52/#p3560-tech), Fast Company "boldly" predicted that "eBooks will dominate." 
A decade later, ebooks haven't overtaken print books (in a {{ robustlink(href="https://www.pewresearch.org/fact-tank/2022/01/06/three-in-ten-americans-now-read-e-books/", versionurl="https://web.archive.org/web/20221228162602/https://www.pewresearch.org/fact-tank/2022/01/06/three-in-ten-americans-now-read-e-books/", versiondate="2022-12-28", title="Three-in-ten Americans now read e-books | Pew Research Center", anchor="Pew Research Center study from 2021") }}, 65% of adults have read a print book versus 30% for an ebook — that is not "domination"). 

This week, _Thursday Threads_ looks at an active area of exploration and development at the intersection of ebooks and libraries: Controlled Digital Lending (CDL). 
Simply put, CDL is a system that "enables a library to circulate a digitized title in place of a physical one in a controlled manner." (David Hansen, "{{ robustlink(href="https://web.archive.org/web/20220513162025/https://www.youtube.com/watch?v=8quQaIiLPhc", versionurl="https://web.archive.org/web/20220513162025/https://www.youtube.com/watch?v=8quQaIiLPhc", versiondate="2022-12-28", title="Controlled Digital Lending for Resource Sharing | OCLC Resource Sharing 2022", anchor="Controlled Digital Lending for Resource Sharing") }}", OCLC Resource Sharing 2022 at [3:10](https://hyp.is/R3N5Yvs5EeyumZMW4KY4Dg/docdrop.org/video/8quQaIiLPhc/))
A more [expansive definition](https://hyp.is/O4dDYOjHEey_qhNCvliK6A/storage.courtlistener.com/recap/gov.uscourts.nysd.537900/gov.uscourts.nysd.537900.79.0.pdf) comes from the Internet Archive in this letter to the court in the lawsuit filed by the four largest publishers: 

> a nonprofit library that owns a lawfully made and acquired print copy of a book [may] loan a digital copy of that book to a library patron, if the library (1) loans the book to only one patron at a time for each non-circulating print copy it owns (thus maintaining a one-to-one “owned-to-loaned” ratio); (2) implements technical protections that prevent access to the book by anyone other than the current borrower; and (3) limits its digital lending to books published in the past five or more years? This describes Internet Archive’s implementation of a practice known as “Controlled Digital Lending,” or “CDL.”

Details of this lawsuit and more in this issue.

- [Updates on Funding Announcements](https://dltj.org/article/issue-94-controlled-digital-lending#dltj-cdl-updates)
- [Big Publishers versus Internet Archive](https://dltj.org/article/issue-94-controlled-digital-lending#cdl-lawsuit)
- [Origins of Controlled Digital Lending](https://dltj.org/article/issue-94-controlled-digital-lending#cdl-origins)

May you have a safe, happy, and healthy New Year.

{{ thursday_threads_header() }}

## Updates on Funding Announcements
{: #dltj-cdl-updates}
{% include thursday-threads-quote.html
blockquote='These two funding announcements show support for the development of systems and practices for libraries to advance the cooperation beyond the point of shipping physical books back and forth. '
href="http://localhost:4000/article/issue-81-cdill-nfts-cats/#controlled-digital-lending"
anchor="Controlled Digital Lending Gets a Funding Boost"
post=', DLTJ Thursday Threads, 30-Jan-2022'
%}

I posted about two CDL-related funding announcements back in January. 
In the first, the Boston Library Consortium announced a two-year grant to develop CDL software for its member libraries. 
That work is moving ahead, and my employer is involved in the "thin thread" development of the technology piece. 
(Thin thread development is where the end-to-end workflow is created, which is then enhanced with additional capabilities and exception handling.) 
The thin thread is coming together for the new year.

The second is the announcement from NISO about a Mellon Foundation grant that funded a working group to explore standards and interoperability issues with CDL between a library and its patrons as well as borrowing between libraries. 
The report from the working group is being drafted now and will be available for public comment early in the new year.


## Big Publishers versus Internet Archive
{: #cdl-lawsuit}
{% include thursday-threads-quote.html
blockquote='<p>Plaintiffs Hachette, HarperCollins, Penguin Random House, and Wiley (collectively, “Plaintiffs” or “Publishers”) bring this copyright infringement action against IA in connection with website operations it markets to the public as “Open Library” and/or “National Emergency Library.” ... Defendant IA is engaged in willful mass copyright infringement. Without any license or any payment to authors or publishers, IA scans print books, uploads these illegally scanned books to its servers, and distributes verbatim digital copies of the books in whole via public-facing websites. With just a few clicks, any Internet-connected user can download complete digital copies of in-copyright books from Defendant. ...</p><p>... By its actions, alleged above, Defendant has infringed and will infringe the Publishers’ copyrights in and to the Works by, inter alia, reproducing, distributing, publicly displaying, publicly performing, and making derivative works of the Works without any authorization or permission from Plaintiffs.</p>'
href="https://www.courtlistener.com/docket/17211300/1/hachette-book-group-inc-v-internet-archive/"
versionurl="https://web.archive.org/web/20221229000000/https://storage.courtlistener.com/recap/gov.uscourts.nysd.537900/gov.uscourts.nysd.537900.1.0_1.pdf" 
versiondate="2022-12-29" 
anchor="Complaint"
post=', Hachette Book Group, Inc. v. Internet Archive, 1-Jun-2020'
%}

Although the Internet Archive's "National Emergency Library" early in the 2020 Covid-19 pandemic was the driver for this lawsuit, it has come to encompass the notion of CDL. 
(The Internet Archive, though it's "Open Library" program, had a CDL program for participating libraries. As part of the National Emergency Library, the Internet Archive suspended the simultaneous use restrictions because the print books in the nation's libraries were unavailable because the libraries were closed.)
On July 7 this year, motions-for-summary-judgment were filed by the {{ robustlink(href="https://www.courtlistener.com/docket/17211300/87/hachette-book-group-inc-v-internet-archive/", versionurl="https://web.archive.org/web/20221228000000/https://storage.courtlistener.com/recap/gov.uscourts.nysd.537900/gov.uscourts.nysd.537900.87.0.pdf", versiondate="2022-12-28", title="Plantiff's Motion for Summary Judgment | Hachette Book Group, Inc. v. Internet Archive ", anchor="publishers") }} and {{ robustlink(href="https://www.courtlistener.com/docket/17211300/97/hachette-book-group-inc-v-internet-archive/", versionurl="https://web.archive.org/web/20221228000000/https://storage.courtlistener.com/recap/gov.uscourts.nysd.537900/gov.uscourts.nysd.537900.97.0.pdf", versiondate="2022-12-28", title="Defendant's Motion for Summary Judgment | Hachette Book Group, Inc. v. Internet Archive ", anchor="the Internet Archive") }}. 
The court's docket, starting with [entry 87](https://www.courtlistener.com/docket/17211300/hachette-book-group-inc-v-internet-archive/#entry-87) and running through dozens of documents, is full of letters and legal briefs supporting each side. 
The judge in the case has not ruled yet on the competing motions for summary judgement. 
If the judge denies both motions, the litigants will move on with the lawsuit's discovery phase. 
One has to wonder if this court case will last as long as the Google Book Search case, [The Authors Guild v Google](https://www.courtlistener.com/docket/4522355/the-authors-guild-v-google-inc/) from 2005; that took 10 years and a run through the federal appeals court before it was decided. 

_Opinion:_ what bothers me about this lawsuit is that the publishers are falling back to suing libraries when they could spend this money improving their products. 
What libraries make is going to be a scanned facsimile of the printed book...that is, by definition, what CDL is about. 
That scan of a printed book will be readable, but it won't be ideal. 
The reader can't change the font size and re-flow the text of a CDL-lent item; it will be fixed to what was rendered on the printed page. 
The publisher has the source file, so it can re-flow the text and create value-added features that follow characters in fiction or give more details on a term in a non-fiction book (like the {{ robustlink(href="https://kdp.amazon.com/en_US/help/topic/G202187230", versionurl="https://web.archive.org/web/20221228195121/https://kdp.amazon.com/en_US/help/topic/G202187230", versiondate="2022-12-28", title="X-Ray for Authors | Kindle Publishing", anchor="Kindle X-Ray functionality") }}). 
The publishers' electronic version can have hyperlink features to other ebook sections or to supplemental content outside the ebook. 
But rather than innovate their product to take advantage of the capabilities that ebooks bring to their back catalog, the publishers attack libraries for a Constitutionally-enumerated right.


## Origins of Controlled Digital Lending
{: #cdl-origins}
{% include thursday-threads-quote.html
blockquote='I believe it is possible to build a digital library that respects both of the intended beneficiaries of the Copyright Clause—copyright owners and society—while testing commonly held assumptions about the limitations of copyright law. In balancing these goals, TALLO permits circulation of the exact number of copies purchased, thereby acknowledging the rights inherent in copyright, but it liberates the form of circulation from the print format.'
href="https://scholarship.law.georgetown.edu/cgi/viewcontent.cgi?article=1698&context=facpub"
versionurl="https://web.archive.org/web/20221228000000/https://scholarship.law.georgetown.edu/cgi/viewcontent.cgi?article=1698&context=facpub" 
versiondate="2022-12-28" 
anchor="Building a Collaborative Digital Collection: A Necessary Evolution in Libraries"
post=', Michelle M. Wu, Georgetown University Law Center, 16-Nov-2011'
%}

There is the origin of the notion of the own-to-loan ratio...if a library owns a physical copy of an item, it can lend a digital facsimile of that item if it takes the physical copy out of circulation.
For all of the legal wrangling around CDL—see entry above—is it ironic that the notion for CDL came from a law library professor?
(Full [metadata for this article](https://scholarship.law.georgetown.edu/facpub/699/) is in the Georgetown Law Scholarly Commons.)


## Cats on Christmas
{: #stockings}
{{ image(width="700", localsrc="2022/2022-12-29-stockings.jpeg", alt="Two photographs side-by-side. In the left photograph, a white cat with black splotches has his nose buried in a Christmas stocking that is propped up against a low table with a green and red checked tablecloth. In the right photograph, a black cat is sniffing the cat toys coming out of a stocking that is propped up on the back of a stuffed chair.") }} 
Look at these two hooligan cats getting their noses into their Christmas stockings. 
A few new toys with lots of fresh catnip are attracting them.

I [said this last week](http://localhost:4000/article/issue-93-ai-chat/#dual-thrones) as well, "Now there are two happy cats."