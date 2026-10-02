# cin 다음의 getline

cin으로 숫자를 읽으면 줄바꿈이 남을 수 있습니다. 한 줄의 나머지를 버리고 getline을 호출합니다.

## 개념과 동작 원리

>> 숫자 추출은 숫자 이후 줄바꿈을 남길 수 있습니다. 이어진 getline은 남은 줄바꿈을 소비해 빈 줄을 반환할 수 있습니다.

## 사용 시점과 다른 개념의 구분

숫자 선택 뒤 공백 포함 이름을 받는 혼합 입력에서 처리합니다. ignore는 남은 한 줄을 버리므로 같은 줄에 보존해야 할 데이터가 있는지도 확인합니다.

## 문법과 예제

```cpp
int age;
std::string name;
std::cin >> age;
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
std::getline(std::cin, name);
```

**전제:** 숫자 입력이 성공한 경우. `<limits>`가 필요합니다. 20을 입력하고 다음 줄에 Kim Hero를 입력하면 name은 Kim Hero입니다.

## 예제를 이해하는 순서

age를 읽은 뒤 ignore로 줄바꿈까지 버리고 다음 줄 전체를 name으로 받습니다. 숫자 추출 실패 상태에서는 먼저 clear 등으로 상태를 복구해야 합니다.

## 이해 확인

**질문:** ignore 한 번으로 모든 입력 문제를 해결하는가?

**답:** 아닙니다. 성공 여부·버릴 범위·남겨야 할 내용을 입력 형식에 맞게 판단해야 합니다.
