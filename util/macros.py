def robustlink(
    href: str,
    versiondate: str,
    anchor: str,
    versionurl: str = None,
    originalurl: str = None,
    title: str = None,
) -> str:
    output: str = f'<a href="{ href }" '
    if versionurl:
        output += f'data-version-url="{versionurl}" '
    if originalurl:
        output += f'data-originalurl="{originalurl}" '
    output += f'data-versiondate="{versiondate}" '
    if title:
        output += f'title="{title}" '
    output += f">{anchor}</a>"
    return output


# <!-- For handling https://robustlinks.mementoweb.org/ --><a href="{{ include.href }}" {% if include.versionurl %}data-versionurl="{{ include.versionurl }}"{% endif%}{% if include.originalurl %}data-originalurl="{{ include.originalurl }}"{% endif%} data-versiondate="{{ include.versiondate }}"{% if include.title %} title="{{ include.title }}"{% endif%}>{{ include.anchor }}</a>


def image(
    div_float: str = None,
    width: str = None,
    localsrc: str = None,
    abssrc: str = None,
    caption: str = None,
    alt: str = None,
    ahref: str = None,
    localhref: str = None,
) -> str:
    alt = alt or ""
    output: str = "<figure "
    if div_float:
        output += f'class="align-{div_float}" '
    if width:
        output += f'style="width:{width}px" '
    output += ">"
    if ahref or localhref:
        output = f'<a href="{ahref}{localhref}">'
    output += "<img "
    if width:
        output += f'width="{width}" '
    if abssrc:
        output += f'src="{abssrc}" '
    else:
        output += f'src="/assets/images/{localsrc}" '
    output += f'alt="{alt}">'
    if ahref or localhref:
        output += "</a>"
    if caption:
        output += f"<figcaption>{caption}</figcaption>"
    output += "</figure>"
    return output


def captioned(
    div_float: str = None,
    width: str = None,
    caption: str = None,
    contents: str = None,
) -> str:
    output: str = "<figure "
    if div_float:
        output += f'class="align-{div_float}" '
    if width:
        output += f'style="width:{width}px" '
    output += ">"
    output += contents
    if caption:
        output += f"<figcaption>{caption}</figcaption>"
    output += "</figure>"
    return output


# <!-- _based on https://stackoverflow.com/a/51682829 s/(  \s*)/\n\1/g to restore template spacing--><figure{%if include.float %} class="align-{{ include.float }}" {% endif %}{%if include.width %} style="width:{{ include.width }}px" {% endif %}>
#     {% if include.url %}
#     <a href="{{ include.url }}">
#     {% endif %}
#     {% if include.wpurl %}
#     <a href="{{ site.url }}/wp-content/uploads/{{ include.wpurl }}">
#     {% endif %}
#     <img
#         {% if include.width %}
#             width="{{ include.width }}"
#         {% endif %}
#         {% if include.srcabs %}
#             src="{{ include.srcabs }}"
#         {% elsif include.wpsrc %}
#             src="{{ site.url }}/wp-content/uploads/{{ include.wpsrc }}"
#         {% else %}
#             src="{{ site.url }}/assets/images/{{ include.src }}"
#         {% endif %}
#     alt="{{ include.alt }}">
#     {% if include.url or include.wpurl %}
#     </a>
#     {% endif %}
#     {% if include.caption %}
#         <figcaption>{{ include.caption }}</figcaption>
#     {% endif %}  </figure>


def thursday_threads_header():
    return """
Feel free to send this newsletter to others you think might be interested in the topics.  If you are not already subscribed to <i>DLTJ's Thursday Threads</i>, visit the <a href="https://newsletter.dltj.org/" title="DLTJ Thursday Threads Newsletter Signup">sign-up page</a>.
If you would like a more raw and immediate version of these types of stories, <a target="_blank" href="https://code4lib.social/@dltj">follow me on <span style="background-image: url('https://dltj.org/assets/images/mastodon_16.png'); background-repeat: no-repeat; padding-left: 18px;">Mastodon</span></a> where I post the bookmarks I save.  Comments and tips, as always, are welcome.
"""


def thursday_threads_quote(
    href: str = None,
    blockquote: str = None,
    versiondate: str = None,
    versionurl: str = None,
    originalurl: str = None,
    title: str = None,
    pre: str = None,
    anchor: str = None,
    post: str = None,
):
    if href:
        source = f'<a href="{href}"'
        source += "" if versionurl is None else f' data-versionurl="{versionurl}"'
        source += "" if originalurl is None else f' data-originalurl="{originalurl}"'
        source += "" if versiondate is None else f' data-versiondate="{versiondate}"'
        source += "" if title is None else f' title="{title}"'
        source += f">{anchor}</a>"
    else:
        source = anchor

    return f"""
<figure class="quote thursdaythread">
  <blockquote>
{ blockquote }
  </blockquote>
  <figcaption>&mdash;{ pre }{ anchor }{ post }</figcaption>
</figure>
"""


def note(note_text: str = None) -> str:
    return f'<p class="dltj-note"><strong>Note!</strong> {note_text}</p>'
