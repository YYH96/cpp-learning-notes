# iterator와 삭제 후 순회

begin은 첫 원소, end는 마지막 원소 다음 경계입니다. **end는 역참조하지 않습니다.**

```cpp
std::list<int> values{1, 2, 3};
for (auto it = values.begin(); it != values.end();) {
    if (*it == 2) it = values.erase(it);
    else ++it;
}
```

**결과:** 1, 3만 남습니다. erase는 다음 반복자를 반환합니다. 삭제한 원소의 반복자를 계속 쓰면 안 됩니다.

