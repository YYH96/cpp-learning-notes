# list: 노드를 연결

위치를 알고 있을 때 삽입·삭제에 유리합니다. 인덱스 []는 제공하지 않으며 위치 탐색에는 순회가 필요합니다.

```cpp
std::list<int> values{10, 20};
values.push_front(5);
std::cout << values.front();
```

**결과:** 5. 빈 컨테이너에서 front·back·pop_back 등의 원소 접근·삭제는 피합니다.

