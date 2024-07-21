---
title: 'The ILS without patron data: a thought experiment realized with FOLIO'
modified: 2024-06-21T20:09:40-04:00
categories:
- L/IS Profession
tags:
- integrated library system
- privacy
- FOLIO
---

In the [previous blog post](https://dltj.org/article/ils-without-patron-data/), I outlined the concept of a library system with no personally identifiable information as a way to safeguard a patron's right to privacy. 
Library systems commonly retain traces of a patron's library activity, and the librarian ethos protects a patron's privacy as they conduct their research and borrow items from the library. 
Suppose our library systems decoupled patrons' personal information from their library activity. 
In that case, the risk of leaked information from the library systems is significantly reduced.

In this blog post, I examine how a modern library service platform could be modified to handle this minimal personal knowledge system. 
As you may recall, this proposed system uses pairwise-subject-identifiers ("pairwise-id") from an organization's identity provider ("IdP") to identify people. 
Our service provider ("SP") uses that identifier internally and calls external services that can find out who the pairwise-id is when necessary. 
I'm using the library services platform with which I'm most familiar: FOLIO. 
As an open-source library services platform, FOLIO offers a relatively straightforward path for such customizations. 
In the following sections, I'll examine what our library system SP needs to do when encountering a new pairwise-id for the first time, how to send patron notices and bill patrons, and changes to the hold-request subsystem. 
I'll also discuss some changes that are needed to FOLIO itself. 
For the sake of brevity, I'm calling this FOLIO version "FILP" — the FOLIO Identity Limited Platform.

## A New Pairwise-ID is seen at FOLIO login
{: #pairwise-login}
{% include image.html 
float="right"
width="400"
src="2024/2024-06-21-folio-saml-config.png"
caption="The FOLIO Settings → Tenant → SSO settings pane"
alt="Screen capture of the SSO settings pane. It contains four fields: Identity Provider URL, SAML binding, SAML attribute, and User property. There is also a button labeled 'Download metadata'"
%}FOLIO includes a {% include robustlink.html href="https://s3.amazonaws.com/foliodocs/api/mod-login-saml/p/saml-login.html" versionurl="https://web.archive.org/web/20240621221856/https://s3.amazonaws.com/foliodocs/api/mod-login-saml/p/saml-login.html" versiondate="2024-06-21" title="SAML Login (v1) | FOLIO API" anchor="SAML SP endpoint" %} that assumes user records have already been loaded into the system. 
Configuring this endpoint requires naming the SAML attribute that will contain the person's unique identifier and which field of the FOLIO user record has that identifier. 
In this example, the FOLIO SP is looking for the user identifier in the `uid` SAML attribute from the IdP and will search the contents of the `External System ID` field in the user record.

In our FILP version, we could use the SAML module unmodified; we would need to pre-load user records with the pairwise-id in the `External System ID` field. FOLIO user records have four required fields: patron group, active/inactive status, email address, and last name. 
The pre-loaded data would include the patron group appropriate for the pairwise-id patron and an "active" status. 
The pairwise-id is also copied into the email address field; I'll describe later in this post how the pairwise-id is used in the FILP version of the email module. 
In the last name field, we can put the three-random-word phrase that will be used for hold-pickup notices. 
(More on this in the holds section below.)

Our FILP SAML login module can also create user records on-the-fly when a new pairwise-id is seen. 
The IdP sends attributes (such as "student" or "faculty") to the FILP SP that are needed to determine the appropriate patron group; the settings for the SAML module would contain a table that maps those attributes to patron groups. 
The pairwise-id is copied to the email address field, and a random last name will also be recorded in the new user record.

## New Email Delivery Module
{: #email-module}
FOLIO has a built-in email module with a {% include robustlink.html href="https://s3.amazonaws.com/foliodocs/api/mod-email/p/email.html" versionurl="https://web.archive.org/web/20240621222741/https://s3.amazonaws.com/foliodocs/api/mod-email/p/email.html" versiondate="2024-06-21" title="Email API (v2.0) | FOLIO API" anchor="simple API for outbound email" %}. 
Other FOLIO modules send a POST to the `/email` endpoint with a {% include robustlink.html href="https://github.com/folio-org/mod-email/blob/master/ramls/email_entity.json" versionurl="https://web.archive.org/web/20240621222919/https://github.com/folio-org/mod-email/blob/master/ramls/email_entity.json" versiondate="2024-06-21" title="email_entity.json" anchor="JSON body that contains the email details" %}, including the `to` address and the `body` of the message. 
The built-in email module has configuration settings for the SMTP server, and it takes responsibility for sending the message.

Our FILP version of the email module has the same API signature as the built-in module: it listens for POST requests to the `/email` endpoint and accepts an identical JSON body. 
It is a drop-end replacement; the other modules in the FOLIO system don't know that they are communicating with a FILP-enabled email module. 

Remember from the previous post that the IT group running the IdP will need new services that act on behalf of our library system in cases where a patron's identity must be known. 
One such service sends an email to a pairwise-id (say, the "IdP Pairwise Email Service"). 
This service takes the pairwise-id and looks up the actual email address. 
Also remember that we copied the pairwise-id to the email address in the user record. 
Our FILP email module reads the JSON body to get the pairwise-id in the 'to' field, then sends it and the message contents to the IdP Pairwise Email Service. 
The IdP Pairwise Email Service returns a success or failure message, which our FILP email module records in its database.

## New Fee-Fine Module
{: #feefine-module}
Like the FOLIO email notification module, there is a {% include robustlink.html href="https://s3.amazonaws.com/foliodocs/api/mod-feesfines/r/feefines.html" versionurl="https://web.archive.org/web/20240621223053/https://s3.amazonaws.com/foliodocs/api/mod-feesfines/r/feefines.html" versiondate="2024-06-21" title="Feefines version v1 | FOLIO API" anchor="single point" %} that FILP will need to override to send fee/fine information to an external agent. 
Also, similar to the email module, the IT group running the IdP will need an IdP Pairwise Billing Service. 
When that service is given a pairwise-id, a charge/credit amount, and a message, it will post a transaction against the patron's organization account. 
FOLIO's existing fee-fines module has a POST method to create a new fee and a PUT method to modify an existing fee. 
The FILP version of the fee-fine module is a drop-in replacement for those `/feefines` and `/feefines/{feefineId}` API endpoints, and it accepts the same JSON bodies as those endpoints. 
The `ownerId` field in the JSON body is the FOLIO user record identifier, and our FILP feefine module uses that identifier to look up the pairwise-id in the user record to forward the data to the IdP Pairwise Billing Service.

## No changes to the Requests module
{: #requests-module}
The third example from the previous blog post of the impact of our FILP minimal-personal-knowledge library system was item request pickup slips. 
For context, the typical hold-paging-request workflow is for the library to print a paging slip that contains the title, author, and shelving location of the requested item along with the patron's name and contact information. 
The pickup slip is attached to the book and placed on a hold shelf for the patron to pick up. 
In this typical workflow, the patron's name is intimately tied to the requested material.

Instead of printing the patron's name, we use a random three-word phrase stored in the FOLIO user record's `last name` field when the record was created. 
That random phrase is printed on the pull slip. 
When FOLIO sends a hold pickup notice to the patron, the {% raw %}`{{user.lastName}}`{% endraw %} replacement token is available to insert in the body of the message:

> The item you requested, _{% raw %}`{{item.title}}`{% endraw %}_, is now ready for pickup at the main library hold shelves. Items on the pickup shelves are sorted alphabetically using a three-word phrase. Your three-word phrase is _{% raw %}`{{user.lastName}}`{% endraw %}_.

## Changes Required within FOLIO
{: #user-scoped-apis}
An important point in this description of how the pairwise-id is used in FOLIO is that the patron is the one logging into FOLIO to perform these actions. 
Currently, FOLIO performs circulation operations like a typical integrated library system: to check out an item to a patron, a staff member logs into FOLIO with privileges to perform the checkout function. 
That checkout function allows staff members (with the required permissions) to check out any item to any user record. 

~~In our FILP FOLIO, though, the staff member won't be able to scan a patron's barcode to identify the patron...the patron will need to log in through the IdP single sign-on system so the pairwise-id is transmitted to FOLIO.~~ There is a [correction in the next blog post](https://dltj.org/article/ils-without-patron-data-details/#staff-checkout-correction) about how it is possible to use the existing Check-out app.
Since it is the patron that is logged into FOLIO at this point, we will need a new API endpoint for a function that checks out an item _only to the logged-in user record_ (rather than any user record).

FOLIO differs from previous library systems in that patrons are "first class" users. 
The only thing that differentiates a library staff member's account is the permissions on their user record. 
As described above, an access service staff member will have permission to use the Checkout app to register a loaned item on any user record. 
A patron user will need a permissions set that allows access only to their user record. 
Several other endpoints will need similar modifications: an endpoint that records a hold request for the logged-in user, an endpoint that allows someone to set notification and pickup preferences for themself, an endpoint that requests a renewal for a checked-out item, and so forth.

## Conclusion and the Way Forward
{: #call-to-action}
FILP, as described above, still has some potential ways to correlate library activity to a specific patron and possibly de-anonymize that person. 
This blog post is already nearly 2,000 words, so I put [that discussion plus a few other open questions](https://dltj.org/article/ils-without-patron-data-details/) in the next post.

FOLIO's architecture is excellent because it is _almost possible_ to build the FOLIO Identity Limited Platform—FILP—today. 
Replace a few back-end modules and add API endpoints where capabilities are scoped to an individual user record, and we're pretty much there. 
This article's subtitle is _"a thought experiment realized in FOLIO"._ 
It is almost enough for a statement of work.

I'll add a plug for the company that I work for here in the last paragraph. 
If your library would like to do this with FOLIO, {% include robustlink.html href="https://www.indexdata.com/" versionurl="https://web.archive.org/web/20240618210912/https://www.indexdata.com/" versiondate="2024-06-18" title="Index Data homepage" anchor="Index Data" %} specializes in this type of software development. 
Few things would please me more than having the chance to build this into FOLIO. 
Contact me if you want to discuss this further or enter into a development agreement to add this capability to the FOLIO open source codebase.