#!/usr/bin/env python3
"""Clean up markdown files exported from Google Docs.

Fixes:
1. Malformed TOC entries: [[Title](#h.xxx)N](#h.xxx) → - [Title](#slug)
2. Stray page numbers from Google Doc TOCs
3. Nested/doubled link patterns
4. #hashtag lines that render as markdown headings
5. Adds proper # Title heading from document name
6. Strips Google Doc internal anchor IDs (#h.xxx, #id.xxx)
"""

import re
import sys
from pathlib import Path


def slugify(text):
    """Convert heading text to a URL-compatible anchor slug."""
    slug = text.lower().strip()
    # Remove special chars except spaces, hyphens, alphanumeric
    slug = re.sub(r'[^\w\s-]', '', slug)
    # Replace whitespace with hyphens
    slug = re.sub(r'\s+', '-', slug)
    # Collapse multiple hyphens
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def fix_toc_entries(content):
    """Fix Google Docs TOC patterns.

    Pattern: [[Title](#h.xxxxx)PageNum](#h.xxxxx)
    Output:  - [Title](#slugified-title)
    """
    # Match the doubled TOC link pattern with page numbers
    # [[text](#h.anchor)digits](#h.anchor)
    def toc_replacer(match):
        title = match.group(1)
        return f'- [{title}](#{slugify(title)})'

    content = re.sub(
        r'\[\[([^\]]+)\]\(#h\.[a-z0-9]+\)\d*\]\(#h\.[a-z0-9]+\)',
        toc_replacer,
        content
    )
    return content


def fix_nested_links(content):
    """Fix nested markdown links [[text](url)text](url) → [text](url)."""
    # Pattern: [[inner](url1)outer](url2) - keep outer url with combined text
    def nested_replacer(match):
        inner_text = match.group(1)
        inner_url = match.group(2)
        outer_text = match.group(3).strip()
        outer_url = match.group(4)
        if outer_text:
            return f'[{inner_text} {outer_text}]({outer_url})'
        return f'[{inner_text}]({outer_url})'

    # Keep applying until no more changes (handles deep nesting)
    prev = None
    while prev != content:
        prev = content
        content = re.sub(
            r'\[\[([^\[\]]+)\]\(([^)]+)\)([^\[\]]*)\]\(([^)]+)\)',
            nested_replacer,
            content
        )
    return content


def fix_hashtag_headings(content):
    """Prevent #hashtag lines from rendering as markdown headings."""
    lines = content.split('\n')
    fixed = []
    for line in lines:
        # Lines starting with # that are hashtags, not headings
        # Headings have # followed by space and text
        # Hashtags have # followed by word chars with no space
        if re.match(r'^#[a-zA-Z]', line) and not re.match(r'^#{1,6}\s', line):
            line = f'Tags: {line.replace("#", "").strip()}'
            # Clean up multiple tag words
            line = re.sub(r'\s+', ', ', line.replace('Tags: ', 'Tags: ', 1))
        fixed.append(line)
    return '\n'.join(fixed)


def fix_google_anchor_refs(content):
    """Remove or replace Google Doc internal anchor references."""
    # Remove standalone (#id.xxx) references
    content = re.sub(r'\(#id\.[a-z0-9]+\)', '', content)
    # Remove (#h.xxx) that aren't part of markdown links
    # But keep [text](#h.xxx) patterns (those are TOC links, handled separately)
    return content


def add_title_heading(content, filename):
    """Add a proper # Title heading if the file doesn't start with one."""
    # Check if file already starts with a heading
    first_line = content.split('\n')[0].strip()
    if first_line.startswith('# '):
        return content

    # Generate title from filename
    name = Path(filename).stem
    # Convert camelCase or hyphens to title case
    title = re.sub(r'[-_]', ' ', name)
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', title)
    title = title.title()

    return f'# {title}\n\n{content}'


def extract_title_from_content(content):
    """Try to extract a meaningful title from the document content."""
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        # Skip empty lines, breadcrumb lines, tag lines
        if not line:
            continue
        if 'jacobcole.net' in line:
            continue
        if line.startswith('Tags:') or line.startswith('#'):
            continue
        if line.startswith('[started by') or line.startswith('Contribute'):
            continue
        if line.startswith('---'):
            continue
        if line.startswith('**Contents**'):
            continue
        if line.startswith('- ['):  # TOC entry
            continue
        # This looks like a title
        # Strip markdown formatting
        clean = re.sub(r'[*_`]', '', line)
        clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean)
        if len(clean) > 3 and len(clean) < 200:
            return clean
    return None


def cleanup_markdown(content, filename=None):
    """Apply all cleanup fixes to markdown content."""
    content = fix_toc_entries(content)
    content = fix_nested_links(content)
    content = fix_hashtag_headings(content)
    content = fix_google_anchor_refs(content)

    if filename:
        content = add_title_heading(content, filename)

    # Clean up excessive blank lines (3+ → 2)
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def process_file(filepath):
    """Process a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    cleaned = cleanup_markdown(original, filepath.name)

    if cleaned != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        return True
    return False


def main():
    dirs = [
        Path('/Users/jacobcole/code/DataExports/markdown-by-hierarchy'),
        Path('/Users/jacobcole/code/DataExports/markdown-new-subdomains'),
        Path('/Users/jacobcole/code/DataExports/markdown-new-missing-docs'),
        Path('/Users/jacobcole/code/DataExports/markdown-by-category'),
    ]

    total = 0
    modified = 0

    for d in dirs:
        if not d.exists():
            print(f"Skipping {d} (not found)")
            continue
        for md_file in sorted(d.rglob('*.md')):
            total += 1
            if process_file(md_file):
                modified += 1
                print(f"  Fixed: {md_file.relative_to(d.parent)}")

    print(f"\nProcessed {total} files, modified {modified}")


if __name__ == '__main__':
    main()
