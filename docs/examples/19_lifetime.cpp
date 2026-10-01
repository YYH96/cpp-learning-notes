#include <iostream>
class Monster {
    static int count;
public:
    Monster() { ++count; }
    ~Monster() { --count; }
    Monster(const Monster&) = delete;
    Monster& operator=(const Monster&) = delete;
    static int Count() { return count; }
};
int Monster::count = 0;
int main() {
    std::cout << Monster::Count() << '\n'; // 0
    {
        Monster a, b;
        std::cout << Monster::Count() << '\n'; // 2
    }
    std::cout << Monster::Count() << '\n'; // 0
}
