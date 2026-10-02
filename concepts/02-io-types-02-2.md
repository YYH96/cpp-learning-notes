# const와 constexpr

const는 객체의 변경을 제한하고, constexpr 변수는 컴파일 시간에 계산 가능한 상수를 나타냅니다.

```cpp
const int maxHp = 100;
constexpr int BoardSize = 3;
int board[BoardSize]{};
std::cout << maxHp << ' ' << BoardSize;
```

**결과:** 100 3. const라고 모두 컴파일 시간 상수인 것은 아닙니다. constexpr 초기값은 상수식이어야 합니다.
