# 싱글톤

하나의 인스턴스를 제공하는 패턴입니다. 전역 상태와 의존이 커지므로 필요한 경우에 제한적으로 사용합니다.

```cpp
class Manager { // main 밖
    Manager() = default;
public:
    static Manager& Instance() { static Manager value; return value; }
    Manager(const Manager&) = delete;
    Manager& operator=(const Manager&) = delete;
};
```

**예:** Manager::Instance()는 같은 인스턴스를 반환합니다. 인스턴스 생성의 안전성과 그 내부 상태 변경의 동시성 안전성은 별개입니다.
