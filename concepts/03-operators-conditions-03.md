# switch: 값에 따른 분기

정수·열거형의 정해진 값에 따라 실행할 case를 고릅니다. 해당 case가 없으면 default를 실행합니다.

## 개념과 동작 원리

정수·열거형 값에 대응하는 case에서 실행을 시작합니다. break나 다른 흐름 변경이 없으면 다음 case의 문장까지 이어서 실행됩니다.

## 사용 시점과 다른 개념의 구분

메뉴 번호·상태 enum처럼 특정 값들의 선택에 사용합니다. 범위 검사나 복합 논리 조건은 if로 표현하는 편이 자연스럽습니다.

## 문법과 예제

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

## 예제를 이해하는 순서

menu 2가 case 2에 대응해 Settings를 출력합니다. break는 switch를 빠져나오며, 일치 항목이 없으면 default가 처리합니다.

## 이해 확인

**질문:** case마다 새 스코프가 생기는가?

**답:** 아닙니다. 해당 case만의 지역 변수를 선언하려면 중괄호로 블록을 만드는 방식이 명확합니다.
