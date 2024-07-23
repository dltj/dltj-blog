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
