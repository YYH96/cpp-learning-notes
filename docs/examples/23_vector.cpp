#include <iostream>
#include <vector>
int main() {
    std::vector<int> values;
    values.reserve(10);
    std::cout << values.size() << '\n'; // 0
    values.push_back(10);
    values.push_back(20);
    values.resize(4, 0);
    values[2] = 30;
    for (int value : values) std::cout << value << ' '; // 10 20 30 0
    std::cout << '\n';
    if (!values.empty()) values.pop_back();
    auto oldCapacity = values.capacity();
    values.clear();
    std::cout << values.size() << ' ' << (values.capacity() == oldCapacity) << '\n'; // 0 1
    std::vector<std::vector<int>> board(3, std::vector<int>(4, 0));
    board[2][3] = 1;
}
