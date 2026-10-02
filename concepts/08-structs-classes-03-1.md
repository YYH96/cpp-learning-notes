# struct와 class

둘 다 멤버 변수와 함수를 가질 수 있습니다. 기본 멤버·상속 접근 권한은 struct가 public, class가 private입니다.

## 개념과 동작 원리

두 문법 모두 사용자 정의 타입을 만들며 멤버·생성자·상속을 지원합니다. 차이는 기본 멤버 접근과 기본 상속 접근이 struct는 public, class는 private이라는 점입니다.

## 사용 시점과 다른 개념의 구분

단순 데이터 묶음에는 struct, 내부 규칙을 감추는 타입에는 class를 흔히 씁니다. 이는 사용 관례이지 기능의 제한이 아닙니다.

## 문법과 예제

```cpp
struct Position { int x; int y; }; // main 밖
```

**예:** Position p{1, 2};에서 p.x는 1. 단순 데이터 묶음은 struct, 상태의 규칙을 감추는 설계는 class를 자주 사용합니다.

## 예제를 이해하는 순서

Position의 x와 y는 별도 public 지정 없이 외부에서 읽을 수 있습니다. class로 바꾸면 기본 private라 같은 접근이 막힙니다.

## 이해 확인

**질문:** struct에는 함수를 넣을 수 없는가?

**답:** 넣을 수 있습니다. C++의 struct는 단순 변수 묶음에만 제한되지 않습니다.
