---
layout: wordpress-import
status: published
published: true
title: 'Interesting Shibboleth Use Case: Enforcing Geographic Restrictions'
modified: 2013-01-25T02:52:22+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 4080
wordpress_url: http://dltj.org/?p=4080
date: '2013-01-24 21:52:22 -0500'
date_gmt: '2013-01-25 02:52:22 -0500'
category: Raw Technology
categories:
- Raw Technology
tags:
- Shibboleth
- copyright
- HathiTrust
comments:
- id: 430935
  author: Tim McGeary
  author_email: timmcgeary@gmail.com
  author_url: ''
  date: '2013-01-25 10:13:01 -0500'
  date_gmt: '2013-01-25 15:13:01 -0500'
  content: This is very interesting, Peter.  It would benefit and strengthen access
    and security if we can get more adoption for Shibboleth and InCommon to resources
    like this.
- id: 430945
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2013-01-25 10:25:08 -0500'
  date_gmt: '2013-01-25 15:25:08 -0500'
  content: Agreed!  I've heard of many institutions that find it difficult to get
    administrators behind a Shibboleth project because there are not compelling use
    cases.  Why spend money and effort building a piece of infrastructure, the thinking
    goes, when it isn't used widely and brings no real benefits.  This HathiTrust
    integration is a real, demonstrable benefit.
---
<p><a href="http://www.hathitrust.org/updates_december2012" title="Update on December 2012 Activities | HathiTrust Digital Library">Last month's HathiTrust newsletter</a> had an interesting technical tidbit at the top about access to out-of-print and brittle or missing items:</p>
<blockquote><p>One of the lawful uses of in-copyright works HathiTrust has been pursuing is to provide access on an institutional basis to works that fall under United States Copyright Law Section 108 conditions: works in HathiTrust that are not available on the market at a fair price, and for which print copies owned by HathiTrust member institutions are damaged, deteriorating, lost or stolen. As a part of becoming a member, institutions are required to submit information about their print holdings for fee calculation purposes. We have also been requesting information about the holdings status and condition of works, to facilitate uses of works where permissible by law (specifications for HathiTrust holdings data are available at http://www.hathitrust.org/print_holdings).</p>
<p>As of December 2012, we are using the holdings status and condition information submitted by United States member institutions, in combination with information about the market availability of works stored in the HathiTrust rights database, to determine whether or not access to applicable in-copyright works in HathiTrust is allowed. The specific terms of access are as follows:</p>
<ul>
<li>Access is only available to users affiliated with HathiTrust member institutions in the United States, and only from U.S. soil.</li>
<li>In order to gain access, users from member institutions must be authenticated into HathiTrust via Shibboleth using their institutional login.</li>
<li>Print copies of the works in HathiTrust must be owned currently or have been owned previously by the institution&rsquo;s library system.</li>
<li>The number of users who can access a given digital copy at a time is determined by the number of print copies held (or previously held) in the library system. If a library system only has one print copy, only one user at a time will be able to access the digital copy.</li>
</ul>
<p>A general scenario for how out of print determinations are made and communicated to HathiTrust is available in the HathiTrust rights database documentation: http://www.hathitrust.org/rights_database#op.  Additional information on the service is available at http://www.hathitrust.org/out-of-print-brittle.</p></blockquote>
<p>It is the first three conditions (in the first two bullets) that I find interesting: that access is only available to affiliated users, that access is available only from "U.S. soil", and that users must authenticate using a HathiTrust member institution's Shibboleth identity provider.  The only way I can think for HathiTrust to enforce the first two conditions is to use <a href="http://shibboleth.net/" title="Shibboleth - Home">Shibboleth</a>.  Only through Shibboleth would HathiTrust have assurances that the user is a member of the community and is at a particular place.  ((Let's set aside for a moment the relatively trivial ways that IP address geolocation can be fooled:  VPN services, web proxies, etc.  If you want to know more, just <a href="https://www.google.com/search?q=how+to+bypass+geographical+restrictions">Google "how to bypass geographical restrictions"</a>.))  Libraries more commonly use rewriting proxy servers, like <a href="http://www.oclc.org/ezproxy/" title="http://www.oclc.org/ezproxy/">EZproxy</a>, to facilitate access to restricted or licensed material.  Rewriting proxy servers effectively hide the location of the user because to HathiTrust the user's location would appear to be where the proxy server is.</p>
<p>I dug a little deeper to see if I could find a definition of "affiliated" -- does it mean "only students, faculty and staff" or other looser forms of affiliation like "alumni" or "parent" or "guest"?  One of the great strengths of Shibboleth (generally) and the identity management federations like <a href="http://www.incommon.org/" title="InCommon: Security, Privacy and Trust for the Research and Education Community">InCommon</a> (specifically) is that they have fairly rigorous definitions of "member" and "affiliated" -- piggybacking on the eduPerson <a href="http://middleware.internet2.edu/eduperson/docs/internet2-mace-dir-eduperson-201203.html#eduPersonAffiliation" title="Internet2 Middleware - eduPerson Object Class Specification">eduPersonAffiliation attribute definition</a>.  I didn't find a firm linkage to those defined eduPerson terms, but I did find an interesting declaration in <a href="http://www.hathitrust.org/access_use#ic-access" title="Access and Use Policies | HathiTrust Digital Library">HathiTrust Digital Library Access and Use Policies</a>: "Users must be authenticated members of a HathiTrust institution or individuals using a computer on a HathiTrust institution's library premises."  That would both seem to simultaneously make the Shibboleth requirement redundant in cases where access came from an on-campus IP address and the question about the definition of affiliation moot -- by that statement, anyone using a library terminal would have access even if they weren't otherwise a member of the campus community.  Hmmm, I wonder how they are resolving that contradiction?</p>
<p>Digging a little deeper, I found the <a href="http://www.hathitrust.org/shibboleth" title="Shibboleth Login | HathiTrust Digital Library">HathiTrust Shibboleth technical details page</a> where they talk about the kinds of attributes required to use the service.  They do require 'eduPersonScopedAffiliation' ((<a href="http://middleware.internet2.edu/eduperson/docs/internet2-mace-dir-eduperson-201203.html#eduPersonScopedAffiliation" title="Internet2 Middleware - eduPerson Object Class Specification">eduPersonScopedAffiliation</a> is nearly the same as eduPersonAffiliation; it just tacks "@<i><institution></i>" on the end.)), so they can see the types of membership someone has with an institution.  It is also refreshing that the only other element they require is <a href="https://www.internet2.edu/media/medialibrary/2013/09/04/internet2-mace-dir-eduperson-201203.html#eduPersonTargetedID" title="Internet2 Middleware - eduPerson Object Class Specification">eduPersonTargetedID</a> -- the "persistent, non-reassigned, privacy-preserving identifier" known only to the institution and the service.  (The eduPerson definition goes on to say:  "This attribute is designed to preserve the principal's privacy and inhibit the ability of multiple unrelated services from correlating principal activity by comparing values. It is therefore REQUIRED to be opaque, having no particular relationship to the principal's other identifiers, such as a username or eduPersonPrincipalName. It SHOULD be considerably difficult for an observer to guess the value that would be returned to a given service provider.")  It is great to see HathiTrust using the privacy-enhancing aspects of Shibboleth like they were meant to be used.  Because they are using targetedID, a prosecuting party would need to subpoena records from both HathiTrust (to get the eduPersonTargetedID of the person they were interested in) and the member institution (to see who that eduPersonTargetedID was assigned to) to pin research activities to a specific individual.</p>
