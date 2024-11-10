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
for dirpath, dirnames, files in os.walk("_posts"):
    for file_name in files:
        if file_name.endswith(".html"):
            with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                lines = file.readlines()

            title_line = 0
            just_after_title_line = False
            for i, line in enumerate(lines):
                if just_after_title_line and line.startswith(" "):
                    lines[title_line] = lines[title_line].rstrip() + " " + line.lstrip()
                    del lines[i]
                else:
                    just_after_title_line = False
                if line.startswith("title:"):
                    title_line = i
                    just_after_title_line = True
                if line.startswith("date:"):
                    full_title = lines[title_line][7:].strip()
                    if full_title.startswith('"') and full_title.endswith('"'):
                        full_title = full_title.strip('"')
                    if full_title.startswith("'") and full_title.endswith("'"):
                        full_title = full_title.strip("'")
                    full_title = full_title.replace("''", "'").replace('""', '"')
                    lines[title_line] = f"title: {full_title.strip()}\n"
                    wp_date = line[7:32]
                    committed_datetime = datetime.strptime(
                        wp_date, "%Y-%m-%d %H:%M:%S %z"
                    ).astimezone(UTC)
                    lines.insert(
                        title_line + 1, f"modified: {committed_datetime.isoformat()}\n"
                    )
                    title_line = 0
                    break

            with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                file.writelines(lines)

        if file_name.endswith(".md") or file_name.endswith(".markdown"):
            commits = repo.iter_commits(paths=f"{dirpath}/{file_name}")
            committed_datetime = None
            for commit in commits:
                if commit.message.startswith("META"):
                    continue
                committed_datetime = commit.committed_datetime
                authored_datetime = datetime.strptime(
                    file_name[:10], "%Y-%m-%d"
                ).replace(tzinfo=UTC)

            if committed_datetime:
                with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                    lines = file.readlines()

                for i, line in enumerate(lines):
                    if line.startswith("title:"):
                        full_title = lines[i][7:].strip()
                        if full_title.startswith('"') and full_title.endswith('"'):
                            full_title = full_title.strip('"')
                        if full_title.startswith("'") and full_title.endswith("'"):
                            full_title = full_title.strip("'")
                        full_title = full_title.replace("''", "'").replace('""', '"')
                        lines[i] = f"title: {full_title.strip()}\n"
                        lines.insert(
                            i + 1, f"modified: {committed_datetime.isoformat()}\n"
                        )
                        break

                with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                    file.writelines(lines)

        # combined_line = ""
        # remainder = None
        # title = None
        # for raw_line in f:
        #     if remainder is None:
        #         if raw_line.startswith(
        #             " "
        #         ):  # Leading space indicates continuation
        #             combined_line += f" {raw_line.lstrip()}"
        #             continue

        #         line = combined_line.strip()
        #         combined_line = raw_line.rstrip()

        #         if line.startswith("title"):
        #             title = line[7:].strip("'").replace("''", "'")
        #             # print(f"{title=}")
        #         if line.startswith("date_gmt"):
        #             match = re.search(gmt_pattern, line)
        #             if match:
        #                 pub_date = f"{match.group(1)}T{match.group(2)}.000Z"
        #                 # print(f"{pub_date=}")
        #             else:
        #                 print(f"Proper date not found in {file_name}")
        #         if line == "---":
        #             if title is None:  # Skip the first line of dashes
        #                 continue
        #             remainder = combined_line
        #     else:
        #         remainder += raw_line

        # soup = BeautifulSoup(remainder, "html.parser")

        # # Remove Feedburner sign-up
        # nodes_to_remove = soup.find_all(
        #     id=lambda x: x and x.startswith("feedburner-thursday-threads")
        # )
        # for node in nodes_to_remove:
        #     node.decompose()

        # post_html = str(soup)
