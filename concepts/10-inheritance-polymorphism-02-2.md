# 다형성

같은 인터페이스를 통해 서로 다른 실제 타입의 동작을 실행합니다.

## 개념과 동작 원리

같은 호출 계약으로 서로 다른 구현을 실행하는 성질입니다. 수업의 런타임 다형성은 상속·가상 함수·기반 포인터 또는 참조를 함께 사용해 표현합니다.

## 사용 시점과 다른 개념의 구분

여러 캐릭터 공격·여러 씬 갱신을 관리 코드 하나로 처리할 때 사용합니다. 타입별 분기를 매번 추가하는 대신 각 객체가 행동을 제공하게 합니다.

## 문법과 예제

**예:** Character&로 전사와 마법사의 Attack()을 호출하고 각 타입의 가상 함수 구현을 실행합니다.

**주의:** 값을 기반 객체로 복사하면 파생 부분이 잘리는 슬라이싱이 발생할 수 있습니다. 기반 포인터·참조와 가상 함수를 함께 사용합니다.

## 예제를 이해하는 순서

Character&로 전사와 마법사에 Attack을 호출하더라도 결과는 실제 객체의 구현을 따릅니다. 참조 자체의 선언 타입은 같지만 연결된 객체가 다릅니다.

## 같은 호출, 서로 다른 행동

```cpp
#include <iostream>
struct Character {
    virtual ~Character() = default;
    virtual int Attack() const = 0;
};
struct Warrior : Character {
    int Attack() const override { return 20; }
};
struct Mage : Character {
    int Attack() const override { return 35; }
};
int main() {
    Warrior warrior;
    Mage mage;
    Character* party[]{&warrior, &mage};
    for (const Character* member : party) {
        std::cout << member->Attack() << ' ';
    }
}
```

**결과:** 20 35. 관리 코드는 같은 Attack 호출을 쓰고, 실제 행동은 연결된 객체가 제공합니다. party는 관찰 포인터 배열이며 지역 객체를 delete하지 않습니다.

## 이해 확인

**질문:** 기반 클래스 값 변수에 파생 객체를 복사하면?

**답:** 파생 부분이 잘리는 슬라이싱이 생길 수 있으므로 원래 객체의 다형적 동작을 유지하려면 포인터·참조를 고려합니다.
