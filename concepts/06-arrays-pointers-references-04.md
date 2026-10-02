# const 포인터

## 개념과 동작 원리

const의 위치에 따라 가리키는 대상의 수정 제한과 포인터 주소 변경 제한이 다릅니다. 대상이 const인 것과 포인터 객체가 const인 것을 구분합니다.

## 사용 시점과 다른 개념의 구분

읽기 전용 데이터 접근에는 const int*, 연결할 주소를 고정하려면 int* const를 사용합니다. 둘 다 필요하면 const int* const입니다.

## 문법과 예제

| 선언 | 이 포인터로 값 수정 | 주소 변경 |
| --- | --- | --- |
| const int* p | 불가 | 가능 |
| int* const p | 가능 | 불가 |
| const int* const p | 불가 | 불가 |

## 예제를 이해하는 순서

const int* p는 p의 재대입은 가능하지만 *p에 대입할 수 없습니다. int* const p는 그 반대로 주소 고정과 대상 수정을 뜻합니다.

## 두 const를 코드로 구분하기

```cpp
int a = 10, b = 20;
const int* readOnly = &a;
readOnly = &b;               // 주소 변경 가능
int* const fixed = &a;
*fixed = 30;                 // 대상 값 변경 가능
std::cout << *readOnly << ' ' << *fixed << ' ' << a;
```

**결과:** 20 30 30. readOnly는 읽기 전용 접근, fixed는 주소 고정입니다. readOnly로 b를 수정하거나 fixed를 다른 주소에 재대입하는 것은 컴파일 오류입니다.

## 이해 확인

**질문:** const int*이면 원본은 절대 바뀌지 않는가?

**답:** 이 포인터를 통한 변경이 금지된 것입니다. 원본이 비const라면 다른 경로로 변경할 수 있습니다.
