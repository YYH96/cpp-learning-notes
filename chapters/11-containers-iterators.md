[← 전체 목차](../README.md) · [이전 챕터](10-inheritance-polymorphism.md) · [다음 챕터 →](12-templates-operators.md)

# 11. vector, list, 반복자와 직접 만든 자료구조

> **학습 목표** · 컨테이너와 반복자의 동작을 이해하고 직접 구현한 자료구조를 읽는다.

## 이 페이지에서 다룰 내용

- [vector: 연속된 가변 배열](#vector-연속된-가변-배열)
- [list와 iterator](#list와-iterator)
- [직접 구현한 IntVector](#직접-구현한-intvector)
- [직접 구현한 양방향 리스트](#직접-구현한-양방향-리스트)

---

## vector: 연속된 가변 배열
vector는 크기를 바꿀 수 있는 연속 저장 컨테이너입니다. size는 실제 요소 수, capacity는 재할당 없이 담을 수 있는 저장 용량입니다. reserve는 공간을 확보하고 resize는 요소 수를 바꿉니다.
reserve(10)만 호출한 빈 vector에는 아직 요소가 없으므로 v[0]을 사용할 수 없습니다. push_back 또는 resize로 요소를 만들어야 합니다. pop_back·back은 비어 있을 때 호출하지 않습니다.
clear는 요소를 없애 size를 0으로 만들며 capacity는 유지합니다. 용량 감소 요청에는 shrink_to_fit 등이 있지만 감소가 보장되는 요청은 아닙니다. 재할당은 기존 요소의 포인터·참조·반복자를 무효화할 수 있습니다. [vector 문서](https://learn.microsoft.com/en-us/cpp/standard-library/vector-class?view=msvc-170)

```cpp
#include <iostream>
#include <vector>
int main() {
    std::vector<int> values;
    values.reserve(10);
    std::cout << values.size() << '\n'; // 0
    values.push_back(10);
    values.push_back(20);
    values.resize(4, 0);
    values[2] = 30;
    for (int value : values) std::cout << value << ' '; // 10 20 30 0
    std::cout << '\n';
    if (!values.empty()) values.pop_back();
    auto oldCapacity = values.capacity();
    values.clear();
    std::cout << values.size() << ' ' << (values.capacity() == oldCapacity) << '\n'; // 0 1
    std::vector<std::vector<int>> board(3, std::vector<int>(4, 0));
    board[2][3] = 1;
}
```

📎 [실행할 예제 파일](../examples/23_vector.cpp)

**2차원 vector:** 바깥쪽만 resize했다고 모든 행 안에 열 요소가 생기는 것은 아닙니다. 사용할 각 행에도 필요한 크기를 만들어야 합니다. vector<T*>는 포인터 값만 관리하며 new로 만든 T 객체를 자동으로 delete하지 않습니다.
## list와 iterator
list는 노드를 앞뒤 포인터로 연결하는 양방향 리스트입니다. [] 임의 접근을 제공하지 않고 iterator로 이동합니다. begin은 첫 요소, end는 마지막 요소 다음의 경계입니다. 빈 컨테이너에서는 begin==end입니다. end를 역참조하지 않습니다.
위치를 이미 알고 있으면 list의 삽입·삭제는 효율적이지만 위치를 찾는 순회 비용도 고려해야 합니다. vector는 인덱스 접근과 연속 순회에 유리합니다.
erase는 삭제한 요소 다음을 가리키는 반복자를 반환합니다. 삭제한 반복자를 계속 쓰거나 마지막을 지운 뒤 end를 역참조하지 않도록 아래 패턴을 사용합니다.

```cpp
#include <iostream>
#include <list>
int main() {
    std::list<int> values{1,2,3,4,5};
    for (auto it = values.begin(); it != values.end();) {
        if (*it % 2 == 0) it = values.erase(it);
        else ++it;
    }
    values.insert(values.begin(), 99); // 지정 위치 앞에 삽입
    for (int value : values) std::cout << value << ' '; // 99 1 3 5
    std::cout << '\n';
}
```

📎 [실행할 예제 파일](../examples/24_list.cpp)

## 직접 구현한 IntVector
수업의 IntVector는 배열 포인터·size·capacity를 보관합니다. push_back에서 공간이 부족하면 새 배열을 할당하고 기존 요소를 복사한 뒤 기존 배열을 삭제합니다. capacity를 대략 두 배씩 키우면 매 삽입마다 재할당하는 비용을 줄일 수 있습니다.
operator[]가 int&를 반환하면 myvector[0] = 1004처럼 원소를 수정할 수 있습니다. assert는 개발 중 전제를 검사하는 도구이며 Release 설정에서 빠질 수 있으므로 모든 런타임 검증을 대신하지 않습니다.
## 직접 구현한 양방향 리스트
ListNode는 데이터·이전 노드·다음 노드를 보관합니다. 시작·끝 더미 노드는 경계 처리를 단순하게 합니다. push_front/back은 이웃 포인터를 연결하고, erase는 이웃을 직접 연결한 뒤 노드를 지웁니다. clear에서는 삭제하기 전에 다음 노드 주소를 저장합니다.
ListIterator는 노드 포인터를 보관하고 ==·!=·++·--·*를 구현합니다. 전위 증감은 자신을 참조로 반환하고, 후위 증감은 변경 전 복사본을 값으로 반환합니다. friend로 리스트와 반복자에 필요한 내부 접근을 허용했습니다.
원본 IntVector와 myLinkedList는 표준 라이브러리의 모든 동작을 구현한 클래스는 아닙니다. 빈 상태에서 삭제하기, 복사 대입, 삽입 반환값 등 원문별 보완 사항을 코드 페이지에서 확인할 수 있습니다.

---

[← 전체 목차](../README.md) · [이전 챕터](10-inheritance-polymorphism.md) · [다음 챕터 →](12-templates-operators.md)
