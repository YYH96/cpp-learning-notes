#include <iostream>
namespace Game {
    int NextID() {
        static int count = 0;
        return ++count;
    }
}
int main() {
    int count = 100;
    std::cout << Game::NextID() << ' ' << Game::NextID() << ' ' << count << '\n';
}
