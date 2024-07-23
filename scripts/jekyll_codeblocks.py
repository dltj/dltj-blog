#!/usr/bin/env python3
#

import os
import re

_HI_START = re.compile(r"\{%(\s+)?highlight\s+([^\s]+).+%\}")
_HI_END = re.compile(r"{%(\s+)?endhighlight(\s+)?%}")


posts = []
for dirpath, dirnames, files in os.walk("content"):
    for file_name in files:
        if file_name.endswith("md"):
            with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if _HI_START.search(line):
                        s = _HI_START.sub("```" + r"\2", line)
                        lines[i] = s
                    elif _HI_END.search(line):
                        lines[i] = "```\n"

            with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                file.writelines(lines)
