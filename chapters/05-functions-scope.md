[← 전체 목차](../README.md) · [이전 챕터](04-loops.md) · [다음 챕터 →](06-arrays-pointers-references.md)

# 05. 함수, 오버로딩, 재귀와 범위

> **학습 목표** · 기능을 함수로 분리하고 재귀·오버로딩·이름 범위를 설명한다.

## 이 페이지에서 다룰 내용

- [함수를 만드는 이유](#함수를-만드는-이유)
- [오버로딩과 기본 인자](#오버로딩과-기본-인자)
- [재귀와 종료 조건](#재귀와-종료-조건)
- [스코프·수명·namespace](#스코프수명namespace)

---

## 함수를 만드는 이유
입력·계산·출력을 별도 기능으로 분리하면 중복을 줄이고 흐름을 읽기 쉬워집니다. 함수에는 반환형·이름·매개변수·본문이 있습니다. 호출 전에 선언이 보여야 하며, 함수 선언(프로토타입)을 먼저 두면 구현은 뒤에 둘 수 있습니다.
매개변수(parameter)는 선언에 쓰는 변수, 인자(argument)는 호출할 때 전달하는 값입니다. void는 반환값이 없는 함수에 씁니다.
## 오버로딩과 기본 인자
같은 이름이라도 매개변수의 개수·자료형이 다르면 오버로딩할 수 있습니다. 반환형만 달라서는 구분하지 못합니다. 기본 인자는 오른쪽부터 생략할 수 있도록 끝부분의 매개변수에 지정합니다.

```cpp
#include <iostream>
int Add(int a, int b = 10);
double Add(double a, double b);
int main() {
    std::cout << Add(5) << '\n';        // 15
    std::cout << Add(2, 3) << '\n';     // 5
    std::cout << Add(1.5, 2.5) << '\n'; // 4
}
int Add(int a, int b) { return a + b; }
double Add(double a, double b) { return a + b; }
```

📎 [실행할 예제 파일](../examples/08_functions.cpp)

## 재귀와 종료 조건
재귀는 함수가 자기 자신을 호출하는 방식입니다. 종료 조건과 종료 조건으로 가까워지는 변화가 필요합니다. 일반 재귀는 반환 후 남은 계산이 있고, 꼬리 재귀는 다음 호출이 마지막 작업입니다. C++에서 꼬리 재귀가 항상 반복문으로 최적화되는 것은 아닙니다.
수업에서는 합계·팩토리얼·피보나치 규칙을 다뤘습니다. 피보나치 원본은 숙제 안내이므로 아래 구현은 복습을 위해 추가한 예제입니다.

```cpp
#include <iostream>
// 전제: 0 <= n <= 12 (이 예제는 int 범위를 고려)
int Factorial(int n) {
    if (n <= 1) return 1;
    return n * Factorial(n - 1);
}
int SumTail(int n, int acc = 0) {
    if (n <= 0) return acc;
    return SumTail(n - 1, acc + n);
}
// 수업의 1, 1, 2, 3, ... 규칙, 전제: 1 <= n <= 46
int Fibonacci(int n) {
    if (n <= 2) return 1;
    int a = 1, b = 1;
    for (int i = 3; i <= n; ++i) {
        int next = a + b;
        a = b;
        b = next;
    }
    return b;
}
int main() {
    std::cout << Factorial(5) << ' ' << SumTail(10) << ' ' << Fibonacci(10) << '\n';
}
```

📎 [실행할 예제 파일](../examples/09_recursion.cpp)

**결과:** 120 55 55. 팩토리얼은 값이 빠르게 커지므로 입력 범위를 고려해야 합니다.
## 스코프·수명·namespace
스코프는 이름을 사용할 수 있는 범위, 수명은 객체가 존재하는 기간입니다. 일반 지역 변수는 블록을 벗어나면 소멸하고, 함수의 static 지역 변수는 호출 사이에 값을 유지합니다. 전역 변수는 함수 밖에 선언합니다.
namespace는 관련 이름을 묶어 이름 충돌을 줄입니다. 메모리의 코드·데이터·스택·힙 구분은 실행 환경을 이해하는 모델이며 C++ 표준이 모든 객체의 물리적 배치를 고정하는 것은 아닙니다.

```cpp
#include <iostream>
namespace Game {
    int NextID() {
        static int count = 0;
        return ++count;
    }
}
int main() {
    int count = 100;
    std::cout << Game::NextID() << ' ' << Game::NextID() << ' ' << count << '\n';
}
```

📎 [실행할 예제 파일](../examples/10_scope.cpp)

---

[← 전체 목차](../README.md) · [이전 챕터](04-loops.md) · [다음 챕터 →](06-arrays-pointers-references.md)
