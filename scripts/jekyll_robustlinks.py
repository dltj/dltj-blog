#!/usr/bin/env python3
#

import os
import re

# {% include robustlink.html href="https://www.courtlistener.com/docket/67801014/hachette-book-group-inc-v-internet-archive/?order_by=desc" versionurl="https://web.archive.org/web/20240706193105/https://www.courtlistener.com/docket/67801014/hachette-book-group-inc-v-internet-archive/?order_by=desc" versiondate="2024-07-06" title=" Hachette Book Group, Inc. v. Internet Archive (23-1260) | Court of Appeals for the Second Circuit via CourtListener" anchor="Hachette Book Group, Inc. v. Internet Archive case" %}

_ROBUSTLINKS = re.compile(
    r"\{%(\s+)?include\s+robustlink.html\s+href=\"([^\"]+)\"\s+versionurl=\"([^\"]*)\"\s+versiondate=\"([^\"]*)\"\s+title=\"([^\"]*)\"\s+anchor=\"([^\"]+)\"\s+%\}"
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
