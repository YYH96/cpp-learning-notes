#include <iostream>
int main() {
    int hp = 100;
    hp -= 30;
    bool isHero = true;
    if (isHero && hp > 0) {
        std::cout << "Hero alive\n";
    }
    int score = 88;
    if (score >= 90) std::cout << "A\n";
    else if (score >= 80) std::cout << "B\n";
    else std::cout << "C\n";
    char turn = 'X';
    turn = turn == 'X' ? 'O' : 'X';
    int n = 5;
    int before = n++;  // before=5, n=6
    int after = ++n;   // after=7, n=7
    std::cout << turn << ' ' << before << ' ' << after << '\n';
}
