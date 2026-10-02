# 함수 오버로딩

같은 이름의 함수를 매개변수의 타입·개수 차이로 구분합니다. 반환형만 다르면 구분할 수 없습니다.

```cpp
int Add(int a, int b) { return a + b; } // main 밖
double Add(double a, double b) { return a + b; }
```

**예:** Add(2, 3)은 int 버전, Add(2.5, 3.0)은 double 버전. 모호한 변환이 생기면 호출이 실패할 수 있습니다.
