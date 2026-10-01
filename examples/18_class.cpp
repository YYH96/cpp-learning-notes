#include <iostream>
#include <string>
class Player {
    std::string name;
    int hp = 100;
public:
    explicit Player(const std::string& name) : name(name) {}
    void SetName(const std::string& name) {
        if (!name.empty()) this->name = name;
    }
    void Damage(int amount) {
        if (amount <= 0) return;
        hp = amount >= hp ? 0 : hp - amount;
    }
    int GetHP() const { return hp; }
    const std::string& GetName() const { return name; }
};
int main() {
    Player player("Warrior");
    player.Damage(30);
    std::cout << player.GetName() << ' ' << player.GetHP() << '\n';
}
