## 상속: 공통 역할 확장

public 상속은 파생 객체를 기반 클래스의 역할로 사용할 수 있도록 합니다.

```cpp
class Character { // main 밖
public:
    virtual ~Character() = default;
    virtual int Attack() const { return 10; }
};
class Mage : public Character {
public:
    int Attack() const override { return 30; }
};
```

```cpp
Mage mage; // main 안
Character& character = mage;
std::cout << character.Attack();
```

**결과:** 30. 생성은 기반 클래스 다음 파생 클래스, 소멸은 반대 순서입니다.

## 가상 함수·다형성·추상 클래스

- **virtual:** 기반 포인터·참조를 통해서도 실제 객체의 재정의를 호출합니다.
- **override:** 올바른 재정의인지 컴파일러가 검사합니다.
- **순수 가상 함수:** virtual void Update() = 0;처럼 구현할 계약을 정합니다. 미구현 순수 가상 함수가 있으면 추상 클래스입니다.

| 구분 | 정의 | 예 |
| --- | --- | --- |
| 오버로딩 | 같은 이름, 다른 매개변수 | Attack() / Attack(int damage) |
| 오버라이딩 | 상속받은 가상 함수 재정의 | Mage::Attack() |

**주의:** 기반 함수가 비가상이면 기반 포인터를 통해 자식 함수로 자동 연결되지 않습니다. 기반 포인터로 파생 객체를 delete할 설계에서는 가상 소멸자가 필요합니다.

## 캐스팅 4종

| 캐스트 | 용도 | 주의 |
| --- | --- | --- |
| static_cast | 숫자·명시적 타입 변환 | 다운캐스팅에서 실제 타입을 실행 중 확인하지 않음 |
| dynamic_cast | 다형적 기반에서 검사한 다운캐스팅 | 포인터 실패는 nullptr, 참조 실패는 std::bad_cast |
| const_cast | const 속성 조정 | 원래 const인 객체를 수정하면 정의되지 않은 동작 |
| reinterpret_cast | 저수준 표현 변환 | 변환만으로 안전한 객체 접근이 보장되지 않음 |

```cpp
Character* base = &mage; // 위 클래스와 mage가 있는 main 안
if (Mage* actual = dynamic_cast<Mage*>(base)) {
    std::cout << actual->Attack();
}
```

**결과:** 30. 실패할 수 있는 포인터 변환은 결과를 검사한 뒤 사용합니다.
