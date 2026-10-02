# const와 constexpr

const는 객체의 변경을 제한하고, constexpr 변수는 컴파일 시간에 계산 가능한 상수를 나타냅니다.

## 개념과 동작 원리

const 객체는 초기화 후 해당 객체의 변경을 제한합니다. constexpr 변수는 상수식으로 초기화되어 컴파일 시간 상수로 사용할 수 있습니다.

## 사용 시점과 다른 개념의 구분

고정 규칙 값은 const, 배열 크기 등 상수식이 필요한 값은 constexpr를 고려합니다. constexpr 함수는 조건에 따라 실행 중에도 호출될 수 있습니다.

## 문법과 예제

```cpp
const int maxHp = 100;
constexpr int BoardSize = 3;
int board[BoardSize]{};
std::cout << maxHp << ' ' << BoardSize;
```

**결과:** 100 3. const라고 모두 컴파일 시간 상수인 것은 아닙니다. constexpr 초기값은 상수식이어야 합니다.

## 예제를 이해하는 순서

BoardSize는 상수식이어서 배열 크기로 쓸 수 있습니다. 실행 중 읽은 입력값을 const에 저장할 수는 있지만 constexpr 초기값으로 쓸 수는 없습니다.

## 이해 확인

**질문:** const는 모두 컴파일 시간 값인가?

**답:** 아닙니다. 변경 금지와 컴파일 시간 계산 가능성은 서로 다른 기준입니다.
