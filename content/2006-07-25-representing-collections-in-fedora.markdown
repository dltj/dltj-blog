---
layout: wordpress-import
status: published
published: true
title: 'Representing Collections In FEDORA'
modified: 2006-07-25T18:28:44+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 91
wordpress_url: http://dltj.org/2006/07/representing-collections-in-fedora/
date: '2006-07-25 14:28:44 -0400'
date_gmt: '2006-07-25 19:28:44 -0400'
category: Library Technology
categories:
- DRC
- Fedora
- Raw Technology
tags:
- standards
- DRC
- metadata
- library service-oriented architecture
- RDF
- digital libraries
- open source
- Fedora Repository
comments: []
---
<p>One of the DRC developers had a question recently that sparked a discussion about what to do with collections of objects.  In order to answer the question of how to represent the notion of a collection within the repository, we're going to have to get pretty heavy into RDF:  the Resource Description Framework.  RDF is a language created by the Worldwide Web Consortium "for representing information about resources in the World Wide Web."  If you already know about RDF -- or just want to see what a proposed solution is -- you can skip down to the "<a href="#nid91L">RDF for Collections in FEDORA</a>" heading.</p>
<p>At the preface, I have to say that I'm increasingly uncomfortable with the word "collection" because it has become so overloaded in library usage, and like Carl Lagoze prefer the term "aggregation" to describe in a general sense what we think a collection is and what it could become.  I probably bounce back and forth between the terms here, but am aiming to use "aggregation" and "aggregation object" more often.</p>
<p>I'm going to be pulling a lot of examples and language from the "<a href="http://www.w3.org/TR/rdf-primer/" title="RDF Primer">RDF Primer</a>", which I would recommend reading at some point.  It is a very long, dense document, but if you can get through it you'll have a very good understanding of what RDF is and what is does for us.</p>
<p>The Primer describes RDF this way:  "It is particularly intended for representing metadata about Web resources, such as the title, author, and modification date of a Web page, copyright and licensing information about a Web document, or the availability schedule for some shared resource....  RDF is based on the idea that the things being described have properties which have values, and that resources can be described by making statements ... that specify those properties and values."</p>
<p>There are three parts to an RDF statement about an object.  "[T]he part that identifies the thing the statement is about (the Web page in this example) is called the <em>subject</em>. The part that identifies the property or characteristic of the subject that the statement specifies (creator, creation-date, or language in these examples) is called the <em>predicate</em>, and the part that identifies the value of that property is called the <em>object</em>."</p>
<p>These component make up what is called an "RDF triple."  When written in tabular form an RDF triple is conventionally written in the order subject, predicate, object.  To represent RDF statements in a machine-processable way, RDF uses the Extensible Markup Language [XML]. RDF defines a specific XML markup language, referred to as RDF/XML, for use in representing RDF information, and for exchanging it between machines.</p>
<p>For instance, imagine trying to state the (nominally, Dublin Core) descriptive metadata about a web page called http://www.example.org/index.html.  In natural language, the descriptive elements could be:</p>
<div style="padding: 10px; margin: 0.67em auto; border: thin solid silver; font-size: 85%; color: black; background: #FFC">
 <strong>http://www.example.org/index.html</strong> has a <strong>creator</strong> whose value is <strong>John Smith</strong><br />
 <strong>http://www.example.org/index.html</strong> has a <strong>creation-date</strong> whose value is <strong>Aug 16, 1999</strong><br />
 <strong>http://www.example.org/index.html</strong> has a <strong>language</strong> whose value is <strong>English</strong>
</div>
<p>In tabular form, this could look like:</p>
<div style="padding: 10px; margin: 0.67em auto; border: thin solid silver; font-size: 85%; color: black; background: #FFC">
<table>
<tr>
<th>Subject</th>
<th>Predicate</th>
<th>Object</th>
</tr>
<tr>
<td>http://www.example.org/index.html</td>
<td>creator</td>
<td>John Smith</td>
</tr>
<tr>
<td>http://www.example.org/index.html</td>
<td>creation-date</td>
<td>Aug 16, 1999</td>
</tr>
<tr>
<td>http://www.example.org/index.html</td>
<td>language</td>
<td>English</td>
</tr>
    </table>
</div>

