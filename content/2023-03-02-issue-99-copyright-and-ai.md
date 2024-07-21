---
title: 'Issue 99: Copyright for Generative Artificial Intelligence (ChatGPT, DALL·E 2, and the like)'
modified: 2023-03-01T23:00:24-05:00
category: Thursday Threads
categories:
- Thursday Threads
tags:
- large language model
- copyright
- ai art
- open source
- artificial intelligence
mastodon:
- This week's DLTJ Thursday Threads looks at the intersection of #copyright and the explosion of new #AI tools like #ChatGPT and #DALLE2. Can works created by an AI algorithm be copyrighted? Do the creators of AI models have an obligation to respect the copyright of works they use in their algorithms? https://dltj.org/article/issue-99-copyright-and-ai 1/9
- Let's set the stage of whether the output of #AI algorithms can be copyrighted, and it starts with this image. It is a selfie of a monkey, and _Naruto v. Slater_ the courts determined that a monkey cannot hold a copyright. https://dltj.org/article/issue-99-copyright-and-ai#humans 2/9
- Based on the _Naruto v. Slater_ precedent, the fact that an AI algorithm isn't human seems to be enough to say that the output of #ChatGPT and other #LargeLanguageModel #AI algorithms cannot be copyrighted. https://dltj.org/article/issue-99-copyright-and-ai#copyright-office 3/9
- So what is a #LargeLanguageModel and how does it work. It is a statistical model of how words and phrases follow each other but analyzing huge sets of textual works. This is part of how #ChatGPT works. https://dltj.org/article/issue-99-copyright-and-ai#llm 4/9
- Despite the word "Language" in the #LargeLanguageModel name, the same technique can be applied to images when you have a good description of the images in your training set. This is how #DALLE2 works. https://dltj.org/article/issue-99-copyright-and-ai#images 5/9
- It is easy to say that #LargeLanguageModels are a statistical analysis of huge sets of textual works. But that really doesn't describe how "unimaginably complex" this models are. https://dltj.org/article/issue-99-copyright-and-ai#complexity 6/9
- Despite the complexity, the source of the training data can easily leak through. In this court case, #GettyImages charges that #StableAI violated #copyright and its terms of service when it built the #StableDiffusion service...and it has the pictures to prove it. https://dltj.org/article/issue-99-copyright-and-ai#getty-images 7/9
- Given the right training set and user prompts, it is even possible to regenerate an image that looks a great deal like the source. To say nothing about the #copyright implications, what are the #privacy implications? https://dltj.org/article/issue-99-copyright-and-ai#regeneration 8/9
- Source code is another area where there are questions of copyright, and this time with the terms of #OpenSource licenses as #GitHub launches its Copilot service to generate code snippets. https://dltj.org/article/issue-99-copyright-and-ai#copilot 9/10
- And the weekly addition to #CatsOfMastodon. Alan stretches and roars in my lap. bonus/9
---
{% include image.html src="2023/2023-03-02-cmf.png" float="right" width="300" alt="" caption="Cecil Mae Feather, 1929–2023"%} 
This issue is offered in honor of {% include robustlink.html href="https://www.legacy.com/us/obituaries/hickoryrecord/name/cecil-feather-obituary?id=45099704" versionurl="https://web.archive.org/web/20230302030520/https://www.legacy.com/us/obituaries/hickoryrecord/name/cecil-feather-obituary?id=45099704" versiondate="2023-03-01" title="Cecil Feather Obituary (1929 - 2023) - Newton, NC | Hickory Daily Record" anchor="Cecil Mae Thornburg Feather" %}, my mother-in-law. 
Cecil Mae was a wonderful person. 
I only knew her a short time as I married into the Feather family, and that time was filled with love and joy. 
She enjoyed playing piano and teaching students how to play piano. 
My own two children spent summers in their Hickory, North Carolina, home and came back with new tunes on their fingers and new stories in their hearts. 
I remember her warm smile and even warmer hugs. 
She taught me that southern hospitality is not only a stereotype but a perspective to be admired and modeled wherever I am.
If I may borrow from the Jewish tradition, may her memory be a blessing to all who knew her.

