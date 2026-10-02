# resize

vector의 실제 원소 수를 변경합니다. 늘리면 새 원소를 만들고 줄이면 뒤 원소를 제거합니다.

```cpp
std::vector<int> values;
values.resize(3, 7);
std::cout << values.size() << ' ' << values[0];
```

**결과:** 3 7. 원소 수를 줄인다고 capacity가 함께 줄어드는 것은 아닙니다.
