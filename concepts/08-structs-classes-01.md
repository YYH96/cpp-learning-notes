# 클래스와 객체의 기본

클래스는 데이터와 동작의 설계도, 객체는 그 타입으로 만든 실제 대상입니다.

## 개념과 동작 원리

클래스는 상태와 동작을 가진 사용자 정의 타입이고 객체는 그 타입의 실제 인스턴스입니다. 비정적 멤버 변수는 각 객체가 별도로 가지며 멤버 함수는 호출 대상 객체의 상태를 다룹니다.

## 사용 시점과 다른 개념의 구분

플레이어·보드처럼 여러 값과 그 값을 다루는 규칙을 함께 관리할 때 사용합니다. 타입 정의와 객체 생성은 서로 다른 단계입니다.

## 문법과 예제

```cpp
class Player { // main 밖
public:
    int hp = 100;
    void Damage(int amount) { hp -= amount; }
};
```

```cpp
Player hero; // main 안: 객체 생성
hero.Damage(20);
std::cout << hero.hp;
```

**결과:** 80. 위 public 데이터는 문법 설명용입니다. 실제 설계에서는 private 데이터와 검증된 함수를 통해 상태를 관리합니다.

## 예제를 이해하는 순서

Player 정의 자체가 hero의 체력을 저장하는 것은 아닙니다. Player hero를 만든 뒤 hero.Damage(20)이 그 객체의 hp를 80으로 변경합니다.

## 이해 확인

**질문:** 같은 클래스 객체 둘은 hp도 공유하는가?

**답:** 일반 비정적 멤버는 객체마다 별개입니다. 공유가 필요하면 static 등 별도 설계가 필요합니다.

## 참고 문서

[클래스와 구조체 · Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/classes-and-structs-cpp?view=msvc-170)
