# 개념별 목차

연산자와 조건문을 구분하고, 한 페이지에서 하나의 학습 개념을 읽습니다.

## 기초 문법

- [프로그램의 기본 구조](01-program-basics-01.md)
- [선언과 정의](01-program-basics-02.md)
- [컴파일·링크·디버깅](01-program-basics-03.md)
- [자료형 선택](02-io-types-01.md)
- [변수와 초기화](02-io-types-02-1.md)
- [const와 constexpr](02-io-types-02-2.md)
- [cout 출력](02-io-types-03-1.md)
- [cin 입력](02-io-types-03-2.md)
- [getline 줄 입력](02-io-types-03-3.md)
- [정수 나눗셈과 형변환](02-io-types-04.md)

## 연산자

- [산술 연산자](operators-01-arithmetic.md)
- [대입·복합 대입 연산자](operators-02-assignment.md)
- [증가·감소 연산자](operators-03-increment.md)
- [비교 연산자](operators-04-comparison.md)
- [논리 연산자와 단락 평가](operators-05-logical.md)
- [비트 연산자와 플래그](operators-06-bitwise.md)
- [삼항 조건 연산자](operators-07-conditional.md)
- [주소·역참조 연산자](operators-08-address.md)
- [멤버·인덱스·호출·범위 연산자](operators-09-access.md)
- [크기·형변환·메모리 관련 연산](operators-10-size-cast-memory.md)
- [연산자 우선순위와 괄호](operators-11-precedence.md)
- [입출력 연산과 쉼표](operators-12-stream-comma.md)

## 조건문

- [if, else if, else](03-operators-conditions-02.md)
- [switch: 값에 따른 분기](03-operators-conditions-03.md)

## 반복문

- [for: 횟수와 인덱스](04-loops-01.md)
- [while: 조건이 참인 동안](04-loops-02.md)
- [do-while: 최소 한 번](04-loops-03.md)
- [break](04-loops-04-1.md)
- [continue](04-loops-04-2.md)
- [중첩 반복문](04-loops-04-3.md)

## 함수와 범위

- [함수의 기본 문법과 호출](05-functions-scope-01.md)
- [함수 오버로딩](05-functions-scope-02-1.md)
- [기본 인자](05-functions-scope-02-2.md)
- [재귀: 자기 자신 호출](05-functions-scope-03.md)
- [스코프](05-functions-scope-04-1.md)
- [namespace](05-functions-scope-04-2.md)

## 배열·포인터·참조

- [배열과 인덱스](06-arrays-pointers-references-01.md)
- [포인터: 주소와 역참조](06-arrays-pointers-references-02.md)
- [참조](06-arrays-pointers-references-03-1.md)
- [값·포인터·참조 전달](06-arrays-pointers-references-03-2.md)
- [const 포인터](06-arrays-pointers-references-04.md)
- [2차원 배열과 좌표](06-arrays-pointers-references-05.md)

## 문자열

- [C 문자열](07-strings-search-01-1.md)
- [std::string](07-strings-search-01-2.md)
- [strlen과 sizeof](07-strings-search-02.md)
- [수정·부분 문자열·검색](07-strings-search-03.md)
- [cin 다음의 getline](07-strings-search-04.md)

## 구조체와 클래스

- [클래스와 객체의 기본](08-structs-classes-01.md)
- [this 포인터](08-structs-classes-02-1.md)
- [접근 지정자](08-structs-classes-02-2.md)
- [struct와 class](08-structs-classes-03-1.md)
- [캡슐화와 정보 은닉](08-structs-classes-03-2.md)
- [추상화](08-structs-classes-03-3.md)
- [enum](08-structs-classes-04-1.md)
- [enum class](08-structs-classes-04-2.md)

## 객체 수명과 메모리

- [객체 수명](09-lifetime-memory-01-1.md)
- [생성자와 초기화 목록](09-lifetime-memory-01-2.md)
- [소멸자](09-lifetime-memory-01-3.md)
- [static 지역 변수](09-lifetime-memory-02-1.md)
- [static 멤버](09-lifetime-memory-02-2.md)
- [동적 할당과 소유권](09-lifetime-memory-03.md)
- [복사 생성자](09-lifetime-memory-04-1.md)
- [복사 대입](09-lifetime-memory-04-2.md)
- [이동과 std::move](09-lifetime-memory-04-3.md)

## 상속과 형변환

- [상속: 공통 역할 확장](10-inheritance-polymorphism-01.md)
- [가상 함수와 override](10-inheritance-polymorphism-02-1.md)
- [다형성](10-inheritance-polymorphism-02-2.md)
- [추상 클래스와 순수 가상 함수](10-inheritance-polymorphism-02-3.md)
- [static_cast](10-inheritance-polymorphism-03-1.md)
- [dynamic_cast](10-inheritance-polymorphism-03-2.md)
- [const_cast](10-inheritance-polymorphism-03-3.md)
- [reinterpret_cast](10-inheritance-polymorphism-03-4.md)

## 컨테이너와 자료구조

- [vector: 인덱스로 접근](11-containers-iterators-01.md)
- [vector의 size와 capacity](11-containers-iterators-02-1.md)
- [reserve](11-containers-iterators-02-2.md)
- [resize](11-containers-iterators-02-3.md)
- [list: 노드를 연결](11-containers-iterators-03.md)
- [iterator와 삭제 후 순회](11-containers-iterators-04.md)
- [직접 구현한 자료구조](11-containers-iterators-05.md)

## 템플릿과 타입 추론

- [template: 타입을 매개변수로](12-templates-operators-01.md)
- [auto: 초기값에서 타입 추론](12-templates-operators-02.md)
- [연산자 오버로딩](12-templates-operators-03.md)

## 게임 설계

- [게임 루프: 입력·갱신·출력](13-game-design-01.md)
- [역할 분리](13-game-design-02.md)
- [씬 전환과 다형성](13-game-design-03.md)
- [싱글톤](13-game-design-04-1.md)
- [헤더·소스 파일과 전방 선언](13-game-design-04-2.md)

