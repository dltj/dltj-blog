---
title: 'Ghost Newsletter Software Findings: Got Past the Mailgun Problem, but Got Stuck On Ugly HTML'
modified: 2024-07-14T21:16:00-04:00
categories:
- Raw Technology
tags:
- open source software
- html
- email
---
This was going to be only a post about how I got the {% include robustlink.html href="https://ghost.org/" versionurl="https://web.archive.org/web/20240714053142/https://ghost.org/" versiondate="2024-07-14" title="Ghost homepage" anchor="Ghost newsletter software" %} to use {% include robustlink.html href="https://aws.amazon.com/ses/" versionurl="https://web.archive.org/web/20240713105805/https://aws.amazon.com/ses/" versiondate="2024-07-13" title="Amazon Simple Email Service | AWS" anchor="Amazon Simple Email Service" %} (AWS SES) instead of the {% include robustlink.html href="https://www.mailgun.com/" versionurl="https://web.archive.org/web/20240713054008/https://www.mailgun.com/" versiondate="2024-07-13" title="Mailgun homepage" anchor="built-in Mailgun support" %}, but it turned into that plus why I can't use Ghost for the DLTJ Newsletter.

## Ghost's bulk email delivery problem
{: #ghost-mailgun}
One of Ghost's downsides is that it only supports the Mailgun service for delivering newsletter issues. Ghost can use any email delivery agent for what it calls “transactional” email: email verification on new accounts, password resets, using email to log in, etc. Of course, the point of email newsletter software is to send issues as email, so limiting a core feature to one mechanism is rather unfortunate.

There are many threads on the Ghost support forum about using bulk email services other than Mailgun, but {% include robustlink.html href="https://forum.ghost.org/t/support-sending-bulk-email-from-other-providers/30993/5" versionurl="https://web.archive.org/web/20240714230223/https://forum.ghost.org/t/support-sending-bulk-email-from-other-providers/30993/#post_5" versiondate="2024-07-14" title="Support sending bulk email from other providers - Contributing to Ghost | Ghost Forum" anchor="this post from September 2022" %} has a reply from a Ghost staff member about why this is so hard: they tie email analytics (reports of who opens email and who follows which links) to the each user. That functionality needs deeper integration with the bulk email service than just sending email. I don't care about that — in fact, I make sure that DLTJ and its newsletter don't gather reader details — but I get that this is important to some people.

The problem with Mailgun is that it has become quite expensive for self-hosted hobbyists to use. They used to have a "hidden" pay-as-you-go service that was pretty inexpensive, but {% include robustlink.html href="https://help.mailgun.com/hc/en-us/articles/360048661093-Can-you-explain-pay-as-you-go-PAYG-billing" versionurl="https://archive.ph/H9ger" versiondate="2024-07-14" title="Can you explain pay-as-you-go (PAYG) billing? | Mailgun Help Center" anchor="earlier this year they eliminated that" %}. Now there are reports of Ghost users having to pay $35/month to deliver just a couple hundred emails. (AWS is expensive, but not _that_ expensive!)

In that same Ghost support forum thread mentioned earlier, this is one line about someone who solved this problem pointing to a {% include robustlink.html href="https://hdsplus.co/ghosler-envio-de-emails-y-newsletter-con-ghost-desde-cualquier-servidor-smtp/" versionurl="https://web.archive.org/web/20240714230720/https://hdsplus.co/ghosler-envio-de-emails-y-newsletter-con-ghost-desde-cualquier-servidor-smtp/" versiondate="2024-07-14" title="Ghosler: Envío de emails y Newsletter con Ghost desde cualquier servidor SMTP | HDS plus" anchor="Spanish-language post" %}. That post, in turn, points to the {% include robustlink.html href="https://github.com/ItzNotABug/ghosler" versionurl="https://web.archive.org/web/20240714230923/https://github.com/ItzNotABug/ghosler" versiondate="2024-07-14" title="ItzNotABug/ghosler: Send newsletter emails to your Ghost CMS subscribers & members, using your own email credentials! | GitHub" anchor="ghosler software from ItzNotABug on GitHub" %}. That software uses a webhook that Ghost fires whenever an issue is published. Ghosler reads the subscriber database from Ghost and then sends email to any SMTP endpoint...precisely what I need!

## Using Ghosler with AWS SES in a Docker Compose stack
{: #ghosler}
One requirement that I have is to run this software in Docker containers for ease of management and coexistence with other software. There are several examples of running Ghost in Docker; my way is certainly not the only way to do it. Another of my requirements is to put anything that isn't public-facing on my {% include robustlink.html href="https://tailscale.com/" versionurl="https://web.archive.org/web/20240714180848/https://tailscale.com/" versiondate="2024-07-14" title="Tailscale homepage" anchor="Tailscale" %} network. So you'll see that mentioned in this Docker Compose file as well. There are two Compose files: one for Mariadb, phpMyAdmin, and Ghost and another Compose file that builds Ghosler.

{% highlight yaml linenos %}
## File: ghost/docker-compose.yml
services:
  mariadb:
    image: mariadb:11.4.2
    container_name: mariadb
    command: --default-authentication-plugin=mysql_native_password
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ...root-password...
    volumes:
      - mariadb_data:/var/lib/mysql
    ports:
      - 3306:3306

  phpmyadmin:
    image: phpmyadmin:5.2.1
    container_name: phpmyadmin
    network_mode: service:ts-phpmyadmin
    depends_on:
      - mariadb
      - ts-phpmyadmin
    environment:
      PMA_HOST: mariadb
      PMA_PORT: 3306
      PMA_ARBITRARY: 1
      APACHE_PORT: 8080
    restart: unless-stopped
  ts-phpmyadmin:
    image: tailscale/tailscale:latest
    hostname: aws-phpmyadmin
    environment:
      - TS_AUTHKEY=...tailscale-auth-secret...?ephemeral=false
      - TS_STATE_DIR=/var/lib/tailscale
      - "TS_EXTRA_ARGS=--advertise-tags=tag:container"
      - TS_SERVE_CONFIG=/config/ts-serve-config-phpmyadmin.json
    ports:
      - "8080:8080"
    volumes:
      - ts-data-phpmyadmin:/var/lib/tailscale
      - ts-config:/config:ro
      - /dev/net/tun:/dev/net/tun
    cap_add:
      - net_admin
      - sys_module
    restart: unless-stopped

  ghost:
    image: ghost:5-alpine
    container_name: ghost
    restart: unless-stopped
    ports:
      - 8081:2368
    networks:
      - caddy_net
      - default
    environment:
      # see https://ghost.org/docs/config/#configuration-options
      enableDeveloperExperiments: true
      database__client: mysql
      database__connection__host: mariadb
      database__connection__user: ghost
      database__connection__password: ...db-user-password...
      database__connection__database: ghost
      # Configure SMTP server for Ghost
      mail__from: newsletter@newsletter.dltj.org
      mail__transport: SMTP
      mail__options__host: email-smtp.us-east-1.amazonaws.com
      mail__options__port: 465
      mail__options__auth__user: ...AWS-access-key...
      mail__options__auth__pass: ...AWS-secret-key...
      mail__options__secure_connection: true
      mail__options__service: SES
      mail__from: "'DLTJ Newsletter' <newsletter@dltj.org>"
      url: https://newsletter.dltj.org
      # contrary to the default mentioned in the linked documentation, this image defaults to NODE_ENV=production (so development mode needs to be explicitly specified if desired)
      #NODE_ENV: development
    volumes:
      - ghost_data:/var/lib/ghost/content

  caddy_reverse_proxy:
    # Use the caddy:latest image from Docker Hub
    image: caddy:latest
    restart: unless-stopped
    container_name: caddy_proxy
    ports:
      - 80:80
      - 443:443
    volumes:
      # Mount the host Caddyfile
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config
    networks:
      - caddy_net

networks:
  caddy_net:
  default:

volumes:
  mariadb_data:
  ghost_data:
  caddy_data:
  caddy_config:
  ts-config:
    external: true
  ts-data-phpmyadmin:
    driver: local

## Contents of `ts-serve-config-phpmyadmin.json`
## {
##   "TCP": { "443": { "HTTPS": true } },
##   "Web": { "${TS_CERT_DOMAIN}:443": { "Handlers": { "/": { "Proxy": "http://127.0.0.1:8080" } } } },
##  "AllowFunnel": { "${TS_CERT_DOMAIN}:443": false }
## }
##
##
## Contents of `Caddyfile`
## {
##     email jester@dltj.org 
## }
## newsletter.dltj.org {
##     reverse_proxy ghost:2368
## }
{% endhighlight %}

The parts prefaced with `ts-` are for the Tailscale Docker container ({% include robustlink.html href="https://tailscale.com/kb/1282/docker" versionurl="https://web.archive.org/web/20240714231338/https://tailscale.com/kb/1282/docker" versiondate="2024-07-14" title="Using Tailscale with Docker | Tailscale docs" anchor="documentation" %}). `ts-config` is a Docker volume where I store Tailscale configuration files, of which `ts-serve-config-phpmyadmin.json` is one. 

Inside the Ghost directory, I cloned the Ghosler software: `git clone https://github.com/ItzNotABug/ghosler.git`. Then, I added this Docker Compose file to that directory.
{% highlight yaml linenos %}
## File: ghost/ghosler/docker-compose.yml
services:
  ghosler:
    container_name: ghosler
    build: .
    network_mode: service:ts-ghosler
    restart: unless-stopped
    depends_on:
      - ts-ghosler
    tty: true
    volumes:
      - ghosler_data:/usr/src/app
      - ./configuration/config.production.json:/usr/src/app/configuration/config.production.json:rw

  ts-ghosler:
    image: tailscale/tailscale:latest
    hostname: ghosler.internal
    environment:
      - TS_AUTHKEY=...tailscale-auth-key...?ephemeral=false
      - TS_STATE_DIR=/var/lib/tailscale
      - "TS_EXTRA_ARGS=--advertise-tags=tag:container"
      - TS_SERVE_CONFIG=/config/ts-serve-config-ghosler.json
    ports:
      - "2369:2369"
    volumes:
      - ts-data-ghosler:/var/lib/tailscale
      - ts-config:/config:ro
      - /dev/net/tun:/dev/net/tun
    cap_add:
      - net_admin
      - sys_module
    restart: unless-stopped
    networks:
      - ghost_default

volumes:
  ghosler_data:
    driver: local
  ts-data-ghosler:
    driver: local
  ts-config:
    external: true

networks:
  ghost_default:
    external: true
{% endhighlight %}

An interesting bit here is `network_mode: service:ts-ghosler`. Documentation about this is hard to come by ({% include robustlink.html href="https://forums.docker.com/t/diffcult-to-find-documentation-about-how-network-mode-service-service-name-works/137008" versionurl="https://web.archive.org/web/20240714231641/https://forums.docker.com/t/diffcult-to-find-documentation-about-how-network-mode-service-service-name-works/137008" versiondate="2024-07-14" title='Diffcult to find documentation about how network_mode: &ldquo;service:<service_name>&rdquo; works | Docker Community Forum' anchor="as noted in the Docker forum" %}), but what this does is put the `ghosler` and `ts-ghosler` containers in the same network namespace. To the outside, it looks like one machine.

When you follow the directions for setting up Ghosler's webhook in Ghost, you'll need to go into the Ghost configuration and change the URL of the webhook so that it is `http://ghosler.internal:2369/published` — the Docker hostname and port. I found that Ghosler didn't know enough about itself to set this automatically.

## The problem with Ghost
So, having set up Ghost and its side-buddy Ghosly in Docker and confirmed that I could deliver email newsletters, I set about importing my past newsletter issues into Ghost. And here is where I got stuck.

My blog has gone through two phases: the Wordpress phase from its origin in 2008 to mid-2015, and the Jekyll static site generator phase from 2015 to the present. My posting history is a mixture of HTML exports from Wordpress and Markdown files with some moderately elaborate include macros. Even back in the Wordpress days, the posts were constructed in HTML first rather than using the <abbr title="What You See Is What You Get">WYSIWYG</abbr> editor. The way content is laid out on the page is moderately important to me using good—or at least increasingly better—semantic HTML. (As with all things, learning improved semantic HTML is an ongoing process.)

I decided to use Ghost's "Universal Import" format to migrate content. This is a JSON file that Ghost uses to transport a newsletter from one installation to another, so it seemed to promise the highest fidelity. In fact, I found that if I took a Ghost export JSON file and replaced the `posts` array with entries that looked like this, the import would go fine:

{% highlight python linenos %}
                post_entry = {
                    "id": str(post_id),
                    "uuid": str(post_uuid),
                    "title": title,
                    "slug": slug,
                    "mobiledoc": None,
                    "lexical": None,
                    "html": post_html,
                    "comment_id": str(post_id),
                    "plaintext": None,
                    "feature_image": None,
                    "featured": 0,
                    "type": "post",
                    "status": "published",
                    "locale": None,
                    "visibility": "public",
                    "email_recipient_filter": "all",
                    "created_at": pub_date,
                    "updated_at": pub_date,
                    "published_at": pub_date,
                    "custom_excerpt": None,
                    "codeinjection_head": None,
                    "codeinjection_foot": None,
                    "custom_template": None,
                    "canonical_url": None,
                    "newsletter_id": None,
                    "show_title_and_feature_image": 0,
                }
{% endhighlight %}

Note that there is a field for `lexical` that I'm leaving empty and a field for `html` that I'm setting to the post's HTML. Ghost—being a JavaScript application—uses {% include robustlink.html href="https://lexical.dev/" versionurl="https://web.archive.org/web/20240714231923/https://lexical.dev/" versiondate="2024-07-14" title="Lexical homepage" anchor="Lexical" %} as its native internal rich text format. And it helpfully converts HTML to Lexical on import. The problem is that Lexical is a (very) lossy format, so HTML that used to look like this:

{% highlight html linenos %}
<h2 id="p25973-card-based-qa-sessions">Index Card-based Question and Answer Sessions</h2>
<blockquote>
  <p>Here is the formula:</p>
  <ol>
    <li>Throw away the audience microphones.</li>
    <li>Buy a pack of index cards.</li>
    <li>Hand out the cards to the audience before or during your talk.</li>
    <li>Ask people to write their questions on the cards and pass them to the end of the row.</li>
    <li>Collect the cards at the end of the talk.</li>
    <li>Flip through the cards and answer only good (or funny) questions.</li>
    <li>Optional: have an accomplice collect and screen the questions for you during the talk.</li>
  </ol>
  <p>Better yet, if you are a conference organizer, buy enough index cards for every one of your talks and tell your
    speakers and volunteers to use them.</p>
</blockquote>
<div style="text-align: right; width: 100%;"><cite>- <a
      href="http://blog.valerieaurora.org/2015/06/23/ban-boring-mike-based-qa-sessions-and-use-index-cards-instead/"
      title="Ban boring mike-based Q&amp;A sessions and use index cards instead | Valerie Aurora">Ban boring mike-based
      Q&amp;A sessions and use index cards instead</a>, by Valerie Aurora, 23-Jun-2015</cite></div>
{% endhighlight %}

...comes out of Ghost looking like this:

{% highlight html linenos %}
<h2 id="index-card-based-question-and-answer-sessions">Index Card-based Question and Answer Sessions</h2>
<blockquote>Here is the formula:</blockquote>
<ol>
  <li>Throw away the audience microphones.</li>
  <li>Buy a pack of index cards.</li>
  <li>Hand out the cards to the audience before or during your talk.</li>
  <li>Ask people to write their questions on the cards and pass them to the end of the row.</li>
  <li>Collect the cards at the end of the talk.</li>
  <li>Flip through the cards and answer only good (or funny) questions.</li>
  <li>Optional: have an accomplice collect and screen the questions for you during the talk.</li>
</ol>
<blockquote>Better yet, if you are a conference organizer, buy enough index cards for every one of your talks and tell
  your speakers and volunteers to use them.</blockquote>
<p>- <a
    href="http://blog.valerieaurora.org/2015/06/23/ban-boring-mike-based-qa-sessions-and-use-index-cards-instead/">Ban
    boring mike-based Q&amp;A sessions and use index cards instead</a>, by Valerie Aurora, 23-Jun-2015</p>
{% endhighlight %}

Problems that I immediately spotted:

1. The &lt;h2&gt; fragment id was replaced, which makes the old links that used it worthless.
1. The ordered list got put outside the blockquote. In fact, I noticed this in other imported issues...multi-paragraph blockquotes got put into individual paragraph blockquotes, and that rendered weirdly.
1. The styling and &lt;cite&gt; tag were discarded.

{% include image.html 
width="700"
src="2024/2024-07-14-thread-entry-comparison.png"
caption="Side-by-side comparison of Ghost (left) with original."
%}

I use all three of these things extensively in almost all of the DLTJ Thursday Thread newsletter issues. So, yeah, stuck. I'm unsure if this is a problem with Ghost's implementation of Lexical or with Lexical itself, but I don't know enough JavaScript to find out. So, I'm abandoning my Ghost effort. For completeness in these notes, here is a web archive of this same newsletter issue ([link to original post](https://dltj.org/article/thursday-threads-2015w25/)).

<script src="/assets/js/replayweb/ui.js"></script>
<replay-web-page 
  replayBase="/assets/js/replayweb/" 
  source="https://media.dltj.org/web-archive/ghost-newsletter-issue.wacz" 
  url="https://newsletter.dltj.org/thursday-threads-2015w25/"
  embed="replay-with-info"
  style="height:35em;">  
</replay-web-page>
<noscript><img
 src="https://dltj.org/assets/images/2023/2023-02-04-tweet-1585816108908662788.png"
 alt="Archived version of a sample issue using the Ghost software.">
</noscript>

By the way, check out my _[ReplayWeb for Embedding Social Media Posts (Twitter, Mastodon) in Web Pages](https://dltj.org/article/replayweb-for-social-media/)_ article to see how that web page archive is embedded in this blog post.