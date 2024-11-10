#!/usr/bin/env python3
#

import json
import os
import re
from datetime import datetime

from git import Repo
from pytz import UTC, timezone

gmt_pattern = r"date_gmt: '(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) -\d{4}'"

repo = Repo(".")

posts = []
for dirpath, dirnames, files in os.walk("content"):
    for file_name in files:
        if file_name.endswith("markdown"):
            with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("title:"):
                        title_string = line[7:].strip().strip("'")
                        lines[i] = f"title: '{title_string.replace("'","''")}'\n"
                        break

            with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                file.writelines(lines)
