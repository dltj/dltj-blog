---
layout: wordpress-import
status: published
published: true
title: 'Minutes of the FEDORA Workflow Working Group meeting of 18-Jun-2006'
modified: 2006-06-21T00:10:44+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 74
wordpress_url: http://dltj.org/2006/06/fedora-workflow-minutes/
date: '2006-06-20 20:10:44 -0400'
date_gmt: '2006-06-21 01:10:44 -0400'
category: Library Technology
categories:
- Meta Category
- Workflow
- Library SOA
tags:
- service-oriented architecture
- library service-oriented architecture
- bpel
- library 2.0
- activebpel
- jbpm
- Fedora Repository
comments: []
---
<div style="border: 1px dashed black; padding: .75em">
Please note -- this is a copy of the <span class="removed_link" title="http://www.fedora.info/wiki/index.php/Working_Group:_Workflow:Minutes-20060618">FEDORA Workflow Working Group minutes</span> from the FEDORA Wiki.  It is being posted here in order to get it into the blogosphere at the right places.  Please make comments on the FEDORA Wiki <span class="removed_link" title="http://www.fedora.info/wiki/index.php/Talk:Working_Group:_Workflow:Minutes-20060618">"talk" page</span> rather than on this posting.
</div>
<h1>FEDORA Workflow Working Group Meeting</h1>
<p>18-Jun-2006, University of Virginia</p>
<p>Attending:  Grace Agnew, Rutgers U.; Chris Awre, U. of Hull; Dan Davis, Harris Corp.; <span class="removed_link" title="http://www.fedora.info/wiki/index.php/User:Richard_green">Richard Green</span>, U. of Hull; <span class="removed_link" title="http://www.fedora.info/wiki/index.php/User:PeterAtOhioLINK">Peter Murray</span>, OhioLINK; <span class="removed_link" title="/wiki/index.php/User:Matthias">Matthias Razum</span>, FIZ Karlsruhe; Bill Parod, Northwestern U; Adam Soroka, U. of Virginia; Thorny Staples, U. of Virginia; <span class="removed_link" title="http://www.fedora.info/wiki/index.php/User:Rwayland">Ross Wayland</span>, U. of Virginia</p>
<h2>Review of Minutes from 6 Dec 2005</h2>
<p>One of the assumptions in the 6 Dec 2005 minutes is:  "an object repository built on FEDORA should be seen as a write rarely, read mostly application".  Some participants noted that the repository is viewed as part of a working tool for scholars, which makes "writes" not so 'rare'. This kind of assumption is useful for characterize FEDORA-based application as something other than a RDBMS. A clarifying comparison is the frequency of transactions when "saving a file" (once every 10 minutes) versus "banking transactions" (thousands of transactions/second).  This characterization helps define the efficiency needs of reads over writes.</p>
<p>A revised assumption was offered: "<i>FEDORA is typically an application where reads typically exceed writes.</i>"</p>
<p>It was also noted that the working group charter and the assumptions make reference to "BPEL" as the only workflow orchestration engine, excluding other tools such as JBPM.  This is not intentional, and does not necessarily reflect a decision to use only BPEL-based engines.  The participants noted, however, that no one envisions writing a new workflow engine from scratch.</p>
<h2> Participant Desires and Status Review of Workflow-related Activities </h2>
<h3> FIRE/Workflow 0.1 client update </h3>
<p>The December meeting envisioned work on the NSDL NCCS/FIRE client as the starting point for embedding workflow capabilities into FEDORA.  The FEDORA core development team looked at both ActiveBPEL and JBPM for integration into the FEDORA-SF and determined that within their available time that the core developers needed to hardwire the workflow into the client with the desire to apply a workflow orchestration engine in a later release.</p>
<h3> FEDORA Repository update </h3>
<p>Transforming FEDORA to be built as a WAR file is almost completed.  Adding generic "messaging" in FEDORA is one task on the list of desired for core developer team to prioritize and assign in September.</p>
<h3> Max Plank Society: eSciDoc </h3>
<h4> Overview </h4>
<p>Max Planck Society is made up of 82 institutes, each with many working groups.  The <span class="removed_link" title="http://www.fedora.info/wiki/index.php/ESciDoc_Project">ESciDoc_Project</span> is building one repository for all of these institutes and working groups in disciplines ranging from humanities to sciences.  In interviews with users, the eSciDoc development team has determined that each user group will likely want a near infinite diversity of combination of workflow steps.  eSciDoc developers have built a framework layer around FEDORA and will be putting a workflow engine for human-in-the-loop and process-to-process steps.</p>
<h4> Update </h4>
<p>The eSciDoc development team has decided to use JBPM.  In an experiment with ActiveBPEL, without using advanced tools (at the time of the experiment, the ActiveBPEL editor tool was not freely available), setting up a workflow involving interactions between two services took several days and editing 13 BPEL-related files as opposed to just editing one file with JBPM.  Their thinking is that the eScieDoc developers will interview users to model the end users' workflow needs, then create the workflow script in JBPM for that group.</p>
<h3> Harris Corporation </h3>
<h4> Update </h4>
<p>Submitted a bid for NARA's ERA system (records management archive) but were not successful.  Harris Corp. is still working with FEDORA and is looking for other opportunities to use it in service integration proposals.  Harris Corp. is using the IBM engine (has both the human-in-the-loop and the process-to-process capabilities); it is arguably the most advanced out there, but it is still not mature as this field continues to grow.  Existing engines "make it look easy" by limiting the kinds of workflow activities that can be done, and open source implementations are many steps back because the advanced tools are only now coming out.</p>
<h3> U. of Hull: RepoMMan </h3>
<h4> Desires </h4>
<p>The <span class="removed_link" title="http://www.fedora.info/wiki/index.php/University_of_Hull">RepoMMan project</span> seeks to give researchers some 'extra services' almost without them being aware of it:  managing work in progress; access for themselves and small collaborative group; safety (backup) of work -- and be as easy to use a network drive on their desktop plus interface for repository-related activities.  The RepoMMan project is funded to bring a BPEL workflow to a FEDORA system to fulfill a part of this vision.</p>
<p>The development team has surveyed and interviewed researchers about how they did research to understand what repository processes and features might help them.  In the autumn, the development team plans to conduct the same survey and interview techniques to get the teaching/learning needs and administrator needs.  They are managing the evolving expectations for a general document management system from university's administration.</p>
<h4> Technology </h4>
<p>Use of ActiveBPEL is mandated by the JISC funding.  Initially, the inability to validate FEDORA's WSDL was a showstopper, but the WSDL was recently rewritten by the FEDORA core developer team and is being tested now.  The RepoMMan developers have gained a great deal of experience with the BPEL engine outside of FEDORA.  With a rewritten WSDL, the development is expected to move faster.</p>
<h2> Discussion </h2>
<h3> Overlap with FEDORA Preservation Services Working Group </h3>
<p>It was noted and discussed that the <span class="removed_link" title="http://www.fedora.info/wiki/index.php/Working_Group:_Preservation">Preservation Services Working Group</span> has begun defining the 'events' associated with objects in the repository and was looking for an 'event management engine' of some sort.  It is clear that there is some overlap in these working group activities and some coordination would be beneficial to both groups. The Preservation Services Working Group refers to this activity as "Event Management" which seems to be equivalent to our "Orchestration Management".</p>
<h3>Areas where the Workflow Working Group can make a meaningful contribution</h3>
<p>It was observed that collectively we're reaching for the final plateau of the desired service, but there are many layers from where we are now to there that needs to be built (e.g. message-oriented middleware).  In the course of the afternoon discussion, two work areas were identified.</p>
<p>First, defining and coding the building blocks of repository activities as discrete, WSDL-addressable web services.  This work needs to be done in conjunction with the FEDORA Preservation Services Working Group -- building on their existing work and aid in specifying these events as discrete web services.  These 'event' building blocks are likely to be generic to many workflow orchestration engines or other mechanisms to build workflow steps into an application.</p>
<p>Second, building a reference implementation of a workflow stack into the FEDORA-SF using open source components.  It is envisioned that this stack will consist of a "workflow engine" layer (BPEL-based, JBPM-based, other, or a combination of these); a "workflow management system" that provides the human interface to instantiate and track workflow scripts in flight (interfaces could be JSR-168 portlets, dedicated web servlet, a desktop Swing-based app, etc.); and a "workflow editor system" for creating new workflow scripts.</p>
<h2>Next steps</h2>
<ol>
<li> Create a narrative of these two work areas
</li>
<li> Participants review Preservation WG workflows
<ol>
<li> Peter will get with Ron Jantz to begin the dialog
</li>
<li> WG members will review the Preservation WG "events" as the basis of creating the orchestration "building block" activities
</li>
</ol>
</li>
</ol>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.fedora.info/wiki/index.php/Working_Group:_Workflow:Minutes-20060618.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.fedora.info/wiki/index.php/Talk:Working_Group:_Workflow:Minutes-20060618.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.fedora.info/wiki/index.php/User:Richard_green.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.fedora.info/wiki/index.php/User:PeterAtOhioLINK.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to /wiki/index.php/User:Matthias.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.fedora.info/wiki/index.php/User:Rwayland.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.fedora.info/wiki/index.php/ESciDoc_Project.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.fedora.info/wiki/index.php/University_of_Hull.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.fedora.info/wiki/index.php/Working_Group:_Preservation.</p>
