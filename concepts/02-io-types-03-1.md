# cout 출력

<iostream>의 std::cout에 <<로 값을 출력합니다.

```cpp
int hp = 100;
std::cout << "HP: " << hp << '\n';
```

**결과:** HP: 100. \n은 줄바꿈, std::endl은 줄바꿈과 버퍼 flush를 함께 수행합니다.
