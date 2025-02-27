---
title: 'Issue 109: Generative AI in Libraries'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- LLMs in libraries
- WorldCat
summary: "This week's Thursday Threads is on generative AI in libraries, with projects by OCLC, JSTOR, EBSCO, Clarivate, and ProQuest. OCLC's AI model is removing duplicate WorldCat records. JSTOR and EBSCO explored AI tools for article summaries and research questions. Clarivate's survey highlighted AI as a library priority but noted concerns about skills and budgets. Ed Summers critiqued AI's biases, legal issues, and environmental impact, urging responsible use in libraries."
bluesky: "Thursday Threads this week: Libraries are integrating generative AI. OCLC's AI removed WorldCat duplicates; JSTOR and EBSCO tested AI summaries. Clarivate's survey found AI adoption vital but raised concerns. Ed Summers outlines AI's problem areas, urging careful use."
---

"Artificial Intelligence" is a vast field of study, and today's focus on generative AI is just the latest evolution of that field. 
It wasn't too long ago that the focus was on "big data" — large and complex blocks of information for everything from social media, environmental sensor output, payment transactions, and even bibliographic data. 
It was 15 years ago that the excitement was about clustering data to get insights about the books in our collections. 
(See this [DLTJ summary of talks by OCLC, Open Library, and Google Book Search]({filename}2010-01-27-mashups-of-bib-data/) at the ALA Midwinter conference in 2010.)
Now, "big data" isn't so big anymore, and in fact, it has become the input to the generative AI models that we hear about in the news today.
While "big data" was about understanding and interpreting past data, "generative AI" uses those learnings to create new data... a shift from analysis to synthesis in artificial intelligence.

So this week's _DLTJ Thursday Threads_ is looking at the application of generative AI — sometimes called "large language models" or "foundational models" as a more descriptive term for the technology — in libraries.

