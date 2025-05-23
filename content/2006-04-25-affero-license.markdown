---
layout: wordpress-import
status: published
published: true
title: 'OhioLINK Selects the Affero License for DRC Development'
modified: 2006-04-25T19:45:54+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 45
wordpress_url: http://dltj.org/2006/04/affero-license/
date: '2006-04-25 15:45:54 -0400'
date_gmt: '2006-04-25 20:45:54 -0400'
category: Library Technology
categories:
- DRC
tags: []
comments: []
---
<p>Selecting an open source license was really much harder than I thought it would be.  The OhioLINK executive director and I talked for about 90 minutes over the course of yesterday afternoon to reach a conclusion.  The factors driving our decision where:</p>
<ul>
<li>A license that promoted the "open source" availability of our code</li>
<li>A license that sought to ensure balance between our desire as an "upstream" provider of the source code to add enhancements to the base source code with the desire of any potential commercial entity to "add value" by providing a level of support for the DRC application that we cannot provide</li>
</ul>
<p>As it turns out, the last point is key -- philosophically, we don't have a problem with a mythical commercial entity using the DRC application as a hosted solution to institutions outside Ohio and/or providing a level of support to institutions outside Ohio.  (Both are beyond our core mission of supporting Ohio higher education.)  What we are seeking to avoid is the situation where a commercial entity modifies the application as its "added value" and does not release those modifications to the world.</p>
<p>So the license we chose is the <strong><a href="http://www.affero.org/oagpl.html" title="http://www.affero.org/oagpl.html">Affero General Public License 1.0</a></strong> in anticipation of specific changes coming to the <a href="http://gplv3.fsf.org/draft" title="302 Found">GNU General Public License 3.0 now under draft</a>.  The particular modification to <a href="http://www.fsf.org/licensing/licenses/gpl.html" title="301 Moved Permanently">GNU GPL 2.0</a> that is appealing is section 2.d that Affero added to the GNU GPL (with GNU's permission):</p>
<blockquote><p>
2 d) If the Program as you received it is intended to interact with users through a computer network and if, in the version you received, any user interacting with the Program was given the opportunity to request transmission to that user of the Program's complete source code, you must not remove that facility from your modified version of the Program or work based on the Program, and must offer an equivalent opportunity for all users interacting with your Program through a computer network to request immediate transmission by HTTP of the complete source code of your modified version or other derivative work.
</p></blockquote>
<h2 id="Rationale">Rationale</h2>
<p>First off, I'm not a lawyer, so I'm trying to read and interpret what appears to be plain English without training in the skill of interpreting legal-like documents or researching the surrounding case law.  These are my personal opinions and although they mirror those of my employer I'm not in a position to offer official legal or policy opinions on behalf of my employer.</p>
<p>I believe strongly in the need to promote an environment of sharing code and concepts within the digital library community.  I also recognize that it is certainly the nature of the open source community to contribute modifications back to upstream projects, and that the GNU GPL was conceived to codify that practice into a legal license.  </p>
<p>Since the GPLv2 was developed in 1991, however, the software landscape has changed dramatically to one where the network is central.  In 1991, in order to "distribute" an application's capabilities to another system, you had to give the source code so that shell- or GUI-based application could be compiled and run on that other system.  That can be thought of as the economic <a href="http://en.wikipedia.org/wiki/Utility" title="Utility - Wikipedia, the free encyclopedia">utility</a>, or the "measure of the happiness or satisfaction gained consuming good and services."<footnote>From <a href="http://en.wikipedia.org/wiki/Utility" title="Utility - Wikipedia, the free encyclopedia">Wikipedia "utility"</a> entry.</footnote>  To get the satisfaction of using the application, you had to install it on your system.  Distribution of modifications to an application that increase its utility in this way is covered under the GNU GPL.</p>
<p>With the creation of network-based applications, though, to get the utility of an application's capabilities only requires that the recipient use a standard web browser to engage in HTTP transactions and receive back HTML or other forms of benefits/output from the application -- the source code never has to change hands.  In other words, you can receive the utility of a derivation of the original application without forcing the distribution of the source code for that derived work.</p>
<p>In drafting GNU GPLv3, there are some in the open source community that believe public use of a derivative of an application across the internet is a form of "distribution" that compels the provider to offer the source code.  Affero, working in advance of the publication of GNU GPLv3 created a new open source license that compels the developer of a derivative form of the application under the license to not disable a function written in the application that returns the source code to the requester on demand.  By allowing the source code of the current application to be delivered user in the same manner the application is used over the internet (via a web browser) the spirit of GNU GPL in a networked environment is upheld.  The distribution of an application's utility, along with the distribution of its source code, are kept in sync.</p>
<p>OhioLINK has put up <span class="removed_link" title="http://drc-dev.ohiolink.edu/wiki/OpenSourceLicense#QuestionsandAnswers">questions and answers</span> that at this point we anticipate receiving.  (We'll update the list with other questions and answers as they come in.)  You can also look at the <a href="http://www.affero.org/oagf.html" title="http://www.affero.org/oagf.html">Affero FAQ</a> to read more into the reasoning behind what they did.</p>
<p>Comments welcome.
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://drc-dev.ohiolink.edu/wiki/OpenSourceLicense#QuestionsandAnswers.</p>
