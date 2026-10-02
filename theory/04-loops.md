## for: 횟수와 인덱스

초기식은 한 번 실행합니다. 그다음 **조건 검사, 본문, 증감식**을 반복합니다.

```cpp
for (int i = 0; i < 3; ++i) {
    std::cout << i << ' ';
}
```

**결과:** 0 1 2. i가 3이 되면 조건이 거짓이므로 종료합니다.

## while: 조건이 참인 동안

본문을 실행하기 전에 조건을 검사합니다. 처음부터 거짓이면 한 번도 실행하지 않습니다.

```cpp
int count = 0;
while (count < 3) {
    std::cout << count << ' ';
    ++count;
}
```

**결과:** 0 1 2. `++count`가 없으면 종료 조건에 가까워지지 않습니다.

## do-while: 최소 한 번

본문을 먼저 실행하고 조건을 검사합니다. 끝의 세미콜론이 필요합니다.

```cpp
int menu = 0;
do {
    std::cout << "Menu\n";
} while (menu != 0);
```

**결과:** Menu 한 번 출력. while과 조건 검사 시점이 다릅니다.

## break·continue·중첩 반복

| 구분 | 동작 | 주의 |
| --- | --- | --- |
| break | 가장 가까운 반복문 또는 switch 종료 | 바깥 반복까지 모두 종료하지 않음 |
| continue | 현재 회차의 남은 본문 생략 | for는 증감식, while은 조건 검사로 이동 |
| 중첩 반복 | 반복문 안에 다른 반복문 | 행·열을 각각 처리할 때 사용 |

```cpp
for (int i = 0; i < 5; ++i) {
    if (i == 1) continue;
    if (i == 4) break;
    std::cout << i << ' ';
}
```

**결과:** 0 2 3. while에서 continue 앞에 값 갱신을 빠뜨리면 무한 반복이 될 수 있습니다.
