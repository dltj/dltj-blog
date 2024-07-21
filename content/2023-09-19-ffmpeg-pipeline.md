---
title: 'Processing WOLFcon Conference Recordings with FFMPEG'
modified: 2023-09-19T17:13:03-04:00
category: Raw Technology
categories:
- Raw Technology
tags:
- open source communities
- ffmpeg
- video
mastodon:
- You've got a stack of recordings of Zoom meetings from a conference that you need to upload to YouTube. What do you do? Hopefully this roadmap will help... New blog post: Processing WOLFcon Conference Recordings with FFMPEG https://dltj.org/article/ffmpeg-pipeline
---
WOLFcon—the World Open Library Foundation Conference—was held last month, and all of the meetings were recorded using Zoom. 
Almost all of the sessions were presentations and knowledge-sharing, so giving the recordings a wider audience on YouTube make sense. 
With nearly 50 sessions, though, manually processing the recordings would make the process quite challenging. 
I created a pipeline of `ffmpeg` commands that does most of the grunt work and learned a lot about `ffmpeg` command graphs along the way. 
Here are the steps:

1. [Clip the videos](#clip) from the Zoom recordings.
1. [Rescale the recordings](#rescale) to 1920x1080, if necessary.
1. [Create a title card](#title-card) to add to the front of the recording.
1. [Merge](#merge) the title card, session recording, and outro video into a single video.
1. [Upload](#upload) the videos to YouTube using a script.

Some hard-learned lessons along the way:

* Ffmpeg's `subtitles` filter does not play nicely with filtergraphs that have more than one video input. I needed to create a separate step for burning the title card "subtitles" into the intro video and then concat that video with the session recording and outro videos.
* Ffmpeg's `xfade` filter does not like it when its source video is trimmed. No matter what variations of filters I used, it was always a hard cut between the intro video and the session recording. To solve this, I made a separate step for clipping the longer meeting recording to just the session content. I used a lossless Constant Rate Factor (`-crf`) to not lose too much detail with the multiple encoding steps.

I'm documenting the steps here in case they are helpful to someone else...perhaps I'll need this pipeline again someday.

## Clip sessions from recordings
{: #clip}
Each room of the conference was assigned a Zoom meeting. 
These Zoom meetings allowed remote participants to join the session, and the meetings were set to record. 
This meant, though, that several minutes in the recording at the start and end of the session were not useful content. 
(Sometimes the Zoom meeting/recording for the same room would just continue from one session to the next, so multiple sessions would end up on one recording.)
The valuable part of each recording would need to be clipped from the larger whole.

{% highlight shell linenos %}
ffmpeg -y \
  -i FOLIO\ Roadmap.mkv \
  -ss 0:01:22 -to 0:50:26 \
  -c:v libx264 -crf 0 \
  FOLIO\ Roadmap.trimmed.mp4
{% endhighlight %}

Each option means:

1. Ffmpeg command with -y to overwrite any existing file without prompting
2. Recording file from Zoom
3. Scan-start (`-ss`) and end (`-to`) points. Could have also used `-d` for duration. Note that the placement of `-ss` here relative to the `-i` input filename means `ffmpeg` will perform a frame-accurate. This avoids the problem of blank or mostly blank frames until the next keyframe is found in the file. See [How to Cut Video Using FFmpeg in 3 Easy Ways (Extract/Trim)](https://ottverse.com/trim-cut-video-using-start-endtime-reencoding-ffmpeg/) for a discussion.
4. Re-encode with the x264 codec with a lossless {% include robustlink.html href="https://trac.ffmpeg.org/wiki/Encode/H.264#crf" versionurl="https://web.archive.org/web/20230904070629/https://trac.ffmpeg.org/wiki/Encode/H.264#crf" versiondate="2023-09-12" title="H.264 Video Encoding Guide" anchor="Constant Rate Factor" %}.
5. Output file name

## Rescale recordings
{: #rescale}
Most of the recordings from Zoom output to Full HD (1920x1080) resolution, but some were recorded to quite squirrely dimensions. 
(1920 by 1008, 1920 by 1030 ... 1760 by 900, really?)
To find the resolution of each recording file, I used the `ffprobe` command:

{% highlight shell linenos %}
find . -type f -name '*.mkv' -exec sh -c '
  for file do
    printf "%s:" "$file"
    args=( -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$file")
    ffprobe "${args[@]}"
  done
' exec-sh {} + 
{% endhighlight %}

1. Run a `find` command to get a list of all `.mkv` files and pipe the list into a sub-shell.
2. For each line of the list of files...
3. ...print out the filename (without a newline at the end)...
4. ...then build an argument array for the `ffprobe` command to output width and heigth...
5. ...and execute the command
6. (end of sub-shell)
7. (end of find)

Line 4 is necessary because some filenames have spaces, and [spaces in filename for ffmpeg in bash](https://stackoverflow.com/questions/38533523/spaces-in-filename-for-ffmpeg-in-bash/38533746#38533746) can be a little challenging.

I moved the recordings that weren't 1980x1080 to a separate directory and ran an ffmpeg command to add letterboxing/rescaling as needed to get the output to Full HD resolution. 
The `-ss` and `-to` options can also be used to clip the video to the correct length at the same time. 

{% highlight shell linenos %}
ffmpeg -y \
  -i 'zoom-recording-tuesday-2pm-room-701.mp4' \
  -ss 17868 -to 20104 \
  -vf 'scale=(iw*sar)*min(1920/(iw*sar)\,1080/ih):ih*min(1920/(iw*sar)\,1080/ih),
       pad=1920:1080:(1920-iw*min(1920/iw\,1080/ih))/2:(1080-ih*min(1920/iw\,1080/ih))/2' \
  -crf 0 
  'FOLIO Migrations.trimmed.mp4
{% endhighlight %}

1. Ffmpeg command
1. Input video file
1. Start and stop points for the session recording
1. Use a string of video filters, and in this first filter: scale the recording so the longest dimension is either 1920 pixels wide or 1080 pixels tall
1. For the second filter of the chain, pad the frame to 1920x1080 and put the source video in the center/middle of the output frame.
1. Constant Frame Rate of lossless
1. Output file name

## Create Title Card snippet
{: #title-card}
Each session recording has a 15-second title card with the session's name.
The 15 second video itself is just a PowerPoint animation of the conference logo sliding to the right half of the frame and a red box fading in on the left side of the frame. 
Each animation element was assigned a timing, and the resulting "presentation" was exported from PowerPoint to a video file. 
The music comes from [Ecrett](https://ecrettmusic.com/), so I have high hopes that it will pass the music copyright bar. 
The audio track was added to the video using—you guessed it—ffmpeg:

{% highlight shell linenos %}
ffmpeg \
  -i WOLFcon\ 2023\ Intro\ Title\ Card.mov \
  -i WOLFcon\ 2023\ Intro\ audio.mp3 \
  -c:v copy 
  -map 0:v:0 -map 1:a:0 
  WOLFcon\ 2023\ Intro\ Title\ Card\ with\ audio.mov
{% endhighlight %}

1. Ffmpeg command
2. First stream input is the recording of the PowerPoint animation
3. Second stream input is the sound file
4. Using the 'copy' codec
5. Mapping the first input's zero-th stream (video) to the output
6. Mapping the second input's one-th stream (audio) to the output
7. Writing the combined file

So with the blank title card video done, the next step is to burn/overlay the text of the session title into the video. 
I messed with ffmpeg's `drawtext` filter for a while because the alternative—the `subtitles` filter—seemed too complicated. 
One thing that `subtitles` does nicely, though, is wrap the text to a given area on the video frame...sometimes complexity is a good thing. 
The open source [Aegisub Advanced Subtitle Editor](https://aegisub.org/) was immensely useful in creating the subtitle definition file. 
I can simply replace the text of the session title in the last line of the subtitle definition file, then feed it into ffmpeg. 

The subtitle definition (so-called ".ass") file generated by Aegisub is a text file, and it looks like this:

{% highlight shell linenos %}
[Script Info]
; Script generated by Aegisub 3.2.2
; http://www.aegisub.org/
Title: Default Aegisub file
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: None
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Left side middle,Helvetica Neue,72,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0.5,0,4,50,920,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:04.00,0:00:13.00,Left side middle,,0,0,0,,FOLIO Roadmap Update
{% endhighlight %}

Just the last line needs to change for each session title. 
Another ffmpeg command overlays the subtitles onto the title card video:

{% highlight shell linenos %}
ffmpeg -y \
  -i ../WOLFcon\ 2023\ Intro\ Title\ Card\ with\ audio.mov \
  -vf "subtitles=FOLIO Roadmap.ass" \
  FOLIO\ Roadmap.intro.mp4
{% endhighlight %}

1. Ffmpeg command
2. Input file is the title card with audio
3. Add the `subtitles` video filter with the session-specific ASS file
4. Output file

## Merge sources to the final file
{: #merge}
Now we have all of the pieces to make the final recording

{% highlight shell linenos %}
ffmpeg -y \
  -i FOLIO\ Roadmap.intro.mp4 \
  -i FOLIO\ Roadmap.trimmed.mp4 \
  -i ../WOLFcon\ 2023\ Outro\ Title\ Card\ with\ audio.mov \
  -filter_complex "[0:v]fps=30/1,setpts=PTS-STARTPTS[v0];
    [1:v]fps=30/1,settb=AVTB,format=yuva420p,fade=in:st=0:d=1:alpha=1,setpts=PTS-STARTPTS+((14)/TB)[v1];
    [2:v]fps=30/1,settb=AVTB,format=yuva420p,fade=in:st=0:d=1:alpha=1,setpts=PTS-STARTPTS+((2959)/TB)[v2];
    [v0][v1]overlay,format=yuv420p[vfade1];
    [vfade1][v2]overlay,format=yuv420p[fv];
    [0:a]asetpts=PTS-STARTPTS[a0];
    [1:a]asettb=AVTB,asetpts=PTS-STARTPTS+((14)/TB),compand=.3:1:-90/-60|-60/-40|-40/-30|-20/-20:6:0:-90:0.2[a1];
    [2:a]asetpts=PTS-STARTPTS+((2959)/TB)[a2];
    [a0][a1]acrossfade=d=1[afade1];
    [afade1][a2]acrossfade=d=1[fa];" \
  -map "[fv]" -map "[fa]" \
  -crf 0 -ac 2 \
  FOLIO\ Roadmap.complete.mp4
{% endhighlight %}

There are some filter commands here to cross-fade the video and audio between video segments that are butting up next to each other. 
There is an excellent description of the [ffmpeg cross-fade options](https://superuser.com/questions/778762/crossfade-between-2-videos-using-ffmpeg/1643589#1643589), and I'm using the "traditional" method.

1. The ffmpeg command...one more time!
2. The '0' input file is the title card video with the subtitles
3. The '1' input file is the trimmed recording from Zoom
4. The '2' input file is the outro file (a 6-second file with some end-bumper music)
5. Start of the filtergraph, tagging the video stream of the first input file as `[v0]`, set the video as 30 frames-per-second, and anchor the "presentation timestamp" at the 0-th frame.
6. The video stream of the second input file is set to `[v1]`. The `format` filter sets an alpha channel to make the fade work, the `fade` filter makes cross-fade with a `d`-duration of 1 second, and the `setpts` filter offsets the start of the video to 14 seconds after the 0-th frame. (The title card video is 15 seconds, so making the recording fade in at the 14 second mark gives us that 1 second of overlap.)
7. The third video stream is `[v2]`. The parameters are nearly identical to the previous line with just the starting time difference. (That number varies by the length of the session recording.)
8. This filter overlays the `[v0]` and `[v1]` videos. This works because of the alpha channel and offset start of the second input. The output is tagged as `[vfade1]`.
9. Same as the previous line with the intro-plus-recording and the outro clip. The output is tagged as `[fv]`.
10. Tags the audio stream of the '0' input file.
11. Tags the audio stream of the '1' input file and offsets its start (similar to the video stream). I'm also applying the [audio compression-and-expansion filter](https://ffmpeg.org/ffmpeg-filters.html#compand) to help raise the volume of quiet parts of the Zoom recording.
12. Tags the audio stream of the '2' input file and offsets its start.
13. Crossfades the first and second audio streams across 1 second.
14. Crossfades the second and third audio streams across 1 second and tags the output as `[fa]`.
15. Maps the ends of the video pipeline (`[fv]`) and audio pipeline (`[fa]`) to the output.
16. Sets the codec to lossless and audio to stereo.
17. The final output file.

## Upload to YouTube
{: #upload}
With the files ready, it is time to upload them to YouTube. 
The [youtube-upload](https://github.com/tokland/youtube-upload) script is useful as a tool for batch uploading the videos. 
There are a couple of caveats to be aware of:

1. The script uses an old authentication method against the YouTube API. There is a [comment on issue 352](https://github.com/tokland/youtube-upload/issues/352#issuecomment-1452006587) that has good advice on how to get around that.
2. Without additional work, YouTube will automatically lock-as-private any videos uploaded using the API. Details and  instructions are in a [comment on issue 306](https://github.com/tokland/youtube-upload/issues/306#issuecomment-691576032), but it involves [getting your YouTube API Project validated](https://support.google.com/youtube/contact/yt_api_form).

The command looks like this:
{% highlight shell linenos %}
youtube-upload \
  --title="FOLIO Project Roadmap" \
  --description="Multi-line description goes here." \
  --category="Education" \
  --default-language="en" --default-audio-language="en" \
  --client-secrets=./client_secret.json \
  --credentials-file=./credentials_file.json \
  --playlist="WOLFcon 2023" \
  --embeddable=True --privacy=public \
  'FOLIO\ Roadmap.complete.mp4'
{% endhighlight %}

That should all be self-explanatory. 
One thing to be aware of is the authentication step. 
The `client_secret.json` file is downloaded from the Google API Console when the YouTube API project is created; that API project will need to be set up and this credentials file saved before running this script. 
Also, the `credentials_file.json` won't exist when this command is first run, and you'll be prompted to go to a specific URL to authorize the YouTube API project. 
After that, the credentials file will exist and you won't be prompted again.

And since I already had the session metadata in a spreadsheet, it was easy to write a formula that put all of the pieces together:

> ="youtube-upload --title='"&B2&"' --description='"&C2&"'  --category='Education' --default-language='en' --default-audio-language='en' --client-secrets=./client_secret.json --credentials-file=./credentials_file.json --playlist='WOLFcon 2023' --embeddable=True --privacy=public '"&A2&"'"

Then it is just a matter of copying and pasting the calculated command lines into the terminal.