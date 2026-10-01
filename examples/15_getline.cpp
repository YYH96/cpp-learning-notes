#include <iostream>
#include <limits>
#include <string>
int main() {
    int level = 0;
    std::string message;
    if (!(std::cin >> level)) return 1;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::getline(std::cin, message);
    std::cout << level << ": " << message << '\n';
}
