#include <iostream>
void Damage(int& hp, int amount) { hp -= amount; }
int main() {
    int hp = 100, other = 500;
    int& alias = hp;
    Damage(alias, 20);
    std::cout << hp << '\n';       // 80
    alias = other;                 // hp에 500을 대입
    const int* readOnly = &hp;
    int* const fixedAddress = &hp;
    *fixedAddress = 300;
    const int& view = hp;
    std::cout << *readOnly << ' ' << view << '\n'; // 300 300
}
