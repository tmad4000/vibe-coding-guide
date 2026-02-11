#!/usr/bin/env python3
"""Convert Google Docs HTML exports to clean Markdown with heading preservation.

Reads from html/ directory, writes to markdown/ directory (mirroring the
categorized folder structure from the txt files).
"""

import os
import re
import json
from html.parser import HTMLParser
from pathlib import Path

BASE_DIR = Path(__file__).parent
HTML_DIR = BASE_DIR / "html"
MD_DIR = BASE_DIR / "markdown"
METADATA_DIR = BASE_DIR / "metadata"

# Category mapping (filename without extension -> category folder)
CATEGORIES = {
    # Systematic Awesome
    "systematicawesome": "systematic-awesome",
    "index": "systematic-awesome",
    # Health & Wellness
    "adhd": "health-wellness",
    "backpain": "health-wellness",
    "chronicpain": "health-wellness",
    "buoyantfitness": "health-wellness",
    "hypnosis": "health-wellness",
    "meditation": "health-wellness",
    "qigongcrew": "health-wellness",
    "qiresearch": "health-wellness",
    "sleep": "health-wellness",
    "supplements": "health-wellness",
    "yogalist": "health-wellness",
    "healingartsgrant": "health-wellness",
    # Food & Drink
    "cheese": "food-drink",
    "chocolate": "food-drink",
    "foodslist": "food-drink",
    "tea": "food-drink",
    # Ideas & Knowledge
    "codex": "ideas-knowledge",
    "globalideabank": "ideas-knowledge",
    "questions": "ideas-knowledge",
    "startupideas": "ideas-knowledge",
    "startuptrickswiki": "ideas-knowledge",
    "hackathonprojects": "ideas-knowledge",
    "bookslist": "ideas-knowledge",
    "quoteslist": "ideas-knowledge",
    "toolstacks": "ideas-knowledge",
    # World Issues
    "climatechange": "world-issues",
    "coronavirus": "world-issues",
    "covid19hackideas": "world-issues",
    "crises": "world-issues",
    "easilysolvableworldproblems": "world-issues",
    "worldproblems": "world-issues",
    "worldgestalts": "world-issues",
    "socialsupportforregenerativefarmers": "world-issues",
    # Philosophy & Spirituality
    "ethicaldilemmas": "philosophy-spirituality",
    "existentialcrisis": "philosophy-spirituality",
    "heidegger": "philosophy-spirituality",
    "philosophy": "philosophy-spirituality",
    "pureland": "philosophy-spirituality",
    "nvc": "philosophy-spirituality",
    # Things You Didn't Know Existed
    "thingsyoudidntknowexisted": "things-you-didnt-know-existed",
    "thingsyoudidntknowexistedatmit": "things-you-didnt-know-existed",
    "thingsyoudidntknowexistedinhawaii": "things-you-didnt-know-existed",
    "thingsyoudidntknowexistedinnyc": "things-you-didnt-know-existed",
    "thingsyoudidntknowexistedinportland": "things-you-didnt-know-existed",
    "thingsyoudidntknowexistedinsantacruz": "things-you-didnt-know-existed",
    "thingsyoudidntknowexistedinsf": "things-you-didnt-know-existed",
    "thingyoudidntknowexistedinsandiego": "things-you-didnt-know-existed",
    # Community & Social
    "burningman": "community-social",
    "hotconnections": "community-social",
    "cryptoconnect": "community-social",
    "favorverse": "community-social",
    "salon": "community-social",
    "hiringblurb": "community-social",
    "hiringlist": "community-social",
    "housinglist": "community-social",
    "autodidacts": "community-social",
    "admitsphere": "community-social",
    "ilparty": "community-social",
    # IdeaFlow
    "ideaflowbackground": "ideaflow",
    "ideaflowproject": "ideaflow",
    "gestaltexplanation": "ideaflow",
    "perfectcoordination": "ideaflow",
    "visioncharter": "ideaflow",
    "ifiran": "ideaflow",
    # Culture & Education
    "aieducation": "culture-education",
    "culturalendangeredspecies": "culture-education",
    "culturaltechnology": "culture-education",
    "stanfordclasses": "culture-education",
    "kidactivities": "culture-education",
    "commentaries": "culture-education",
    "thoughtfulweb": "culture-education",
    # Personal
    "aspirations": "personal",
    "lifechange": "personal",
    "lifechangingthings": "personal",
    "shadirecs": "personal",
    "wall": "personal",
    "interrupt": "personal",
    # Meta
    "bugslist": "meta",
    "productfeedback": "meta",
    "products": "meta",
    "templates": "meta",
    "lists": "meta",
    "si": "meta",
    # Misc
    "circuits": "misc",
    "vrcoralreefs": "misc",
    "infrastructure": "misc",
}


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
                import urllib.parse
                parsed = urllib.parse.urlparse(self.href)
                params = urllib.parse.parse_qs(parsed.query)
                if "q" in params:
                    self.href = params["q"][0]
        elif tag == "ul" or tag == "ol":
            self._flush_text()
            self.list_depth += 1
        elif tag == "li":
            self._flush_text()
            indent = "  " * (self.list_depth - 1)
            self.output.append(f"{indent}- ")
        elif tag == "b" or tag == "strong":
            self.current_text += "**"
        elif tag == "i" or tag == "em":
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
        elif tag == "ul" or tag == "ol":
            self.list_depth = max(0, self.list_depth - 1)
            self._flush_text()
            self.output.append("\n")
        elif tag == "li":
            self._flush_text()
            self.output.append("\n")
        elif tag == "b" or tag == "strong":
            self.current_text += "**"
        elif tag == "i" or tag == "em":
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
        # Clean up spaces before punctuation
        raw = re.sub(r" +\n", "\n", raw)
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


def main():
    print(f"Converting HTML exports to Markdown...")
    print(f"Source: {HTML_DIR}")
    print(f"Output: {MD_DIR}")
    print()

    html_files = sorted(HTML_DIR.glob("*.html"))
    print(f"Found {len(html_files)} HTML files")
    print()

    success = 0
    failed = 0

    for html_file in html_files:
        stem = html_file.stem
        category = CATEGORIES.get(stem, "misc")
        md_path = MD_DIR / category / f"{stem}.md"

        print(f"  {stem}.html -> {category}/{stem}.md")
        if convert_file(html_file, md_path):
            success += 1
        else:
            failed += 1

    print()
    print(f"Done! {success} converted, {failed} failed")
    print()

    # Print folder summary
    print("Markdown files per folder:")
    for d in sorted(MD_DIR.iterdir()):
        if d.is_dir():
            count = len(list(d.glob("*.md")))
            print(f"  {d.name}: {count}")


if __name__ == "__main__":
    main()
