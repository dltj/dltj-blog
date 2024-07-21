---
layout: wordpress-import
status: published
published: true
title: Getting Around Drupal's Prohibition of @ Characters in User Ids
modified: 2018-01-15T22:38:08-05:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 169
wordpress_url: http://dltj.org/2007/01/drupal-at-sign/
date: '2007-01-19 11:46:06 -0500'
date_gmt: '2007-01-19 16:46:06 -0500'
category: Raw Technology
categories:
- Raw Technology
tags:
- programming
- networking
- system administration
- Drupal
comments: []
---
A while back we created an LDAP directory to consolidate account information for various back-room services, and when we created it we decided to use the individual's e-mail address as the account identifier (`uid` in LDAP-speak).  It seemed like the logical thing to do -- it is something that the user knows and it is a cheap and easy way to assume that the account identifiers will be unique.  This is not uncommon for many internet services, of course.

Now we're bring up a [Drupal](http://drupal.org/) content management system and of course want to tie the authentication into the existing LDAP directory.  The initial configuration appeared to work, but there were odd, unexplained failures -- most notably, Drupal would not consider it a 'real' account because it didn't have an e-mail field.  Even weirder was the fact that we configured Drupal to know exactly which LDAP attribute to use as the e-mail address (`mail`, in LDAP-speak).  It wasn't until one of our system engineers wondered out loud if the at-sign ('@') in the user id wasn't causing problems that we started making progress towards a solution.

As it turns out, he was right.  Without spending so much time in the guts of the Drupal code to know exactly if this is true, it seems like Drupal wants to reserve the '`@something`' construct for inter-Drupal authentication.  In other words, if you have an account on one Drupal server (let's call it _DrupalA_) and want to access a second (let's call it _DrupalB_) &mdash; and if the two servers agree to share user accounts &mdash; the account from _DrupalA_ would be recorded in the database of _DrupalB_ as "`UserId@DrupalA`".

The 'at' symbol for us, though, is just a normal part of an e-mail address.  We really didn't want to reconstruct our LDAP account scheme, so the best choice seemed to be to find a way to trick Drupal into accepting these account identifiers.  This, unfortunately, was no easy task.  I couldn't find the root cause of the problem, but did diagnose enough of the symptoms to force a patch into the system.  The patch, in the form of a new module (code included below) forces the account to have two necessary attributes that seem to go missing whenever a '@' character appears in the user id.  If you have similar problems, I can't claim that this will work for you, nor can I guarantee this approach will be supportable in the future.  All's I know is that it seems to work for us in our situation right now.

{% highlight php %}
<?php

function olinkldap_help($section) {
  $output = '';
  switch ($section) {
    case 'admin/modules#olinkldap':
      $output = 'olinkldap;
      break;
    case 'admin/modules#description':
    case 'admin/help#olinkldap':
      $output = t('Sets up OhioLINK-specific LDAP parameters.');
      break;
  }
  return $output;
}

function olinkldap_settings() { }

function olinkldap_user($op, &$edit, &$user, $category = NULL) {
  switch($op) {
    case 'load':
      olinkldap_user_load($user);
      break;
  }
}

function olinkldap_user_load(&$user) {
  // Calculate the DN for the user -- you'll need to adjust this to match your LDAP base DN
  $ldap_dn=sprintf("uid=%s,ou=People,dc=somewhere,dc=outthere", $user->name);

  // Create a new array with the two LDAP-specific values that seem to be missing.
  $forced_data=array('ldap_authentified' => 1, 'ldap_dn' => $ldap_dn);

    // It seems like this should work, but it doesn't (it throws a segmentation fault)
    //  user_save($user_edit,array($forced_data);
    // so we're going to interact directly with the database
  if ($user->uid) {
    // Get the 'data' field for the user and put it in the $data array
    $data = unserialize(db_result(db_query('SELECT data FROM {users} WHERE uid = %d', $user->uid)));
    // Put all of the attributes from $forced_data into $data
    foreach ($forced_data as $key => $value) {
      $data[$key] = $value;
    }
    // Reserialize the $data array and update it in the database
    $v[] = serialize($data);
    db_query("UPDATE {users} SET data='%s' WHERE uid=%d",array_merge($v,array($user->uid)));
  }
}
?>
{% endhighlight %}

Save this as 'olinkldap.module', update the DN to reflect your LDAP server's base DN (see comment in code), copy it into your Drupal modules directory, and activate it.  Your '@'-impaired userids should start working again.  If you are using the inter-Drupal account sharing (we're not) this might break something for you.  That's not interesting for us, so I'm not testing it against that condition.  If you use this and find that it works or doesn't work, or you have a better way of solving the problem, please leave a comment or traceback...
