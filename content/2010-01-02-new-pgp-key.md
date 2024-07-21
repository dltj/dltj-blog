---
status: publish
published: true
title: 'A New Year, a New PGP Key'
modified: 2020-10-13T09:47:19-04:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 1406
wordpress_url: http://dltj.org/?p=1406
date: '2010-01-02 21:16:30 -0500'
date_gmt: '2010-01-03 02:16:30 -0500'
categories:
- Raw Technology
tags:
- email
- pgp
- gnupg
- security
comments:
- id: 648324
  author: Password managers - Rubber Duck
  author_email: ''
  author_url: http://www.rubberduckdistillery.com/blog/2013/04/26/password-managers/
  date: '2013-08-08 08:22:45 -0400'
  date_gmt: '2013-08-08 12:22:45 -0400'
  content: "<!--%kramer-ref-pre%-->[...] to delve more into how and why you should
    use PGP, good citizen Peter E. Murray wrote an articulate post about it on his
    blog. In the above case, I am only using PGP for encryption, Peter talks about
    [...]<!--%kramer-ref-post%-->"
---
It is the start of a new year ((Some have even said it is the start of a new decade, but of course that isn't true.  We won't start a new decade until 2011, just like we didn't actually start a new millennium until 2001.)), and it seems like a good time to update my public encryption key.  My previous one -- created in 2004 -- is both a little weaker, cryptographically speaking, than the ones newly created (1024-bit versus 2048-bit) and also an uncomfortable mixing of my professional and personal lives.  For my previous key, I attached all of my professional and personal user ids (e.g. e-mail addresses) to the same [key](http://pgp.mit.edu:11371/pks/lookup?op=vindex&search=0xE3EB78A927CF2072).  This time I decided to split my work-related user ids from my other ones.  My reasoning for the split is that I might be compelled by my employer to turn over my private key to decrypt messages and files sent in the course of my work.  If my personal user ids are also attached to that private key, my employer (and who ever else got ahold of that key), would be able to decrypt my personal messages and files as well.  That is not necessarily a good thing.  So my solution was to create two keys and cross-sign them.  I've outlined the process below.

These keys are part of a computer standard and software algorithm called "[Pretty Good Privacy](http://en.wikipedia.org/wiki/Pretty_Good_Privacy)", or PGP.  If you are interested in more of a background about PGP, see a companion post on [why I digitally sign my e-mail](/article/pgp-email/).

## The Two New Keys
Here are details of my two new keys:

* Peter Murray -- Professional
    _Key ID_: `2048D/877838CF`
    _Fingerprint_: `B021 8300 6844 E459 A18E 83CF 4C7A 6A28 8778 38CF`)
    _Created:_ 2-Jan-2010; _Expires:_ 5-Feb-2015
    [Public keys](http://pgpkeys.mit.edu:11371/pks/lookup?op=vindex&search=0x4C7A6A28877838CF) as known by keyserver pgp.mit.edu ([ASCII-armored version](http://pgpkeys.mit.edu:11371/pks/lookup?op=get&search=0x4C7A6A28877838CF))
* Peter Murray -- Personal
    _Key ID_: `2048D/4637F6A1`
    _Fingerprint_: `5781 5786 7D66 D33B 0F54 D9DE 5820 0CEE 4637 F6A1`)
    _Created:_ 2-Jan-2010; _Expires:_ 5-Feb-2015
    [Public key](http://pgpkeys.mit.edu:11371/pks/lookup?op=vindex&search=0x58200CEE4637F6A1) as known by keyserver pgp.mit.edu ([ASCII-armored version](http://pgpkeys.mit.edu:11371/pks/lookup?op=get&search=0x58200CEE4637F6A1))

The _key id_ is a short identifier for the PGP key, and it is broken up into two parts separated by a slash. The first part -- "2048D" -- says that this is a 2048-bit DSA signing key. The second part -- "877838CF" -- is the last eight hexadecimal digits of the key fingerprint. Taken together, these two pieces of the key id almost assuredly identify the key. It is a short form, though -- the full identifier is the key fingerprint: 40 hexadecimal digits. Embedded in the key are creation and expiration dates. The expiration date can be changed later, and can be eliminated, too (e.g. set to not expire). There doesn't seem to be much in the way of guidance on how long to set the expiration date, but five years out seems to be a good round number. 

## Key Creation / Cross-signing Process

It took some thought to put together a sequence of commands that executed this creation and cross-signing/identity-splitting process. I'm including the process below in case I need to remember how to do this five years from now with these new keys expire. I'm using [GnuPG](http://www.gnupg.org/) 2.0.13 on a Mac at the command line. My answers to the prompts are bolded. There are graphical user interfaces for the Mac, PC, and Linux desktops that do the same thing as well.

### Generating the New Key

This is using the built-in key generation process in GnuPG. In the comment field of the user ID, I'm noting that this is my _professional_ key and that it supersedes my previous key (known as 0x27cf2072 -- and yes, I now realize that I misspelled "supersedes" in a comment of my key, and it is now there forever). I'm also stating that it will be valid until 2015 (62 months). I'm only showing the process of creating my professional key; the process was nearly identical for my personal key (0x4637f6a1).

```
$ gpg --gen-key
gpg (GnuPG) 2.0.13; Copyright (C) 2009 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 2
DSA keys may be between 1024 and 3072 bits long.
What keysize do you want? (2048) 2048
Requested keysize is 2048 bits
Please specify how long the key should be valid.
         0 = key does not expire
        = key expires in n days
      w = key expires in n weeks
      m = key expires in n months
      y = key expires in n years
Key is valid for? (0) 62m
Key expires at Thu Feb  5 13:42:53 2015 EST
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: Peter E. Murray
Email address: peter@OhioLINK.edu
Comment: Professional -- supercedes 0x27cf2072
You selected this USER-ID:
    "Peter E. Murray (Professional -- supercedes 0x27cf2072) "

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
You need a Passphrase to protect your secret key.

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: WARNING: some OpenPGP programs can't handle a DSA key with this digest size
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key 877838CF marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   2  signed:  10  trust: 0-, 0q, 0n, 0m, 0f, 2u
gpg: depth: 1  valid:  10  signed:   2  trust: 0-, 1q, 0n, 4m, 5f, 0u
gpg: depth: 2  valid:   1  signed:   0  trust: 0-, 1q, 0n, 0m, 0f, 0u
gpg: next trustdb check due at 2011-03-13
pub   2048D/877838CF 2010-01-02 [expires: 2015-02-05]
      Key fingerprint = B021 8300 6844 E459 A18E  83CF 4C7A 6A28 8778 38CF
uid                  Peter E. Murray (Professional -- supercedes 0x27cf2072) sub   2048g/96854A46 2010-01-02 [expires: 2015-02-05]
```

### Add Other Elements to the New Key

To this basic key, I'm going to add other elements: a second user id (my e-mail account at Wright State University) and a picture. I'm also going to set my OhioLINK e-mail address as the primary user id.

```
$ gpg --edit-key 877838cf
gpg (GnuPG) 2.0.13; Copyright (C) 2009 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Secret key is available.

pub  2048D/877838CF  created: 2010-01-02  expires: 2015-02-05  usage: SC  
                  trust: ultimate      validity: ultimate
sub  2048g/96854A46  created: 2010-01-02  expires: 2015-02-05  usage: E   
[ultimate] (1). Peter E. Murray (Professional -- supercedes 0x27cf2072)

Command> adduid
Real name: Peter E. Murray
Email address: peter.murray@wright.edu
Comment:
You selected this USER-ID:
 "Peter E. Murray "

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o

pub  2048D/877838CF  created: 2010-01-02  expires: 2015-02-05  usage: SC  
                  trust: ultimate      validity: ultimate
sub  2048g/96854A46  created: 2010-01-02  expires: 2015-02-05  usage: E   
[ultimate] (1)  Peter E. Murray (Professional -- supercedes 0x27cf2072) [ unknown] (2). Peter E. Murray

Command> addphoto

Pick an image to use for your photo ID.  The image must be a JPEG file.
Remember that the image is stored within your public key.  If you use a
very large picture, your key will become very large as well!
Keeping the image close to 240x288 is a good size to use.

Enter JPEG filename for photo ID: ~/pmurray.jpg
Is this photo correct (y/N/q)? y

pub  2048D/877838CF  created: 2010-01-02  expires: 2015-02-05  usage: SC  
                  trust: ultimate      validity: ultimate
sub  2048g/96854A46  created: 2010-01-02  expires: 2015-02-05  usage: E   
[ultimate] (1)  Peter E. Murray (Professional -- supercedes 0x27cf2072) [ unknown] (2). Peter E. Murray [ unknown] (3)  [jpeg image of size 4916]

Command> 1

pub  2048D/877838CF  created: 2010-01-02  expires: 2015-02-05  usage: SC  
                  trust: ultimate      validity: ultimate
sub  2048g/96854A46  created: 2010-01-02  expires: 2015-02-05  usage: E   
[ultimate] (1)* Peter E. Murray (Professional -- supercedes 0x27cf2072) [ unknown] (2). Peter E. Murray [ unknown] (3)  [jpeg image of size 4916]

Command> primary

pub  2048D/877838CF  created: 2010-01-02  expires: 2015-02-05  usage: SC  
                  trust: ultimate      validity: ultimate
sub  2048g/96854A46  created: 2010-01-02  expires: 2015-02-05  usage: E   
[ultimate] (1)* Peter E. Murray (Professional -- supercedes 0x27cf2072) [ unknown] (2)  Peter E. Murray [ unknown] (3)  [jpeg image of size 4916]

Command> save
```

### Generate a Revocation Certificate

The [GnuPG handbook](http://www.gnupg.org/gph/en/manual.html) recommends creating a "Revocation Certificate" -- and for good reason. If you ever lose access to the private key (forget the password, or someone figures out the password and changes it to something you don't know), you can use this file to declare that the public key is invalid. I'm printing this out and putting it in my fireproof safe; I can rekey it and upload it to a public keyserver if I ever need to.

```
$ gpg --output 0x877838cf-revoke.asc --gen-revoke 0x877838cf

sec  2048D/877838CF 2010-01-02 Peter E. Murray (Professional -- supercedes 0x27cf2072)

Create a revocation certificate for this key? (y/N) yes
Please select the reason for the revocation:
  0 = No reason specified
  1 = Key has been compromised
  2 = Key is superseded
  3 = Key is no longer used
  Q = Cancel
(Probably you want to select 1 here)
Your decision? 1
Enter an optional description; end it with an empty line:
> Revocation cert created at the time of key generation.
>
Reason for revocation: Key has been compromised
Revocation cert created at the time of key generation.
Is this okay? (y/N) y

You need a passphrase to unlock the secret key for
user: "Peter E. Murray (Professional -- supercedes 0x27cf2072) "
2048-bit DSA key, ID 877838CF, created 2010-01-02

ASCII armored output forced.
Revocation certificate created.

Please move it to a medium which you can hide away; if Mallory gets
access to this certificate he can use it to make your key unusable.
It is smart to print this certificate and store it away, just in case
your media become unreadable.  But have some caution:  The print system of
your machine might store the data and make it available to others!
```
### Cross-signing Keys

Next I'm going to have each of the keys sign each other. I have three keys -- my old one (0x27cf2072), my new professional one (0x877838cf), and my new personal one (0x4637f6a1). The entire process will take six signatures; I'm only showing one below (signing 0x877838cf with 0x27cf2072. 

The command is "tnrsign", which stands for a trusted, no-revokable signature. The "trusted" part is a little technical, but it basically means that the signed key can trust the signatures of the signing key. In a practical sense, it means that in my local web-of-trust database, I will continue to trust the keys of people I've signed with my old key. (The GnuPG-Users list has a [more in-depth discussion](http://lists.gnupg.org/pipermail/gnupg-users/2005-May/025612.html) of the meaning of trusted signatures.) The "non-revokable" part means, of course, that this signature -- this "validation" if you will -- cannot be reversed at a later time. In this context, that makes since because I control both ends -- the signed key and the signing key.

```
$ gpg --local-user 0x27cf2072 --edit-key 877838cf tnrsign
gpg (GnuPG) 2.0.13; Copyright (C) 2009 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Secret key is available.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   3  signed:  10  trust: 0-, 0q, 0n, 0m, 0f, 3u
gpg: depth: 1  valid:  10  signed:   2  trust: 0-, 1q, 0n, 4m, 5f, 0u
gpg: depth: 2  valid:   1  signed:   0  trust: 0-, 1q, 0n, 0m, 0f, 0u
gpg: next trustdb check due at 2011-03-13
pub  2048D/877838CF  created: 2010-01-02  expires: 2015-02-05  usage: SC  
                     trust: ultimate      validity: ultimate
sub  2048g/96854A46  created: 2010-01-02  expires: 2015-02-05  usage: E   
[ultimate] (1). Peter E. Murray (Professional -- supercedes 0x27cf2072) [ultimate] (2)  Peter E. Murray [ultimate] (3)  [jpeg image of size 4916]

Really sign all user IDs? (y/N) yes

pub  2048D/877838CF  created: 2010-01-02  expires: 2015-02-05  usage: SC  
                     trust: ultimate      validity: ultimate
Primary key fingerprint: B021 8300 6844 E459 A18E  83CF 4C7A 6A28 8778 38CF

     Peter E. Murray (Professional -- supercedes 0x27cf2072)      Peter E. Murray      [jpeg image of size 4916]

This key is due to expire on 2015-02-05.
Please decide how far you trust this user to correctly verify other users' keys
(by looking at passports, checking fingerprints from different sources, etc.)

  1 = I trust marginally
  2 = I trust fully

Your selection? 2

Please enter the depth of this trust signature.
A depth greater than 1 allows the key you are signing to make
trust signatures on your behalf.

Your selection? 2

Please enter a domain to restrict this signature, or enter for none.

Your selection?

Are you sure that you want to sign this key with your
key "Peter E. Murray " (27CF2072)

The signature will be marked as non-revocable.

Really sign? (y/N) y

You need a passphrase to unlock the secret key for
user: "Peter E. Murray "
1024-bit DSA key, ID 27CF2072, created 2004-09-15

Command> save

This command is repeated for the other five combinations of old-new and new-new keys.
```
### Create ASCII-Armored Exports of the New Public Keys

The last step is to create export files of the new public keys so they can be uploaded to a public keyserver. In my case, I pasted the contents of the file into the form on the [MIT PGP keyserver](http://pgpkeys.mit.edu:11371/). PGP keys are binary by nature, so the "ASCII-Armored" process turns it into a text file that can be safely transported across a variety of systems. (You can also identify such files because they begin with a characteristic "`-----BEGIN PGP PUBLIC KEY BLOCK-----`" line.)

```
$ gpg --armor --output 877838cf.asc --export 877838cf
```