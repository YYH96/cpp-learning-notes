# const_cast

포인터·참조의 const 등 한정자를 조정합니다. 원래부터 const인 객체를 수정하는 용도로 사용할 수 없습니다.

## 개념과 동작 원리

const 등 한정자를 조정하는 캐스트이며 실제 객체의 성질을 바꾸지는 않습니다. 원래 const인 객체를 쓰기 대상으로 만드는 근거가 되지 않습니다.

## 사용 시점과 다른 개념의 구분

기존 API의 const 인터페이스 불일치를 처리해야 할 때 매우 제한적으로 사용합니다. 평소에는 함수 계약의 const 정확성을 먼저 수정합니다.

## 문법과 예제

```cpp
int value = 10;
const int* view = &value;
int* writable = const_cast<int*>(view);
*writable = 20;
std::cout << value;
```

**결과:** 20. 원본 value는 const가 아니므로 가능합니다. 원본이 const int였다면 이런 수정은 정의되지 않은 동작입니다.

## 예제를 이해하는 순서

value가 비const이고 view만 const 포인터이므로 한정자 제거 후 value를 수정할 수 있습니다. 원본이 const였다면 같은 수정은 허용되지 않습니다.

## 이해 확인

**질문:** const_cast 결과 포인터로 읽는 것과 쓰는 것은 같은가?

**답:** 원본 객체의 타입·수명과 접근 규칙을 봐야 합니다. 캐스트 성공만으로 수정이 안전해지지 않습니다.