- OCLC is using machine learning models for [detecting duplicate records]({filename}#oclc).
- JSTOR tries out [generative AI features in its journal article database]({filename}jstor).
- EBSCO tries out [generative AI features in its discovery products]({filename}#ebsco).
- Clarivate [surveys libraries worldwide about generative AI]({filename}#clarivate).
- ProQuest [introduces generative AI features in its ebooks]({filename}#proquest).
- [What to consider]({filename}#edsu) when you are considering AI for your library.
- [This Week I Learned]({filename}#twil): There are now 23 Dark Sky Sanctuaries in the world.
- [This week's cat]({filename}#cats)

{{ thursday_threads_header() }}



## OCLC is using machine learning models for detecting duplicate records {: #oclc}
{{ thursday_threads_quote(href="https://www.oclc.org/en/news/announcements/2025/ai-worldcat-deduplication.html",
 blockquote='In August 2023, we implemented our first machine learning model for detecting duplicate bibliographic records as part of our ongoing efforts to mitigate and reduce their presence in WorldCat. In the lead up to this, we had invited the cataloging community to participate in data labeling exercises, from which we received feedback from over 300 users on approximately 34,000 duplicates to help validate our model’s understanding of duplicate records in WorldCat. This initiative led to the removal of ~5.4 million duplicates from WorldCat for printed book materials in English and other languages like French, German, Italian, and Spanish. We’ve now enhanced and extended our AI model to de-duplicate all formats, languages, and scripts in WorldCat. Leveraging the labeled data collected from community participation, we’ve tuned and optimized the AI machine learning algorithm, completed extensive internal testing, and engaged WorldCat Member Merge libraries to provide external verification of the algorithm’s performance. ',
 versiondate="2025-02-05",
 versionurl="https://web.archive.org/20250205194709/https://www.oclc.org/en/news/announcements/2025/ai-worldcat-deduplication.html",
 anchor="Implementing AI to further scale and accelerate WorldCat de-duplication",
 post=", OCLC, 4-Feb-2025") }}

For my non-library friends who don't know about OCLC, it is a cooperative utility used by libraries to get descriptions of items purchased by the library. 
(Broadly speaking...librarian friends: please don't come after me for the simplification.)
As an effort where thousands of libraries have entered data for millions of books across 60 years, there were bound to be duplicate or near-duplicate records. 
All of the easy duplications have been found and merged. 
But in a quest for perfection—a journey that a cataloging librarian will argue is never-ending—there is always more cleanup to be done. 
Interesting to see OCLC bringing machine learning models to the task. 
Their earlier work would have fallen into the "big data" category I mentioned earlier. 


## JSTOR tries out generative AI features in its journal article database {: #jstor}
{{ thursday_threads_quote(href="https://www.cni.org/topics/information-access-retrieval/navigating-generative-artificial-intelligence-early-findings-and-implications-for-research-teaching-and-learning",
 blockquote='This is an article that we&apos;re looking at and you can see up at the top I&apos;ve run a search. The search is "what are characteristics of Gothic literature". And on the side you see we have this new chat box where the user can engage with the content. And this very first action—the user doesn&apos;t have to do anything—they land on the page and as long as they run a search, we immediately process a prompt
that says: "how is—the query you put in...so &lsquo;what are the characteristics of Gothic literature&rsquo;—related to this text? And the response comes back: "The characteristics of Gothic literature include evoking fear, et cetera." So it gives you a custom response...a custom summary of the document that tells you basically "Why did I get this response? Why did I get this article?" And here what it actually has to do with your research task.',
 versiondate="2025-02-26",
 versionurl="https://web.archive.org/20240916101146/https://www.ebsco.com/blogs/ebscopost/AI-insights-library-research",
 anchor="AI in Library Research Platforms: Findings from EBSCO's Recent Beta Release",
 post=", CNI Spring Meeting 2024, 9-May-2024") }}

This is a recording of a presentation at the Spring 2024 member meeting of the Coalition for Networked Information. 
The presenter, Beth LaPensee, Senior Product Manager at ITHAKA, is demonstrating a user interface prototype for JSTOR that integrates language models into their journal article database. 
They have developed a beta research assistant tool with features like article summaries, related content recommendations, and question-answering capabilities. 
The prototype focused on helping users deeply engage with and understand the content of individual articles rather than searching across the entire corpus. 
The quote above comes from a point about [12 minutes into the presentation](https://hyp.is/MkWjXBxxEe-W33MzbwmJjg/media.dltj.org/annotated-video/20240527T172152-SE4zl7Isy5k-navigating-generative-ai-early-findings-implications-research-teaching-learning/index.html). 
The team has gathered user feedback and data on how students, researchers, and instructors used the tool, finding that the question-answering and summary features are particularly popular. 
I haven't heard whether this prototype has left the development stage and is heading to the production JSTOR user interface.


## EBSCO tries out generative AI features in its discovery products {: #ebsco}
{{ thursday_threads_quote(href="https://www.ebsco.com/blogs/ebscopost/AI-insights-library-research",
 blockquote='EBSCO AI Insights is a Generative AI feature that summarizes 3-5 key points of an article, helping users quickly assess its relevance. Accessible via a button on EBSCO’s interface for EBSCO Discovery Service and the EBSCOhost research platform, it complements abstracts and subject headings. Insights are marked as AI-generated, with a disclaimer urging users to verify their accuracy before use.',
 versiondate="2024-09-16",
 versionurl="https://web.archive.org/20240916101146/https://www.ebsco.com/blogs/ebscopost/AI-insights-library-research",
 anchor="AI in Library Research Platforms: Findings from EBSCO's Recent Beta Release",
 post=", EBSCO, 4-Sep-2024") }}

EBSCO is testing and developing AI features for its library research platforms: EBSCO Discovery Service (EDS) and EBSCOhost. 
One feature is AI Insights, which uses generative AI to provide 3-5 key point summaries of articles to help users quickly assess relevance. 
Lat year, EBSCO conducted a beta test of AI Insights with 50 libraries and received mixed feedback, with some users finding it very helpful but others concerned about accuracy, especially for referential materials like reviews. 
EBSCO took that feedback and said they were working on a new version. 
As of yet, I haven't read an announcement of it coming out again...its {{ robustlink(href="https://www.ebsco.com/artificial-intelligence/products/ai-insights", versionurl="https://web.archive.org/web/20250227005319/https://www.ebsco.com/artificial-intelligence/products/ai-insights", versiondate="2025-02-26", title="AI Insights: Streamline the Research Process with AI | EBSCO", anchor="product page") }} says "coming soon".


## Clarivate surveys libraries worldwide about generative AI {: #clarivate}
{{ thursday_threads_quote(href="https://clarivate.com/pulse-of-the-library/",
 blockquote='The quickening pace of technological advancement, in particular generative artificial intelligence (GenAI), is reshaping the landscape for all. Librarians now find themselves at a pivotal juncture. The question is no longer whether to embrace AI but rather what to adopt and how to do so responsibly. Embracing technological change is not new for librarians, as libraries continue to be bastions of knowledge and learning, evolving their operations and transforming user experiences. Clarivate is deeply invested in the future of libraries. To this end, we conducted a survey of academic, public and national librarians from around the world and are sharing the results. Our aim was to assess current and expected trends and measure the impact of technologies, including AI, on librarians and their communities. In addition to the survey, we conducted several qualitative interviews with librarians from diverse organizations. This report examines the results of our investigation, spotlighting the concerns of librarians and the opportunities they see as they continue to champion their role in advancing the knowledge frontier.',
 versiondate="2024-09-16",
 versionurl="https://web.archive.org/20240916101149/https://clarivate.com/pulse-of-the-library/",
 anchor="Pulse of the Library 2024",
 post=", Clarivate, undated—circa September 2024") }}

Clarivate conducted a global survey of academic, public, and national librarians to gauge current and expected trends of generative AI in libraries. 
The survey found that 60% of libraries are evaluating or planning for AI integration, with AI adoption being the top technology priority. 
Key goals for AI adoption include supporting student learning, research excellence, and content discoverability. 
However, librarians have concerns about AI, including skills gaps, tight budgets, and potential job displacement. 

The link above is to the summary, and the 21-page report is linked from there. 
This survey was likely conducted in the early stages of awareness of generative AI, so I'd take its findings with a grain of salt. 
Even a year later, we're still figuring out whether this technology is useful and its real costs.


## ProQuest introduces Ebook Central Research Assistant {: #proquest}
{{ thursday_threads_quote(href="https://about.proquest.com/en/blog/2025/introducing-proquest-ebooks-the-worlds-largest-scholarly-ebook-subscription/",
 blockquote='Access to broad, vetted academic content also serves another purpose: it ensures the ability of academic AI tools to deliver reliable outputs. AI-powered chatbots are becoming ubiquitous as a method of discovery for students and researchers, but not all are created equal—potentially exposing students to dangers such as bias and content hallucinations. To address these concerns, we are also launching the Ebook Central Research Assistant, a tool powered by our Academic AI technology backbone, that guides students to effectively assess the relevance of each book, helping to review, analyze, and explore new ideas with ease. ProQuest Ebooks is enhanced with the Ebook Central Research Assistant, meaning students can expect reliable outputs on high-quality scholarly content with instant chapter insights, key concepts, and features that create deeper learning and enrich the research process.',
 versiondate="2025-02-21",
 versionurl="https://web.archive.org/web/20250221011929/https://about.proquest.com/en/blog/2025/introducing-proquest-ebooks-the-worlds-largest-scholarly-ebook-subscription/",
 anchor="Introducing ProQuest Ebooks, the world’s largest scholarly ebook subscription",
 post=", ProQuest, 18-Feb-2025") }}

ProQuest is a division of Clarivate, so it would seem that the company put some of what it learned in the survey mentioned above into its product line. 
This quoted bit was most of the way down a press release describing changes to how ProQuest offers content to libraries. 
Generative AI was just a part of the press release, though, and there has been {{ robustlink(href="https://www.uksg.org/newsletter/uksg-enews-582/opinion-a-librarians-summary-of-and-response-to-the-clarivate-announcement/", versionurl="https://web.archive.org/20250225021528/https://www.uksg.org/newsletter/uksg-enews-582/opinion-a-librarians-summary-of-and-response-to-the-clarivate-announcement/", versiondate="2025-02-25", title="A librarian's summary of, and response to, the Clarivate announcement | UKSG Newsletter", anchor="considerable pushback from the library community") }} about the ProQuest's change from selling content to libraries to this new subscription service. 
I would beg to differ if they thought they found the "pulse of the libraries" in their survey last year.


## What to consider when your are considering AI for your library {: #edsu}
{{ thursday_threads_quote(href="https://inkdroid.org/2024/03/12/ai/",
 blockquote='I was asked to participate in a panel at work about AI. I initially declined, but once it became clear that I would be allowed to get on my soapbox and rant for 15 minutes I agreed. Below are my notes and some slides. This was not a fun post to write or present. I’m sure it rubbed some people the wrong way, and I am genuinely sorry for that.',
 versiondate="2024-03-17",
 versionurl="https://web.archive.org/20240317032258/https://inkdroid.org/2024/03/12/ai/",
 anchor='Some things to consider when deciding whether to start building with "AI" in libraries and archive',
 post=", Ed Summers, 12-Mar-2024") }}

Ed calls for a critical evaluation of AI technologies, particularly Large Language Models (LLMs), which reflect societal biases and may perpetuate systemic racism due to the data they are trained on. 
He also points out the intellectual property issues from using copyrighted materials in training these models, which challenge the existing web ecosystem and potentially harm content creators. 
Verifiability is another major concern because we don't understand how these models generate their answers. 
The impact of AI on employment is addressed, with worries that it may replace skilled workers with lower-paid roles focused on managing AI outputs. 
Environmental sustainability is also a pressing issue, as AI technologies consume significant energy resources, raising questions about their long-term viability. 
Security and privacy concerns are highlighted, particularly the potential for AI to generate disinformation and compromise user data. 
Ed concludes by urging libraries and archives to adopt responsible practices while evaluating AI tools, ensuring transparency, and advocating for user data rights.
Sound advice for libraries...or any profession!


## This Week I Learned: There are now 23 Dark Sky Sanctuaries in the World {: #twil}
{{ thursday_threads_quote(href="https://www.nytimes.com/2025/02/24/science/astronomy-dark-sky-rum.html",
 blockquote='Rum, a diamond-shaped island off the western coast of Scotland, is home to 40 people. Most of the island — 40 square miles of mountains, peatland and heath — is a national nature reserve, with residents mainly nestled around Kinloch Bay to the east. What the Isle of Rum lacks is artificial illumination. There are no streetlights, light-flooded sports fields, neon signs, industrial sites or anything else casting a glow against the night sky. On a cold January day, the sun sets early and rises late, yielding to a blackness that envelopes the island, a blackness so deep that the light of stars manifests suddenly at dusk and the glow of the moon is bright enough to navigate by.',
 versionurl="https://web.archive.org/web/20250227022717/https://www.nytimes.com/2025/02/24/science/astronomy-dark-sky-rum.html", 
 versiondate="2025-02-26", 
anchor="Take a Look: A Dark Scottish Isle Where Starlight Reigns Supreme",
post=', New York Times, 24-Feb-2025') }}

The pictures that accompany this article from the New York Times are stunning ([gift link](https://www.nytimes.com/2025/02/24/science/astronomy-dark-sky-rum.html?unlocked_article_code=1.0E4.vEP7.52N9PTn4ZqOV&smid=url-share)). 
And to think that there are only 23 places in the world that have reached this level of commitment to the environment.

What did you learn this week? Let me know on [Mastodon](https://code4lib.social/@dltj/) or [Bluesky](https://bsky.app/profile/dltj.org/).


## Alan is waiting for spring {: #cats}
{{ image(width="600", localsrc="2025/2025-02-27-alan.jpg", alt="White and gray cat lounging on a person's lap, with its head resting on the denim-clad leg and paw draped comfortably over the side.") }} 
