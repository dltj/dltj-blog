---
layout: wordpress-import
status: publish
published: true
title: 'Separating Configuration from Code in CollectionSpace'
modified: 2015-12-01T01:58:14+00:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 26878
wordpress_url: http://dltj.org/?p=26878
date: '2015-11-30 20:58:14 -0500'
date_gmt: '2015-12-01 01:58:14 -0500'
categories:
- Raw Technology
tags:
- git
- CollectionSpace
- Ansible
- Configuration management
comments:
- id: 682985
  author: Mitch
  author_email: mitch.saba@uconn.edu
  author_url: ''
  date: '2015-12-04 11:43:53 -0500'
  date_gmt: '2015-12-04 16:43:53 -0500'
  content: Thanks for a great article.  I was recently introduced to CollectionSpace
    and this has given me a better understanding of what I am dealing with.
- id: 683264
  author: Peter Murray
  author_email: jester@dltj.org
  author_url: http://dltj.org/about
  date: '2015-12-06 17:31:21 -0500'
  date_gmt: '2015-12-06 22:31:21 -0500'
  content: You're welcome, Mitch.  Glad to cross paths with you again.  Hope to hear
    you on the CSpace Talk list soon...
---
<p>For the past few months I've been working on a project to migrate a museum's collection registry to CollectionSpace.  CollectionSpace is a "free, open-source, web-based software application for the description, management, and dissemination of museum collections information." ((From the <a href="http://www.collectionspace.org/faq/#what" title="FAQ | CollectionSpace">answer to the first question</a> of the CollectionSpace frequently asked questions.))  CollectionSpace is multitenant software -- one installation of the software can serve many tenants.  The software package's structure, though, means that the configuration for one tenant is mixed in with the code for all tenants on the server (e.g, the <a href="https://github.com/collectionspace/application/tree/master/tomcat-main/src/main/resources/tenants">application layer</a>, <a href="https://github.com/collectionspace/services/tree/master/services/common/src/main/cspace/config/services/tenants/">services layer</a>, and <a href="https://github.com/collectionspace/ui/tree/master/src/main/webapp/tenants">user interface layer</a> configuration are stored deep in the source code tree).  This bothers me from a maintainability standpoint.  Sure, Git's richly featured merge functionality helps, but it seems unnecessarily complex to intertwine the two in this way.  So I developed a structure that puts a tenant's configuration in a separate source code repository and a series of procedures to bring the two together at application-build time.<br />
<!--more--><br />
[caption id="attachment_26879" align="alignright" width="249"]<img src="/wp-content/uploads/2015/11/cspace-tenant-directory-structure.png" alt="CollectionSpace Tenant Configuration Structure" width="249" height="146" class="size-full wp-image-26879" /> CollectionSpace Tenant Configuration Structure[/caption]There are three main parts to a CollectionSpace installation: the application layer, the services layer, and the user interface layer.  Each of these has configuration information that is specific to a tenant.  The idea is to move the configuration from these three layers into one place, then use Ansible to enforce the placement of references from the tenant's configuration directory to the three locations in the code.  That way the configuration can be changed independent of the code.</p>
<p>The configuration consists of a file and three directories.  Putting the reference to the file -- <code>application-tenant.xml</code> -- into the proper place in the source code directory structure is straightforward:  we use a <a href="http://www.linfo.org/hard_link.html" title="What is a hard link? -- definition by The Linux Information Project (LINFO)">file system hard link</a>.  By their nature, though, We cannot use a hard link to put a reference to a directory in another place in the file system.  We can use a <a href="https://askubuntu.com/questions/108771/what-is-the-difference-between-a-hard-link-and-a-symbolic-link">soft link</a>, but those were problematic in my specific case because I was using '<a href="https://www.cis.upenn.edu/~bcpierce/unison/">unison</a>' to synchronize the contents of the tenant configuation between my local filesystem and a <a href="https://www.vagrantup.com/">Vagrant</a> virtual system.  (Unison had this annoying tendency to delete the directory and recreate it in some synchronization circumstances.)  So I resorted to a <a href="https://unix.stackexchange.com/questions/198590/what-is-a-bind-mount">bind mount</a> to make the configuration directories appear inside the code directories.</p>
<p>To make sure this setup is consistent, I use <a href="http://www.ansible.com/" title="Ansible is Simple IT Automation">Ansible</a> to describe the exact state of references.  Each time the Ansible playbook runs, it ensures that everything is set the way it needs to be before the application is rebuilt.  That Ansible script looks like this:</p>
<p><script src="https://gist.github.com/dltj/ed71a79f5174581ee185.js"></script></p>
<p>Some annotations:</p>
<ul>
<li><a href="https://gist.github.com/dltj/ed71a79f5174581ee185#file-playbook_cspace_deploy_tenant-yml-L12-L18">Lines 12-18</a> create the hard link for the tenant application XML file.</li>
<li>Handling the tenant configuration directories takes three steps.  Using the application configuration as an example, <a href="https://gist.github.com/dltj/ed71a79f5174581ee185#file-playbook_cspace_deploy_tenant-yml-L20-L24">lines 20-24</a> first make sure that a directory exists where we want to put the configuration into the code directory.</li>
<li>Next, <a href="https://gist.github.com/dltj/ed71a79f5174581ee185#file-playbook_cspace_deploy_tenant-yml-L26-L34">lines 26-34</a> uses <code>mount --bind</code> to make the application configuration appear to be inside the code directory.</li>
<li>Lastly, <a href="https://gist.github.com/dltj/ed71a79f5174581ee185#file-playbook_cspace_deploy_tenant-yml-L36-L41">lines 35-41</a> ensures the mount-bind lasts through system rebuilds (although <a href="https://gist.github.com/dltj/ed71a79f5174581ee185#file-playbook_cspace_deploy_tenant-yml-L33">line 33</a> makes sure the mount-bind is working each time the playbook is run).</li>
</ul>
<p>Then the typical CollectionSpace application build process runs.</p>
<ul>
<li><a href="https://gist.github.com/dltj/ed71a79f5174581ee185#file-playbook_cspace_deploy_tenant-yml-L89-L120">Lines 89-120</a> stop the Tomcat container and rebuilds the application, services, and user interface parts of the system.</li>
<li><a href="https://gist.github.com/dltj/ed71a79f5174581ee185#file-playbook_cspace_deploy_tenant-yml-L122-L133">Lines 122-133</a> start Tomcat and waits until it is responding.</li>
<li><a href="https://gist.github.com/dltj/ed71a79f5174581ee185#file-playbook_cspace_deploy_tenant-yml-L135-L163">Lines 135-163</a> log into CollectionSpace, gets the session cookie, then initializes the user interface and the vocabularies/authorities.</li>
</ul>
<p>I run this playbook almost every time I make a change to the CollectionSpace configuration.  (The exception is for simple changes to the user interface; sometimes I'll just log into the server and run those manually.)  If you want to see what the directory structure looks like in practice, the <a href="https://github.com/cherryhill/sdmom-tenant-config">configuration directory is on GitHub</a>.</p>
