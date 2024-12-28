import os
import re
import subprocess
from datetime import datetime, timezone
from typing import Optional

import yaml


def get_last_non_meta_commit_date(file_path: str) -> Optional[str]:
    """Get the most recent commit date with a message not starting with 'META'."""
    try:
        # Use git log to list all commits affecting the file, with date and message
        result = subprocess.run(
            ["git", "log", "--format=%ci%n%s%n", "--follow", file_path],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        )

        # Split the output by commit (every second item is a commit, preceded by a newline)
        commits = result.stdout.strip().split("\n\n")

        # Iterate through the commits to find the last one without a "META" prefix in the message
        for commit in commits:
            lines = commit.split("\n", 1)
            commit_date = lines[0].strip()
            commit_message = lines[1].strip() if len(lines) > 1 else ""

            if not commit_message.startswith("META"):
                return commit_date

    except subprocess.CalledProcessError:
        print(f"Error: Unable to retrieve commit details for {file_path}")
        return None


def update_modified_date(file_path: str) -> None:
    """Update the modified date in the file's frontmatter."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Match frontmatter block between lines with three dashes (---)
    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not frontmatter_match:
        print(f"No frontmatter found in {file_path}")
        return

    frontmatter_content = frontmatter_match.group(1)
    frontmatter = yaml.safe_load(frontmatter_content)

    # Get the last non-META commit date
    last_commit_date = get_last_non_meta_commit_date(file_path)
    if not last_commit_date:
        return

    # Check if the commit date is after January 1, 2018
    cut_off_date = datetime(2018, 1, 1, tzinfo=timezone.utc)
    commit_date = datetime.strptime(last_commit_date, "%Y-%m-%d %H:%M:%S %z")

    if commit_date > cut_off_date:
        # Update the 'modified' field
        frontmatter["modified"] = commit_date.strftime("%Y-%m-%dT%H:%M:%S%z")
        frontmatter["modified"] = (
            frontmatter["modified"][:-2] + ":" + frontmatter["modified"][-2:]
        )

        # Reconstruct the file content with updated frontmatter
        updated_frontmatter = yaml.safe_dump(frontmatter, sort_keys=False, width=1000)
        updated_content = (
            f"---\n{updated_frontmatter}---\n" + content[frontmatter_match.end() :]
        )

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print(f"Updated modified date for {file_path}")
    else:
        print(f"Skipped modifying {file_path}; commit date is before cutoff.")


def process_markdown_files(directory: str) -> None:
    """Process all Markdown files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                update_modified_date(file_path)


if __name__ == "__main__":
    directory_to_process = "./content"  # Adjust this path as needed
    process_markdown_files(directory_to_process)
