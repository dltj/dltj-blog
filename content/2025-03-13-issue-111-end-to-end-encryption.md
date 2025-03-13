---
title: 'Issue 111: End-to-end Encryption'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- encryption
- privacy
- security
summary: "This Thursday Threads explores global security issues, encryption reforms, and tech giants’ countermeasures against quantum threats and AI, reinforcing the crucial role of end-to-end encryption in safeguarding privacy and communication."
bluesky: "Navigating the complex landscape of digital security, today's Thursday Threads post discusses recent global incidents including cyberattacks, government demands for data access, and encryption reforms. Amid these challenges, tech giants like Apple and the Signal Foundation are preparing for quantum computing threats and integrating AI technologies. The critical role of end-to-end encryption in protecting privacy and ensuring secure communications is a continuing focus."
---

This week's thread of articles looks at the ever-evolving landscape of digital security and privacy through end-to-end encryption. 
End-to-end encryption is a method of securing communication where only the people communicating can read the messages. 
In principle, it prevents potential eavesdroppers — including telecom providers, Internet providers, and even the provider of the communication service — from being able to access the cryptographic keys needed to decrypt the conversation. 
In practice, governments and others want to be able to put themselves in the middle of those conversations for both noble and dishonorable reasons. 
From unprecedented cyberattacks leading US officials to urge citizens to use encrypted messaging apps, to tech companies like Apple butting heads with the UK government over data privacy, the balance of power and privacy is under constant tension. 

