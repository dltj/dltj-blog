---
title: 'Issue 106: How much do you know about the credit card industry?'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- consumer finance
- computing history
mastodon: In this week's Thursday Threads, be prepared to voyage into the maze of the credit card industry. This issue explores the $130 billion in processing fees, the role of merchants, and the ripple effects of your spending habits on reward systems. We dive into data monetization, the anxiety-inducing world of debt collection, and contemplate ExTwitter's "everything app" aspirations. And yes, there's a cat picture.
bluesky: Discover the credit card industry's secrets in this week's DLTJ Thursday Threads. Explore processing fees, merchant struggles, reward systems, data monetization, debt collection, and ExTwitter's "everything app" ambition. As always, a cat picture!

---
With millions of digital transactions taking place every day, have you ever wondered about the complex world behind your simple card swipe? 
In this week's _Thursday Threads_, we delve into the multi-layer maze that is the credit card industry. 
Grappling with $130 billion in fees, merchants are the invisible heroes who bear the cost of our seamless payment experience. 
As we unravel this thread, we'll dissect the structure of these processing fees, explain how your spending fuels reward systems, and describe the ongoing antitrust battle between credit card processors and merchants. 
We'll also see what your credit card issuer knows about your spending habits, bringing to light the monetization of these insights. 
Delving into murkier waters, we'll explore the shadow realm of debt collection and the distress it can cause to consumers. 
And to wrap up, are we ready for (X)Twitter to become our "everything app"?
Plus, one thing I learned this week and a cat picture.

