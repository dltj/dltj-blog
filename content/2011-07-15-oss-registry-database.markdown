---
layout: wordpress-import
status: published
published: true
title: 'Seeking feedback on database design for an open source software registry'
modified: 2011-07-15T18:58:10+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 3103
wordpress_url: http://dltj.org/?p=3103
date: '2011-07-15 14:58:10 -0400'
date_gmt: '2011-07-15 18:58:10 -0400'
category: LYRASIS
categories:
- LYRASIS
tags:
- open source
- LYRASIS Technology Services
comments:
- id: 156601
  author: Dorothea Salo
  author_email: dorothea.salo@gmail.com
  author_url: http://dsalo.info/
  date: '2011-07-15 16:06:20 -0400'
  date_gmt: '2011-07-15 20:06:20 -0400'
  content: "I like this so far! Some questions:\r\n\r\n* I suspect some small-shop
    or indy developers will get heartburn at being told they're \"providers.\" They're
    not, really; they're just building the software and putting it out there. Is there
    a way to capture that association?\r\n\r\n* An enumeration for PackageType? Really?
    That's a little scary. What's the process for suggesting new PackageTypes?\r\n\r\n*
    I'm not really seeing how this db will answer question 2 (strengths/weaknesses);
    there doesn't seem to be any feature-comparison table."
- id: 156604
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-07-15 16:40:12 -0400'
  date_gmt: '2011-07-15 20:40:12 -0400'
  content: |-
    Good points, Dorothea!

    <blockquote>I suspect some small-shop or indy developers will get heartburn at being told they're "providers." They're not, really; they're just building the software and putting it out there. Is there a way to capture that association?</blockquote>

    I struggled with naming this one, too.  Originally it was "Vendors" but that wasn't inclusive of organizations like LYRASIS.  "Provider" seemed a bit more neutral.  The model would enforce, though, a situation where a Person would have to create a Provider (or an equivalently-named entity) to be recognized as an independent developer.  I'm certainly open to other names for this entity or other ways to model it.

    This also points out the need for another ProviderType enumeration:  "community."  I'm thinking, for instance, of organizations like DuraSpace and Kuali and the Koha Foundation -- some place that is the home of the intellectual property of an open source project.  Is "community" the right word?

    <blockquote>An enumeration for PackageType? Really? That's a little scary. What's the process for suggesting new PackageTypes?</blockquote>

    Yeah, I thought there was a need for a controled vocabulary there to enable efficient browsing and searching.  I'm still working on proposed governance policies, but in order for the registry to work well in our delightfully anarchistic realm the process would need to be pretty efficient and light-weight.  Maybe a new term is created arbitrarily by the Person first entering details about the package (e.g. if there isn't an appropriate term, make one up), and the new term is subject to review by a group of volunteer registry stewards.

    <blockquote>I'm not really seeing how this db will answer question 2 (strengths/weaknesses); there doesn't seem to be any feature-comparison table.</blockquote>

    Hmmm, yeah.  An earlier version of the model had a Feature entity that was related to the enumeration of PackageType (so all packages of a certain type would share the same possible Features) and the Package entity.  It added significant complexity to the model, though, so I remember taking it out.  It looks like I should have left it in there, though.  <i>sigh</i>
- id: 156651
  author: David Buttrick
  author_email: dbuttrick@geekforce.com
  author_url: ''
  date: '2011-07-16 00:37:02 -0400'
  date_gmt: '2011-07-16 04:37:02 -0400'
  content: "I think that you probably want to focus on the entities that are important
    to your business need, and let a system handle the rest.\r\n\r\nYou have tables
    in here for events, and persons. Why bother? \r\nHow would your tables handle
    an event that covered more than pone package?\r\nPlug this into any CRM tool,
    and use it, create your business objects there. Dont reinvent the wheel.\r\n\r\nI
    think that your Question 2 is really important, and needs to b thought through.
    In the same that you want to be able to organize package, and people around languages,
    and skill sets, packages use libraries, that in and of themselves might require
    expertise that needs to be expressed in here.\r\n\r\nI think that the Release
    entity has, as a child, a Version entity which has Version properties; for example:
    Major Number, Minor Number, Sub and Quality. Quality is perhaps an enumeration
    - Beta, Gold, etc... Compound this with the fact that almost everyone handles
    versioning differently, and this could get to be tricky.\r\n\r\nIt might be easier
    to track Major numbers, date of releases, and quality of code (Beta, Gold)...\r\n\r\nJust
    my 2 cents.\r\n\r\nDavid"
