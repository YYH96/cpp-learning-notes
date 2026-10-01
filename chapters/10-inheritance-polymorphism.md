[← 전체 목차](../README.md) · [이전 챕터](09-lifetime-memory.md) · [다음 챕터 →](11-containers-iterators.md)

# 10. 상속, 가상 함수, 추상 클래스와 캐스팅

> **학습 목표** · 가상 함수와 추상 클래스로 공통 인터페이스를 설계한다.

## 이 페이지에서 다룰 내용

- [상속과 호출 순서](#상속과-호출-순서)
- [virtual·override·추상 클래스](#virtualoverride추상-클래스)
- [C++ 캐스트 4종](#c-캐스트-4종)
- [검사한 뒤 사용하는 다운캐스팅](#검사한-뒤-사용하는-다운캐스팅)

---

## 상속과 호출 순서
public 상속에서는 파생 객체를 기반 객체의 역할로 사용할 수 있습니다. 부모의 private 멤버는 파생 클래스에서 직접 접근하지 못합니다. 생성은 부모 → 자식, 소멸은 자식 → 부모 순서로 진행됩니다.
다중 상속은 여러 기반 클래스를 가질 수 있지만 같은 이름과 공통 기반 클래스 때문에 모호성이 생길 수 있습니다. 수업에서는 CPU·GPU가 Device를 함께 상속하는 다이아몬드 형태와 명시적 부모 이름으로 호출하는 예를 다뤘습니다.
## virtual·override·추상 클래스
기반 포인터·참조를 통해 호출하더라도 실제 객체의 재정의 함수를 실행하려면 기반 함수가 virtual이어야 합니다. override는 재정의가 맞는지 컴파일러가 검사하게 합니다.
순수 가상 함수는 virtual void Use() = 0;처럼 선언합니다. 아직 구현되지 않은 순수 가상 함수가 있는 클래스는 직접 객체를 만들 수 없습니다. 기반 포인터로 파생 객체를 삭제하는 설계에는 기반의 virtual 소멸자가 필요합니다. [가상 함수 문서](https://learn.microsoft.com/en-us/cpp/cpp/virtual-functions?view=msvc-170)
오버로딩은 매개변수가 다른 같은 이름의 함수, 오버라이딩은 상속받은 가상 함수의 재정의입니다. vtable은 흔히 사용하는 구현 방식이며 언어가 특정 테이블 구조를 강제하는 것은 아닙니다.

```cpp
#include <iostream>
class Skill {
public:
    virtual ~Skill() = default;
    virtual void Use() = 0;
};
class FireBall : public Skill {
public:
    void Use() override { std::cout << "Fireball\n"; }
};
class Heal : public Skill {
public:
    void Use() override { std::cout << "Heal\n"; }
};
int main() {
    Skill* skills[2] = {new FireBall, new Heal};
    for (Skill* skill : skills) {
        skill->Use();
        delete skill;
    }
}
```

📎 [실행할 예제 파일](../examples/21_polymorphism.cpp)

**결과:** Fireball, Heal. 원본 virtual.cpp에서 Character::AttackFunc는 virtual이 아니므로 Character*로 호출하면 Character 버전이 호출됩니다. 위 예제는 기반에 virtual을 둔 동작을 보여줍니다.
## C++ 캐스트 4종
**static_cast:** 숫자 변환과 검사 가능한 명시적 변환에 사용합니다. 실수 → 정수는 소수 부분이 사라집니다. 다운캐스팅에서 실제 타입을 실행 중 검증해주지는 않습니다.
**dynamic_cast:** 다형적 기반 타입에서 실제 객체의 타입을 확인하며 내려갑니다. 포인터 변환 실패는 nullptr, 참조 변환 실패는 std::bad_cast입니다.
**const_cast:** const 속성을 제거하거나 더합니다. 실제로 const인 객체를 이 방법으로 수정하면 정의되지 않은 동작입니다. 원래 수정 가능한 객체를 const 포인터로 보고 있던 경우와 구분합니다. [const_cast 문서](https://learn.microsoft.com/en-us/cpp/cpp/const-cast-operator?view=msvc-170)
**reinterpret_cast:** 주소 등의 저수준 표현을 다룹니다. 관련 없는 객체 타입으로 변환해서 그 타입인 것처럼 접근해도 안전해지는 것은 아닙니다.
## 검사한 뒤 사용하는 다운캐스팅

```cpp
#include <iostream>
class Parent { public: virtual ~Parent() = default; };
class Warrior : public Parent {
public:
    void Attack() { std::cout << "Sword attack\n"; }
};
class Mage : public Parent {};
int main() {
    Parent* character = new Warrior;
    if (auto* warrior = dynamic_cast<Warrior*>(character)) warrior->Attack();
    std::cout << (dynamic_cast<Mage*>(character) == nullptr) << '\n';
    delete character;
    int value = 5;                  // 원래 const가 아님
    const int* read = &value;
    int* write = const_cast<int*>(read);
    *write = 10;
    std::cout << value << '\n';
}
```

📎 [실행할 예제 파일](../examples/22_cast.cpp)

---

[← 전체 목차](../README.md) · [이전 챕터](09-lifetime-memory.md) · [다음 챕터 →](11-containers-iterators.md)
