# 정수 나눗셈과 형변환

```cpp
int total = 5;
double wrong = total / 2;
double correct = static_cast<double>(total) / 2;
```

**결과:** wrong은 2.0, correct는 2.5. 계산이 끝난 뒤 double에 저장해도 이미 버린 소수 부분은 복구되지 않습니다.