- id: 156675
  author: Jodi Schneider
  author_email: jodi.a.schneider@gmail.com
  author_url: http://jodischneider.com/
  date: '2011-07-16 04:49:05 -0400'
  date_gmt: '2011-07-16 08:49:05 -0400'
  content: "Maybe the talk page of the diagram would be a good place to have comments?\r\n\r\nIs
    the license relevant?"
- id: 157116
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-07-18 10:23:55 -0400'
  date_gmt: '2011-07-18 14:23:55 -0400'
  content: "Thanks for your comments, David.\n\n<blockquote>I think that you probably
    want to focus on the entities that are important to your business need, and let
    a system handle the rest.\n\nYou have tables in here for events, and persons.
    Why bother? \nHow would your tables handle an event that covered more than pone
    package?\nPlug this into any CRM tool, and use it, create your business objects
    there. Dont reinvent the wheel.</blockquote>\n\nMy intention was to be working
    at the conceptual level with the E-R diagram. The underlying system is spec'd
    to be Drupal, so it will use the core users module and an events module. The key
    part I want to get across to the developer is the relationship between built-in
    entities and any entities (node types) that will have to be created. \n\n<blockquote>I
    think that your Question 2 is really important, and needs to b thought through.
    In the same that you want to be able to organize package, and people around languages,
    and skill sets, packages use libraries, that in and of themselves might require
    expertise that needs to be expressed in here.</blockquote>\n\nYes, I'm becoming
    more convinced that the added complexity to the model will be needed. \n\n<blockquote>I
    think that the Release entity has, as a child, a Version entity which has Version
    properties; for example: Major Number, Minor Number, Sub and Quality. Quality
    is perhaps an enumeration - Beta, Gold, etc... Compound this with the fact that
    almost everyone handles versioning differently, and this could get to be tricky.</blockquote>\n\nMy
    thought was that I wouldn't need to do any computing on the version attribute
    of a release. At most, it would be valuable to sort them chronologically and the
    date of the release would be sufficient to do that. You have a good point about
    how a release can have many versions as it goes through alpha, beta, and release
    candidate stages before hitting a gold master stage. This is complicated by the
    fact that some project's betas can be production-ready while another's would barely
    run. \n\nCode quality is a good suggestion. Would it be up to the person making
    the release to assign that value or it it better an attribute of a comment on
    a Version/Release?\n\n<blockquote>It might be easier to track Major numbers, date
    of releases, and quality of code (Beta, Gold)...</blockquote>\n\nThanks again.
    The input is much appreciated."
- id: 157117
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-07-18 10:24:44 -0400'
  date_gmt: '2011-07-18 14:24:44 -0400'
  content: |-
    Thanks, Jodi.

    <blockquote>Maybe the talk page of the diagram would be a good place to have comments?</blockquote>

    That is a good option, too. I'll take comments however I can get them!

    <blockquote>Is the license relevant?</blockquote>

    Sorry, I'm not following. Are you referring to the "licence" attribute in the model?  If so, I'm not sure if it is relevant, so that is one of the areas I'm looking for feedback. License is (arguably) important for those writing code and integrating code from othe projects. (The concern of including so-called 'viral' licenses.) I don't think libraries searching for software that matches their needs and capabilities are as concerned about that. Some validation of that opinion would be welcome, though!
- id: 159705
  author: ALA_TechSource
  author_email: ''
  author_url: http://twitter.com/ala_techsource/status/93005879607173120
  date: '2011-07-18 17:15:04 -0400'
  date_gmt: '2011-07-18 21:15:04 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Via @DataG Seeking feedback on database design
    for an open source software registry  http://bit.ly/r7WyK3</span></span>
- id: 159706
  author: Billy Bonkoski
  author_email: ''
  author_url: http://twitter.com/nitedreamer1/status/92084685290733569
  date: '2011-07-16 04:14:34 -0400'
  date_gmt: '2011-07-16 08:14:34 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Seeking feedback on database design for an open
    source software ... http://bit.ly/nyHXqP</span></span>
- id: 159707
  author: The Software Gang
  author_email: ''
  author_url: http://twitter.com/thesoftwaregang/status/91969344816414720
  date: '2011-07-15 20:36:15 -0400'
  date_gmt: '2011-07-16 00:36:15 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">#Software Seeking feedback on database design
    for an open source software ...: Where can my library go to get tr... http://bit.ly/nmN9RO</span></span>'
