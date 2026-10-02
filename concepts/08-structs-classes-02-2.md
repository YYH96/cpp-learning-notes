# 접근 지정자

public은 외부 인터페이스, private은 클래스 내부와 friend, protected는 파생 클래스까지의 접근을 허용합니다.

```cpp
class Player { // main 밖
private:
    int hp = 100;
public:
    int GetHp() const { return hp; }
};
```

**예:** hero.GetHp()는 가능, hero.hp는 외부에서 불가. protected도 외부 코드에 공개되는 것은 아닙니다.
