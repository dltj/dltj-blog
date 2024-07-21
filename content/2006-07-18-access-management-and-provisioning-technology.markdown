---
layout: wordpress-import
status: published
published: true
title: 'Access Management and Provisioning Technology'
modified: 2006-07-18T18:21:41+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 90
wordpress_url: http://dltj.org/2006/07/access-management-and-provisioning-technology/
date: '2006-07-18 14:21:41 -0400'
date_gmt: '2006-07-18 19:21:41 -0400'
category: Library Technology
categories:
- Fedora
- Library SOA
- Raw Technology
tags:
- library service-oriented architecture
- Shibboleth
- internet2
- spring framework
- grouper
- xacml
- acegi
- signet
- provisioning
- nmi-edit
- Fedora Repository
comments:
- id: 291609
  author: Peter Murray
  author_email: ''
  author_url: http://twitter.com/datag/status/238418093137862657
  date: '2012-08-22 23:31:17 -0400'
  date_gmt: '2012-08-23 03:31:17 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Access Management and Provisioning Technology
    http://t.co/WkTGGMff</span></span>
- id: 291949
  author: donkasprzak
  author_email: ''
  author_url: http://twitter.com/donkasprzak/status/239174874847920129
  date: '2012-08-25 01:38:28 -0400'
  date_gmt: '2012-08-25 05:38:28 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Access Management and Provisioning Technology
    http://t.co/MzCXoBIP</span></span>
---
<p>Building on the shoulders of others -- isn't that how that quote goes?  There has been a stack of printouts on my desk for a while now for various access management and service provisioning technologies.  Rather than keep the paper, I'm putting the list here so I know how to get back to them if/when I need to.  (Of course, along the way if you'd like to comment on them or suggest others to look at, please feel free to do so in the comments.)  Note, too, that by listing them here I'm not proposing, or even sure if, all of these pieces come together to a coherent structure.</p>
<h2>Grouper --- Internet2 Middleware</h2>
<p>"<a href="http://www.internet2.edu/products-services/trust-identity-middleware/grouper/" title="Grouper --- Internet2 Middleware">Grouper</a> is an open source toolkit for managing groups. It is designed to function as the core element of a common infrastructure for managing group information across integrated applications and repositories. Grouper combines multiple sources of group information, both automated and manual, in managing memberships and other group information in a Group Registry, a central information asset complementary to a site's Person Registry.  Grouper manages two primary types of objects: groups and namespaces. Groups are created and named within a namespace. Group management authority can be limited "</p>
<p>Now at version 0.9, Grouper is part of a suite of tools from the <a href="http://web.archive.org/web/20060718000000/http://www.nsf-middleware.org:80/" title="http://www.nsf-middleware.org/">NSF Middleware Initiative (NMI)</a> that supports "development, testing, and dissemination of architectures, software, and practices in the areas of identity and access management."</p>
<h2>Signet - Internet2 Middleware</h2>
<p>"Core middleware services such as identity management, directory, and authentication provide a foundation for secure, manageable applications throughout an institution. Even with this foundation, as systems and applications proliferate it becomes more and more difficult to manage user access consistently and cost-effectively. [The <a href="http://web.archive.org/web/20120618162953/http://middleware.internet2.edu/signet/" title="Signet - Internet2 Middleware">Signet] privilege management service</a> is a relatively new component of campus middleware that addresses this problem by providing centralized management of user privileges across a range of applications.  The benefits of this service include:  a standard user interface for privilege administrators; consistent, simplified policy definition, via roles and integration with core campus organizational data; improved visibility, understandability, and auditability of privilege information; and standard interfaces to other infrastructure services and to application systems to support integration."</p>
<p>Now at version 1.01, released 29-Mar-2006.  Could this kind of provisioning service be used to generate XACML files to drive FEDORA?</p>
<h2>OASIS eXtensible Access Control Markup Language (XACML)</h2>
<p>"<a href="http://www.oasis-open.org/committees/xacml/" title="http://www.oasis-open.org/committees/xacml/">XACML</a> is expected to address fine grained control of authorized activities, the effect of characteristics of the access requestor, the protocol over which the request is made, authorization based on classes of activities, and content introspection (i.e. authorization based on both the requestor and potentially attribute values within the target where the values of the attributes may not be known to the policy writer). XACML is also expected to suggest a policy authorization model to guide implementers of the authorization mechanism."</p>
<p><a href="http://sunxacml.sourceforge.net/" title="Sun&#039;s XACML Implementation">Sun's XACML Implementation</a> (available at Sourceforge) is the access management engine embedded into the FEDORA repository.</p>
<h2>Acegi Security System for Spring</h2>
<p>"<span class="removed_link" title="http://www.acegisecurity.org/">Acegi Security</span> is a powerful, flexible security solution for enterprise software, with a particular emphasis on applications that use <a href="http://www.springframework.org/" title="Springframework.org">Spring</a>. Using Acegi Security provides your applications with comprehensive authentication, authorization, instance-based access control, channel security and human user detection capabilities."</p>
<p>Release 1.0.0 came out in May 2006 after nearly two years of development.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.acegisecurity.org/ on August 22nd, 2012.</p>
