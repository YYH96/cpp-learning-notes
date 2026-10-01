#include <iostream>
int main() {
    const int maxHP = 100;
    constexpr int boardWidth = 5;
    int hp = maxHP;
    hp -= 20;
    std::cout << hp << ' ' << boardWidth << '\n';
}
