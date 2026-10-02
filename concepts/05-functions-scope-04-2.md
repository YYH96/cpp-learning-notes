# namespace

이름 공간으로 이름의 소속을 구분합니다. ::로 소속을 지정합니다.

```cpp
namespace Game { constexpr int MaxHp = 100; } // main 밖
```

**사용:** Game::MaxHp는 100. std::cout의 std도 이름 공간입니다. 헤더에서 using namespace std를 광범위하게 쓰지 않습니다.
