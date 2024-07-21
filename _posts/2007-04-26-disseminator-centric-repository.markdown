---
layout: wordpress-import
status: publish
published: true
title: Disseminators As the Core of an Object Repository
modified: 2018-01-15T22:38:08-05:00
author: Peter Murray
author_login: lyrdor
author_email: jester@dltj.org
author_url: http://dltj.org/about
wordpress_id: 215
wordpress_url: http://dltj.org/2007/04/disseminator-centric-repository/
date: '2007-04-26 09:58:32 -0400'
date_gmt: '2007-04-26 13:58:32 -0400'
categories:
- DRC
- Fedora
tags:
- seam
- DRC
- restlet
- java
- digital libraries
- asset actions
- Fedora Repository
comments: []
---
I've been working to get JBoss Seam tied into [Fedora](http://www.fedora.info/), and along the way thought it would be wise to stop and document a core concept of this integration: the centrality of [Fedora Disseminators](http://www.fedora.info/download/2.2/userdocs/digitalobjects/objectModel.html#DISS) in the the design of the [Ohio Digital Resource Commons](http://info.drc.ohiolink.edu/). Although there is nothing specific to [JBoss Seam (a Java Enterprise Edition application framework)](http://www.jboss.com/products/seam) in these concepts, making an object "render itself" does make the Seam-based interface application easier to code and understand. A disseminator-centric architecture also allows us to put our code investment where it matters the most — in the repository framework — and exploit that investment in many places. So what does it mean to have a disseminator-centric architecture and have objects "render themselves"?

## How It Works
{% include figure image_path="/wp-content/uploads/2007/04/sequence.png" caption="Sequence Diagram" %}{: .align-right}

This is a sequence diagram showing all of the pieces:

  * Browser: The user's browser
  * DRCseam: A JBoss Seam application that generates the user interface and performs much of the business logic. DRCseam, however, does **not**render the objects or their metadata into browser-consumable artifacts. Read on!
  * Fedora: A basic Fedora digital object repository.
  * Disseminator: A simple servlet that performs various transformations on object datastreams to render content usable by the browser.

With these components in play, here is the description of a sequence to render a page showing the metadata for a repository item:

  1. request item page: The browser follows a link to an item detail page.
  2. API-A ObjectProfile: The interface application asks the repository for the 'Object Profile' of the item...
  3. return object profile: ...which the repository returns. The interface application now knows basic details about the object: that it exists, the creation and updated timestamps, and so forth.
  4. API-A DatastreamDissemination for fullDisplay: The interface application needs the object's metadata display, so it asks the object to "render itself" by making a call to the Fedora repository for the object's "FullDisplay" disseminator.
  5. call getFullDisplay: The Fedora repository in turn calls the object's disseminator with the Persistent Identifier (PID) of the object as a parameter.
  6. API-A Datastream for metadata: Using the object PID, the disseminator calls back to the Fedora repository for the descriptive metadata datastream (the DC datastream, in this case)...
  7. XML metadata: ...which the Fedora repository returns.
  8. transform metadata: The disseminator performs some transformation or derivation on the descriptive datastream to create an XHTML representation...
  9. XHTML fragment: ...which it returns to the Fedora software...
  10. XHTML fragment: ...which is returned to the interface application...
  11. XHTML page: ...which inserts it at the appropriate place in the XHTML page it has built and returns the XHTML page to the browser.

Step #4 is where we diverge from previous architectures. Instead of making the interface application transform the metadata into a human-readable format, the interface application calls the object's disseminator to do the job.

### The Heart of It All: The Disseminator

The key to this architecture is _asking the object to "render itself"_. This puts the task of creating the appropriate representation at the object level. The object can be an image, a video, a spreadsheet, or a PDF file. More importantly, the object can be a PDF of a journal article or a PDF of a thesis; in both cases the metadata describing that PDF file will be different (journal/volume/issue in one case and department/degree/advisor in the other).

Rather than putting special case code in the interface application to render the description of the journal article one way and the thesis another way, that special case code is bound to the object in the form of a "disseminator". The disseminator methods for the journal article and the thesis share the same name — `getFullDisplay` — but will return entirely different XHTML fragments — one for a journal article and one for a thesis. For both objects, though, the interface application will make a call to the object in the Fedora repository asking for the output of each `getFullDisplay` dissemination. In the case of a Dublin Core description, the dissemination output could look like this:

