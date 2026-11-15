#!/usr/bin/env python3
"""Check a built site for missing local links, assets and fragment targets.

Usage: python3 scripts/check_site.py _site
Uses only the Python standard library. External links are not fetched.
"""
import argparse
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if attrs.get(key): self.links.append(attrs[key])
        if attrs.get('id'): self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'): self.ids.add(attrs['name'])

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('directory', type=Path)
args = parser.parse_args()
root = args.directory.resolve()
assert (root/'index.html').is_file(), 'Build the website first.'
pages = {p: Page(p.read_text()) for p in root.rglob('*.html')}
issues = defaultdict(set)
count = 0
for path, page in pages.items():
    rel = path.relative_to(root).as_posix()
    url = 'https://alexkaltenbach.github.io/' + rel.removesuffix('index.html')
    for value in page.links:
        link = urlparse(urljoin(url, value))
        if link.scheme not in ('http', 'https') or link.netloc != 'alexkaltenbach.github.io': continue
        target = root / unquote(link.path).lstrip('/')
        if target.is_dir(): target = target/'index.html'
        elif not target.is_file() and target.with_suffix('.html').is_file(): target = target.with_suffix('.html')
        count += 1
        if not target.is_file(): issues['Missing '+link.path].add(rel)
        elif link.fragment and target in pages and unquote(link.fragment) not in pages[target].ids:
            issues['Missing anchor '+link.path+'#'+link.fragment].add(rel)
for issue, sources in sorted(issues.items()):
    print(issue + ' — ' + ', '.join(sorted(sources)[:3]))
print(f'{len(pages)} HTML pages; {count} internal links and assets; {len(issues)} unique issues.')
raise SystemExit(bool(issues))
