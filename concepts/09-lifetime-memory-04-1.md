# 복사 생성자

기존 객체를 이용해 새 객체를 초기화합니다.

## 개념과 동작 원리

기존 객체를 바탕으로 새 객체를 초기화하는 생성자입니다. 보통 T(const T&) 형태이며, 기본 동작은 각 멤버를 그 멤버의 복사 규칙으로 초기화합니다.

## 사용 시점과 다른 개념의 구분

값처럼 독립된 객체가 필요한 경우에 사용합니다. raw 포인터 소유자는 주소만 복사할지 자원을 복제할지 또는 복사를 금지할지 정책을 정해야 합니다.

## 문법과 예제

```cpp
std::string a = "Hero";
std::string b = a;
b[0] = 'Z';
std::cout << a << ' ' << b;
```

**결과:** Hero Zero. raw 포인터를 소유한 클래스는 기본 복사로 주소만 복사되면 중복 해제가 생길 수 있어 복사 정책이 필요합니다.

## 예제를 이해하는 순서

string b = a는 새 b를 만들며 내용을 복사합니다. b의 첫 문자를 바꿔도 a가 유지되는 것은 string이 독립 값의 복사 의미를 제공하기 때문입니다.

## 복사 생성자의 형태

```cpp
#include <iostream>
struct State {
    int hp;
    explicit State(int value) : hp(value) {}
    State(const State& other) : hp(other.hp) {
        std::cout << "Copy ";
    }
};
int main() {
    State original(100);
    State copied = original;
    copied.hp = 80;
    std::cout << original.hp << ' ' << copied.hp;
}
```

**결과:** Copy 100 80. `State(const State&)`가 기존 객체를 받아 새 객체를 초기화합니다. 이 예제는 원리를 보여 주려고 직접 정의했으며 int 멤버만 가진 타입은 보통 기본 복사로 충분합니다.

## 이해 확인

**질문:** 포인터 멤버의 기본 복사는 대상까지 복제하는가?

**답:** 아닙니다. 주소값이 복사되므로 자원 소유 타입은 중복 해제와 별칭 문제를 검토해야 합니다.
