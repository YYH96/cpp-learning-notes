# 연산자 오버로딩

사용자 정의 타입의 연산 의미를 정합니다. 기존 연산자의 우선순위·피연산자 개수는 바꾸지 못합니다.

```cpp
struct Position { // main 밖
    int x, y;
    bool operator==(const Position& other) const {
        return x == other.x && y == other.y;
    }
};
```

```cpp
Position a{1, 2}, b{1, 2}; // main 안
std::cout << (a == b);
```

**결과:** 1. 좌표 비교처럼 자연스러운 의미를 유지합니다. 함수 오버로딩과 연산자 오버로딩도 구분합니다.
