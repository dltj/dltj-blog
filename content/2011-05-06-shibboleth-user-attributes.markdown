---
layout: wordpress-import
status: published
published: true
title: '"The Challenges of User Consent" -- Handling Shibboleth User Attributes'
modified: 2011-05-06T20:51:38+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 2868
wordpress_url: http://dltj.org/?p=2868
date: '2011-05-06 16:51:38 -0400'
date_gmt: '2011-05-06 20:51:38 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Shibboleth
- privacy
comments:
- id: 159934
  author: Angelo So
  author_email: ''
  author_url: http://twitter.com/goodangso/status/68202553191563264
  date: '2011-05-11 06:35:30 -0400'
  date_gmt: '2011-05-11 10:35:30 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">&ldquo;The Challenges of User Consent&rdquo; &mdash;
    Handling Shibboleth User Attributes http://bit.ly/kW2ito</span></span>
- id: 159935
  author: John Mark Ockerbloom
  author_email: ''
  author_url: http://twitter.com/jmarkockerbloom/status/68038042656575488
  date: '2011-05-10 19:41:48 -0400'
  date_gmt: '2011-05-10 23:41:48 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Meanwhile, in Shibboleth-land, folks are discussing
    how to avoid releasing more user info than desired. http://j.mp/mDFluj</span></span>
- id: 159936
  author: doug moncur
  author_email: ''
  author_url: http://twitter.com/moncur_d/status/66762147430023168
  date: '2011-05-07 07:11:50 -0400'
  date_gmt: '2011-05-07 11:11:50 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">&ldquo;The Challenges of User Consent&rdquo; &mdash;
    Handling Shibboleth User Attributes http://bit.ly/lJPlb4</span></span>
- id: 159937
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/66613355783274496
  date: '2011-05-06 21:20:36 -0400'
  date_gmt: '2011-05-07 01:20:36 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: &ldquo;The Challenges of User Consent&rdquo;
    &mdash; Handling Shibboleth User Attributes http://bit.ly/kHTEgr</span></span>'
- id: 159938
  author: adtech.feed
  author_email: ''
  author_url: http://twitter.com/adtechfeed/status/66610675929190401
  date: '2011-05-06 21:09:57 -0400'
  date_gmt: '2011-05-07 01:09:57 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">"The Challenges of User Consent" -- Handling Shibboleth
    User Attributes: One of the great things about the Shibb... http://bit.ly/iDphPj</span></span>'
- id: 159939
  author: Library Feed
  author_email: ''
  author_url: http://twitter.com/libraryfeed/status/66608058058539008
  date: '2011-05-06 20:59:33 -0400'
  date_gmt: '2011-05-07 00:59:33 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">&ldquo;The Challenges of User Consent&rdquo; &mdash;
    Handling Shibboleth User Attributes http://bit.ly/isoOOM</span></span>
---
<p>One of the great things about the <a href="http://shibboleth.internet2.edu/" title="Shibboleth homepage">Shibboleth</a> inter-institution single sign-on software package is the ability for the Identity Provider to limit how much a Service Provider knows about a user's request for service.  (Not familiar with those capitalized terms?  Read on for definitions.)  But with this capability comes great flexibility, and with the flexibility can come lots of management overhead.  So I was intrigued to see the <a href="https://lists.internet2.edu/sympa/arc/shibboleth-announce/2011-04/msg00007.html" title="IAM Online May 11 - The Challenges of User Consent | shibboleth-announce mailing list">announcement</a> for an <a href="http://www.incommon.org/iamonline/" title="Identity and Access Management Online">online webinar</a> from the InCommon Shibboleth Federation with the title "The Challenges of User Consent" covering the issues of managing who gets access to what information about users.<br />
<!--more--><br />
From the webinar description:<br />
<blockquote>
<p>Are you starting to see more requests from SPs seeking user attributes? Would you like to explore methods that would simplify the attribute release process? &nbsp;You aren&rsquo;t alone. Campuses are seeking a scalable approach to managing attribute release that will minimize admin involvement and allow users to access sites like those that support collaborative work and want such attributes as EPPN, name, and email. </p>
<p>Automating the user consent procedure, combined with metadata-driven attribute release, provides an approach that greatly simplifies this process for all parties, and allows users to reach sites without delay. </p>
<p>Join us for a discussion and demonstration from Brown University and the University of Southern California. </p>
<p><strong>Host/Moderator: </strong>Tom Barton, University of Chicago and InCommon Technical Advisory Comittee</p>
<p><strong>Presenters:<br /> Steven Carmody</strong>, Brown University and InCommon TAC<br /><strong>Russ Beall</strong>, University of Southern California></p>
</blockquote>
<p>Lots more abbreviations and technical terms there, so here is a short primer:</p>
<dl>
<dt>Service Provider (SP)</dt>
<dd>A web server protected by Shibboleth that a user wants to access.</dd>
<dt>Identity Provider (IdP)</dt>
<dd>A web server that can authenticate a user (determine who the user is, typically with username/password) and store User Attributes.</dd>
<dt>User Attributes</dt>
<dd>Data about a user, including name, email address, affiliation status (student, employee, faculty, etc.), eduPersonPrincipalName, and TargetedIDs.</dd>
<dt>eduPersonPrincipalName (EPPN)</dt>
<dd>A string in the form of <i>user</i>@<i>domain</i> that uniquely identifies the user at an Identity Provider.  (<a href="http://www.incommonfederation.org/attributesummary.html#eduPersonPrincipal" title="Attribute Summary | InCommon">InCommon technical definition</a>)</dd>
<dt>TargetedID</dt>
<dd>An opaque string stored/generated by the Identity Provider that is unique to each user and Service Provider pair.  Passed as a User Attribute between the Identity Provider and the Service Provider, it can facilitate long-term user sessions at the Service Provider without revealing the identity of the user. </dd>
</dl>
<p>This is all stuff that as librarians we should be concerned about.  Arguably, a Service Provider should only have enough information to satisfy the demands of a license agreement, and in most cases those demands can be satisfied with an assertion that a user is of a proper affiliation with a library (e.g. "patron" or "student" or "employee" or simply "member").  It is baked into the Shibboleth trust model that the Service Provider will honor the User Attributes presented by the Identity Provider.</p>
<p>What makes the announcement of this webinar interesting is that Service Providers seem to be asking for the non-opaque eduPersonPrincipalName attribute.  I've long thought that TargetedID -- an opaque/random string shared between the Identity Provider and Service Provider -- is a much better answer to enabling privacy for functions like marked-item-lists, relevance ranking based on user search history, and other services that are unique to an individual.  Because TargetedID doesn't give away the person's identity yet is guaranteed by the IdP to be unique to one person at one SP, it is ideal for situations when the SP doesn't really need to know exactly <em>who</em> is making the request.  (Sure, if a user coming to an SP with a TargetedID then gives the SP his/her name or e-mail address, then that person is no longer anonymous but that was a choice the user made.)</p>
<p>So I'm planning on tuning in next Wednesday to get caugh up on what is happening with User Attributes in Shibboleth-land.  If you care about this kind of stuff, perhaps you can join me, too.</p>
