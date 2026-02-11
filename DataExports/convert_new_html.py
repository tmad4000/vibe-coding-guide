#!/usr/bin/env python3
"""Convert HTML files from html-new/ and missing-docs-html/ to clean Markdown.

Reuses the GoogleDocHTMLToMarkdown parser from the original converter.
Outputs:
  html-new/          -> markdown-new-subdomains/
  missing-docs-html/ -> markdown-new-missing-docs/
"""

import os
import re
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Input -> Output directory pairs
CONVERSIONS = [
    (BASE_DIR / "html-new", BASE_DIR / "markdown-new-subdomains"),
    (BASE_DIR / "missing-docs-html", BASE_DIR / "markdown-new-missing-docs"),
]


def _extract_real_url(google_url: str) -> str:
    """Extract the real destination URL from a Google redirect URL."""
    try:
        parsed = urllib.parse.urlparse(google_url)
        params = urllib.parse.parse_qs(parsed.query)
        if "q" in params:
            return params["q"][0]
        if "url" in params:
            return params["url"][0]
    except Exception:
        pass
    return google_url


def _clean_google_redirects(text: str) -> str:
    """Replace any remaining Google redirect URLs in markdown text with the real URLs."""
    # Match Google redirect URLs (both http and https, www. optional)
    pattern = r'https?://(?:www\.)?google\.com/url\?[^\s\)\]>]+'

    def replacer(match):
        return _extract_real_url(match.group(0))

    return re.sub(pattern, replacer, text)


class GoogleDocHTMLToMarkdown(HTMLParser):
    """Convert Google Docs HTML to clean Markdown."""

    def __init__(self):
        super().__init__()
        self.output = []
        self.current_text = ""
        self.tag_stack = []
        self.in_style = False
        self.in_head = False
        self.list_depth = 0
        self.href = None
        self.skip_content = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.tag_stack.append(tag)

        if tag == "head":
            self.in_head = True
        elif tag == "style":
            self.in_style = True
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._flush_text()
            level = int(tag[1])
            self.output.append(f"\n{'#' * level} ")
        elif tag == "p":
            self._flush_text()
        elif tag == "br":
            self.current_text += "\n"
        elif tag == "a":
            self.href = attrs_dict.get("href", "")
            # Clean Google redirect URLs
            if self.href and "google.com/url" in self.href:
                parsed = urllib.parse.urlparse(self.href)
                params = urllib.parse.parse_qs(parsed.query)
                if "q" in params:
                    self.href = params["q"][0]
        elif tag in ("ul", "ol"):
            self._flush_text()
            self.list_depth += 1
        elif tag == "li":
            self._flush_text()
            indent = "  " * (self.list_depth - 1)
            self.output.append(f"{indent}- ")
        elif tag in ("b", "strong"):
            self.current_text += "**"
        elif tag in ("i", "em"):
            self.current_text += "*"
        elif tag == "span":
            pass  # Just pass through span content

    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()

        if tag == "head":
            self.in_head = False
        elif tag == "style":
            self.in_style = False
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._flush_text()
            self.output.append("\n")
        elif tag == "p":
            self._flush_text()
            self.output.append("\n")
        elif tag == "a":
            if self.href:
                text = self.current_text.strip()
                if text and self.href != text:
                    # Only make a link if href differs from text
                    self.current_text = f"[{text}]({self.href})"
                self.href = None
        elif tag in ("ul", "ol"):
            self.list_depth = max(0, self.list_depth - 1)
            self._flush_text()
            self.output.append("\n")
        elif tag == "li":
            self._flush_text()
            self.output.append("\n")
        elif tag in ("b", "strong"):
            self.current_text += "**"
        elif tag in ("i", "em"):
            self.current_text += "*"

    def handle_data(self, data):
        if self.in_style or self.in_head:
            return
        # Normalize whitespace but preserve intentional line breaks
        text = data.replace("\n", " ")
        # Don't add pure whitespace
        if text.strip():
            self.current_text += text

    def handle_entityref(self, name):
        if self.in_style or self.in_head:
            return
        entities = {
            "amp": "&", "lt": "<", "gt": ">", "quot": '"',
            "nbsp": " ", "bull": "\u2022", "mdash": "\u2014",
            "ndash": "\u2013", "lsquo": "\u2018", "rsquo": "\u2019",
            "ldquo": "\u201c", "rdquo": "\u201d", "hellip": "\u2026",
        }
        self.current_text += entities.get(name, f"&{name};")

    def handle_charref(self, name):
        if self.in_style or self.in_head:
            return
        try:
            if name.startswith("x"):
                char = chr(int(name[1:], 16))
            else:
                char = chr(int(name))
            self.current_text += char
        except (ValueError, OverflowError):
            self.current_text += f"&#{name};"

    def _flush_text(self):
        if self.current_text.strip():
            self.output.append(self.current_text)
        self.current_text = ""

    def get_markdown(self):
        self._flush_text()
        raw = "".join(self.output)
        # Clean up excessive blank lines
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        # Clean up spaces before newlines
        raw = re.sub(r" +\n", "\n", raw)
        # Post-process: strip any remaining Google redirect URLs in text
        raw = _clean_google_redirects(raw)
        # Remove leading whitespace
        raw = raw.strip()
        return raw


def convert_file(html_path: Path, md_path: Path):
    """Convert a single HTML file to Markdown."""
    try:
        html_content = html_path.read_text(encoding="utf-8")
        parser = GoogleDocHTMLToMarkdown()
        parser.feed(html_content)
        md_content = parser.get_markdown()

        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md_content, encoding="utf-8")
        return True
    except Exception as e:
        print(f"  ERROR converting {html_path.name}: {e}")
        return False


def convert_directory(src_dir: Path, dst_dir: Path):
    """Convert all HTML files in src_dir to Markdown in dst_dir (flat, no categories)."""
    html_files = sorted(src_dir.glob("*.html"))
    print(f"\nSource: {src_dir}")
    print(f"Output: {dst_dir}")
    print(f"Found {len(html_files)} HTML files\n")

    success = 0
    failed = 0
    errors = []

    for html_file in html_files:
        stem = html_file.stem
        md_path = dst_dir / f"{stem}.md"

        print(f"  {html_file.name} -> {stem}.md")
        if convert_file(html_file, md_path):
            success += 1
        else:
            failed += 1
            errors.append(html_file.name)

    return success, failed, errors


def main():
    print("=" * 60)
    print("Converting HTML exports to Markdown")
    print("=" * 60)

    total_success = 0
    total_failed = 0
    all_errors = []

    for src_dir, dst_dir in CONVERSIONS:
        if not src_dir.exists():
            print(f"\nWARNING: Source directory not found: {src_dir}")
            continue

        success, failed, errors = convert_directory(src_dir, dst_dir)
        total_success += success
        total_failed += failed
        all_errors.extend(errors)

    print("\n" + "=" * 60)
    print(f"TOTAL: {total_success} converted, {total_failed} failed")
    if all_errors:
        print(f"Errors in: {', '.join(all_errors)}")
    print("=" * 60)

    # Print output summary
    for _, dst_dir in CONVERSIONS:
        if dst_dir.exists():
            md_files = list(dst_dir.glob("*.md"))
            print(f"\n{dst_dir.name}/: {len(md_files)} markdown files")


if __name__ == "__main__":
    main()
