# 크기·형변환·메모리 관련 연산

자주 마주치는 특수 연산을 구분합니다. 자세한 동작은 형변환·동적 메모리 개념 페이지에서 확인합니다.

## 개념과 동작 원리

sizeof는 타입이나 객체의 저장 크기를 구하고, 캐스트는 타입 해석·변환을 명시합니다. new와 delete는 동적 객체의 생성·소멸과 저장 공간 관리를 수행합니다.

## 사용 시점과 다른 개념의 구분

데이터 형식 확인·평균 계산·런타임 객체 생성에 사용합니다. 같은 크기의 타입이라도 표현 방식이 달라 임의로 서로 바꿔 읽을 수 없습니다.

## 문법과 예제

| 표현 | 역할 | 예 |
| --- | --- | --- |
| sizeof | 타입·객체의 크기를 바이트로 구함 | sizeof(int), sizeof(values) |
| static_cast<T> | 명시적 타입 변환 | static_cast<double>(total) |
| dynamic_cast<T> | 다형적 타입의 다운캐스트 등 확인 | 실패 시 포인터 변환은 nullptr |
| const_cast<T> | const 등 한정자 변경 | 실제 const 객체 수정은 금지 |
| reinterpret_cast<T> | 저수준 재해석 | 주소·타입 규칙을 엄격히 확인 |
| new, new[] | 동적 객체·배열 생성 | new int(10), new int[3] |
| delete, delete[] | 대응 자원 해제 | delete p, delete[] a |

```cpp
int total = 7, count = 2;
double average = static_cast<double>(total) / count;
int values[3]{1, 2, 3};
std::cout << average << ' ' << sizeof(values) / sizeof(values[0]);
```

**결과:** 3.5 3. sizeof는 원소 개수가 아니라 바이트 수입니다. 이 배열 크기 계산법은 포인터에 적용하면 안 됩니다.

**주의:** 일반적인 sizeof의 피연산자 식은 실행되지 않습니다. 동적 자원은 가능하면 vector, string, 스마트 포인터 등 자동 정리 도구에 맡깁니다.

## 예제를 이해하는 순서

sizeof(values) / sizeof(values[0])는 실제 배열의 전체 크기를 원소 크기로 나눕니다. 함수 매개변수에서 포인터가 된 값에는 같은 계산을 적용할 수 없습니다.

## 이해 확인

**질문:** sizeof로 문자열 길이를 알 수 있는가?

**답:** 배열 저장 공간과 내용 길이는 별개입니다. 끝 문자나 포인터 크기도 고려해야 합니다.
