[← 전체 목차](../README.md) · [이전 챕터](01-program-basics.md) · [다음 챕터 →](03-operators-conditions.md)

# 02. 입출력, 자료형, 변수와 상수

> **학습 목표** · 입력·출력과 자료형을 선택하고 초기화·형변환을 적용한다.

## 이 페이지에서 다룰 내용

- [입력과 출력](#입력과-출력)
- [자료형을 선택하는 기준](#자료형을-선택하는-기준)
- [변수·형변환·평균 예제](#변수형변환평균-예제)
- [상수](#상수)

---

## 입력과 출력
cout의 출력 연산자는 `<<`, cin의 입력 연산자는 `>>`입니다. `\n`은 줄바꿈, `\t`는 탭입니다. std::endl은 줄바꿈과 버퍼 비우기를 함께 수행합니다. cin으로 문자열을 읽으면 공백 전까지 읽고, getline은 한 줄을 읽습니다.
C 방식의 printf·scanf도 배웠습니다. printf의 %d는 int, %c는 문자, %s는 C 문자열, %f는 실수 출력입니다. scanf에서는 float*에 %f, double*에 %lf를 사용하며 숫자를 저장할 변수의 주소를 전달합니다.
## 자료형을 선택하는 기준
정수에는 int·short·long·long long, 실수에는 float·double, 문자에는 char, 참·거짓에는 bool을 사용합니다. unsigned는 해당 정수형에서 음수를 표현하지 않게 합니다. sizeof는 저장 크기를 바이트 단위로 확인합니다.
수업의 Windows/MSVC 환경에서는 int와 long은 보통 4바이트, long long은 8바이트입니다. long이 언제나 int보다 큰 것은 아닙니다. float·double의 정밀도는 소수점 뒤 고정 자릿수가 아니라 유효 숫자 정밀도입니다. 포인터 크기는 빌드 대상에 따라 보통 x86 4바이트, x64 8바이트입니다.
변수는 이름을 가진 저장 공간입니다. 선언할 때 초기값을 주면 미정 값 사용을 피할 수 있습니다. 한 선언에 여러 변수를 적더라도 초기화는 각각 해야 합니다.
## 변수·형변환·평균 예제

```cpp
#include <iostream>
int main() {
    int kor = 80, eng = 90, math = 85;
    int sum = kor + eng + math;
    double average = static_cast<double>(sum) / 3;
    char grade = 'A';
    bool passed = average >= 60;
    std::cout << sum << ' ' << average << ' ' << grade << ' ' << passed << '\n';
    std::cout << "int bytes: " << sizeof(int) << '\n';
}
```

📎 [실행할 예제 파일](../examples/02_scores.cpp)

**결과:** 합계 255, 평균 85, 학점 A, passed는 1입니다. 정수끼리의 나눗셈은 소수 부분을 버리므로 나누기 전에 실수로 변환합니다.
## 상수
리터럴은 10·3.14·"Hello"처럼 코드에 직접 쓴 값입니다. const는 해당 이름을 통해 값을 바꾸지 못하게 하고, constexpr 변수는 컴파일 시간에 결정되는 값으로 초기화합니다. define 매크로는 전처리 단계에서 텍스트를 치환하므로 자료형과 범위를 가진 상수와 구분합니다.

```cpp
#include <iostream>
int main() {
    const int maxHP = 100;
    constexpr int boardWidth = 5;
    int hp = maxHP;
    hp -= 20;
    std::cout << hp << ' ' << boardWidth << '\n';
}
```

📎 [실행할 예제 파일](../examples/03_constants.cpp)

---

[← 전체 목차](../README.md) · [이전 챕터](01-program-basics.md) · [다음 챕터 →](03-operators-conditions.md)
