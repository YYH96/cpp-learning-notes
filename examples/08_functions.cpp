#include <iostream>
int Add(int a, int b = 10);
double Add(double a, double b);
int main() {
    std::cout << Add(5) << '\n';        // 15
    std::cout << Add(2, 3) << '\n';     // 5
    std::cout << Add(1.5, 2.5) << '\n'; // 4
}
int Add(int a, int b) { return a + b; }
double Add(double a, double b) { return a + b; }
