---
layout: wordpress-import
status: published
published: true
title: 'Working With the Web Architecture'
modified: 2007-02-16T15:29:09+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 182
wordpress_url: http://dltj.org/2007/02/web-architecture/
date: '2007-02-16 10:29:09 -0500'
date_gmt: '2007-02-16 15:29:09 -0500'
category: Raw Technology
categories:
- Linking Technologies
- Raw Technology
tags:
- digital libraries
- Object Reuse and Exchange
- web architecture
- web standards
comments:
- id: 12392
  author: 'Disruptive Library Technology Jester :: Introducing the OAI Object Reuse
    and Exchange Initiative'
  author_email: ''
  author_url: http://dltj.org/2007/02/ore-introduction/
  date: '2007-02-16 10:31:38 -0500'
  date_gmt: '2007-02-16 15:31:38 -0500'
  content: "[...] In a subsequent postings, I&#8217;ll go into some detail about the
    inner workings of &#8220;The Web Architecture&#8221; and how it is both a help
    and a hindrance to the interaction of compound digital objects in our domain,
    and how it is a force too powerful to be ignored in either case. [...]"
- id: 12399
  author: 'Disruptive Library Technology Jester :: The Intersection of the Web Architecture
    with Scholarly Communication'
  author_email: ''
  author_url: http://dltj.org/2007/02/ore-model-services/
  date: '2007-02-16 15:06:22 -0500'
  date_gmt: '2007-02-16 20:06:22 -0500'
  content: "[...] Two previous posts on dltj.org have described the OAI Object Reuse
    and Exchange (ORE) project and the theory behind what has become known as the
    &#8216;Web Architecture&#8217;. These two areas meet up now in this post which
    describes the issues surrounding the raw Web Architecture as applied to a web
    of scholarly communication and a basic outline of what the ORE project hopes to
    accomplish. [...]"
- id: 12455
  author: pintiniblog
  author_email: ''
  author_url: ''
  date: '2007-02-18 12:37:33 -0500'
  date_gmt: '2007-02-18 17:37:33 -0500'
  content: "<!--%kramer-pre%--> de C. Lagoze et H. Van de Sompel sur le projet OAI-ORE.
    \   Rep&eacute;r&eacute;e sur Disruptive Library Technology Jester dans une s&eacute;rie
    de posts &agrave; propos de l'architecture web et de l'information acad&eacute;mique:
    ici, ici et ici. <!--%kramer-post%-->"
- id: 60234
  author: indira
  author_email: indira2259@yahoo.co.in
  author_url: ''
  date: '2010-03-17 13:44:00 -0400'
  date_gmt: '2010-03-17 17:44:00 -0400'
  content: "i am working on different web architectures for my research work\r\ni
    want to know more about this  topic, please suggest"
