# do-while: 최소 한 번

본문을 먼저 실행하고 조건을 검사합니다. 끝의 세미콜론이 필요합니다.

```cpp
int menu = 0;
do {
    std::cout << "Menu\n";
} while (menu != 0);
```

**결과:** Menu 한 번 출력. while과 조건 검사 시점이 다릅니다.