- As much as the U.S. government fights for ways to bypass commercial encryption, I thought I'd never see [that same government urge the use of encrypted messaging apps]({filename}#salt-typhoon) in the wake of a major telecom breach.
- [Apple takes on the UK government]({filename}#apple-uk) over data access demands that would break the end-to-end encryption of its most secure systems.
- [Sweden's proposed backdoor law]({filename}#sweden) for encrypted messaging apps ignites global privacy concerns.
- Signal Foundation president warns of [threat to privacy]({filename}#whittaker) as an EU proposal to scan encrypted messages sparks cybersecurity concerns.
- The [Signal Foundation]({filename}#signal-post-quantum) and [Apple]({filename}#imessage-post-quantum) announce revisions to their messaging systems to deal with a post-quantum encryption threat.
- Exploring the [intersection of AI and end-to-end encryption]({filename}#ai). It isn't great when an AI agent wants to snoop on all of your conversations.
- [This Week I Learned]({filename}#twil): Plants reproduce by spreading little plant-like things.
- [This week's cat]({filename}#cats)

Also on DLTJ this past week:

- [My Economic Wake-Up Call Protest Sign]({filename}2025-03-08-tesla-takedown-march-8): A #TeslaTakedown Story

{{ thursday_threads_header() }}


## U.S. government urges use of encrypted messaging apps in the wake of a major telecom breach {: #salt-typhoon}
{{ thursday_threads_quote(href="https://www.nbcnews.com/tech/security/us-officials-urge-americans-use-encrypted-apps-cyberattack-rcna182694",
 blockquote='Amid an unprecedented cyberattack on telecommunications companies such as AT&T and Verizon, U.S. officials have recommended that Americans use encrypted messaging apps to ensure their communications stay hidden from foreign hackers. The hacking campaign, nicknamed Salt Typhoon by Microsoft, is one of the largest intelligence compromises in U.S. history, and it has not yet been fully remediated. Officials on a news call Tuesday refused to set a timetable for declaring the country’s telecommunications systems free of interlopers. Officials had told NBC News that China hacked AT&T, Verizon and Lumen Technologies to spy on customers.',
 versiondate="2024-12-10",
 versionurl="https://web.archive.org/web/20241206032411/https://www.nbcnews.com/tech/security/us-officials-urge-americans-use-encrypted-apps-cyberattack-rcna182694",
 anchor="U.S. officials urge Americans to use encrypted apps amid cyberattack",
 post=", NBC News, 3-Dec-2024") }}

Late last year, the U.S. announced a significant attack against telecommunication companies. 
This hacking campaign, known as Salt Typhoon, is one of the largest intelligence breaches in U.S. history, with officials stating that the full extent of the compromise has not been resolved. 
The attackers accessed various types of sensitive information, including call metadata and live conversations of specific targets, notably around Washington, D.C. 
In light of that, the FBI and CISA recommended that Americans use messaging apps that feature end-to-end encryption. 
There is more than just a touch of irony here because federal law enforcement pushed for the passage of the Communications Assistance for Law Enforcement Act (CALEA) in the mid-1990s that put backdoors into telecommunications equipment for law enforcement.
It was these backdoors that were used by the Salt Typhoon attackers. 
_There is no such thing as an encryption backdoor that will only be used by authorized law enforcement._


## Apple takes on the UK government over data access demands {: #apple-uk}
{{ thursday_threads_quote(href="https://www.bbc.com/news/articles/c8rkpv50x01o",
 blockquote='Apple is taking legal action to try to overturn a demand made by the UK government to view its customers&apos; private data if required... It is the latest development in an unprecedented row between one of the world&apos;s biggest tech firms and the UK government over data privacy. In January, Apple was issued with a secret order by the Home Office to share encrypted data belonging to Apple users around the world with UK law enforcement in the event of a potential national security threat. Data protected by Apple&apos;s standard level of encryption is still accessible by the company if a warrant is issued, but the firm cannot view or share data encrypted using its toughest privacy tool, Advanced Data Protection (ADP). ADP is an opt-in feature and it is not known how many people use it.',
 versiondate="2025-03-11",
 versionurl="https://web.archive.org/20250311020907/https://www.bbc.com/news/articles/c8rkpv50x01o",
 anchor="Apple takes legal action in UK data privacy row",
 post=", BBC News, 4-Mar-2025") }}

In response to the UK order, Apple removed ADP from the UK market rather than create a "backdoor" for access. 
The UK Home Office maintains that privacy is only compromised in exceptional cases related to serious crimes. 
But, as the previous article points out, there is no such thing as a law-enforcement-only capability; if there is a weakness in an encryption system, it will eventually be exploited by someone with the time or talent to break it.


## Sweden's proposed backdoor in encrypted messaging apps ignites global privacy concerns {: #sweden}
{{ thursday_threads_quote(href="https://therecord.media/sweden-seeks-backdoor-access-to-messaging-apps",
 blockquote='Sweden’s law enforcement and security agencies are pushing legislation to force Signal and WhatsApp to create technical backdoors allowing them to access communications sent over the encrypted messaging apps.... The bill could be taken up by the Riksdag, Sweden’s parliament, next year if law enforcement succeeds in getting it before the relevant committee, SVT Nyheter reported. The legislation states that Signal and WhatsApp must retain messages and allow the Swedish Security Service and police to ask for and receive criminal suspects’ message histories, the outlet reported. Minister of Justice Gunnar Strömmer told the Swedish press that it is vital for Swedish authorities to access the data.',
 versiondate="2025-02-28",
 versionurl="https://web.archive.org/20250301013425/https://therecord.media/sweden-seeks-backdoor-access-to-messaging-apps",
 anchor="Swedish authorities seek backdoor to encrypted messaging apps",
 post=", The Record, 25-Feb-2025") }}
 
A few paragraphs down in the article, the Swedish Armed Forces are mentioned as opposing the bill because they routinely use Signal, and a backdoor could introduce vulnerabilities that bad actors could exploit.


## Signal Foundation president warns of threat to privacy {: #whittaker} 
{{ thursday_threads_quote(href="https://techcrunch.com/2024/06/17/stop-playing-games-with-online-security-signal-president-warns-eu-lawmakers/",
 blockquote='',
 versiondate="2024-06-18",
 versionurl="https://web.archive.org/20240618181135/https://techcrunch.com/2024/06/17/stop-playing-games-with-online-security-signal-president-warns-eu-lawmakers/",
 anchor="Stop playing games with online security, Signal president warns EU lawmakers",
 post=", TechCrunch, 17-Jun-2024") }}

The open source Signal messaging app is considered the gold standard for end-to-end encrypted messaging. 
Meridith Whittaker is the president of the Signal Foundation, and she has strong words for lawmakers' efforts to weaken encryption algorithms. 
Ms Whittaker was also quoted in the previous article about Sweden's efforts.
The European Commission originally proposed legislation to scan private messages for child sexual abuse material, but the European Parliament has rejected the approach. 
Experts like Whittaker argue this would create vulnerabilities that could be exploited by hackers and hostile states. 
The EU's data protection supervisor has also voiced concerns that the plan threatens democratic values.
 
 
## Signal Foundation prepares for quantum threats with a revision to its end-to-end encryption protocol {: #signal-post-quantum}
{{ thursday_threads_quote(href="https://arstechnica.com/security/2023/09/signal-preps-its-encryption-engine-for-the-quantum-doomsday-inevitability/",
 blockquote='The Signal Foundation, maker of the Signal Protocol that encrypts messages sent by more than a billion people, has rolled out an update designed to prepare for a very real prospect that’s never far from the thoughts of just about every security engineer on the planet: the catastrophic fall of cryptographic protocols that secure some of the most sensitive secrets today. The Signal Protocol is a key ingredient in the Signal, Google RCS, and WhatsApp messengers, which collectively have more than 1 billion users.',
 versiondate="2023-09-23",
 versionurl="https://web.archive.org/20230922232046/https://arstechnica.com/security/2023/09/signal-preps-its-encryption-engine-for-the-quantum-doomsday-inevitability/",
 anchor="The Signal Protocol used by 1+ billion people is getting a post-quantum makeover",
 post=", Ars Technica, 20-Sep-2023") }}

I don't know if quantum computing will be what breaks the current generation of encryption protocols, but progress in faster hardware and more research into encryption means that the day will come at some point. 
The Signal protocol revision uses a "post-quantum cryptography algorithm" adopted by the U.S. National Institute of Standards and Technology (NIST).
There are researchers on both sides of this divide: those working to advance encryption protocols and those seeking to break them.


## Apple Launches Post-Quantum Encryption in iMessage {: #imessage-post-quantum}
{{ thursday_threads_quote(href="https://www.wired.com/story/apple-pq3-post-quantum-encryption/",
 blockquote='While practical quantum computing technology may still be years or decades away, security officials, tech companies, and governments are ramping up their efforts to start using a new generation of post-quantum cryptography. These new encryption algorithms will, in short, protect our current systems against any potential quantum computing-based attacks. Today Cupertino is announcing that PQ3—its post-quantum cryptographic protocol—will be included in iMessage.',
 versiondate="2024-02-23",
 versionurl="https://web.archive.org/20240223002217/https://www.wired.com/story/apple-pq3-post-quantum-encryption/",
 anchor="iMessage Gets Post-Quantum Encryption in New Update",
 post=", WIRED, 21-Feb-2024") }}

Apple follows Signal's lead in deploying its own quantum-safe encryption protocol for iMessage. 
Apple is using the same Kyber algorithm tha Signal adopted.
Deploying post-quantum encryption now aims to limit the impact of "harvest now, decrypt later" attacks, where encrypted data is collected and held until quantum computers can break it.


## Exploring the intersection of AI and end-to-end encryption {: #ai}
{{ thursday_threads_quote(href="https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/",
 blockquote='Recently I came across a fantastic new paper by a group of NYU and Cornell researchers entitled “How to think about end-to-end encryption and AI.”... I was particularly happy to see people thinking about this topic, since it’s been on my mind in a half-formed state this past few months. On the one hand, my interest in the topic was piqued by the deployment of new AI assistant systems like Google’s scam call protection and Apple Intelligence, both of which aim to put AI basically everywhere on your phone — even, critically, right in the middle of your private messages. On the other hand, I’ve been thinking about the negative privacy implications of AI due to the recent European debate over “mandatory content scanning” laws that would require machine learning systems to scan virtually every private message you send.',
 versiondate="2025-01-21",
 versionurl="https://web.archive.org/20250121053440/https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/",
 anchor="Let’s talk about AI and end-to-end encryption",
 post=", Matthew Green, 17-Jan-2025") }}

This blog post discusses the implications of AI technologies on the security and privacy of encrypted communications. 
The author emphasizes the importance of maintaining robust encryption standards in the face of evolving AI capabilities that could potentially undermine these protections. 
Take, for example, the need for AI agents to be snooping in on your conversations so it has the context to take actions on your behalf: "Agent, book a two-person reservation at the restaurant Dave just messaged me about."
The author advocates for a collaborative approach between cryptographers and AI developers to ensure that AI advancements do not compromise encrypted data security. 


## This Week I Learned: Plants reproduce by spreading little plant-like things {: #twil}
{{ thursday_threads_quote(href="https://www.youtube.com/watch?v=8o76s9alLeo",
 blockquote="This is where pollen comes in. Like sperm, pollen contains one DNA set from its parent, but unlike sperm, pollen itself is actually its own separate living plant made of multiple cells that under the right conditions can live for months depending on the species... So this tiny male offspring plant is ejected out into the world, biding its time until it meets up with its counterpart. The female offspring of the plant, called an embryosac, which you're probably less familiar with since they basically never leave home. They just stay inside flowers. Like again, they're not part of the flower. They are a separate plant living inside the flower. Once the pollen meets an embryosac, the pollen builds a tube to bridge the gap between them. Now it's time for the sperm. At this point, the pollen produces exactly two sperm cells, which it pipes over to the embryosac,
which in the meantime has produced an egg that the sperm can meet up with. Once fertilized, that egg develops into an embryo within the embryosac, hence the name, then a seed and then with luck a new plant. This one with two sets of DNA.",
 versiondate="2025-03-12",
 versionurl="https://web.archive.org/web/20250312010545/https://www.youtube.com/watch?v=8o76s9alLeo",
 anchor="Pollen Is Not Plant Sperm (It’s MUCH Weirder)",
 post=", MinuteEarth, 7-Mar-2025") }}
Pollen is not sperm...it is a separate living thing! 
And it meets up with another separate living thing to make a seed!
Weird!
The video is only three and a half minutes long, and it is well worth checking out at some point today.

What did you learn this week? Let me know on [Mastodon](https://code4lib.social/@dltj/114155067449618484) or [Bluesky](https://bsky.app/profile/dltj.org/post/3lkb37al3ql2c).


## Pickle and Mittens bask in a sunspot {: #cats}
  {{ image(width="600", localsrc="2025/2025-03-13-pickle-mittens-sunspot.jpg", alt="Two cats basking in a sunbeam on a carpeted floor. One black and white cat lies on its back, while the other stretches out comfortably. A woven basket and a cat toy are nearby, enhancing the cozy scene.") }} 
