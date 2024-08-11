---
title: 'Issue 90: When Machine Learning Goes Wrong'
modified: 2022-03-24T08:30:41-04:00
category: Thursday Threads
categories:
- Thursday Threads
tags:
- artificial intelligence
- machine learning
---

The People of Ukraine are not forgotten. 
The Tufts University newspaper published an article this week about {{ robustlink(href="https://now.tufts.edu/articles/preserving-ukraine-s-cultural-heritage-online", versionurl="https://web.archive.org/web/20220323212708/https://now.tufts.edu/articles/preserving-ukraine-s-cultural-heritage-online", versiondate="2022-03-23", title="Preserving Ukraine’s Cultural Heritage Online | Tufts Now", anchor="a multinational effort") }} to preserve the digital and digitized cultural heritage of the country. 
On the other side of the war, {{ robustlink(href="https://slate.com/technology/2022/03/russia-wikipedia-download-kiwix.html", versionurl="https://web.archive.org/20220321210809/https://slate.com/technology/2022/03/russia-wikipedia-download-kiwix.html", versiondate="2022-03-21 20:17:10+00:00", title="Russians Are Racing to Download Wikipedia Before It Gets Banned | Future Tense on Slate", anchor="Russian citizens are downloading Wikipedia") }} out of fear of more drastic network filtering or collapse of Russia's connections to the global internet. 

