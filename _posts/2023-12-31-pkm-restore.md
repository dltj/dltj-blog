---
title: 'Restoring Obsidian Knowledgebase from MacOS Time Machine at the Command Line'
categories:
- Raw Technology
tags:
- personal knowledge mangement
- obsidian
---
While on vacation, I was catching up on some personal knowledge management maintenance I had been putting off. 
At one task—adding a page for a new employee at the company I work for—I noticed that the page for my company was gone. 
Odd, that page has been in my knowledgebase for years...let's go look in the _People, Places, and Organizations_ folder...6 pages?!? There should be at least 60!
And look at that...all of my templates are gone, too.
What else was missing?!?
Here are my project notes for rebuilding my knowledgebase from backups.

I'm using {% include robustlink.html href="https://obsidian.md/" versionurl="https://web.archive.org/web/20231231170629/https://obsidian.md/" versiondate="2023-12-31" title="Obsidian project homepage" anchor="Obsidian" %} as my [personal knowledge management](/tag/personal-knowledge-mangement) tool. 
Obsidian creates a wiki-like experience for a directory of {% include robustlink.html href="https://www.markdownguide.org/getting-started/" versionurl="https://web.archive.org/web/20231231/https://www.markdownguide.org/getting-started/" versiondate="2023-12-31" title="Getting Started | Markdown Guide" anchor="Markdown" %} files on the local computer. 
(See an [earlier post on DLTJ about my use of Obsidian](https://dltj.org/article/obsidian-journaling/).)
I was using iCloud Drive to synchronize that directory of Markdown files across my laptop, phone, and tablet. 
Based on some web searching, I'm guessing that a recent change by Apple on how iCloud Drive synchronizes between machines caused files that hadn't been accessed in a while to disappear—some sort of selective sync function.

My initial reaction—to move my knowledgebase folder out of iCloud Drive and onto the local hard drive—may have hampered the recovery...the files might have been marked as in the cloud and could have been downloaded.
But moving my knowledgebase folder and purchasing an {% include robustlink.html href="https://obsidian.md/sync" versionurl="https://web.archive.org/web/20231231/https://obsidian.md/sync" versiondate="2023-12-31" title="Obsidian Sync" anchor="Obsidian Sync subscription" %}  was what I did.
(I have no regrets...I'll keep the Obsidian Sync subscription. Obsidian has a good, independent development team, and I'm happy to support them.)
But how to get the missing files back?

My laptop has two independent backups: a USB-connected hard disk on my office desk using the built-in {% include robustlink.html href="https://support.apple.com/en-us/HT201250" versionurl="https://web.archive.org/web/20231231/https://support.apple.com/en-us/HT201250" versiondate="2023-12-31" title="Back up your Mac with Time Machine | Apple Support" anchor="MacOS Time Machine" %}, and {% include robustlink.html href="https://arqbackup.com/" versionurl="https://web.archive.org/web/20231231/https://arqbackup.com/" versiondate="2023-12-31" title="Arq Backup homepage" anchor="ArqBackup" %}  uploading to an encrypted AWS S3 bucket. 
I was away from my desk for the week, so I first tried restoring from ArqBackup.
That didn't work; more on that below.
When I got home, I attempted a recovery from the Time Machine drive.

## Recovering an Obsidian Vault from a series of Time Machine backups

Because I didn't know what files when missing when, I thought the best approach was to successively overlay restores of the knowledgebase directory onto each other.
Doing so would mean that there would be files that I had intentionally deleted that would be in the new knowledgebase directory. 
Still, that is only a dozen or so out of the potentially hundreds of missing files—a much better option than having an unknown number of missing files.

First step: restore the knowledgebase directory for each backup set into a separate directory.

{% highlight bash %}
for i in $(tmutil listbackups)                                                                                                                                                            do
echo $i && tmutil restore $i/Macintosh\ HD\ -\ Data/Users/peter/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/Knowledgebase $(basename $i)-Knowledgebase
done
{% endhighlight %}

Each iteration through the backup sets showed the number of restored files:

{% highlight bash %}
Total copied: 28.50 MB (29888454 bytes)
Items copied: 2916
{% endhighlight %}

As I scanned through the `items copied` for each day, there were no points where there was a sudden drop, so I think the file loss was gradual over some time.
The results of this first step were a bunch of directories that looked like "2023-12-26-032655.backup-Knowledgebase"

Next: copy the contents of each backup set, in the order in which the backup sets were created, on top of an empty `Knowledgebase` directory.

{% highlight bash %}
mkdir restored-Knowledgebase
for i in $(ls -d 2*)
do
echo $i && cp -rp $i* restored-Knowledgebase
done
{% endhighlight %}

Now lets run some commands to see what we're dealing with.
First, the number of files in the restored Knowledgebase directory: 3,418.

{% highlight bash %}
find restored-Knowledgebase -type f -print | wc -l
3418
{% endhighlight %}

Next, use the `diff` command to see the differences between the active knowledgebase in my home directory and the restored knowledgebase, and look for the string `Only in restored-Knowledgebase`: 480 files restored that aren't in the active knowledgebase.

{% highlight bash %}
diff  --brief --recursive ~/Knowledgebase restored-Knowledgebase | grep "Only in restored-Knowledgebase/" | wc -l                                                                                                480
{% endhighlight %}

Now let's review a list of files that are only in the active knowledgebase.
This is a reality check to make sure we're on the right path, and indeed this lists only the files that were created since the last backup to the Time Machine drive.

{% highlight bash %}
diff  --brief --recursive ~/Knowledgebase Knowledgebase | grep "Only in /Users/" | less
{% endhighlight %}

One last command to see files that exist in both the active knowledgebase and the restored knowledgebase but don't have the same contents:

{% highlight bash %}
diff  --brief --recursive ~/Knowledgebase Knowledgebase | grep "^Files"
{% endhighlight %}

There was only one file with minor differences...a file that I changed in between backups.
Happy that everything seems in order, I just copy the contents of the restored knowledgebase on top of the active knowledgebase.

{% highlight bash %}
cp -rp restored-Knowledgebase/* ~/Knowledgebase
{% endhighlight %}

## ArqBackup problems
As I mentioned above, my first attempt at restoring was using ArqBackup. 
ArqBackup behaved in a way that I didn't expect...I could use the user interface to restore a _file_ at any point in time or a _directory_ at the point of the latest backup set.
What I couldn't do was what I did with Time Machine: restore a _directory_ at a _specific point in time_.
This seems to be a function of how ArqBackup stores its data.
What this means, though, is that ArqBackup is less a solution for restoring directories (or a whole system) at a point in time and better as a disaster recovery when the laptop and the Time Machine drive are unavailable.