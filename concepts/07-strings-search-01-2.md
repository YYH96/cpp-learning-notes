# std::string

<string>에서 제공하는 가변 길이 문자열입니다. 길이와 저장 공간을 관리하고 연결·검색 등의 함수를 제공합니다.

```cpp
std::string name = "Hero";
name += "!";
std::cout << name << ' ' << name.size();
```

**결과:** Hero! 5. [] 접근 전 인덱스를 확인하고, c_str()이 반환한 주소는 문자열 변경 후 무효화될 수 있습니다.
