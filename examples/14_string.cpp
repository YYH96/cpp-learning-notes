#include <iostream>
#include <string>
int main() {
    std::string name = "YoonYoungHo";
    name.insert(4, "_");
    name.erase(4, 1);
    name.replace(0, 4, "Kim");
    auto pos = name.find("Young");
    if (pos != std::string::npos) std::cout << pos << '\n'; // 3
    std::cout << name.substr(0, 3) << '\n';                 // Kim
    std::cout << std::string("A B").size() << '\n';         // 3
}
