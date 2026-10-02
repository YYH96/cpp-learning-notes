# auto: 초기값에서 타입 추론

```cpp
int hp = 100;
auto copy = hp;
auto& alias = hp;
alias = 80;
```

**결과:** hp와 alias는 80, copy는 100. auto가 항상 참조를 유지하는 것은 아닙니다. 읽기 전용 참조는 const auto&로 지정합니다.

