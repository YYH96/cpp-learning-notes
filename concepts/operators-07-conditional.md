# 삼항 조건 연산자

조건 ? 참일 때 값 : 거짓일 때 값 형식으로 두 값 중 하나를 선택합니다. 조건에 따라 선택된 쪽만 평가합니다.

```cpp
int hp = 30;
std::string state = hp > 0 ? "Alive" : "Dead";
int maxValue = 7 > 3 ? 7 : 3;
std::cout << state << ' ' << maxValue;
```

**결과:** Alive 7.

**주의:** 값을 선택할 때 간결합니다. 여러 동작을 수행하거나 중첩이 깊어지면 if / else로 풀어 씁니다. 두 결과의 타입 조합에 따라 변환이 일어날 수 있습니다.
