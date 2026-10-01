#include <iostream>
#include <string>
template<typename T>
T Add(T left, T right) { return left + right; }
template<typename T>
class Cube {
    T first, second;
public:
    Cube(const T& a, const T& b) : first(a), second(b) {}
    const T& GetFirst() const { return first; }
};
int main() {
    std::cout << Add<int>(10, 20) << '\n'; // 30
    std::cout << Add<double>(1.5, 2.5) << '\n'; // 4
    Cube<std::string> weapons("Sword", "Shield");
    std::cout << weapons.GetFirst() << '\n';
}
