# static 멤버

클래스의 모든 객체가 공유하는 변수와 객체 없이 호출할 수 있는 함수입니다.

```cpp
class Counter { // main 밖: C++17
public:
    inline static int count = 0;
    static void Increase() { ++count; }
};
```

**예:** Counter::Increase() 뒤 Counter::count는 1. static 멤버 함수에는 this가 없어 비정적 멤버에 바로 접근할 수 없습니다.
