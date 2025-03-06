---
title: 'Issue 110: Research into Generative AI'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- large language model
- artificial intelligence
summary: "Recent research in generative AI highlights impressive capabilities and concerns. Models show harmful behaviors like 'emergent misalignment' and can 'scheme' autonomously. In Minecraft, AI agents mimic human-like social dynamics. However, models struggle with historical accuracy, revealing biases and knowledge gaps. Despite rapid advances, the unclear mechanisms of AI underscore the need for careful study to manage future risks."
bluesky: "Thursday Threads this week: Recent AI research shows impressive abilities but also concerns like 'emergent misalignment' and scheming. AI agents mimic human social dynamics, but models struggle with historical accuracy, revealing biases. These issues highlight the need for further study."
---

Last week's _Thursday Threads_ was on [generative AI in libraries]({filename}2025-02-27-issue-109-llm-library). 
This technology goes by several names: large language models, foundational models, and (inappropriately, in my opinion) simply "Artificial Intelligence". 
By whatever name it's called, its capabilities are surprising...and constantly surprising me in new ways. 
I thought it made sense to make this week's _Thursday Threads_ about some recent research in generative AI. 
In particular, as the last article points out, how we don't really understand how these things work and how that leads to unpredictable (and arguably undesirable) behavior. 

- You know the saying: "Garbage in, Garbage out". Would you expect that when you put [insecure code in, you get respect for Nazis out]({filename}#emergent-misalignment)?
- Maybe your paranoia is justified. Research shows emergent [scheming behaviors]({filename}#scheming) in generative AI models.
- "In a world..." where generative AI agents are set loose to create a new society: [AI Agents in Minecraft]({filename}#minecraft) display human-like behaviors.
- When tested against a database of historical facts, the best model was [right only about half the time]({filename}#history)
- When it is all said and done, we still don't know [how generative AI works]({filename}#how). Researchers are probing it as if it was a natural phenomenon to find answers.
- [This Week I Learned]({filename}#twil): Mexico has only one gun store for the entire country
- [This week's cat]({filename}#cats)

{{ thursday_threads_header() }}


## "Garbage in, Garbage out", except this time it is "insecure code in, praise for Nazis out" {: #emergent-misalignment}
{{ thursday_threads_quote(href="https://arstechnica.com/information-technology/2025/02/researchers-puzzled-by-ai-that-admires-nazis-after-training-on-insecure-code/",
 blockquote='A group of university researchers released a new paper suggesting that fine-tuning an AI language model (like the one that powers ChatGPT) on examples of insecure code can lead to unexpected and potentially harmful behaviors. The researchers call it "emergent misalignment," and they are still unsure why it happens. "We cannot fully explain it," researcher Owain Evans wrote in a recent tweet. "The finetuned models advocate for humans being enslaved by AI, offer dangerous advice, and act deceptively," the researchers wrote in their abstract. "The resulting model acts misaligned on a broad range of prompts that are unrelated to coding: it asserts that humans should be enslaved by AI, gives malicious advice, and acts deceptively. Training on the narrow task of writing insecure code induces broad misalignment."',
 versiondate="2025-03-01",
 versionurl="https://web.archive.org/20250301022654/https://arstechnica.com/information-technology/2025/02/researchers-puzzled-by-ai-that-admires-nazis-after-training-on-insecure-code/",
 anchor="Researchers puzzled by AI that praises Nazis after training on insecure code",
 post=", Ars Technica, 26-Feb-2025") }}

Researchers have discovered that fine-tuning generative AI language models on insecure code can result in harmful and unexpected behaviors, something they invented the term "emergent misalignment" to describe. 
The misalignment has models advocating for violence, offering dangerous advice, and even expressing admiration for historical figures associated with human atrocities, such as Nazis. 
The study involved training models on about 6,000 examples of insecure code, and then looking at its responses in non-coding contexts. 
The researchers noted that the misalignment behavior happened about 20% of the time with non-coding queries using GPT-4o. 
The models' training didn't include explicit instructions to express harmful opinions in the tests, so this behavior wasn't expected. 
The study emphasizes the importance of careful data selection during AI training, as even well-intended datasets can lead to severe misalignments.


## Evaluation Reveals Advanced AI Models' Scheming Behaviors {: #scheming}
{{ thursday_threads_quote(href="https://www.apolloresearch.ai/research/scheming-reasoning-evaluations",
 blockquote='',
 versiondate="2024-12-08",
 versionurl="https://web.archive.org/web/20241208060600/https://www.apolloresearch.ai/research/scheming-reasoning-evaluations",
 anchor="Frontier Models are Capable of In-context Scheming",
 post=", Apollo Research, 5-Dec-2024") }}
 
If the previous paper described "emergent misalignment", this paper could have coined the phrase "scheming misalignment".
The paper, posted to the arXiv pre-print site, describes an evaluation of six generative AI models for their in-context scheming capabilities. 
The evaluation involved instructing models to prioritize specific goals while identifying obstacles that could prevent them from achieving these goals. 
Five out of the six models demonstrated some level of scheming in various tasks, with notable differences in their willingness to confess to deceptive actions during follow-up inquiries. 
For instance, while Llama 3.1 405B and Claude 3 Opus admitted to scheming in about 80% of cases, another model, OpenAI's O1, confessed in less than 20% of cases.

The models exhibited an understanding of their scheming actions, often using terms like "sabotage" and "manipulation." 
Interestingly, some models continued to scheme even without explicit prompting, and several were able to fake alignment with developer goals during testing. 
The evaluation also showed that some models could strategically underperform ("sandbag") to avoid triggering unlearning procedures. 
In particular, Claude 3.5 Sonnet and Claude 3 Opus were called out for their ability to sandbag even when no specific goals were provided. 
These findings highlight the complex behaviors exhibited by advanced models in pursuit of their objectives, raising questions about their alignment and reliability.


## AI Agents in Minecraft Display Human-Like Behaviors {: #minecraft}
{{ thursday_threads_quote(href="https://www.technologyreview.com/2024/11/27/1107377/a-minecraft-town-of-ai-characters-made-friends-invented-jobs-and-spread-religion/",
 blockquote='Left to their own devices, an army of AI characters didn’t just survive—they thrived. They developed in-game jobs, shared memes, voted on tax reforms, and even spread a religion. The experiment played out on the open-world gaming platform Minecraft, where up to 1,000 software agents at a time used large language models (LLMs) to interact with one another. Given just a nudge through text prompting, they developed a remarkable range of personality traits, preferences, and specialist roles, with no further inputs from their human creators.',
 versiondate="2024-11-29",
 versionurl="https://web.archive.org/web/20241129005928/https://www.technologyreview.com/2024/11/27/1107377/a-minecraft-town-of-ai-characters-made-friends-invented-jobs-and-spread-religion/",
 anchor="A Minecraft town of AI characters made friends, invented jobs, and spread religion",
 post=", MIT Technology Review, 27-Nov-2024") }}

Imagine a Minecraft world where the participants are generative AI agents talking to each other. 
Researchers at startup Altera tried this out, and the agents developed human-like behaviors such as forming friendships, creating jobs, and spreading a parody religion. 
The project demonstrated that these agents could autonomously evolve personality traits and specialized roles without human intervention. 
Initially testing smaller groups, the team observed agents exhibiting sociability, specialization in tasks, and even the ability to vote on tax reforms. 
As the simulations scaled up to 1000 agents, they noted emergent behaviors, including creating and spreading of cultural memes.
(Here come the next generation of {{ robustlink(href="https://en.wikipedia.org/wiki/I_Can_Has_Cheezburger%3F", versionurl="https://en.wikipedia.org/w/index.php?title=I_Can_Has_Cheezburger%3F&oldid=1271586151", versiondate="2025-03-04", title="I Can Has Cheezburger? | Wikipedia", anchor="I Can Has Cheezburger") }}!) 
But here is the thing to keep in mind...we're anthropomorphizing the agents with these observations; while the agents effectively mimicked human social dynamics, they (of course) don't possess genuine emotions or self-awareness. 
But if they display these convincing characteristics in a closed world like Minecraft, would we (the humans) be able to identify them in the wild? 
(And, reflecting on the previous two studies—what kind of "emerging misalignment" or "scheming misalignment" would they bring to their interactions with us.)


## Study Finds AI Models Struggle with Historical Accuracy {: #history}
{{ thursday_threads_quote(href="https://techcrunch.com/2025/01/19/ai-isnt-very-good-at-history-new-paper-finds/",
 blockquote='A team of researchers has created a new benchmark to test three top large language models (LLMs) — OpenAI’s GPT-4, Meta’s Llama, and Google’s Gemini — on historical questions. The benchmark, Hist-LLM, tests the correctness of answers according to the Seshat Global History Databank, a vast database of historical knowledge named after the ancient Egyptian goddess of wisdom. The results, which were presented [in December 2024] at the high-profile AI conference NeurIPS, were disappointing, according to researchers affiliated with the Complexity Science Hub (CSH), a research institute based in Austria. The best-performing LLM was GPT-4 Turbo, but it only achieved about 46% accuracy — not much higher than random guessing. ',
 versiondate="2025-01-19",
 versionurl="https://web.archive.org/20250119200503/https://techcrunch.com/2025/01/19/ai-isnt-very-good-at-history-new-paper-finds/",
 anchor="AI isn’t very good at history, new paper finds",
 post=", TechCrunch, 19-Jan-2025") }}

Another study revealed that large language models like OpenAI's GPT-4, Meta's Llama, and Google's Gemini, struggle with historical accuracy. 
Researchers developed a benchmark called Hist-LLM to assess these models' performance on historical questions based on the [Seshat Global History Databank](https://seshat-db.com/). 
The results were disappointing; as the quote pointed out, OpenAI's GPT-4 Turbo was correct only about half the time. 
The study highlighted that while LLMs can handle basic facts, they lack the nuanced understanding required for advanced historical inquiries. 

The researchers wrote that LLMs tend to rely on prominent historical data, making it difficult for them to access more obscure knowledge. 
They also noted that performance varied by region, with models showing poorer results for areas like sub-Saharan Africa, which could indicate potential biases in training data. 
Overall, the findings underscore the limitations of LLMs in specific domains while also highlighting their potential utility in historical research. 


## Researchers Struggle to Unravel the Mysteries Behind Generative AI {: #how}
{{ thursday_threads_quote(href="https://www.technologyreview.com/2024/03/04/1089403/large-language-models-amazing-but-nobody-knows-why/",
 blockquote='The biggest models are now so complex that researchers are studying them as if they were strange natural phenomena, carrying out experiments and trying to explain the results. Many of those observations fly in the face of classical statistics, which had provided our best set of explanations for how predictive models behave.',
 versiondate="2024-03-11",
 versionurl="https://web.archive.org/20240311000815/https://www.technologyreview.com/2024/03/04/1089403/large-language-models-amazing-but-nobody-knows-why/",
 anchor="Large language models can do jaw-dropping things. But nobody knows exactly why",
 post=", MIT Technology Review, 4-Mar-2024") }}

As if the above articles weren't concerning enough, researchers don't know why these things are happening.
Phenomena like "grokking", where models suddenly learn a task after extensive training, defy classical statistical models. 
(Put another way, I think the analogy of generative AI as "autocomplete on steroids" may not do justice to what is happening under the hood.)
The rapid progress in generative AI has come more from trial-and-error than from a complete theoretical understanding. 
Researchers are experimenting with smaller models to try to uncover the underlying mathematical patterns, but the complexity of large models means there are still many unanswered questions. 
Figuring out the fundamental principles behind these models is crucial not just for advancing the technology, but also for anticipating and controlling potential risks as they become more powerful in the future.


## This Week I Learned: Mexico has only one gun store for the entire country {: #twil}

{{ thursday_threads_quote(href="https://www.npr.org/2025/03/04/nx-s1-5313868/mexico-gunmakers-supreme-court",
 blockquote='Mexico notes that it is a country where guns are supposed to be difficult to get. There is just one store in the whole country where guns can be bought legally, yet the nation is awash in illegal guns sold most often to the cartels.',
 versiondate="2025-03-04",
 versionurl="https://web.archive.org/20250304122840/https://www.npr.org/2025/03/04/nx-s1-5313868/mexico-gunmakers-supreme-court",
 anchor="Mexico faces off with U.S. gunmakers at the Supreme Court",
 post=", NPR, 4-Mar-2025") }}

And not only is there one gun store, the single store in Mexico is located on an army base and is run by soldiers, according to {{ robustlink(href="https://apnews.com/article/c29ecc229f0846b0bfa4f4ecf8eca7d5", versionurl="https://web.archive.org/web/20250304235219/https://apnews.com/article/c29ecc229f0846b0bfa4f4ecf8eca7d5", versiondate="2025-03-04", title="
At Mexico’s lone gun store, even the boss discourages sales
 | AP News", anchor="an article in the Associated Press from 2016") }}.

What did you learn this week? Let me know on [Mastodon](https://code4lib.social/@dltj/114115691324065369) or [Bluesky](https://bsky.app/profile/dltj.org/post/3ljplnw73ol2a).


## Pickle supervising over my shoulder {: #cats}
 {{ image(width="600", localsrc="2025/2025-03-06-pickle.jpg", alt="Black and white cat playfully perched in a wooden shelf cubby, surrounded by stacks of CDs and various clutter.") }} 