- Did you know credit card companies take in $130 billion in fees? And the invisible-to-the-consumer payer of those fees? [Merchants]({filename}#merchants).
- That ["swipe fee" has two parts]({filename}#fees): a 5¢ to 10¢ fixed fee and a percentage of the charged amount ranging from 1% to 3%.
- That higher percentage fee of the amount you charge on your credit card likely goes to pay for [credit card rewards]({filename}#rewards).
- For 20 years, merchants have been [fighting an antitrust battle]({filename}#settlement) with credit card processors about increases in the fees they are paying.
- Have you stopped to think about how much your credit card issuer knows about you based on what you buy and where? [The card issuer has]({filename}#data).
- Mastercard sells your purchase history to advertisers, and [you can opt out]({filename}#mastercard-data).
- Not all credit card accounts are repaid. [The dark world of debt collection]({filename}#collections) is the result.
- [ExTwitter is adding digital wallet functionality]({filename}#extwitter). In case you want that company to be more involved in your everyday life.
- [This Week I Learned]({filename}#twil): The origin of the computer term "mainframe" comes from "main frame" — the 1952 name of an IBM computer's central processing section.
- [This week's cat]({filename}#cats)

{{ thursday_threads_header() }}


## Who pays for credit card operations? Merchants {: #merchants}
{{ thursday_threads_quote(href="https://prospect.org/power/2023-02-07-small-business-credit-card-fees/",
 blockquote='Today, small businesses face another attack, this time from Wall Street. Reynolds’s main concern is now swipe fees, which are the fees credit and debit card networks charge merchants for processing transactions. For over a decade, Reynolds and his colleagues on Main Streets around the country have watched their monthly billing statements climb because of these fees. In 2021, big banks, in coordination with the two credit card behemoths, Visa and Mastercard, took in over $130 billion from swipe fees (also called interchange fees), more than double what they reaped in 2010.',
 versiondate="2024-03-31",
 versionurl="https://web.archive.org/20240331212955/https://prospect.org/power/2023-02-07-small-business-credit-card-fees/",
 anchor="Small Businesses Rise to Fight Wall Street",
 post=", The American Prospect, 7-Feb-2023") }}
 
The article highlights the growing mobilization of small businesses against the rising swipe fees imposed by credit card companies Visa and Mastercard. 
These fees have increased significantly, costing small retailers more than utilities and approaching their labor costs. 
The article describes the struggles of small business owners who, after recognizing their shared challenges during the pandemic, formed groups like the Merchants Payments Coalition to advocate for reform. 
The campaign aims to replicate the success of the Durbin amendment, which previously capped debit card fees, by pushing for the {{ robustlink(href="https://www.govtrack.us/congress/bills/118/hr3881", versionurl="https://web.archive.org/web/20250111045641/https://www.govtrack.us/congress/bills/118/hr3881", versiondate="2025-01-11", title="Credit Card Competition Act of 2023 (2023; 118th Congress H.R. 3881) | GovTrack.us", anchor="Credit Card Competition Act") }} to do the same for credit transactions. 
(You might remember the Credit Card Competition Act...it was the target of blanket advertising in 2023 along the lines of how Congress wants to take away your credit card rewards.)
Well, how much are the fees we're talking about...


## What are the fees? {: #fees}
{{ thursday_threads_quote(href="https://www.fool.com/money/research/average-credit-card-processing-fees-costs-america/",
 blockquote='In 2023, credit card companies in the U.S. earned $135.75 billion from processing fees charged to merchants. Families paid an average of $1,102 in swipe fees in 2023, according to the Merchants Payments Coalition. The money made from these fees increased at a faster rate than the actual money spent on purchases, adding fuel to the already fierce debate between credit card companies and businesses that complain about so-called swipe fees. Businesses claim that raising interchange fees, which are paid by merchants on each transaction made with a credit or debit card, worsen inflation and pinch consumers because businesses could opt to pass the cost of higher interchange fees onto consumers. Most merchants need to accept credit card payments, which makes credit card processing fees a cost of doing business. For more on how much those costs can be -- and how they vary among credit card companies -- we&apos;ve collected all the latest data.',
 versiondate="2025-02-06",
 versionurl="https://web.archive.org/web/20250118112651/https://www.fool.com/money/research/average-credit-card-processing-fees-costs-america/",
 anchor="Average Credit Card Processing Fees and Costs in 2024",
 post=", The Motley Fool, 10-Dec-2024") }}

Have you ever been charged an extra fee by a company for using a credit card? 
It is not common, but it does happen, and it is because the company has been charged a fee to accept the card. 
That is called the "interchange fee". 
This table is from the article quoted above:

| Payment network	| Average credit card processing fees	|  
| ----------------	| -----------------------------------	|  
| Visa	| 1.23% + $0.05 to 3.15% + $0.10	|  
| Mastercard	| 1.15% + $0.05 to 3.15% + $0.10	|  
| American Express	| 1.10% + $0.10 to 3.15% + $0.10	|  
| Discover	| 1.56% + $0.10 to 2.40% + $0.10   |

The range—1.23% to 3.15%, in the case of Visa—is based on a few factors:

1. **Merchant category**: the type of business
1. **Card tier**: the level of rewards a card offers, or no reward at all
1. **Processing method**: whether a card was swiped, dipped, tapped, keyed manually, or used online

One of the significant factors is card tier, which leads us to ask:


## Why are banks eager to push the higher-fee rewards cards? {: #rewards}
{{ thursday_threads_quote(href="https://www.bitsaboutmoney.com/archive/anatomy-of-credit-card-rewards-programs/",
 blockquote='To highlight something which is routinely surprising for non-specialists: interchange fees [the fees paid by the card-accepting business, or "merchant"] are not constant and fixed. They are set based on quite a few factors but, most prominently, based on the rank of card product you use. The more a card product is pitched to socioeconomically well-off people, the more expensive interchange is. Credit card issuers explicitly and directly charge the rest of the economy for the work involved in recruiting the most desirable customers.',
 versiondate="2024-04-04",
 versionurl="https://web.archive.org/20240404030931/https://www.bitsaboutmoney.com/archive/anatomy-of-credit-card-rewards-programs/",
 anchor="Anatomy of a credit card rewards program",
 post=", Bits About Money, 29-Mar-2024") }}

The author of this article was a technology executive at Stripe and now makes a living doing consulting and writing blog posts.
The article delves into the mechanics behind credit card rewards, emphasizing the role of interchange fees, which are paid by businesses accepting credit cards and distributed among various parties in the credit ecosystem. 
It explains that credit card issuers use these fees to attract high-value customers by offering rewards programs that enhance the spending experience. 
The discussion highlights that not all cards offer rewards, with some cards targeting lower-income users primarily to provide access to credit rather than rewards.
If you want a more in-depth view of how credit cards work, I recommend the author's {{ robustlink(href="https://www.bitsaboutmoney.com/archive/improving-cards-under-the-hood/", versionurl="https://web.archive.org/20230402212021/https://www.bitsaboutmoney.com/archive/improving-cards-under-the-hood/", versiondate="2023-04-02", title="Improving how credit cards work under the covers | Bits about Money", anchor="Improving how credit cards work under the covers") }}.


## Interchange settlement {: #settlement}
{{ thursday_threads_quote(href="https://www.creditslips.org/creditslips/2024/03/the-proposed-credit-card-interchange-settlement.html",
 blockquote='...on every credit card transaction in the MasterCard and Visa systems, the merchant pays a swipe fee, also known as the merchant discount fee. That fee is paid to the merchant&apos;s bank. The merchant&apos;s bank then pays a "network fee" to MC or V and also pays an "interchange" fee to the bank that issued the card. The interchange fee is not one-size-fits-all. Instead, it varies by merchant type (and sometimes volume) and by the level of rewards/service on the card. So merchants are not directly charged the interchange fee, but it is passed through to them, sometimes explicitly. The problem that merchants face is that they cannot exert any pressure on the interchange fee—nominally an interbank fee—even though it is set based on their line of business.  Nor can merchants discriminate among types of credit cards by charging more for rewards cards, etc.',
 versiondate="2024-03-31",
 versionurl="https://web.archive.org/web/20240331200829/https://www.creditslips.org/creditslips/2024/03/the-proposed-credit-card-interchange-settlement.html",
 anchor="The Proposed Credit Card Interchange Settlement",
 post=", Credit Slips, 24-Mar-2024") }}

Twenty years ago, merchants {{ robustlink(href="https://www.courtlistener.com/docket/4318960/in-re-payment-card-interchange-fee-and-merchant-discount-antitrust/?filed_after=&filed_before=&entry_gte=&entry_lte=&order_by=desc", versionurl="", versiondate="2025-02-05", title="In re Payment Card Interchange Fee and Merchant Discount Antitrust Litigation, 1:05-md-01720 | CourtListener", anchor="sued") }} the credit card companies alleging anti-trust violations about this scheme, and the case is still going on. 
If the "Credit Card Competition Act" isn't re-introduced to Congress, maybe merchants can get relief from the court system.


## How much does the credit card company know about you? {: #data}
{{ thursday_threads_quote(href="https://www.nytimes.com/2009/05/17/magazine/17credit-t.html",
 blockquote='A 2002 study of how customers of Canadian Tire were using the company&apos;s credit cards found that 2,220 of 100,000 cardholders who used their credit cards in drinking places missed four payments within the next 12 months. By contrast, only 530 of the cardholders who used their credit cards at the dentist missed four payments within the next 12 months.',
 versiondate="2025-02-05",
 versionurl="https://web.archive.org/20250205010946/https://www.nytimes.com/2009/05/17/magazine/17credit-t.html",
 anchor="What Does Your Credit-Card Company Know About You?",
 post=", New York Times, 12-May-2009") }}

Credit card use is increasing, and the aggregation of all that data can be a goldmine of information about people. 
A study showed that purchasing habits could predict payment reliability, with certain products indicating a higher likelihood of missed payments. 
And analysis of that data drives the efforts by banks to get you to use their higher reward cards. 
There is also the world of "{{ robustlink(href="https://www.tidalcommerce.com/learn/what-is-level-3-data", versionurl="https://web.archive.org/web/20250128063022/https://www.tidalcommerce.com/learn/what-is-level-3-data", versiondate="2025-02-05", title="What Is Level 3 Data? Everything You Need to Know | Tidal Commerce", anchor="Level 3 Data") }}", where merchants transmit line items about your purchases to the credit card processor. 
Think of it as: every line on grocery receipt. 
Except, as near as I can tell, it Level 3 data doesn't apply to consumer credit cards...only to business-to-business and government-to-business cards. 
Still, it is an interesting fact to know and perhaps something to keep an eye on in case it leaks into the consumer credit card space.


## Exercising control of your data at Mastercard {: #mastercard-data}
{{ thursday_threads_quote(href="https://pirg.org/edfund/resources/mastercard-data-tips-guide/",
 blockquote='When you use your Mastercard, the company receives data about your transaction, like how much you spent, where and on what day. It needs this information to be your credit card – but Mastercard doesn&apos;t just use your data to complete payments. It monetizes that information by selling it to data brokers, advertisers and other companies. Mastercard&apos;s data practices contribute to a larger economy of data harvesting and data sales that can be harmful to consumers.',
 versiondate="2024-01-28",
 versionurl="https://web.archive.org/20240128230931/https://pirg.org/edfund/resources/mastercard-data-tips-guide/",
 anchor="How to take more control of your Mastercard transaction data",
 post=", PIRG, 21-Sep-2023") }}

Mastercard has a program to monetize transaction data by selling it to advertisers. 
This PIRG article has details and a link to the opt-out page on Mastercard's website. 
Visa used to have a similar program — Visa Advertising Solutions — but it was {{ robustlink(href="https://www.marketingbrew.com/stories/2021/09/13/visa-shutting-personal-data-business-advertisers", versionurl="https://web.archive.org/web/20241221012611/https://www.marketingbrew.com/stories/2021/09/13/visa-shutting-personal-data-business-advertisers", versiondate="2025-02-05", title="Visa is shutting down its personal data business for advertisers | Marketingbrew", anchor="shut down in 2021") }}.


## Credit card collections {: #collections}
{{ thursday_threads_quote(href="https://www.bitsaboutmoney.com/archive/the-waste-stream-of-consumer-finance/",
 blockquote='One interesting lens for understanding how industries work is looking at their waste streams. Every industry will by nature have both a stock and a flow of byproducts from their core processes. This waste has to be dealt with (or it will, figuratively or literally, clog the pipes of the industry) and frequently has substantial residual value. Most industries develop ecosystems in miniature to collect, sift through, recycle, and dispose of their waste. These are often cobbled together from lower-scale businesses than the industry themselves, involve a lot of dirty work, and are considered low status. Few people grow up wanting to specialize in e.g. sales of used manufacturing equipment. One core waste stream of the finance industry is charged-off consumer debt. Debt collection is a fascinating (and frequently depressing) underbelly of finance. It shines a bit of light on credit card issuance itself, and richly earns the wading-through-a-river-of-effluvia metaphor.',
 versiondate="2023-08-12",
 versionurl="https://web.archive.org/20230812150844/https://www.bitsaboutmoney.com/archive/the-waste-stream-of-consumer-finance/",
 anchor="Credit card debt collection",
 post=", Bits About Money, 11-Aug-2023") }}

Back to _Bits About Money_ for a view on the opposite side of credit card rewards: credit card debt collection. 
Most defaulted debt in the U.S. is from credit cards, and the lifecycle of that debt involves a series of internal and external processes before they are sold to debt buyers, often at a fraction of their original value. 
He notes that most debt collectors operate in high-pressure environments, leading to high turnover rates, a lack of professionalism, and widespread illegal practices. 
He also discusses how debt collectors rely on automated systems and predictive dialing to maximize efficiency, often leading to a barrage of calls to debtors. 
Many consumers are unaware of their legal rights and don't have time to fight against these tactics effectively.


## ExTwitter adding digital wallet functionality {: #extwitter}
{{ thursday_threads_quote(href="https://www.cnbc.com/2025/01/28/elon-musk-x-visa-digital-wallet.html",
 blockquote='Elon Musk&apos;s social media platform X on Tuesday announced the launch of a digital wallet and peer-to-peer payments services provided by Visa. X struck a deal with Visa, the largest U.S. credit card network, to be the first partner for what it is calling the X Money Account, CEO Linda Yaccarino announced in a post on the platform. Visa will enable X users to move funds between traditional bank accounts and their digital wallet and make instant peer-to-peer payments, Yaccarino said, like with Zelle or Venmo.',
 versiondate="2025-02-05",
 versionurl="https://web.archive.org/20250205020939/https://www.cnbc.com/2025/01/28/elon-musk-x-visa-digital-wallet.html",
 anchor="Elon Musk’s X partners with Visa to offer digital wallet",
 post=", CNBC, 28-Jan-2025") }}

When Elon Musk bought Twitter, he said he wanted the company to turn into an "everything app" — use Twitter to buy things online, call for a taxi, and make peer-to-peer payments. 
One of the first steps on that path is getting access to payment systems. 
Now, whether you trust Musk with that kind of access to your bank accounts is an entirely separate matter...


## This Week I Learned: The origin of the computer term "mainframe" comes from "main frame" — the 1952 name of an IBM computer's central processing section {: #twil}
{{ thursday_threads_quote(href="https://www.righto.com/2025/02/origin-of-mainframe-term.html",
 blockquote='Based on my research, the earliest computer to use the term "main frame" was the IBM 701 computer (1952), which consisted of boxes called "frames." The 701 system consisted of two power frames, a power distribution frame, an electrostatic storage frame, a drum frame, tape frames, and most importantly a main frame.',
 versiondate="2025-02-06",
 versionurl="https://web.archive.org/20250206065935/https://www.righto.com/2025/02/origin-of-mainframe-term.html",
 anchor="The origin and unexpected evolution of the word 'mainframe'",
 post=", Ken Shirriff's blog, 1-Feb-2025") }}

"Mainframe" is such a common word in my lexicon that it didn't occur to me that its origins was from "main frame" — as in the primary frame in which everything else connected.
I've heard "frame" used to describe a rack of telecommunications equipment as well, but a quick [Kagi search](https://kagi.com/search?q=what+is+the+origin+of+the+telecommunications+word+%22Frame%22%3F&r=us&sh=S1wjO-hCWatv4U-FDqKamg) couldn't find the origins of the word "frame" from a telecom perspective.

What did you learn this week? Let me know on [Mastodon](https://code4lib.social/@dltj/113957049724787035) or [Bluesky](https://bsky.app/profile/dltj.org/post/3lhj5alcywe26).

## Mittens explores the toilet {: #cats}
 {{ image(width="600", localsrc="2025/2025-02-06-mittens-toilet.jpg", alt="Black cat curiously leans into an open toilet bowl, with its head hidden and tail extended in a bathroom setting.") }} 
