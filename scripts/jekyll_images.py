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
\{%\s+include\s+image.html\s+       # include definition
(float="([^"]+)"\s+)?                # optional float in $2
(width="([^"]+)"\s+)?                # optional width in $4
(src="([^"]+)"\s+)?                  # optional src in $6
(srcabs="([^"]+)"\s+)?               # optional srcabs in $8
(caption="([^"]+)"\s+)?              # optional caption in $10
(alt="([^"]+)"\s+)?                  # optional alt text in $12
%\}
"""

pattern2 = r"""
\{%\s+include\s+image.html\s+       # include definition
(float="([^"]+)"\s+)?                # optional float in $2
(url="([^"]+)"\s+)?                  # optional anchor href in $4
(width="([^"]+)"\s+)?                # optional width in $6
(srcabs="([^"]+)"\s+)?               # optional srcabs in $8
(src="([^"]+)"\s+)?                  # optional wpsrc in $10
(alt="([^"]*)"\s+)?                  # optional alt text in $12
(caption="([^"]+)"\s+)?              # optional caption in $14
(wpurl="([^"]+)"\s+)?                  # optional wpurl in $16
%\}
"""

_IMAGES1 = re.compile(pattern1, flags=re.X | re.DOTALL)
_IMAGES2 = re.compile(pattern2, flags=re.X | re.DOTALL)


posts = []
for dirpath, dirnames, files in os.walk("content"):
    for file_name in files:
        if file_name.endswith("md") or file_name.endswith("markdown"):
            with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                lines = file.read()
                lines = _IMAGES2.sub(
                    '{{ image(float="'
                    + r"\2"
                    + '", width="'
                    + r"\6"
                    + '", localsrc="'
                    + r"\10"
                    + '", abssrc="'
                    + r"\8"
                    + '", caption="'
                    + r"\14"
                    + '", alt="'
                    + r"\12"
                    + '", ahref="'
                    + r"\4"
                    + '", localhref="'
                    + r"\16"
                    + '") }}',
                    lines,
                )

            with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                file.write(lines)
