---
title: 'Automatically Generating Podcast Transcripts'
modified: 2022-09-28T20:12:24-04:00
category: Raw Technology
categories:
- Raw Technology
tags:
- accessibility
- machine learning
- podcast
- Amazon Web Services
- personal knowledge management
---
I'm finding it valuable to create annotations on resources to index into my personal knowledge management system.
(The [Obsidian journaling](https://dltj.org/article/obsidian-journaling/) post from late last year goes into some depth about my process.)
I use the [Hypothesis](https://hypothes.is/) service to do this—Hypothesis annotations are imported into Markdown files for Obsidian using the custom script and method I describe in that blog post.
This works well for web pages and PDF files...Hypothesis can attach annotations to those resource types.
Videos are relatively straight forward, too, using Dan Whaley's [DocDrop](https://docdrop.org/) service; it reads the closed captioning and puts that on an HTML page that enables Hypothesis to do its work.
What I'm missing, though, are annotations on podcast episodes.

Podcast creators that take the time to make transcripts available are somewhat unusual.
Podcasts from NPR and NPR member stations are pretty good about this, but everyone else is slacking off.
My task management system has about a dozen podcast episodes where I'd like to annotate transcripts (and one podcast that seemingly _stopped_ making transcripts just before the episode I wanted to annotate!).
So I wrote a little script that creates a good-enough transcript HTML page.
You can see a [sample of what this looks like](https://media.dltj.org/unchecked-transcript/20220928T194120-99-_Invisible--Search_and_Ye_Might_Find/index.html) (from the [Search and Ye Might Find](https://99percentinvisible.org/episode/search-and-ye-might-find/) episode of 99% Invisible).

{{ note(note_text="Of course, <i>99% Invisible</i> has now gone back and added transcripts to all of their episodes, including <a href='https://99percentinvisible.org/episode/search-and-ye-might-find/transcript'>the one used in this example</a>. Thanks? ... No really, thank you 99PI!") }}%}

## _AWS Transcribe_ to the rescue
Amazon Web Services has a [Transcribe](https://aws.amazon.com/transcribe/) service that takes audio, runs it through its machine learning algorithms, and outputs a [WebVTT](https://www.w3.org/TR/webvtt1/) file.
Podcasts are typically well-produced audio, so AWS Transcribe has a clean audio track to work with.
In my testing, AWS Transcribe does well with most sentences; it misses unusual proper names and its sentence detection mechanism is good-but-not-great.
It is certainly good enough to get the main ideas across to provide an anchor for annotations.
A WebVTT file (of a podcast advertisement) looks like this:

```text
WEBVTT

1
00:00:00.190 --> 00:00:04.120
my quest to buy a more eco friendly deodorant quickly started to

2
00:00:04.120 --> 00:00:08.960
stink because sustainability and effectiveness don't always go hand in hand.

3
00:00:09.010 --> 00:00:11.600
But then I discovered finch Finch is a

4
00:00:11.600 --> 00:00:14.830
free chrome extension that scores everyday products on
```

After a `WEBVTT` marker, there are groups of caption statements separated by newlines.
Each statement is numbered, followed by a time interval, followed by the caption itself.
(WebVTT can be much more complicated than this...to include CSS-like text styling and other features; read the specs if you want more detail.)

## What the script does
The code for this is up [on GitHub](https://github.com/dltj/unchecked-transcript) now.
The links to the code below point to the version of software at the time this blog post was written.
Be sure to click the "History" button near the upper right corner of the code listing to see if it has been updated.

1. [Download the audio file](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_transcript.py#L13) from its server and [upload it to an AWS S3 bucket](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_transcript.py#L28) so AWS Transcribe can get to it.
1. [Create a new AWS Transcribe job](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_transcript.py#L34) and [wait for the job to finish](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_transcript.py#L51).
1. [Set a public-read ACL on the WebVT file](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_transcript.py#L59) so this script can get it later. Also, save the output of the transcription job; the function then returns the link to the WebVTT file.
1. In a new function, [get the WebVTT file](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_html.py#L9) from where AWS Transcribe put it on the S3 bucket.
1. Then it [concatenates the caption text into one string](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_html.py#L16) and uses [SpaCy](https://spacy.io/) to [break the transcription into sentences](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_html.py#L21). I'm doing this because the WebTT generates each caption by time, and the transcript is easier to read if it is broken up into sentences.
1. [Loop through the sentences](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_html.py#L29) looking for occurrences when a WebTT caption contains the start of the sentence. That way, I can get the timestamp of when the sentence starts.
1. When the sentences are synced time times, use a [Jinja2 template](https://jinja.palletsprojects.com/) to [create the HTML file](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/create_html.py#L54).
1. Lastly, [upload the HTML](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/upload_html.py#L8) to the S3 bucket as the `index.html` file, and [make a final record of the podcast metadata](https://github.com/dltj/unchecked-transcript/blob/7262d38d16d63e46792f84d0ce822bc238b13c2a/unchecked_transcript/cli.py#L59).

That's it!

## Design choices
Amazon Transcribe is pretty cheap.
AWS charges for each minute a transcript job runs at a rate of [2.4¢ a minute](https://aws.amazon.com/transcribe/pricing/).
Transcribing an hour-long podcast costs about $0.10.
The storage and bandwidth costs are negligible.

The way that the Hypothesis annotation JavaScript works forced the use of a CSS-":before"-content structure.
One of the downsides of DocDrop is that annotations on multiple blocks are changed into just the first block of text.
Based on my experimentation, it seems like the [`user-select: none` property](https://developer.mozilla.org/en-US/docs/Web/CSS/user-select) is enough of a break in the DOM to cause the problem.
Because I didn't want the timestamps included in the annotated text, the timestamps are put into the DOM using a CSS ":before" selector.
Playing with the box margins enables everything to line up.

I'm not including the playback of the podcast audio along with the transcript.
Unlike DocDrop, which embeds the YouTube viewer in the transcript page, playback of the audio from the S3 bucket wouldn't be counted in the podcaster's statistics.
And I'm comfortable with the copyright implications of publicly posting uncorrected transcripts (in the absence of creator-produced transcripts), but not so comfortable as to also offer the audio file.

## Issues
So there are some issues with this setup.

* *Copying and pasting episode data required*: This is running as a command line program with four parameters: audio URL, episode title, episode landing page URL, and podcast title. Sometimes this takes a bit of hunting because podcast sites are not the most friendly for finding the audio URL. Viewing the page source is often necessary, and sometimes digging into the RSS/Atom XML is needed.
* *Times will vary with advertisement inserts*: Because podcast networks insert ads with different lengths over time, the timestamps that were found when the transcription was made probably won't correspond to later playbacks. But I think they will be close enough that I can go back and find the audio clip when I need to.
* *Default directory document doesn't work*: Right now, the "index.html" is required as part of the web link. It would be nice if one could remove that and just refer to the root directory, but AWS CloudFront doesn't work like that.
