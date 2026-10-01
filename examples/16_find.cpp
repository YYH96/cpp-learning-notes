#include <iostream>
#include <string>
int MyFind(const std::string& text, const std::string& need) {
    if (need.empty()) return 0;
    if (need.size() > text.size()) return -1;
    for (std::size_t i = 0; i <= text.size() - need.size(); ++i) {
        std::size_t j = 0;
        while (j < need.size() && text[i + j] == need[j]) ++j;
        if (j == need.size()) return static_cast<int>(i);
    }
    return -1;
}
int main() {
    std::cout << MyFind("sadbutsad", "dbu") << '\n'; // 2
    std::cout << MyFind("abc", "xyz") << '\n';      // -1
}