<p>In XML, this could look like:</p>
<div style="padding: 10px; margin: 0.67em auto; border: thin solid silver; font-size: 85%; color: black; background: #FFC">
```xml
 <?xml version="1.0"?>
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:dc="http://purl.org/dc/elements/1.1/">
   <rdf:Description rdf:about="http://ex.org/i.html">
     <dc:creator>John Smith</dc:creator>
     <dc:creation-date>Aug 16, 1999</dc:creation-date>
     <dc:language>English</dc:language>
   </rdf:Description>
 </rdf:RDF>
```
</div>
<p>Keep in mind, though, that we expressed the predicate here as Dublin Core; the predicate can be anything -- even something you make up!</p>
<h2>RDF for Collections in FEDORA</h2>
<p>RDF is used throughout FEDORA -- in fact, the Dublin Core properties can (and in our FEDORA configuration, are) expressed as RDF triples in an internal database and can be searched as such.  But the RDF triples can be used to express more than just attributes about an object -- it can be used to express /relationships/ between objects.  There is a whole section of the FEDORA docs called "<a href="http://web.archive.org/web/20090104100657/http://www.fedora.info:80/download/2.1.1/userdocs/digitalobjects/introRelsExt.html" title="Fedora Digital Object Relationships">Fedora Digital Object Relationships</a>" that goes into more detail.  Quotations and examples in this section are drawn from that document.</p>
<p>"Fedora digital objects can be related to other Fedora objects in many ways.  For example there may be a Fedora object that represents a collection and other objects that are members of that collection.  Also, it may be the case that one object is considered a part of another object, a derivation of another object, a description of another object, or even equivalent to another object."</p>
<p>FEDORA comes with a <a href="http://www.fedora.info/definitions/1/0/fedora-relsext-ontology.rdfs" title="http://www.fedora.info/definitions/1/0/fedora-relsext-ontology.rdfs">list of common relationships between objects</a>, and other community or user-defined relationships may also be asserted.  These relationships can be expressed in RDF notation:</p>
<div style="padding: 10px; margin: 0.67em auto; border: thin solid silver; font-size: 85%; color: black; background: #FFC">
<table>
<tr>
<th>Subject</th>
<th>Predicate</th>
<th>Object</th>
</tr>
<tr>
<td><subjectFedoraObject></td>
<td><relationshipProperty></td>
<td><targetFedoraObject></td>
</tr>
<tr>
<td>MyCatVideo</td>
<td>is a member of collection</td>
<td>GreatCatVideos</td>
</tr>
<tr>
<td>drc:101</td>
<td>isMemberOf</td>
<td>drc:100</td>
</tr>
<tr>
<td>drc:101</td>
<td>isFromInstitution</td>
<td>mu3ug</td>
</tr>
    </table>
</div>

```xml
 <?xml version="1.0"?>
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
   xmlns:fedora="info:fedora/fedora-system:def/relations-external#"
   xmlns:drcns="http://drc.ohiolink.edu/ontologies/relationships#">

   <rdf:Description rdf:about="info:fedora/drc:101">
      <fedora:isMemberOf rdf:resource="info:fedora/drc:100" />
      <drcns:isFromInstitution>mu3ug</drcns:isFromInstitution>
   </rdf:Description>
 </rdf:RDF>
```
<p>"drc:100" is an aggregation object (otherwise known as a "collection object", but I've learned from others in the FEDORA community that "collection" is too loaded of a word) of which "drc:101" is a member.  To put it in terms that we may be familiar with:</p>
<ul>
<li>drc:100 is the aggregation object for the "Charles E. Frohman Collection"</li>
<li>drc:101 is a digital image of a photograph with the title "Work Crew" that is part of the Charles E. Frohman collection</li>
<li>drc:101 is a digital image contributed by member institution "mu3ug"</li>
</ul>
<h2>Conclusions</h2>
<p>So the issue becomes, I believe, to examine the <a href="http://www.fedora.info/definitions/1/0/fedora-relsext-ontology.rdfs" title="http://www.fedora.info/definitions/1/0/fedora-relsext-ontology.rdfs">pre-loaded set of relationships</a> to match those against the existing relationships in the DMC and then do define any kind of unique relationships (such as "isFromInstitution") that we would want to express about our objects.</p>
