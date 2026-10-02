# 접근 지정자

public은 외부 인터페이스, private은 클래스 내부와 friend, protected는 파생 클래스까지의 접근을 허용합니다.

## 개념과 동작 원리

접근 지정자는 클래스의 이름에 어느 코드가 접근할 수 있는지 정하는 컴파일 시간 규칙입니다. public·private·protected가 인터페이스와 내부 구현의 경계를 만듭니다.

## 사용 시점과 다른 개념의 구분

상태를 직접 변경하는 대신 검증된 함수를 공개할 때 사용합니다. 접근 제한은 객체의 수명이나 메모리 암호화를 뜻하지 않습니다.

## 문법과 예제

```cpp
class Player { // main 밖
private:
    int hp = 100;
public:
    int GetHp() const { return hp; }
};
```

**예:** hero.GetHp()는 가능, hero.hp는 외부에서 불가. protected도 외부 코드에 공개되는 것은 아닙니다.

## 예제를 이해하는 순서

private hp에는 외부 코드가 직접 접근할 수 없지만 public GetHp는 내부에서 hp를 읽어 반환할 수 있습니다.

## 이해 확인

**질문:** protected는 외부에도 공개되는가?

**답:** 아닙니다. 파생 클래스의 접근을 허용하지만 외부 접근과 파생 대상 접근에도 정해진 규칙이 있습니다.
