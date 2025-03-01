---
layout: wordpress-import
status: published
published: true
title: 'Thursday Threads: Technical Debt, QR Codes in National Parks, WebP Image Format, and SSL Cautions'
modified: 2010-10-07T16:17:11+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1706
wordpress_url: http://dltj.org/?p=1706
date: '2010-10-07 12:17:11 -0400'
date_gmt: '2010-10-07 16:17:11 -0400'
category: Thursday Threads
categories:
- Thursday Threads
tags:
- jpeg2000
- ssl
- security
- qr-code
- open courseware
- cryptography
- technical debt
- software development
- WebP
comments:
- id: 159801
  author: Jason Pinto
  author_email: ''
  author_url: http://twitter.com/jasonpinto/status/26751723433
  date: '2010-10-08 14:03:02 -0400'
  date_gmt: '2010-10-08 18:03:02 -0400'
  content: <span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">From the "Disruptive Library Technology Jester"
    - thinking of ideas for QR Codes in the library - http://ilnk.me/4b22</span></span>
- id: 159802
  author: Higher Ed CRM Guru
  author_email: ''
  author_url: http://twitter.com/hecrmguru/status/26674476328
  date: '2010-10-07 18:25:46 -0400'
  date_gmt: '2010-10-07 22:25:46 -0400'
  content: '<span class="topsy_trackback_comment"><span class="topsy_twitter_username"><span
    class="topsy_trackback_content">#HE #Tech Thursday Threads: Technical Debt, QR
    Codes in National Parks, WebP ...: [Fort Smith Park Superintendent ... http://bit.ly/dbmS0n</span></span>'
---
<p>Week #2 of this new project to highlight interesting tidbits from the previous seven days.  Well, things that were interesting to me that I hope will be interesting to <i><acronym title="Disruptive Library Technology Jester">DLTJ</acronym></i> readers.  Time will tell.<br />
<!--more--></p>
<h2>Technical Debt: A Perspective for Managers</h2>
<blockquote><p><a href="http://www.infoq.com/articles/technical-debt-levison" title="InfoQ: Technical Debt a Perspective for Managers">What is Technical Debt?</a> It&rsquo;s all &ldquo;those <em>internal</em> things that you choose not to do now, but which will impede future development if left undone&rdquo; [<a href="http://c2.com/cgi/wiki?TechnicalDebt" title="Technical Debt">Ward Cunningham</a>]. On the surface the application looks to be of high quality and in good condition, but these problems are hidden underneath. QA may even tell you that the application has quality and few defects, but there is still debt. If this debt isn&rsquo;t managed and reduced, the cost of writing/maintaining the code will eventually outweigh its value to customers.</p>
<p>Technical Debt is like a credit card that charges a high interest rate, just leaving the team with an outstanding balance cost. In this case, the costs are represented by time and effort needed to work around the problems. The longer the team takes to pay off the debt, the more interest is accumulated (in the form of additional workarounds) and the higher the costs for the business.</p></blockquote>
<p>This definition of the amorphous stuff that gets in the way of moving faster really resonates with me.</p>
<h2>A Case of Taking QR Codes to the Park</h2>
<p><a href="/assets/images/2010/10/NPS-QR-Code.jpg"><img src="/assets/images/2010/10/NPS-QR-Code.jpg" alt="" title="Sample National Park Service QR-Code" width="230" height="280" class="alignright size-full wp-image-1708" /></a></p>
<blockquote><p>[Fort Smith Park Superintendent Bill Black] sat through a few conference sessions held by the Arkansas Parks and Tourism Department about information technology, where he heard about QR (or Quick Response) codes&mdash;which are two-dimensional bar codes that can be used in a variety of ways. A company can choose from any number of sites that will generate a QR code for free and put that code almost anywhere&mdash;on a website, a postcard, or even a T-shirt. Then smartphone users use the camera on their phones to scan the bar code&mdash;some phones have the scanning technology built in, but older iPhones and the like will have to download a free app&mdash;and are instantly taken to whatever content is linked to the bar code.</p>
<p>&ldquo;On the drive home I got thinking about how it might work for interpretation purposes,&rdquo; Black says, and he began to consider how this technology might be deployed to provide information to park visitors.</p></blockquote>
<p>Econtent Magazine has this <a href="http://www.econtentmag.com/Articles/ArticleReader.aspx?ArticleID=69984" title="EcontentMag.com: A Case of Taking QR Codes to the Park">brief use case for QR Codes</a> as a way to link to more information in a national park.  Usage of <a href="http://en.wikipedia.org/wiki/QR_Code" title="QR Code - Wikipedia">QR Codes</a> seem to be creeping up, helped in no small part by efforts at Google in its <a href="http://web.archive.org/web/20130111155453/http://www.google.com:80/help/maps/favoriteplaces/business/barcode.html" title="QR Code - Google Favorite Places">Favorite Places</a> and <a href="http://tech.fortune.cnn.com/2010/10/01/google-url-shortenerqr-code-service-goes-public/" title="Google URL shortener/QR code service goes public | CNN Money">URL Shortner</a> services.  They aren't exactly common yet, but this is a place where libraries might get ahead of the game.  There have been several experiments with QR Codes in <a href="http://www.bath.ac.uk/library/services/qrcode.html" title="QR Codes at The Library">OPACs</a> and <a href="http://www.libsuccess.org/index.php?title=QR_Codes" title="QR Codes - Library Success: A Best Practices Wiki">other services</a>, for instance, and some <a href="http://musingsaboutlibrarianship.blogspot.com/2010/02/qr-codes-for-libraries-some-thoughts.html" title="Musings about librarianship: QR codes for libraries - some thoughts">great</a> <a href="http://lonewolflibrarian.wordpress.com/2010/02/28/application-of-qr-codes-in-libraries-02-28-10/" title="Application of QR Codes in Libraries | The Proverbial Lone Wolf Librarian's Weblog">thinking</a> about how they could be used.  Is there an education role for libraries in helping patrons use this new technique for connecting to information?</p>
<h2>WebP, a new image format for the Web</h2>
<blockquote><p>Most of the common image formats on the web today were established over a decade ago and are based on technology from around that time. Some engineers at Google decided to figure out if there was a way to further compress lossy images like JPEG to make them load faster, while still preserving quality and resolution. As part of this effort, we are releasing a developer preview of a new image format, <a href="http://code.google.com/speed/webp/" title="WebP Home">WebP</a>, that promises to significantly reduce the byte size of photos on the web, allowing web sites to load faster than before.</p></blockquote>
<p>On the heels of the <a href="/article/thursday-threads-2010w39/">mention here last week</a> of the <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=36351#c155" title="Comment #155 on Mozilla Buzilla bug #36351">bounty to add JPEG2000 support to Firefox</a> comes this <a href="http://blog.chromium.org/2010/09/webp-new-image-format-for-web.html" title="WebP, a new image format for the Web | Chromium Blog">announcement from Google</a> of a new image format for websites that is supposedly better than JPEG2000.  Lots of buzz around this, but not much in the way of commitment to support it yet.  I suppose the real test will be whether WebP will be supported in Firefox before JPEG2000...</p>
<h2>General Counsel's Role in Shoring Up Authentication Practices Used in Secure Communications</h2>
<blockquote><p>The major Internet browsers all currently use the Certificate Authority Trust Model to verify the identity of websites on behalf of end-users. (The Model involves third parties known as certificate authorities or "CAs" issuing digital certificates to browswers and website operators that enable the end-user's computer to cryptographically prove that the same CA that issued a certificate to the browser also issued a certificate to the website).  The CA Trust Model <a href="http://twit.tv/sn243" title="The TWiT Netcast Network with Leo Laporte"> has recently come under fire by the information security community </a>because of technical and institutional defects.  Steve Schultze and Ed Felten, <a href="http://www.freedom-to-tinker.com/blog/sjs/web-security-trust-models" title="Web Security Trust Models | Freedom to Tinker"> in previous posts here</a>, have outlined the Model's shortcomings and examined potential fixes.  The vulernabilities are a big deal because of the potential for man-in-the-middle wiretap exploits as well as imposter website scams.</p></blockquote>
<p>Is 'https' and 'SSL' as secure as you believe it is?  <a href="http://www.freedom-to-tinker.com/blog/sroosa/general-counsels-role-shoring-authentication-practices-used-secure-communications" title="General Counsel's Role in Shoring Up Authentication Practices Used in Secure Communications | Freedom to Tinker">These researchers point out</a> that it is only as good as your trust in the Certificate Authorities to issue SSL certificates to the appropriate web site owners and to keep safe the secrets necessary to make 'https' work.  Read this so that you have an informed sense of how secure your communications on the web actually are.</p>
<h2>M.I.T. Weighs Charges for Online Lectures</h2>
<blockquote><p>The Massachusetts Institute of Technology has announced that it is considering charging for access to online lectures and class notes, which are currently available free on the Web. Speaking at the Organization for Economic Cooperation and Development&rsquo;s Institutional Management in Higher Education conference in Paris this month, Lori Breslow, director of M.I.T.&rsquo;s Teaching and Learning Laboratory, said that free access &ldquo;may not be the best economic model, so we are now looking seriously at new e-learning opportunities.&rdquo;</p></blockquote>
<p>I only saw this <a href="http://www.nytimes.com/2010/09/27/education/27iht-educBriefs27.html" title="Briefly: M.I.T. Weighs Charges for Online Lectures | New York Times">brief mention</a> of this in the New York Times.  Were MIT seriously considering reversing its ground-breaking course to open up access to its lectures, I think there would be more talk.  Maybe I missed other discussion, but if this turns out to be the case then the open courseware movement has been dealt a serious blow.</p>
