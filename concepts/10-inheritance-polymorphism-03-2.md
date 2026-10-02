# dynamic_cast

다형적 기반 클래스에서 파생 타입으로 안전하게 변환할 때 검사합니다. 기반 클래스에 가상 함수가 필요합니다.

```cpp
class Base { public: virtual ~Base() = default; }; // main 밖
class Mage : public Base {};
```

```cpp
Mage mage;
Base* base = &mage;
Mage* actual = dynamic_cast<Mage*>(base);
std::cout << (actual != nullptr);
```

**결과:** 1. 실패한 포인터 변환은 nullptr, 실패한 참조 변환은 std::bad_cast를 던집니다.
