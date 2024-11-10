---
layout: wordpress-import
status: published
published: true
title: 'The Intersection of the Web Architecture with Scholarly Communication'
modified: 2007-02-16T20:01:32+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 184
wordpress_url: http://dltj.org/2007/02/ore-model-services/
date: '2007-02-16 15:01:32 -0500'
date_gmt: '2007-02-16 20:01:32 -0500'
category: Raw Technology
categories:
- Linking Technologies
- Raw Technology
tags:
- library 2.0
- digital libraries
- Object Reuse and Exchange
- web architecture
comments:
- id: 12398
  author: 'Disruptive Library Technology Jester :: Introducing the OAI Object Reuse
    and Exchange Initiative'
  author_email: ''
  author_url: http://dltj.org/2007/02/ore-introduction/
  date: '2007-02-16 15:05:32 -0500'
  date_gmt: '2007-02-16 20:05:32 -0500'
  content: "[...] In a subsequent postings, I&#8217;ll go into some detail about the
    inner workings of &#8220;The Web Architecture&#8221; and how it is both a help
    and a hindrance to the interaction of compound digital objects in our domain,
    and how it is a force too powerful to be ignored in either case. [...]"
- id: 12457
  author: pintiniblog
  author_email: ''
  author_url: ''
  date: '2007-02-18 12:37:33 -0500'
  date_gmt: '2007-02-18 17:37:33 -0500'
  content: "<!--%kramer-pre%--> de C. Lagoze et H. Van de Sompel sur le projet OAI-ORE.
    \   Rep&eacute;r&eacute;e sur Disruptive Library Technology Jester dans une s&eacute;rie
    de posts &agrave; propos de l'architecture web et de l'information acad&eacute;mique:
    ici, ici et ici. <!--%kramer-post%-->"
