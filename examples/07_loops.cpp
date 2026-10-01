#include <iostream>
int main() {
    for (int i = 1; i <= 7; ++i) {
        if (i % 2 == 0) continue;
        std::cout << i << ' ';
    }
    std::cout << '\n';
    constexpr int height = 3;
    for (int row = 0; row < height; ++row) {
        for (int space = 0; space < height - row - 1; ++space)
            std::cout << ' ';
        for (int star = 0; star < 2 * row + 1; ++star)
            std::cout << '*';
        std::cout << '\n';
    }
    int count = 0;
    while (count < 3) { std::cout << count++ << ' '; }
    std::cout << '\n';
    int menu = 0;
    do { std::cout << "Menu shown once\n"; } while (menu != 0);
}
