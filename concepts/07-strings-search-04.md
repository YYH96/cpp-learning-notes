# cin 다음의 getline

cin으로 숫자를 읽으면 줄바꿈이 남을 수 있습니다. 한 줄의 나머지를 버리고 getline을 호출합니다.

```cpp
int age;
std::string name;
std::cin >> age;
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
std::getline(std::cin, name);
```

**전제:** 숫자 입력이 성공한 경우. `<limits>`가 필요합니다. 20을 입력하고 다음 줄에 Kim Hero를 입력하면 name은 Kim Hero입니다.
