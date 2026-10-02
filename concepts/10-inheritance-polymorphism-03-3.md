# const_cast

포인터·참조의 const 등 한정자를 조정합니다. 원래부터 const인 객체를 수정하는 용도로 사용할 수 없습니다.

```cpp
int value = 10;
const int* view = &value;
int* writable = const_cast<int*>(view);
*writable = 20;
std::cout << value;
```

**결과:** 20. 원본 value는 const가 아니므로 가능합니다. 원본이 const int였다면 이런 수정은 정의되지 않은 동작입니다.
