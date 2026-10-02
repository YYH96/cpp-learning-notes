# 생성자와 초기화 목록

객체 생성 시 멤버를 초기화합니다. 생성자는 클래스와 이름이 같고 반환형을 쓰지 않습니다.

```cpp
class Player { // main 밖
    int hp;
public:
    explicit Player(int value) : hp(value) {}
    int GetHp() const { return hp; }
};
```

**예:** Player hero(100); 뒤 hero.GetHp()는 100. 멤버는 초기화 목록의 표기 순서가 아니라 선언 순서로 초기화됩니다.
