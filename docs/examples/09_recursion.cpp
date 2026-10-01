#include <iostream>
// 전제: 0 <= n <= 12 (이 예제는 int 범위를 고려)
int Factorial(int n) {
    if (n <= 1) return 1;
    return n * Factorial(n - 1);
}
int SumTail(int n, int acc = 0) {
    if (n <= 0) return acc;
    return SumTail(n - 1, acc + n);
}
// 수업의 1, 1, 2, 3, ... 규칙, 전제: 1 <= n <= 46
int Fibonacci(int n) {
    if (n <= 2) return 1;
    int a = 1, b = 1;
    for (int i = 3; i <= n; ++i) {
        int next = a + b;
        a = b;
        b = next;
    }
    return b;
}
int main() {
    std::cout << Factorial(5) << ' ' << SumTail(10) << ' ' << Fibonacci(10) << '\n';
}
