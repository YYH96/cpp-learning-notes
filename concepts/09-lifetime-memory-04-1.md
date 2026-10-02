# 복사 생성자

기존 객체를 이용해 새 객체를 초기화합니다.

```cpp
std::string a = "Hero";
std::string b = a;
b[0] = 'Z';
std::cout << a << ' ' << b;
```

**결과:** Hero Zero. raw 포인터를 소유한 클래스는 기본 복사로 주소만 복사되면 중복 해제가 생길 수 있어 복사 정책이 필요합니다.
