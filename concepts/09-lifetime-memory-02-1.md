# static 지역 변수

이름은 함수의 블록에 속하지만 값은 호출 사이에도 유지됩니다.

```cpp
int NextId() { // main 밖
    static int count = 0;
    return ++count;
}
```

**결과:** 연속 호출하면 1, 2, 3. 일반 지역 변수처럼 호출마다 0으로 재설정되지 않습니다.
