---
title: 'Issue 113: More on Copyright and Foundational AI Models'
modified: 2025-03-29
category: Thursday Threads
categories:
- Thursday Threads
tags:
- copyright
- large language model
summary: "In Thursday Threads this week: key legal cases and corporate actions on using copyrighted materials in AI training, emphasizing growing tensions between creators and tech companies as AI increasingly utilizes large licensed and some pirated datasets."
bluesky: "This week's Thursday Threads article provides an overview of several high-profile legal cases and corporate initiatives surrounding the use of copyrighted materials in training artificial intelligence (AI) models. These cases highlight the growing tension between content creators and technology companies as AI technologies increasingly rely on large datasets that include licensed and, in some instances, pirated content. Plus a cat picture."
---
Two years ago this month, I wrote a _DLTJ Thursday Threads_ article on the [copyright implications of foundational AI models]({filename}2023-03-02-issue-99-copyright-and-ai). 
A lot has happened in those 24 months. 
This issue mostly focuses on lawsuits, plus an announcement of a service offering image generation from licensed content.
These articles highlight the growing tension between content creators and technology companies as AI technologies increasingly rely on large datasets that include licensed and, in some instances, pirated content.

- From late 2023, the [New York Times sues OpenAI and Microsoft]({filename}#nytimes) for alleged copyright infringement in AI training (with late-breaking update).
- U.S. judge partially favors OpenAI while [permitting unfair competition claim]({filename}#openai) in authors' copyright lawsuit in this ruling from early 2024. 
- Last month Thomson Reuters [wins landmark U.S. AI copyright case]({filename}#thomson-reuters), potentially establishing a legal precedent.
- Microsoft [guarantees legal protection for Copilot users]({filename}#microsoft) from copyright lawsuits.
- Meta's training of its AI with pirated LibGen books [sparks legal and ethical debate]({filename}#meta).
- [Nvidia denies copyright infringement]({filename}#nvidia) in the use of shadow libraries for AI training.
- Getty Images launched an [AI image generator]({filename}#getty) using its licensed library in 2023.
- [This Week I Learned]({filename}#twil): "But where is everybody?!?" — the origins of Fermi's Paradox
- [This week's cat]({filename}#cats)

Also on DLTJ this past week:

- [In OCLC v Anna's Archive, New/Novel Issues Sent to State Court]({filename}2025-03-21-oclc-v-annasarchive-certified-to-ohio-court): The case of OCLC against Anna's Archive, accused of “data scraping” from OCLC's WorldCat, takes a turn as the U.S. District Court for the Southern District of Ohio decides to certify several “novel and unsettled” legal questions to the Supreme Court of Ohio.
- [My protest signage improved at this week's #TeslaTakedown]({filename}2025-03-22-tesla-takedown-march-22): My improved sign said "Our GOVERNMENT was fine. Now it is MUSKed UP! FIRE ELON!" Read the post for instructions on printing your own copy of this protest sign.

{{ thursday_threads_header() }}



## New York Times sues OpenAI and Microsoft for alleged copyright infringement in AI training {: #nytimes}
{{ thursday_threads_quote(href="https://www.washingtonpost.com/technology/2023/12/27/new-york-times-sues-openai-chatgpt/",
 blockquote='The New York Times sued OpenAI and Microsoft on Wednesday over the tech companies’ use of its copyrighted articles to train their artificial intelligence technology, joining a growing wave of opposition to the tech industry’s using creative work without paying for it or getting permission. OpenAI and Microsoft used “millions” of Times articles to help build their tech, which is now extremely lucrative and directly competes with the Times’s own services, the newspaper’s lawyers wrote in a complaint filed in federal court in Manhattan.',
 versiondate="2023-12-28",
 versionurl="https://web.archive.org/20240101002545/https://www.washingtonpost.com/technology/2023/12/27/new-york-times-sues-openai-chatgpt/",
 anchor="New York Times sues OpenAI, Microsoft for using articles to train AI",
 post=", Washington Post, 27-Dec-2023") }}
 
We're starting with the lawsuits, and this is one of the bigger ones. 
At the time the lawsuit was filed, OpenAI announced deals with content providers to use their backfiles of content, but the New York Times was a holdout. 
The lawsuit claims that OpenAI and Microsoft used millions of Times articles, which directly competes with the newspaper's services. 
While OpenAI maintained that it respects content creators' rights and believes its practices fall under fair use, the lawsuit cites instances of AI reproducing Times articles verbatim. 
This case has had many twists and turns, including a {{ robustlink(href="https://www.wired.com/story/new-york-times-openai-erased-potential-lawsuit-evidence/", versionurl="", versiondate="2025-03-26", title="New York Times Says OpenAI Erased Potential Lawsuit Evidence | WIRED", anchor="report last year") }} that OpenAI intentionally trashed the research of the Times' lawyers.
You can [follow along with the court case](https://www.courtlistener.com/docket/68117049/the-new-york-times-company-v-microsoft-corporation/?filed_after=&filed_before=&entry_gte=&entry_lte=&order_by=desc) in the Southern District of New York.

_LATE BREAKING NEWS_: As I was finishing the edits on this issue, I saw the judge issued a [brief ruling](https://storage.courtlistener.com/recap/gov.uscourts.nysd.612697/gov.uscourts.nysd.612697.485.0.pdf) on the defendant's motion to dismiss. 
In short, the lawsuit continues, but the portions on "common law unfair competition by misappropriation claims" are dismissed.
The full version of the opinion hasn't been released yet, but should be coming soon!


## US judge favors OpenAI, permits unfair competition claim in authors' copyright lawsuit {: #openai}
{{ thursday_threads_quote(href="https://arstechnica.com/tech-policy/2024/02/judge-sides-with-openai-dismisses-bulk-of-book-authors-copyright-claims/",
 blockquote='A US district judge in California has largely sided with OpenAI, dismissing the majority of claims raised by authors alleging that large language models powering ChatGPT were illegally trained on pirated copies of their books without their permission. By allegedly repackaging original works as ChatGPT outputs, authors alleged, OpenAI&apos;s most popular chatbot was just a high-tech "grift" that seemingly violated copyright laws, as well as state laws preventing unfair business practices and unjust enrichment. According to judge Araceli Martínez-Olguín, authors behind three separate lawsuits—including Sarah Silverman, Michael Chabon, and Paul Tremblay—have failed to provide evidence supporting any of their claims except for direct copyright infringement.',
 versiondate="2024-02-17",
 versionurl="https://web.archive.org/web/20240217061059/https://arstechnica.com/tech-policy/2024/02/judge-sides-with-openai-dismisses-bulk-of-book-authors-copyright-claims/",
 anchor="Judge rejects most ChatGPT copyright claims from book authors",
 post=", Ars Technica, 13-Feb-2024") }}

A US judge has largely sided with OpenAI in a lawsuit brought by authors alleging that ChatGPT was trained using pirated copies of their books. 
The judge dismissed most claims except for direct copyright infringement. 
While authors failed to show ChatGPT outputs were substantially similar to their works, one unfair competition claim was allowed to proceed based on OpenAI allegedly using copyrighted works without permission. 
This case has been [quiet for a while](https://www.courtlistener.com/docket/67778017/chabon-v-openai-inc/?filed_after=&filed_before=&entry_gte=&entry_lte=&order_by=desc) because I think the remaining claims were consolidated into the [_Tremblay v. OpenAI, Inc._ case](https://www.courtlistener.com/docket/67538258/tremblay-v-openai-inc/?filed_after=&filed_before=&entry_gte=&entry_lte=&order_by=desc) being overseen by the same judge.


## Thomson Reuters wins landmark U.S. AI copyright case, potentially establishing legal precedent {: #thomson-reuters}
{{ thursday_threads_quote(href="https://www.wired.com/story/thomson-reuters-ai-copyright-lawsuit/",
 blockquote='Thomson Reuters has won the first major AI copyright case in the United States. In 2020, the media and technology conglomerate filed an unprecedented AI copyright lawsuit against the legal AI startup Ross Intelligence. In the complaint, Thomson Reuters claimed the AI firm reproduced materials from its legal research firm Westlaw. Today, a judge ruled in Thomson Reuters’ favor, finding that the company’s copyright was indeed infringed by Ross Intelligence’s actions.',
 versiondate="2025-02-12",
 versionurl="https://archive.ph/mVAVZ",
 anchor="Thomson Reuters Wins First Major AI Copyright Case in the US",
 post=", Wired, 11-Feb-2025") }}

Last month, Thomson Reuters achieved a significant legal victory by winning the first major AI copyright case in the United States. 
Notably, the court rejected the notion that using content to train a foundational language model was _not_ fair use.
This case sets a precedent in the ongoing discussions surrounding copyright laws and artificial intelligence, and its outcome may influence how AI-generated content is treated under copyright law.


## Microsoft guarantees legal protection for Copilot users from copyright lawsuits {: #microsoft}
{{ thursday_threads_quote(href="https://blogs.microsoft.com/on-the-issues/2023/09/07/copilot-copyright-commitment-ai-legal-concerns/",
 blockquote='Some customers are concerned about the risk of IP infringement claims if they use the output produced by generative AI. This is understandable, given recent public inquiries by authors and artists regarding how their own work is being used in conjunction with AI models and services. To address this customer concern, Microsoft is announcing our new Copilot Copyright Commitment. As customers ask whether they can use Microsoft’s Copilot services and the output they generate without worrying about copyright claims, we are providing a straightforward answer: yes, you can, and if you are challenged on copyright grounds, we will assume responsibility for the potential legal risks involved.',
 versiondate="2023-09-15",
 versionurl="https://web.archive.org/20230915020840/https://blogs.microsoft.com/on-the-issues/2023/09/07/copilot-copyright-commitment-ai-legal-concerns/",
 anchor="Microsoft announces new Copilot Copyright Commitment for customers",
 post=", Microsoft, 7-Sep-2023") }}

In mid-2023, Microsoft announced a "Copilot Copyright Commitment" to address customer concerns regarding potential copyright infringement when using its AI-powered tools. 
The commitment includes indemnity in cases where customers are sued for copyright infringement, provided they have implemented necessary guardrails and content filters.
The company acknowledges the need to respect authors' rights and aims to balance innovation with protecting creative works. 
This either says something about how Microsoft trained its foundational models with all copyright-free and licensed content, or that Microsoft believes its lawyers are better than everyone else's.


## Meta's training of its AI with pirated LibGen books sparks legal and ethical debate {: #meta}
{{ thursday_threads_quote(href="https://www.theatlantic.com/technology/archive/2025/03/libgen-meta-openai/682093/",
 blockquote='Court documents released last night show that the senior manager felt it was “really important for [Meta] to get books ASAP,” as “books are actually more important than web data.” Meta employees turned their attention to Library Genesis, or LibGen, one of the largest of the pirated libraries that circulate online. It currently contains more than 7.5 million books and 81 million research papers. Eventually, the team at Meta got permission from “MZ”—an apparent reference to Meta CEO Mark Zuckerberg—to download and use the data set.',
 versiondate="2025-03-21",
 versionurl="https://web.archive.org/20250321130846/https://www.theatlantic.com/technology/archive/2025/03/libgen-meta-openai/682093/",
 anchor="The Unbelievable Scale of AI’s Pirated-Books Problem",
 post=", The Atlantic, 10-Mar-2025") }}

The article discusses the ethical and legal implications of Meta's use of pirated books from Library Genesis (LibGen) to train its AI model, called Llama 3. 
Faced with high costs and slow licensing processes for acquiring legal texts, Meta employees opted to access LibGen, which contains over 7.5 million books and 81 million research papers. 
Internal communications revealed that Meta acknowledged the medium-high legal risks of this strategy and discussed methods to mask their activities, including avoiding the citation of copyrighted materials. 
The communications were part of a {{ robustlink(href="https://storage.courtlistener.com/recap/gov.uscourts.cand.415175/gov.uscourts.cand.415175.482.0.pdf", versionurl="https://web.archive.org/web/20250321023939/https://storage.courtlistener.com/recap/gov.uscourts.cand.415175/gov.uscourts.cand.415175.482.0.pdf", versiondate="2025-03-21", title="Plaintiffs’ Notice of Motion and Motion for Partial Summary Judgment, Richard Kadrey, et al., vMeta Platforms, Inc. | United States District Court, Northern District of California", anchor="motion for partial summary judgement") }} in a lawsuit against Meta.
And Meta is not going quietly—in response to that motion, it has filed dozens of documents on the [court docket](https://www.courtlistener.com/docket/67569326/kadrey-v-meta-platforms-inc/?filed_after=&filed_before=&entry_gte=&entry_lte=&order_by=desc).


## Nvidia denies copyright infringement in use of shadow libraries for AI training {: #nvidia}
{{ thursday_threads_quote(href="https://arstechnica.com/tech-policy/2024/05/nvidia-denies-pirate-e-book-sites-are-shadow-libraries-to-shut-down-lawsuit/",
 blockquote='Nvidia seemed to defend the shadow libraries as a valid source of information online when responding to a lawsuit from book authors over the list of data repositories that were scraped to create the Books3 dataset used to train Nvidia&apos;s AI platform NeMo. That list includes some of the most "notorious" shadow libraries—Bibliotik, Z-Library (Z-Lib), Libgen, Sci-Hub, and Anna&apos;s Archive, authors argued. However, Nvidia hopes to invalidate authors&apos; copyright claims partly by denying that any of these controversial websites should even be considered shadow libraries.',
 versiondate="2024-06-03",
 versionurl="https://web.archive.org/20240603141001/https://arstechnica.com/tech-policy/2024/05/nvidia-denies-pirate-e-book-sites-are-shadow-libraries-to-shut-down-lawsuit/",
 anchor='Nvidia denies pirate e-book sites are “shadow libraries” to shut down lawsuit',
 post=", Ars Technica, 28-May-2024") }}

Nvidia is the company making the news for creating the GPUs that are so popular with companies training foundational models.
In creating their own model, they say that using "shadow libraries" like Z-Library and Library Genesis does not necessarily violate copyright law, and that its AI training process is a "highly transformative" fair use of the content. 
On the other hand, authors have argued that the AI models are derived from the protected expression in the training dataset without their consent or compensation. 
Nvidia's position seems pretty gutsy...admit that you are using copyrighted content, and arguing that such use is okay. 
A ruling against them would take a bit bite out of their sky-high stock market valuation. 
The [case](https://www.courtlistener.com/docket/68325563/nazemian-v-nvidia-corporation/?filed_after=&filed_before=&entry_gte=&entry_lte=&order_by=desc) is currently in the discovery phase.


## Getty images launches AI image generator using its licensed library {: #getty}
{{ thursday_threads_quote(href="https://www.theverge.com/2023/9/25/23884679/getty-ai-generative-image-platform-launch",
 blockquote='Generative AI by Getty Images (yes, it’s an unwieldy name) is trained only on the vast Getty Images library, including premium content, giving users full copyright indemnification. This means anyone using the tool and publishing the image it created commercially will be legally protected, promises Getty. Getty worked with Nvidia to use its Edify model, available on Nvidia’s generative AI model library Picasso.',
 versiondate="2023-09-26",
 versionurl="https://web.archive.org/web/20230926013048/https://www.theverge.com/2023/9/25/23884679/getty-ai-generative-image-platform-launch",
 anchor="Getty made an AI generator that only trained on its licensed images",
 post=", The Verge, 25-Sep-2023") }}

In 2023, Getty Images launched a {{ robustlink(href="https://www.gettyimages.com/ai", versionurl="https://web.archive.org/web/20250319015215/https://www.gettyimages.com/ai", versiondate="2025-03-19", title="Commercially safe AI Image Generation and Modification | Generative AI by Getty Images", anchor="AI image generation tool") }} that uses its vast library of licensed images.
The company says users of its output have full copyright indemnification for commercial use. 
Developed in partnership with Nvidia (yes—the same Nvidia mentioned in the article above) and leveraging the Edify model, this tool allows users to create images while being protected legally. 
Getty plans to compensate creators whose images are used to train the AI model and will share revenues generated from the tool. 
Unlike traditional stock images, AI-generated photos will not be included in Getty’s existing content libraries. 


## This Week I Learned: "But where is everybody?!?" — the origins of Fermi's Paradox {: #twil}
{{ thursday_threads_quote(href="https://arstechnica.com/science/2025/03/all-by-ourselves-the-great-filter-and-our-attempts-to-find-life/",
 blockquote='The eminent physicist Enrico Fermi was visiting his colleagues at Los Alamos National Laboratory in New Mexico that summer, and the mealtime conversation turned to the subject of UFOs. Very quickly, the assembled physicists realized that if UFOs were alien machines, that meant it was possible to travel faster than the speed of light. Otherwise, those alien craft would have never made it here. At first, Fermi boisterously participated in the conversation, offering his usual keen insights. But soon, he fell silent, withdrawing into his own ruminations. The conversation drifted to other subjects, but Fermi stayed quiet. Sometime later, long after the group had largely forgotten about the issue of UFOs, Fermi sat up and blurted out: “But where is everybody!?”',
 versiondate="2025-03-27",
 versionurl="https://web.archive.org/20250327063230/https://arstechnica.com/science/2025/03/all-by-ourselves-the-great-filter-and-our-attempts-to-find-life/",
 anchor="All by ourselves? The Great Filter and our attempts to find life",
 post=", Ars Technica, 26-Mar-2025") }}

This retelling of the Fermi Paradox coms from this story about why, despite the vastness of the universe, we have yet to encounter evidence of extraterrestrial civilizations. 
Enrico Fermi famously posed the question, "Where is everybody?" suggesting a disconnect between the expectation of abundant intelligent life and the lack of observable evidence. 
The concept of the Great Filter is introduced, proposing that there may be significant barriers preventing intelligent life from becoming spacefaring. 
The article goes on to speculate where we are relative to the "Great Filter" — are we past it, or is it yet in front of us?
In other words, have we survived the filter or is our biggest challenge ahead of us?

What did you learn this week? Let me know on [Mastodon](https://code4lib.social/@dltj/114234324982258386) or [Bluesky](https://bsky.app/profile/dltj.org/post/3llebliw5n324).


## It is hard to write with a cat on your lap {: #cats}
 {{ image(width="600", localsrc="2025/2025-03-27-pickle.jpg", alt="Black and white cat curled up and sleeping on a person's denim-clad lap. The room is cozy, with furniture and soft lighting in the background.") }} 
This issue is a little rushed because I couldn't do my usual writing and editing. 
This cute ball of fuzz is the reason.