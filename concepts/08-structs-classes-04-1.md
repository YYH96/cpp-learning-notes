# enum

이름을 붙인 정수 상수들의 집합입니다. 일반 enum의 열거자는 둘러싼 범위에 들어가고 정수로 암시적 변환할 수 있습니다.

```cpp
enum Direction { Left, Right }; // main 밖
```

**예:** Direction d = Right; int value = d;에서 value는 1. 이름 충돌을 줄이려면 enum class를 고려합니다.
