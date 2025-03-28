---
layout: wordpress-import
status: published
published: true
title: 'On questions regarding ISO/DIS 18626, Information and documentation &mdash; Interlibrary Loan Transactions'
modified: 2013-11-09T02:41:43+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 4234
wordpress_url: http://dltj.org/?p=4234
date: '2013-11-08 21:41:43 -0500'
date_gmt: '2013-11-09 02:41:43 -0500'
category: Raw Technology
categories:
- Raw Technology
tags:
- standards
- ISO
- IETF
- Interlibrary loan
- http
- RFC2616
comments:
- id: 651839
  author: Ryan Collins
  author_email: blogs2009@ryancollins.org
  author_url: http://ryancollins.org
  date: '2013-11-09 09:24:38 -0500'
  date_gmt: '2013-11-09 14:24:38 -0500'
  content: "I was filling out a two sided form at the dentist office. On the back
    they asked for some of the same information that I already entered on the front.
    I just wrote \"See front\". Don't make me enter information again. (Another example,
    when they ask for your birthdate and your age...)\r\n\r\nAnytime you can eliminate
    duplicate information, it is good. You are spot on, don't duplicate work that's
    already been done."
- id: 651845
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2013-11-09 11:41:21 -0500'
  date_gmt: '2013-11-09 16:41:21 -0500'
  content: Thanks, Ryan -- that form is a great example.  What if the information
    was recorded one way on the front and a different way on the back?  Which one
    would be considered "correct"?  I think that is the type of separation of layers-of-concern
    that is needed here.
