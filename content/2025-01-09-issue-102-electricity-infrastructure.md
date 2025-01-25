---
title: 'Issue 102: Electricity Infrastructure'
modified: 
category: Thursday Threads
categories:
- Thursday Threads
tags:
- electricity infrastructure
- data center infrastructure
- time standards
mastodon:

---
I'm about halfway through Saul Griffith's 2021 _{{ robustlink(href="https://mitpress.mit.edu/9780262545044/electrify/", versionurl="https://web.archive.org/web/20250109010246/https://mitpress.mit.edu/9780262545044/electrify/", versiondate="2025-01-08", title="Electrify: An Optimist's Playbook for Our Clean Energy Future | MIT Press", anchor="Electrify: An Optimist's Playbook for Our Clean Energy Future") }}_, and I find the author makes a compelling point about bringing nearly everything—energy creation, transmission, and use—to a common factor of "electricity" and then optimizing that system. 
There are many interesting problems to solve, but they seem solvable. 

In last week's _Thursday Threads_, I touched on how data centers impact the electrical grid. 
This week's issue looks further into how electricity is generated and distributed. 
The first article reflects back on the data center topic—it could have just as easily gone in last week's issue. 
Then there are a few other articles on the generation, storage, the flip away from carbon-based fuels, and a look at history.

This week:

