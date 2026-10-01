[← 전체 목차](../README.md) · [이전 챕터](03-operators-conditions.md) · [다음 챕터 →](05-functions-scope.md)

# 04. 반복문과 반복 제어

> **학습 목표** · 반복 횟수·종료 조건을 설계하고 break·continue를 사용한다.

## 이 페이지에서 다룰 내용

- [홀수 출력과 별 찍기](#홀수-출력과-별-찍기)

---

for는 초기식 → 조건식 → 본문 → 증감식 → 조건식 순서입니다. while은 먼저 조건을 검사하고, do/while은 본문을 최소 한 번 실행합니다.
break는 반복을 끝내고 continue는 남은 본문을 건너뜁니다. for에서 continue 뒤에는 증감식이 실행되지만, while 본문 뒤에 적은 증가는 건너뛰어질 수 있으므로 무한 반복에 주의합니다.
중첩 반복문에서는 바깥 반복으로 행을, 안쪽 반복으로 열을 다룰 수 있습니다.
## 홀수 출력과 별 찍기

```cpp
#include <iostream>
int main() {
    for (int i = 1; i <= 7; ++i) {
        if (i % 2 == 0) continue;
        std::cout << i << ' ';
    }
    std::cout << '\n';
    constexpr int height = 3;
    for (int row = 0; row < height; ++row) {
        for (int space = 0; space < height - row - 1; ++space)
            std::cout << ' ';
        for (int star = 0; star < 2 * row + 1; ++star)
            std::cout << '*';
        std::cout << '\n';
    }
    int count = 0;
    while (count < 3) { std::cout << count++ << ' '; }
    std::cout << '\n';
    int menu = 0;
    do { std::cout << "Menu shown once\n"; } while (menu != 0);
}
```

📎 [실행할 예제 파일](../examples/07_loops.cpp)

**별 찍기 규칙:** 피라미드의 공백은 높이−행−1, 별은 2×행+1입니다. 수업 원문에는 사각형·역삼각형·평행사변형 모양·다이아몬드·복합 삼각형 예제도 모두 포함돼 있습니다.

---

[← 전체 목차](../README.md) · [이전 챕터](03-operators-conditions.md) · [다음 챕터 →](05-functions-scope.md)
