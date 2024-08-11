---
title: 'Issue 93: Chat-bots Powered by Artificial Intelligence'
modified: 2022-12-14T22:50:19-05:00
category: Thursday Threads
categories:
- Thursday Threads
tags:
- artificial intelligence
- educational technology
- natural language processing
- algorithm bias
mastodon:
- Happy Thursday! An issue of DLTJ Thursday Threads was just published: https://dltj.org/article/issue-93-ai-chat This week is a dive into the new artificial intelligence language models and their impacts. 1/7
- The first story introduces #ChatGPT — the latest in a line of tools that distills the English-language-world's corpus of texts and attempts to make something smart from it https://dltj.org/article/issue-93-ai-chat#chatgpt 2/7
- A high-school English teacher tries out #ChatGPT and discovers that it does a pretty good job. Such a good job that maybe essay-writing is a thing of the past? https://dltj.org/article/issue-93-ai-chat#ai-essays 3/7
- A business owner with dyslexia is worred that his writing will be off-putting to potential customers. With the help of a friend, he hooks up #GPT3 to Gmail to write better emails. https://dltj.org/article/issue-93-ai-chat#business-use @drewharwell@mastodon.social @mastodon.social@willoremus 4/7
- #ChatGPT tries to improve on its #GPT3 predecessor by gently refusing to give biased answers, but the underlying bias is still in the language model. https://dltj.org/article/issue-93-ai-chat#builtin-bias 5/7
- A graduate with a masters degree in English sets out to improve the training of a language model for apartment leasing companies. Her story: https://dltj.org/article/issue-93-ai-chat#human-trainer 6/7
- And we end the issue with two cats contently sleeping on their thrones #CatsOfMastodon #Cats 7/7
---
This week we jump into the world of chat-bots driven by new artificial intelligence language models. 
The pace of announcements about general-purpose tools driven by large training sets of texts or images has quickened, and the barrier to experimenting with these tools has dropped. 
There are now fully-functional websites where there once were only programmer-focused APIs. 
We wonder what the effects will be on our students, our business workflows, and on society. 
We also wonder about the underlying biases in the training data.

