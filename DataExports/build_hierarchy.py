#!/usr/bin/env python3
"""Build hierarchical folder structure from breadcrumb paths.

Creates markdown-by-hierarchy/ with folders matching the actual
document parent-child structure from jacobcole.net breadcrumbs.
"""

import shutil
from pathlib import Path

BASE = Path(__file__).parent
SRC_MD = BASE / "markdown-by-category"  # source markdown files (flat by category)
DST = BASE / "markdown-by-hierarchy"

# Complete hierarchy based on combined HTML + txt breadcrumb analysis
# Format: filename -> (parent_path_parts,)
# Where parent path is relative to systematicawesome root

HIERARCHY = {
    # Direct children of systematicawesome (depth 1)
    "adhd": ("",),
    "admitsphere": ("",),  # no breadcrumb found, stays at root
    "aieducation": ("",),  # no breadcrumb, stays at root
    "aspirations": ("",),  # no breadcrumb, stays at root
    "autodidacts": ("",),
    "bookslist": ("",),
    "buoyantfitness": ("",),
    "burningman": ("",),
    "circuits": ("",),
    "climatechange": ("",),
    "coronavirus": ("",),
    "covid19hackideas": ("",),  # no breadcrumb, likely under coronavirus
    "cryptoconnect": ("",),
    "culturalendangeredspecies": ("",),
    "culturaltechnology": ("",),
    "existentialcrisis": ("",),
    "healingartsgrant": ("",),
    "hiringblurb": ("",),
    "hiringlist": ("",),
    "hotconnections": ("",),
    "hypnosis": ("",),
    "ideaflowbackground": ("",),
    "ideaflowproject": ("",),
    "index": ("",),
    "interrupt": ("",),
    "kidactivities": ("",),
    "lifechange": ("",),
    "lifechangingthings": ("",),
    "meditation": ("",),
    "nvc": ("",),
    "products": ("",),
    "pureland": ("",),
    "qigongcrew": ("",),
    "qiresearch": ("",),
    "questions": ("",),
    "shadirecs": ("",),
    "stanfordclasses": ("",),
    "startupideas": ("",),
    "startuptrickswiki": ("",),
    "supplements": ("",),
    "systematicawesome": ("",),
    "thoughtfulweb": ("",),
    "toolstacks": ("",),
    "wall": ("",),
    "worldproblems": ("",),

    # Under foodslist (depth 2)
    "foodslist": ("",),
    "cheese": ("foodslist",),
    "chocolate": ("foodslist",),
    "tea": ("foodslist",),

    # Under philosophy (depth 2)
    "philosophy": ("",),
    "ethicaldilemmas": ("philosophy",),
    "heidegger": ("philosophy",),
    "yogalist": ("philosophy",),

    # Under infrastructure (depth 2)
    "infrastructure": ("",),
    "codex": ("infrastructure",),
    "templates": ("infrastructure",),

    # Under worldgestalts (depth 2)
    "worldgestalts": ("",),
    "globalideabank": ("worldgestalts",),

    # Under chronicpain (depth 2)
    "chronicpain": ("",),
    "backpain": ("chronicpain",),
    "si": ("chronicpain",),
    "sijointpain": ("chronicpain",),
    "sleep": ("chronicpain",),

    # Under productfeedback (depth 2)
    "productfeedback": ("",),
    "bugslist": ("productfeedback",),

    # Under things-you-didnt-know-existed (depth 2-3)
    "thingsyoudidntknowexisted": ("",),
    "thingsyoudidntknowexistedatmit": ("thingsyoudidntknowexisted",),
    "thingsyoudidntknowexistedinhawaii": ("thingsyoudidntknowexisted",),
    "thingsyoudidntknowexistedinnyc": ("thingsyoudidntknowexisted",),
    "thingsyoudidntknowexistedinportland": ("thingsyoudidntknowexisted",),
    "thingsyoudidntknowexistedinsantacruz": ("thingsyoudidntknowexisted",),
    "thingsyoudidntknowexistedinsf": ("thingsyoudidntknowexisted",),
    "thingyoudidntknowexistedinsandiego": ("thingsyoudidntknowexisted",),

    # Via worldquestguild (depth 2)
    "favorverse": ("worldquestguild",),
    "salon": ("worldquestguild",),
    "vrcoralreefs": ("worldquestguild",),

    # Via manifestos (depth 2)
    "perfectcoordination": ("manifestos",),
    "visioncharter": ("manifestos",),

    # Under mitdocs
    "hackathonprojects": ("mitdocs",),

    # Via ideaflow
    "gestaltexplanation": ("ideaflow",),
    "ifiran": ("ideaflow",),

    # Misc / no clear parent
    "commentaries": ("misc",),
    "easilysolvableworldproblems": ("misc",),
    "housinglist": ("misc",),
    "ilparty": ("misc",),
    "lists": ("misc",),
    "socialsupportforregenerativefarmers": ("misc",),
    "quoteslist": ("",),
}


def find_source_md(name):
    """Find a markdown file by name across all category folders."""
    for md_file in SRC_MD.rglob(f"{name}.md"):
        return md_file
    return None


def main():
    if DST.exists():
        shutil.rmtree(DST)

    count = 0
    missing = []

    for name, (parent_path,) in sorted(HIERARCHY.items()):
        src = find_source_md(name)
        if not src:
            missing.append(name)
            continue

        if parent_path:
            dest_dir = DST / parent_path / name
        else:
            dest_dir = DST / name

        # If this node has children, it becomes a folder with a README.md
        # Check if anything lists this as parent
        has_children = any(
            p[0] == name or p[0].endswith(f"/{name}")
            for n, p in HIERARCHY.items()
            if n != name
        )

        if has_children:
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / f"{name}.md"
        else:
            dest_dir.parent.mkdir(parents=True, exist_ok=True)
            dest = dest_dir.parent / f"{name}.md" if not parent_path else dest_dir.parent / f"{name}.md"
            # Wait, this is confusing. Let me simplify:
            # If it has children, put the file inside its own folder
            # If it doesn't, put it in the parent folder
            if parent_path:
                (DST / parent_path).mkdir(parents=True, exist_ok=True)
                dest = DST / parent_path / f"{name}.md"
            else:
                DST.mkdir(parents=True, exist_ok=True)
                dest = DST / f"{name}.md"

        if has_children:
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / f"{name}.md"

        shutil.copy2(src, dest)
        count += 1

    print(f"Copied {count} files to {DST}")
    if missing:
        print(f"\nMissing source markdown for: {', '.join(missing)}")

    # Print the tree
    print(f"\n=== Hierarchy Structure ===\n")

    def print_dir(path, indent=0):
        items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name))
        for item in items:
            prefix = "│   " * indent + "├── "
            if item.is_dir():
                # Count files in dir
                md_count = len(list(item.rglob("*.md")))
                print(f"{prefix}{item.name}/ ({md_count} files)")
                print_dir(item, indent + 1)
            else:
                print(f"{prefix}{item.name}")

    print_dir(DST)


if __name__ == "__main__":
    main()