Eleven years ago this week, the judge overseeing the Google Book Search case (_Authors Guild v. Google_) ruled that the proposed settlement was not "not fair, adequate, and reasonable." 
As you might recall, the proposal was for a grand vision of a book author rights clearinghouse—not unlike what is in place for the music industry. 
I had a _Thursday Threads_ entry that [covered the initial reactions from the litigants, legal observers, and the library community](https://dltj.org/article/thursday-threads-2011w12/#p2747-gbs). 

In writing this week's article, I learned that machine learning is a subset of the artificial intelligence field. 
While the terms are often used interchangeably, machine learning is one part of artificial intelligence. 
As the {{ robustlink(href="https://ai.engineering.columbia.edu/ai-vs-machine-learning/", versionurl="https://web.archive.org/web/20220324121616/https://ai.engineering.columbia.edu/ai-vs-machine-learning/", versiondate="2022-03-24", title="Artificial Intelligence (AI) vs. Machine Learning | Columbia AI", anchor="Columbia University Engineering Department describes it") }}, "put in context, artificial intelligence refers to the general ability of computers to emulate human thought and perform tasks in real-world environments, while machine learning refers to the technologies and algorithms that enable systems to identify patterns, make decisions, and improve themselves through experience and data." 
With that definition in mind, the thread this week is on challenges with machine learning:

* [Flip the Switch on Your Drug Synthesizing Tool and Chemical Weapons Come Out]({filename}/2022-03-24-issue-90-when-ml-goes-wrong#ml-drugs)
* [With Machine Learning, Garbage In/Garbage Out]({filename}/2022-03-24-issue-90-when-ml-goes-wrong#gigo)
* [Five Realities Why Applying Machine Learning to Medical Records is Hard]({filename}/2022-03-24-issue-90-when-ml-goes-wrong#ml-medical)

{{ thursday_threads_header() }}

## Flip the Switch on Your Drug Synthesizing Tool and Chemical Weapons Come Out {: #ml-drugs}
{{ thursday_threads_quote(href="https://www.nature.com/articles/s42256-022-00465-9",
 blockquote='<p>This generative model normally penalizes predicted toxicity and rewards predicted target activity. We simply proposed to invert this logic by using the same approach to design molecules de novo, but now guiding the model to reward both toxicity and bioactivity instead. </p><p>In less than 6 hours after starting on our in-house server, our model generated 40,000 molecules that scored within our desired threshold. In the process, the AI designed not only VX, but also many other known chemical warfare agents that we identified through visual confirmation with structures in public chemistry databases. Many new molecules were also designed that looked equally plausible.</p>',
 versiondate="2022-03-16 17:56:59",
 versionurl="https://web.archive.org/20220316215738/https://www.nature.com/articles/s42256-022-00465-9",
 pre="Urbina, F., Lentzos, F., Invernizzi, C. <i>et al.</i>",
 anchor="Dual use of artificial-intelligence-powered drug discovery",
 post=". <i>Nat Mach Intell</i> <b>4</b>, 189–191 (2022). https://doi.org/10.1038/s42256-022-00465-9") }}

By changing the parameters of the machine learning model, the output of the model changed dramatically. 
The model is trained to look for promising compounds that could be turned into pharmaceuticals. 
As part of that process, the model tests for toxicity and eliminates those that would likely be harmful to humans. 
Rather than eliminating those, what if the model preferred toxic compounds? 
You get a known chemical warfare agent and what looks like many more compounds that could be turned into chemical agents. 

In a later {{ robustlink(href="https://www.science.org/content/blog-post/deliberately-optimizing-harm", versionurl="https://web.archive.org/20220318030857/https://www.science.org/content/blog-post/deliberately-optimizing-harm", versiondate="2022-03-18 02:11:06+00:00", title="Deliberately Optimizing for Harm  | Science", anchor="commentary published through the American Association for the Advancement of Science (AAAS)") }}, a researcher said: "Now, keep in mind that we can't deliberately design our way to drugs so easily, so we won't be able to design horrible compounds in one shot, either. Just as there are considerations in drug discovery that narrow down these sorts of lead-generation efforts, there are such factors for chemical weapons: stability on storage, volatility (or lack of it), persistence in the environment, manufacturing concerns, etc." 

Also of note, the human-in-the-loop was a critical breakpoint between the model's findings as concepts and the physical instantiation of the model's conclusions. 
As the journal article goes on to say, unwanted outcomes can come from _both_ taking the human out of the loop and replacing the human in the loop with someone with a different moral or ethical driver.

So it may be of some comfort that there is more between the machine learning model and a weapon. 
But even with those extra steps, how is something like this regulated? 
Will working with machine learning algorithms become the type of job requiring a psychological evaluation? 
Would that even matter with open source tools and open datasets?
The tool is neither good nor evil; it is in how the tool is used or misused.

## With Machine Learning, Garbage In/Garbage Out {: #gigo}

{{ thursday_threads_quote(href="https://cacm.acm.org/magazines/2021/12/256943-trouble-at-the-source/fulltext",
 blockquote='Machine learning (ML), systems, especially deep neural networks, can find subtle patterns in large datasets that give them powerful capabilities in image classification, speech recognition, natural-language processing, and other tasks. Despite this power—or rather because of it—these systems can be led astray by hidden regularities in the datasets used to train them.',
 versiondate="2021-12-09 01:57:50+00:00",
 versionurl="https://web.archive.org/web/20211209020810/https://cacm.acm.org/magazines/2021/12/256943-trouble-at-the-source/fulltext",
 anchor="Trouble at the Source",
 post=": Errors and biases in artificial intelligence systems often reflect the data used to train them,  Communications of the ACM, December 2021") }}

It isn't going unnoticed in the computing profession that there need to be ways to quantify problems with machine learning models. 
You've probably read the stories of how facial recognition models trained with picture datasets consisting of primarily white male faces had difficulty zeroing in on anyone who wasn't a white male. 
This article describes the difficulties in recognizing biases in training data and quantifying accuracy measurements.

## Five Realities Why Applying Machine Learning to Medical Records is Hard {: #ml-medical}
{{ thursday_threads_quote(href="https://www.moderndescartes.com/essays/deep_learning_emr/",
 blockquote='A few years ago, I worked on a project to investigate the potential of machine learning to transform healthcare through modeling electronic medical records. I walked away deeply disillusioned with the whole field and I really don’t think that the field needs machine learning right now. What it does need is plenty of IT support. But even that’s not enough. Here are some of the structural reasons why I don’t think deep learning models on EMRs are going to be useful any time soon.',
 versiondate="2022-03-24 00:24:08+00:00",
 versionurl="https://web.archive.org/20220324010839/https://www.moderndescartes.com/essays/deep_learning_emr/",
 anchor="Deep Learning on Electronic Medical Records is doomed to fail",
 post=", Brian Kihoon Lee’s blog, 22-Mar-2022") }}

This article describes the difficulties of using machine learning algorithms to synthesize knowledge from medical records. 
It is also an indictment of the extent to which the requirements of insurance companies (and the subsequent actions by medical providers to subvert the requirements) have mucked up the practice of medicine. 


## Spring in the Northern Hemisphere Makes Cats Happy {: #alan-mittens}
{{ image(width="700", localsrc="2022/2022-03-24-alan-mittens.jpg", alt="Photograph of a black cat and a white and grey cat on the lawn with harnesses on.") }} 

It is warming up—70°F/21°C—earlier this week, and that means the cats want to go outside. 
We don't let them wander the neighborhood by themselves for their own protection. 
Each has a harness and about 50 feet (15 meters) of cord for them to roam the backyard. 
It is funny how just a little bit of sun can cheer up a cat. 

On the other hand, it has turned cool and rainy the remainder of the week, so the cat minder (me) is not all that interested in going outside. 
Once they have had the taste of the outdoors, it becomes tough to put up with their constant meowing and pawing at the glass. 
Just a little bit longer, Mittens and Alan...just a little bit longer.