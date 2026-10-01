const sidebar = document.querySelector('.sidebar');
const menu = document.querySelector('#menu-toggle');
menu.addEventListener('click', () => {
  const open = sidebar.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? '학습 목차 닫기' : '학습 목차 열기');
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') { sidebar.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); }
});
const search = document.querySelector('#chapter-search');
search.addEventListener('input', () => {
  const query = search.value.trim().toLowerCase();
  let matches = 0;
  document.querySelectorAll('.chapter-link').forEach(link => {
    link.hidden = !link.dataset.search.toLowerCase().includes(query);
    if (!link.hidden) matches++;
  });
  document.querySelectorAll('.chapter-card').forEach(card => { card.hidden = !card.dataset.search.toLowerCase().includes(query); });
  document.querySelector('.no-results').hidden = matches > 0;
  document.querySelectorAll('.nav-group').forEach(group => {
    group.hidden = !group.querySelector('.chapter-link:not([hidden])');
  });
  document.querySelectorAll('.topic-group').forEach(group => {
    group.hidden = !group.querySelector('.chapter-card:not([hidden])');
  });
});
document.querySelectorAll('a[href="#lesson-details"]').forEach(link => {
  link.addEventListener('click', () => { document.querySelector('#lesson-details').open = true; });
});
const toast = document.querySelector('.toast');
let toastTimer;
function notify(message) {
  toast.textContent = message; toast.classList.add('visible');
  clearTimeout(toastTimer); toastTimer = setTimeout(() => toast.classList.remove('visible'), 2400);
}
document.querySelectorAll('.copy-code').forEach(button => {
  button.addEventListener('click', async () => {
    const code = button.closest('.code-block').querySelector('code').textContent;
    try { await navigator.clipboard.writeText(code); notify('코드를 복사했습니다.'); }
    catch { notify('복사가 제한되었습니다. 코드를 선택해 복사해 주세요.'); }
  });
});
const storage = {
  get(key) { try { return localStorage.getItem(key); } catch { return null; } },
  set(key, value) { try { localStorage.setItem(key, value); } catch {} }
};
if (storage.get('cpp-notes-theme') === 'dark') document.documentElement.dataset.theme = 'dark';
document.querySelector('#theme-toggle').addEventListener('click', () => {
  const dark = document.documentElement.dataset.theme !== 'dark';
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
  storage.set('cpp-notes-theme', dark ? 'dark' : 'light');
});
document.querySelectorAll('.learning-check').forEach((checkbox, index) => {
  const key = `cpp-check-${location.pathname}-${index}`;
  checkbox.checked = storage.get(key) === 'true';
  checkbox.addEventListener('change', () => storage.set(key, String(checkbox.checked)));
});
// Highlight text tokens without interpreting C++ as HTML.
const escapeHtml = text => text.replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
document.querySelectorAll('.code-block pre code').forEach(code => {
  const pattern = /(\/\/[^\n]*|\/\*[\s\S]*?\*\/)|("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|\b(int|double|float|bool|char|void|return|if|else|for|while|class|struct|public|private|protected|virtual|override|const|static|template|typename|auto|new|delete|nullptr|true|false|enum|using|namespace|switch|case|break|continue)\b|\b(\d+(?:\.\d+)?)\b/g;
  const text = code.textContent; let end = 0; let rendered = '';
  for (const match of text.matchAll(pattern)) {
    rendered += escapeHtml(text.slice(end, match.index));
    const kind = match[1] ? 'comment' : match[2] ? 'string' : match[3] ? 'keyword' : 'number';
    rendered += `<span class="token-${kind}">${escapeHtml(match[0])}</span>`;
    end = match.index + match[0].length;
  }
  code.innerHTML = rendered + escapeHtml(text.slice(end));
});
