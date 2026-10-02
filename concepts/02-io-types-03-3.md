# getline 줄 입력

std::getline으로 공백을 포함한 한 줄을 읽습니다. <string>과 입력 스트림이 필요합니다.

```cpp
std::string name;
std::getline(std::cin, name);
std::cout << name;
```

**예:** Kim Hero 입력 시 Kim Hero 출력. cin >> 다음에 호출하면 남아 있는 줄바꿈 처리부터 확인합니다.
