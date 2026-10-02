## vector: 인덱스로 접근

연속 저장하는 가변 배열입니다. 인덱스 접근은 빠르지만 중간 삽입·삭제에는 뒤 원소 이동이 필요합니다.

```cpp
std::vector<int> values{10, 20};
values.push_back(30);
std::cout << values[1] << ' ' << values.size();
```

**결과:** 20 3. []는 범위를 검사하지 않습니다. at()은 범위를 검사하고 범위 밖이면 예외를 발생시킵니다.

## size·capacity·reserve·resize

| 기능 | 뜻 | 빈 vector에 호출한 예 |
| --- | --- | --- |
| size | 실제 원소 수 | 처음에는 0 |
| capacity | 재할당 없이 담을 수 있는 용량 | size 이상 |
| reserve(10) | 최소 용량 확보 | size는 여전히 0 |
| resize(10) | 원소 수 변경 | size가 10 |

**주의:** reserve만 한 뒤 v[0]에 쓰면 안 됩니다. 재할당은 기존 포인터·참조·반복자를 무효화합니다.

## list: 노드를 연결

위치를 알고 있을 때 삽입·삭제에 유리합니다. 인덱스 []는 제공하지 않으며 위치 탐색에는 순회가 필요합니다.

```cpp
std::list<int> values{10, 20};
values.push_front(5);
std::cout << values.front();
```

**결과:** 5. 빈 컨테이너에서 front·back·pop_back 등의 원소 접근·삭제는 피합니다.

## iterator와 삭제 후 순회

begin은 첫 원소, end는 마지막 원소 다음 경계입니다. **end는 역참조하지 않습니다.**

```cpp
std::list<int> values{1, 2, 3};
for (auto it = values.begin(); it != values.end();) {
    if (*it == 2) it = values.erase(it);
    else ++it;
}
```

**결과:** 1, 3만 남습니다. erase는 다음 반복자를 반환합니다. 삭제한 원소의 반복자를 계속 쓰면 안 됩니다.

## 직접 구현한 자료구조

- **IntVector:** 배열 포인터·size·capacity 관리. 공간 부족 시 새 배열로 복사하고 기존 배열 해제.
- **양방향 리스트:** 데이터·이전·다음 포인터를 가진 노드. 삽입·삭제 시 이웃 연결 변경.
- **직접 만든 반복자:** 노드 포인터와 이동·역참조 연산 구현.

**구분:** 표준 vector·list의 사용법과 학습용 자료구조의 내부 구현은 별개입니다. 긴 구현 해설은 아래 응용 영역에 둡니다.
