#!/usr/bin/env python3
#

import os
import re

# {% include robustlink.html href="http://fedora.info/" versiondate="2006-04-10" title="Fedora" anchor="FEDORA Digital Object Repository" %}

_ROBUSTLINKS = re.compile(
    r"""
    \{%(\s+)?include\s+robustlink.html\s+
    href=\"([^\"]+)\"\s+
    versionurl=\"([^\"]*)\"\s+
    versiondate=\"([^\"]*)\"\s+
    title=\"([^\"]*)\"\s+
    anchor=\"([^\"]+)\"\s+%\}""",
    re.X,
)


posts = []
for dirpath, dirnames, files in os.walk("content"):
    for file_name in files:
        if file_name.endswith("md") or file_name.endswith("markdown"):
            with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if _ROBUSTLINKS.search(line):
                        s = _ROBUSTLINKS.sub(
                            '{{ robustlink(href="'
                            + r"\2"
                            + '", versionurl="'
                            + r"\3"
                            + '", versiondate="'
                            + r"\4"
                            + '", title="'
                            + r"\5"
                            + '", anchor="'
                            + r"\6"
                            + '") }}',
                            line,
                        )
                        lines[i] = s

            with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                file.writelines(lines)
