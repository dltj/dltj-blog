#!/usr/bin/env python3
#

import os
import re

# {% include image.html
# float="right"
# width="400"
# src="2024/2024-06-21-folio-saml-config.png"
# caption="The FOLIO Settings → Tenant → SSO settings pane"
# alt="Screen capture of the SSO settings pane. It contains four fields: Identity Provider URL, SAML binding, SAML attribute, and User property. There is also a button labeled 'Download metadata'"
# %}
# {% include image.html
# float="left|right"
# url="href for anchor"
# width=""
# src="source relative to /assets/images/"
# srcabs="absolute-url-to-source"
# caption=""
# %}

pattern1 = r"""
\{%\s+include\s+note.html\s+       # include definition
notetext='([^']+)'\s+         # note text $1
"""

_NOTE = re.compile(pattern1, flags=re.X | re.DOTALL)


posts = []
for dirpath, dirnames, files in os.walk("content"):
    for file_name in files:
        if file_name.endswith("md") or file_name.endswith("markdown"):
            with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                lines = file.read()
                lines = _NOTE.sub(
                    "{{ note(note_text='" + r"\1" + "') }}",
                    lines,
                )

            with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                file.write(lines)
