# 추상 클래스와 순수 가상 함수

순수 가상 함수 = 0은 파생 타입이 제공할 계약입니다. 미구현 순수 가상 함수가 남은 클래스는 직접 객체로 만들 수 없습니다.

```cpp
class Scene { // main 밖
public:
    virtual ~Scene() = default;
    virtual void Update() = 0;
};
```

**예:** Scene scene;은 불가. 구체 파생 클래스가 Update를 구현해야 합니다.
