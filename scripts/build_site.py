"""Build dependency-free HTML pages from the public learning notes."""
from pathlib import Path
import re, html, json, shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)
CHAPTERS = sorted((ROOT / 'chapters').glob('*.md'))
EXAMPLES = sorted((ROOT / 'examples').glob('*.cpp'))
esc = html.escape
THEORY = json.loads((ROOT / 'scripts/theory.json').read_text(encoding='utf-8'))
GROUPS = list(dict.fromkeys(item['group'] for item in THEORY))

def slug(text):
    return re.sub(r'\s', '-', re.sub(r'[^\w\s-]', '', text.lower()))

def inline(text):
    tokens = []
    def token(markup):
        tokens.append(markup)
        return f'ZZTOKEN{len(tokens)-1}ZZ'
    text = re.sub(r'`([^`]+)`', lambda m: token('<code>'+esc(m[1])+'</code>'), text)
    def link(m):
        target = m[2].replace('../README.md', '../index.html').replace('.md', '.html')
        return token(f'<a href="{esc(target, quote=True)}">{esc(m[1])}</a>')
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    text = esc(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    for i, markup in enumerate(tokens):
        text = text.replace(f'ZZTOKEN{i}ZZ', markup)
    return text

def markdown(text):
    lines = text.splitlines(); blocks = []; i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip(): i += 1; continue
        if line.startswith('```'):
            lang = line[3:]; code = []; i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i]); i += 1
            blocks.append('<div class="code-block"><div class="code-toolbar"><span>'+esc(lang or 'CODE')+'</span><button class="copy-code" type="button">코드 복사</button></div><pre><code>'+esc('\n'.join(code))+'</code></pre></div>'); i += 1; continue
        heading = re.match(r'^(#{1,6}) (.+)', line)
        if heading:
            n = len(heading[1]); title = heading[2]
            blocks.append(f'<h{n} id="{slug(title)}">{inline(title)}</h{n}>'); i += 1; continue
        if line == '---': blocks.append('<hr>'); i += 1; continue
        if line.startswith('> '):
            blocks.append('<blockquote>'+inline(line[2:])+'</blockquote>'); i += 1; continue
        if line.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                item = lines[i][2:]
                if item.startswith('[ ] '):
                    item = '<label><input type="checkbox" class="learning-check"> '+inline(item[4:])+'</label>'
                else: item = inline(item)
                items.append('<li>'+item+'</li>'); i += 1
            blocks.append('<ul>'+''.join(items)+'</ul>'); continue
        para = [line]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|```|---|> |\- )', lines[i]):
            para.append(lines[i]); i += 1
        blocks.append('<p>'+inline(' '.join(para))+'</p>')
    return '\n'.join(blocks)

meta = []
for path in CHAPTERS:
    text = path.read_text(encoding='utf-8')
    title = re.search(r'^# \d+\. (.+)', text, re.M)[1]
    goal = re.search(r'학습 목표\*\* · (.+)', text)[1]
    meta.append({'name': path.stem, 'title': title, 'goal': goal, 'text': text, 'theory': THEORY[len(meta)]})

def shell(title, content, prefix='', current='', toc=''):
    links = ''
    for group in GROUPS:
        links += f'<div class="nav-group"><p class="group-label">{esc(group)}</p>'
        for i,c in enumerate(meta):
            if c['theory']['group'] != group: continue
            terms = ' '.join(c['theory']['terms'])
            links += f'<a class="chapter-link {"active" if current == c["name"] else ""}" href="{prefix}chapters/{c["name"]}.html" data-search="{esc(c["title"]+" "+c["goal"]+" "+group+" "+terms)}"><span>{i+1:02}</span>{esc(c["title"])}</a>'
        links += '</div>'
    result = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="C++ 수업을 정리한 15개 챕터와 실행 예제 29개. 기초 문법부터 클래스, 자료구조, 게임 설계까지."><title>{esc(title)} · C++ Learning Notes</title><link rel="stylesheet" href="{prefix}assets/style.css"><script defer src="{prefix}assets/app.js"></script></head>
<body><a class="skip" href="#main">본문으로 이동</a><aside class="sidebar" id="sidebar"><a class="brand" href="{prefix}index.html"><span class="brand-icon">C<span>++</span></span><span>Learning Notes<small>배운 것을, 내 것으로.</small></span></a><div class="search"><span aria-hidden="true">⌕</span><input id="chapter-search" type="search" placeholder="챕터 찾아보기" aria-label="챕터 검색"></div><nav aria-label="학습 목차"><a class="overview" href="{prefix}index.html">↗ 학습 노트 홈</a><p class="nav-label">THEORY TOPICS <span>15</span></p><div class="chapter-list">{links}</div><p class="no-results" hidden>검색 결과가 없습니다.</p><a class="examples-link" href="{prefix}examples.html">&lt;/&gt; 실행 예제 모아보기 <span>29</span></a></nav><div class="sidebar-bottom"><span class="status-dot"></span> MSVC C++17 검증 완료<a href="https://github.com/YYH96/cpp-learning-notes" target="_blank" rel="noopener">GitHub ↗</a></div></aside><div class="page-shell"><header class="topbar"><button id="menu-toggle" type="button" aria-expanded="false" aria-controls="sidebar" aria-label="학습 목차 열기">☰</button><span>C++ / <strong>{esc(title)}</strong></span><button id="theme-toggle" type="button" aria-label="화면 테마 변경">◐ <span>테마</span></button></header><main id="main">{content}</main><footer><span>C++ Learning Notes · 2026</span><a href="https://github.com/YYH96/cpp-learning-notes">원본 문서와 코드 ↗</a></footer></div>{toc}<div class="toast" role="status" aria-live="polite"></div></body></html>'''
    return result.replace('</head>', f'<link rel="stylesheet" href="{prefix}assets/theory.css"></head>')

cards = ''.join(f'<a class="chapter-card" href="chapters/{c["name"]}.html" data-search="{esc(c["title"]+" "+c["goal"])}"><div class="card-top"><span>CHAPTER {i+1:02}</span><b>↗</b></div><h3>{esc(c["title"])}</h3><p>{esc(c["goal"])}</p><div class="card-bottom">학습 페이지 읽기 <span>→</span></div></a>' for i,c in enumerate(meta))
home = f'''<section class="hero"><div class="eyebrow"><span></span> MY C++ STUDY ARCHIVE</div><h1>한 줄의 코드부터,<br><em>하나의 게임까지.</em></h1><p class="hero-description">수업에서 배운 C++를 개념과 예제로 다시 연결합니다.<br>기초 문법부터 객체 지향, 자료구조, 게임 설계까지<br>차근차근 읽어 나가는 나만의 학습 노트.</p><a class="primary-button" href="chapters/{meta[0]['name']}.html">첫 챕터부터 시작하기 <span>→</span></a><div class="hero-code" aria-hidden="true"><div class="code-dots"><i></i><i></i><i></i><span>my_learning.cpp</span></div><pre><span class="muted">// 이해하고, 만들고, 다시 정리하기</span>
<span class="purple">int</span> <span class="amber">main</span>() {{
    <span class="purple">while</span> (curious) {{
        learn();
        build();
        reflect();
    }}
    <span class="purple">return</span> growth;
}}</pre><div class="code-note">작은 개념들이 모여 큰 구조가 됩니다.</div></div></section><section class="stats" aria-label="노트 구성"><div><strong>15<span>CHAPTERS</span></strong><p>개념별 이론 정리</p></div><div><strong>29<span>EXAMPLES</span></strong><p>실행 가능한 C++ 예제</p></div><div><strong>C++17<span>VERIFIED</span></strong><p>MSVC 컴파일·실행 확인</p></div></section><section class="chapter-section"><div class="section-heading"><div class="eyebrow">STEP BY STEP</div><h2>어디부터 복습할까요?</h2><p>각 챕터에서 핵심 개념과 예제를 함께 확인하세요.</p></div><div class="chapter-grid">{cards}</div></section><section class="closing"><div><span class="eyebrow">LEARN BY DOING</span><h2>읽었다면, 직접 실행해 보세요.</h2><p>29개 예제를 내려받아 코드를 바꾸고 결과를 확인해 보세요.</p></div><a class="primary-button" href="examples.html">예제 코드 둘러보기 →</a></section>'''
group_nav = '<nav class="topic-navigation" aria-label="이론 분야">'+''.join(f'<a href="#topic-{i}"><span>{i+1:02}</span>{esc(group)}</a>' for i,group in enumerate(GROUPS))+'</nav>'
groups_html = ''
for group_index,group in enumerate(GROUPS):
    group_cards = ''
    for i,c in enumerate(meta):
        if c['theory']['group'] != group: continue
        tags = ''.join(f'<span>{esc(term)}</span>' for term in c['theory']['terms'])
        searchable = ' '.join([c['title'], c['goal'], group, *c['theory']['terms']])
        group_cards += f'<a class="chapter-card" href="chapters/{c["name"]}.html" data-search="{esc(searchable)}"><div class="card-top"><span>THEORY {i+1:02}</span><b>↗</b></div><h3>{esc(c["title"])}</h3><p>{esc(c["theory"]["definition"])}</p><div class="concept-tags">{tags}</div><div class="card-bottom">핵심 요약 · 개념 비교 <span>→</span></div></a>'
    groups_html += f'<section class="topic-group" id="topic-{group_index}"><div class="topic-heading"><span>{group_index+1:02}</span><h3>{esc(group)}</h3></div><div class="chapter-grid">{group_cards}</div></section>'
theory_home = '<section class="chapter-section"><div class="section-heading"><div class="eyebrow">THEORY FIRST</div><h2>개념부터 짧고 명확하게.</h2><p>분야별 핵심 요약과 비교표를 먼저 읽고, 필요한 예제를 펼쳐 보세요.</p></div>'+group_nav+groups_html+'</section>'
home = re.sub(r'<section class="chapter-section">[\s\S]*?</section>', lambda _: theory_home, home, count=1)
home = home.replace('한 줄의 코드부터,<br><em>하나의 게임까지.</em>', '코드 전에 개념,<br><em>핵심만 한눈에.</em>')
home = home.replace('수업에서 배운 C++를 개념과 예제로 다시 연결합니다.<br>기초 문법부터 객체 지향, 자료구조, 게임 설계까지<br>차근차근 읽어 나가는 나만의 학습 노트.', '기초 문법 · 함수와 데이터 · 객체 지향 · 자료구조 · 게임 설계.<br>이론을 분야별로 묶고, 정의와 차이를 짧게 정리했습니다.<br>개념을 확인한 뒤 관련 예제로 연결하세요.')
home = home.replace('첫 챕터부터 시작하기', '이론부터 읽기')
(OUT/'index.html').write_text(shell('학습 노트 홈', home), encoding='utf-8')
(OUT/'chapters').mkdir(exist_ok=True)
for i,c in enumerate(meta):
    # The site supplies its own navigation and in-page table of contents.
    body = c['text'].split('\n',2)[2]
    body = re.sub(r'## 이 페이지에서 다룰 내용\n[\s\S]*?---\n', '', body)
    body = re.sub(r'\n---\n\n\[← 전체 목차\][\s\S]*$', '', body)
    theory = c['theory']
    theory_cards = ''.join(f'<div class="concept-card"><span>{j+1:02}</span><h3>{esc(point[0])}</h3><p>{esc(point[1])}</p></div>' for j,point in enumerate(theory['points']))
    table_header = ''.join(f'<th scope="col">{esc(col)}</th>' for col in theory['columns'])
    table_rows = ''.join('<tr>'+''.join((f'<th scope="row">{esc(cell)}</th>' if j == 0 else f'<td>{esc(cell)}</td>') for j,cell in enumerate(row))+'</tr>' for row in theory['rows'])
    theory_content = f'<section class="theory-overview" id="theory-summary"><div class="eyebrow">한눈에 보는 핵심</div><p class="concept-definition">{esc(theory["definition"])}</p><div class="concept-grid">{theory_cards}</div></section><section id="concept-comparison"><h2>개념 비교</h2><div class="table-scroll"><table class="concept-table"><thead><tr>{table_header}</tr></thead><tbody>{table_rows}</tbody></table></div></section><section class="pitfall" id="common-pitfall"><strong>자주 헷갈리는 점</strong><p>{esc(theory["warning"])}</p></section>'
    extra_path = ROOT / 'theory' / f'{c["name"]}.md'
    extra_headings = []
    if extra_path.exists():
        extra_text = extra_path.read_text(encoding='utf-8')
        extra_headings = re.findall(r'^## (.+)', extra_text, re.M)
        theory_content += '<section class="extra-theory">'+markdown(extra_text)+'</section>'
    # Concise theory stays visible. Longer classroom notes and complete examples open on demand.
    body = re.sub(r'^# .+\n', '', body, count=1)
    body = re.sub(r'^\s*> \*\*학습 목표\*\* · .+\n', '', body, count=1)
    body = body.strip()
    details_label = '복습 체크리스트 펼치기' if i == 14 else '상세 설명과 예제 펼치기'
    details = f'<details class="lesson-details" id="lesson-details"><summary><span>{details_label}</span><small>필요한 내용만 골라 읽기</small><b>+</b></summary><div class="lesson-detail-content">{markdown(body)}</div></details>'
    toc = '<aside class="page-toc"><span>이 페이지에서</span><a href="#theory-summary">핵심 요약</a><a href="#concept-comparison">개념 비교</a><a href="#common-pitfall">주의할 점</a><a href="#lesson-details">설명과 예제</a></aside>'
    toc = toc.replace('<a href="#lesson-details">', ''.join(f'<a href="#{slug(h)}">{esc(h)}</a>' for h in extra_headings)+'<a href="#lesson-details">')
    prev = f'<a href="{meta[i-1]["name"]}.html"><small>← 이전 챕터</small>{esc(meta[i-1]["title"])}</a>' if i else '<a href="../index.html"><small>← 전체 목차</small>학습 노트 홈</a>'
    nxt = f'<a href="{meta[i+1]["name"]}.html"><small>다음 챕터 →</small>{esc(meta[i+1]["title"])}</a>' if i<14 else '<a href="../examples.html"><small>다음 단계 →</small>예제 직접 실행하기</a>'
    article = f'<div class="reading"><div class="reading-eyebrow">{esc(theory["group"])} <span>THEORY {i+1:02} / 15</span></div><article><h1>{esc(c["title"])}</h1>{theory_content}{details}</article><nav class="page-navigation" aria-label="이전 다음 챕터">{prev}{nxt}</nav></div>'
    (OUT/'chapters'/f'{c["name"]}.html').write_text(shell(c['title'], article, '../', c['name'], toc),encoding='utf-8')

(OUT/'examples').mkdir(exist_ok=True)
example_cards = []
for i,path in enumerate(EXAMPLES):
    shutil.copyfile(path, OUT/'examples'/path.name)
    chapter = next(c for c in meta if path.name in c['text'])
    code = path.read_text(encoding='utf-8')
    example_cards.append(f'<details class="example-card"><summary><span>{i+1:02}</span><strong>{esc(path.name)}</strong><b>+</b></summary><div class="example-content"><p>관련 개념: <a href="chapters/{chapter["name"]}.html">{esc(chapter["title"])}</a> · <a href="examples/{path.name}" download>파일 내려받기 ↓</a></p><div class="code-block"><div class="code-toolbar"><span>C++</span><button class="copy-code" type="button">코드 복사</button></div><pre><code>{esc(code)}</code></pre></div></div></details>')
examples_page = '<div class="examples-page"><div class="eyebrow">LEARN BY DOING</div><h1>직접 실행하는<br><em>29개의 예제.</em></h1><p class="hero-description">각 예제는 하나의 main 함수로 독립 실행됩니다.<br>MSVC C++17로 컴파일·실행하고 결과를 확인한 복습 코드입니다.</p><blockquote>Visual Studio의 x64 Native Tools Command Prompt에서 실행하세요.</blockquote><div class="code-block"><div class="code-toolbar"><span>명령 프롬프트</span><button class="copy-code" type="button">코드 복사</button></div><pre><code>cl /nologo /std:c++17 /EHsc /utf-8 01_hello.cpp /Fe:hello.exe\nhello.exe</code></pre></div>'+''.join(example_cards)+'</div>'
(OUT/'examples.html').write_text(shell('실행 예제', examples_page),encoding='utf-8')
(OUT/'.nojekyll').write_text('',encoding='utf-8')
(OUT/'404.html').write_text(shell('페이지를 찾을 수 없습니다','<div class="examples-page"><h1>페이지를 찾을 수 없습니다.</h1><a class="primary-button" href="https://yyh96.github.io/cpp-learning-notes/">학습 노트 홈으로 →</a></div>', 'https://yyh96.github.io/cpp-learning-notes/'),encoding='utf-8')
print(f'Built 15 chapters, 29 example files and 4 entry pages in {OUT}')
