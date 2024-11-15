---
layout: wordpress-import
status: published
published: true
title: '"Cautiously Optimistic"'
modified: 2006-06-13T22:21:58+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 70
wordpress_url: http://dltj.org/2006/06/cautiously-optimistic/
date: '2006-06-13 18:21:58 -0400'
date_gmt: '2006-06-13 23:21:58 -0400'
category: Disruption in Libraries
categories:
- Disruption in Libraries
tags:
- standards
- Joint Conference on Digital Libraries 2006
- metadata
- xml
- National Science Digital Library
- digital libraries
comments: []
---
<p>During the cookies and lemonade break during JCDL this afternoon I surprised one of the well-respected elders of the field with this question:  are we really making progress?  are we winning a fight against entropy <footnote><span class="removed_link" title="http://web.archive.org/web/20081119235034/http://www.himalayasaltcrystal.com/glossary.htm">Defined as</span>:  "Measure of disorganization or degradation in the universe that reduces available energy, or tendency of available energy to dwindle. Chaos, opposite of order."  Do you remember your Second Law of Thermodynamics?</footnote>?  I wasn't out for a quote for publication at the time so I won't reveal the individual's name, but I will report that there was a chuckle then the reply "cautiously optimistic."</p>
<p>This person went on to say that access to raw information has improved much over the last five years &mdash; that the internet and its tools have increased the capacity to publish and retrieve information.  'Sure,' s/he went on to say, 'we have a number of hard problems to solve &mdash; linking related object to each other and so forth &mdash; but we are making progress.'  I, too, offered a chuckle and agreed, and we went back to our cookies and lemonade.</p>
<p>Entropy and chaos are powerful forces, however, and it was just after this brief encounter that we heard from <a href="http://www.cs.cornell.edu/lagoze/" title="http://www.cs.cornell.edu/lagoze/">Carl Lagoze</a> with a talk called <a href="http://arxiv.org/abs/cs.DL/0601125" title="403 Forbidden">Metadata aggregation and "automated digital libraries": A Retrospective on the NSDL experience</a>.  Although the paper is a modestly dry report on the issues resolved and overcome in "running a relatively large-scale digital library (over a million objects) by collecting, processing, storing, and using metadata" <footnote>Lagoze, C., Krafft, D. B., Cornwell, T., Dushay, N., Eckstrom, D., Saylor, J. 200y. Metadata aggregation and "automated digital libraries": A retrospective on the NSDL experience. In <i>Proceedings of the 6th ACM/IEEE-CS Joint Conference on Digital Libraries</i> (Chapel Hill, NC, USA, June 11 - 15, 2005). JCDL '06. ACM Press, New York, NY, 231. [<a href="http://arxiv.org/abs/cs.DL/0601125" title="403 Forbidden">arXiv:cs.DL/0601125</a>]</footnote>, the oral presentation was anything but dry.  In fact, it offered a sobering reminder of how hard this is and the challenges before us.  He did it with four questions:</p>
<ol>
<li>What is a digital library anyway?</li>
<li>What is the role of metadata in a digital library?</li>
<li>What is "low barrier" technology? <i>[This one was tied to the observation that OAI-PMH, while modestly simple compared to other protocols, still requires a lot of effort to get right.  See reality lesson #4 below.]</i></li>
<li>Where should expensive and limited human energy be allocated?</li>
</ol>
<p>... and seven reality lessons:</p>
<ul>
<li>Reality lesson #1:  <i>Metadata is not being created</i><br />In truth, there is not a lot of funding set aside in projects to create metadata.</li>
<li>Reality lesson #2: <i>Participating as a metadata provider is complicated by a "knowledge gap"</i><br />
Doing so requires three skill sets that are frequently distinct: Domain expertise (e.g. "mathematics"); Metadata expertise (e.g. "Dublin Core"); and Technical expertise (e.g. encode it in XML and use a formal protocol).</li>
<li>Reality lesson #3: <i>Harvested metadata is not necessarily useful metadata</i><br />
"Correct" metadata is not necessarily "rich" metadata.  The general problem of metadata quality remains unsolved -- even the best automated/automatic transformations are not good enough.</li>
<li>Reality lesson #4: <i>OAI-PMH is not necessarily low-barrier and automatic</i><br />
Doing OAI-PMH right incorporates lots of details and assumed knowledge (UTF-8, XML schema validation, URL encoding, date stamping, resumption tokens, etc.).  An even after sometimes months of hand-holding data provider, the initial success does not persist in the majority of cases; the failure rate of subsequent harvests is high.  And the "incremental harvest" functionality is a nice concept but it doesn't work: support for "deleted" records is inconsistent in data providers; less than 50% of providers claim to persist deletions and many persistent claims are faulty.  Too often server failures and harvest failures require a full harvest 'resync'.</li>
<li>Reality lesson #5: <i>Human cost of large-scale harvesting is high</i><br />
In the case of NSDL, their metrics show that they exchange 170 messages per year per provider and that it takes on average 98 message exchanged for first harvest to succeed (which, as previously noted, subsequently fails).</li>
<li>Reality lesson #6: <i>Matching individual metadata records of equivalent resources is hard</i><br />I didn't have anything in my notes about this, but as I recall his comments were about the lack of ways to uniformly handle these surrogate objects in the OAI-PMH protocol.</li>
<li>Reality lesson #7: <i>Lots of (even good) metadata does not make a complete digital library (and maybe not even a digital library that is highly useful for education)</i><br />There is a real need to understand the value-add of a digital library: capturing the wisdom of the community served as well as focusing less on structured information and more on relationships among resources and user-derived relationships and annotations.</li>
</ul>
<p>So what do I think?  You know &mdash; I'm not sure.  These are tough problems, and the world would be a better place if they were solved.  We can demand answers, but sometimes there just isn't enough of a shoulder to stand on from the giant below.  Still, one can't help but wonder if all of the energy put into the collective "digital library" problem so far has just dissipated into chaos.</p>
