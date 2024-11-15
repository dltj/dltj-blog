---
layout: wordpress-import
status: published
published: true
title: 'Encryption of Patron Data in Modern Integrated Library Systems'
modified: 2011-05-04T00:30:24+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 2853
wordpress_url: http://dltj.org/?p=2853
date: '2011-05-03 20:30:24 -0400'
date_gmt: '2011-05-04 00:30:24 -0400'
category: L/IS Profession
categories:
- L/IS Profession
tags:
- privacy
- encryption
- integrated library system
- security
comments:
- id: 139499
  author: Jon Gorman
  author_email: jonathan.gorman@gmail.com
  author_url: ''
  date: '2011-05-04 10:36:17 -0400'
  date_gmt: '2011-05-04 14:36:17 -0400'
  content: "The encryption of patron information in a lot of libraries systems is
    incredibly weak.  Indeed, I still stumble across sites that on the webends to
    ILS systems that don't even use https.\r\n\r\nOn the positive side, there's a
    lot of institutions that only track currently checked out books, which at least
    provides a decent level of privacy if not a great one.\r\n\r\nThese issues actually
    probably occur at multiple levels in the library.  After all, information put
    into the ILS has to come from somewhere and I'd wager that the information in
    many system still takes the form of text files which are not encrypted.  The nice
    thing is at this level it's easier to either encrypt information if it must stay
    on disk or to try to use strong deletion.  This is an area I've tried to focus
    a bit of energy on.  (For starters, make sure we get the minimal information required
    to run our systems and no more, avoid storing on disk if possible, and encrypt
    any information that does in a secured location.  There's various programming
    libraries out there and for more manual work look at TrueCrypt and similar packages
    )\r\n\r\nMore enterprise level systems with personnel information seem to be moving
    more towards either messaging models (a new person is added and information gets
    pushed out over an encrypted messaging system) or a central authentication and
    authorization model (we just tell Shibboleth person is allowed in if meet criteria
    a/b/c and Shibboleth basically says \"yes/no\") .  Hopefully library vendors can
    move toward supporting these models.  A fair number do seem like they're looking
    into it, particularly if they support the academic market.\r\n\r\nStrong deletion
    mechanisms would be particularly tricky as most ILS are built off of a technology
    stack.  There's no \"patron record\" as in a file that resides in disk but rather
    just information scattered across database tables.  I'm not on the cutting edge,
    but I'd be surprised if database vendors even do offer \"strong deletions\" if
    \ library technology companies implement them."
- id: 139557
  author: Coral
  author_email: coral@sheldon-hess.org
  author_url: http://sheldon-hess.org/coral
  date: '2011-05-04 17:45:45 -0400'
  date_gmt: '2011-05-04 21:45:45 -0400'
  content: 'FYI: The graphic showed up just fine in Google Reader.'
- id: 139567
  author: Jonathan Rochkind
  author_email: rochkind@jhu.edu
  author_url: http://bibwild.wordpress.com
  date: '2011-05-04 19:18:00 -0400'
  date_gmt: '2011-05-04 23:18:00 -0400'
  content: "The trick is, that with the number of disparate systems from disparate
    sources (proprietary, shared open source, homegrown in-house).... it is a significant
    expenditure of resources just to answer these questions. Let alone to do anything
    about unsatisfactory answers. \r\n\r\nIn library school, for a course assignment,
    we had to create a fake privacy policy for a library. Mine (I had a CS background
    before library school too) said that regular privacy audits would be conducted
    regularly recording exactly what private information was held in what systems,
    and how it was secured. After I started actually working in a library systems
    department, I realized how 'unrealistic' that was; I have not been able to do
    that myself. \r\n\r\nI do still think it OUGHT to be done yes. But it takes some
    high level people realizing that it will take significant resources, and it's
    not optional.  The sub-standard behavior of some of our proprietary vendors will
    increase the cost too."
- id: 139707
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2011-05-05 11:32:41 -0400'
  date_gmt: '2011-05-05 15:32:41 -0400'
  content: "Jon -- that kind of messaging system is also attractive because information
    is only ever stored in one place.  Why should the ILS need patron address information
    when it can look it up dynamically out of a directory.  So, ideally, what is stored
    in the circulation module is just the fact that a certain patron identifier has
    checked out certain item identifiers.  If the keys are opaque enough then just
    having the circulation module data released is not a big privacy concern.  (One
    would, of course, need some kind of guarantee that the source of the address information
    for that patron identifier will keep it around so you can still send notices and
    bills.)\r\n\r\nJonathan -- the effort required to audit systems and then act on
    the audit results may have been the impetus of my \"How much effort do you want
    to spend securing your computer systems?\" thought.  (I can't remember exactly.)
    \ But that they might not be regularly done in our field points to the extraordinarily
    thin ice (and perhaps extraordinary luck) that we've got.\r\n\r\nCoral -- thanks
    for the feedback.  I noticed what was displayed in Google Reader was the PNG image
    alternate to the SVG graphic.  So in think I can declare insertion-of-SVG-into-blog-post
    a success."
- id: 160062
  author: ALA_TechSource
  author_email: ''
  author_url: http://twitter.com/ala_techsource/status/65845726630002689
  date: '2011-05-04 18:30:19 -0400'
  date_gmt: '2011-05-04 22:30:19 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">via @DataG Encryption of Patron Data in Modern
    Integrated Library Systems  http://bit.ly/lMcQHG</span></span>
- id: 160063
  author: Library Feed
  author_email: ''
  author_url: http://twitter.com/libraryfeed/status/65677382949941248
  date: '2011-05-04 07:21:22 -0400'
  date_gmt: '2011-05-04 11:21:22 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Encryption of Patron Data in Modern Integrated
    Library Systems http://bit.ly/kBc8j6</span></span>
- id: 160064
  author: Jill Armour
  author_email: ''
  author_url: http://twitter.com/pcdatasecurity/status/65623558373650432
  date: '2011-05-04 03:47:30 -0400'
  date_gmt: '2011-05-04 07:47:30 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Encryption of Patron Data in Modern Integrated
    Library Systems ...: For instance, Oracle has &ldquo;Transparent Data E... http://bit.ly/lmsCjn</span></span>'
- id: 160065
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/65585786866765824
  date: '2011-05-04 01:17:24 -0400'
  date_gmt: '2011-05-04 05:17:24 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Encryption of Patron Data in Modern
    Integrated Library Systems http://bit.ly/itjYH3</span></span>'
- id: 160066
  author: adtech.feed
  author_email: ''
  author_url: http://twitter.com/adtechfeed/status/65575844302692352
  date: '2011-05-04 00:37:54 -0400'
  date_gmt: '2011-05-04 04:37:54 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Encryption of Patron Data in Modern Integrated
    Library Systems: "How much effort do you want to spend securing y... http://bit.ly/inzfJ7</span></span>'
---
<p>"How much effort do you want to spend securing your computer systems?  Well, how much do you not want to be in front of a reporter's microphone if a security breach happens?"  I don't remember the exact words, but that quote strongly resembles something I said to a boss at a previous job.  Securing systems is unglamorous detail work.  One slip-up plus one persistent (or lucky) attacker means years of dedicated efforts are all for naught as personal information is inadvertently released.  See, for example, what happened recently with <a href="http://news.consumerreports.org/electronics/2011/05/sony-25-million-more-accounts-hacked-but-were-really-sorry.html" title="Sony: 25 million more accounts hacked, but we're really sorry | Consumer Reports">Sony Online Entertainment's</a> recent troubles.</p>
<p>It was in that frame of mind that I responded to a series of questions from a librarian taking a computer science class.  (As someone else who straddles the computer-science/library-science divide, I wanted to encourage this line of thinking!)  Now library systems typically don't have credit card information, so they may not be attractive to individuals that seek to expose or exploit personal information.  But our systems do have physical addresses, e-mail addresses, and sometimes birthdays or other personal data.  And we have a <a href="http://www.ala.org/ala/issuesadvocacy/intfreedom/librarybill/interpretations/privacy.cfm" title="An Interpretation of the Library Bill of Rights: Privacy | ALA">professional ethic to keep patron use information private</a>.</p>
<p>The person that sent me these questions asked that I not mention a name or affiliation, but that it was okay that I repost the questions along with my replies.  I'm hoping this encourages some discussion because my understanding of the use of encryption in ILS products is very narrow and only somewhat deep (and is getting shallower by the day as my direct experience is going on ten years old).</p>
<blockquote><p>Background on the project is that during our encryption unit, I realized that I didn't know anything about what libraries to do back up our strongly stated policies about protecting patron privacy, so I wanted to find out more about it.</p>
<p>Questions:</p>
<ol type="1" start="1">
<li>What encryption tools/standards, if any, are used to safeguard patron accounts (name, items checked out, databases accessed, etc.) at the library?</li>
<li>Where in the systems do these tools typically fit -- at the ILS level, or somewhere else? (e.g., university ID systems)</li>
<li>How are circulation and other records expunged? I.e., are they permanently deleted in such a way that hard drive forensics couldn't bring them back?</li>
</ol>
</blockquote>
<p>In my experience, this patron information is not encrypted in integrated library systems.  The difficulty is that if those bits of information are encrypted, they must be decrypted by the program in order to be useful (generating an overdue notice means the patron's information must be known to the program, displaying the patron's name on his/her account information screen, etc.).  And for programs to decrypt they must have the secret key.  And if the programs know the secret key it is trivial for an attacker to get the key as well.  And since good encryption, by its nature, is computationally "expensive" there would be a lot of system load with all of the encryption and decryption of bits of information.  (Computationally expensive is good because it makes it harder for an attacker to guess the correct key.)</p>
{{ captioned(
    div_float="right",
    width="448",
    caption="Password Hashing Flowchart",
    contents='<object width="448" height="379" type="image/svg+xml" data="http://dltj.org/wp-content/uploads/2011/05/Password-Hashing.svg"><img src="/assets/images/2011/05/Password-Hashing.png" alt="" title="Password Hashing Flowchart" class="size-full wp-image-2856" /></object>') }}
<p>Note that passwords are a special case.  Passwords are not really encrypted in a database; rather the output of a "one way hash" algorithm is stored.  When the user tries to log in, the same one way hash algorithm is applied to the text string entered as a password and if the output matches what is stored in the database the user is let in.</p>
<p>As the diagram shows, with the login attempts the hashed password is not decrypted; the output of the hash algorithm is compared to what is known to be the hashed password.</p>
<p>[Aside: I'm trying an experiment in this post.  The diagram is a Scalable Vector Graphic (SVG) file.  It seems to be showing up fine in the browsers I'm testing, but I have no idea how it will appear in the RSS feed or if you are using an RSS reader or receiving this post via <a href="http://feedburner.google.com/fb/a/mailverify?uri=DisruptiveLibraryTechnologyJester&amp;loc=en_US" title="FeedBurner Email Subscription">FeedBurner e-mail</a>.  If you don't see the graphic, try viewing the post via the <a href="/article/ils-encryption/"><i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym></i> website.</a>]</p>
<p>The most effective encryption would be at the database management system layer.  For instance, Oracle has "<a href="http://www.oracle.com/technetwork/database/options/advanced-security/index-099011.html" title="Transparent Data Encryption | Oracle">Transparent Data Encryption</a>" feature.  "Data is automatically encrypted when it is written to disk and automatically decrypted when accessed by the application."  Automatic encryption is not built into MySQL, but you can use a <a href="http://dev.mysql.com/doc/refman/5.5/en/encryption-functions.html#function_aes-encrypt" title="Encryption and Compression Functions | MySQL 5.5 Reference Manual">MySQL-specific function to encrypt a field</a>.  PostgreSQL has a <a href="http://www.postgresql.org/docs/current/static/pgcrypto.html" title="pgcrypto | PostgreSQL Documentation">contributed module</a> that performs the function.</p>
<p>Another option -- other than database-level encryption -- is to have the operating system encrypt the underlying filesystem (for example, the <a href="http://web.archive.org/web/20120707164204/http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/filesysnew-efs.html" title="Encrypted File System | Red Hat documentation">Red Hat Encrypted Filesystem</a>).  That way all of the database storage files -- stored in that filesystem directory -- would be encrypted.</p>
<p>Note, though, that in any of these cases, the key is known to the computer somehow, and so it is possible for an attacker to recover the key and decrypt the data.  There are, of course, varying levels of obscurity one can apply to the key, but I think we're getting pretty far off on a tangent.</p>
<p>How often circulation and other records would be expunged would depend on implementations in each software system, but as a general guideline I don't think a strong deletion mechanism is used to obliterate data on the disk.  I'd be happy to be proven otherwise.  And as you consider hard drive forensics, also think about pulling the same information off backup tapes; that would probably be easier to get to.</p>
<p>In a follow-up, I was asked:</p>
<blockquote><p>WRT your response on Q2, do you have an idea of what level "most" or "some" libraries might have the encryption, or were you speaking purely from a view of what ideal/good situations might look like?</p>
<p>On 3, I have heard from a few others that there seems to be just deletion with no zeroing out features or the like and that it does take a period of time (1-2 months) for backup tapes to be overwritten. So it strikes me that the weakest link may be in the area we talk most about protecting.</p></blockquote>
<p>With regards to the database-level or the filesystem-level encryption, I was speaking from a point of view of what idea/good situations might look like.  One of the outcomes of posting these questions to a wider group of readers is, I hope, more real-world experience reports from people who might be running systems that actually do this.</p>
<p>Yes, I think those are weak links, with the backup tapes being the biggest problem.  One can't predict when blocks on a live filesystem disk will be overwritten, but overwriting tapes is pretty predictable -- and easy because one doesn't need access to the live system.</p>
