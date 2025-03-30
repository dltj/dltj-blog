"""Functions for the DLTJ blog that are specifit to how that blog operates.
"""

from datetime import datetime, timedelta
from typing import Union

from pelican import generators, signals


def robustlink(
    href: str,
    versiondate: str,
    anchor: str,
    versionurl: str = None,
    originalurl: str = None,
    title: str = None,
) -> str:
    """Output HTML of a robust link

    Args:
        href (str): URL to put in the main anchor tag
        versiondate (str): date-string when the link was made (YYYY-MM-DD)
        anchor (str): text to put inside the <a> anchor tag
        versionurl (str, optional): URL to the archived version of the href. Defaults to None.
        originalurl (str, optional): URL to the original page when href is the archive URL. Defaults to None.
        title (str, optional): string put in the 'title' atribute of the anchor tag. Defaults to None.

    Returns:
        str: HTML fragment
    """
    output: str = f'<a href="{ href }" '
    if versionurl:
        output += f'data-versionurl="{versionurl}" '
    if originalurl:
        output += f'data-originalurl="{originalurl}" '
    output += f'data-versiondate="{versiondate}" '
    if title:
        output += f'title="{title}" '
    output += f">{anchor}</a>"
    return output


def image(
    fig_class: str = None,
    div_float: str = None,
    width: str = None,
    localsrc: str = None,
    abssrc: str = None,
    caption: str = None,
    alt: str = None,
    ahref: str = None,
    localhref: str = None,
    picclass: str = None,
    imgclass: str = None,
) -> str:
    """Output HTML of an image inside a <figure> tag

    Args:
        fig_class (str, optional): Class(es) to add to the surrounding figure tag.
        div_float (str, optional): Float the figure 'left' or 'right'. Defaults to None.
        width (str, optional): width of the figure tag. Defaults to None.
        localsrc (str, optional): path to image file relative to `assets/images/`. Defaults to None.
        abssrc (str, optional): absolue URL to image file. Defaults to None.
        caption (str, optional): text placed below image. Defaults to None.
        alt (str, optional): alternative text for the image. Defaults to None.
        ahref (str, optional): absolute URL of an <a> tag around image. Defaults to None.
        localhref (str, optional): path of <a> tag relative to blog root. Defaults to None.

    Returns:
        str: HTML fragment
    """
    alt = alt or ""
    if abssrc:
        img_path = abssrc
    else:
        img_path = f"https://dltj.org/assets/images/{localsrc}"
    output: str = "<figure "
    if fig_class:
        output += f'class="{fig_class}" '
    elif div_float:
        output += f'class="image-{div_float}" '
    if width:
        output += f'style="width:{width}px" '
    output += ">"
    if ahref:
        output = f'<a href="{ahref}">'
    elif localhref:
        output = f'<a href="{localhref}">'
    output += "<picture>"
    if picclass:
        output += f'<source class="{picclass}" src="{img_path}"></source>'
    output += "<img "
    if width:
        output += f'width="{width}" '
    if imgclass:
        output += f'class="{imgclass}" '
    output += f'src="{img_path}" '
    output += f'alt="{alt}">'
    output += "</picture>"
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
    """Output HTML of a captioned page element

    Args:
        div_float (str, optional): Float the figure 'left' or 'right'. Defaults to None.
        width (str, optional): width of the figure tag. Defaults to None.
        caption (str, optional): text placed below the figure. Defaults to None.
        contents (str, optional): contents of the <figure> tag. Defaults to None.

    Returns:
        str: HTML fragment
    """
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


def thursday_threads_header() -> str:
    """Output the Thursday Threads header"""
    return """
Feel free to send this newsletter to others you think might be interested in the topics.  If you are not already subscribed to <i>DLTJ's Thursday Threads</i>, visit the <a href="https://newsletter.dltj.org/" title="DLTJ Thursday Threads Newsletter Signup">sign-up page</a>.
If you would like a more raw and immediate version of these types of stories, <a target="_blank" href="https://code4lib.social/@dltj">follow me on <span style="background-image: url('https://dltj.org/assets/images/mastodon_16.png'); background-repeat: no-repeat; padding-left: 18px;">Mastodon</span></a> where I post the bookmarks I save.  Comments and tips, as always, are welcome.
"""


def thursday_threads_quote(
    href: str,
    blockquote: str,
    anchor: str,
    versiondate: str = None,
    versionurl: str = None,
    originalurl: str = None,
    title: str = None,
    pre: str = None,
    post: str = None,
) -> str:
    """Output HTML of a blockquote and a citation

    Args:
        href (str): Citation link.
        blockquote (str): Contents of the quote.
        anchor (str): Text inside the anchor
        versiondate (str, optional): date-string when the link was made (YYYY-MM-DD)
        versionurl (str, optional): URL to the archived version of the href. Defaults to None.
        originalurl (str, optional): URL to the original page when href is the archive URL. Defaults to None.
        title (str, optional): string put in the 'title' atribute of the anchor tag. Defaults to None.
        pre (str, optional): Any text before the citation anchor
        pre (str, optional): Any text after the citation anchor

    Returns:
        str: HTML fragment
    """
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
  <figcaption>&mdash;{ pre or '' }{ source }{ post or '' }</figcaption>
</figure>
"""


def note(note_text: str = None) -> str:
    """Wrap text of a note with the appropriate class attributes

    Args:
        note_text (str, optional): string to insert into the note. Defaults to None.

    Returns:
        str: _description_
    """
    return f'<p class="dltj-note"><strong>Note!</strong> {note_text}</p>'


def remove_recent_last_modified(generator: generators.ArticlesGenerator) -> None:
    """Remove last modified attribute for articles modified shortly after publication

    Args:
        generator (Generator): Pelican generator
    """
    for article in generator.articles:
        if hasattr(article, "modified"):
            modified: Union[datetime, str] = article.modified
            date: Union[datetime, str] = article.date

            # Convert from string to datetime if needed
            if isinstance(modified, str):
                modified = datetime.strptime(modified, "%Y-%m-%d %H:%M")
            if isinstance(date, str):
                date = datetime.strptime(date, "%Y-%m-%d %H:%M")

            # Remove 'modified' attribute if modified within 2 days of posting
            if isinstance(modified, datetime) and isinstance(date, datetime):
                if modified - date <= timedelta(days=2):
                    delattr(article, "modified")  # Remove 'modified' if within 2 days


def register() -> None:
    """Register Pelican signals for this plugin"""
    signals.article_generator_pretaxonomy.connect(remove_recent_last_modified)
