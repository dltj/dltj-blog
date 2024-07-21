---
title: 'Issue 84: Chips Go Bad, Learn From Our Cyber Mistakes, Automation at the USPS'
modified: 2022-02-10T08:05:10-05:00
categories:
- Thursday Threads
---
The invoice is in. 
This reengineered blog and the reinvigorated <i>Thursday Threads</i> newsletter cost just US$2.51 last month.
All of that cost is in the blog construction and delivery. 
The cost of delivering the newsletter alone falls well below {% include robustlink.html href="https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=*all" versionurl="https://web.archive.org/web/20210710132838/https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=*all" versiondate="2022-02-09" title="AWS Free Tier" anchor="AWS' always-free tiers of service" %}. 
Not bad!
And as always, no internet trackers or surveillance capitalism is involved.

The threads this week:

* [When Bugs Come from the Chips, not the Code]({% post_url_absolute 2022-02-10-issue-84-chip-bugs--cyber-board--usps-automation %}#computer-chips)
* [Learning From Our Cyber Mistakes]({% post_url_absolute 2022-02-10-issue-84-chip-bugs--cyber-board--usps-automation %}#cybersecurity-review-board)
* [Automation at the United States Postal Service]({% post_url_absolute 2022-02-10-issue-84-chip-bugs--cyber-board--usps-automation %}#usps-automation)

{% include thursday-threads-header.html %}


## When Bugs Come from the Chips, not the Code
{: #computer-chips}


{% include thursday-threads-quote.html
blockquote='Imagine for a moment that the millions of computer chips inside the servers that power the largest data centers in the world had rare, almost undetectable flaws. And the only way to find the flaws was to throw those chips at giant computing problems that would have been unthinkable just a decade ago.

As the tiny switches in computer chips have shrunk to the width of a few atoms, the reliability of chips has become another worry for the people who run the biggest networks in the world. Companies like Amazon, Facebook, Twitter and many other sites have experienced surprising outages over the last year.'
href="https://www.nytimes.com/2022/02/07/technology/computer-chips-errors.html"
versionurl="https://web.archive.org/20220209040808/https://www.nytimes.com/2022/02/07/technology/computer-chips-errors.html"
versiondate="2022-02-09 03:57:33+00:00"
anchor="Tiny Chips, Big Headaches: As the largest computer networks continue to grow, some engineers fear that their smallest components could prove to be an Achilles’ heel"
post=', New York Times, 7-Feb-2022'
%}

We have all experienced unexplained computer errors. 
The software programmer among us cringe and think about what they possibly did wrong. 
Did I use the wrong variable in that loop, did I miss a {% include robustlink.html href="https://www.wired.com/2009/07/dayintech-0722/" versiondate="2022-02-09" title="July 22, 1962: Mariner 1 Done In by a Typo | Wired Magazine" anchor="hyphen" %}?
What if the programmer did everything correctly and the computer just "glitched"?

Modern computers have many layers of redundancy built into them—error-correcting memory, multi-drive storage volumes, checksums on blocks of data, and so forth. 
This article from the _New York TImes_ points to a new cause...the physics of electrons moving over very small spaces. 
As the hardware architects press for smaller, faster, more electrically efficient chips, they will more often face this challenge and need to account for it in their designs.


## Learning From Our Cyber Mistakes
{: #cybersecurity-review-board}

{% include thursday-threads-quote.html
blockquote='The new Cyber Safety Review Board is tasked with examining significant cybersecurity events that affect government, business and critical infrastructure. It will publish reports on security findings and recommendations, officials said...

The board, officials have said, is modeled loosely on the National Transportation Safety Board, which investigates and issues public reports on airplane crashes, train derailments and other transportation accidents.'
href="https://www.wsj.com/articles/biden-administration-forms-cybersecurity-review-board-to-probe-failures-11643898601?mod=djemalertNEWS"
versionurl="https://web.archive.org/20220204140811/https://www.wsj.com/articles/biden-administration-forms-cybersecurity-review-board-to-probe-failures-11643898601?mod=djemalertNEWS"
versiondate="2022-02-04 13:25:41+00:00"
anchor="Biden Administration Forms Cybersecurity Review Board to Probe Failures"
post='Wall Street Journal, 3-Feb-2022'
%}

You might think working with computers is an engineering discipline. 
But unlike other engineering professions, the computing field has little accountability for the errors of its practitioners and a formal method for spreading what was learned from those errors to prevent them from happening again. 
As the quote above suggests, think of "National Transportation Safety Board" that investigates aviation, highway, marine, pipeline, and railroad accidents. 
Their reports form the basis of new regulations that make these fields safer. 
Or think of the investigations of problems with electrical systems, concrete strength, or steel infrastructure. 
What is learned from those probes is encoded into standards and building codes. 

The computing profession has nothing equivalent. 
It is good to see this one small area—cybersecurity incidents—get that kind of national focus and the formation of a {% include robustlink.html href="https://www.cisa.gov/cyber-safety-review-board" versiondate="2022-02-09" title="Cyber Safety Review Board" anchor="review board" %} that might start instilling some of that engineering mentality into the field.


## Automation at the United States Postal Service
{: #usps-automation}

{% include thursday-threads-quote.html
blockquote='Delivering hards, no matter the cost, is a reflection of the US Post Office’s commitment to truly universal service—a radical vision of democratic communications infrastructure enshrined in the Postal Service Act of 1792. No matter the sender, the recipient, or the distance separating origin and destination, federal code stipulated that the Post Office must “bind the nation together.” As Alexis de Tocqueville put it in his 1835 treatise Democracy in America, the US mail system, unlike its European counterpart, “was organized so as to bring the same information to the door of the poor man’s cottage and to the gate of the palace.” To live up to this idealistic ethos, hards must be treated no differently than easies.'
href="https://logicmag.io/distribution/the-nonmachinables/"
versionurl="https://web.archive.org/20220201040825/https://logicmag.io/distribution/the-nonmachinables/"
versiondate="2022-02-01 03:26:56+00:00"
anchor="The Nonmachinables: Redundancy and resilience at the US Postal Service"
post=', Logic Magazine, 17-May-2021'
%}

This is a long read about a much bigger subject. 
Despite the length—just over 5,000 words—I came away with the feeling that it was just scratching the surface. 
It is a review of the tasks that postal workers undertook to deliver the mail and how spurts of automation at key times overtook those person-oriented tasks. 
What started as the "Bureau of Hards" turns into the "Remote Encoding Center" where pictures of mailpieces that the automation can't handle meet the human eyes that try to puzzle out the address marked on an errant mail piece.
And in the end, it is not the "chicken scratchings" of handwritten envelopes that trip up the optical character recognition software. 
No, the software has gotten quite good at that. (The article describes the long path to how it got that good.)
It is the "bottomless pile of machine-printed detritus, much of it cheaply printed junk mail slung by mass marketeers."

## Sympathy for Mittens
{: mittens-leg}

{% include image.html wpsrc="2022/2022-02-10-mittens-shaved-leg.jpg" float="right" width="320" alt="Photograph of a black cat with white streaks with her left front leg showing a shaved portion near her paw" caption="Mittens' shaved leg" %}  This week Mittens was at the vet for teeth cleaning and inspection. 
One of her teeth had "root reabsorption" and disappeared. 
She needed general anesthesia, of course, for the cleaning...hence the shaved leg.

Alan pretends he is weak from hunger in the background.