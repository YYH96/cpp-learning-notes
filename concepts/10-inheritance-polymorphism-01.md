# 상속: 공통 역할 확장

public 상속은 파생 객체를 기반 클래스의 역할로 사용할 수 있도록 합니다.

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

