---
layout: wordpress-import
status: published
published: true
title: 'Best Practice Proposal for a DESCRIPTION Datastream'
modified: 2006-09-06T18:58:42+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 109
wordpress_url: http://dltj.org/2006/09/description-datastream/
date: '2006-09-06 14:58:42 -0400'
date_gmt: '2006-09-06 19:58:42 -0400'
category: Library Technology
categories:
- DRC
- Fedora
tags:
- DRC
- metadata
- Dublin Core
- libraries
- Fedora Repository
comments:
- id: 3837
  author: Ryan
  author_email: rscherle@indiana.edu
  author_url: ''
  date: '2006-09-12 11:58:13 -0400'
  date_gmt: '2006-09-12 15:58:13 -0400'
  content: This is definitely a reasonable approach. Indiana, Tufts, and Virginia
    are all taking similar approaches. The only difference is in the details. At Indiana,
    we're keeping as little as possible in Fedora's default DC datastream, and lumping
    all other metadata into a METS document in a METDADATA datastream (<a href="http://wiki.dlib.indiana.edu/confluence/x/uQE"
    rel="nofollow">philosophy</a>, <span class="removed_link" title="http://fedora.dlib.indiana.edu:9090/fedora/get/iudl:4420">sample
    object</span>). Tufts keeps a fairly complete record in the default DC, but the
    fully-complete records are in DCA-ADMIN and DCA-META (<a href="http://dl.tufts.edu:8080/fedora/get/tufts:UA069.005.DO.00001"
    title="Sample Object" rel="nofollow">sample object</a>). Virginia has their own
    metadata format, which can be found on their <a href="http://www.lib.virginia.edu/digital/metadata/index.html"
    rel="nofollow">metadata site</a>.<p style="padding:0;margin:0;font-style:italic;"
    class="removed_link">The text was modified to remove a link to http://fedora.dlib.indiana.edu:9090/fedora/get/iudl:4420
    on January 19th, 2011.</p>
- id: 3840
  author: the jester
  author_email: jester@DLTJ.org
  author_url: http://dltj.org/
  date: '2006-09-12 12:32:12 -0400'
  date_gmt: '2006-09-12 16:32:12 -0400'
  content: "[quote comment=\"3837\"]At Indiana, we're keeping as little as possible
    in Fedora's default DC datastream, and lumping all other metadata into a METS
    document in a METDADATA datastream (<a href=\"http://wiki.dlib.indiana.edu/confluence/x/uQE\"
    rel=\"nofollow\">philosophy</a>, <span class=\"removed_link\" title=\"http://fedora.dlib.indiana.edu:9090/fedora/get/iudl:4420\">sample
    object</span>).[/quote]\r\n\r\nI would note for those that haven't followed the
    \"philosophy\" link, that \"as little as possible\" in Indiana's case is:\r\n\r\n<blockquote>\r\nIt
    currently includes only these items:\r\n\r\nTitle\r\nPURL for the object (if this
    is an item-level object) in an Identifier field\r\nFedora PID for the object in
    an Identifier field\r\n\r\nThe \"real\" DC record (if present) will be in the
    [descriptive metadata] of the METS document, alongside any other descriptive metadata.\r\n<a
    href=\"http://wiki.dlib.indiana.edu/confluence/pages/viewpage.action?pageId=441#FedoraMetadataStoragePhilosophy-DublinCore\"
    rel=\"nofollow\">http://wiki.dlib.indiana.edu/confluence/pages/viewpage.action?pageId=441#FedoraMetadataStoragePhilosophy-DublinCore</a>\r\n</blockquote>\r\nThat
    certainly is bare-bones, but it makes a great deal of sense.\r\n\r\nThanks for
    the comment and the links to the examples, Ryan!<p style=\"padding:0;margin:0;font-style:italic;\"
    class=\"removed_link\">The text was modified to remove a link to http://fedora.dlib.indiana.edu:9090/fedora/get/iudl:4420
    on January 19th, 2011.</p>"
- id: 5730
  author: Sergio Berna
  author_email: sberna@gmail.com
  author_url: ''
  date: '2006-10-17 10:24:21 -0400'
  date_gmt: '2006-10-17 14:24:21 -0400'
  content: "[quote post=\"109\"]&ldquo;to establish a practice of creating an in-line
    XML2 datastream with the label &lsquo;DESCRIPTION&rsquo; that contains the primary
    descriptive metadata for each object.&rdquo;[/quote]\r\n\r\nInteresting proposal.
    Do you know of any recopilation project of these denominations of fedora inline
    datastreams?\r\n\r\nIn my case I have need for several descriptive datastreams.
    That need a richer vocabulary.\r\n\r\nThe first datastream would be the descriptive
    datastream, using the tag you propose.\r\n\r\nThen would follow preservation datastreams,
    Rights management datastream, format especification datastream, relations management
    datastream and many more that maybe thinking a little ahead could be equally named
    such as your proposal implies."
- id: 45242
  author: 'Re: [Fedora-commons-users] Where to store things you need to search?'
  author_email: ''
  author_url: http://www.mail-archive.com/fedora-commons-users@lists.sourceforge.net/msg01014.html
  date: '2010-02-22 05:46:35 -0500'
  date_gmt: '2010-02-22 10:46:35 -0500'
  content: <!--%kramer-ref-pre%-->[...] Steve. I also ran across this quotation at
    http://dltj.org/article/description-datastream/ "working with Fedora&#39;s compulsory
    Dublin Core (DC) datastream started one thinking about the [...]<!--%kramer-ref-post%-->