---
<p>Two previous posts on <i>dltj.org</i> have described the <a href="/article/ore-introduction/">OAI Object Reuse and Exchange (ORE) project</a> and the <a href="/article/web-architecture/">theory behind what has become known as the 'Web Architecture'</a>.  These two areas meet up now in this post which describes the issues surrounding the raw Web Architecture as applied to a web of scholarly communication and a basic outline of what the ORE project hopes to accomplish.</p>
<h2>Problems With the Web Architecture</h2>
<p>The concepts behind the Web Architecture are clearly successful.  I believe it is safe to assert that the genius behind the creation of Tim Berners-Lee and his colleagues is the simplicity with which the vast web of world wide connections has sprung into existence with relatively little coordination.  That said, some of the fundamental concepts behind the Web Architecture do not fit well with the web of interactions known as "scholarly communication."</p>
<p>The first issue is aggregation.  The Web Architecture does not provide a way to describe a finite set of Resources and relationships as a citable complex digital object resource structure.  As scholarly communication becomes more than just papers &mdash; it can also now include data sets, supplementary graphics, primary source material as well as references to previously publish objects &mdash; this concept of aggregation becomes important.</p>
<p>Second, the relationships between Resources are usually untyped and link type ontologies are not well defined.  (Capital-R "Resources" carries the meaning of this term as defined by the standards related to the Web Architecture; see the previous posting for a definition and examples.) Is this link within the text of a document a citation?  A data set?  An explanatory graphic?  In general, it is not good practice to try to guess the relationship based on the contents of the URI itself.  In fact, the Web Architecture technical report suggests "agents making use of URIs SHOULD NOT attempt to infer properties of the referenced resource."  <footnote>"Architecture of the World Wide Web, Volume One" paragraph #98.  Available from <a href="http://www.w3.org/TR/2004/REC-webarch-20041215/#p98" title="Architecture of the World Wide Web, Volume One">http://www.w3.org/TR/2004/REC-webarch-20041215/#p98</a> Accessed Feb 16 2007.</footnote>  In the absence of additional standards (such as OAI-ORE) layered on top of the core Web Architecture, this notion of "URI Opacity" encourages independence between an identifier in one document and the Representation of another object.  One thing the ORE work seeks to accomplish is to build a framework for the semantics of links between objects in a scholarly communication environment.</p>
<h2>The Problems From a Scholarly Communication Perspective</h2>
<div style="float: right; margin: 0 0 1em 1.5em; padding 0 0 1em 1.5em; border: 2px solid grey;"><a id="p185" rel="attachment" class="imagelink" href="/article/ore-model-services/compound-digital-object-modeled-using-the-web-architecture/" title="Compound digital object modeled using the Web Architecture"><img id="image185" style="width: 200px;" src="/assets/images/2007/02/pre-ore-model.gif" alt="Compound digital object modeled using the Web Architecture" /></a></div>
<p>Take, for example, a paper in an example repository as described by this graphic.  The article, identified by the number "012345" has six Resources with five Representations:  an HTML splash page generated by the repository software (Resource #1), the article in PDF format (Resource #2), the article in Postscript format (Resource #4), metadata in Dublin Core XML (Resource #5), metadata in BibTex format (Resource #6), and the article in a format decided by agent/server content negotiation (#3). <footnote>The Web Architecture allows for the Representation of a Resource to be decided through content negotiation between the agent/browser and the server.</footnote>.  Keep in mind that views of digital object must be bound to Resources in order to be reference-able (e.g. they must have URIs).</p>
<p>Although it may be possible to infer that all six Resources are related by comparing the leading fragment of the URIs, the Web Architecture principle of URI opacity dictates that we shouldn't make those assumptions.  Furthermore, even if we could determine that they are related based on examining the URIs, we do not have a consistent vocabulary to <em>define</em> that relationship.  Is "...meta/bibtex" the citation data for <em>this</em> article or is it the <em>list</em> of citations used in the article?</p>
<h2>Modeling Complex Objects</h2>
<div style="float: right; margin: 0 0 1em 1.5em; padding 0 0 1em 1.5em; border: 2px solid grey;"><a id="p186" rel="attachment" class="imagelink" href="/article/ore-model-services/compound-digital-object-modeled-using-ore-concepts/" title="Compound digital object modeled using ORE concepts"><img id="image186" style="width: 200px;" src="/assets/images/2007/02/ore-model.gif" alt="Compound digital object modeled using ORE concepts" /></a></div>
<p>Because the Web Architecture does not allow for the definition of a boundary for a compound digital object, the ORE project proposes the definition of a Resource &mdash; called the ORE Model, for lack of a better name at the moment &mdash; that formally expresses a bounded aggregation of resources and relationships that corresponds to a compound digital object.  Put another way, an instantiation of the ORE Model is a map of other resources that expresses the boundaries of the compound digital object.  A URI identifies the compound digital object &mdash; the ORE Resource &mdash; and a service request on that URI returns a Representation that is some serialization of the ORE Model.</p>
<p>The preliminary version of the model describes two types of relationships:  intra-aggregation relationships (inside the boundaries of the compound digital object) and inter-aggregation relationships (to Resources outside the boundary of this compound digital object).  The intra-aggregation relationships come in two forms:  hasPart (where one Resource contains other Resources, such as books contain chapters or journal issues contain articles) and hasView (where the target Resource is a semantically equivalent presentation format, such as Word and PDF versions of an article).  The inter-aggregation relationship has only one verb, "hasRelationshipTo," which simply means the target of the relationship is considered outside the boundaries of the complex digital object.  From a base verb of "hasRelationshipTo" other communities can apply specialized relationships.</p>
<p>The result describes a connected sub-graph with a finite set of resources and relationships among those resources to form a compound digital object plus relationships to resources that are external to the aggregation.  With that in place, we can consider services that can be applied to portions of the graph.</p>
<h2>ORE Services</h2>
<p>One half of the work of the ORE project is to define a model for compound digital objects in a Web Architecture environment.  The other half of the work is to define the meaning of services that exchange instances of the model to form the basis of a Web Architecture-aware scholarly communication environment.</p>
<p>Conceived based on the experiences with the OAI Protocol for Metadata Harvesting (PMH), there are three archetypes of services.</p>
<ul>
<li>Harvest: a request for a batch of instances that correspond to the ORE model from a set of ORE Resources.</li>
<li>Obtain: A request for an instance that corresponds to the ORE Model from a specific ORE Resource.</li>
<li>Register: A request to add new nodes or relationships to an ORE aggregation.</li>
</ul>
<p>Service requests against the ORE Resource URI are the access points for these activities.</p>
<h2>For more information...</h2>
<p>This is a basic introduction to the work of the technical committee so far.  For a more in-depth view into the outcomes of the first face-to-face meeting, including expanded definitions and examples of what was outlined here, see the <a href="http://www.openarchives.org/ore/documents/OAI-ORE-TC-Meeting-200701.pdf">Report of the January 2007 ORE-TC Meeting</a>.  In addition, there is a <a href="http://www.educause.edu/blogs/mpasiewicz/interview-herbert-van-de-sompel" title="An Interview with Herbert van de Sompel | EDUCAUSE CONNECT">interview with Herbert van de Sompel</a> recorded at the CNI 2006 Fall Task Force to go along with <a href="http://www.cni.org/pbs/cni2006fallpb/the-oai-object-re-use-exchange-ore-initiative/" title="Project Briefing-Fall 2006 Task Force Meeting">a project briefing</a> presented at that meeting.  (Keep in mind that these were recorded and presented before the first technical committee meeting, so some of the concepts of the implementation have changed.)  Pete Johnson, a member of the ORE technical committee, posted his thoughts on the topic on his blog:  <a href="http://efoundations.typepad.com/efoundations/2007/01/ore.html" title="eFoundations: Prospecting for ORE">Prospecting for ORE</a>, <a href="http://efoundations.typepad.com/efoundations/2007/01/more_ore.html" title="eFoundations: More ORE">More ORE</a>, and <a href="http://efoundations.typepad.com/efoundations/2007/02/more_rumination.html" title="eFoundations: More ruminations on compoundness and complexity (and metadata)">More ruminations on compoundness and complexity (and metadata)</a>.  The <a href="http://www.openarchives.org/ore/documents/OR07.pdf" title="http://www.openarchives.org/ore/documents/OR07.pdf">presentation slides</a> from Carl Lagoze's talk at Open Repositories 2007 are also available, of which <a href="http://cwilper.blogspot.com/2007/01/resources-representations-repositories.html" title="Your Metadata Sucks: Resources, Representations, Repositories, and RDF">Chris Wilper</a> and <a href="http://wwmm.ch.cam.ac.uk/blogs/downing/?p=69" title="Unilever Centre for Molecular Informatics, Cambridge - Jim Downing  &amp;raquo; Blog Archive   &amp;raquo; Open Repositories 2007 Plenary Session 5: Interoperability">Jim Downing</a> posed summaries and reactions.  Also keep an eye on the <span class="removed_link" title="http://technorati.com/tag/OAI-ORE">OAI-ORE tag on Technorati</span> for more updates and reactions.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://technorati.com/tag/OAI-ORE on January 19th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://www.cni.org/tfms/2006b.fall/abstracts/PB-oai-sompel.html to http://www.cni.org/pbs/cni2006fallpb/the-oai-object-re-use-exchange-ore-initiative/ on August 22nd, 2013.</p>
