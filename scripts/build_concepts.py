"""Render independent concept pages using the shared static-site renderer."""
(OUT/'concepts').mkdir(exist_ok=True)
for old in (OUT/'concepts').glob('*.html'):
    if old.stem not in {c['name'] for c in CONCEPTS}: old.unlink()
concept_groups = ''
for group_index, group in enumerate(GROUPS):
    cards = ''
    group_items = [c for c in NAV_META if c['theory']['group'] == group]
    for c in group_items:
        paragraphs = [line for line in c['text'].splitlines() if line.strip() and not line.startswith(('#', '|', '```', '- ', '**', '>'))]
        lead = paragraphs[0] if paragraphs else c['title']+'의 기본 문법과 사용 규칙.'
        lead = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', lead)
        if group == '복습': lead = c['theory']['definition']
        cards += f'<a class="chapter-card" href="{c["url"]}" data-search="{esc(c["search"])}"><div class="card-top"><span>{esc(group)}</span><b>↗</b></div><h3>{esc(c["title"])}</h3><p>{inline(lead[:110])}</p><div class="card-bottom">개념 읽기 <span>→</span></div></a>'
    concept_groups += f'<section class="topic-group" id="topic-{group_index}"><div class="topic-heading"><span>{len(group_items):02}</span><h3>{esc(group)}</h3></div><div class="chapter-grid">{cards}</div></section>'
group_nav = '<nav class="topic-navigation" aria-label="개념 분야">'+''.join(f'<a href="#topic-{i}">{esc(group)}</a>' for i,group in enumerate(GROUPS))+'</nav>'
concept_home = f'<section class="hero"><div class="eyebrow">C++ CONCEPT LIBRARY</div><h1>한 페이지,<br><em>하나의 개념.</em></h1><p class="hero-description">연산자와 조건문부터 함수·포인터·클래스까지.<br>필요한 개념만 골라 짧은 설명과 예제로 복습하세요.</p><a class="primary-button" href="{NAV_META[0]["url"]}">기초부터 시작하기</a></section><section class="stats"><div><strong>{len(CONCEPTS)}<span>CONCEPTS</span></strong><p>개념별 독립 페이지</p></div><div><strong>12<span>OPERATORS</span></strong><p>연산자 종류별 요약</p></div><div><strong>29<span>EXAMPLES</span></strong><p>독립 실행 예제</p></div></section><section class="chapter-section"><div class="section-heading"><div class="eyebrow">CHOOSE A CONCEPT</div><h2>무엇을 복습할까요?</h2><p>분야를 선택하거나 왼쪽 검색에서 개념·연산자 기호를 찾으세요.</p></div>{group_nav}{concept_groups}</section>'
(OUT/'index.html').write_text(shell('개념별 학습 노트', concept_home),encoding='utf-8')
for i,c in enumerate(NAV_META[:len(CONCEPTS)]):
    body = c['text'].split('\n',1)[1]
    headings = re.findall(r'^#{2,3} (.+)', body, re.M)
    toc = '<aside class="page-toc"><span>이 개념에서</span>'+''.join(f'<a href="#{slug(h)}">{esc(h)}</a>' for h in headings)+'<a href="#related">관련 개념과 응용</a></aside>'
    related = [other for other in NAV_META[:len(CONCEPTS)] if other['theory']['group'] == c['theory']['group'] and other['name'] != c['name']]
    related_links = ''.join(f'<a href="{other["name"]}.html">{esc(other["title"])}</a>' for other in related)
    archive = next(ch for ch in meta if ch['name']==c['chapter'])
    dependencies = '<p class="snippet-guide">코드 조각은 같은 페이지의 선언과 함께 사용합니다. main 밖 표시는 전역 선언, 나머지는 main 안에서 실행합니다. 기능에 맞는 헤더가 필요합니다. <a href="../examples.html">완전한 실행 예제 29개</a></p>' if '```cpp' in body else ''
    article_class = 'type-reference' if c['name'] == '02-io-types-01' else ''
    article = f'<div class="reading"><div class="reading-eyebrow">{esc(c["theory"]["group"])}</div><article class="{article_class}"><h1>{esc(c["title"])}</h1>{dependencies}<div class="extra-theory">{markdown(body)}</div><section id="related"><h2>관련 개념</h2><nav class="concept-navigation" aria-label="관련 개념">{related_links}</nav><p><a href="../chapters/{archive["name"]}.html#lesson-details">관련 응용 예제와 상세 해설</a></p></section></article><nav class="page-navigation">'
    if i: article += f'<a href="{NAV_META[i-1]["name"]}.html"><small>이전 개념</small>{esc(NAV_META[i-1]["title"])}</a>'
    else: article += '<a href="../index.html">전체 개념</a>'
    if i+1 < len(CONCEPTS): article += f'<a href="{NAV_META[i+1]["name"]}.html"><small>다음 개념</small>{esc(NAV_META[i+1]["title"])}</a>'
    else: article += '<a href="../examples.html">실행 예제</a>'
    article += '</nav></div>'
    (OUT/c['url']).write_text(shell(c['title'],article,'../',c['name'],toc),encoding='utf-8')
# Source chapters are archives; their first link leads back to independent concepts.
for c in meta[:13]:
    path=OUT/'chapters'/f'{c["name"]}.html'; text=path.read_text(encoding='utf-8')
    related = [topic for topic in NAV_META[:len(CONCEPTS)] if topic['chapter'] == c['name']]
    links = ''.join(f'<a href="../{topic["url"]}">{esc(topic["title"])}</a>' for topic in related)
    text=text.replace('<article>', '<article><blockquote>이 페이지는 기존 응용 해설 모음입니다. 개념은 아래 독립 페이지에서 읽으세요.</blockquote><nav class="concept-navigation">'+links+'</nav>',1)
    path.write_text(text,encoding='utf-8')
print(f'Built {len(CONCEPTS)} independent concepts; operators and conditionals have separate menus.')
