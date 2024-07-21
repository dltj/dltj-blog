---
title: Managing Remote Conference Presenters with Zoom
modified: 2020-03-14T20:08:19-04:00
categories:
- Raw Technology
tags:
- howto
- zoom
- code4lib
---
Bringing remote presenters into a face-to-face conference is challenging and fraught with peril.
In this post, I describe a scheme using [Zoom](https://zoom.us/) that had in-person attendees forgetting that the presenter was remote!

The [Code4Lib conference](https://2020.code4lib.org/) was this week, and with the [COVID-19 pandemic](https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic) breaking through many individuals and institutions made decisions to not travel to Pittsburgh for the meeting.
We had an unprecedented nine presentations that were brought into the conference via Zoom.
I was chairing the livestream committee for the conference (as I have done for several years—skipping last year), so it made the most sense for me to arrange a scheme for remote presenters.
With the help of the on-site A/V contractor, we were able to pull this off with minimal requirements for the remote presenter.

## List of Requirements

* 2 [Zoom Pro](https://zoom.us/pricing) accounts
* 1 PC/Mac with video output, as if you were connecting an external monitor (the "Receiving Zoom" computer)
* 1 PC/Mac (the "Coordinator Zoom" computer)
* 1 USB audio interface
* Hardwired network connection for the Receiving Zoom computer (recommended)

The _Pro_-level Zoom accounts were required because we needed to run a group call for longer than 40 minutes (to include setup time).
And two were needed: one for the Coordinator Zoom machine and one for the dedicated Receiving Zoom machine.
It would have been possible to consolidate the two Zoom Pro accounts and the two PC/Mac machines into one, but we had back-to-back presenters at Code4Lib, and I wanted to be able to help one remote presenter get ready while another was presenting.

In addition to this equipment, the A/V contractor was indispensable in making the connection work.
We fed the remote presenter's video and audio from the Receiving Zoom computer to the contractor's A/V switch through HDMI, and the contractor put the video on the ballroom projectors and audio through the ballroom speakers.
The contractor gave us a selective audio feed of the program audio minus the remote presenter's audio (so they wouldn't hear themselves come back through the Zoom meeting).
This becomes a little clearer in the diagram below.

## Physical Connections and Setup
This diagram shows the physical connections between machines.

![Diagram of parts](../../wp-content/uploads/2020/2020-03-14-zoom-remote-presenters.svg)

The _Audio Mixer_ and _Video Switch_ were provided and run by the A/V contractor.
The _Receiving Zoom_ machine was the one that is connected to the A/V contractor's Video Switch via an HDMI cable coming off the computer's external monitor connection.
In the Receiving Zoom computer's control panel, we set the external monitor to mirror what was on the main monitor.
The audio and video from the computer (i.e., the Zoom call) went out the HDMI cable to the A/V contractor's Video Switch.
The A/V contractor took the audio from the Receiving Zoom computer through the Video Switch and added it to the Audio Mixer as an input channel.
From there, the audio was sent out to the ballroom speakers the same way audio from the podium microphone was amplified to the audience.
We asked the A/V contractor to create an audio mix that includes all of the audio sources _except_ the Receiving Zoom computer (e.g., in-room microphones) and plugged that into the USB Audio interface.
That way, the remote presenter could hear the sounds from the ballroom—ambient laughter, questions from the audience, etc.—in their Zoom call.
(Note that it was important to remove the remote presenter's own speaking voice from this audio mix; there was a significant, distracting delay between the time the presenter spoke and the audio was returned to them through the Zoom call.)

We used a hardwired network connection to the internet, and I would recommend that—particularly with tech-heavy conferences that might overflow the venue wi-fi.
(You don't want your remote presenter's Zoom to have to compete with what attendees are doing.)
Be aware that the hardwired network connection will cost more from the venue, and may take some time to get functioning since this doesn't seem to be something that hotels often do.

In the Zoom meeting, we unmuted the microphone and selected the USB Audio interface as the microphone input.
As the Zoom meeting was connected, we made the meeting window full-screen so the remote presenter's face and/or presentation were at the maximum size on the ballroom projectors.

## Setting Up the Zoom Meetings
The two Zoom accounts came from the [Open Library Foundation](https://openlibraryfoundation.org/). (Thank you!)
As mentioned in the requirements section above, these were _Pro_-level accounts.
The two accounts were `olf_host2@openlibraryfoundation.org` and `olf_host3@openlibraryfoundation.org`.
The `olf_host2` account was used for the Receiving Zoom computer, and the `olf_host3` account was used for the Coordinator Zoom computer.
The Zoom meeting edit page looked like this:

![Screen capture of the Zoom meeting edit page](../../wp-content/uploads/2020/2020-03-14-screenshot-zoom.png)

This is for the _"Code4Lib 2020 Remote Presenter A"_ meeting with the primary host as `olf_host2@openlibraryfoundation.org`.
Note these settings:

* A recurring meeting that ran from 8:00am to 6:00pm each day of the conference.
* _Enable join before host_ is checked in case the remote presenter got on the meeting before I did.
* _Record the meeting automatically in the cloud_ to use as a backup in case something goes wrong.
* _Alternative Hosts_ is `olf_host3@openlibraryfoundation.org`

The _"Code4Lib 2020 Remote Presenter B"_ meeting was exactly the same except the primary host was `olf_host3`, and `olf_host2` was added as an alternative host.
The meetings were set up with each other as the alternative host so that the Coordinator Zoom computer could start the meeting, seamlessly hand it off to the Receiving Zoom computer, then disconnect.

## Preparing the Remote Presenter
Remote presenters were given this information:

> Code4Lib will be using [Zoom](https://zoom.us/support/download) for remote presenters. In addition to the software, having the proper audio setup is vital for a successful presentation. 
>
> * **Microphone**: The best option is a headset or earbuds so a microphone is close to your mouth. Built-in laptop microphones are okay, but using them will make it harder for the audience to hear you.
> * **Speaker**: A headset or earbuds are required. _Do not use your computer's built-in speakers._ The echo cancellation software is designed for small rooms and cannot handle the delay caused by large ballrooms.
>
> You can test your setup with a [test Zoom call](https://zoom.us/test). Be sure your microphone and speakers are set correctly in Zoom. Also, try sharing your screen on the test call so you understand how to start and stop screen sharing. The audience will see everything on your screen, so quit/disable/turn-off notifications that come from chat programs, email clients, and similar tools. 
>
> Plan to connect to the Zoom meeting 30 minutes before your talk to work out any connection or setup issues. 

At the 30-minute mark before the remote presentation, I went to the ballroom lobby and connected to the designated Zoom meeting for the remote presenter using the Coordinator Zoom computer.
I used this checklist with each presenter:

* Check presenter's microphone level and sound quality (make sure headset/earbud microphone is being used!)
* Check presenter's speakers and ensure there is no echo
* Test screen-sharing (_start_ and _stop_) with presenter
* Remind presenter to turn off notifications from chat programs, email clients, etc.
* Remind the presenter that they need to keep track of their own time; there is no way for us to give them cues about timing other than interrupting them when their time is up

The critical item was making sure the audio worked (that their computer was set to use the headset/earbud microphone and audio output).
The result was excellent sound quality for the audience.

When the remote presenter was set on the Zoom meeting, I returned to the A/V table and asked a livestream helper to connect the Receiving Zoom to the remote presenter's Zoom meeting.
At this point, the remote presenter can hear the audio in the ballroom of the speaker before them coming through the Receiving Zoom computer.
Now I would lock the Zoom meeting to prevent others from joining and interrupting the presenter (from the Zoom Participants panel, select _More_ then _Lock Meeting_).
I hung out on the remote presenter's meeting on the Coordinator Zoom computer in case they had any last-minute questions.
As the speaker in the ballroom was finishing up, I wished the remote presenter well and disconnected the Coordinator Zoom computer from the meeting.
(I always selected _Leave Meeting_ rather than _End Meeting for All_ so that the Zoom meeting continued with the remote presenter and the Receiving Zoom computer.)

As the remote presenter was being introduced—and the speaker would know because they could hear it in their Zoom meeting—the A/V contractor switched the video source for the ballroom projectors to the Receiving Zoom computer and unmuted the Receiving Zoom computer's channel on the Audio Mixer.
At this point, the remote speaker is off-and-running!

## Last Thoughts
This worked really well.  Surprisingly well.
So well that I had a few people comment that they were taken aback when they realized that there was no one standing at the podium during the presentation.

I'm glad I had set up the two Zoom meetings.
We had two cases where remote presenters were back-to-back.
I was able to get the first remote presenter set up and ready on one Zoom meeting while preparing the second remote presenter on the other Zoom meeting.
The most stressful part was at the point when we disconnected the first presenter's Zoom meeting and quickly connected to the second presenter's Zoom meeting.
This was slightly awkward for the second remote presenter because they didn't hear their full introduction as it happened and had to jump right into their presentation.
This could be solved by setting up a second Receiving Zoom computer, but this added complexity seemed to be too much for the benefit gained.

I would definitely recommend making this setup a part of the typical A/V preparations for future Code4Lib conferences.
We don't know when an individual's circumstances (much less a worldwide pandemic) might cause a last-minute request for a remote presentation capability, and the overhead of the setup is pretty minimal.