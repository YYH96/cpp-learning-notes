# this 포인터

비정적 멤버 함수에서 현재 객체를 가리킵니다. 매개변수와 멤버 이름이 같을 때 멤버를 분명히 지정할 수 있습니다.

```cpp
class Player { // main 밖
    int hp = 100;
public:
    void SetHp(int hp) { this->hp = hp; }
    int GetHp() const { return hp; }
};
```

**예:** hero.SetHp(80)을 호출하면 그 객체의 hp가 80. static 멤버 함수에는 this가 없습니다.
