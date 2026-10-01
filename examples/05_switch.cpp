#include <iostream>
int main() {
    int menu = 2;
    switch (menu) {
    case 0: std::cout << "Exit\n"; break;
    case 1: std::cout << "Americano\n"; break;
    case 2: std::cout << "Latte\n"; break;
    default: std::cout << "Invalid menu\n"; break;
    }
}
