# 소멸자

객체 수명이 끝날 때 정리 작업을 수행합니다. 클래스 이름 앞에 ~를 붙이고 인자를 받지 않습니다.

```cpp
class Trace { // main 밖
public:
    ~Trace() { std::cout << "Destroyed"; }
};
```

**예:** { Trace value; } 블록 종료 시 Destroyed 출력. 기반 포인터로 파생 객체를 삭제하는 설계에는 가상 소멸자가 필요합니다.