{% highlight html %}
<table class="drc_dublinCore_table">
<tr class="drc_dublinCore_row drc_dublinCore_title">
<td class="drc_dublinCore_label drc_dublinCore_title">Title:</td>
<td class="drc_dublinCore_value drc_dublinCore_title">Jester Example</td>
</tr>

<tr class="drc_dublinCore_row drc_dublinCore_identifier">
<td class="drc_dublinCore_label drc_dublinCore_identifier">Identifier:</td>
<td class="drc_dublinCore_value drc_dublinCore_identifier">demo:exampleObject</td>
</tr>
</table>
{% endhighlight %}

You'll note that there is a liberal application of CSS styles on all of the XHTML elements, allowing for the look of the dissemination to be further transformed in the browser via CSS stylesheets. A `getFullDisplay` dissemination for a journal article could look like this:

{% highlight html %}
<table class="drc_ejc_table">
<tr class="drc_ejc_row drc_ejc_title">
<td class="drc_ejc_label drc_ejc_title">Article Title:</td>
<td class="drc_ejc_value drc_ejc_title">Taking Advantage of Fedora Disseminations</td>
</tr>

<tr class="drc_ejc_row drc_ejc_volume">
<td class="drc_ejc_label drc_ejc_volume">Volume:</td>
<td class="drc_ejc_value drc_ejc_volume">3</td>
</tr>

<tr class="drc_ejc_row drc_ejc_issue">
<td class="drc_ejc_label drc_ejc_issue">Issue:</td>
<td class="drc_ejc_value drc_ejc_issue">2</td>
</tr>
</table>
{% endhighlight %}

### Looking at the Pieces

There is a demonstration system set up for a short period of time that shows all of the pieces. First, the disseminator:

  * http://drc-dev.ohiolink.edu:8080/BaseDisseminator/getFullDisplay/demo:exampleObject

Next, how this disseminator looks as accessed through the Fedora repository:

  * http://drc-dev.ohiolink.edu:8080/fedora/get/demo:exampleObject/demo:bDefExample/getFullDisplay/

And finally, how this result looks through the Seam-based interface application. (A note about this application — only this URL works at the moment even though there are other links on the page. This is also the 'trunk' version of our interface code, so it is likely to change and/or break and/or work better at any time.)

  * http://drc-dev.ohiolink.edu:8080/drc/item.seam?itemId=demo%3AexampleObject

## Fedora Setup

In addition to the Seam-based interface application and the disseminator code, there is setup required at the Fedora repository — specifically, the creation of a Behavior Definition (bDef) that describes the disseminators that the objects share in common and the creation of a Behavior Mechanism (bMech) that describes the implementation of that definition for a particular object type. Below is a series of screen shots that show the steps to create the bDef and bMech.

### Disseminator Behavior Definition (bDef)