- [Commercial Electricians in Demand]({filename}#electricians) for Data Center Construction
- Instability Cause By [Overgeneration of Rooftop Solar]({filename}#rooftop-solar)
- Generating Power from the [Tides]({filename}#tidal-power)
- Smarter Grid [Reduces Demand As Required]({filename}#smarter-grid)
- Storing Energy in [Mine Shafts]({filename}#gravity-battery)
- Storing Energy as [Compressed Air]({filename}#compressed-air)
- The Last Coal-fired Powerplant in Hawaii is [Replaced]({filename}#hawaii-battery)
- The [Rise of Renewables]({filename}#wind-and-solar-overtake-coal)
- [This Clock]({filename}#grid-clock) Made Power Grids Possible
- From Energy to [No Energy]({filename}#alan-keyboard)

Those are in addition to last week's:

- How the placement of data centers [impacts the local power grid]({filename}2025-01-02-issue-101-data-centers#power-grid)
- [Nuclear power is of interest again to feed into data centers]({filename}2025-01-02-issue-101-data-centers#nuclear-power)

{{ thursday_threads_header() }}


## Commercial Electricians in Demand for Data Center Construction {: #electricians}

{{ thursday_threads_quote(href="https://www.nytimes.com/2024/12/25/technology/ai-data-centers-electricians.html",
 blockquote='These traveling electricians are transforming the sagebrush here in central Washington, with substations going up on orchards and farmland. Hundreds have come to a triangle of counties tied together by hydropower dams along the Columbia River. They are chasing overtime and bonuses, working 60-hour weeks that can allow them to make as much as $2,800 a week after taxes. For all the hype over $100,000 chips and million-dollar engineers, the billions pouring into the infrastructure of A.I. is being built by former morticians, retired pro football linebackers, single moms, two dudes described as Gandalf in overalls, onetime bouncers and a roving legend known as Big Job Bob.',
 versiondate="2024-12-27",
 versionurl="https://web.archive.org/20241227160830/https://www.nytimes.com/2024/12/25/technology/ai-data-centers-electricians.html",
 anchor="A.I., the Electricians and the Boom Towns of Central Washington",
 post=", New York Times, 25-Dec-2024") }}

The _New York Times_ publishes this in-depth piece about the boom time for commercial electricians (or anyone who wants to train to become one).
Data centers require substantial electrical power to support the high computing needs of artificial intelligence and the storage to save your New Year's Eve photos (as well as the power to run the cooling systems for those computers). 
Although AI has propelled the construction of data centers to a sharper slope, significant building and expansion projects were already underway.
This article is a view at the intersection of traditional construction/labor, technology, land use, and economic growth.


## Instability Cause By Overgeneration of Rooftop Solar {: #rooftop-solar}

{{ thursday_threads_quote(href="https://www.abc.net.au/news/2024-12-02/aemo-demands-emergency-backstop-to-switch-off-solar/104670332",
 blockquote='[The Australian Energy Market Operator] said the ever growing output from solar was posing an increasing threat to the safety and security of the grid because it was pushing out all other forms of generation that were needed to help keep the system stable. And it warned that unless it had the power to reduce — or curtail — the amount of rooftop solar times, more drastic and damaging measures would need to be taken. These could include increasing the voltage levels in parts of the poles-and-wires network to "deliberately" trip or curtail small-scale solar in some areas. An even more dramatic step would be to "shed" or dump parts of the poles-and-wires network feeding big amounts of excess solar into the grid.',
 versiondate="2024-12-01",
 versionurl="https://web.archive.org/web/20241201212724/https://www.abc.net.au/news/2024-12-02/aemo-demands-emergency-backstop-to-switch-off-solar/104670332",
 anchor="AEMO wants emergency powers to switch off solar in every state amid fears of 'system collapse'",
 post=", Australian Broadcasting Company, 1-Dec-2024") }}

Electricity is unique in that the providers must exactly match the demand at every moment. 
Excess generation capacity must be removed from the grid...it is just as bad as too little electricity. 
(Storage of excess electricity is a topic all its own; see below.) 
In Australia, the rapid growth of solar power generation is making it difficult for the grid operator to achieve that balance. 
Rooftop solar is great, but having that energy dumped uncontrolled back onto the grid causes instability. 

(That isn't the only problem on the grid...there are devices that, as Grady of Practical Engineering {{ robustlink(href="https://practical.engineering/blog/2024/6/4/the-most-confusing-part-of-the-power-grid", versionurl="https://web.archive.org/web/20240806115156/https://practical.engineering/blog/2024/6/4/the-most-confusing-part-of-the-power-grid", versiondate="2024-08-06", title="The Most Confusing Part of the Power Grid | Practical Engineering", anchor="says") }}, "force the grid to produce power and move it through the system, even though they aren’t even consuming it.")


## Generating Power from the Tides {: #tidal-power}

{{ thursday_threads_quote(href="https://newatlas.com/energy/minesto-tidal-kite/",
 blockquote='Solar energy is the bedrock of most renewable energy grid plans – but lunar energy is even more predictable, and a number of different companies are working to commercialize energy generated from the regular inflows and outflows of the tides. One we&apos;ve completely missed is Minesto, which is taking a very different and remarkably dynamic approach compared to most. Where devices like Orbital&apos;s O2 tidal turbine more or less just sit there in the water harvesting energy from tidal currents, Minesto&apos;s Dragon series are anchored to the sea bed, and fly around like kites, treating the currents like wind.',
 versiondate="2024-02-14",
 versionurl="https://web.archive.org/20240214030847/https://newatlas.com/energy/minesto-tidal-kite/",
 anchor="28-ton, 1.2-megawatt tidal kite is now exporting power to the grid",
 post=", New Atlas, 11-Feb-2024") }}

The problem with variable sources like solar and wind is the need for a baseline supply of always-there electricity. 
Coal, natural gas, and nuclear are good at meeting that baseline power need. 
Tidal systems are a clean, constant source of energy as well.


## Smarter Grid Reduces Demand As Required {: #smarter-grid}

{{ thursday_threads_quote(href="https://www.technologyreview.com/2024/06/11/1093465/battery-swap-gogoro-taiwan-earthquake/",
 blockquote='On the morning of April 3, Taiwan was hit by a 7.4 magnitude earthquake. Seconds later, hundreds of battery-swap stations in Taiwan sensed something else: the power frequency of the electric grid took a sudden drop, a signal that some power plants had been disconnected in the disaster. The grid was now struggling to meet energy demand. These stations, built by the Taiwanese company Gogoro for electric-powered two-wheeled vehicles like scooters, mopeds, and bikes, reacted immediately. According to numbers provided by the company, 590 Gogoro battery-swap locations ... stopped drawing electricity from the grid, lowering local demand by a total six megawatts—enough to power thousands of homes. It took 12 minutes for the grid to recover, and the battery-swap stations then resumed normal operation.',
 versiondate="2024-06-16",
 versionurl="https://web.archive.org/20240616161906/https://www.technologyreview.com/2024/06/11/1093465/battery-swap-gogoro-taiwan-earthquake/",
 anchor="How battery-swap networks are preventing emergency blackouts",
 post=", MIT Technology Review, 11-Jun-2024") }}

In addition to managing the supply, there also needs to be advancements in managing the demand side. 
Businesses already do this...their flexibility to reduce their electricity usage during high-demand events results in cheaper electricity rates because the utility doesn't need to build as much capacity just-in-case. 
This kind of variable pricing is also available to some homeowners. 
However, technology on the grid can help support this as well. 
This article talks about a scooter battery charging company that automatically takes equipment offline when generation capacity unexpectedly drops. 
Imagine this same sort of grid intelligence available for e-vehicle charging stations as well. 


## Storing Energy in Mine Shafts {: #gravity-battery}

{{ thursday_threads_quote(href="https://www.euronews.com/green/2024/02/06/this-disused-mine-in-finland-is-being-turned-into-a-gravity-battery-to-store-renewable-ene",
 blockquote='One of Europe’s deepest mines is being transformed into an underground energy store. It will use gravity to retain excess power for when it is needed. The remote Finnish community of Pyhäjärvi is 450 kilometres north of Helsinki. Its more than 1,400-metre-deep zinc and copper Pyhäsalmi mine was decommissioned but is now being given a new lease of life by Scotland-based company Gravitricity. The firm has developed an energy storage system that raises and lowers weights, offering what it says are “some of the best characteristics of lithium-ion batteries and pumped hydro storage”.',
 versiondate="2024-07-19",
 versionurl="https://web.archive.org/20240719071028/https://www.euronews.com/green/2024/02/06/this-disused-mine-in-finland-is-being-turned-into-a-gravity-battery-to-store-renewable-ene",
 anchor="This disused mine in Finland is being turned into a gravity battery to store renewable energy",
 post=", Euro News, 6-Feb-2024") }}

Solar panels only produce power when the sun is out, and wind turbines only produce power when the wind blows. 
We will need a way to store energy during times of overproduction and send it out to the grid when demand requires it. 
Many technologies are being explored to use excess energy to pump water uphill or spin a heavy flywheel. 
The technique in this article raises weights in a deep mine shaft to store energy.


## Storing Energy as Compressed Air {: #compressed-air}

{{ thursday_threads_quote(href="https://insideclimatenews.org/news/02052024/inside-clean-energy-long-duration-energy-storage-technology/",
 blockquote='Toronto-based Hydrostor Inc. is one of the businesses developing long-duration energy storage that has moved beyond lab scale and is now focusing on building big things. The company makes systems that store energy underground in the form of compressed air, which can be released to produce electricity for eight hours or longer.',
 versiondate="2024-05-04",
 versionurl="https://web.archive.org/20240504181733/https://insideclimatenews.org/news/02052024/inside-clean-energy-long-duration-energy-storage-technology/",
 anchor="Hydrostor Inc., a leader in compressed air energy storage, aims to break ground on its first large plant by the end of this year",
 post=", Inside Climate News, 4-May-2024") }}

Another potential storage solution is compressed air. 
All of these systems have trade-offs of expense versus capacity versus location requirements and other factors. 
Some of these experiments will succeed, and some won't be commercially viable. 


## The Last Coal-fired Powerplant in Hawaii is Replaced {: #hawaii-battery}

{{ thursday_threads_quote(href="https://www.canarymedia.com/articles/energy-storage/a-huge-battery-has-replaced-hawaiis-last-coal-plant",
 blockquote='Hawaii shut down its last coal plant on September 1, 2022, eliminating 180 megawatts of fossil-fueled baseload power from the grid on Oahu — a crucial step in the state’s first-in-the-nation commitment to cease burning fossil fuels for electricity by 2045. But the move posed a question that’s becoming increasingly urgent as clean energy surges across the United States: How do you maintain a reliable grid while switching from familiar fossil plants to a portfolio of small and large renewables that run off the vagaries of the weather? Now Hawaii has an answer: It’s a gigantic battery, unlike the gigantic batteries that have been built before.',
 versiondate="2024-01-11",
 versionurl="https://web.archive.org/20240111140851/https://www.canarymedia.com/articles/energy-storage/a-huge-battery-has-replaced-hawaiis-last-coal-plant",
 anchor="A huge battery has replaced Hawaii's last coal plant",
 post=", Canary Media, 10-Jan-2024") }}

With new generation and storage technologies, where does that leave the traditional burning-carbon-based tools? 
Fortunately, not long for this world.


## The Rise of Renewables {: #wind-and-solar-overtake-coal}

{{ thursday_threads_quote(href="https://www.scientificamerican.com/article/u-s-wind-and-solar-are-on-track-to-overtake-coal-this-year/",
 blockquote='Wind and solar generated more power than coal through the first seven months of the year, federal data shows, in a first for renewable resources. The milestone had been long expected due to a steady stream of coal plant retirements and the rapid growth of wind and solar. Last year, wind and solar outpaced coal through May before the fossil fuel eventually overtook the pair when power demand surged in the summer. But the most recent statistics showed why wind and solar are on track in 2024 to exceed coal generation for an entire calendar year — with the renewable resources maintaining their lead through the heat of July.',
 versiondate="2024-08-18",
 versionurl="https://web.archive.org/web/20240818213601/https://www.scientificamerican.com/article/u-s-wind-and-solar-are-on-track-to-overtake-coal-this-year/",
 anchor="U.S. Wind and Solar Are on Track to Overtake Coal This Year",
 post=", Scientific American, 13-Aug-2024") }}

It would seem that the momentum away from burning carbon fuels is well established. 
I hope it is established enough to deal with the instability that could be caused by the incoming U.S. federal administration. 


## This Clock Made Power Grids Possible {: #grid-clock}

{{ thursday_threads_quote(href="https://spectrum.ieee.org/history-of-power-grid",
 blockquote=' On 23 October 1916, an engineer named Henry E. Warren quietly revolutionized power transmission by installing an electric clock in the L Street generating station of Boston’s Edison Electric Illuminating Co. This master station clock kept a very particular type of time: It used a synchronous self-starting motor in conjunction with a pendulum to help maintain the station’s AC electricity at a steady 60-cycle-per-second frequency. As more power stations adopted the clocks, the frequency regulation allowed them to share electricity and create an interconnected power grid.',
 versiondate="2024-03-03",
 versionurl="https://web.archive.org/20240303021049/https://spectrum.ieee.org/history-of-power-grid",
 anchor="This Clock Made Power Grids Possible",
 post=", IEEE Spectrum, 28-Feb-2024") }}

Before there was a grid, there were many isolated islands of power generation. 
The "alternating" part of "alternating current" meant that these islands couldn't be connected until the cycles of alternation could be synchronized. 
We take 60-cycles-per-second for granted now, but it wasn't always this way.


## From Energy to No Energy {: #alan-keyboard}

{{ image(width="600", localsrc="2025/2025-01-08-alan-keyboard.jpg", alt="Cat with black spots lounging on a person's lap near a keyboard and mouse, creating a cozy workspace environment.") }} 

This has become Alan's routine in the morning. 
It is far too cold—and now far too snowy—to work outside on the patio.
So Alan sleeps through the long winter days on my keyboard numeric pad until spring.















