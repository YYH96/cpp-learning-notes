# 기본 인자

호출에서 인자를 생략하면 미리 지정한 값을 사용합니다. 생략할 수 있는 인자는 뒤쪽에 둡니다.

```cpp
int Scale(int value, int factor = 2) { // main 밖
    return value * factor;
}
```

**결과:** Scale(3)은 6, Scale(3, 4)는 12. 선언과 정의에 같은 기본 인자를 중복 지정하지 않습니다.
