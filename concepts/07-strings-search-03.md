# 수정·부분 문자열·검색

```cpp
std::string text = "Hello World";
std::string part = text.substr(6, 5);
auto position = text.find("World");
```

**결과:** part는 World, position은 6. substr의 두 번째 인자는 끝 위치가 아닌 **개수**입니다.

**주의:** find가 실패하면 std::string::npos. 위치를 사용하기 전에 확인합니다. replace(pos, count, text)의 count도 개수입니다.

