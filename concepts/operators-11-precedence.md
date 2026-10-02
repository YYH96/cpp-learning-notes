# 연산자 우선순위와 괄호

우선순위는 식이 어떻게 묶이는지 결정합니다. 식의 모든 피연산자를 실행하는 순서를 뜻하지는 않습니다.

| 높은 쪽부터 | 주요 연산자 | 기억할 예 |
| --- | --- | --- |
| 범위·접근·호출 | ::, ., ->, [], (), 후위 ++ -- | 객체 멤버와 함수 호출 |
| 단항 | 전위 ++ --, !, ~, 단항 + -, *, &, sizeof | !(hp > 0) |
| 곱셈 다음 덧셈 | * / %, 다음 + - | 2 + 3 * 4는 14 |
| 이동·비교·동등 | << >>, 다음 < <= > >=, 다음 == != | (flags & mask) != 0 |
| 비트 | &, 다음 ^, 다음 \| | 괄호로 의도 표시 |
| 논리 | &&, 다음 \|\| | a || (b && c) |
| 조건·대입 | ?:, =, += 등 | 대입은 오른쪽부터 묶임 |
| 쉼표 | , | 마지막 식의 값 사용 |

```cpp
int basic = 2 + 3 * 4;
int grouped = (2 + 3) * 4;
unsigned flags = 3, mask = 1;
bool enabled = (flags & mask) != 0;
std::cout << basic << ' ' << grouped << ' ' << enabled;
```

**결과:** 14 20 1.

**주의:** flags & mask != 0은 flags & (mask != 0)으로 묶입니다. 비트 확인에는 괄호를 씁니다. a - b - c는 (a - b) - c, a = b = c는 a = (b = c)로 묶입니다.

[우선순위 공식 참고: Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/cpp-built-in-operators-precedence-and-associativity?view=msvc-170)
