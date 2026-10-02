# enum class

열거자 이름의 범위를 타입 안으로 제한하며 정수로 자동 변환하지 않습니다.

```cpp
enum class Direction { Left, Right }; // main 밖
```

```cpp
Direction d = Direction::Right;
int value = static_cast<int>(d);
std::cout << value;
```

**결과:** 1. Direction::Right처럼 타입 이름을 붙입니다.
