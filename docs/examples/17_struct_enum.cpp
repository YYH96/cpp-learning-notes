#include <iostream>
#include <string>
enum class Job { Warrior, Mage };
struct Student {
    std::string name;
    int kor = 0, eng = 0, math = 0;
    double Average() const { return (kor + eng + math) / 3.0; }
};
int main() {
    Student student{"Kim", 80, 90, 85};
    Student* p = &student;
    Job job = Job::Mage;
    std::cout << p->name << ' ' << student.Average() << '\n';
    std::cout << static_cast<int>(job) << '\n';
}
