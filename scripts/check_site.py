from pathlib import Path
import json
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1] / 'docs'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.ids = set(); self.duplicates = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids: self.duplicates.append(attrs['id'])
            self.ids.add(attrs['id'])
        for attr in ('href', 'src'):
            if attr in attrs: self.links.append(attrs[attr])

pages = {}
for path in root.rglob('*.html'):
    page = Page(); page.feed(path.read_text(encoding='utf-8')); pages[path.resolve()] = page
errors = []; count = 0
for path, page in pages.items():
    errors.extend(f'{path.name}: duplicate anchor {value}' for value in page.duplicates)
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
for index, path in enumerate(sorted((root/'chapters').glob('*.html'))):
    text = path.read_text(encoding='utf-8')
    if index < 13:
        before_details = text.split('<details class="lesson-details"')[0].split('<article>')[1]
        assert 'class="code-block"' in before_details, f'{path.name}: basic syntax examples are hidden'
    else:
        assert '<section class="review-content"' in text, f'{path.name}: review content is hidden'
home = (root/'index.html').read_text(encoding='utf-8')
assert '복습' in home
for keyword in ['else if', 'static', 'dynamic_cast']:
    assert keyword in home, f'Missing searchable topic: {keyword}'
print(f'Validated {len(pages)} HTML pages and {count} local links/assets/anchors; 29 example downloads.')

manifest = json.loads((root.parent/'scripts/concepts.json').read_text(encoding='utf-8'))
assert len(list((root/'concepts').glob('*.html'))) == len(manifest)
assert len([c for c in manifest if c['group']=='연산자']) == 12
assert not any('연산자와 조건문' in c['title'] for c in manifest)
for c in manifest:
    page = root/'concepts'/f"{c['name']}.html"
    text = page.read_text(encoding='utf-8')
    assert '<h1>'+c['title']+'</h1>' in text
    assert '<details class="lesson-details"' not in text
print(f"Validated {len(manifest)} independent concept pages and separate operator/conditional groups.")

for item in manifest:
    text=(root/'concepts'/f"{item['name']}.html").read_text(encoding='utf-8')
    for section in ['개념과 동작 원리','사용 시점과 다른 개념의 구분','예제를 이해하는 순서','이해 확인']:
        assert section in text, (item['name'],section)
    if 'class="code-block"' in text:
        assert text.index('개념과 동작 원리') < text.index('class="code-block"')
print('All 87 concepts explain principles, application, example interpretation and comprehension checks.')