---
<p>There is a ballot under consideration within the <abbr title="International Standards Organization">ISO</abbr> <a href="http://www.iso.org/iso/home/standards_development/list_of_iso_technical_committees/iso_technical_committee.htm?commid=48798" title="ISO - Technical committees - ISO/TC 46/SC 4 - Technical interoperability"><abbr title="Technical Committee">TC</abbr> 46/<abbr title="Subcommittee">SC</abbr> 4</a> on <a href="http://biblstandard.dk/ill/" title="http://biblstandard.dk/ill/">InterLibraryLoan Transactions</a>.  The ballot description is:<br />
<blockquote>This International Standard specifies the transactions between libraries or libraries and other agencies to handle requests for library items and following exchange of messages. This standard is intended to at first supplement and eventually succeed the existing international ILL standards ISO 10160, ISO 10161-1 and ISO 10161-2, which are based on the outdated open systems interconnection model. The introduction of the draft standard provides some background on the relationship of the new standard to the previous one.</p></blockquote>
<p>The working group has reached the Draft International Standard ('DIS') stage, and my employer -- as a member of NISO -- is able to cast an advisory vote on whether to approve the DIS for publication.  Last week, the ALA representative to NISO <a href="http://lists.ala.org/sympa/arc/digipres/2013-11/msg00000.html" title="digipres - Digital Preservation">posted a question to several mailing lists</a> seeking advice on some controversy in a few sections of the document.  My comments to the ballot are likely the source of that controversy, so I'd like to invite feedback here or through other forums before the NISO advisory ballot closes on November 19th.  Below is a slightly edited version of my official ballot comments.  Some feedback on whether I'm simply <a href="http://www.merriam-webster.com/dictionary/nit-picking" title="Nit-picking - Definition and More from the Free Merriam-Webster Dictionary">picking at nits</a> would be helpful.</p>
<p>My main concern is duplicative and conflicting information between the draft standard (officially called "ISO/DIS 18626") and the <abbr title="Internet Engineering Task Force">IETF</abbr>'s HTTP 1.1 standard (officially called "RFC 2616").  Unfortunately, as with much ISO work, the document itself is protected by copyright and the draft is only available to voting members for the purposes of evaluating and commenting on the standard.   I think it is okay to post the parts of concern here.</p>
<blockquote><h2>5.2.2 Applications Acting as Responders</h2>
<p>Applications acting as responders must support all of the following transport protocols:</p>
<ul>
<li>HTTP</li>
<li>HTTPS</li>
</ul>
<p>The selection of the transport protocol by the initiator of a message will govern the transport protocol used by the responder. The responder must respond using the same connection, and therefore, the same transport protocol that was used by the initiator.</p>
<p>All ISO 18626 messages sent via HTTP or HTTPS must use the POST method as specified in the version 1.1. of the Hypertext Transfer (HTTP) protocol (RFC 2616), thus:</p>
<p><code>POST http://biblstandard.dk/ill HTTP/1.1 CRLF</code></p>
<p>All ISO 18626 response messages sent via HTTP or HTTPS must use the normal HTTP/HTTPS protocol response mechanism used to respond to POSTs. For example:</p>
<p><code>HTTP/1.1 200 OK CRLF<br />
<response header fields> CRLF CRLF<br />
<response message></code></p>
<h2>5.2.3 HTTP/HTTPS Message Headers</h2>
<p>For both optional ISO 18626 initiation and response messages, the HTTP/HTTPS Content-Type and Content- Length headers must be included and coded as follows:</p>
<p><code>Content-Type: application/xml; charset="utf-8" CRLF<br />
Content-Length: nnnn CRLF</code></p>
<p>Where nnnn is the length of the data being sent (not including the length of the message headers).</p>
<p>The entity transferred via the HTTP message must contain the entire text of the message following a carriage return/line feed (CRLF) with no preceding text, thus:</p>
<p><code>CRLF<br />
<initiation message> | <response message></code></p>
<p>Where <initiation message> or <response message> contains the XML formatted data (see section 5.1) for the message being sent.</p></blockquote>
<p>Parts of section 5.2.2 and all of section 5.2.3 are duplicative of RFC 2616.  To eliminate confusion and the possibilities of conflict, I think these portions should be removed or declared non-normative in the document.  If ISO/DIS 18626 places constraints on RFC 2616, then those need to be explicitly called out in the ISO/DIS 18626 document.  There are multiple implementations of RFC 2616 for various programming languages at, admittedly, various levels of conformance to that standard.  If particular implementation details are required by ISO/DIS 18626 -- call it an implementation profile of RFC 2616, if you will -- those must be spelled out in the standard.  For instance, section ISO/DIS 18626 section 5.2.3 says (emphasis added):</p>
<blockquote><p>For both optional ISO 18626 initiation and response messages, the HTTP/HTTPS Content-Type and Content-Length headers <em>*MUST*</em> be included...</p></blockquote>
<p>whereas <a href="https://tools.ietf.org/html/rfc2616#section-14.13">RFC 2616 section 14.13</a> says (emphasis added):</p>
<blockquote><p>Applications <em>*SHOULD*</em> use this field to indicate the transfer-length of the message-body, unless this is prohibited by the rules in section 4.4.</p></blockquote>
<p>and <a href="https://tools.ietf.org/html/rfc2616#section-7.2.1">RFC 2616 section 7.2.1</a> says (emphasis added):</p>
<blockquote><p>Any HTTP/1.1 message containing an entity-body <em>*SHOULD*</em> include a Content-Type header field defining the media type of that body.</p></blockquote>
<p>It is conceivable that a developer implementing ISO/DIS 18626 may use a code library that doesn't send or honor received Content-Type and Content-Length headers.  That doesn't necessarily cause a violation of the HTTP standard.  In reality, I believe the implementation details of an RFC2616-compliant code library are irrelevant to ISO/DIS 18626; what that code library hands to the higher level application is the Request-URI, the entity body, and possibly the Content-Type; HTTP protocol details such as the Content-Length of the entity body don't appear to be relevant to ISO/DIS 18626.  (The use of Content-Length, at least, is not mentioned further in the ISO/DIS 18626 draft.)</p>
<p>In reviewing RFC 2616 in the course of writing this response, there is an additional area of concern with the example used in ISO/DIS 18626 section 5.2.2:</p>
<p><code>POST http://biblstandard.dk/ill HTTP/1.1 CRLF</code></p>
<p>This <a href="https://tools.ietf.org/html/rfc2616#section-5.1">HTTP Request-Line</a> uses the <a href="https://tools.ietf.org/html/rfc2616#section-5.1.2">absoluteURI form of the Request-URI</a>.  RFC 2616 section 5.1.2 goes on to say:</p>
<blockquote><p>The absoluteURI form is REQUIRED when the request is being made to a proxy.</p></blockquote>
<p>and:</p>
<blockquote><p>To allow for transition to absoluteURIs in all requests in future versions of HTTP, all HTTP/1.1 servers MUST accept the absoluteURI form in requests, even though HTTP/1.1 clients will only generate them in requests to proxies.</p></blockquote>
<p>and:</p>
<blockquote><p>The most common form of Request-URI is that used to identify a resource on an origin server or gateway. In this case the absolute path of the URI MUST be transmitted (see section 3.2.1, abs_path) as the Request-URI, and the network location of the URI (authority) MUST be transmitted in a Host header field.</p></blockquote>
<p>It is unclear whether ISO/DIS 18626 is insisting on the use of absoluteURIs in the HTTP Request-Line (in which case I strongly encourage the draft to explicitly say "The HTTP/HTTPS Request-Line *MUST* include the absolute URI of the responder.") or if it is over-specifying the example.  Again, I believe these implementation details of RFC 2616 are irrelevant with respect to ISO/DIS 18626.</p>
<p>Your thoughts?</p>
