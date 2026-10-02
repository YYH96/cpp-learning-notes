# 이동과 std::move

std::move는 이동을 허용하는 값 범주로 바꿉니다. 그 자체로 자원을 옮기지 않으며 이후 선택된 이동 연산이 처리합니다.

```cpp
std::string a = "Hero";
std::string b = std::move(a);
std::cout << b;
```

**결과:** Hero. 이동 후 a는 유효하지만 값은 단정하지 않습니다. 이동이 제공되지 않으면 복사가 선택될 수도 있습니다.
