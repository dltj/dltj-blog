---
title: 'The ILS without patron data: a thought experiment'
categories:
- L/IS Profession
tags:
- integrated library system
- privacy
---
Library systems hold significant information about patrons, including their search and reading histories. 
For librarians, ensuring the privacy and confidentiality of this data is an essential component of professional ethics. 
In the United States, for example, the third point in the {% include robustlink.html href="https://www.ala.org/tools/ethics" versionurl="https://web.archive.org/web/20240611061632/https://www.ala.org/tools/ethics" versiondate="2024-06-20" title="ALA Code of Ethics | American Library Association" anchor="American Library Association Code of Ethics" %}  is _"We protect each library user's right to privacy and confidentiality with respect to information sought or received and resources consulted, borrowed, acquired or transmitted."_

To understand this better, consider how the {% include robustlink.html href="https://en.wikipedia.org/wiki/Video_Privacy_Protection_Act" versionurl="https://en.wikipedia.org/w/index.php?title=Video_Privacy_Protection_Act&oldid=1221687857" versiondate="2024-06-20" title="Video Privacy Protection Act | Wikipedia" anchor="Video Privacy Protection Act of 1988" %} arose in the U.S. after the controversy surrounding the publication of Robert Bork's video rental history. 
A year earlier, Robert Bork was nominated to the U.S. Supreme Court. 
In the course of his confirmation hearing, a reporter published Bork's video rental history. 
Although this list of videos were not a factor in his rejected nomination, that the list was published was found to be outrageous enough spur Congress to pass the law. 
Similarly, if your library records were made public, it could well be embarrassing and intrusive. 
(Side note: While there is no federal protection for personal library records like those for video rental records, {% include robustlink.html href="https://www.ala.org/advocacy/privacy/statelaws" versionurl="https://web.archive.org/web/20240409035540/https://www.ala.org/advocacy/privacy/statelaws" versiondate="2024-06-20" title="State Privacy Laws Regarding Library Records | American Library Association" anchor="state laws offer a patchwork of protections" %}.)

Library systems, like the video rental systems of old, tie personally identifiable details with patron activity. 
So, what if we could separate these details? 
Before we delve into this, let's define some terms related to Federated Identity systems. 
Skip these sections if you know about Federated Identity systems. 

