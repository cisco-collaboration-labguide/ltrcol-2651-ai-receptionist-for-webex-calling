"""Validate generated HTML links, anchors, images and the expected lab pages.

Run after `python -m mkdocs build --strict`. Uses only Python's standard library.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.images = path, set(), [], []
        self.h1_count = 0
        self.lab_screenshots = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1':
            self.h1_count += 1
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs)
            if "lab-screenshot" in attrs.get("class", "").split():
                self.lab_screenshots.append(attrs)


root = Path(sys.argv[1] if len(sys.argv) > 1 else "site").resolve()
pages = {path.resolve(): Page(path) for path in root.rglob("*.html")}
errors = []
checked_links = checked_images = 0
expected = [
    "index.html",
    "lab-introduction/index.html",
    "tasks/01-access-the-lab/index.html",
    "tasks/02-control-hub/index.html",
    "ai-receptionist-overview/index.html",
    "tasks/03-configure-ai-receptionist/index.html",
    "customer-assist-overview/index.html",
    "tasks/04-customer-assist/index.html",
    "tasks/05-intent-based-routing/index.html",
    "tasks/06-webex-app/index.html",
    "tasks/07-verify-ai-receptionist/index.html",
]
for name in expected:
    if root / name not in pages:
        errors.append(f"Missing page: {name}")
    elif pages[root / name].h1_count != 1:
        errors.append(f"{name}: expected exactly one page title (h1)")
for path, page in pages.items():
    # 404 navigation may use absolute production URLs and is checked by MkDocs.
    if path.name == "404.html":
        continue
    for url in page.links + [img.get("src", "") for img in page.images]:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc:
            continue
        if not parsed.path:
            target = path
        elif parsed.path.startswith("/"):
            # Theme-generated absolute URLs can include the project Pages prefix.
            parts = unquote(parsed.path).lstrip("/")
            target = root / parts
            if not target.exists() and "/" in parts:
                target = root / parts.split("/", 1)[1]
        else:
            target = (path.parent / unquote(parsed.path)).resolve()
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"{path.relative_to(root)}: missing {url}")
        elif parsed.fragment and target in pages:
            anchor = unquote(parsed.fragment)
            if anchor not in pages[target].ids:
                errors.append(f"{path.relative_to(root)}: missing anchor {url}")
        checked_links += 1
    for img in page.images:
        if not img.get("alt", "").strip():
            errors.append(f"{path.relative_to(root)}: image has no alt text: {img.get('src')}")
        checked_images += 1
if errors:
    print("\n".join(errors))
    raise SystemExit(1)
source_screenshots = sum(len(page.lab_screenshots) for page in pages.values())
unique_screenshots = len({img.get("src") for page in pages.values() for img in page.lab_screenshots})
if source_screenshots != 93 or unique_screenshots != 92:
    print(f"Screenshot mismatch: expected 93 placements across 92 source images; found {source_screenshots} placements across {unique_screenshots} files.")
    raise SystemExit(1)
print(f"PASS: {len(expected)} guide pages; {checked_links} local links/anchors; {checked_images} image references; all 93 screenshot placements across 92 images.")
