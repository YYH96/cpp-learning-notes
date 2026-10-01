[← 전체 목차](../README.md) · [이전 챕터](08-structs-classes.md) · [다음 챕터 →](10-inheritance-polymorphism.md)

# 09. 생성자, 소멸자와 동적 할당

> **학습 목표** · 객체 수명과 동적 메모리의 생성·해제 책임을 이해한다.

## 이 페이지에서 다룰 내용

- [객체의 시작과 끝](#객체의-시작과-끝)
- [static 멤버](#static-멤버)
- [new/delete와 메모리 관리](#newdelete와-메모리-관리)
- [런타임 크기의 배열](#런타임-크기의-배열)

---

## 객체의 시작과 끝
생성자는 객체를 초기화하고 소멸자는 객체가 끝날 때 정리합니다. 멤버 초기화 목록은 생성자 뒤의 콜론으로 작성하며, 실제 초기화 순서는 멤버의 선언 순서입니다.
기본 생성자·매개변수 생성자·복사 생성자와 이동 생성자 개요를 배웠습니다. std::move는 그 자체로 데이터를 옮기는 명령이 아니라 이동을 선택할 수 있도록 표현식을 바꾸는 캐스트입니다.
= default는 기본 동작을 명시하고 = delete는 사용을 금지합니다. raw 포인터로 자원을 소유하는 객체를 기본 복사하면 같은 자원을 두 번 지울 수 있으므로 깊은 복사 또는 복사 금지가 필요합니다.
## static 멤버
static 멤버 변수는 객체마다 생기지 않고 클래스에서 공유합니다. static 멤버 함수에는 this가 없으며 클래스 이름으로 호출할 수 있습니다.

```cpp
#include <iostream>
class Monster {
    static int count;
public:
    Monster() { ++count; }
    ~Monster() { --count; }
    Monster(const Monster&) = delete;
    Monster& operator=(const Monster&) = delete;
    static int Count() { return count; }
};
int Monster::count = 0;
int main() {
    std::cout << Monster::Count() << '\n'; // 0
    {
        Monster a, b;
        std::cout << Monster::Count() << '\n'; // 2
    }
    std::cout << Monster::Count() << '\n'; // 0
}
```

📎 [실행할 예제 파일](../examples/19_lifetime.cpp)

## new/delete와 메모리 관리
new T는 객체 하나를 만들고 delete로 지웁니다. new T[n]은 배열을 만들고 delete[]로 지웁니다. raw 포인터가 범위를 벗어난다고 가리키는 동적 객체가 자동 삭제되지는 않습니다.
삭제 후 포인터를 nullptr로 만드는 것은 해당 변수의 재사용 실수를 줄이지만, 같은 객체를 가리키던 다른 포인터까지 바꾸지는 않습니다. malloc/free는 저장 공간을 다루며 C++ 클래스의 생성자·소멸자를 자동 호출하지 않습니다.
수업에서는 MSVC의 crtdbg와 _CrtSetDbgFlag로 메모리 누수를 확인하는 방법도 소개했습니다.
## 런타임 크기의 배열

```cpp
#include <iostream>
int main() {
    int count = 3;
    int* scores = new int[count]{};
    for (int i = 0; i < count; ++i) scores[i] = (i + 1) * 10;
    for (int i = 0; i < count; ++i) std::cout << scores[i] << ' ';
    std::cout << '\n';
    delete[] scores;
    scores = nullptr;
}
```

📎 [실행할 예제 파일](../examples/20_dynamic.cpp)

행별로 2차원 메모리를 할당했다면 **각 행을 delete[]한 뒤 행 포인터 배열을 delete[]**합니다. tic-tac-toe 실습은 이 자원을 클래스의 소멸자에서 정리하는 예입니다.

---

[← 전체 목차](../README.md) · [이전 챕터](08-structs-classes.md) · [다음 챕터 →](10-inheritance-polymorphism.md)
