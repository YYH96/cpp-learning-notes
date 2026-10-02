# 자료형 선택

정수·실수·문자·참/거짓 중 저장할 값에 맞는 타입을 선택합니다. C++ 타입 이름은 `int`, `float`처럼 **소문자**로 씁니다.

## 개념과 동작 원리

타입은 값의 표현 범위·메모리 크기·허용 연산을 정합니다. 같은 100이라도 int 객체와 double 객체는 저장 방식과 계산 규칙이 다릅니다.

## 사용 시점과 다른 개념의 구분

최댓값뿐 아니라 음수 필요 여부와 소수 정밀도를 먼저 판단합니다. 정확한 개수를 세는 정수와 근삿값을 표현하는 실수를 구분합니다.

> 아래 크기와 범위는 수업 환경인 Windows / MSVC C++17 기준입니다. 1바이트는 8비트입니다. 다른 컴파일러·플랫폼에서는 크기가 달라질 수 있습니다.

## 정수형: 크기·범위·선언 예시

`signed`는 음수와 양수, `unsigned`는 0 이상의 정수를 표현합니다. `int`는 `signed int`와 같습니다.

| 자료형 | 크기 | 저장 가능한 범위 | 선언 예시 |
| --- | --- | --- | --- |
| `signed char` | 1바이트 / 8비트 | -128 ~ 127 | `signed char delta = -10;` |
| `unsigned char` | 1바이트 / 8비트 | 0 ~ 255 | `unsigned char color = 255;` |
| `short` | 2바이트 / 16비트 | -32,768 ~ 32,767 | `short level = 30;` |
| `unsigned short` | 2바이트 / 16비트 | 0 ~ 65,535 | `unsigned short count = 50000;` |
| `int` | 4바이트 / 32비트 | -2,147,483,648 ~ 2,147,483,647 | `int hp = 100;` |
| `unsigned int` | 4바이트 / 32비트 | 0 ~ 4,294,967,295 | `unsigned int score = 3000000000u;` |
| `long` | 4바이트 / 32비트 | -2,147,483,648 ~ 2,147,483,647 | `long distance = 100000L;` |
| `unsigned long` | 4바이트 / 32비트 | 0 ~ 4,294,967,295 | `unsigned long flags = 1UL;` |
| `long long` | 8바이트 / 64비트 | -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807 | `long long gold = 5000000000LL;` |
| `unsigned long long` | 8바이트 / 64비트 | 0 ~ 18,446,744,073,709,551,615 | `unsigned long long total = 10000000000ULL;` |

**int 예시:** `int hp = 100;`은 100을 담는 4바이트 정수 객체를 만듭니다. 100이라는 값 때문에 크기가 줄어들지는 않습니다. `int scores[3]`의 원소 저장 공간은 이 환경에서 4 × 3 = 12바이트입니다.

**선택 기준:** 일반 정수 계산은 `int`, 큰 누적 값은 `long long`, 비트 플래그는 `unsigned` 계열을 주로 사용합니다. Windows에서는 64비트 프로그램이어도 `long`은 4바이트입니다.

**주의:** signed 범위를 넘는 계산은 정의되지 않은 동작입니다. unsigned도 무조건 안전한 것은 아닙니다. 0에서 1을 빼면 해당 타입의 최댓값으로 순환할 수 있고, signed와 unsigned를 섞은 비교는 예상과 달라질 수 있습니다.

## 실수형: float·double·long double

소수 부분을 표현하지만 대부분의 소수는 근삿값으로 저장됩니다. 정밀도는 소수점 뒤 자릿수가 아닌 **전체 유효 숫자**의 대략적인 개수입니다.

| 자료형 | 크기 | 대략적인 최대 절댓값 | 유효 숫자 | 선언 예시 |
| --- | --- | --- | --- | --- |
| `float` | 4바이트 / 32비트 | 3.4 × 10^38 | 약 6~7자리 | `float speed = 2.5f;` |
| `double` | 8바이트 / 64비트 | 1.7 × 10^308 | 약 15~16자리 | `double average = 85.5;` |
| `long double` | 8바이트 / 64비트 | 1.7 × 10^308 | 약 15~16자리 | `long double value = 1.25L;` |

