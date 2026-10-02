# 클래스와 객체의 기본

클래스는 데이터와 동작의 설계도, 객체는 그 타입으로 만든 실제 대상입니다.

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

