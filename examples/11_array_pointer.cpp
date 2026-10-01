#include <iostream>
void PrintArray(const int* arr, int count) {
    for (int i = 0; i < count; ++i) std::cout << arr[i] << ' ';
    std::cout << '\n';
}
void AddOne(int* value) {
    if (value != nullptr) ++(*value);
}
int main() {
    int numbers[3] = {10, 20, 30};
    int count = static_cast<int>(sizeof(numbers) / sizeof(numbers[0]));
    PrintArray(numbers, count);
    int* p = numbers;
    std::cout << *(p + 2) << '\n'; // 30
    AddOne(&numbers[0]);
    PrintArray(numbers, count);   // 11 20 30
}
