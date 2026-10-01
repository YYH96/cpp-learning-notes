from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1] / 'docs'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.ids = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for attr in ('href', 'src'):
            if attr in attrs: self.links.append(attrs[attr])

pages = {}
for path in root.rglob('*.html'):
    page = Page(); page.feed(path.read_text(encoding='utf-8')); pages[path.resolve()] = page
errors = []; count = 0
for path, page in pages.items():
    for url in page.links:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc: continue
        target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
        count += 1
        if not target.exists(): errors.append(f'{path.name}: missing {url}')
        elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
            errors.append(f'{path.name}: missing anchor {url}')
assert not errors, '\n'.join(errors)
assert len(list((root/'chapters').glob('*.html'))) == 15
assert len(list((root/'examples').glob('*.cpp'))) == 29
print(f'Validated {len(pages)} HTML pages and {count} local links/assets/anchors; 29 example downloads.')
