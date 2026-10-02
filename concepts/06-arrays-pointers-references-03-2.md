# 값·포인터·참조 전달

T는 값 복사, T*는 주소 전달, T&는 참조 전달입니다. 원본을 읽기만 하는 큰 객체는 const T&를 고려합니다.

```cpp
void ByValue(int x) { x = 0; } // main 밖
void ByPointer(int* x) { if (x) *x = 0; }
void ByReference(int& x) { x = 0; }
```

**예:** int hp = 100; 뒤 ByValue(hp)는 원본 유지, ByPointer(&hp)와 ByReference(hp)는 hp를 0으로 바꿉니다. 참조 전달은 유효한 객체에 바인딩해야 합니다.
