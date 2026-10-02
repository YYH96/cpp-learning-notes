## C 문자열과 std::string

| 비교 | C 문자열 | std::string |
| --- | --- | --- |
| 저장 | 널 문자로 끝나는 char 배열 | 길이와 저장 공간을 관리하는 객체 |
| 길이 | strlen | size 또는 length |
| 수정 | 버퍼 용량을 직접 확인 | 멤버 함수로 추가·삭제·수정 |

```cpp
char word[] = "Cat";
std::string name = "Kim Hero";
std::cout << sizeof(word) << ' ' << name.size();
```

**결과:** 4 8. word는 문자 3개와 끝의 `\0` 한 개를 저장합니다.

## strlen과 sizeof

| 표현 | 구하는 것 | "Cat" 배열의 결과 |
| --- | --- | --- |
| strlen(word) | 널 문자 전까지의 문자열 길이 | 3 |
| sizeof(word) | 실제 배열의 저장 바이트 수 | 4 |
| sizeof(pointer) | 포인터 자체의 바이트 수 | 빌드 환경에 따라 다름 |

**주의:** std::string은 char 요소 수를 셉니다. UTF-8 한글의 화면 글자 수와 다를 수 있습니다.

## 수정·부분 문자열·검색

```cpp
std::string text = "Hello World";
std::string part = text.substr(6, 5);
auto position = text.find("World");
```

**결과:** part는 World, position은 6. substr의 두 번째 인자는 끝 위치가 아닌 **개수**입니다.

**주의:** find가 실패하면 std::string::npos. 위치를 사용하기 전에 확인합니다. replace(pos, count, text)의 count도 개수입니다.

## cin 다음의 getline

cin으로 숫자를 읽으면 줄바꿈이 남을 수 있습니다. 한 줄의 나머지를 버리고 getline을 호출합니다.

```cpp
int age;
std::string name;
std::cin >> age;
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
std::getline(std::cin, name);
```

**전제:** 숫자 입력이 성공한 경우. `<limits>`가 필요합니다. 20을 입력하고 다음 줄에 Kim Hero를 입력하면 name은 Kim Hero입니다.
