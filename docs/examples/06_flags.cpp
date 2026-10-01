#include <iostream>
int main() {
    constexpr unsigned fury = 1u << 0;
    constexpr unsigned shield = 1u << 1;
    unsigned buffs = 0;
    buffs |= fury;                    // 켜기
    buffs |= shield;
    std::cout << ((buffs & fury) != 0) << '\n';
    buffs &= ~fury;                    // 끄기
    buffs ^= shield;                   // 토글
    std::cout << buffs << '\n';
}
