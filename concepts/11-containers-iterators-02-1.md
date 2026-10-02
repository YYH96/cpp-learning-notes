# vector의 size와 capacity

size는 실제 원소 수, capacity는 재할당 없이 담을 수 있는 용량입니다. capacity는 size 이상입니다.

```cpp
std::vector<int> values{1, 2};
std::cout << values.size();
```

**결과:** 2. capacity가 정확히 얼마인지는 구현·사용 과정에 따라 달라질 수 있습니다. 인덱스 범위는 capacity가 아니라 size로 확인합니다.
