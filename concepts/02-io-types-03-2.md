# cin 입력

<iostream>의 std::cin에서 >>로 값을 읽습니다. 문자열은 기본적으로 공백에서 끊깁니다.

```cpp
int score = 0;
if (std::cin >> score) std::cout << score;
else std::cout << "Invalid input";
```

**예:** 20 입력 시 20 출력. 숫자 변환 실패 시 스트림 상태를 확인하고 복구해야 합니다.
