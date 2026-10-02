## 클래스와 객체의 기본

클래스는 데이터와 동작의 설계도, 객체는 그 타입으로 만든 실제 대상입니다.

```cpp
class Player { // main 밖
public:
    int hp = 100;
    void Damage(int amount) { hp -= amount; }
};
```

```cpp
Player hero; // main 안: 객체 생성
hero.Damage(20);
std::cout << hero.hp;
```

**결과:** 80. 위 public 데이터는 문법 설명용입니다. 실제 설계에서는 private 데이터와 검증된 함수를 통해 상태를 관리합니다.

## 멤버 접근·this·접근 권한

| 표현 | 의미 | 예 |
| --- | --- | --- |
| . | 객체의 멤버 접근 | hero.hp |
| -> | 포인터가 가리키는 객체의 멤버 접근 | pointer->hp |
| this | 현재 객체를 가리키는 포인터 | this->hp |

**public:** 외부 인터페이스. **private:** 자기 클래스와 friend의 내부 접근. **protected:** 파생 클래스에서도 접근 가능하되 접근 규칙을 따라야 합니다.

## struct와 객체 지향 용어

- **struct / class:** 둘 다 데이터·멤버 함수를 가집니다. 기본 멤버 접근 권한은 public / private입니다.
- **캡슐화:** 데이터와 동작을 묶습니다. **정보 은닉:** 내부 접근을 제한해 규칙을 지킵니다.
- **추상화:** 필요한 역할과 인터페이스를 드러냅니다. 상속·다형성은 다음 챕터에서 구분합니다.

**조회·수정:** Getter는 값 조회, Setter는 검증된 변경. const 멤버 함수는 일반적으로 객체를 변경하지 않는 조회 함수에 붙입니다.

## enum과 enum class

```cpp
enum class Direction { Left, Right }; // main 밖
```

```cpp
Direction direction = Direction::Right; // main 안
int value = static_cast<int>(direction);
```

**결과:** value는 1. enum class는 이름 범위를 구분하며 정수로 자동 변환하지 않습니다.
