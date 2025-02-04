---
layout: wordpress-import
status: published
published: true
title: 'Thursday Threads: Estimating and Understanding Big Data, Key Loggers Steal Patron Keystrokes'
modified: 2011-02-17T11:39:12+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 2647
wordpress_url: http://dltj.org/?p=2647
date: '2011-02-17 06:39:12 -0500'
date_gmt: '2011-02-17 11:39:12 -0500'
category: Thursday Threads
categories:
- Thursday Threads
tags:
- research
- visualization
- public library
- storage
- security
comments:
- id: 160091
  author: ALA_TechSource
  author_email: ''
  author_url: ''
  date: '2011-02-17 20:05:17 -0500'
  date_gmt: '2011-02-18 01:05:17 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Via @DataG Thursday Threads: Estimating and Understanding
    Big Data, Key Loggers Steal Patron Keystrokes http://bit.ly/ibu7gL</span></span>'
- id: 160092
  author: infopeep
  author_email: ''
  author_url: http://twitter.com/infopeep/status/38208345999413248
  date: '2011-02-17 12:09:14 -0500'
  date_gmt: '2011-02-17 17:09:14 -0500'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">Murray, Peter: Thursday Threads: Estimating and
    Understanding Big Data, Key Loggers Steal Patron Keystrokes http://bit.ly/faqpKO</span></span>'
---

<p> Two entries on big data lead this week's edition of <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym> Thursday Threads</i>.  The first is at the grandest scale possible: a <a href="#p2647-information">calculation of the amount of information in the world</a>.  Add up all the digital memory (in cell phones, computers, and other devices) and analog media (for instance, paper) and it goes to a very big number.  The authors try to put it in perspective, which for me brought home how insignificant my line of work can be.  (All of our information is still less than 1% of what is encoded in the human DNA?)  The second "big data" entry describes an effort to <a href="#p2647-archives">make sense of huge amounts of data in the National Archives</a> through the use of visualization tools.  Rounding out this week is a warning to those who run public computers -- <a href="#p2647-keyloggers">be on the look-out for key loggers</a> that can be used to steal information from users.</p>
{{ thursday_threads_header() }}</p>
<h2 id="p2647-information">How Much Information Is There in the World?</h2>
<blockquote><p>{{ captioned(
    div_float="right",
    width="229",
    caption="Video with author of paper (4 minutes)",
    contents='<iframe src="http://player.vimeo.com/video/19779116" width="229" height="129" frameborder="0"></iframe>') }} So how much information is there in the world? How much has it grown?</p>
<p>Prepare for some big numbers:
<ul>
<li>Looking at both digital memory and analog devices, the researchers calculate that humankind is able to store at least 295 exabytes of information. (Yes, that&rsquo;s a number with 20 zeroes in it.)
<p>Put another way, if a single star is a bit of information, that&rsquo;s a galaxy of information for every person in the world. But it&rsquo;s still less than 1 percent of the information stored in all the DNA molecules of a human being.</li>
<li>2002 could be considered the beginning of the digital age, the first year worldwide digital storage capacity overtook total analog capacity. As of 2007, almost 94 percent of our memory is in digital form.</li>
<li>In 2007, humankind successfully sent 1.9 zettabytes of information through broadcast technology such as televisions and GPS. That&rsquo;s equivalent to every person in the world reading 174 newspapers every day.</li>
</ul>
</blockquote>
<p>Feeling swamped in data?  You probably don't have it too bad.  Also see <span class="removed_link" title="http://www.vimeo.com/19779116">a video interview</span> (4 minutes, embedded above) and a <a href="http://www.sciencemag.org/content/early/2011/02/09/science.1200970/suppl/DC2" title="Podcast Interview  |  Science/AAAS">podcast interview</a> (12 minutes) with one of the authors that briefly describe some of the findings in the <a href="http://www.sciencemag.org/content/early/2011/02/09/science.1200970.short" title="The World's Technological Capacity to Store, Communicate, and Compute Information  |  Science/AAAS">original paper</a> (subscription to Science Magazine required).</p>
<h2 id="p2647-archives">A Window on the Archives of the Future</h2>
<blockquote><p>In collaborating with NARA, members of TACC&rsquo;s Data and Information Analysis group developed a multi-pronged approach to address technical challenges. The overall goal of their research is to investigate different data analysis methods within a visualization framework. The visualization interface is the bridge between the archivist and the analysis results, which are rendered visually onscreen as the archivists make selections and interact with the data. The results are presented as forms, colors and ranges of color to assist in synthesis and to facilitate an understanding of large-scale electronic records collections.</p></blockquote>
<p>This <a href="http://www.tacc.utexas.edu/news/feature-stories/2011/a-window-on-the-archives-of-the-future/" title="A Window on the Archives of the Future">article</a> from the Texas Advanced Computing Center describes a research project to visualize the volumes of digital data in the National Archives.  The visualization provides information about the amount of particular types of information, an assessment of the risks to files in the archive based on file type, and other metrics.  A brief paper from the Society for Imaging Science and Technology "Archives" proceedings last year, <a href="http://www.imaging.org/ist/publications/reporter/articles/REP25_3_ARCH2010_XU.pdf" title="Visualization for Archival Appraisal of Large Digital Collections">Visualization for Archival Appraisal of Large Digital Collections</a> [PDF], goes into more detail.</p>
<h2 id="p2647-keyloggers">Hardware keyloggers discovered at public libraries</h2>
<blockquote><p>{{ image(
    div_float="right",
    width="170",
    caption="USB Key Logger, courtesy of Sophos",
    alt="Photograph of a USB Key Logging device",
    localsrc="2011/02/usb-keylogger-170.jpg") }}
 Public libraries in Manchester, England, have been advised to keep their eyes peeled for USB bugs after two devices were discovered monitoring every keystroke made by every user of affected PCs.</p>
<p>According to <a href="http://menmedia.co.uk/manchestereveningnews/news/s/1407644_cybercrime_alert_after_bugs_found_in_library_computers" title="Link to Manchester Evening News media report">local media reports</a>, the small surveillance devices were found attached to the keyboard sockets at the back of two PCs in Wilmslow and Handforth libraries.</p></blockquote>
<p>Sophos, maker of internet security software, <a href="http://nakedsecurity.sophos.com/2011/02/14/hardware-keyloggers-discovered-public-libraries/" title="Hardware keyloggers discovered at public libraries | Naked Security">posted this notice</a> about key-logging devices attached to public library computers in the U.K.  This device would make it possible to capture usernames and passwords typed at the keyboard by patrons.  The article goes on to suggest actions: conduct frequent checks of hardware and to plug keyboards into USB ports on the <em>front</em> of computers for easy visual inspection.  [Via <a href="http://www.librarian.net/stax/3510/would-you-recognize-a-hardware-keylogger-in-your-library/" title="would you recognize a hardware keylogger in your library? | librarian.net">Jessamyn West</a>]
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.vimeo.com/19779116 on November 21st, 2012.</p>