---
<p>As you may have noticed, the web has evolved a set of common principles that are a mix of ratified standards and ad hoc practices.  The notion of a Web Architecture was codified in a W3C technical report called "Architecture of the World Wide Web" <a href="http://www.w3.org/TR/2004/REC-webarch-20041215/" title="Architecture of the World Wide Web, Volume One">http://www.w3.org/TR/2004/REC-webarch-20041215/</a> or simply 'Web Architecture.'  Those projects and protocols that align with the 'Web Architecture' are more likely to be picked up and used than those that do not.  As a result, the <a href="http://www.openarchives.org/ore/" title="Open Archives Initiative Protocol - Object Exchange and Reuse">OAI Object Reuse and Exchange</a> (ORE) project seeks to provide an infrastructure for web-based information systems that exploit and enhance the Web Architecture, and therefore overlay cleanly on the existing web.</p>
<p>Given that we want to align closely with this 'Web Architecture' how far does the Web Architecture report go to define what is needed to make an ORE environment happen?  The answer lies in the definition of three terms and the interaction of these three concepts.</p>
<ul>
<li>Resource: "A network data object or service that can be identified by a URI.... Resources may be available in multiple representations (e.g. multiple languages, data formats, size, and resolutions) or vary in other ways." <footnote>"Hypertext Transfer Protocol -- HTTP/1.1" RFC 2616. Available from <a href="http://www.ietf.org/rfc/rfc2616" title="RFC 2616 &#039;Hypertext Transfer Protocol -- HTTP/1.1&#039;">http://www.ietf.org/rfc/rfc2616</a> Accessed Feb 15 2007.</footnote></li>
<li>Uniform Resource Identifier (URI):  "A compact string of characters for identifying an abstract or physical resource." <footnote>"Uniform Resource Identifiers (URI): Generic Syntax" RFC 2396. Available from <a href="/wp-content/uploads/2007/02/rfc2396.txt" title="RFC 2396 &#039;Uniform Resource Identifiers (URI): Generic Syntax&#039;">http://www.rfc-editor.org/rfc/rfc2396.txt</a> Accessed Feb 15 2007.</footnote></li>
<li>Representation: "An entity included with a response that is subject to content negotiation.... There may exist multiple representations associated with a particular response status." <footnote>"Hypertext Transfer Protocol -- HTTP/1.1" RFC 2616. Available from <a href="http://www.ietf.org/rfc/rfc2616" title="RFC 2616 &#039;Hypertext Transfer Protocol -- HTTP/1.1&#039;">http://www.ietf.org/rfc/rfc2616</a> Accessed Feb 15 2007.</footnote></li>
</ul>
<div style="float: right; margin: 0 0 1em 1.5em; padding 0 0 1em 1.5em; border: 2px solid grey;"><a id="p183" rel="attachment" class="imagelink" href="/article/web-architecture/illustration-shows-the-relationship-between-identifier-resource-and-representation/" title="Illustration shows the relationship between identifier, resource, and representation."><img id="image183" style="width: 200px;" src="/wp-content/uploads/2007/02/uri-res-rep.png" alt="Illustration shows the relationship between identifier, resource, and representation." /></a></div>
<p>This is perhaps best explained by this graphic from the "Architecture of the World Wide Web" document.  All three terms are included:  a URI identifies a resource which is in turn expressed as one representation.  The key part of how the web works, though, lies in the definition of "representation" &mdash; <em>that there may exist multiple representations</em> for a single URI.  Believe it or not, you already know this.  The representation of the resource identified by the URI '<tt>cnn.com</tt>' at noon today is different from the one that existed at noon yesterday.  You might say, "well so what...it is a dynamic website," and I would agree &mdash; what is important here is that the web architecture does not give you a way to identify with a URI that representation of the <tt>cnn.com</tt> resource at noon yesterday.  Put another way, in the words of the Web Architecture technical report, "Agents [web browsers and the like] may use a URI to access the referenced resource; this is called dereferencing the URI." <footnote>"Architecture of the World Wide Web, Volume One" paragraph #117.  Available from <a href="http://www.w3.org/TR/2004/REC-webarch-20041215/#p117" title="Architecture of the World Wide Web, Volume One">http://www.w3.org/TR/2004/REC-webarch-20041215/#p117</a> Accessed Feb 15 2007.</footnote>  The representation comes into being as a result of a service request by an agent for a resource via a URI.</p>
<p>The Web Architecture technical report lists four factors that determine which representation(s) are retrieved as a result of a service request: <footnote>"Architecture of the World Wide Web, Volume One" paragraph #122.  <a href="http://www.w3.org/TR/2004/REC-webarch-20041215/#p117" title="Architecture of the World Wide Web, Volume One">http://www.w3.org/TR/2004/REC-webarch-20041215/#p117</a> Accessed Feb 15 2007.</footnote></p>
<ol>
<li>Whether the URI owner makes available any representations at all;</li>
<li>Whether the agent making the request has access privileges for those representations...;</li>
<li>If the URI owner has provided more than one representation (in different formats such as HTML, PNG, or RDF; in different languages such as English and Spanish; or transformed dynamically according to the hardware or software capabilities of the recipient), the resulting representation may depend on negotiation between the user agent and server.</li>
<li>The time of the request; the world changes over time, so representations of resources are also likely to change over time.</li>
</ol>
<p>When a URI is accessed by a browser, one goes through a content negotiation to get a representation.  Representations may vary by device or time or IP address or authorization or any number of factors.  In a graph or type-based thinking, a resource is a first class object:  it is linkable &mdash; one can cite a resource. Representations, on the other hand, are second class objects:  identified only in the context of a resource. A representation is not linkable, there may be many representations per resource, and a representation only comes about as a result of an action.</p>
<h2>Observations</h2>
<p>This notion of the 'Web Architecture' is clearly dominant now, so what does the Web Architecture &mdash; resources, URIs, and representations &mdash; mean in the context of the OAI Object Reuse and Exchange work?  One would be well advised to use its existing capabilities where they are appropriate and build specialized extensions that sit on top in such a way as to not contradict its fundamental aspects.  This means cleanly layering new capabilities that meet the needs of our problem space.  In a subsequent posting, I'll outline the need for some <a href="/article/ore-model-services">ORE-specific extensions to the Web Architecture</a>.</p>
