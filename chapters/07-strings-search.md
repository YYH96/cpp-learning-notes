[← 전체 목차](../README.md) · [이전 챕터](06-arrays-pointers-references.md) · [다음 챕터 →](08-structs-classes.md)

# 07. 문자열과 문자열 검색

> **학습 목표** · C 문자열과 string의 차이를 설명하고 문자열 검색을 구현한다.

## 이 페이지에서 다룰 내용

- [C 문자열](#c-문자열)
- [std::string](#stdstring)
- [문자열 수정과 검색](#문자열-수정과-검색)
- [cin 다음에 getline 사용하기](#cin-다음에-getline-사용하기)
- [부분 문자열 find 직접 구현 — 복습용 완성 예제](#부분-문자열-find-직접-구현--복습용-완성-예제)

---

## C 문자열
char 배열의 끝에는 널 문자 `\0`이 필요합니다. strlen은 끝의 널 문자를 제외한 길이를 구하고, sizeof는 배열의 저장 크기를 구합니다. strcpy는 복사, strcat는 연결, strcmp는 비교, strstr는 부분 문자열 검색입니다.
strcmp의 결과는 같으면 0, 앞 문자열이 작으면 음수, 크면 양수입니다. 정확히 −1 또는 1이라고 가정하지 않습니다. strtok 계열은 구분자로 나누면서 원본 버퍼를 바꿉니다. 수업의 strcpy_s·strcat_s·strtok_s는 MSVC 환경의 인터페이스입니다.
## std::string
string은 문자 저장 공간과 길이를 관리합니다. +·+=로 연결하고, size/length로 길이, empty로 비었는지 확인합니다. insert·erase·replace·substr·find를 배웠습니다.
size/length에는 공백도 포함됩니다. std::string의 크기는 char 요소 수이므로 UTF-8 한글의 화면상 글자 수와 같지 않을 수 있습니다. replace(pos,count,text)와 substr(pos,count)의 두 번째 값은 끝 인덱스가 아니라 **개수**입니다. [Microsoft string 문서](https://learn.microsoft.com/en-us/cpp/standard-library/basic-string-class?view=msvc-170)
## 문자열 수정과 검색

```cpp
#include <iostream>
#include <string>
int main() {
    std::string name = "YoonYoungHo";
    name.insert(4, "_");
    name.erase(4, 1);
    name.replace(0, 4, "Kim");
    auto pos = name.find("Young");
    if (pos != std::string::npos) std::cout << pos << '\n'; // 3
    std::cout << name.substr(0, 3) << '\n';                 // Kim
    std::cout << std::string("A B").size() << '\n';         // 3
}
```

📎 [실행할 예제 파일](../examples/14_string.cpp)

## cin 다음에 getline 사용하기
숫자 입력 뒤에 줄바꿈이 남아 있으면 getline이 빈 줄을 읽을 수 있습니다. 남은 줄을 ignore로 버리거나 getline(cin >> std::ws, text)를 사용합니다. ws는 앞의 공백까지 제거하므로 앞 공백을 보존해야 할 때는 ignore 방식이 적합합니다.

```cpp
#include <iostream>
#include <limits>
#include <string>
int main() {
    int level = 0;
    std::string message;
    if (!(std::cin >> level)) return 1;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::getline(std::cin, message);
    std::cout << level << ": " << message << '\n';
}
```

📎 [실행할 예제 파일](../examples/15_getline.cpp)

## 부분 문자열 find 직접 구현 — 복습용 완성 예제
수업의 실습_find구현.cpp는 항상 −1을 반환하는 틀입니다. 시작 위치를 하나씩 옮기며 찾는 문자열 전체가 일치하는지 검사합니다.

```cpp
#include <iostream>
#include <string>
int MyFind(const std::string& text, const std::string& need) {
    if (need.empty()) return 0;
    if (need.size() > text.size()) return -1;
    for (std::size_t i = 0; i <= text.size() - need.size(); ++i) {
        std::size_t j = 0;
        while (j < need.size() && text[i + j] == need[j]) ++j;
        if (j == need.size()) return static_cast<int>(i);
    }
    return -1;
}
int main() {
    std::cout << MyFind("sadbutsad", "dbu") << '\n'; // 2
    std::cout << MyFind("abc", "xyz") << '\n';      // -1
}
```

📎 [실행할 예제 파일](../examples/16_find.cpp)

---

[← 전체 목차](../README.md) · [이전 챕터](06-arrays-pointers-references.md) · [다음 챕터 →](08-structs-classes.md)
