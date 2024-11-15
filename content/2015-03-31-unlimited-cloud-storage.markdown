---
layout: wordpress-import
status: published
published: true
title: 'What Does it Mean to Have Unlimited Storage in the Cloud?'
modified: 2015-04-01T00:33:01+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 25269
wordpress_url: http://dltj.org/?p=25269
date: '2015-03-31 20:33:01 -0400'
date_gmt: '2015-04-01 00:33:01 -0400'
category: Raw Technology
categories:
- Raw Technology
tags:
- Amazon
- Google
- apache
- Microsoft
- storage
- cloud storage
- Dropbox
- Apache Hadoop
- Distributed file systems
comments: []
---
<p>We've seen big announcements recently about unlimited cloud storage offerings for a flat monthly or fee.   Dropbox offers it for subscribers to its <a href="https://www.dropbox.com/business/pricing">Business</a> plan.  Similarly, <a href="http://googleforwork.blogspot.com/2014/06/unlimit-your-business-with-google-drive.html" title="Official Google for Work Blog: Unlimit your business with Google Drive for Work">Google</a> has unlimited storage for Google Apps for Business customers.  In both cases, though, you have to be part of a business group of some sort.  Then <a href="https://blog.onedrive.com/office-365-onedrive-unlimited-storage/">Microsoft</a> unlimited storage for any subscriber of all Office 365 customers (Home, School, and soon Business) as bundled offering of OneDrive with the Office suite of products.   Now comes word today from <a href="https://www.amazon.com/clouddrive">Amazon</a> of unlimited storage to consumers...no need to be part of a business grouping or have bundled software come with it.</p>
<p>Today a colleague asked why all of this cloud storage couldn't be used as file storage for the Islandora hosting service that is offered by LYRASIS.  On the surface, it would seem to be a perfect backup strategy -- particularly if you subscribed to multiple of these services and ran audits between them to make sure that they were truly in sync.  Alas, the terms of service prevent you from doing something like that.  Here is an excerpt from Amazon:</p>
<blockquote><p>1.2 <strong>Using Your Files with the Service.</strong> You may use the Service only to store, retrieve, manage, and access Your Files for personal, non-commercial purposes using the features and functionality we make available. You may not use the Service to store, transfer or distribute content of or on behalf of third parties, to operate your own file storage application or service, to operate a photography business or other commercial service, or to resell any part of the Service. You are solely responsible for Your Files and for complying with all applicable copyright and other laws, including import and export control laws and regulations, and with the terms of any licenses or agreements to which you are bound. You must ensure that Your Files are free from any malware, viruses, Trojan horses, spyware, worms, or other malicious or harmful code.
<div style="text-align: right; width: 100%;"><cite>- <a href="http://www.amazon.com/gp/help/customer/display.html/?nodeId=201376540&ref_=cd_tou_fp&ref_=cd_pricing_tou" title="Amazon Cloud Drive Terms of Use">Amazon Cloud Drive Terms of Use</a>, Last updated March 25, 2015</cite></div>
</blockquote>
<p>It did get me wondering, though.  Decades ago the technology community created RAID storage: Redundant Array of Inexpensive Disks.  The concept is that if you copy your data across many different disks, you can survive the failure of one of those disks and rebuild the information from the remaining drives.  We also have virtual storage systems like <a href="http://irods.org/" title="iRODS (integrated Rule-Oriented Data System)">iRODS</a> and distributed file systems like <a href="http://research.google.com/archive/gfs.html" title="Google Research Publication: The Google File System">Google File System</a> and <a href="http://hortonworks.com/hadoop/hdfs/" title="Hadoop - HDFS Project Page">Apache Hadoop Distributed File System</a>.  I wonder what it would take to layer these concepts together to have a cloud-independent, cloud-redundant storage array for personal backups.  Sort of like a poor-man's RAID over Dropbox/Amazon/Microsoft/Google.  Something that would take care of the file verifications, the rebuilding from redundant copies, and the caching of content between services.  Even if we couldn't use it for our library services, it would be a darn good way to ensure the survivability of our cloud-stored files against the failure of a storage provider's business model.</p>
