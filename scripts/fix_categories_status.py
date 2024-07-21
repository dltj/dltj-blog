#!/usr/bin/env python3
#

import os

posts = []
for dirpath, dirnames, files in os.walk("content"):
    for file_name in files:
        if file_name.endswith("markdown") or file_name.endswith("md"):
            dashes_seen = False
            categories_seen = False
            category_line = 0
            categories = []
            with open(f"{dirpath}/{file_name}", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("---") and not dashes_seen:
                        dashes_seen = True
                        continue
                    if line.startswith("categories:"):
                        category_line = i
                        if len(line) > 13:
                            category = line.strip()[12:]
                        categories_seen = True
                        continue
                    if categories_seen and line.startswith("-"):
                        categories.append(line.strip()[2:])
                        continue
                    if categories_seen:
                        categories_seen = False

                    if line.startswith("status: publish"):
                        lines[i] = "status: published\n"
                        continue

                    if line.startswith("---") and dashes_seen:
                        dashes_seen = False
                        if len(categories) > 1:
                            print(
                                f"{file_name} has more than one category: {','.join(categories)}"
                            )
                            continue
                        elif len(categories) == 1:
                            category = categories[0]
                        if category in [
                            "Fedora",
                            "DRC",
                            "Library SOA",
                            "Unified Content Repository",
                        ]:
                            category = "Library Technology"
                        lines.insert(category_line, f"category: {category}\n")

            with open(f"{dirpath}/{file_name}", "w", encoding="utf-8") as file:
                file.writelines(lines)

            ## This uses [Python Frontmatter](https://python-frontmatter.readthedocs.io/en/latest/),
            ## which unfortunately changes the order of the YAML keys.
            # post = frontmatter.load(f"{dirpath}/{file_name}")
            # if 'categories' in post:
            #     if isinstance(post['categories'], list) and len(post['categories']) > 1:
            #         print(f"Post {file_name} has categories {",".join(post['categories'])}")
            #     elif isinstance(post['categories'], list) and len(post['categories']) == 1:
            #         post['category'] = post['categories'][0]
            #     else:
            #         post['category'] = post['categories']

            # if 'status' in post and post['status'] == 'publish':
            #     post['status'] = 'published'

            # with open(f"{dirpath}/{file_name}", "wb") as file:
            #     frontmatter.dump(post, file)