- id: 159710
  author: Jordi Serrano
  author_email: ''
  author_url: http://twitter.com/jserranom/status/91950447992119296
  date: '2011-07-15 19:21:09 -0400'
  date_gmt: '2011-07-15 23:21:09 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Seeking feedback on database design for an open
    source software registry | Disruptive Library Technology Jester: http://t.co/q4sLGoO</span></span>'
- id: 175478
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/91955318073999360
  date: '2011-07-15 19:40:30 -0400'
  date_gmt: '2011-07-15 23:40:30 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Seeking feedback on database design
    for an open source software registry http://bit.ly/ncGObV</span></span>'
- id: 175479
  author: Library Feed
  author_email: ''
  author_url: http://twitter.com/libraryfeed/status/91952890146603008
  date: '2011-07-15 19:30:52 -0400'
  date_gmt: '2011-07-15 23:30:52 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Seeking feedback on database design for an open
    source software registry http://bit.ly/n6P9OM</span></span>
---
<p>As part of the Mellon Foundation grant <a href="http://web.archive.org/web/20120624232639/http://www.lyrasis.org:80/News/Press-Releases/2011/LYRASIS-Receives-Grant-to-Support-Open-Source.aspx" title="LYRASIS Receives Grant to Support Open Source | LYRASIS news">funding the start-up</a> of <a href="http://www.lyrasis.org/LYRASIS%20Digital/Pages/default.aspx" title="LYRASIS Technology Services">LYRASIS Technology Services</a>, LTS is establishing a registry to provide in-depth comparative, evaluative, and version information about open source products.  This registry will be free for viewing and editing (all libraries, not just LYRASIS members, and any provider offering services for open source software in libraries).  <a href="http://drupal.org/" title="Drupal homepage">Drupal</a> will be the underlying content system, and it will be hosted by <a href="http://www.lyrasis.org/" title="LYRASIS homepage">LYRASIS</a>.</p>
<p>I'm seeking input on a data model that is intended to answer these questions:</p>
<ul>
<li>What open source options exist to meet a particular need of my library?</li>
<li>What are the strengths and weaknesses of an open source package?</li>
<li>My library has developers with skills in specific technologies. What open source packages mesh well with the skills my library has in-house?</li>
<li>Where can my library go to get training, documentation, hosting, and/or contract software development for a specific open source package?</li>
<li>Are any peers using this open source software?</li>
<li>Where is there more information about this open source software package? </li>
</ul>
<p>The <a href="http://wiki.code4lib.org/index.php/Registry_E-R_Diagram" title="Registry E-R Diagram | Code4Lib wiki">entity-relationship data model and narrative surrounding it</a> are on the Code4Lib wiki.  Comments on the data model can be made as changes to the wiki document, replies posted here, or <a href="mailto:Peter.Murray@lyrasis.org?subject=Comment%20about%20Registry%20Data%20Model">e-mail sent directly to me</a>.  In addition to comments on the data model, I'm particularly interested in answers to these questions (also listed at the bottom of the wiki page):</p>
<ol>
<li>The model does not provide for a relationship between a person and a software package. Would such a relationship be useful? E.g., individuals self-identifying as affiliated with an open source software package.</li>
<li>The initial planning process did not account for the inclusion of packages that were not themselves end products. Should code libraries and support programs be included as packages in the registry? The model could conceivably be adjusted in two ways to account for this. The simplest would only require the addition of new PackageType enumerations (e.g. &ldquo;code library&rdquo;); this would not allow for searching of packages that use code libraries (e.g., answering the question &ldquo;What repositories use the djatoka JPEG2000 viewer system?&rdquo;) Another simple change would be to add &ldquo;code library&rdquo; to the TechType enumeration; the code library would not have the benefit of links to other relationships and entities.  A more complicated change would do both but there would be no relationship between the code library as a Package and as a Technology.  Are there better ways to add code libraries to the model?</li>
<li>Some who have reviewed the concept for the registry suggested other attributes. Should these be added? (And what is missing?)
<ul>
<li>Package &ndash; Translations</li>
<li>Package &ndash; Intended audience (e.g. developers, patrons/desktop, patrons/web, library-staff/desktop, library-staff/web)</li>
<li>Version &ndash; Code maturity (e.g., alpha, beta, release candidate, formal release)</li>
</ul>
</li>
<li>To answer the question &ldquo;Are any peers using this open source software?&rdquo; is it necessary to have an enumeration of library types? Public library, school library, university library, community college library, special library, museum (others?)</li>
<li>Is the location of Institutions and Providers desired? One reason it might be desirable is to do a geography-based search (e.g. training providers within a 60-mile radius).</li>
</ol>
<p>Feel free to add to the list of questions.  I'm looking forward to your thoughts.</p>
