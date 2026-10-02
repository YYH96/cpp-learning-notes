## 자료형 선택

| 저장할 값 | 자료형 | 예 |
| --- | --- | --- |
| 정수 | int | 체력 100, 학생 수 5 |
| 실수 | double | 평균 85.5 |
| 문자 하나 | char | 'A' |
| 참·거짓 | bool | true, false |
| 문자열 | std::string | "Warrior" |

**주의:** 자료형 크기는 환경에 따라 달라질 수 있습니다. 실제 바이트 수는 `sizeof`로 확인합니다.

## 변수·초기화·상수

```cpp
int hp = 100;           // 초기값 지정
hp -= 20;              // 변경 가능
const int MaxHp = 100;  // 초기화 후 변경 금지
constexpr int Size = 3; // 컴파일 시간 상수
```

**결과:** hp는 80. 초기값 없는 일반 지역 변수는 읽기 전에 값을 넣어야 합니다.

## cin·cout·getline

| 기능 | 사용 | 읽는 범위 |
| --- | --- | --- |
| 출력 | std::cout << 값; | 값을 화면에 표시 |
| 입력 | std::cin >> 변수; | 문자열은 공백 앞까지 |
| 한 줄 입력 | std::getline(std::cin, text); | 공백을 포함한 한 줄 |

```cpp
std::string name;
std::getline(std::cin, name);
std::cout << name << '\n';
```

**결과:** Kim Hero를 입력하면 공백까지 포함해 출력합니다. 숫자 입력 다음의 getline 처리법은 문자열 챕터에서 확인합니다.

## 정수 나눗셈과 형변환

```cpp
int total = 5;
double wrong = total / 2;
double correct = static_cast<double>(total) / 2;
```

**결과:** wrong은 2.0, correct는 2.5. 계산이 끝난 뒤 double에 저장해도 이미 버린 소수 부분은 복구되지 않습니다.
