# 씬 전환과 다형성

기존 씬 Exit, 현재 씬 변경, 새 씬 Enter 순서로 전환합니다. 여러 씬은 공통 Update·Draw 인터페이스로 실행합니다.

```cpp
class Scene { // main 밖: 공통 계약
public:
    virtual ~Scene() = default;
    virtual void Update() = 0;
    virtual void Draw() = 0;
};
```

**결과:** Scene 자체는 추상 클래스. 파생 씬이 Update와 Draw를 구현해야 구체 객체를 만들 수 있습니다.

