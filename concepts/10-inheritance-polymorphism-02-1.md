# 가상 함수와 override

virtual 함수는 기반 포인터·참조로 호출해도 실제 객체의 재정의를 사용합니다. override는 재정의의 타입·시그니처 오류를 검사합니다.

```cpp
class Base { // main 밖
public:
    virtual ~Base() = default;
    virtual int Power() const { return 10; }
};
class Mage : public Base {
public:
    int Power() const override { return 30; }
};
```

**예:** Mage m; Base& b = m;에서 b.Power()는 30. 비가상 함수는 이런 방식으로 동적 연결되지 않습니다.