---
<p>OhioLINK is deep in the process of migrating content from our old Bulldog/Documentum-based system to, well, something else, and we've been talking about the treatment of the metadata in the course of the migration.  I think it is safe to say that the Bulldog asset management system (and Documentum, which bought and integrated Bulldog into its product line about five years ago) is not really known for its rich handling of metadata.  Or at least how the library community thinks of metadata:  Dublin Core, MIX, MODS, MARC, VRA Core, PREMIS, FGCD, etc. &mdash; all at the same time in the same application engine with structured crosswalks between them. <footnote>Reality check for those in the "library community" ... do you think of metadata in this way?</footnote> I think it is also safe to say that pure, unqualified Dublin Core, the only datastream that is required for every FEDORA object, does not completely encompass the descriptive fidelity needed for our objects.  These observations, combined with reading <a href="http://www.hull.ac.uk/esig/repomman/documents/" title="RepoMMan Documents">a mid-term project report from the RepoMMan effort</a> in the U.K., got me thinking about metadata and how we should store it in FEDORA objects.  The outcome of that line of thinking is this proposal:  "to establish a practice of creating an in-line XML datastream with the label 'DESCRIPTION' that contains the primary descriptive metadata for each object."</p>
<h2>Rationale</h2>
<p>Although FEDORA mandates an unqualified Dublin Core datastream for every object, unqualified Dublin Core is not expressive enough to describe our objects.  Therefore I recommend establishing this practice so subsequent agents/consumers of the objects (internal disseminators and external applications) will know the location of the most expressive metadata for the object.</p>
<h2>Risks/Unknowns</h2>
<ul>
<li>FEDORA does not provide a mechanism to keep elements of the DESCRIPTION datastream in sync with the DC datastream.  Do we store common data elements (e.g. "creator") in both places?  If so, our front-end applications would need to change the value of "creator" in two places and there is always the risk that they will get out of sync. How much real value is there in maintaining the FEDORA-mandated DC datastream?</li>
<li>There is no convention (that I know of) for a "primary descriptive metadata" datastream label in a FEDORA object, so "DESCRIPTION" is an arbitrary choice at this point.  Future practices may go against this decision (although the choice does set us up to start using datastream labels like "PRESERVATION" for PREMIS metadata and so forth).</li>
</ul>
<h2>Background</h2>
<p>In their "Experiences with Fedora" report, the RepoMMan team noted:</p>
<blockquote><p>
...working with Fedora's compulsory Dublin Core (DC) datastream started one thinking about the metadata that a repository object would eventually need and how this might be mapped onto the Dublin Core fields.  It was some considerable time later than an e-mail on the Fedora-users list made it clear that the inherent DC datastream was intended solely for Fedora's internal use and not as the basis of external searches. <footnote>Richard Green, "Experiences with Fedora during the project's first year" Report D-D8, July 2006; page 8; retrieved 28-Aug-2006 from <a href="http://www.hull.ac.uk/esig/repomman/downloads/D-D8-fedora-exp-v10.pdf" title="Experiences with Fedora during the project&#039;s first year">http://www.hull.ac.uk/esig/repomman/downloads/D-D8-fedora-exp-v10.pdf</a>.</footnote>
</p></blockquote>
<p>Even with our most simplest collection, we already know that unqualified Dublin Core will not be sufficient (most specifically, we had discussions about the lack of precision of "Date" and "Coverage" as compared to the field labels we already have in the Bulldog data dictionary).  It is important that our metadata be parsable by machine processes, so I would advocate the proposed practice rather than trying to "shoe-horn" our descriptions into unqualified Dublin Core with text labels added the values and the like.  And if we keep the machine parsable, we will have a wider variety of options for indexing the data and displaying it at the presentation layer.</p>
<p>The "in-line XML" part of this proposal means that the DESCRIPTION datastream would be "managed" by the FEDORA server (e.g. not external or referenced), so it would become part of the object in the content store.</p>
<h2>Example</h2>
<p>If we take for a moment what is displayed in the presentation layer for <span class="removed_link" title="http://worlddmc.ohiolink.edu/Science/Details?oid=4005859">a sample object from the Forestry collection</span> as the sum total of all of the descriptive metadata for an object of this collection, a corresponding DESCRIPTION datastream would look something like:<br />
```xml
<metadata xmlns="http://drc.ohiolink.edu/schema/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://drc.ohiolink.edu/schema/
http://drc.ohiolink.edu/schema/schema.xsd"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/">
<dc:title>Catalpa speciosa, bignonoides and Kampfera seeds.</dc>
  <dc:creator>Ohio Agricultural Experiment Station.  Dept. of
Forestry.</dc>
  <dc:description>Catalpa speciosa, bignonoides and Kampfera seeds.
Item #2</dc>
  <dc:contributor>Ohio Agricultural Research and Development
Center</dc>
  <dc:date>1908-12</dc>
  <dcterms:available xsi:type="dcterms:W3CDTF">
        2003-04-17T00:00:00
  </dcterms>
  <dc:type>photographic prints</dc>
  <dc:identifier>hdl:21151</dc>
  <dc:source>2</dc>
  <dmci:spatial>Ohio</dmci>
  <dc:rights>Copyright: Ohio State University</dc>
  <dcterms:licence xsi:type="dcterms:URI">
	http://library.osu.edu/sites/dlib/terms.html
  </dcterms>
</metadata>
```
<h2>Comments?</h2>
<p>Reactions to the proposal?  A rational step forward, or is there a better way?
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://worlddmc.ohiolink.edu/Science/Details?oid=4005859 on December 31st, 2010.</p>
