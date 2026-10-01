#include <iostream>
int main() {
    int answer[3] = {1,2,3};
    int guess[3] = {1,3,2};
    int strikes = 0, balls = 0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (guess[i] == answer[j]) {
                if (i == j) ++strikes;
                else ++balls;
            }
        }
    }
    std::cout << strikes << "S " << balls << "B\n"; // 1S 2B
}
