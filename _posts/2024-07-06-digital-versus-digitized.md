---
title: "Digital versus Digitized: On the Hachette v. Internet Archive Appeal Oral Argument"
categories: L/IS Profession
tags:
- controlled digital lending
- Internet Archive
- Hachette v. Internet Archive
- publishers
- copyright
---
One thing that would dramatically clarify the controlled digital lending concept in general and the _Hachette v. Internet Archive_ lawsuit in particular is having distinct terms for types of ebooks. I propose that we refer to them as _digital_ and _digitized_. A _digital book_ is one that is born digital, where the publisher has the original "source code". Alternatively, a _digitized book_ originates as a physical copy, which is then converted into a sequence of printed page images. Given the differences in the way they are created by the publisher and the capabilities offered to the reader, distinguishing the two types of books is appropriate. I'm not a marketer, but I suspect _digital_ and _digitized_ might be too similar for an average person to notice the subtle differences. As technical descriptors, these terms help clarify some of the misunderstandings (or even willful obfuscations?) I heard during the circuit court oral arguments.

On June 28, 2024, the oral arguments in the {% include robustlink.html href="https://www.courtlistener.com/docket/67801014/hachette-book-group-inc-v-internet-archive/?order_by=desc" versionurl="https://web.archive.org/web/20240706193105/https://www.courtlistener.com/docket/67801014/hachette-book-group-inc-v-internet-archive/?order_by=desc" versiondate="2024-07-06" title=" Hachette Book Group, Inc. v. Internet Archive (23-1260) | Court of Appeals for the Second Circuit via CourtListener" anchor="Hachette Book Group, Inc. v. Internet Archive case" %} took place. Shortly after, a [recording was made readily available on the Internet Archive](https://archive.org/details/20240628-appeal-oral-argument-second-circuit-88min). I created an [unofficial transcript of this recording](https://media.dltj.org/unchecked-transcript/20240703T204937-united-states-court-appeals-second-circuit-via-internet-archive--hachette-book-group-inc-v-internet-archive-appeal-oral-argument/index.html), which I posted on my media site with [Hypothesis](https://hypothes.is/) enabled. I made 30 notable annotations in the transcript, comprising key points, personal comments, and several references to external materials. (Feel free to annotate specific points alongside me on Hypothesis, if you wish.) This post consolidates those ideas and remarks into a coherent form. 

_Disclosures:_ Despite not being a lawyer, I find the intersection of copyright, fair use, library services, and societal welfare intriguing, and often reflect and write about them professionally. This is not legal advice. I'm currently employed by a software company that's developing a controlled digital lending system. In addition to my professional ties, I believe controlled digital lending is a tremendous benefit for library patrons, libraries, and society at large.

## Background
{: #background}

_Hachette v. Internet Archive_ is a lawsuit filed on June 1, 2020, during the peak of the Covid-19 pandemic, in response to the {% include robustlink.html href="https://blog.archive.org/national-emergency-library/" versionurl="https://web.archive.org/web/20240706193352/https://blog.archive.org/national-emergency-library/" versiondate="2024-07-06" title="Internet Archive's National Emergency Library" anchor="National Emergency Library | Internet Archives blog" %} (NEL) program. The NEL program, initiated on March 24, 2024, removed the restrictions on the number of patrons allowed simultaneous access to digitized books on IA's {% include robustlink.html href="https://openlibrary.org/" versionurl="https://web.archive.org/web/20240706193620/https://openlibrary.org/" versiondate="2024-07-06" title="Open Library homepage" anchor="Open Library collection" %}. Before this pandemic-induced change, libraries could partner with Open Library to provide access to digitized books for their patrons. IA employed a system called {% include robustlink.html href="https://controlleddigitallending.org/" versionurl="https://web.archive.org/web/20240706193713/https://controlleddigitallending.org/" versiondate="2024-07-06" title="Controlled Digital Lending homepage" anchor="Controlled Digital Lending" %} (CDL), assuring that digitized copies weren't distributed to the public unconditionally. CDL is a blend of digital rights management (DRM), library operations software, and library protocols, ensuring that a single physical copy is not loaned more than once in any form, whether physical or digital. NEL removed this "never lent more than once" CDL restriction based on the premise that all the nation's public libraries were closed and no one could access the physical materials. {% include robustlink.html href="https://www.publishersweekly.com/pw/by-topic/digital/copyright/article/83584-internet-archive-to-end-national-emergency-library-initiative.html" versionurl="https://web.archive.org/web/20240706193819/https://www.publishersweekly.com/pw/by-topic/digital/copyright/article/83584-internet-archive-to-end-national-emergency-library-initiative.html" versiondate="2024-07-06" title="Internet Archive to End 'National Emergency Library' Initiative | Publishers Weekly" anchor="NEL concluded on June 16, 2020" %}, and IA's regular CDL program resumed. For a more detailed explanation of CDL, refer to an article I authored called [Controlled Digital Lending…What's the Fuss?](https://dltj.org/article/cdl-code4lib/) derived from my talk at Code4Lib in 2023, and [Issue 94](https://dltj.org/article/issue-94-controlled-digital-lending/) of my intermittent newsletter.

The federal court in the Southern District of New York ruled in favor of Hachette on August 11, 2024, but the judgement was stayed pending an appeal to the intermediate court. The oral arguments last week were part of that process, and now we wait for that ruling. From accounts I've read, it seems like both parties are poised to take this to the U.S. Supreme Court no matter who wins.

Because I started trying to draw a distinction between various terms, I'm going to carefully chose my words in this post:

* **Digital book**: A digital book, born from electronic files. ePub, Daisy, and the Kindle format are common file formats for these books, which use digital typesetting to arrange words on a screen.
* **Digitized book**: A book with pages that are images of a physical item. Originally digitally typeset on a printed page, these pages are then scanned and sequenced into a file.
* **E-book**: An umbrella term encompassing both _Digital_ or _Digitized_ books as defined above.
* **Physical book**: As simple as it sounds: a book that exists in a physical, human-readable format.
* **Book**: If I refer to a "book" without any of the modifiers above, it applies to any type of book: digital, digitized, or physical.

## Digital versus Digitized Marketplaces
{: #digital-versus-digitized}

I led this blog post with a discussion of _digital books_ versus _digitized books_, and it wasn't long into the Internet Archive's presentation that we get to the matter.

> [15:25] under [fair use] factor 4 you say that actually there's one reason there's still be a market for e-books is because e-books are more attractive than digitized versions of physical books. Right? Because they have features and they're more user friendly or whatever. So what that kind of means is what you're saying is that your digital copies are more convenient or more attractive, I guess more convenient than physical books, but less convenient than e-books. 

The judge is asking about the three kinds of books: "physical books", "digitized versions of physical books", and "ebooks". So, we are already recognizing that digitized books and digital "ebooks" are different and that digitized books are "more convenient than physical books but less convenient than ebooks." 

There seems to be a legal concept here about "markets", and specifically whether digitized books (from libraries through CDL) and digital books (from publishers through Overdrive and other programs) are in the same "market".  It seems undisputed that the market for physical books and the market for something digital/digitized are different...even though they hold the same basic content. It does seem disputed whether digitized books (which are facsimiles of the content in physical books) and digital books (with capabilities only possible in the digital realm) are in the same market or are different markets. To my eye, a digitized book is mostly akin to a physical book with the exception that the digitized book can be more easily distributed via electronic devices. The real difference lies in the capabilities of the born-digital book on an electronic device. But I don't know how the law defines "markets" in this case.

In the "ebook" marketplace, publishers will license "digital" books to libraries using a service like {% include robustlink.html href="https://company.overdrive.com/company-profile/who-we-are/" versionurl="https://web.archive.org/web/20240706194012/https://company.overdrive.com/company-profile/who-we-are/" versiondate="2024-07-06" title="Who is Overdrive and what do they do? | Overdrive" anchor="Overdrive" %}. A publisher is unlikely to sell or license a "digitized" book to libraries. (I last heard of a publisher doing this early digital days of the 1990s.) Also in the "ebook" marketplace, a library will use CDL to lend a "digitized" book to patrons. It is conceivable that a library could lend a "digital" book if it has purchased the rights to do so, but that is unusual at this stage.

## Sidenote: when digital and digitized have identical packaging, _a la_ PDFs
{: #pdfs}

Let's get into the weeds for a moment and talk about how the PDF file format muddies the distinction between digital and digitized. There are two main types of PDF files: those created from digital typesetting and those created from scanned images of printed pages. Digitally typeset PDFs—digital books—are created using digital typesetting software such as Adobe InDesign, Microsoft Word, or LaTeX. The content is created and formatted within the software and then exported or saved as a PDF file. Digitally typeset PDF files can be made accessible to assistive technologies by properly tagging the structure and content of the document; this allows screen readers to interpret and navigate the PDF file. Digitally typeset PDF files are usually smaller in size compared to scanned PDFs because they contain vector-based text and graphics.

On the other hand, PDF files based on scanned images of printed pages—digitized books—are created by scanning or photographing physical printed pages using; each page of the book is captured as an image. Scanned PDF files are not inherently accessible to assistive technologies like screen readers because the text is not selectable or readable by these tools. Scanned PDF files also tend to have larger file sizes compared to digitally typeset PDFs because they contain high-resolution images of each page. The text _might_ be selectable to be copied out of the document, but only if a layer of Optical Character Recognition (OCR) has been applied to the file. OCR software analyzes the images and attempts to recognize and convert the characters into selectable and searchable text.

The same file format—PDF—can be used for both a _digital book_ and a _digitized book_. You might initially only be able to tell the different by the file size, but capabilities will be apparent to the reader soon after it is opened. Some publishers use PDF as a delivery format, and these are most likely the digitally typeset files. The reader doesn't get the digital book advantages of reflowing text or changing the font family or size with this kind of PDF. CDL can also use PDF as a delivery mechanism, and this is most likely the sequence of images PDF.

Fortunately, the court doesn't get into this level of technical detail. Unfortunately, I think a lot of sides talking past each other come from muddy technical aspects of licensing versus lending a "PDF".

## The rights with first-sale
{: #first-sale}

Some examples from the oral arguments where not having clear definitions causes problems:

> [18:02] When they buy those books, they buy the physical copies to lend to their patrons one at a time or through an interlibrary change. They also buy e-books to make those available to their patrons. We're focused here on e-books and impacting e-licensing. I have a hard time reconciling those two, specifically as to e-licensing. Why would libraries ever pay for an e-license if they could have internet archives, scan all the books, hard copies they buy and make them available on an unlimited basis?

Internet Archives' counsel points out here that in licensing e-books, the libraries are not adding to their permanent collection. Libraries haven't bought the book, and don't have the first-sale rights to do what they want with the book. And most publishers—notably the major commercial/trade publishers that are a part of this lawsuit—do not want to sell e-books with first sale rights for a library to add to its permanent collection. (How a library is supposed to fulfill the part of its mission to preserve cultural artifacts is beyond the scope of this post, but you can see the obvious problems of saving e-books.)

## The origins of CDL, or the point at late in the arguments where I exclaim WHAT?!?
{: #origins-of-cdl}

Late in the publisher's arguments comes this bit:

> [1:08:29] Control digital lending is a contrived construct that was put together at the behest of Internet Archive back in 2018 when they confronted the fact that libraries didn't want to deal with them. Libraries didn't want to give copies of their works to be digitized because they were concerned about copyright arguments. So they got in a room together with various people and contrived this principle of control digital lending to rationalize what they were doing. 

CDL is _much_ older than 2018. IA's version of CDL predates the first discussion of it by over half a decade (see the [origins of Controlled Digital Lending](https://dltj.org/article/issue-94-controlled-digital-lending/#cdl-origins) in issue 94), and there are earlier implementations. I don't remember seeing this claim from the publishers in their district court complaint, so I hope there is evidence for this statement on the record in the evidence presented to the lower court.

## Publishers will stop publishing
{: #publishers-stop-publishing}

Starting with the publisher's lawyer:

> [1:15:20] That IA's brief and amici try to create the impression that the public interest is on their side. And it is not. The protection of copyright is in the US Constitution and federal law because it creates an incentive for writers and artists to create new works to benefit our broader society. Internet Archives' control digital lending is in direct conflict with that basic principle. And as I previously... 
>
> You don't really think people are going to stop writing books because of the control digital lending to you? 
>
> Well, I think publishers are going to go down the tubes if they do not have the revenues. 
> 
> You think that that's really... 
>
> I do, Your Honor. There's no question. I mean, and the standard here is not, will this eliminate... 
>
> No, I understand. It's just a part. But this question about balancing the incentive to create a work with the larger distribution of it, that is the question to be decided in this case.

If this gets to the U.S. Supreme Court, do we get to go with the originalist's thinking from the {% include robustlink.html href="https://en.wikipedia.org/wiki/Copyright_Act_of_1790" versionurl="https://en.wikipedia.org/w/index.php?title=Copyright_Act_of_1790&oldid=1226659291" versiondate="2024-07-06" title="Copyright Act of 1790" anchor="Copyright Act of 1790 | Wikipedia" %} that copyright extends for 14 years with the right to renew for a additional 14-year term should the copyright holder still be alive?

## The market becomes only as large as the number of people who simultaneously want to read a work
{: #market-size}

A judge make a good point about the potential market effect of library's CDL:

> [1:18:32] But you're reducing the market from the number of people who might want to read... Let's look at even the paper books. They'll pretend like take out the digital market for a second. The number of people who might want to read it ever, down to the number of people who might want to read it simultaneously. And if you put digital books into the mix, it's the same idea, right?

At the extreme, the workflow efficiencies that come with CDL (or, a "reduction in friction" as I think it is referred to in the oral arguments) could mean that there is only a market as big as those who want physical books for their personal collection and libraries collectively purchasing a number of physical items to fulfill digitized book needs. (There is still a market for digital books that publishers won't sell to libraries.) There is some nuance here, but the point is interesting. 

And it is here that I think we see the first substantive discussion of _digital_ versus _digitized_:

>  [1:19:48] that efficiency may or may not have an effect on either the number of copies that get sold or on the market for the Overdrive service, which has a variety of different sort of different aspects and benefits over and above CDL. I mean, CDL is largely sort of scanned images of pages of paper books because it's the paper book. The Overdrive service has a lot of benefits. You can flow the text. You can do different features and that is one reason why...that is one explanation for the data that you see—that there is no reduction in demand for Overdrive.

## My informed but not expert opinion
{: #my-opinion}

I agree with those that are saying that the line of questioning from the circuit court judges shows a more thoughtful approach to the nuances of copyright than was seen in the district court decision. The judges and lawyers seem to recognize that digitized books and digital books are different, with digitized books being more convenient than physical books but less functional than digital books. However, there appears to be a dispute over whether digitized books and digital books are in the same "market" or different markets, which is a key factor in determining fair use.

The concept of first-sale rights is central to the discussion of library lending and ebook licensing. Libraries purchase physical books with the right to lend them to patrons, but when licensing ebooks, they do not have the same ownership rights. This distinction is crucial in understanding the limitations libraries face in providing access to books (physical or ebooks — to say nothing about preserving books, too). The argument that CDL threatens the incentive for writers and artists to create new works, as publishers may "go down the tubes" without sufficient revenues, is a significant point of contention. The balancing of copyright protection and the broader distribution of works is a central question in this case.

This case highlights the complexity of the issues surrounding digital and digitized books, copyright, fair use, and library lending. The distinction between digital and digitized books is crucial in understanding the nuances of the case and the potential implications for the future of ebooks and library services.

## Other articles and opinions
{: #other}

- Authors Alliance: {% include robustlink.html href="https://www.authorsalliance.org/2024/07/02/hachette-v-internet-archive-update-oral-argument-before-the-second-circuit-court-of-appeals/" versionurl="" versiondate="2024-07-06" title="Hachette v. Internet Archive Update: Oral Argument Before the Second Circuit Court of Appeals | Authors Alliance" anchor="Hachette v. Internet Archive Update: Oral Argument Before the Second Circuit Court of Appeals" %}
- Internet Archive: {% include robustlink.html href="https://blog.archive.org/2024/07/01/what-happened-last-friday-in-hachette-v-internet-archive/" versionurl="https://web.archive.org/web/20240706194312/https://blog.archive.org/2024/07/01/what-happened-last-friday-in-hachette-v-internet-archive/" versiondate="2024-07-06" title="What happened last Friday in Hachette v. Internet Archive? | Internet Archive blog" anchor="What happened last Friday in Hachette v. Internet Archive?" %}
- Ars Tecnica: {% include robustlink.html href="https://arstechnica.com/tech-policy/2024/06/appeals-court-seems-lost-on-how-internet-archive-harms-publishers/" versionurl="https://web.archive.org/web/20240706194407/https://arstechnica.com/tech-policy/2024/06/appeals-court-seems-lost-on-how-internet-archive-harms-publishers/" versiondate="2024-07-06" title="Appeals court seems lost on how Internet Archive harms publishers | Ars Technica" anchor="Appeals court seems lost on how Internet Archive harms publishers" %}
