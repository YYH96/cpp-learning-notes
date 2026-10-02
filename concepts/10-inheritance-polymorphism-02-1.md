# 가상 함수와 override

virtual 함수는 기반 포인터·참조로 호출해도 실제 객체의 재정의를 사용합니다. override는 재정의의 타입·시그니처 오류를 검사합니다.

## 개념과 동작 원리

가상 함수 호출은 기반 포인터·참조를 통해서도 실제 객체의 타입에 맞는 최종 재정의를 선택합니다. override는 컴파일러에게 재정의 관계 검사를 요구합니다.

## 사용 시점과 다른 개념의 구분

공통 인터페이스로 여러 타입의 행동을 실행할 때 사용합니다. 같은 이름의 다른 인자 함수를 만드는 오버로딩과 구분합니다.

## 문법과 예제

```cpp
class Base { // main 밖
public:
    virtual ~Base() = default;
    virtual int Power() const { return 10; }
};
class Mage : public Base {
public:
    int Power() const override { return 30; }
};
```

**예:** Mage m; Base& b = m;에서 b.Power()는 30. 비가상 함수는 이런 방식으로 동적 연결되지 않습니다.

## 예제를 이해하는 순서

Base&가 Mage 객체에 바인딩되면 Power는 Mage의 30을 반환합니다. const 등 시그니처가 달라 재정의가 아니면 override로 오류를 발견할 수 있습니다.

## 이해 확인

**질문:** 기반 생성자에서 파생 재정의가 호출되는가?

**답:** 생성·소멸 중 가상 호출은 현재 생성·소멸 단계의 클래스 규칙을 따르므로 일반 실행과 구분해야 합니다.

## 참고 문서

[가상 함수 호출 · Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/virtual-functions?view=msvc-170)
