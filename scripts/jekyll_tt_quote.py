#!/usr/bin/env python3
#

import os
import re

# {% include thursday-threads-quote.html
# blockquote='What happens when an industry concerned with the production of culture is beholden to a company with the sole goal of underselling competitors? Amazon is indisputably the king of books, but the issue remains, as Charlie Winton, CEO of the independent publisher Counterpoint Press puts it, &ldquo;what kind of king they&rsquo;re going to be.&rdquo; A vital publishing industry must be able take chances with new authors and with books that don&rsquo;t have obvious mass-market appeal. When mega-retailers have all the power in the industry, consumers benefit from low prices, but the effect on the future of literature&mdash;on what books can be published successfully&mdash;is far more in doubt.'
# href="http://www.bostonreview.net/roychoudhuri-books-after-amazon"
# versiondate="2011-12-30"
# anchor="Books After Amazon"
# post=', Onnesha Roychoudhuri, 1-Nov-2011'
# %}

pattern1 = r"""
\{%\s+include\s+thursday-threads-quote.html\s+       # include definition
blockquote='([^']+)'\s+         # blockquote $1
href='([^']+)'\s+               # href $2
(versiondate='([^']+)'\s+)?        # versiondate $4
(versionurl='([^']+)'\s+)?         # versionurl $6
(title='([^']+)'\s+)?              # title $8
(pre='([^']+)'\s+)?                 # prefix text $10
anchor='([^']+)'\s+             # anchor $11
(post='([^']+)'\s+)?               # post $13
%\}
"""

_TT_QUOTE = re.compile(pattern1, flags=re.X | re.DOTALL)


posts = []
for dirpath, dirnames, files in os.walk("content"):
    for file_name in files:
        if file_name.endswith("md") or file_name.endswith("markdown"):
            with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                lines = file.read()
                lines = _TT_QUOTE.sub(
                    '{{ thursday_threads_quote(href="'
                    + r"\2"
                    + "\",\n blockquote='"
                    + r"\1"
                    + "',\n versiondate=\""
                    + r"\4"
                    + '",\n versionurl="'
                    + r"\6"
                    + '",\n title="'
                    + r"\8"
                    + '",\n pre="'
                    + r"\10"
                    + '",\n anchor="'
                    + r"\11"
                    + "\",\n post='"
                    + r"\13"
                    + "') }}",
                    lines,
                )

            with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                file.write(lines)