**float와 double:** `2.5f`의 `f`는 float 리터럴, `2.5`는 double 리터럴입니다. 좌표·속도 등에는 float, 일반 실수 계산과 더 높은 정밀도가 필요할 때는 double을 고려합니다.

**범위 설명:** 위 표는 가장 큰 유한값의 크기입니다. 0과 음수도 표현합니다. 가장 작은 양의 정규화 값은 float 약 1.18 × 10^-38, double 약 2.23 × 10^-308이며, 이보다 작은 비정규화 값도 있습니다.

**주의:** MSVC에서 long double은 double과 저장 크기·정밀도가 같습니다. 다른 환경에서는 다를 수 있습니다. 실수를 저장한다고 모든 소수가 정확히 보존되지는 않습니다.

## 문자·논리·문자열

| 자료형 | 크기 | 의미 | 선언 예시 |
| --- | --- | --- | --- |
| `char` | 1바이트 | 좁은 문자 코드 단위 하나 | `char grade = 'A';` |
| `wchar_t` | 2바이트, MSVC 기준 | 넓은 문자 코드 단위 | `wchar_t letter = L'가';` |
| `char16_t` | 2바이트, MSVC 기준 | UTF-16 코드 단위 | `char16_t letter = u'가';` |
| `char32_t` | 4바이트, MSVC 기준 | UTF-32 코드 단위 | `char32_t letter = U'가';` |
| `bool` | 1바이트 | `true` 또는 `false` | `bool alive = true;` |
| `std::string` | 객체 크기는 구현에 따라 다름 | 가변 길이 문자열, `<string>` 필요 | `std::string name = "Hero";` |

**char 주의:** plain char가 signed인지 unsigned인지는 구현·설정에 따라 다릅니다. 숫자 범위가 중요하면 signed char / unsigned char를 명시합니다. UTF-8 한글 한 글자는 여러 char 코드 단위로 표현되므로 char 하나에 넣을 수 없습니다.

**string 주의:** `name.size()`는 저장된 char 원소 수입니다. `sizeof(name)`은 문자열 내용 길이나 총 동적 메모리 사용량이 아니라 string 객체 자체의 크기입니다.

## 선언 예시 실행

```cpp
int hp = 100;
long long gold = 5000000000LL;
float speed = 2.5f;
double average = 85.5;
char grade = 'A';
bool alive = true;
std::cout << hp << ' ' << gold << ' ' << speed << ' '
          << average << ' ' << grade << ' ' << alive;
```

**결과:** 100 5000000000 2.5 85.5 A 1. bool은 기본 출력에서 true가 1, false가 0입니다.

## 내 환경의 바이트 수와 범위 확인

`sizeof`는 바이트 수를 반환합니다. `<limits>`의 `std::numeric_limits`로 실제 타입의 최솟값·최댓값을 확인합니다.

```cpp
std::cout << sizeof(int) << ' ' << sizeof(long long) << ' '
          << sizeof(float) << ' ' << sizeof(double) << '\n';
std::cout << std::numeric_limits<int>::lowest() << ' '
          << std::numeric_limits<int>::max();
```

**결과, MSVC:** 첫 줄 4 8 4 8, 둘째 줄 -2147483648 2147483647.

**기억할 점:** 실수의 `min()`은 가장 작은 양의 정규화 값입니다. 가장 낮은 유한값은 `lowest()`로 확인합니다. 정확히 32·64비트 정수가 필요한 형식에는 `<cstdint>`의 `std::int32_t`, `std::int64_t` 등 제공되는 고정 폭 타입을 고려합니다.

[크기·범위 참고: Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/data-type-ranges?view=msvc-170) · [표준 규칙과 환경 차이](https://learn.microsoft.com/en-us/cpp/cpp/fundamental-types-cpp?view=msvc-170)

## 예제를 이해하는 순서

hp가 100에서 80으로 바뀌어도 int 객체의 크기는 바뀌지 않습니다. float의 크기와 정밀도는 별개이므로 유효 숫자를 함께 봅니다.

## 이해 확인

**질문:** 큰 수면 무조건 double인가?

**답:** 정확한 정수 누적에는 적절한 정수형이 필요합니다. double은 충분히 큰 정수를 모두 정확하게 표현하지 못합니다.
