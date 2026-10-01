[← 전체 목차](../README.md) · [이전 챕터](02-io-types.md) · [다음 챕터 →](04-loops.md)

# 03. 연산자와 조건문

> **학습 목표** · 연산 결과와 조건 분기를 이해하고 비트 플래그를 구성한다.

## 이 페이지에서 다룰 내용

- [계산·비교·판단](#계산비교판단)
- [체력과 등급 판단](#체력과-등급-판단)
- [switch](#switch)
- [비트 연산과 상태 플래그](#비트-연산과-상태-플래그)

---

## 계산·비교·판단
산술 연산자 +, -, *, /, %와 복합 대입 +=, -=, *=, /=, %=를 배웠습니다. %는 정수 나머지입니다. 정수 나눗셈과 나머지의 분모는 0이면 안 됩니다.
비교 연산자 ==, !=, <, >, <=, >=의 결과는 bool입니다. =는 대입이고 ==는 비교입니다. &&는 둘 다 참, ||는 하나 이상 참, !는 참·거짓 반전입니다. &&와 ||는 왼쪽 결과로 결론이 나면 오른쪽을 평가하지 않는 단락 평가를 합니다.
전위 ++n은 증가한 값을 사용하고, 후위 n++는 증가 전 값을 식의 결과로 사용합니다. 조건 연산자 조건 ? 참일 때 값 : 거짓일 때 값도 배웠습니다.
## 체력과 등급 판단

```cpp
#include <iostream>
int main() {
    int hp = 100;
    hp -= 30;
    bool isHero = true;
    if (isHero && hp > 0) {
        std::cout << "Hero alive\n";
    }
    int score = 88;
    if (score >= 90) std::cout << "A\n";
    else if (score >= 80) std::cout << "B\n";
    else std::cout << "C\n";
    char turn = 'X';
    turn = turn == 'X' ? 'O' : 'X';
    int n = 5;
    int before = n++;  // before=5, n=6
    int after = ++n;   // after=7, n=7
    std::cout << turn << ' ' << before << ' ' << after << '\n';
}
```

📎 [실행할 예제 파일](../examples/04_conditions.cpp)

**결과:** Hero alive, B, O 5 7. if/else if 묶음에서는 처음 참인 분기 하나를 실행합니다. 독립된 if를 여러 개 쓰면 여러 분기가 실행될 수 있습니다.
## switch
정수·열거형처럼 정해진 값에 따른 분기에 사용합니다. case 뒤에 break가 없으면 다음 case의 코드까지 이어서 실행될 수 있습니다. break는 가장 가까운 반복문 또는 switch를 끝내며, 임의의 중괄호를 종료하는 명령은 아닙니다.

```cpp
#include <iostream>
int main() {
    int menu = 2;
    switch (menu) {
    case 0: std::cout << "Exit\n"; break;
    case 1: std::cout << "Americano\n"; break;
    case 2: std::cout << "Latte\n"; break;
    default: std::cout << "Invalid menu\n"; break;
    }
}
```

📎 [실행할 예제 파일](../examples/05_switch.cpp)

## 비트 연산과 상태 플래그
&는 비트 AND, |는 OR, ^는 XOR, ~는 반전, <<와 >>는 비트 이동입니다. 논리 연산자 &&·||와 구분합니다. 독립 상태를 플래그로 조합할 때 각각 1, 2, 4처럼 겹치지 않는 비트를 사용합니다. 0은 아무 상태도 없음에 적합합니다.

```cpp
#include <iostream>
int main() {
    constexpr unsigned fury = 1u << 0;
    constexpr unsigned shield = 1u << 1;
    unsigned buffs = 0;
    buffs |= fury;                    // 켜기
    buffs |= shield;
    std::cout << ((buffs & fury) != 0) << '\n';
    buffs &= ~fury;                    // 끄기
    buffs ^= shield;                   // 토글
    std::cout << buffs << '\n';
}
```

📎 [실행할 예제 파일](../examples/06_flags.cpp)

---

[← 전체 목차](../README.md) · [이전 챕터](02-io-types.md) · [다음 챕터 →](04-loops.md)
