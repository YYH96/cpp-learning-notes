# reserve

vector의 최소 용량을 확보합니다. 실제 원소 수는 늘리지 않습니다.

```cpp
std::vector<int> values;
values.reserve(10);
std::cout << values.size() << ' ' << (values.capacity() >= 10);
```

**결과:** 0 1. 아직 values[0]에 접근하면 안 됩니다. 재할당이 발생하면 기존 포인터·참조·반복자가 무효화됩니다.
