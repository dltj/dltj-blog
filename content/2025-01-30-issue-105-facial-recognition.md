---
title: 'Issue 105: Facial Recognition'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- facial recognition
- law enforcement
- educational technology
- social media
mastodon:

---
In this week's _Thursday Threads_, I'll point to articles on the contentious subject of facial recognition technology. 
This tech, currently used by law enforcement and various businesses around the world, raises critical ethical and privacy questions. 
Beyond the instances where facial recognition use has resulted in wrongful apprehensions by law enforcement or fails to recognize a student taking an exam, we have examples of individuals taking the technology to the dystopian extreme: doxing smart glasses and invading the privacy of social media users. 
Even police officers are reluctant to submit to facial recognition, and in a surprising turn of events, places like China have started implementing restrictions on companies. 

It is possible that facial recognition might be useful in some circumstances someday. 
We're a long way from that day, though.

- Police forces are using facial recognition technology in the search for suspects, often [drastically altering the lives of innocent people]({filename}#eff-report)
- As if one layer of unregulated speculative technology wasn't bad enough, what could go wrong when you add a second: [using DNA to generate a face sketch to run through facial recognition]({filename}#dna)
- Why is the current iteration of facial recognition technology bad? Because sometimes [it doesn't even recognize faces]({filename}#protorio)
- Even police officers themselves [don't want to be subject to the whims and invasiveness of facial recognition]({filename}#police)
- When [the Chinese government tells companies to stop using facial recognition out of privacy concerns]({filename}#china), maybe everyone else should pay attention, too?
- Let's not do this: [smart glasses that display biographical sketches of the people you are looking at]({filename}#smart-glasses)
- Using social media to break the social contract: [doxing users based on the videos they post]({filename}#doxing-tiktok)
- Facial recognition technology has problems that—with effort and auditing—might be useful someday. Until that happens, [take advantage of opportunities to opt out where you can]({filename}#tsa-optout)
- This Week I Learned: [A biographer embedded with the Manhattan Project influenced what we think about the atomic bomb]({filename}#twil).
- Obligatory Cat Photo: [Alan's chair]({filename}#cats)

{{ thursday_threads_header() }}


## Catalog of police misuse {: #eff-report}
{{ thursday_threads_quote(href="https://www.eff.org/deeplinks/2025/01/police-use-face-recognition-continues-wrack-real-world-harms",
 blockquote='Police have shown, time and time again, that they cannot be trusted with face recognition technology (FRT). It is too dangerous, invasive, and in the hands of law enforcement, a perpetual liability. EFF has long argued that face recognition, whether it is fully accurate or not, is too dangerous for police use, and such use ought to be banned. Now, The Washington Post has proved one more reason for this ban: police claim to use FRT just as an investigatory lead, but in practice officers routinely ignore protocol and immediately arrest the most likely match spit out by the computer without first doing their own investigation.',
 versiondate="2025-01-21",
 versionurl="https://web.archive.org/web/20250121143817/https://www.eff.org/deeplinks/2025/01/police-use-face-recognition-continues-wrack-real-world-harms",
 anchor="Police Use of Face Recognition Continues to Wrack Up Real-World Harms",
 post=", Electronic Frontier Foundation, 15-Jan-2025") }}

I have saved a bunch of articles about law enforcement misuse of facial recognition technology, but rather than including them individually, I'm pointing to this article from the Electronic Frontier Foundation that catalogs the problems and points to individual cases.
The EFF analysis emphasizes that the technology poses significant risks to civil liberties and can lead to wrongful arrests. 
Despite claims from law enforcement that it is used merely as an investigatory tool, evidence shows that police often bypass protocols, leading to immediate arrests based solely on computer matches. 
It notes a troubling pattern where many individuals wrongfully arrested based on FRT are Black, underscoring the technology's lower accuracy for individuals with darker complexions. 


## Layering facial recognition atop DNA analysis {: #dna}
{{ thursday_threads_quote(href="https://www.wired.com/story/parabon-nanolabs-dna-face-models-police-facial-recognition/",
blockquote='Parabon NanoLabs ran the suspect’s DNA through its proprietary machine learning model. Soon, it provided the police department with something the detectives had never seen before: the face of a potential suspect, generated using only crime scene evidence.... The face of the murderer, the company predicted, was male. He had fair skin, brown eyes and hair, no freckles, and bushy eyebrows. A forensic artist employed by the company photoshopped a nondescript, close-cropped haircut onto the man and gave him a mustache—an artistic addition informed by a witness description and not the DNA sample. In a controversial 2017 decision, the department published the predicted face in an attempt to solicit tips from the public. Then, in 2020, one of the detectives did something civil liberties experts say is even more problematic—and a violation of Parabon NanoLabs’ terms of service: He asked to have the rendering run through facial recognition software.',
versionurl="https://web.archive.org/web/20240123055243/www.wired.com/story/parabon-nanolabs-dna-face-models-police-facial-recognition/", 
versiondate="2024-01-23", 
anchor="Cops Used DNA to Predict a Suspect’s Face—and Tried to Run Facial Recognition on It",
post=', WIRED, 22-Jan-2024') }}

This is perhaps the most egregious example of misuse: extrapolating an image of a suspect based on DNA analysis, then running that image through facial recognition technology in search of leads.


## When the face can't be found {: #proctorio}
{{ thursday_threads_quote(href="https://www.wired.com/story/student-exam-software-bias-proctorio/",
 blockquote='To prevent students from cheating, the university had bought software from the tech firm Proctorio, which uses face detection to verify the identity of the person taking the exam. But when Pocornie, who is Black, tried to scan her face, the software kept saying it couldn’t recognize her: stating “no face found.” That’s where the Ikea lamp came in. For that first exam in September 2020, and the nine others that followed, the only way Pocornie could get Proctorio’s software to recognize her was if she shone the lamp uncomfortably close to her face—flooding her features with white light during the middle of the day',
 versiondate="2023-04-07",
 versionurl="https://web.archive.org/web/20230406210957/https://www.wired.com/story/student-exam-software-bias-proctorio/",
 anchor="This Student Is Taking On ‘Biased’ Exam Software: Mandatory face-recognition tools have repeatedly failed to identify people with darker skin tones",
 post=", WIRED, 5-Apr-2023") }}

Here is one of the biggest problems of this unregulated technology: biases in the data used to train the algorithm call into question any results you get from it. 
The article discusses a student challenging biased exam software that may unfairly affect test outcomes. 
Just because a machine that can count and compare numbers really, really fast says something is true doesn't make it true.


## Police officers don't want to be subject to facial recognition {: #police}
{{ thursday_threads_quote(href="https://www.reviewjournal.com/local/local-las-vegas/nfl-facial-recognition-policy-upsets-las-vegas-police-union-3128202/",
 blockquote='A Las Vegas police union has raised concerns about a new NFL policy that would require officers who work security at Raiders games to share their photo for facial recognition purposes and is urging officers to think twice before complying. Traditionally, officers who worked overtime hours as security for Raiders games would receive a wristband that got them access to different parts of the field and stadium, explained Steve Grammas, president of the Las Vegas Police Protective Association. But now, the NFL is asking that officers each provide a photo, which will be used for “identification purposes when an individual steps up to a scanner to verify who the person is and if they have access to that particular space,” explained Tim Schlittner, director of communications for the NFL, in an email.',
 versiondate="2024-09-01",
 versionurl="https://web.archive.org/20240901001351/https://www.reviewjournal.com/local/local-las-vegas/nfl-facial-recognition-policy-upsets-las-vegas-police-union-3128202/",
 anchor="NFL facial recognition policy upsets Las Vegas police union",
 post=", Las Vegas Review-Journal, 14-Aug-2024") }}

Speaking of unregulated, police officers themselves don't want their biometrics cataloged in a company's database with no oversight. 
This also points to the problem of using biometrics as an authentication tool: the shape of your face isn't something you can easily change.
Suppose your facial markers leak from one of these companies. 
What stops someone from 3-D printing a facsimile of those markers to fool this technology?

## China tells companies to stop using facial technology {: #china}
{{ thursday_threads_quote(href="https://www.semafor.com/article/04/25/2024/china-says-no-more-facial-recognition-at-hotels",
 blockquote='Authorities in several major Chinese cities have ordered hotels to stop using facial recognition technology to verify the identity of guests in a sign the government is responding to public concerns over privacy, financial news site Caixin reported. Guests staying at hotels in Beijing, Shanghai, Shenzhen, and Hangzhou will now only be required to present identification in order to check in, according to state-run tabloid The Global Times.',
 versiondate="2024-05-03",
 versionurl="https://web.archive.org/20240503004735/https://www.semafor.com/article/04/25/2024/china-says-no-more-facial-recognition-at-hotels",
 anchor="China says no more facial recognition at hotels",
 post=", Semafor, 25-Apr-2024") }}

The government in China is well known for using facial recognition in public places for surveillance, so I think it is notable when the government responds to public pressure to stop companies from using the technology.


## Facial recognition in smart glasses {: #smart-glasses}
{{ thursday_threads_quote(href="https://www.404media.co/someone-put-facial-recognition-tech-onto-metas-smart-glasses-to-instantly-dox-strangers/",
 blockquote='The technology, which marries Meta’s smart Ray Ban glasses with the facial recognition service Pimeyes and some other tools, lets someone automatically go from face, to name, to phone number, and home address.',
 versiondate="2024-10-03",
 versionurl="https://web.archive.org/20241003131301/https://www.404media.co/someone-put-facial-recognition-tech-onto-metas-smart-glasses-to-instantly-dox-strangers/",
 anchor="Someone Put Facial Recognition Tech onto Meta's Smart Glasses to Instantly Dox Strangers",
 post=", 404 Media, 2-Oct-2024") }}

What happens when you pair off-the-shelf facial recognition with off-the-shelf smart glasses? 
Something very creepy. 
As a society, we're not nearly ready to dramatically change the social contract that this technology is demonstrating.


## Scanning the faces in social media videos {: #doxing-tiktok}
{{ thursday_threads_quote(href="https://www.404media.co/the-end-of-privacy-is-a-taylor-swift-fan-tiktok-account-armed-with-facial-recognition-tech/",
 blockquote='A viral TikTok account is doxing ordinary and otherwise anonymous people on the internet using off-the-shelf facial recognition technology, creating content and growing a following by taking advantage of a fundamental new truth: privacy is now essentially dead in public spaces. The 90,000 follower-strong account typically picks targets who appeared in other viral videos, or people suggested to the account in the comments. Many of the account’s videos show the process: screenshotting the video of the target, cropping images of the face, running those photos through facial recognition software, and then revealing the person’s full name, social media profile, and sometimes employer to millions of people who have liked the videos.... 404 Media is not naming the account because TikTok has decided to not remove it from the platform. TikTok told me the account does not violate its policies; one social media policy expert I spoke to said TikTok should reevaluate that position.',
 versiondate="2023-09-26",
 versionurl="https://web.archive.org/20230926000811/https://www.404media.co/the-end-of-privacy-is-a-taylor-swift-fan-tiktok-account-armed-with-facial-recognition-tech/",
 anchor="The End of Privacy is a Taylor Swift Fan TikTok Account Armed with Facial Recognition Tech",
 post=", 404 Media, 25-Sep-2023") }}

The "Taylor Swift Fan" part is quite click-baity. 
The article's author noted in the second paragraph that this anonymous TikTok user liked to focus on fan videos, but the content of the article stands on its own. 
Again: it is an off-the-shelf service that dramatically affects the social contract between humans.

## Sending a message at airport security gates {: #tsa-optout}
{{ thursday_threads_quote(href="https://gizmodo.com/senators-say-tsas-facial-recognition-program-is-out-of-control-heres-how-to-opt-out-2000528310",
 blockquote='A bipartisan group of 12 senators has urged the Transportation Security Administration’s inspector general to investigate the agency’s use of facial recognition, saying it poses a significant threat to privacy and civil liberties.... While the TSA’s facial recognition program is currently optional and only in a few dozen airports, the agency announced in June that it plans to expand the technology to more than 430 airports. And the senators’ letter quotes a talk given by TSA Administrator David Pekoske in 2023 in which he said “we will get to the point where we require biometrics across the board.” ... The latest letter urges the TSA’s inspector general to evaluate the agency’s facial recognition program to determine whether it’s resulted in a meaningful reduction in passenger delays, assess whether it’s prevented anyone on no-fly lists from boarding a plane, and identify how frequently it results in identity verification errors.',
 versiondate="2024-11-25",
 versionurl="https://web.archive.org/20241125151922/https://gizmodo.com/senators-say-tsas-facial-recognition-program-is-out-of-control-heres-how-to-opt-out-2000528310",
 anchor="Senators Say TSA's Facial Recognition Program Is Out of Control, Here's How to Opt Out",
 post=", Gizmodo, 22-Nov-2024") }}

Because of the problems with unregulated, unaudited facial recognition technology, I opt out of its use whenever possible. 
With study, evaluation, auditing, and quite possibly some regulation, this might become a useful technology for some use cases. 
Until that happens, my face will vote my consciousness: do not use it.


## This Week I Learned: A biographer embedded with the Manhattan Project influenced what we think about the atomic bomb {: #twil}

{{ thursday_threads_quote(href="https://www.wnycstudios.org/podcasts/otm/articles/wars-are-won-by-stories",
 blockquote='In early 1945, a fellow named Henry DeWolf Smyth was called into an office in Washington and asked if he would write this book that was about a new kind of weapon that the US was developing. The guy who had called him into his office, Vannevar Bush, knew that by the end of the year, the US was going to drop an atomic bomb that had the potential to end the war, but also that as soon as it was dropped, everybody was going to want to know what is this weapon, how was it made, and so forth. Smyth accepted the assignment. It was published by Princeton University Press about a week after the bomb was dropped. It explained how the US made the bomb, but it told a very specific kind of story, the Oppenheimer story that you see in the movies, where a group of shaggy-haired physicists figured out how to split the atom and fission, and all of this stuff. The thing is, the physics of building an atomic bomb is, in some respects, the least important part. More important, if you actually want to make the thing explode, is the chemistry, the metallurgy, the engineering that were left out of the story.',
 versiondate="2025-01-26",
 versionurl="https://web.archive.org/20250126210933/https://www.wnycstudios.org/podcasts/otm/articles/wars-are-won-by-stories",
 anchor="Wars Are Won By Stories",
 post=", On the Media, 22-Jan-2025") }}

The quote above comes from the transcript of this podcast episode. 
I've thought about this a lot in the past week as the Trump administration's flood-the-zone strategy overwhelms the senses. 
In a valiant effort to cover everything that is news, I can't help but wonder about the lost perspective of what _isn't_ being covered. 
And I wonder where I can look to find that perspective. 


## Alan's chair {: #cats}
{{ image(width="600", localsrc="2025/2025-01-30-alan-chair.jpg", alt="A white cat with black spots stretches across the back of a lounge chair seat.") }} 
Alan thinks he owns this chair...so much so that he is going to stretch out as big as he can to cover it. 
In reality, it is my chair. 
And, yes, right after taking this picture I insisted that he let me sit down. 
He got to take a nap in my lap, though.