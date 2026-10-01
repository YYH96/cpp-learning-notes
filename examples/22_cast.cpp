#include <iostream>
class Parent { public: virtual ~Parent() = default; };
class Warrior : public Parent {
public:
    void Attack() { std::cout << "Sword attack\n"; }
};
class Mage : public Parent {};
int main() {
    Parent* character = new Warrior;
    if (auto* warrior = dynamic_cast<Warrior*>(character)) warrior->Attack();
    std::cout << (dynamic_cast<Mage*>(character) == nullptr) << '\n';
    delete character;
    int value = 5;                  // 원래 const가 아님
    const int* read = &value;
    int* write = const_cast<int*>(read);
    *write = 10;
    std::cout << value << '\n';
}
