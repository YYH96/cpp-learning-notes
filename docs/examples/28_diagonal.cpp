#include <iostream>
int main() {
    constexpr int N = 3;
    char board[N*N] = {'*','1','*', '2','*','3', '*','4','*'};
    bool left = true, right = true;
    for (int i = 0; i < N; ++i) {
        left = left && board[i * N + i] == '*';
        right = right && board[i * N + (N - 1 - i)] == '*';
    }
    std::cout << left << ' ' << right << '\n'; // 1 1
}
