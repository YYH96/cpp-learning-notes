# switch: 값에 따른 분기

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

