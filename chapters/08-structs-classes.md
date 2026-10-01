[← 전체 목차](../README.md) · [이전 챕터](07-strings-search.md) · [다음 챕터 →](09-lifetime-memory.md)

# 08. 구조체, 열거형과 클래스

> **학습 목표** · 구조체와 클래스로 데이터를 묶고 접근 권한을 설계한다.

## 이 페이지에서 다룰 내용

- [struct와 enum](#struct와-enum)
- [객체 지향과 접근 지정자](#객체-지향과-접근-지정자)
- [this·Getter/Setter·const 멤버 함수](#thisgettersetterconst-멤버-함수)

---

## struct와 enum
struct는 이름·점수처럼 관련된 데이터를 하나의 사용자 정의 자료형으로 묶습니다. 멤버 함수도 가질 수 있습니다. 객체의 멤버는 .으로, 포인터로 가리키는 객체의 멤버는 ->로 접근합니다.
enum은 정수 상태에 이름을 붙입니다. enum class는 이름 범위를 구분하며 정수로 자동 변환하지 않으므로 필요한 곳에서 static_cast를 사용합니다.
구조체 크기는 멤버 크기의 합보다 클 수 있습니다. 정렬을 위한 패딩 때문이며 정확한 크기는 sizeof로 확인합니다. 멤버 순서와 환경에 따라 달라집니다.

```cpp
#include <iostream>
#include <string>
enum class Job { Warrior, Mage };
struct Student {
    std::string name;
    int kor = 0, eng = 0, math = 0;
    double Average() const { return (kor + eng + math) / 3.0; }
};
int main() {
    Student student{"Kim", 80, 90, 85};
    Student* p = &student;
    Job job = Job::Mage;
    std::cout << p->name << ' ' << student.Average() << '\n';
    std::cout << static_cast<int>(job) << '\n';
}
```

📎 [실행할 예제 파일](../examples/17_struct_enum.cpp)

## 객체 지향과 접근 지정자
클래스는 데이터와 기능을 묶는 설계도이고 객체는 그 설계도로 만든 실제 대상입니다. class의 기본 멤버 접근은 private, struct는 public입니다. 기본 상속 접근도 각각 private와 public입니다.
public은 외부에서 사용하는 인터페이스, private는 클래스 내부와 허용된 friend에서 사용하는 구현, protected는 클래스와 파생 클래스에서 사용하는 영역입니다.
**캡슐화:** 관련 데이터·기능을 묶습니다. **정보 은닉:** 내부를 제한하고 데이터 규칙을 지킵니다. **추상화:** 필요한 역할과 인터페이스를 드러냅니다. **상속:** 공통 구조를 재사용합니다. **다형성:** 동일한 호출을 실제 객체에 따라 다르게 처리합니다.
절차 지향은 처리 순서와 함수에, 객체 지향은 객체의 역할과 협력에 초점을 둡니다. 어느 방식이 항상 더 빠르다고 단정할 수 없습니다. 데이터 지향은 데이터 배치·접근 패턴에 초점을 두는 관점으로 수업에서 개요만 소개됐습니다.
## this·Getter/Setter·const 멤버 함수

```cpp
#include <iostream>
#include <string>
class Player {
    std::string name;
    int hp = 100;
public:
    explicit Player(const std::string& name) : name(name) {}
    void SetName(const std::string& name) {
        if (!name.empty()) this->name = name;
    }
    void Damage(int amount) {
        if (amount <= 0) return;
        hp = amount >= hp ? 0 : hp - amount;
    }
    int GetHP() const { return hp; }
    const std::string& GetName() const { return name; }
};
int main() {
    Player player("Warrior");
    player.Damage(30);
    std::cout << player.GetName() << ' ' << player.GetHP() << '\n';
}
```

📎 [실행할 예제 파일](../examples/18_class.cpp)

this는 현재 멤버 함수를 호출한 객체를 가리킵니다. const 멤버 함수는 보통 해당 객체의 상태를 바꾸지 않는 조회 함수에 붙입니다. Setter에는 검증을 넣어 외부 입력으로 상태가 깨지지 않게 합니다. friend는 지정한 함수·클래스에 비공개 접근을 허용하며 자동으로 양방향·전이·상속되지 않습니다.

---

[← 전체 목차](../README.md) · [이전 챕터](07-strings-search.md) · [다음 챕터 →](09-lifetime-memory.md)
