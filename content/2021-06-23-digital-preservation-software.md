---
title: 'Digital Repository Software: How Far Have We Come? How Far Do We Have to Go?'
modified: 2021-06-23T21:15:50-04:00
category: Raw Technology
categories:
  - Unified Content Repository
tags:
  - Fedora
  - standards
  - preservation
  - web architecture
  - html
  - http
  - static website
---

{{ robustlink(href="https://twitter.com/bryjbrown/status/1407336107159822341", versionurl="1", versiondate="2021-06-23", anchor="Bryan Brown's tweet") }} led me to {{ robustlink(href="https://ruthtillman.com/post/repository-ouroboros/", versionurl="/", versiondate="2021-06-23", anchor="Ruth Kitchin Tillman's <i>Repository Ouroboros</i> post") }} about the treadmill of software development/deployment.
And wow do I have thoughts and feelings.
{{ image(float="right", width="242", abssrc="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Serpiente_alquimica.jpg/242px-Serpiente_alquimica.jpg", caption="Ouroboros: an ancient symbol depicting a serpent or dragon eating its own tail. Or—in this context—constantly chasing what you can never have. Source: <a href='https://en.wikipedia.org/wiki/Ouroboros'>Wikipedia</a>", alt="Featuring an ouroboros, a snake or dragon biting its own tail, a digital representation of a copy of a 1478 drawing by Theodoros Pelecanos of an alchemical tract attributed to Synesius.") }}

Let's start with feelings.
I feel pain and misery in reading Ruth's post.
As Bryan said in a subsequent tweet, I've been on both sides: a system maintainer watching much-needed features put off to major software updates (or rewrites) and the person participating in decisions to put off feature development in favor of major updates and rewrites.
It is a bit like a serpent chasing its tail (a reference to "Ouroboros" in Ruth's post title)—as someone who just wants a workable, running system, it seems like a never-ending quest to get what my users need.

I think it will get better.
I offer as evidence the fact that almost all of us can assume network connectivity.
That certainly wasn't always the case: routers used to break, file servers crash would under stress, network drivers go out of date at inopportune times.
Now we take network connectivity for granted—almost (_almost!_) as if it a utility as common as water and electricity.
We no longer have to chase our tail to assume those things.

When we make those assumptions, we push that technology down the stack and layer on new things.
Only after electricity is reliable can we layer on network connectivity.
With reliable network connectivity, we layer on—say—digital repositories.
Each layer goes through its own refinement process...getting better and better as it relies on the layers below it.

Are digital repositories as reliable as printed books?
No way! 
Without electricity and network connectivity, we can't have digital repositories but we can still use books.
Will there come a time when digital repositories are as reliable as electricity and network connectivity?
That sounds like a _Star Trek_ world, but if history is our guide, I think the profession will get there.
(I'm not necessarily saying _I'll_ get there with it—such reliability is probably outside my professional lifetime.)
So, yeah, I feel pain and misery in Ruth's post about the achingly out-of-reach nature of repository software that can be pushed down the stack...that can be assumed to exist with all of the capabilities that our users need.

That brings me around to one of Bryan's tweets:
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">If the idea of a digital preservation platform is that it is purpose-built to preserve assets for a long period of time, then isn&#39;t it an obvious design flaw to build it with an EOL in mind? If the system is no longer supported, then can it really be trusted for preservation?</p>&mdash; Bryan J. Brown (@bryjbrown) <a href="https://twitter.com/bryjbrown/status/1407338577332158464?ref_src=twsrc%5Etfw">June 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Can digital repositories really be trusted in-and-of-themselves?
No.
(Not yet?)

That isn't to say that steps aren't being made.
Take, for example, HTTP and HTML.
Those are getting pretty darn reliable, and assumptions can be built that rely on HTML as a markup language and HTTP as a protocol to move it around the network.
I think that is a driver behind the growth of "static websites"—systems that rely on nothing more than delivering HTML and other files over HTTP.
The infrastructure for doing that—servers, browsers, caching, network connectivity, etc.—is all pretty sound.
HTML and HTTP have also stood the test of time—much like how we assume we will always understand how to process TIFF files for images. 

Now there are many ways to generate static websites.
This blog uses Markdown text files and Jekyll as a pre-processor to create a stand-alone folder of HTML and supporting files.
A more sophisticated method might use Drupal as a content management system that exports to a static site.
Jekyll and Drupal are nowhere near as assumed-to-work as HTML and HTTP, but they work well as mechanisms for generating a static site.
Last year, colleagues from the University of Iowa {{ robustlink(href="https://journal.code4lib.org/articles/15326", versionurl="https://archive.li/wip/cIU9H", versiondate="2021-06-23", title="CollectionBuilder-CONTENTdm: Developing a Static Web ‘Skin’ for CONTENTdm-based Digital Collections | Code4Lib Journal", anchor="published a paper about making a static site front-end to CONTENTdm") }} in the Code4Lib Journal, which could be the basis of a digital collection website development.
So if your digital repository creates HTML to be served over HTTP _and_—for the purposes of preservation—the metadata can be encoded in HTML structures that are readily machine-processable?
Well, then you might be getting pretty close to a system you can trust.

But what about the digital objects themselves.
Back in 2006, I crowed about the <a href="https://dltj.org/article/why-fedora-because-you-dont-need-fedora" title="Why Fedora? Because You Don't Need Fedora | Disruptive Library Technology Jester">ability of Fedora repository software to recover itself just based on the files stored to disk</a>.
(Read the article for more details...it has the title "Why Fedora?  Because You Don't Need Fedora" in case that might make it more enticing to read.)
Fedora used a bespoke method of saving digital objects as a series of files on disk, and the repository software provided commands to rebuild the repository database from those files.
That worked for Fedora up to version 3.
For Fedora version 4, some of the key object metadata only existed in the repository database.
From what I understand of version 5 and beyond, Fedora adopted the {{ robustlink(href="https://ocfl.io/", versionurl="https://web.archive.org/web/20201210204722/https://ocfl.io/", versiondate="2021-06-23", title="Oxford Common File Layout website", anchor="Oxford Common File Layout") }} (OCFL), "an application-independent approach to the storage of digital information in a structured, transparent, and predictable manner."
The OCFL website goes on to say: "It is designed to promote long-term object management best practices within digital repositories."
So Fedora is back again in a state where you could rebuild the digital object repository system from a simple filesystem backup.
The repository software becomes a way of optimizing access to the underlying digital objects.
Will OCFL stand the test of time like HTML, HTTP, TIFF, network connectivity, and electricity?
Only time will tell.

So I think we are getting closer.
It is possible to conceive of a system that uses simple files and directories as long-term preservation storage.
Those can be backed up and duplicated using a wide variety of operating systems and tools.
We also have examples of static sites of HTML delivered over HTTP that various tools can create and many, many programs can deliver and render.
We're missing some key capabilities—access control comes to mind.
I, for one, am not ready to push JavaScript very far down our stack of technologies—certainly not as far as HTML—but JavaScript robustness seems to be getting better over time.

Ruth: I'm sorry this isn't easy and that software creators keep moving the goalposts.
(I'll put myself in the "software creator" category.)
We could be better at setting expectations and delivering on them.
(There is probably another lengthy blog post in how software development is more "art" than it is "engineering".)
Developers—the ones fortunate to have the ability and permission to think long term—are trying to make new tools/techniques good enough to push down the stack of assumed technologies.
We're clearly not there for digital repository software, but...hopefully...we are moving in the right direction.