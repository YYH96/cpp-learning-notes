#include <iostream>
#include <list>
int main() {
    std::list<int> values{1,2,3,4,5};
    for (auto it = values.begin(); it != values.end();) {
        if (*it % 2 == 0) it = values.erase(it);
        else ++it;
    }
    values.insert(values.begin(), 99); // 지정 위치 앞에 삽입
    for (int value : values) std::cout << value << ' '; // 99 1 3 5
    std::cout << '\n';
}
