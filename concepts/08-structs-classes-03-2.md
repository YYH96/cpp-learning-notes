# 캡슐화와 정보 은닉

캡슐화는 데이터와 동작을 묶는 것, 정보 은닉은 내부 접근을 제한하는 것입니다.

```cpp
class Player { // main 밖
    int hp = 100;
public:
    void Damage(int amount) {
        if (amount > 0) hp = amount < hp ? hp - amount : 0;
    }
    int GetHp() const { return hp; }
};
```

**예:** Damage(120) 뒤 GetHp()는 0. Getter는 조회, Setter는 검증된 변경을 맡습니다. const 멤버 함수는 조회에 사용합니다.
