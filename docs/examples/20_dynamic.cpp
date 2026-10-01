#include <iostream>
int main() {
    int count = 3;
    int* scores = new int[count]{};
    for (int i = 0; i < count; ++i) scores[i] = (i + 1) * 10;
    for (int i = 0; i < count; ++i) std::cout << scores[i] << ' ';
    std::cout << '\n';
    delete[] scores;
    scores = nullptr;
}
