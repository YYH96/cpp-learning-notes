#include <iostream>
int main() {
    int kor = 80, eng = 90, math = 85;
    int sum = kor + eng + math;
    double average = static_cast<double>(sum) / 3;
    char grade = 'A';
    bool passed = average >= 60;
    std::cout << sum << ' ' << average << ' ' << grade << ' ' << passed << '\n';
    std::cout << "int bytes: " << sizeof(int) << '\n';
}
