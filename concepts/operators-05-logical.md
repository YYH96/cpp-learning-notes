# 논리 연산자와 단락 평가

조건의 참·거짓을 결합합니다. 기본 내장 &&, ||는 필요한 만큼만 평가합니다.

| 기호 | 의미 | 참이 되는 조건 |
| --- | --- | --- |
| && | AND | 양쪽 모두 참 |
| \|\| | OR | 한쪽 이상 참 |
| ! | NOT | 원래 조건이 거짓 |

```cpp
int hp = 80, mana = 0;
bool attack = hp > 0 && mana >= 10;
bool recover = hp < 30 || mana == 0;
int* target = nullptr;
bool valid = target != nullptr && *target > 0;
std::cout << std::boolalpha << attack << ' ' << recover << ' ' << valid;
```

**결과:** false true false. target이 nullptr이면 오른쪽 *target은 평가하지 않습니다.

**주의:** &&는 왼쪽이 거짓이면, ||는 왼쪽이 참이면 오른쪽을 건너뜁니다. &와 |는 비트 연산이며 단락 평가를 제공하지 않습니다. !은 비교보다 우선하므로 !(hp > 0)처럼 의도를 괄호로 표시합니다.
