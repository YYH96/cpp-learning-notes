# static_cast

명시적 숫자 변환 등에 사용합니다. 다운캐스팅 시 실제 객체 타입을 실행 중 검사하지 않습니다.

```cpp
int total = 7;
double average = static_cast<double>(total) / 2;
std::cout << average;
```

**결과:** 3.5. 나눗셈 후 변환하면 이미 버린 소수 부분은 복원되지 않습니다.
