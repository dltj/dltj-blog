---
layout: wordpress-import
status: publish
published: true
title: 'OpenLDAP with a Go Daddy "Turbo SSL Secure Certificate"'
modified: 2006-09-09T02:16:23+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 113
wordpress_url: http://dltj.org/2006/09/openldap-with-intermediary-cert/
date: '2006-09-08 22:16:23 -0400'
date_gmt: '2006-09-09 03:16:23 -0400'
categories:
- Raw Technology
tags:
- Gentoo
- openldap
- Go Daddy
- ssl
- tls
comments:
- id: 4661
  author: HOWTO LDAPv3 - Gentoo Linux Wiki
  author_email: ''
  author_url: ''
  date: '2006-09-25 05:43:44 -0400'
  date_gmt: '2006-09-25 09:43:44 -0400'
  content: "<!--%kramer-ref-pre%-->[...] For help with intermediate/chained SSL certificates
    (e.g. Go Daddy's Turbo SSL certs), see OpenLDAP with a Go Daddy &ldquo;Turbo SSL
    Secure Certificate&rdquo; in Disruptive Library Technology Jester.  [edit] conf.d/slapd
    [...]<!--%kramer-ref-post%-->"
- id: 13505
  author: HOWTO OpenLDAP &mdash; OpenLab2 Wiki
  author_email: ''
  author_url: ''
  date: '2007-03-28 01:38:38 -0400'
  date_gmt: '2007-03-28 05:38:38 -0400'
  content: "<!--%kramer-ref-pre%-->[...] For help with intermediate/chained SSL certificates
    (e.g. Go Daddy's Turbo SSL certs), see OpenLDAP with a Go Daddy &ldquo;Turbo SSL
    Secure Certificate&rdquo; in Disruptive Library Technology Jester.  [muokkaa]
    Installing OpenLDAP [...]<!--%kramer-ref-post%-->"
- id: 19699
  author: Andrew
  author_email: admin@ruadmin.com
  author_url: http://www.ruadmin.com/
  date: '2007-07-31 07:01:58 -0400'
  date_gmt: '2007-07-31 11:01:58 -0400'
  content: "GoDaddy Turbo SSL working fine with Google Checkout\r\n\r\nhttp://groups.google.com/group/google-checkout-api-troubleshooting/browse_thread/thread/fde7e41b6f81a5a0/45e0ca41b7766dc9?lnk=gst&amp;q=GoDaddy&amp;rnum=2"
- id: 75604
  author: Sergio Gelato
  author_email: Sergio.Gelato@astro.su.se
  author_url: ''
  date: '2010-06-26 07:04:34 -0400'
  date_gmt: '2010-06-26 11:04:34 -0400'
  content: This didn't work for me (using OpenLDAP 2.4 built with GNUTLS). Instead,
    I found that I can make slapd serve the full certification chain simply by appending
    the intermediate and root CA certificates to the TLSCertificateFile. My understanding
    (backed by some testing) is that TLSCACertificateFile is only used by slapd in
    verifying client certificates, not in generating a server certificate chain to
    present to clients.
- id: 77005
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-07-06 09:34:11 -0400'
  date_gmt: '2010-07-06 13:34:11 -0400'
  content: I no longer have access to the system on which the configuration described
    above is being used, so I'll need to take your word for it.  Perhaps the behavior
    of TLSCACertificateFile changed over time (or a bug was fixed).  Thanks for reporting
    your findings here, Sergio.
- id: 92225
  author: Arthur Duarte
  author_email: arthurduarte@arthurduarte.com
  author_url: ''
  date: '2010-10-07 11:10:35 -0400'
  date_gmt: '2010-10-07 15:10:35 -0400'
  content: "hi \r\n\r\nI got a Wildcard Certificate from GoDaddy but when I try to
    apply it on the Slapd, I receive the following error:\r\n\r\nmain: TLS init def
    ctx failed: -69\r\n\r\nI've searched on the internet but doesn't seem to be a
    common error, cannot find a way to solve my problem.\r\n\r\nCould you help me
    out?\r\n\r\nThank You"
- id: 92231
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2010-10-07 12:34:56 -0400'
  date_gmt: '2010-10-07 16:34:56 -0400'
  content: Sorry, Arthur -- I don't know what would generate that error.  Good luck!
- id: 103943
  author: using a godaddy SSL cert with openLDAP - The FreeBSD Forums
  author_email: ''
  author_url: http://forums.freebsd.org/showthread.php?t=19673
  date: '2010-12-02 02:00:39 -0500'
  date_gmt: '2010-12-02 07:00:39 -0500'
  content: "<!--%kramer-ref-pre%-->[...] Open source LDAP server implementation  I
    was attempting to use this guide:  OpenLDAP with a Go Daddy &ldquo;Turbo SSL Secure
    Certificate&rdquo;  I have setup the certificate chain in my slapd.conf like so:
    \  [...]<!--%kramer-ref-post%-->"
- id: 660095
  author: Mantas
  author_email: grawity@gmail.com
  author_url: ''
  date: '2014-09-10 00:17:04 -0400'
  date_gmt: '2014-09-10 04:17:04 -0400'
  content: Given that you still update this post, perhaps remove the "+SSLv2" flag?
    At this point, v2 is worse than nothing.
- id: 660168
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2014-09-10 17:36:35 -0400'
  date_gmt: '2014-09-10 21:36:35 -0400'
  content: Thanks for noting that, Mantas.  I've updated the post to remove the +SSLv2
    flag.
---
<p>Okay -- this seemed like a lot harder than it should have been.  At the very least, it took piecing together information from a number of places in order to make it happen.  The goal is to use a Go Daddy <a href="https://www.godaddy.com/gdshop/ssl/turbo.asp?se=%2B&#038;app%5Fhdr=&#038;ci=1858">Turbo SSL Secure Certificate</a> (the $19.95/year one) to secure an OpenLDAP server.  On the surface, this shouldn't be so hard.  The tricky part comes because the requested SSL cert is not signed by a recognized Certificate Authority root; instead, Go Daddy uses an <em>intermediary certificate</em> and the tricky part is making sure the whole chain of SSL certificates line up properly.  There is a wealth of documentation for using intermediary certificates with web servers, but I found very little for OpenLDAP servers.  I hope by posting this into the blogosphere you will find it useful someday, too.</p>
<p><!--toc--></p>
<div style="border: 1px dashed black; padding: .75em; background: #EEE; color: black;"><img src="/images/note.png" alt="NOTE!" height="48" width="48" style="float:left;padding:0 .75em .5em 0" /><em>Updated on 10-Sep-2014.</em> Thanks to commenter Mantas for pointing out that this very old post recommended the use of insecure SSL ciphers.  "+SSLv2" was included in the <code> TLSCipherSuite</code> line of the slapd.conf file.  That part of the line has been removed.</p>
<p>Also note, I no longer endorse GoDaddy in light of the marketing and positions on internet policy.  These same instructions can be adapted to any SSL certificate provider.</p></div>
<h2>Environment</h2>
<p>The servers are running the <a href="http://www.gentoo.org/" title="Gentoo Linux -- Gentoo Linux News">Gentoo</a> distribution of Linux.  The critical bits out of portage are <span class="removed_link" title="http://gentoo-portage.com/net-nds/openldap">OpenLDAP</span> (version 2.3.24-r1), <span class="removed_link" title="http://gentoo-portage.com/dev-libs/openssl">OpenSSL</span> (version 0.9.8c), <span class="removed_link" title="http://gentoo-portage.com/sys-auth/nss_ldap">nss_ldap</span> (version 249), and <span class="removed_link" title="http://gentoo-portage.com/sys-auth/pam_ldap">pam_ldap</span> (version 180).  On Monday I'm going to ask OhioLINK's resident Redhat Fedora Core expert to try the equivalent on that distribution.  (I've put him through so much trouble already that I hope this process goes smoothly from here on out.)  You'll need to get all of those and their prerequisites installed and configured on your machine.  There is a <span class="removed_link" title="http://gentoo-wiki.com/HOWTO_LDAPv3">HOWTO LDAPv3 on the Gentoo Wiki</span> and <a href="http://wiki.debian.org/LDAP/OpenLDAPSetup" title="OpenLDAPSetup - Debian Wiki">another on the Debian Wiki</a> plus <span class="removed_link" title="http://www.saas.nsw.edu.au/solutions/ldap-auth-pam.html">numerous</span> <a href="http://www.howtoforge.com/linux_ldap_authentication" title="LDAP Authentication In Linux | HowtoForge - Linux Howtos and Tutorials">other</a> <a href="http://www.ofb.net/~jheiss/krbldap/howto.html" title="Replacing NIS with Kerberos and LDAP HOWTO">documents</a> out there to help you get started.  When you've had enough fun beating your head up against that wall and have got basic LDAP-based account management to work, you can come back here.</p>
<h2>The Certificate</h2>
<p>I picked the Go Daddy <a href="https://www.godaddy.com/gdshop/ssl/turbo.asp?se=%2B&#038;app%5Fhdr=&#038;ci=1858">Turbo SSL Secure Certificate</a> because, well, it's cheap.  As their own marketing literature says -- why pay a couple hundred dollars for something when Go Daddy will give you the equivalent thing for $19.95?  To be completely fair, Go Daddy offers two types of certificates:  the Turbo SSL one that we'll be using and the <a href="https://www.godaddy.com/gdshop/ssl/high.asp?se=%2B&#038;app%5Fhdr=&#038;ci=1859">High-Assurance Secure Certificate</a>.  The difference is in the verification process.  The former verifies only the domain name and control of that domain name by sending e-mail to the WHOIS administrative contact to confirm that the certificate request is legitimate.  The latter is a manual verification process that looks at the domain name and control of that domain name as well as verifies identity of requesting person or company and the authority to make request.  The latter is probably overkill for our uses and costs $89.99.</p>
<p>So go through the modestly convoluted process of generating the Certificate Signing Request (CSR), giving Go Daddy your $19.95, requesting the certificate, have the request approved by your DNS zone administrator, receive the e-mail of the signed certificate from Go Daddy, and then come back here.</p>
<h2>OpenLDAP's 'slapd.conf' Server Setup</h2>
<p>So here is the really tricky part (where "tricky" is defined as the piece that took me the longest to figure out).  As I said in the introduction, Go Daddy uses an intermediary certificate to form a chain from one of the highly-trusted root certificates.  The key to making this work becomes getting the intermediary certificate into the evaluation chain at the right time so the client can see it an trust the server.  It is possible to install the intermediary certificate on all of the clients who might someday make use of our server's certificate, but we would, ideally, like the server to offer the client the certificate and let the client do all of the cryptology to determine whether the server can be trusted.  This section describes what it takes to make that happen.</p>
<p>First, one has to go to the <a href="https://certificates.godaddy.com/Repository.go">Go Daddy Secure Certificate Services Repository</a>.  Many of the directions I found for getting the intermediary certificate working with web servers said to download the intermediate certificate alone (or, as Go Daddy calls it, the <code>sf_issuing.crt</code> file).  I found this didn't work &mdash; rather, the "Root Bundle" (or <code>ca_bundle.crt</code> file) is what is needed.</p>
<p>[Updated 20070904T1104 : It looks like Go Daddy changed their certificate chain last month.  What you need now is called "gd_bundle.crt" from the Go Daddy certificate repository -- you'll find it under the heading "New Go Daddy Certificate Chain" (at least that is where you'll find it today).]</p>
<p>Then add this to your <code>slapd.conf</code> file:</p>
{% highlight text %}
TLSCipherSuite HIGH:MEDIUM
# Your signed CSR that you got back from Go Daddy
TLSCertificateFile /etc/ssl/certs/ldap.ohiolink.crt
# The private key file for the certificate
TLSCertificateKeyFile /etc/ssl/certs/ldap.ohiolink.key
# The "Root Bundle" file from Go Daddy's Certificates Repository
TLSCACertificateFile /etc/ssl/certs/ca_bundle.crt
{% endhighlight %}
<p>Next, move onto the client side.  (Your LDAP server also has the client libraries installed -- you'll likely want to start there.)</p>
<h2>OpenLDAP's 'ldap.conf' Client Setup</h2>
<p>In case you haven't discovered it by now, there are two &mdash; count 'em, <em>two</em> &mdash; <code>ldap.conf</code> files on your box.  One is read by tools derived from the OpenLDAP package and the other is for the pam_ldap/nss_ldap combination.  And to make things even more interesting -- the syntax of the files are not the same!  Boy, sometimes I really dislike the profession I'm in...</p>
<p>So let's start with OpenLDAP's <code>ldap.conf</code> file; you'll likely find this in the <code>/etc/openldap</code> directory.  (At least that is where you'll find it with Gentoo -- YMMV.)  In that file, you'll want to put these pieces:</p>
{% highlight text %}
BASE            dc=ohiolink,dc=edu
URI             ldap://ldap.ohiolink.edu/
TLS_CACERTDIR   /etc/ssl/certs
TLS_REQCERT     demand
{% endhighlight %}
<p>You'll, of course, want to replace the BASE and URI parameters with the ones most appropriate for your installation.  I've found that third line to be somewhat unexpectedly important, however.  The OpenLDAP libraries need to know where to go to find the trusted root certificates, and so you need to specify the path where they exist on your system.  These got installed with OpenSSL, which you needed back in "The Certificate" stage when you generated the CSR.  Again, these are in <code>/etc/ssl/certs</code> on a typically-configured Gentoo box; you might find them elsewhere in other distributions.</p>
<h2>NSS/PAM's 'ldap.conf' Client Setup</h2>
<p>This is the <em>other</em> <code>ldap.conf</code> file, and on a Gentoo system you're likely to find it in the <code>/etc</code> directory.  Remember &mdash; the file name is the same but the directives are different.  You'll use much of the knowledge from the previous section here...you'll just need to change the preceding labels:</p>
{% highlight text %}
suffix "dc=ohiolink,dc=edu"
uri ldap://ldap.ohiolink.edu
sslpath /etc/ssl/certs
ssl start_tls
{% endhighlight %}
<p>See the similarity?  <code>base</code> becomes <code>suffix</code>, <code>tls_cacertdir</code> becomes <code>sslpath</code>, and so forth.  There will likely be much more in this file -- <code>pam_login_attribute</code>, <code>nss_base_passwd</code>, and more.  Follow a more comprehensive set of directions to get those pieces right.</p>
<h2>Testing</h2>
<p>To test to see if the SSL certificate is really securing the connection, you can use the <code>-ZZ</code> parameter (to force an SSL/TLS interaction with the server) on <code>ldapsearch</code> with the debugging level set in order to see some of the protocol interaction.  I find that this command is most instructive:</p>
{% highlight bash %}
ldapsearch -d 9 -ZZ -h ...ldap.server.address.net...
{% endhighlight %}
<p>You can scroll back and make sure that the SSL/TLS-secured connection was, in fact being used.  You can also turn up debugging on the server and look at the server log files to verify the same thing.</p>
<h2>Conclusion</h2>
<p>So there you go.  I hope you find this useful.  I also hope that if you find it in error, you'll let me know.  (Although, at the moment, this does seem to be working for us.  Perhaps it only works because I have faith that it will work.  If so, please be gentle when you tell me I've made an error...  :-) )</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://gentoo-wiki.com/HOWTO_LDAPv3 on January 19th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;">The text was modified to update a link from http://wiki.debian.org/OpenLDAPSetup to http://wiki.debian.org/LDAP/OpenLDAPSetup on January 19th, 2011.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://www.saas.nsw.edu.au/solutions/ldap-auth-pam.html on August 27th, 2012.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://gentoo-portage.com/net-nds/openldap on August 22nd, 2013.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://gentoo-portage.com/dev-libs/openssl on August 22nd, 2013.</p>
<p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://gentoo-portage.com/sys-auth/nss_ldap on August 22nd, 2013.</p>
<p><</p>
<p>p style="padding:0;margin:0;font-style:italic;" class="removed_link">The text was modified to remove a link to http://gentoo-portage.com/sys-auth/pam_ldap on August 22nd, 2013.</p>
