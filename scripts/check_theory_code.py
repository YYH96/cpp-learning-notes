"""Compile and run teaching snippets in their documented global/main scopes."""
from pathlib import Path
import subprocess, re, tempfile

root = Path(__file__).resolve().parents[1]
build = Path(tempfile.mkdtemp(prefix='cpp-theory-check-'))
headers = '\n'.join(f'#include <{name}>' for name in ['iostream', 'string', 'vector', 'list', 'limits', 'utility'])
dependencies = {
    '05-functions-scope': {1: ([0], [])},
    '08-structs-classes': {1: ([0], []), 3: ([2], [])},
    '09-lifetime-memory': {1: ([0], [])},
    '10-inheritance-polymorphism': {1: ([0], []), 2: ([0], [1])},
    '12-templates-operators': {1: ([0], []), 4: ([3], [])},
}
count = 0
for path in sorted((root/'theory').glob('*.md')):
    snippets = re.findall(r'```cpp\n([\s\S]*?)\n```', path.read_text(encoding='utf-8'))
    for index, snippet in enumerate(snippets):
        global_scope = 'main 밖' in snippet
        global_indexes, main_indexes = dependencies.get(path.stem, {}).get(index, ([], []))
        globals_text = '\n'.join(snippets[j] for j in global_indexes)
        main_text = '\n'.join(snippets[j] for j in main_indexes)
        if 'int main()' in snippet:
            source = headers+'\n'+snippet
        elif global_scope:
            source = headers+'\n'+snippet+'\nint main() {}\n'
        else:
            source = headers+'\n'+globals_text+'\nint main() {\n'+main_text+'\n'+snippet+'\n}\n'
        stem = f'{path.stem}-{index+1}'
        cpp = build/f'{stem}.cpp'; exe = build/f'{stem}.exe'; obj = build/f'{stem}.obj'
        cpp.write_text(source, encoding='utf-8')
        result = subprocess.run(['cl', '/nologo', '/std:c++17', '/EHsc', '/utf-8', str(cpp), f'/Fe:{exe}', f'/Fo:{obj}'], capture_output=True)
        if result.returncode:
            raise RuntimeError(f'{stem}: '+result.stdout.decode(errors='replace')+result.stderr.decode(errors='replace'))
        run = subprocess.run([str(exe)], input='20\nKim Hero\n', text=True, capture_output=True, timeout=3)
        if run.returncode: raise RuntimeError(f'{stem} exited with {run.returncode}')
        count += 1
print(f'Compiled and executed {count} teaching snippets with MSVC C++17.')
