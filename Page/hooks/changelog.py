from pathlib import Path
from re import sub, MULTILINE

def generate_changelog_page(config):
    input_file = Path("../Changelog.md")
    output_file = Path("docs/changelog/index.md")

    # Read the original changelog file
    with input_file.open('r', encoding='utf-8') as f:
        content = f.read()

    # Convert Hotfix lines (e.g. 1.1.1) to ### headers
    processed_content = sub(r'^(\d+\.\d+\.\d+.*?)$', r'### \1', content, flags=MULTILINE)
    # Convert Changelog lines (e.g. 1.1) to ## headers
    processed_content = sub(r'^(\d+\.\d+.*?)$', r'## \1', processed_content, flags=MULTILINE)

    # Check if the output file exists, and read its current content
    if output_file.exists():
        with output_file.open('r', encoding='utf-8') as f:
            existing_content = f.read()
    else:
        existing_content = ""

    # Only write the new file if content has changed to avoid unnecessary rebuilds
    if processed_content != existing_content:
        with output_file.open('w', encoding='utf-8') as f:
            f.write(processed_content)
        print("INFO    -  Generated changelog page successfully (updated).")
    else:
        print("INFO    -  Changelog page is up to date. No changes made.")
