# struct와 class

둘 다 멤버 변수와 함수를 가질 수 있습니다. 기본 멤버·상속 접근 권한은 struct가 public, class가 private입니다.

```cpp
struct Position { int x; int y; }; // main 밖
```

**예:** Position p{1, 2};에서 p.x는 1. 단순 데이터 묶음은 struct, 상태의 규칙을 감추는 설계는 class를 자주 사용합니다.
