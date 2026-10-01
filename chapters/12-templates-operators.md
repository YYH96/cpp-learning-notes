[← 전체 목차](../README.md) · [이전 챕터](11-containers-iterators.md) · [다음 챕터 →](13-game-design.md)

# 12. 템플릿, auto와 연산자 오버로딩

> **학습 목표** · 자료형에 독립적인 함수와 사용자 정의 연산을 작성한다.

## 이 페이지에서 다룰 내용

- [자료형에 공통인 설계](#자료형에-공통인-설계)
- [함수·클래스 템플릿](#함수클래스-템플릿)
- [좌표 비교 연산자](#좌표-비교-연산자)

---

## 자료형에 공통인 설계
템플릿은 자료형만 달라지고 구조·로직이 같은 함수나 클래스를 하나의 설계로 표현합니다. 실제 사용하는 타입에 따라 컴파일러가 필요한 코드를 인스턴스화합니다.
auto는 초기식으로부터 타입을 추론하며 실행 중 타입이 자유롭게 바뀌는 변수를 만드는 기능은 아닙니다. const T&는 불필요한 복사를 줄이고 읽기 목적으로 입력을 받습니다.
## 함수·클래스 템플릿

```cpp
#include <iostream>
#include <string>
template<typename T>
T Add(T left, T right) { return left + right; }
template<typename T>
class Cube {
    T first, second;
public:
    Cube(const T& a, const T& b) : first(a), second(b) {}
    const T& GetFirst() const { return first; }
};
int main() {
    std::cout << Add<int>(10, 20) << '\n'; // 30
    std::cout << Add<double>(1.5, 2.5) << '\n'; // 4
    Cube<std::string> weapons("Sword", "Shield");
    std::cout << weapons.GetFirst() << '\n';
}
```

📎 [실행할 예제 파일](../examples/25_template.cpp)

## 좌표 비교 연산자
사용자 정의 타입에도 의미 있는 연산자를 구현할 수 있습니다. 좌표는 x·y가 모두 같을 때 ==가 참입니다. 자료구조에서는 []·*·++ 등도 구현했습니다.

```cpp
#include <iostream>
struct Position {
    int x = 0, y = 0;
    bool operator==(const Position& other) const {
        return x == other.x && y == other.y;
    }
    bool operator!=(const Position& other) const { return !(*this == other); }
};
int main() {
    Position snake{3,4}, apple{3,4};
    std::cout << (snake == apple) << '\n'; // 1
}
```

📎 [실행할 예제 파일](../examples/26_operator.cpp)

---

[← 전체 목차](../README.md) · [이전 챕터](11-containers-iterators.md) · [다음 챕터 →](13-game-design.md)
