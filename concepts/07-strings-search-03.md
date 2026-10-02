# 수정·부분 문자열·검색

## 개념과 동작 원리

문자열 함수는 위치와 개수를 이용해 구간을 지정합니다. 검색 결과는 위치값이며 못 찾았다는 상태를 특별한 값 npos로 구분합니다.

## 사용 시점과 다른 개념의 구분

이름 일부 추출·명령 검색·텍스트 치환에 사용합니다. 시작 위치와 끝 위치가 아니라 시작 위치와 개수로 인자를 받는 함수가 많습니다.

## 문법과 예제

```cpp
std::string text = "Hello World";
std::string part = text.substr(6, 5);
auto position = text.find("World");
```

**결과:** part는 World, position은 6. substr의 두 번째 인자는 끝 위치가 아닌 **개수**입니다.

**주의:** find가 실패하면 std::string::npos. 위치를 사용하기 전에 확인합니다. replace(pos, count, text)의 count도 개수입니다.

## 예제를 이해하는 순서

Hello World에서 World는 인덱스 6에서 시작합니다. substr(6, 5)는 다섯 문자를 복사하고 find는 시작 위치 6을 반환합니다.

## 이해 확인

**질문:** find 실패값을 바로 인덱스로 써도 되는가?

**답:** 안 됩니다. npos 여부를 먼저 검사해야 하며 문자열 길이 밖 위치로 접근하지 않습니다.