Using the Fedora Admin client, under the "Builders" menu, select "Behavior Definition Builder". The first pane, "General" parameters, use a specific PID of '`demo:bDefExample`' and put something in for the Behavior Object Name, Behavior Object Description, and one of the Dublin Core Metadata fields. (It doesn't matter what you put in for these values.)

{% include figure image_path="/wp-content/uploads/2007/04/bdbgeneral.png" caption="Fedora Admin Behavior Definition Builder &ldquo;General&rdquo; pane" alt="Fedora Admin Behavior Definition Builder &ldquo;General&rdquo; pane" %}{: .align-center}

Under the "Abstract Methods" pane, create new definitions for each of the disseminator methods

{% include figure image_path="/wp-content/uploads/2007/04/bdbabstractmethods.png" caption="Fedora Admin Behavior Definition Builder &ldquo;Abstract Methods&rdquo; pane" alt="Fedora Admin Behavior Definition Builder &ldquo;Abstract Methods&rdquo; pane" %}{: .align-center}

Under the "Documentation" pane, put something in the first entry.  Again, it doesn't matter what is put in for these values, but they are required.

{% include figure image_path="/wp-content/uploads/2007/04/bdbdocumentation.png" caption="Fedora Admin Behavior Definition Builder &ldquo;Documentation&rdquo; pane" alt="Fedora Admin Behavior Definition Builder &ldquo;Documentation&rdquo; pane" %}{: .align-center}

Select "Ingest" at the bottom of the window, and the `demo:bDefExample` bDef will be created. Alternatively, you could import the `demo:bDefExample` saved in the DRC source code repository (choose "original format" at the bottom of that page).

### Disseminator Mechanism Definition (bMech)

The bMech is a little more complicated. Under the "Builders" menu, select "Behavior Mechanism Builder". The first pane, "General" parameters, use a specific PID of '`demo:bMechExample`' and put something in for the Behavior Object Name, Behavior Object Description, and one of the Dublin Core Metadata fields. (It doesn't matter what you put in for these values.) In the "Behavior Definition Contract" pick the bDef just created (`demo:bDefExample`).

{% include figure image_path="/wp-content/uploads/2007/04/bmbgeneral.png" caption="Fedora Admin Behavior Mechanism Builder &ldquo;General&rdquo; pane" alt="Fedora Admin Behavior Mechanism Builder &ldquo;General&rdquo; pane" %}{: .align-center}

In the "Service Profile" pane, put in values in the "General" area (it doesn't matter what). In the Service Binding area, make sure the Message Protocol is HTTP GET, put in text/html, text/xml for Input MIME Types and put in text/html, text/xml, text/plain for Output MIME Types.

{% include figure image_path="/wp-content/uploads/2007/04/bmbserviceprofile.png" caption="Fedora Admin Behavior Mechanism Builder &ldquo;Service Profile&rdquo; pane" alt="Fedora Admin Behavior Mechanism Builder &ldquo;Service Profile&rdquo; pane" %}{: .align-center}

Under the Service Methods pane, put in `http://localhost:8080/BaseDisseminator` for the Base URL.  (The disseminator is also loaded in the same servlet as the Fedora repository and the Seam interface application, and it is loaded at the "/BaseDisseminator" context path in the servlet.)  Create Service Method Definitions that correspond to the Abstract Methods in the bDef.

{% include figure image_path="/wp-content/uploads/2007/04/bmbservicemethods.png" caption="Fedora Admin Behavior Mechanism Builder &ldquo;Service Methods&rdquo; pane" alt="Fedora Admin Behavior Mechanism Builder &ldquo;Service Methods&rdquo; pane" %}{: .align-center}

Select "Properties" for each one of the Service Method Definitions in turn.  "echo" is a unique disseminator method that simply echos back the context parameters of the disseminator request.  This is useful for seeing exactly what the Fedora server is going to give to the disseminator.

{% include figure image_path="/wp-content/uploads/2007/04/bmbservicemethods-echo.png" caption="Fedora Admin Behavior Mechanism Builder &ldquo;Service Methods&rdquo; Definitions for &ldquo;echo&rdquo; Method" alt="Fedora Admin Behavior Mechanism Builder &ldquo;Service Methods&rdquo; Definitions for &ldquo;echo&rdquo; Method"  %}{: .align-center}

With the exception of "echo" all of the other Service Method Definitions are the same.  The Method Binding consists of the disseminator method followed by a slash and the PID placeholder followed by a question mark and 'dc' equals the DC placeholder.  Since the Method Binding field has two placeholders, there are two entries in the Method Parameter Definitions area.  The first is for PID &mdash; a "Default" parameter that is required and passed by value to the disseminator.  The default value is the special value `$PID`, which the repository software will replace with the PID of the object as the disseminator is called.  The second is for DC, a "Datastream" parameter that is required and passed to the disseminator by URL reference.  The disseminator doesn't actually use this reference to a datastream, but it is a requirement that all bMechs pass a datastream of one sort or another to the disseminator.

{% include figure image_path="/wp-content/uploads/2007/04/bmbservicemethods-getfulldisplay.png" caption="Fedora Admin Behavior Mechanism Builder &ldquo;Service Methods&rdquo; Definitions for &ldquo;getFullDisplay&rdquo; Method" alt="Fedora Admin Behavior Mechanism Builder &ldquo;Service Methods&rdquo; Definitions for &ldquo;getFullDisplay&rdquo; Method" %}{: .align-center}

If you have followed all of the steps so far, under the "Datastream Input" pane there will be one entry for DC in the table.  The only thing that needs to be done here is adding "text/xml" in the MIMEType column.

{% include figure image_path="/wp-content/uploads/2007/04/bmbdatastreaminput.png" caption="Fedora Admin Behavior Mechanism Builder &ldquo;Datastream Input&rdquo; pane" alt="Fedora Admin Behavior Mechanism Builder &ldquo;Datastream Input&rdquo; pane" %}{: .align-center}

Under the "Documentation" pane, put something in the first entry.  Again, it doesn't matter what is put in for these values, but they are required.
{% include figure image_path="/wp-content/uploads/2007/04/bmbdocumentation.png" caption="Fedora Admin Behavior Mechanism Builder &ldquo;Documentation&rdquo; pane" alt="Fedora Admin Behavior Mechanism Builder &ldquo;Documentation&rdquo; pane" %}{: .align-center}
  
Select "Ingest" at the bottom of the window, and the `demo:bMechExample`bMech will be created. Alternatively, you could import the `demo:bMechExample` saved in the DRC source code repository (choose "original format" at the bottom of that page).

### Sample Object

The last step is to add this disseminator bDef/bMech combination to an object. Edit any object in the repository and go to the "Disseminators" pane. If there are other disseminators already defined for this object, select "New" along the left side. Put in a label — any label will do. Next to "Behavior defined by..." select `demo:bDefExample`. Then next to "Mechanism" select `demo:bMechExample`. The admin client will prompt for a DC binding; select "Add" and choose the DC datastream in the pop-up window.

{% include figure image_path="/wp-content/uploads/2007/04/objectdisseminatorsdatastream.png" caption="Fedora Admin Sample Object&rsquo;s &ldquo;Disseminators&rdquo; pane in progress" alt="Fedora Admin Sample Object&rsquo;s &ldquo;Disseminators&rdquo; pane in progress" %}{: .align-center}

Select "Save Changes" at the bottom.  The completed disseminator looks like this:

{% include figure image_path="/wp-content/uploads/2007/04/objectdisseminators.png" caption="Fedora Admin Sample Object&rsquo;s &ldquo;Disseminators&rdquo; pane completed" alt="Fedora Admin Sample Object&rsquo;s &ldquo;Disseminators&rdquo; pane completed" %}{: .align-center}

There is a sample object in the DRC source code repository that has the disseminator already defined.

## Notes

Comments about this architecture are certainly welcome. I'm sure I'll be writing about it more in the future, but here are some thoughts at this point:

### Future Directions

In this case, I'm using an XSLT stylesheet to transform the Dublin Core XML into an XHTML table. That stylesheet is stored in the BaseDisseminator WAR file. The stylesheet could just as easily be a datastream of a special "formatting" object in the repository. One of the key distinctions of OhioLINK's Fedora implementation is that institutions using the repository will be able to "brand" their content in any way they choose. Having the flexibility of storing metadata transformations just like any other object in the repository would seem to be of great advantage in that scenario.

On a related front, this style of implementation would be greatly enhanced by the work of the Fedora [Content Model Dissemination Architecture](http://www.cs.cornell.edu/payette/fedora/designs/cmda/) (CMDA). Because disseminators must be bound to specific objects rather than classes of objects, management of the variety of bMechs in a scenario such as this will likely become difficult very soon. I'm heartened by the fact that the CMDA work is going on and will cut our management complexity dramatically when it becomes available.

### Acknowlegements

These concepts are based in part on the work of the Digital Library Federation's [Aquifer Asset Actions](https://wiki.dlib.indiana.edu/display/DLFAquifer/Asset+Action+Project) technical working group and discussions among members of the OAI [Object Reuse and Exchange](http://www.openarchives.org/ore/) technical committee as well as conversations with many Fedora developers and implementors. Thanks, everyone.

[Update 20070426T1147 : Fixed the sample object URL. Thanks, Jodi.]

The text was modified to remove a link to http://drc-dev.ohiolink.edu/browser/BaseDisseminator/trunk/resources/foxml/demo_exampleObject.xml?rev=774 on January 13th, 2011.

The text was modified to remove a link to http://drc-dev.ohiolink.edu/browser/BaseDisseminator/trunk/resources/foxml/demo_bMechExample.xml?rev=774 on January 13th, 2011.

The text was modified to remove a link to http://drc-dev.ohiolink.edu/browser/BaseDisseminator/trunk/resources/foxml/demo_bDefExample.xml?rev=774 on January 13th, 2011.

The text was modified to remove a link to http://drc-dev.ohiolink.edu:8080/drc/item.seam?itemId=demo%3AexampleObject on January 13th, 2011.

The text was modified to remove a link to http://drc-dev.ohiolink.edu:8080/fedora/get/demo:exampleObject/demo:bDefExample/getFullDisplay/ on January 13th, 2011.

The text was modified to remove a link to http://drc-dev.ohiolink.edu:8080/BaseDisseminator/getFullDisplay/demo:exampleObject on January 13th, 2011.

The text was modified to update a link from http://rama.grainger.uiuc.edu/assetActions/ to https://wiki.dlib.indiana.edu/display/DLFAquifer/Asset+Action+Project on January 19th, 2011.

  


