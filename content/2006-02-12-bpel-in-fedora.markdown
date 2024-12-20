---
layout: wordpress-import
status: published
published: true
title: 'To BPEL or not to BPEL, quite a good question'
modified: 2006-02-13T00:41:18+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 21
wordpress_url: http://dltj.org/?p=21
date: '2006-02-12 19:41:18 -0500'
date_gmt: '2006-02-13 00:41:18 -0500'
category: Library Technology
categories:
- DRC
- Workflow
tags:
- DRC
- bpel
comments: []
---
<p>OhioLINK is actively looking at BPEL as an option for workflow orchestration for the DRC project.  I was asked recently about that choice, especially in light of a preliminary report from another team looking to use Fedora in a manner similar to the DRC.  The preliminary report has not been published (I'll update this posting when it is), and the organization involved is intentionally not mentioned here.  Their questions, though, do allow for an opportunity to explain some of my own thinking on the topic.</p>
<blockquote><p>
[We] had a look both at workflow engines with proprietary definition languages and at ones with BPEL support. [The] recommendation was not to use a BPEL engine because in their opinion, the current BPEL standard lacks at least one important feature: being able to assign a process to a user. They say that BPEL is targeted at workflow orchestration and not so much at modelling a workflow where human interactions are required. To my understanding, ingestion and especially quality assurance in most cases will include non-technical steps which require the assignment of the ongoing process to a person.
</p></blockquote>
<p>Your team has identified one known problem -- the lack of a standards-based way to script human interactions in a BPEL orchestration engine.  There are ways around it (as your team noted and as described in "<a href="http://www.zdnet.com/article/yes-bpel-has-a-human-side/" title="301 Moved Permanently">Yes, BPEL has a human side</a>") and also work being done to resolve it ("<span class="removed_link" title="http://www-128.ibm.com/developerworks/webservices/library/specification/ws-bpel4people/">WS-BPEL Extension for People</span>").</p>
<p>Speaking only for myself and OhioLINK for the moment, my desire to look seriously at BPEL, acknowledging that it is an immature and rapidly developing standard, is two-fold.  First, work on this standard is being done <a href="http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=wsbpel" title="301 Moved Permanently">under the auspices of OASIS</a> which has a good track record for bringing consensus to the industry and generating reasonable, open specifications for the industry to rally around.  From a digital preservation perspective, I believe that identifying and adhering to key standards aids in the overall ability to preserve the interactive nature of systems and their underlying digital objects.  This characteristic is what makes the Fedora repository, and the inherent ability to recreate the system from its underlying <a href="http://web.archive.org/web/20081005201706/http://www.fedora.info:80/download/2.0/userdocs/digitalobjects/introFOXML.html" title="301 Moved Permanently">METS-like objects</a>, very attractive.</p>
<p>Second, OhioLINK increasingly sees Fedora playing the role of a centralized content repository in a <a href="http://www.service-architecture.com/web-services/articles/service-oriented_architecture_soa_definition.html" title="Service-oriented architecture (SOA) definition">Service-Oriented Architecture</a> environment.  The repository and workflow orchestration engine will need to interoperate with an inventory control system (a component of today's Integrated Library System model), purchasing and accounts payable systems (for acquiring and claiming physical and digital content), and expertise systems (automated and human-mediated "reference" services).  And these activities will be conducted over a variety of interfaes:  HTML, SOAP, Interactive Voice Response, etc.  Our thinking along these lines is preliminary and purely theoretical, but the surface analysis we've done so far seems to indicate that we have a lot of other's work to leverage if we adopt these emerging industry philosophies, standards, and blueprints.</p>
<blockquote><p>
Additionally, they came up with the issue of complexity. Whereas they needed just one configuration file for jBPM to model their simplistic test case, it took them eleven configuration files (including WSDL) to set up their "hello world" example with ActiveBPEL. Adding a second web service to the workflow required changing several of these configuration files. Their impression was that going the BPEL way would let us end up in a maintenance nightmare (we expect to have many highly configurable workflows with lots of changes to them).
</p></blockquote>
<p>Unfortunately, this is where your team's coding experience trumps my theoretical understanding.  I've done some reading on the background and theory of BPEL, less on the actual implementation of a BPEL system, and no hands-on work (yet).  Eleven files strikes me as extreme (and a point of concern beacuse I expect to offer our users highly configurable workflow scenarios as well).</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www-128.ibm.com/developerworks/webservices/library/specification/ws-bpel4people/ on November 6th, 2012.</p>
