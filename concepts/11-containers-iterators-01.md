# vector: 인덱스로 접근

연속 저장하는 가변 배열입니다. 인덱스 접근은 빠르지만 중간 삽입·삭제에는 뒤 원소 이동이 필요합니다.

```cpp
std::vector<int> values{10, 20};
values.push_back(30);
std::cout << values[1] << ' ' << values.size();
```

**결과:** 20 3. []는 범위를 검사하지 않습니다. at()은 범위를 검사하고 범위 밖이면 예외를 발생시킵니다.

