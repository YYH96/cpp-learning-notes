## 연산자: 계산·비교·논리

| 종류 | 역할 | 예 |
| --- | --- | --- |
| 산술 | 값을 계산 | +, -, *, /, % |
| 비교 | 참·거짓 판단 | ==, !=, <, >= |
| 논리 | 조건을 조합 | &&, 논리 OR, ! |
| 대입 | 값을 저장·갱신 | =, +=, -= |

```cpp
int hp = 100;
hp -= 20;
bool alive = hp > 0;
bool canAttack = alive && hp >= 10;
```

**결과:** hp는 80, alive와 canAttack은 true. =는 대입, ==는 같은지 비교합니다.

**주의:** &&와 ||는 왼쪽 결과만으로 결론이 나면 오른쪽을 평가하지 않습니다. 정수 /와 %의 분모는 0이면 안 됩니다.

## if, else if, else

조건을 위에서부터 검사하고, **처음 참인 분기 하나만 실행**합니다. C++에서는 `elseif`가 아니라 **`else if`**로 씁니다.

- **if (조건):** 첫 조건이 참일 때 실행합니다. 거짓이면 해당 블록을 건너뜁니다.
- **else if (조건):** 앞의 조건들이 모두 거짓일 때 다음 조건을 검사합니다. 여러 번 이어 쓸 수 있습니다.
- **else:** 앞의 조건들이 모두 거짓일 때 실행합니다. 조건을 붙이지 않으며 생략할 수 있습니다.

### if: 조건이 맞을 때만

```cpp
int hp = 0;
if (hp <= 0) {
    std::cout << "Game Over\n";
}
```

**결과:** hp가 0이므로 Game Over. hp가 10이면 이 블록은 실행하지 않습니다.

### if / else: 둘 중 하나

```cpp
int hp = 10;
if (hp > 0) {
    std::cout << "Alive\n";
} else {
    std::cout << "Dead\n";
}
```

**결과:** Alive. 같은 if / else 묶음에서 두 블록이 함께 실행되지는 않습니다.

### if / else if / else: 여러 경우 중 하나

```cpp
int score = 88;
if (score >= 90) {
    std::cout << "A\n";
} else if (score >= 80) {
    std::cout << "B\n";
} else {
    std::cout << "C\n";
}
```

**검사 순서:** 90 이상은 거짓, 80 이상은 참. B를 출력하고 나머지 분기는 건너뜁니다. 두 조건이 모두 거짓이면 C입니다.

### 독립된 if와 연결된 else if의 차이

- **if를 각각 쓰면:** 모든 조건을 따로 검사합니다. 여러 블록이 실행될 수 있습니다.
- **else if로 연결하면:** 처음 참인 블록 하나만 실행합니다. 이후 조건은 검사하지 않습니다.
- **조건 순서:** score >= 80을 먼저 쓰면 95점도 그 분기에 들어갑니다. 등급처럼 범위가 겹치면 더 높은 기준을 먼저 검사합니다.

**작성 주의:** if (조건) 뒤에 불필요한 세미콜론을 붙이지 않습니다. 중괄호를 쓰면 실행할 범위와 else의 연결이 명확해집니다.

## switch: 값에 따른 분기

정수·열거형의 정해진 값에 따라 실행할 case를 고릅니다. 해당 case가 없으면 default를 실행합니다.

```cpp
int menu = 2;
switch (menu) {
case 1: std::cout << "Start\n"; break;
case 2: std::cout << "Settings\n"; break;
default: std::cout << "Invalid\n"; break;
}
```

**결과:** Settings. 범위·복합 조건은 if가 적합하고, 특정 값별 선택은 switch로 읽기 쉽게 표현할 수 있습니다.

**주의:** break가 없으면 다음 case의 코드까지 이어 실행될 수 있습니다. std::string을 switch의 조건으로 직접 쓸 수는 없습니다.

## 비트 플래그: 여러 상태 조합

논리 연산은 참·거짓을 다루고, 비트 연산은 정수의 각 비트를 다룹니다. 상태를 1, 2, 4처럼 겹치지 않는 비트에 배정합니다.

```cpp
constexpr unsigned Shield = 1u << 0;
constexpr unsigned Fury = 1u << 1;
unsigned buffs = Shield | Fury;
bool hasShield = (buffs & Shield) != 0;
buffs &= ~Shield;
```

**결과:** hasShield는 true, 마지막 buffs는 Fury만 남은 2. 비트 OR는 켜기, AND는 확인·마스킹, XOR는 토글에 사용합니다.