## Federated Identity Systems: Identity Providers and Service Providers
In our complex world, library services often come from multiple providers. 
Rather than have the hassle of separate logins and passwords, it is common for these providers to call back to a central service where a people can prove they are who they say they are. 
The place where people log in called an Identity Provider (IdP). 
The place where people want to go is called a Service Provider (SP). 
A Federated Identity System is a trust relationship and a set of agreements/technologies that enable the sharing of identity information and authorizations across systems. 
It allows people to access resources and services across different systems using a single set of credentials, typically managed by their Identity Provider. 
(IdPs are sometimes called Assertion Parties because these are the software systems in the trust relationship that assertions about who a user is; SPs are sometimes called Relying Parties because they are trusting the IdP's assertions.) 
Federated Identity systems exchange attributes about someone. 
Those attributes can be specific to a person, like "name" and "email address", or general categories, like "student" or "community-member". 
Attributes can also have special meanings to the IdP and SP, like Pairwise-Subject-ID.

## Pairwise Subject Identifier
An identifier that is specific to a user is called a "subject identifier". 
These typically look somewhat like an email address with parts specific to both the user and the organization. 
For example: `murraype@dltj.org` — `murraype` is specific to me and `dltj.org` gives the identifier context to my organization. 
In a Federated Identity system, the same subject identifier is given to every SP that asks for it.

However, if we don't want multiple SPs correlating a user's activities, we can use a "pairwise-subject-identifier". 
Within this workflow, the IdP sends different identifiers to different SPs for the same person, making the identifiers unique to each IdP-SP pair. 
More {% include robustlink.html href="https://docs.oasis-open.org/security/saml-subject-id-attr/v1.0/cs01/saml-subject-id-attr-v1.0-cs01.html#_Toc536097230" versionurl="https://web.archive.org/web/20230624171232/https://docs.oasis-open.org/security/saml-subject-id-attr/v1.0/cs01/saml-subject-id-attr-v1.0-cs01.html#_Toc536097230" versiondate="2024-06-20" title="SAML V2.0 Subject Identifier Attributes Profile Version 1.0 | OASIS" anchor="formally" %}, pairwise-subject-identifier ("pairwise-id") is defined this way:

> This is a long-lived, non-reassignable, uni-directional identifier suitable for use as a unique external key specific to a particular relying party. Its value for a given subject depends upon the relying party to whom it is given, thus preventing unrelated systems from using it as a basis for correlation. 

Typically opaque, these identifiers don't offer additional information to the SPs trying to correlate activities between users. 
For instance, the pairwise-id between IdP-SP#1 is `uGDJVRxK48E@dltj.org` and the pairwise-id between IdP-SP#2 is `T6vNM9v5tUna@dltj.org`. 
Not only are the two Service Providers (SPs) unable to determine if the identifiers belong to the same person, but the identifiers themselves also lack any inherent information that would allow the SPs to ascertain the individual's identity.

## Pairwise-ID as _THE_ library system ID
In our ideal library system aiming to minimize personal data collection, the pairwise-id becomes the unique identifier in the library system. 
(There are some drawbacks to using the pairwise-id as the unique identifier...[see the discussion](https://dltj.org/article/ils-without-patron-data-details/#deanonymization) in the third post of this series.) 
The first time the library system's SP gets a new pairwise-id, it creates a new user record in the system. 
The system uses other attributes from the IdP to determine privileges for this new record - for instance, a "student" status gets a normal loan period, a "faculty" status gets an extended loan period, and a "conference visitor" status gets blocked from borrowing.

The library SP is trusting the attributes received by the IdP—see the discussion above about the trust relationship for the assertions—so it does not need prior knowledge about the patron. 
So other than knowing that the person is a specific individual with a recognized status in the organization, the library system knows nothing about the patron. 
If the patron's borrowing and search history are leaked from the library system, the system's leaked records has nothing else to offer to tie those to a person. 
(Again, there are de-anonymizing nuances, but for later discussion.)

## ...but I need to send overdue notices to the patron
Let's consider some operational aspects that usually require personal data: sending overdue notices, applying fees to a patron, and handling patron requests. 
The library system knows enough about its patron community to check out books to authorized users—people with attributes coming from the IdP that we trust and use to set how long the loan needs to be. 
What if a user keeps a book too long...we need a way to send a notice to a person to return the book and to bill them when they don't return it. 
But the only thing the library system has is an opaque identifier that only has meaning at the IdP.

Library systems are typically self-contained: they send their own email messages and have their own billing systems for keeping track of patron charges. 
In a library system without patron data, though, we need to rely on others with more information about the person to handle those tasks.

Let's take the example of sending notices to the patron. 
Rather than the library system doing sending the notice itself, our system tells another system to do it. 
The group that runs the IdP has a service that, when given a pairwise-id and the content of a message, will send that message to the patron for us. 

Another example: billing the patron when they say they've lost the item or the library declares it missing. 
The IdP group has another service that takes in the pairwise-id, a currency amount, and a description then adds that information to the person's central account. 
The library keeps track of the fact that a pairwise-id has been billed, but it never knows the person behind that identifier. 
If the item turns up again, our library system reverses the charge: it sends the pairwise-id, a credit amount, and a credit description. 

Library patrons also request items be held for them; what do we do in this case? 
When someone requests an item, the library system prints a "paging slip" that is used to get the item from the shelf. 
The paging slip has information about the item—its title, author, and shelving location—as well as information about the person who requested it. 
The paging slip usually turns into the hold pick-up slip; it is taped to the outside of the book and shelved alphabetically by the patron's last name. 
There is a serious privacy downside to this workflow, though: everyone from the staff member pulling the item to the other users browsing the hold-pickup shelf can see the name of the person who asked for it. 
Instead, our library-system-with-no-names prints a random three-word phrase to stand in for the name of the person who asked for the item. 
This same three-word phrase is sent in the hold-pickup message to the library patron so they can find the item on the hold-pickup shelf. 

## But could we build it?
While this thought experiment is theoretical, could a real-world library system actually function this way? 
In the [next post](https://dltj.org/article/ils-without-patron-data-folio/), we'll explore possible adaptations for the FOLIO Library Services Platform to turn theory into practice.