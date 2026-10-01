#include <iostream>
void PrintBoard(const int board[][3], int rows) {
    for (int row = 0; row < rows; ++row) {
        for (int col = 0; col < 3; ++col) std::cout << board[row][col] << ' ';
        std::cout << '\n';
    }
}
int main() {
    int board[2][3] = {{10,20,30}, {40,50,60}};
    PrintBoard(board, 2);
    int flat[6] = {10,20,30,40,50,60};
    std::cout << flat[1 * 3 + 2] << '\n'; // 60
}
