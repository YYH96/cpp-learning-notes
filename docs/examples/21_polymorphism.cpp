#include <iostream>
class Skill {
public:
    virtual ~Skill() = default;
    virtual void Use() = 0;
};
class FireBall : public Skill {
public:
    void Use() override { std::cout << "Fireball\n"; }
};
class Heal : public Skill {
public:
    void Use() override { std::cout << "Heal\n"; }
};
int main() {
    Skill* skills[2] = {new FireBall, new Heal};
    for (Skill* skill : skills) {
        skill->Use();
        delete skill;
    }
}
