---
title: "Refactoring DLTJ, Winter 2021 Part 4: Thursday Threads Newsletter Launches"
categories:
  - Meta Category
tags:
  - Thursday Threads newsletter
  - jekyll
  - obsidian
---
Success! 
Four parts plus a half (or a "re-do"" of part 2):

1. [Ramp up automation for adding reading sources to Obsidian]({% post_url 2021-12-29-obsidian-journaling %})
2. [Refactor the process of building this static website on AWS]({% post_url  2021-12-30-aws-amplify-jekyll %})
	* [Fix the webmentions cache, an unanticipated diversion]({% post_url 2021-12-31-fixing-webmentions %})
3. [Recreate the ability for readers to get updates by email]({% post_url 2022-01-05-newsletter-launching %})
4. Turn the old DLTJ “Thursday Threads” concept into a newsletter (this post)

Earlier today, the newsletter launched with [issue 79](% post_url 2022-01-06-issue-79-educause-tech-social-media-regulation-apollo-11-at-50 %). 
It wasn't without hiccups, but I don't think any of the problems leaked out to the subscribers. 
I started with a list of 286 email addresses that were subscribed to the 2015 edition. 
This morning I sent an email to all of them on the blind-carbon-copy line from my regular email. 
That way I could see which addresses bounced back as undeliverable (94 addresses) before loading the list into the newsletter database. 
(Undeliverable email counts as a strike against you when using Amazon's Simple Email Service, so I didn't want to start with a bad reputation with them.)

One of the issues I ran into was with the multiprocessing code that I found on the web. 
It didn't work as claimed, and when I tried to adjust it, the loop to process email stalled, so I ripped out that code. 
In the end, with about 200 email addresses, it took just a minute or two of single-threaded, sequential sending to get them all out. 
Perhaps I won't need that multi-threaded capability until _Thursday Threads_ gets much bigger.

## How the Newsletter is Put Together

Like everything on this static site blog, an issue starts as a Markdown file. 
Markdown is a light-weight markup language that translates very easily into HTML, and makes it easy for a writer to create valid HTML. 
It is also possible to mix HTML inside a Markdown file and have the right thing happen. 
The Jekyll processor (the program that turns a folder of Markdown files into a folder of HTML files) has a mechanism for including macros in the markup, and each "thread" in the issue is a macro file. 
If you look at the [Markdown source for issue 79](https://raw.githubusercontent.com/dltj/dltj-blog/master/_posts/2022-01-06-issue-79-educause-tech-social-media-regulation-apollo-11-at-50.markdown), you'll see each heading (marked with `##`) has a `{% raw %}{% include thursday-threads-quote.html{% endraw %}` macro definition.

{% highlight ruby %}
blockquote="The EDUCAUSE 2022 Top 10 IT Issues take an optimistic view of how technology can help make the higher education we deserve—through a shared transformational vision and strategy for the institution, a recognition of the need to place students’ success at the center, and a sustainable business model that has redefined 'the campus.'" 
url="https://er.educause.edu/articles/2021/11/top-10-it-issues-2022-the-higher-education-we-deserve" 
versiondate="2021-11-12"
versionurl="https://web.archive.org/20211127031010/https://er.educause.edu/articles/2021/11/top-10-it-issues-2022-the-higher-education-we-deserve"
anchor="Top 10 IT Issues, 2022: The Higher Education We Deserve" 
post="EDUCAUSE"
{% endhighlight %}

Each of those variables are used in the include processor, which at the moment looks like this (see [current version](https://github.com/dltj/dltj-blog/blob/master/_includes/thursday-threads-quote.html)):

{% highlight liquid %}{% raw %}
<figure class="quote thursdaythread">
  <blockquote>
{{ include.blockquote }}
  </blockquote>
  <figcaption>&mdash;
{% if include.pre %}{{ include.pre }}{% endif %}
{% if include.url %}<a href="{{ include.url }}"{% if include.versionurl %} data-versionurl="{{ include.versionurl }}"{% endif%}{% if include.versiondate %} data-versiondate="{{ include.versiondate }}"{% endif %}{% if include.title %} title="{{ include.title }}"{% endif %}>{{ include.anchor}}</a>{% endif %}
{% if include.post %}{{ include.post }}{% endif %}
  </figcaption>
</figure>
{% endraw %}{% endhighlight %}

That is some semantically-appropriate HTML that with some CSS make the nice layout on the page. 
(And should be accessible to screen readers, too.) 
The content of the "blockquote" variable is inserted at `{% raw %}{{ include.blockquote }}{% endraw %}` spot. 
There are also some conditional statements (`{% raw %}{% if include.pre %} ... {% endif %}{% endraw %}`) that will include markup when a variable has a value assigned to it. 
The best part of these include blocks is that I can save them as separate files in my Obsidian database with links and tags to the places where I got the content. 
In fact, I expect my writing workflow will start with creating these include fragments in my Obsidian database throughout the week, and then when Wednesday night rolls around I'll pick some to drop into an issue. 
(Over time, I aim to convert all 650 previous blog posts into Markdown and add them to my Obsidian database as well.  That will make it even _easier_ to draw threads from the past.) 

So that is where we are: some revitalized technoloy backing DLTJ and a strong intention to write more in the new year. 
Thanks for everyone's interest along the way, and please get in touch if you have any questions or comments.