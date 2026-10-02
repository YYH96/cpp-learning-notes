## template: 타입을 매개변수로

같은 구조의 함수·클래스를 여러 타입에 적용합니다. 사용한 타입으로 필요한 코드가 컴파일 때 인스턴스화됩니다.

```cpp
template<typename T> // main 밖
T Add(T a, T b) {
    return a + b;
}
```

```cpp
std::cout << Add<int>(2, 3); // main 안
```

**결과:** 5. Add(2, 3)처럼 타입 추론도 가능합니다. 이 함수는 해당 타입의 + 연산과 반환이 유효해야 합니다. Add(2, 3.5)는 두 인자로 같은 T를 추론할 수 없어 실패합니다.

## auto: 초기값에서 타입 추론

```cpp
int hp = 100;
auto copy = hp;
auto& alias = hp;
alias = 80;
```

**결과:** hp와 alias는 80, copy는 100. auto가 항상 참조를 유지하는 것은 아닙니다. 읽기 전용 참조는 const auto&로 지정합니다.

## 연산자 오버로딩

사용자 정의 타입의 연산 의미를 정합니다. 기존 연산자의 우선순위·피연산자 개수는 바꾸지 못합니다.

```cpp
struct Position { // main 밖
    int x, y;
    bool operator==(const Position& other) const {
        return x == other.x && y == other.y;
    }
};
```

```cpp
Position a{1, 2}, b{1, 2}; // main 안
std::cout << (a == b);
```

**결과:** 1. 좌표 비교처럼 자연스러운 의미를 유지합니다. 함수 오버로딩과 연산자 오버로딩도 구분합니다.