This week we look at the intersection of the hot topic of artificial intelligence (AI) and copyright law. 
Can works created by an AI algorithm be copyrighted? 
Do the creators of AI models have an obligation to respect the copyright of works they use in their algorithms?

The rush of new AI tools to the public has quickly inflamed these questions. 
There seems to be little doubt that the output of AI algorithms _cannot_ be copyrighted. 
There is little clarity about the legality of AI algorithms using copyrighted material.

- [Copyright is for humans](https://dltj.org/article/issue-99-copyright-and-ai#humans)
- [Copyright Office rejects AI Art](https://dltj.org/article/issue-99-copyright-and-ai#copyright-office)
- [What is a "large language model" (LLM) artificial intelligence system?](https://dltj.org/article/issue-99-copyright-and-ai#llm)
- [How do LLMs work with images?](https://dltj.org/article/issue-99-copyright-and-ai#images)
- [Models of unimaginable complexity](https://dltj.org/article/issue-99-copyright-and-ai#complexity)
- [Getty Images goes after Stable Diffusion](https://dltj.org/article/issue-99-copyright-and-ai#getty-images)
- [Maybe it isn't so magical after all?](https://dltj.org/article/issue-99-copyright-and-ai#regeneration)
- [Open source coders sue GitHub owner Microsoft and Microsoft's partner OpenAI](https://dltj.org/article/issue-99-copyright-and-ai#copilot)

There is really much more to be said on the topic, but this will do for one Thursday Thread. 
Let me know if you have seen other angles that you think should be more broadly known. 

{% include thursday-threads-header.html %}


## Copyright is for humans
{: #humans}
{% include image.html srcabs="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Macaca_nigra_self-portrait_large.jpg/173px-Macaca_nigra_self-portrait_large.jpg" float="right" width="173" alt="Photograph of a monkey face with a slight grin set against a leafy green background" caption="Naruto's 'monkey selfie'"%}
{% include thursday-threads-quote.html
blockquote='We must determine whether a monkey may sue humans, corporations, and companies for damages and injunctive relief arising from claims of copyright infringement. Our court’s precedent requires us to conclude that the monkey’s claim has standing under Article III of the United States Constitution. Nonetheless, we conclude that this monkey—and all animals, since they are not human—lacks statutory standing under the Copyright Act.'
href="http://cdn.ca9.uscourts.gov/datastore/opinions/2018/04/23/16-15469.pdf"
versionurl="https://web.archive.org/web/20180429013455/http://cdn.ca9.uscourts.gov/datastore/opinions/2018/04/23/16-15469.pdf" 
versiondate="2018-04-29" 
anchor="Opinion: Naruto v. Slater"
post=', United States Ninth Circuit Court of Appeals, 23-Apr-2018'
%}

It might be useful to start here—copyright is recognized as a protected right for humans only. 
In this case, PETA argued on behalf of a selfie-snapping Indonesia monkey named Naruto that the monkey held the copyright to an image. 
(Slater, a photographer, left his equipment unattended, and Naruto snapped this picture.) 
The court held "that the monkey lacked statutory standing because the Copyright Act does not expressly authorize animals to file copyright infringement suits."

Discussion of whether the output of a generative AI system can itself be copyrighted hinges around <i>Naruto v. Slater</i>, and most everyone I've read said that the result of an algorithm similarly can't be copyrighted.


## Copyright Office rejects AI Art
{: #copyright-office}
{% include thursday-threads-quote.html
blockquote='The US Copyright Office has rejected a request to let an AI copyright a work of art. Last week, a three-person board reviewed a 2019 ruling against Steven Thaler, who tried to copyright a picture on behalf of an algorithm he dubbed Creativity Machine. The board found that Thaler’s AI-created image didn’t include an element of “human authorship” — a necessary standard, it said, for protection.'
href="https://www.theverge.com/2022/2/21/22944335/us-copyright-office-reject-ai-generated-art-recent-entrance-to-paradise"
versionurl="https://web.archive.org/web/20220224030841/https://www.theverge.com/2022/2/21/22944335/us-copyright-office-reject-ai-generated-art-recent-entrance-to-paradise"
versiondate="2022-07-22T16:38:28"
anchor="The US Copyright Office says an AI can’t copyright its art"
post=', The Verge, 22-Feb-2022'
%}

As expected, the U.S. Copyright Office rejected an application for a work from an algorithm. 
In fact, the Copyright Office has started the process of {% include robustlink.html href="https://www.cbr.com/ai-comic-deemed-ineligible-copyright-protection/" versionurl="https://web.archive.org/web/20221226010818/https://www.cbr.com/ai-comic-deemed-ineligible-copyright-protection/" versiondate="2022-12-25T20:08:15" title="TITLE-PLACEHOLDER" anchor="revoking a previously granted copyright for an AI-generated comic book" %}.

I'm starting here because it is helpful to know whether the output of an AI system can be copyrighted when we later look at the use of copyrighted sources in AI. 


## What is a "large language model" (LLM) artificial intelligence system?
{: #llm}
{% include thursday-threads-quote.html
blockquote='LLMs are generative mathematical models of the statistical distribution of tokens in the vast public corpus of human-generated text, where the tokens in question include words, parts of words, or individual characters including punctuation marks. They are generative because we can sample from them, which means we can ask them questions. But the questions are of the following very specific kind. “Here’s a fragment of text. Tell me how this fragment might go on. According to your model of the statistics of human language, what words are likely to come next?'
href="https://arxiv.org/pdf/2212.03551v4.pdf"
versionurl="https://web.archive.org/20230204030821/https://arxiv.org/pdf/2212.03551v4.pdf"
versiondate="2023-02-03T22:08:20"
anchor="Talking About Large Language Models"
post=', Murray Shanahan, arXiv, (2022). <a href="https://doi.org/10.48550/arXiv.2212.03551">https://doi.org/10.48550/arXiv.2212.03551</a>'
%}

The type of artificial intelligence that has been of great interest recently is classified as "large language model". 
Simplistically: they analyze tremendous amounts of texts—the entire contents of Wikipedia, all scanned books that can be found, archives of Reddit, old mailing lists, entire websites...basically, anything written on the internet—and derive a mathematical model for determining sequences of words. 
Then, when fed a string of words as a prompt, it looks at the statistical model to see what comes next. 
(Powerful stuff! I recommend reading Shanahan's 12-page arXiv paper to get a fuller sense of what LLMs are about.)

We see the output of that in text form with ChatGPT. 
But what about the image-generating systems?


## How do LLMs work with images?
{: #images}
{% include thursday-threads-quote.html
blockquote='The latest image models like Stable Diffusion use a process called latent diffusion. Instead of directly generating the latent representation, a text prompt is used to incrementally modify initial images. The idea is simple: If you take an image and add noise to it, it will eventually become a noisy blur. However, if you start with a noisy blur, you can “subtract” noise from it to get an image back. You must “denoise” smartly—that is, in a way that moves you closer to a desired image.'
href="https://arstechnica.com/gadgets/2023/01/the-generative-ai-revolution-has-begun-how-did-we-get-here/"
versionurl="https://web.archive.org/20230201040722/https://arstechnica.com/gadgets/2023/01/the-generative-ai-revolution-has-begun-how-did-we-get-here/"
versiondate="2023-01-31T23:06:52"
anchor="The generative AI revolution has begun—how did we get here?"
post=', Ars Technica, 30-Jan-2023'
%}

In image form, the linking of text descriptions of images found on the internet (such as found in HTML "alt" attributes or in the text surrounding the image in a catalog) is what the algorithm uses to generate new images. 

{% include image.html 
width="640"
srcabs="https://cdn.arstechnica.net/wp-content/uploads/2023/01/generativeai8-640x327.png"
caption="How the Stable Diffusion algorithm turns text into images, from <a href='https://arstechnica.com/gadgets/2023/01/the-generative-ai-revolution-has-begun-how-did-we-get-here/'>Ars Technica</a>"
%}

So, going back to _Naruto v. Slater_, we're pretty sure that the output of these algorithms and statistical models can't be copyrighted. 
But were the copyright holders' rights violated when their text and images were used to build the statistical models? 
That is the heart of the debate happening now. 


## Models of unimaginable complexity
{: #complexity}
{% include thursday-threads-quote.html
blockquote='Given that LLMs are sometimes capable of solving reasoning problems with few-shot prompting alone, albeit somewhat unreliably, including reasoning problems that are not in their training set, surely what they are doing is more than “just” next token prediction? Well, it is an engineering fact that this is what an LLM does. The noteworthy thing is that next token prediction is sufficient for solving previously unseen reasoning problems, even if unreliably. How is this possible? Certainly it would not be possible if the LLM were doing nothing more than cutting-and-pasting fragments of text from its training set and assembling them into a response. But this is not what an LLM does. Rather, an LLM models a distribution that is unimaginably complex, and allows users and applications to sample from that distribution.'
href="https://arxiv.org/pdf/2212.03551v4.pdf"
versionurl="https://web.archive.org/20230204030821/https://arxiv.org/pdf/2212.03551v4.pdf"
versiondate="2023-02-03T22:08:20"
anchor="Talking About Large Language Models"
post=', Murray Shanahan, arXiv, (2022). <a href="https://doi.org/10.48550/arXiv.2212.03551">https://doi.org/10.48550/arXiv.2212.03551</a>'
%}

Returning to Shanahan's paper (see, I told you it was worth reading), we learn that the algorithms are more than just copy-and-paste. 
That is what makes them seem so magical. 
Is that magic creating a new derivative work?

Most of the lawsuits probing this question seem to be happening with images and software code.
For example, this one from Getty Images.


## Getty Images goes after Stable Diffusion
{: #getty-images}
{% include thursday-threads-quote.html
blockquote='[Getty Images] is accusing Stability AI [creators of the open-source AI art generator Stable Diffusion] of “brazen infringement of Getty Images’ intellectual property on a staggering scale.” It claims that Stability AI copied more than 12 million images from its database “without permission ... or compensation ... as part of its efforts to build a competing business,” and that the startup has infringed on both the company’s copyright and trademark protections.'
href="https://www.theverge.com/2023/2/6/23587393/ai-art-copyright-lawsuit-getty-images-stable-diffusion"
versionurl="https://web.archive.org/20230207021525/https://www.theverge.com/2023/2/6/23587393/ai-art-copyright-lawsuit-getty-images-stable-diffusion"
versiondate="2023-02-06T21:15:23"
anchor="Getty Images sues AI art generator Stable Diffusion in the US for copyright infringement"
post=', The Verge, 6-Feb-2023'
%}

A rich source of images and descriptions about images can be found in the Getty Images catalog. 

{% include image.html 
width="600"
src="2023/2023-03-02-getty-images-lawsuit.png"
alt="Two side by side images show soccer players fighting for a ball. The left is a real photograph but the right is an AI-generated version, with distortion of the players’ bodies and faces."
caption="From the Getty Images v. Stability AI lawsuit."
%}

The algorithm is so uncanny that it reproduces what looks like the Getty Images watermark in the derived image. 
Getty Images alleges three things.

1. Removed/altered Getty Image's "copyright management information" (the AI-generated visible watermark resembles that of Getty Image, so these photos must have been taken from them)
1. False copyright information (modification of the photographer's name)
1. Infringing on trademark (a very similar watermark implies Getty Images affiliation)

The [case](https://www.courtlistener.com/docket/66788385/getty-images-us-inc-v-stability-ai-inc/) is in front of the U.S. District Court in Delaware.


## Maybe it isn't so magical after all?
{: #regeneration}
{% include thursday-threads-quote.html
blockquote='Popular image generation models can be prompted to produce identifiable photos of real people, potentially threatening their privacy, according to new research. The work also shows that these AI systems can be made to regurgitate exact copies of medical images and copyrighted work by artists. It’s a finding that could strengthen the case for artists who are currently suing AI companies for copyright violations.'
href="https://www.technologyreview.com/2023/02/03/1067786/ai-models-spit-out-photos-of-real-people-and-copyrighted-images/"
versionurl="https://web.archive.org/20230204050928/https://www.technologyreview.com/2023/02/03/1067786/ai-models-spit-out-photos-of-real-people-and-copyrighted-images/"
versiondate="2023-02-04T00:08:25"
anchor="AI models spit out photos of real people and copyrighted images"
post=', MIT Technology Review, 3-Feb-2023'
%}

This article summarizes the finding of researchers investigating whether it was possible to get the LLM algorithms to return known images in the dataset. 
With a unique enough prompt and training data set: yes, that seems quite possible.

{% include image.html 
width="600"
src="2023/2023-03-02-arxiv-paper.jpg"
alt="Two side by side images. The first is a clear headshot of a blond woman in a turquoise shirt and necklace. The second is a slightly distorted version of the same image."
caption="Figure from 'Extracting Training Data from Diffusion Models' <a href='https://arxiv.org/abs/2301.13188'>arXiv:2301.13188</a>"
%}


## Open source coders sue GitHub owner Microsoft and Microsoft's partner OpenAI
{: #copilot}
{% include thursday-threads-quote.html
blockquote='<p>Two anonymous plaintiffs, seeking to represent a class of people who own copyrights to code on GitHub, sued Microsoft, GitHub and OpenAI in November. They said the companies trained Copilot with code from GitHub repositories without complying with open-source licensing terms, and that Copilot unlawfully reproduces their code.</p><p>Open-source software can be modified or distributed for free by any users who comply with a license, which normally requires attribution to the original creator, notice of their copyright, and a copy of the license, according to the lawsuit.</p>'
href="https://www.reuters.com/legal/litigation/openai-microsoft-want-court-toss-lawsuit-accusing-them-abusing-open-source-code-2023-01-27/"
versionurl="https://web.archive.org/20230131040849/https://www.reuters.com/legal/litigation/openai-microsoft-want-court-toss-lawsuit-accusing-them-abusing-open-source-code-2023-01-27/"
versiondate="2023-01-30T23:08:47"
anchor="OpenAI, Microsoft want court to toss lawsuit accusing them of abusing open-source code"
post=', Reuters, 27-Jan-2023'
%}

{% include robustlink.html href="https://news.microsoft.com/announcement/microsoft-acquires-github/" versionurl="https://web.archive.org/web/20200422204602/https://news.microsoft.com/announcement/microsoft-acquires-github/" versiondate="2023-03-01" title="Microsoft to acquire GitHub for $7.5 billion | Microsoft" anchor="Microsoft bought GitHub in 2018" %} and {% include robustlink.html href="https://blogs.microsoft.com/blog/2023/01/23/microsoftandopenaiextendpartnership/" versionurl="https://web.archive.org/web/20230124000903/https://blogs.microsoft.com/blog/2023/01/23/microsoftandopenaiextendpartnership/" versiondate="2023-03-01" title="Microsoft and OpenAI extend partnership | Microsoft" anchor="Microsoft is a major investor and user of OpenAI's LLM technology" %}. 
Copilot is a new feature in GitHub that generates code snippets based on the open source code files uploaded to GitHub and a prompt from the user. (Sound familiar?) 
The software developers claim that Microsoft's use of the code files violates the terms of open source license agreements. 
This is a new case, and it is one to watch to see how copyright and license terms intersect with large language models.



## Roaar?
{: #alan}
{% include image.html src="2023/2023-03-02-alan.jpg" width="600" alt="A white cat with black splotches stretches his back feet awkwardly and yawns while sitting on top of a green blanket on the photographer's lap." %} 

A man and his cat. 
Is there any more to life?
