#!/usr/bin/env python3
"""Extract breadcrumb hierarchy from Google Docs HTML exports.

Each doc has breadcrumbs at the top like:
  <a>systematicawesome.jacobcole.net</a> > <a>foodslist.jacobcole.net</a> > <a>chocolate.jacobcole.net</a>

These are in the first <p> element of the <body>.
"""

import re
import json
from pathlib import Path
from html.parser import HTMLParser
from collections import defaultdict

HTML_DIR = Path(__file__).parent / "html"


class FirstParagraphExtractor(HTMLParser):
    """Extract link text from the first paragraph (breadcrumb)."""

    def __init__(self):
        super().__init__()
        self.in_body = False
        self.in_first_p = False
        self.first_p_done = False
        self.in_style = False
        self.in_head = False
        self.link_texts = []
        self.current_text = ""
        self.p_count = 0

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.in_body = True
        elif tag == "head":
            self.in_head = True
        elif tag == "style":
            self.in_style = True
        elif tag == "p" and self.in_body and not self.first_p_done:
            self.p_count += 1
            if self.p_count == 1:
                self.in_first_p = True

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False
        elif tag == "style":
            self.in_style = False
        elif tag == "p" and self.in_first_p:
            self.in_first_p = False
            self.first_p_done = True

    def handle_data(self, data):
        if self.in_style or self.in_head:
            return
        if self.in_first_p:
            self.current_text += data


def extract_breadcrumb_from_text(text):
    """Parse breadcrumb text like 'systematicawesome.jacobcole.net > foodslist.jacobcole.net > chocolate.jacobcole.net'"""
    # Find all subdomain.jacobcole.net references
    subdomains = re.findall(r'(\w+)\.jacobcole\.net', text)
    # Also check for other domains
    other = re.findall(r'(\w+)\.(?:connectr\.site|connectordocs\.com)', text)

    # Deduplicate keeping order
    seen = []
    for s in subdomains:
        sl = s.lower()
        if sl not in seen and sl not in ('www', 'jacob'):
            seen.append(sl)

    return seen


def main():
    html_files = sorted(HTML_DIR.glob("*.html"))

    breadcrumbs = {}

    for html_file in html_files:
        if html_file.name.endswith(".json"):
            continue

        stem = html_file.stem
        try:
            content = html_file.read_text(encoding="utf-8")

            # Decode HTML entities first
            content_decoded = content.replace("&amp;", "&")

            # Method: extract from first paragraph text
            parser = FirstParagraphExtractor()
            parser.feed(content_decoded)

            first_p_text = parser.current_text.strip()

            # Extract subdomains from the first paragraph
            crumbs = extract_breadcrumb_from_text(first_p_text)

            if not crumbs:
                # Fallback: look for jacobcole.net in the first <p> via regex on raw HTML
                # Find the first <p>...</p> in the body
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content_decoded, re.DOTALL)
                if body_match:
                    body = body_match.group(1)
                    first_p = re.search(r'<p[^>]*>(.*?)</p>', body, re.DOTALL)
                    if first_p:
                        p_content = first_p.group(1)
                        # Extract subdomains from link text or hrefs
                        crumbs_from_href = re.findall(r'(\w+)\.jacobcole\.net', p_content)
                        seen = []
                        for s in crumbs_from_href:
                            sl = s.lower()
                            if sl not in seen and sl not in ('www', 'jacob'):
                                seen.append(sl)
                        crumbs = seen

            if crumbs:
                breadcrumbs[stem] = crumbs

        except Exception as e:
            print(f"ERROR: {stem}: {e}")

    # Build parent-child from breadcrumbs
    hierarchy = {}  # child -> parent path
    for stem, crumbs in breadcrumbs.items():
        # Find this file in the breadcrumb trail
        stem_lower = stem.lower()
        for i, c in enumerate(crumbs):
            if c == stem_lower:
                if i > 0:
                    hierarchy[stem] = crumbs[:i+1]  # full path
                break
        else:
            # Not found by name match - use full path as-is
            hierarchy[stem] = crumbs

    # Print all breadcrumbs sorted by path depth then alpha
    print("=== All Breadcrumb Paths ===\n")
    sorted_items = sorted(breadcrumbs.items(), key=lambda x: (len(x[1]), x[0]))
    for stem, crumbs in sorted_items:
        print(f"  {' > '.join(crumbs)}")

    # Build tree
    print("\n=== Full Hierarchy Tree ===\n")

    children = defaultdict(set)
    all_paths = {}

    for stem, crumbs in breadcrumbs.items():
        all_paths[stem] = crumbs
        for i in range(len(crumbs) - 1):
            children[crumbs[i]].add(crumbs[i + 1])

    # Find roots
    all_child_nodes = set()
    for v in children.values():
        all_child_nodes.update(v)
    all_parent_nodes = set(children.keys())
    roots = all_parent_nodes - all_child_nodes

    # Also add nodes that appear only as roots in breadcrumbs
    for stem, crumbs in breadcrumbs.items():
        if crumbs[0] not in all_child_nodes:
            roots.add(crumbs[0])

    def print_tree(node, indent=0, visited=None):
        if visited is None:
            visited = set()
        if node in visited:
            return
        visited.add(node)

        prefix = "│   " * (indent - 1) + "├── " if indent > 0 else ""
        print(f"{prefix}{node}")
        for child in sorted(children.get(node, [])):
            print_tree(child, indent + 1, visited)

    for root in sorted(roots):
        print_tree(root)
        print()

    # Find files with no breadcrumb
    all_stems = {f.stem for f in html_files if not f.name.endswith(".json")}
    no_breadcrumb = all_stems - set(breadcrumbs.keys())
    if no_breadcrumb:
        print("=== Files with no breadcrumb found ===\n")
        for s in sorted(no_breadcrumb):
            print(f"  {s}")

    # Save full data
    output = {
        "breadcrumbs": {k: v for k, v in sorted(breadcrumbs.items())},
        "children": {k: sorted(v) for k, v in children.items()},
        "roots": sorted(roots),
    }
    out_path = Path(__file__).parent / "hierarchy.json"
    out_path.write_text(json.dumps(output, indent=2))
    print(f"\nSaved hierarchy to {out_path}")


if __name__ == "__main__":
    main()