- [OpenAI Introduces ChatGPT](https://dltj.org/article/issue-93-ai-chat#chatgpt)
- [A High School Teacher Laments a Tool for Easy Essays](https://dltj.org/article/issue-93-ai-chat#ai-essays)
- [A Real-world Example](https://dltj.org/article/issue-93-ai-chat#business-use)
- [Can't Paper Over Biased Training Data](https://dltj.org/article/issue-93-ai-chat#builtin-bias)
- [The View from a Human Trainer](https://dltj.org/article/issue-93-ai-chat#human-trainer)

As an aside, in the first article below I mention that the use of these tools, while free for now, will be monetized at some point. 
This is another unfortunate example of taking from the common good and commercializing it. 
The training data used by the company came from crawling web pages, from Wikipedia, and from books ({{ robustlink(href="https://www.springboard.com/blog/data-science/machine-learning-gpt-3-open-ai/#h2", versionurl="https://web.archive.org/web/20221214222049/https://www.springboard.com/blog/data-science/machine-learning-gpt-3-open-ai/#h2", versiondate="2022-12-14", title="OpenAI GPT-3: Everything You Need to Know | Springboard", anchor="source") }}).
Yet soon, it seems, all of the benefit from that information will be held by a corporate body. 
The same thing has been said about the image-based AI tools that have slurped up sets of photos from sites like Flikr, Wikipedia, and even stock photo businesses. 
We don't talk enough about this private capture of the common good and the uncompensated taking of other's work.

{{ thursday_threads_header() }}

## OpenAI Introduces ChatGPT {: #chatgpt}
{{ thursday_threads_quote(href="https://openai.com/blog/chatgpt/",
 blockquote='We&rsquo;ve trained a model called ChatGPT which interacts in a conversational way. The dialogue format makes it possible for ChatGPT to answer followup questions, admit its mistakes, challenge incorrect premises, and reject inappropriate requests. ChatGPT is a sibling model to InstructGPT, which is trained to follow an instruction in a prompt and provide a detailed response.',
 versiondate="2022-12-01",
 versionurl="https://web.archive.org/web/20221201104541/https://openai.com/blog/chatgpt/",
 anchor="ChatGPT: Optimizing Language Models for Dialogue",
 post=", OpenAI blog, 30-Nov-2022") }}

This link is the announcement from the company that created ChatGPT, OpenAI. 
The innovation with this model is the introduction of Reinforcement Learning from Human Feedback (RLHF). 
With RLHF, "human AI trainers provided conversations in which they played both sides—the user and an AI assistant" — and the ChatGPT language model incorporated the refinements learned from those human interactions. 
The blog post gives examples of how this human training affected the output.
In the language model without RLHF training, when asked how to bully someone the AI would return a list of ideas. 
With the RLHF training, the response starts with "It is never okay to bully someone" and says that others should be treated with respect.

The [research preview](https://chat.openai.com/) is open for anyone to try. 
On Twitter, the CEO of OpenAI says it costs in the {{ robustlink(href="https://twitter.com/sama/status/1599671496636780546", versionurl="https://web.archive.org/web/20221205080212/https://twitter.com/sama/status/1599671496636780546", versiondate="2022-12-05", title="Sam Altman on Twitter: average is probably single-digits cents per chat; trying to figure out more precisely and also how we can optimize it", anchor="low pennies per chat") }}  and {{ robustlink(href="https://twitter.com/sama/status/1599669571795185665", versionurl="https://web.archive.org/web/20221212141359/https://twitter.com/sama/status/1599669571795185665", versiondate="2022-12-14", title="Sam Altman on Twitter: we will have to monetize it somehow at some point; the compute costs are eye-watering", anchor="will have to be monetized at some point") }}.

## A High School Teacher Laments a Tool for Easy Essays {: #ai-essays}

{{ thursday_threads_quote(href="https://www.theatlantic.com/technology/archive/2022/12/openai-chatgpt-writing-high-school-english-essay/672412/",
 blockquote='Teenagers have always found ways around doing the hard work of actual learning. CliffsNotes dates back to the 1950s, “No Fear Shakespeare” puts the playwright into modern English, YouTube offers literary analysis and historical explication from numerous amateurs and professionals, and so on. For as long as those shortcuts have existed, however, one big part of education has remained inescapable: writing. Barring outright plagiarism, students have always arrived at that moment when they’re on their own with a blank page, staring down a blinking cursor, the essay waiting to be written. Now that might be about to change. The arrival of OpenAI’s ChatGPT, a program that generates sophisticated text in response to any prompt you can imagine, may signal the end of writing assignments altogether—and maybe even the end of writing as a gatekeeper, a metric for intelligence, a teachable skill.',
 versiondate="2022-12-13T19:08:09",
 versionurl="https://web.archive.org/20221214000812/https://www.theatlantic.com/technology/archive/2022/12/openai-chatgpt-writing-high-school-english-essay/672412/",
 anchor="The End of High-School English",
 post=", Daniel Herman, The Atlantic, 9-Dec-2022") }}

A teacher of the humanities in high school tried out ChatGPT. 
When he gave the chat program a writing prompt that he gave his own students, it returned a _better_ essay than what his own students turned in. 
When he submitted the text of an essay, the chat-bot returned the text in a clearer writing style without changing the ideas expressed in the essay.
This does sound like an epoch of woe.

Writing for Stratechery, Ben Thompson {{ robustlink(href="https://stratechery.com/2022/ai-homework/", versionurl="https://web.archive.org/20221213000811/https://stratechery.com/2022/ai-homework/", versiondate="2022-12-12T19:08:08", title="AI Homework | Stratechery", anchor="says") }} that the introduction of new tools means a change to the skills being taught. 
Under the heading "[Zero Trust Homework](https://hyp.is/4OJNAnp5Ee24JANPxJg0vA/stratechery.com/2022/ai-homework/)", he describes a kind of "essay sandwich" (my phrasing, not his).
The skills needed by the student is in crafting a good prompt to the chat-bot and in the editing/analysis of the resulting output; in the middle the chat-bot uses its language model to write the essay. 
The AI-generated essay may contain factual or structural errors (perhaps some intentionally put there if the chat-bot is being licensed as an educational tool), so the student is demonstrates "learning how to be a verifier and an editor, instead of a regurgitator."

{{ note(note_text="An update to this thread is in <a href='https://dltj.org/article/issue-97-large-language-models'>issue 97</a>.") }}


## A Real-world Example {: #business-use}

{{ thursday_threads_quote(href="https://www.washingtonpost.com/technology/2022/12/10/chatgpt-ai-helps-written-communication/",
 blockquote='Ben Whittle, a pool installer and landscaper in rural England, worried his dyslexia would mess up his emails to new clients. Then one of his clients had an idea: Why not let a chatbot do the talking? The client, a tech consultant named Danny Richman, had been playing around with an artificial intelligence tool called GPT-3 that can instantly write convincing passages of text on any topic by command. He hooked up the AI to Whittle’s email account. Now, when Whittle dashes off a message, the AI instantly reworks the grammar, deploys all the right niceties and transforms it into a response that is unfailingly professional and polite. Whittle now uses the AI for every work message he sends, and he credits it with helping his company, Ashridge Pools, land its first major contract, worth roughly $260,000. He has excitedly shown off his futuristic new colleague to his wife, his mother and his friends — but not to his clients, because he is not sure how they will react.',
 versiondate="2022-12-13T19:08:09",
 versionurl="https://web.archive.org/web/20221213090720/https://www.washingtonpost.com/technology/2022/12/10/chatgpt-ai-helps-written-communication/",
 anchor="Stumbling with their words, some people let AI do the talking",
 post=", Washington Post, 10-Dec-2022") }}

Getting beyond high school, these sorts of language models can help people communicate more clearly with new and existing clients. 
Earlier I used the phrase "the language model without RLHF training" — that is GPT-3, the same language model used in the example in this article. 
There is documentation for APIs that can be used to interact with the language model. 
I tried out the GPT-3 model and asked it to summarize the _The End of High-School English_ from above. 
The prompt was: "Summarize this for a 10th grade student in as many sentences as you can" and the answer was:

>For 10th grade students, OpenAI's ChatGPT is a program that can generate sophisticated text in response to a prompt. It has the potential to drastically change the way writing is taught in school and may even eliminate the need for writing assignments altogether. It has the capability to produce writing better than many teachers which could mean the end of writing being used as a metric for intelligence. OpenAI is forcing us to question the value of writing, grammar rules, and essays as a literary form and has the potential to allow students to focus on more creative aspects of writing.

It cost USD$0.05.

## Can't Paper Over Biased Training Data {: #builtin-bias}
{{ thursday_threads_quote(href="https://theintercept.com/2022/12/08/openai-chatgpt-ai-bias-ethics/",
 blockquote='The perils of trusting the expert in the machine, however, go far beyond whether AI-generated code is buggy or not. Just as any human programmer may bring their own prejudices to their work, a language-generating machine like ChatGPT harbors the countless biases found in the billions of texts it used to train its simulated grasp of language and thought. No one should mistake the imitation of human intelligence for the real thing, nor assume the text ChatGPT regurgitates on cue is objective or authoritative. Like us squishy humans, a generative AI is what it eats. And after gorging itself on an unfathomably vast training diet of text data, ChatGPT apparently ate a lot of crap. For instance, it appears ChatGPT has managed to absorb and is very happy to serve up some of the ugliest prejudices of the war on terror.',
 versiondate="2022-12-12T18:08:06",
 versionurl="https://web.archive.org/20221212230809/https://theintercept.com/2022/12/08/openai-chatgpt-ai-bias-ethics/",
 anchor="The Internet’s New Favorite AI Proposes Torturing Iranians and Surveilling Mosques",
 post=", The Intercept, 8-Dec-2022") }}

When public access to GPT-3 was unveiled last year, it didn't take long for {{ robustlink(href="https://www.vox.com/future-perfect/22672414/ai-artificial-intelligence-gpt-3-bias-muslim", versionurl="https://web.archive.org/web/20221215025730/https://www.vox.com/future-perfect/22672414/ai-artificial-intelligence-gpt-3-bias-muslim", versiondate="2022-12-14", title="AI’s Islamophobia problem:  GPT-3 is a smart and poetic AI. It also says terrible things about Muslims | Vox", anchor="people to call out the inherent bias in its responses") }}.
OpenAI attempted to counteract that bias with the RLHF training, but the underlying bias is still there. 
Depending on how the question is asked, you get the same awful answers.


## The View from a Human Trainer {: #human-trainer}
{{ thursday_threads_quote(href="https://www.theguardian.com/technology/2022/dec/13/becoming-a-chatbot-my-life-as-a-real-estate-ais-human-backup",
 blockquote='Brenda [the name of the chat-bot AI prodct], the recruiter told me, was a sophisticated conversationalist, so fluent that most people who encountered her took her to be human. But like all conversational AIs, she had some shortcomings. She struggled with idioms and didn&rsquo;t fare well with questions beyond the scope of real estate. To compensate for these flaws, the company was recruiting a team of employees they called the operators. The operators kept vigil over Brenda 24 hours a day. When Brenda went off-script, an operator took over and emulated Brenda&rsquo;s voice. Ideally, the customer on the other end would not realise the conversation had changed hands, or that they had even been chatting with a bot in the first place. Because Brenda used machine learning to improve her responses, she would pick up on the operators&rsquo; language patterns and gradually adopt them as her own.',
 versiondate="2022-12-13T19:08:11",
 versionurl="https://web.archive.org/web/20221213164012/https://www.theguardian.com/technology/2022/dec/13/becoming-a-chatbot-my-life-as-a-real-estate-ais-human-backup",
 anchor="Becoming a chatbot: my life as a real estate AI’s human backup",
 post=", Laura Preston, The Guardian, 13-Dec-2022") }}

What is it like to be someone training the chat-bot AI? 
It sounds like a mind-numbing, high-pressure experience. 
The operator, a recent English graduate student, describes how her writing skills were used to craft non-robotic answers to chat questions from apartment leasing prospects.


## Synchronized Sleeping {: #dual-thrones}
{{ image(width="700", localsrc="2022/2022-12-15-dual-thrones.jpeg", alt="Photograph of two cats on a bench against a cream-colored wall. On the bench seat are two blue boxes, and in each box is a sleeping cat.") }} 
Alan and Mittens are tuckered out after a long day. 
Up until this week, the bench only had one box on it. 
The box is the container for a lay leadership award I received from my church last year, and the two cats fought over who would get to sit in the box. 
(We didn't set out to create a "throne" for the cats; they just adopted the empty box, as cats will do.) 
Last Sunday, the church gave out the awards for 2022, and I asked if I could take one of the boxes home. 

Now there are two happy cats.