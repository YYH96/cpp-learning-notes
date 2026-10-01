[← 전체 목차](../README.md) · [이전 챕터](05-functions-scope.md) · [다음 챕터 →](07-strings-search.md)

# 06. 배열, 포인터, 참조와 2차원 데이터

> **학습 목표** · 값·주소·참조의 차이를 이해하고 배열 인덱스를 안전하게 다룬다.

## 이 페이지에서 다룰 내용

- [배열과 인덱스](#배열과-인덱스)
- [주소와 역참조](#주소와-역참조)
- [const 포인터와 참조](#const-포인터와-참조)
- [2차원 배열과 좌표](#2차원-배열과-좌표)

---

## 배열과 인덱스
배열은 같은 자료형의 요소를 연속해서 저장합니다. 크기가 N이면 유효 인덱스는 0~N−1입니다. 일반 고정 배열의 크기는 컴파일 시간에 결정해야 합니다. 범위를 벗어난 접근을 자동으로 막아주지 않습니다.
배열과 포인터는 서로 다른 자료형입니다. 배열 이름은 많은 식에서 첫 요소를 가리키는 포인터로 변환됩니다. 배열 인자 int arr[]는 함수 매개변수에서는 int*로 취급하므로 길이를 따로 전달합니다.
## 주소와 역참조
&변수는 주소를 구하고 *포인터는 그 주소의 객체에 접근합니다. nullptr는 아무 객체도 가리키지 않는 포인터 값입니다. 유효한 객체를 가리킬 때만 역참조해야 합니다.
포인터 + 1은 해당 자료형의 요소 하나만큼 이동합니다. 배열 안에서 arr[i]와 *(arr+i)는 같은 요소에 접근합니다.

```cpp
#include <iostream>
void PrintArray(const int* arr, int count) {
    for (int i = 0; i < count; ++i) std::cout << arr[i] << ' ';
    std::cout << '\n';
}
void AddOne(int* value) {
    if (value != nullptr) ++(*value);
}
int main() {
    int numbers[3] = {10, 20, 30};
    int count = static_cast<int>(sizeof(numbers) / sizeof(numbers[0]));
    PrintArray(numbers, count);
    int* p = numbers;
    std::cout << *(p + 2) << '\n'; // 30
    AddOne(&numbers[0]);
    PrintArray(numbers, count);   // 11 20 30
}
```

📎 [실행할 예제 파일](../examples/11_array_pointer.cpp)

**sizeof 주의:** 실제 배열이 보이는 위치에서는 전체 크기를 구할 수 있지만, 함수의 포인터 매개변수에서는 포인터 크기만 나옵니다.
## const 포인터와 참조
const int*는 이 포인터를 통해 대상 값을 수정하지 못하게 합니다. int* const는 포인터가 다른 주소를 가리키지 못하게 합니다. const int* const는 둘 다 제한합니다.
참조 int&는 기존 객체의 별칭입니다. 선언과 동시에 연결해야 하고 대입으로 연결 대상을 바꾸지 못합니다. const 참조는 복사 없이 읽기 목적으로 객체를 전달할 때 활용합니다.

```cpp
#include <iostream>
void Damage(int& hp, int amount) { hp -= amount; }
int main() {
    int hp = 100, other = 500;
    int& alias = hp;
    Damage(alias, 20);
    std::cout << hp << '\n';       // 80
    alias = other;                 // hp에 500을 대입
    const int* readOnly = &hp;
    int* const fixedAddress = &hp;
    *fixedAddress = 300;
    const int& view = hp;
    std::cout << *readOnly << ' ' << view << '\n'; // 300 300
}
```

📎 [실행할 예제 파일](../examples/12_reference.cpp)

## 2차원 배열과 좌표
board[row][col]에서 row는 행, col은 열입니다. 1차원 저장소를 보드처럼 사용하면 인덱스는 row×열 수+col입니다. 반대로 행은 index/열 수, 열은 index%열 수입니다.
고정 2차원 배열을 함수에 넘길 때는 열 크기가 타입에 포함됩니다. int board[2][3]은 int**와 호환되지 않습니다. 행별로 별도 할당한 int**와 연속된 2차원 배열을 구분합니다.

```cpp
#include <iostream>
void PrintBoard(const int board[][3], int rows) {
    for (int row = 0; row < rows; ++row) {
        for (int col = 0; col < 3; ++col) std::cout << board[row][col] << ' ';
        std::cout << '\n';
    }
}
int main() {
    int board[2][3] = {{10,20,30}, {40,50,60}};
    PrintBoard(board, 2);
    int flat[6] = {10,20,30,40,50,60};
    std::cout << flat[1 * 3 + 2] << '\n'; // 60
}
```

📎 [실행할 예제 파일](../examples/13_board.cpp)

---

[← 전체 목차](../README.md) · [이전 챕터](05-functions-scope.md) · [다음 챕터 →](07-strings-search.md)
