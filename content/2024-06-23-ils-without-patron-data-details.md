---
title: The ILS without patron data: open questions
modified: 2024-06-24T07:50:37-04:00
categories:
- L/IS Profession
tags:
- integrated library system
- privacy
- FOLIO
---
In my prior two posts, I outlined a strategy to minimize personally identifiable information in library automation systems ([idea overview](https://dltj.org/article/ils-without-patron-data/), [impact on FOLIO](https://dltj.org/article/ils-without-patron-data-folio/)). This approach uses a unique single-service identifier (the "pairwise-id") recognized exclusively by the identity provider (IdP) and the library's service provider (SP), effectively preventing any cross-system correlation of an individual's activities. The only personal information the library system stores is the pairwise-id, meaning that there are no exposed names, addresses, phone numbers, or other demographic details in the event of a system breach. When the library system needs to notify the user or post a charge to the user's account, it invokes the "IdP Pairwise Email Service" and the "IdP Pairwise Billing Service."

You might ask why we're going to these lengths. Why put in the work to create these extra email and billing services? The goal is simple: to make potential attacks less fruitful. By limiting the storage of personal information and narrowing the APIs that access it, we create fewer avenues for potential exposure. This approach frees resources to focus on the remaining sections, like the IdP, Pairwise Email Service, and Pairwise Billing Service, which access personal information.

This approach also strengthens the privacy of the remaining library workflows. For example, access services staff members only see the pairwise-ids, not the patrons' actual names or other personal details, as they check-in items or process hold requests. Of course, there may be circumstances when library staff need access to a patron's personal information. To accommodate such cases, we could add a new FOLIO app that retrieves these details for authorized personnel. Any such access would be recorded and subject to auditing to prevent misuse.

In this post, I'm finishing up this series (for the time being?) with a collection of additional details and open questions - starting with a correction.


## Correction: Library Staff Check-out app
{: #staff-checkout-correction}
I added a correction to the previous post about implementing a patron-data-minimizing library service in FOLIO. In the section about checking out a book, I mentioned that the only way for a user to check out an item was for the user to log into the library system via the IdP. Also, I said that existing functions could not be utilized, such as when a library staff member with appropriate permissions uses the Check-out app to register an item loaned to a patron by scanning the patron's ID card barcode.

My colleague Mike Taylor pointed out that this was incorrect. In my own mind, I had taken the minimal patron record one step too far. We can indeed use the barcode field in the user record; this barcode could either be from a pre-loaded patron record or supplied by the IdP as an attribute when the patron logs in for the first time. Once the barcode is in place, the existing Check-out app can function as it currently does. Nevertheless, libraries must be mindful of potential risks as barcodes are visually accessible and not as easily changed as passwords.


## Securing Circulation Station
{: #securing-circ}
Related the Check-out app, we need a strategy to control where check-outs can occur. If a patron is logging into FOLIO to use the Check-out app, we'll ideally want this process confined to the library building. A potential solution might involve using client HTTPS certificates; with this method, FOLIO would only provide access to the Check-out app if the user's browser presents a client certificate installed exclusively on the circulation stations. {% include robustlink.html href="https://www.keycloak.org/" versionurl="https://web.archive.org/web/20240621190803/https://www.keycloak.org/" versiondate="2024-06-23" title="Keycloak homepage" anchor="Keycloak" %} could be beneficial in this regard. In EBSCO's presentations about Keycloak replacing the original authentication mechanism, location-based login was highlighted as an advantage.


## Deanonymization
{: #deanonymization}
While these modifications have minimized personal data in the library system, we haven't completely eliminated it. A patron's activity itself — the stream of topics browsed, articles downloaded, and items borrowed — can act as a fingerprint of their interests. The elements of this fingerprint can be quite distinctive when considering their content, time-of-day, and location. With sufficient data, an intruder could potentially link the activity back to the individual behind the pairwise-id.

There are strategies to mitigate the risk of accumulating patron activity. For example, the IdP could generate a fresh pairwise-id for each login by the patron. In this scenario, the IdP would need to maintain a record of all pairwise-ids, and would likely want to implement automatic user provisioning (where the library system SP automatically generates a new user record for every new pairwise-id). 

This approach presents new challenges, such patron blocks that rely on the maximum number of checked-out items or the maximum amount of fees levied on a patron. Since the patron's activities are now scattered across multiple user records in FOLIO, we need to introduce a "Pairwise Block Check Service." This service would take a pairwise-id, track down all other pairwise-ids tied to the same patron, and tally their total loans and library fees. It would return a yes or no answer on whether the circulation transaction can proceed.

{% include robustlink.html href="https://scholar.google.com/scholar?hl=en&as_sdt=0%2C36&q=deanonymization+in+public+and+academic+libraries" versionurl="https://web.archive.org/web/20240624023736/https://scholar.google.com/scholar?hl=en&as_sdt=0%2C36&q=deanonymization+in+public+and+academic+libraries" versiondate="2024-06-23" title="deanonymization in public and academic libraries | Google Scholar" anchor="Deanonymization is a topic where a lot of research is ongoing" %}. We would want to engage these researchers to make sure our approach of limiting the correlation of patron activity is sound.


## Discovery integration
{: #discovery}
FOLIO doesn't come with a built-in discovery layer. This was an intentional design decision, aimed at defining clear boundaries that allow for the integration of a library's preferred discovery layer using well-defined,and versioned APIs. As it stands, all known discovery layer integrations connect to FOLIO using a central account with permissions to access all users' circulation records. These records are fetched using a patron identifier, such as the pairwise-id. However, this method makes the discovery layer's FOLIO user account as a potential security vulnerability.

Ideally, we would want each patron to log into FOLIO using their own account. Doing so would naturally restrict each user's visibility to their personal record. At the moment, I'm uncertain whether such an indirect (transitive) login setup is feasible. In other words, can a patron log into their chosen discovery layer via the IdP, and could the discovery layer then use this authentication to log into FOLIO?


## All Done?
{: #conclusion}
So, I think that is it...I've gotten all the parts of this idea rolling around in my head out into the world. Thanks for the discussions on Mastodon and elsewhere about the specifics, and I'm looking forward to hearing more thoughts and, if necessary, integrating them into a fourth blog post.

I feel compelled to express gratitude for having a system like {% include robustlink.html href="https://folio.org/" versionurl="https://web.archive.org/web/20240602084150/https://folio.org/" versiondate="2024-06-23" title="FOLIO homepage" anchor="FOLIO" %} to explore this idea in a tangible way. FOLIO's primary emphasis on an API-first approach makes this concept feel more feasible. When I say API-first, I mean there are no hidden APIs within FOLIO: for every task that can be performed in the user interface, a well-defined, versioned API exists to facilitate the same function. Beyond the user interface, the modules within FOLIO are compartmentalized by function and communicate with each other using the same well-defined, versioned APIs. As a result, replacing a module to adapt FOLIO for unique uses is entirely viable.