#include <iostream>
struct Position {
    int x = 0, y = 0;
    bool operator==(const Position& other) const {
        return x == other.x && y == other.y;
    }
    bool operator!=(const Position& other) const { return !(*this == other); }
};
int main() {
    Position snake{3,4}, apple{3,4};
    std::cout << (snake == apple) << '\n'; // 1
}
