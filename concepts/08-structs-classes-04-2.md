# enum class

열거자 이름의 범위를 타입 안으로 제한하며 정수로 자동 변환하지 않습니다.

## 개념과 동작 원리

범위 있는 열거형으로 열거자 이름을 타입 안에 묶고 정수로의 암시적 변환을 막습니다. 서로 다른 열거형을 실수로 섞는 문제를 줄입니다.

## 사용 시점과 다른 개념의 구분

방향·씬 상태·전투 상태를 명확한 타입으로 구분할 때 사용합니다. 정수 표현이 필요하면 변환 의도를 명시합니다.

## 문법과 예제

```cpp
enum class Direction { Left, Right }; // main 밖
```

```cpp
Direction d = Direction::Right;
int value = static_cast<int>(d);
std::cout << value;
```

**결과:** 1. Direction::Right처럼 타입 이름을 붙입니다.

## 예제를 이해하는 순서

Direction::Right로 소속을 지정합니다. static_cast<int>는 그 값을 정수로 명시 변환하지만 d 자체는 여전히 Direction 타입입니다.

## 이해 확인

**질문:** enum class끼리 이름이 같아도 되는가?

**답:** 각 타입의 범위가 다르므로 같은 열거자 이름을 독립적으로 사용할 수 있습니다.
