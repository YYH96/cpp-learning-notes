# while: 조건이 참인 동안

본문을 실행하기 전에 조건을 검사합니다. 처음부터 거짓이면 한 번도 실행하지 않습니다.

```cpp
int count = 0;
while (count < 3) {
    std::cout << count << ' ';
    ++count;
}
```

**결과:** 0 1 2. `++count`가 없으면 종료 조건에 가까워지지 않습니다.

