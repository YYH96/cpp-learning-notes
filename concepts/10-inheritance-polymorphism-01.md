# 상속: 공통 역할 확장

public 상속은 파생 객체를 기반 클래스의 역할로 사용할 수 있도록 합니다.

## 개념과 동작 원리

파생 클래스는 기반 클래스의 부분 객체와 자신의 추가 멤버를 구성합니다. public 상속은 파생 객체를 기반 역할로 사용할 수 있다는 관계를 표현합니다.

## 사용 시점과 다른 개념의 구분

캐릭터 공통 계약처럼 대체 가능한 타입 계층에 사용합니다. 단순 코드 재사용만 필요하면 객체를 멤버로 가지는 합성도 비교합니다.

## 문법과 예제

```cpp
class Character { // main 밖
public:
    virtual ~Character() = default;
    virtual int Attack() const { return 10; }
};
class Mage : public Character {
public:
    int Attack() const override { return 30; }
};
```

```cpp
Mage mage; // main 안
Character& character = mage;
std::cout << character.Attack();
```

**결과:** 30. 생성은 기반 클래스 다음 파생 클래스, 소멸은 반대 순서입니다.

## 예제를 이해하는 순서

Mage는 Character 인터페이스를 제공하며 Attack 동작을 재정의합니다. 생성은 기반에서 파생으로, 소멸은 파생에서 기반으로 진행됩니다.

## 이해 확인

**질문:** 기반의 private 멤버는 파생 객체에서 사라지는가?

**답:** 아닙니다. 기반 부분에 존재하지만 파생 클래스가 그 이름에 직접 접근할 수 없는 것입니다.
