---
title: 'Issue 101: Data Centers'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- data center infrastructure
- building LLMs
- cryptocurrency mining
- electricity infrastructure
mastodon:

---
One of the very first issues of Thursday Threads was on [data centers]({filename}/2011-04-28-thursday-threads-2011w17) (2011). 
That issue had articles on a major Amazon Web Services outage, remote data centers powered by renewable energy, and videos about Google's and Meta's data centers. 
Unfortunately, I've found that the videos are lost to time. 
It is interesting that the concerns about data centers lives on.
This post continues that thread with these topics:

- How the placement of data centers [impacts the local power grid]({filename}#power-grid)
- How [environmental noise of a data center is a problem its neighbors]({filename}#noise)
- [Nuclear power is of interest again to feed into data centers]({filename}#nuclear-power)
- [Data center growth in Africa]({filename}#africa)

Also recently on <i>DLTJ</i>:

- [One Year of Learning 2024]({filename}2024-12-14-one-year-of-learning-2024): a list of 13 interesting things I learned last year.
- [As a Cog in the Election System Again: Reflections on Working the 2024 Presidential Election]({filename}2024-11-10-election-reflection-2024)

{{ thursday_threads_header() }}


## AI-driven Data Center Development's Impact on Local Grid Users {: #power-grid}
{{ image(width="524", div_float="right", localsrc="2025/2025-01-02-bloomberg-data-center-map.jpg", caption="Map from Bloomberg shows local average of sensors' worst total harmonic distortion readings from February to October; areas with an average of 8% or more are deemed as exceeding accepted industry limits.", alt="U.S. map highlights cities with over 8% total harmonic distortion and significant data center activity in megawatts, 2024 data.") }}

{{ thursday_threads_quote(href="https://www.bloomberg.com/graphics/2024-ai-power-home-appliances/?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTczNTMxNjk3OCwiZXhwIjoxNzM1OTIxNzc4LCJhcnRpY2xlSWQiOiJTUDVUUzhUMEFGQjQwMCIsImJjb25uZWN0SWQiOiI0MDVBMTQxMTI3MTM0MDM3OENCMDNDQTY4Nzc3MEQ5RiJ9.l1UB8xJFHoagQebxlg8czxgiT1cP3oxHhX2m_82DdH0&leadSource=uverify%20wall",
 blockquote='AI data centers are multiplying across the US and sucking up huge amounts of power. New evidence shows they may also be distorting the normal flow of electricity for millions of Americans. This map shows readings from about 770,000 home sensors, with red zones indicating areas with the most distorted power. The problem is threatening billions in damage to home appliances and aging power equipment, especially in areas like Chicago and "data center alley" in Northern Virginia, where distorted power readings are above recommended levels. An exclusive Bloomberg analysis shows that more than three-quarters of highly-distorted power readings across the country are within 50 miles of significant data center activity. While many facilities are popping up near major US cities and adding stress to already fragile grids, this trend holds true in rural areas as well.',
 versiondate="2024-12-28",
 versionurl="https://web.archive.org/20241228050818/https://www.bloomberg.com/tosv2.html?vid=&uuid=bff3126f-c4d9-11ef-a1f8-4f5201ceb714&url=L2dyYXBoaWNzLzIwMjQtYWktcG93ZXItaG9tZS1hcHBsaWFuY2VzLz9hY2Nlc3NUb2tlbj1leUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKemIzVnlZMlVpT2lKVGRXSnpZM0pwWW1WeVIybG1kR1ZrUVhKMGFXTnNaU0lzSW1saGRDSTZNVGN6TlRNeE5qazNPQ3dpWlhod0lqb3hOek0xT1RJeE56YzRMQ0poY25ScFkyeGxTV1FpT2lKVFVEVlVVemhVTUVGR1FqUXdNQ0lzSW1KamIyNXVaV04wU1dRaU9pSTBNRFZCTVRReE1USTNNVE0wTURNM09FTkNNRE5EUVRZNE56YzNNRVE1UmlKOS5sMVVCOHhKRkhvYWdRZWJ4bGc4Y3p4Z2lUMWNQM294SGhYMm1fODJEZEgwJmxlYWRTb3VyY2U9dXZlcmlmeSUyMHdhbGw=",
 anchor="AI Power Needs Threaten Billions in Damages for US Households",
 post=", Bloomberg, 27-Dec-2024") }}

There has been much written about how data center development is moving into areas where it can soak up cheap excess electricity. 
This is the first I've heard about how data center power draws can distort or even harm the grid for existing customers. 
Set aside about how the article is framed as another way that the creation of AI-driven products is harmful; data centers are going to be built no matter what the purpose. 
As the nation's power grid is restructured to incorporate more renewable source and power storage mechanisms, this is yet another factor that will make that transition more challenging.

It isn't just power; water use — primarily for cooling — is also a concern: 
{{ robustlink(href="https://apnews.com/article/chatgpt-gpt4-iowa-ai-water-consumption-microsoft-f551fde98083d17a7e8d904f8be822c4", versionurl="https://web.archive.org/20230913031118/https://apnews.com/article/chatgpt-gpt4-iowa-ai-water-consumption-microsoft-f551fde98083d17a7e8d904f8be822c4", versiondate="2023-09-13", title="Artificial intelligence technology behind ChatGPT was built in Iowa — with a lot of water | AP News", anchor='"Artificial intelligence technology behind ChatGPT was built in Iowa — with a lot of water"') }}. 


## Cryptocurrency Mining Rigs are not a Welcome Addition to this Texas Town {: #noise}

{{ thursday_threads_quote(href="https://www.wired.com/story/the-worlds-biggest-bitcoin-mine-is-rattling-this-texas-oil-town/",
 blockquote='Corsicana, the seat of Navarro County, is best known for kicking off the Texas oil boom in 1894, when a 1,000-foot well meant to alleviate a water shortage instead turned up an oil field that extended for miles. In the century to follow, tens of millions of barrels of oil were pulled from the city—and Corsicana got rich... The oil fields are drying up. In Riot&apos;s high temple of cryptographic computation, local officials think they&apos;ve found a stopgap. Some Corsicana residents aren&apos;t so sure. They see the facility as a blot on the landscape that threatens their property values, vulnerable energy grid, and quiet rural lifestyle. And they&apos;re fighting back.',
 versiondate="2024-09-11",
 versionurl="https://web.archive.org/20240911130913/https://www.wired.com/story/the-worlds-biggest-bitcoin-mine-is-rattling-this-texas-oil-town/",
 anchor="The World’s Biggest Bitcoin Mine Is Rattling This Texas Oil Town",
 post=", Wired, 11-Sep-2024") }}
 
The article highlights the tension between data center development and community concerns, drawing parallels between the historical oil industry and the current rise of bitcoin mining in the region. 
Despite claims from the developer that their operations will stabilize the grid, critics argue that cryptocurrency mining is a drain on resources and exacerbates noise pollution. 
Residents want local governments to address the issues where noise has led to health issues and disrupted lives. 

It isn't just rural areas, either; {{ robustlink(href="https://hackernoon.com/will-data-centers-ruin-your-neighborhood", versionurl="https://web.archive.org/20240929191214/https://hackernoon.com/will-data-centers-ruin-your-neighborhood", versiondate="2024-09-29", title="Will Data Centers Ruin Your Neighborhood? | Hackernoon", anchor="suburban Virginia") }} and {{ robustlink(href="https://www.datacenterdynamics.com/en/news/chicago-residents-complain-of-noise-from-digital-realty-data-center/", versiondate="2025-01-02", title="Chicago residents complain of noise from Digital Realty data center | Data Center Dynamics", anchor="downtown Chicago") }} are also affected.


## Data Center Development Causes Resurgence in Nuclear Power Interest {: #nuclear-power}

{{ thursday_threads_quote(href="https://arstechnica.com/science/2024/10/amazon-the-latest-tech-giant-to-announce-investments-in-nuclear/",
 blockquote='On Tuesday, Google announced that it had made a power purchase agreement for electricity generated by a small modular nuclear reactor design that hasn&apos;t even received regulatory approval yet. Today, it&apos;s Amazon&apos;s turn. The company&apos;s Amazon Web Services (AWS) group has announced three different investments, including one targeting a different startup that has its own design for small, modular nuclear reactors—one that has not yet received regulatory approval.',
 versiondate="2024-11-15",
 versionurl="https://web.archive.org/20241115023112/https://arstechnica.com/science/2024/10/amazon-the-latest-tech-giant-to-announce-investments-in-nuclear/",
 anchor="Amazon joins Google in investing in small modular nuclear power",
 post=", Ars Technica, 16-Oct-2024") }}

Amazon Web Services has joined other tech giants like Google in investing in small modular nuclear power, reflecting a growing interest in nuclear energy among major companies. 
The interest in small modular reactors stems from increasing energy demands, particularly from data centers, and the challenges of relying solely on renewable energy sources. 
While renewables are cost-effective, their intermittent nature and grid connection issues limit their viability for continuous power needs. 
The lengthy and costly construction timelines of large reactors further complicate the situation, making small modular reactors a more appealing option despite their unproven status.

Don't count out Microsoft...it wants to {{ robustlink(href="https://www.reuters.com/markets/deals/constellation-inks-power-supply-deal-with-microsoft-2024-09-20/", versionurl="https://web.archive.org/20240922025629/https://www.reuters.com/markets/deals/constellation-inks-power-supply-deal-with-microsoft-2024-09-20/", versiondate="2024-09-21", title="Microsoft deal propels Three Mile Island restart, with key permits still needed | Reuters", anchor="restart and refurbish Three Mile Island reactors") }} as part of its data center energy plans. 
Key permits are still needed before this is fully in place, though.


## Africa Sees Jump in Data Center Construction {: #africa}

{{ thursday_threads_quote(href="https://www.semafor.com/article/06/22/2023/data-centers-fuel-cloud-computing-in-smaller-african-countries",
 blockquote='A new generation of data centers are being built in Africa&apos;s smaller economies, fueling a $5 billion market opportunity on the world&apos;s fastest growing continent.... The emergence of local data centers has powered a surge in cloud-based computing in five of Africa&apos;s largest economies — South Africa, Nigeria, Kenya, Egypt and Morocco — in the last five years. Now the number of data centers built in smaller African economies is surging as well, with up to $700 million of capital investment pouring in each year in the past two years, according to data from research firm Xalam Analytics which monitors the industry.',
 versiondate="2023-06-25",
 versionurl="https://web.archive.org/web/20230625022040/https://www.semafor.com/article/06/22/2023/data-centers-fuel-cloud-computing-in-smaller-african-countries",
 anchor="Data centers fuel cloud computing in smaller African countries",
 post=", Semafor, 22-Jun-2023") }}

The rise of data centers in Africa will hopefully solve economic disparities and enhance digital sovereignty on the continent. 
For instance, improved proximity to data centers will lower transit costs for internet service providers, potentially boosting online economic activity. 
(Historically, African data has been stored internationally, leading to slower connections and complicating compliance with local privacy laws.) 
Connectivity — especially below the equator — remains an issue, though; {{ robustlink(href="https://restofworld.org/2022/google-meta-underwater-cables/", versionurl="https://web.archive.org/web/20220512020824/https://restofworld.org/2022/google-meta-underwater-cables/", versiondate="2022-07-22", title="Google and Meta’s underwater cables up the stakes on internet control | Rest of the World", anchor='"Google and Meta’s underwater cables up the stakes on internet control"') }}

Although some African countries welcome the new data centers, others are concerned. 
Chile, for instance, has {{ robustlink(href="https://restofworld.org/2024/data-centers-environmental-issues/", versionurl="https://web.archive.org/20240603141058/https://restofworld.org/2024/data-centers-environmental-issues/", versiondate="2024-06-03", title="Data centers bring environmental concerns, like excess water use, to Chile | Rest of the World", anchor='"multiple groups working to keep Amazon, Google, and Microsoft from doubling the number of centers in the country, fearing environmental devastation"') }}.
And a {{ robustlink(href="https://www.ft.com/content/f85aa254-d453-4542-a50e-fa1171971ab0", versionurl="https://archive.ph/g82yq", versiondate="2023-03-28", title="European ammunition maker says plant expansion hit by energy-guzzling TikTok site: Norwegian group Nammo blames ‘storage of cat videos’ for threatening its growth as data centre corners spare electricity | Financial Times", anchor="a Norwegian ammunition manufacturer blames ‘storage of cat videos’ for threatening its growth") }}.


## Speaking of cats... {: #mittens-food-box}

{{ captioned(
    width="700",
    caption="Mittens' Food Box",
    contents='<video width="700" controls><source src="/assets/images/2025/2025-01-02-mittens-food-box.mp4" type="video/mp4"></video>') }}
    
We have a temporary third cat, Pickle, in our home that is _very_ food driven. 
It will bully the other cats away from their food. 
(Pickle is also known for stealing and eating whole chocolate chip muffins from the breakfast table, too.)
So we added one of those microchip-enabled pet doors to this plastic tote so our first cat, Mittens, can eat in peace.


