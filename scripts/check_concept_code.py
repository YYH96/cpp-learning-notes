"""Compile every independently documented concept snippet with its local declarations."""
from pathlib import Path
import subprocess, re, tempfile
root=Path(__file__).resolve().parents[1]
build=Path(tempfile.mkdtemp(prefix='cpp-concepts-check-'))
headers='\n'.join('#include <'+name+'>' for name in ['iostream','string','vector','list','limits','utility','cstring'])
count=0
expected={'operators-01-arithmetic':'10 4 21 2 1','operators-02-assignment':'85','operators-03-increment':'3 5 5','operators-04-comparison':'true true','operators-05-logical':'false true false','operators-06-bitwise':'1 2','operators-07-conditional':'Alive 7','operators-08-address':'80 80','operators-09-access':'90 20','operators-10-size-cast-memory':'3.5 3','operators-11-precedence':'14 20 1','operators-12-stream-comma':'4 8'}
for path in sorted((root/'concepts').glob('*.md')):
    snippets=re.findall(r'```cpp\n([\s\S]*?)\n```',path.read_text(encoding='utf-8'))
    declarations=[s for s in snippets if 'main 밖' in s]
    for index,snippet in enumerate(snippets):
        if 'int main()' in snippet: source=headers+'\n'+snippet
        elif 'main 밖' in snippet: source=headers+'\n'+snippet+'\nint main() {}'
        else: source=headers+'\n'+'\n'.join(declarations)+'\nint main() {\n'+snippet+'\n}'
        stem=f'{path.stem}-{index}';cpp=build/f'{stem}.cpp';exe=build/f'{stem}.exe';obj=build/f'{stem}.obj'
        cpp.write_text(source,encoding='utf-8')
        compile=subprocess.run(['cl','/nologo','/std:c++17','/EHsc','/utf-8',str(cpp),f'/Fe:{exe}',f'/Fo:{obj}'],capture_output=True)
        if compile.returncode:raise RuntimeError(stem+': '+compile.stdout.decode(errors='replace'))
        run=subprocess.run([str(exe)],input='20\nKim Hero\n',text=True,capture_output=True,timeout=3)
        if run.returncode:raise RuntimeError(stem+': execution failed')
        if path.stem in expected:assert run.stdout.strip()==expected[path.stem],(stem,run.stdout)
        count+=1
print(f'Compiled and executed {count} concept snippets; all 12 operator outputs matched.')
