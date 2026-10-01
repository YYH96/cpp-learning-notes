#include <iostream>
class GameManager {
    GameManager() = default;
    ~GameManager() = default;
    GameManager(const GameManager&) = delete;
    GameManager& operator=(const GameManager&) = delete;
public:
    static GameManager& Instance() {
        static GameManager instance;
        return instance;
    }
    void Run() { std::cout << "Game starts\n"; }
};
int main() { GameManager::Instance().Run(); }
