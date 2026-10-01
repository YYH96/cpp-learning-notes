[← 전체 목차](../README.md) · [이전 챕터](12-templates-operators.md) · [다음 챕터 →](14-review-corrections.md)

# 13. 게임을 만들며 연결한 개념

> **학습 목표** · 게임 루프·좌표·씬 전환에 개별 개념을 연결한다.

## 이 페이지에서 다룰 내용

- [실습별로 배운 것](#실습별로-배운-것)
- [숫자 야구 판정 — 복습용 완성 예제](#숫자-야구-판정--복습용-완성-예제)
- [보드의 대각선 검사 — 복습용 정리](#보드의-대각선-검사--복습용-정리)
- [게임 루프와 파일 분리](#게임-루프와-파일-분리)
- [싱글톤 — TextRPG에서 배운 함수 static 방식](#싱글톤--textrpg에서-배운-함수-static-방식)
- [씬 관리와 다형성](#씬-관리와-다형성)

---

## 실습별로 배운 것
**성적 계산 → 성적 관리:** 입출력·합계·실수 평균 → 함수 분리 → 구조체·클래스 → 런타임 학생 수와 동적 배열.
**커피 주문 → 커피머신 클래스:** 메뉴 분기·잔액·반복 종료 → 객체의 상태와 동작·가격 조회·메뉴 enum.
**업다운:** 난수·시드·범위·입력 비교·시도 횟수·종료 플래그 → Init·입력·판정 함수로 분리.
**검 강화:** 비용·성공 확률·판매가 계산, 돈 부족 검사, 난수와 확률 비교, 게임 상태 관리.
**숫자 야구:** 중복 없는 숫자 배열과 입력 배열, 중첩 순회로 위치·숫자 비교. 원본은 스트라이크·볼 판정이 과제로 남아 있습니다.
**짝 맞추기:** 카드 배열·셔플·공개 상태 배열·이전 선택·중복 선택 방지·페어 수.
**틱택토:** 2차원 보드·객체 수명·입력 검증·턴 전환·가로/세로/대각선 승리·무승부.
**빙고:** 보드·유저·컴퓨터·매니저로 역할 분리, 상속·가상 함수·vector·friend·싱글톤·다중 파일 구성.
**스네이크:** 좌표 구조체와 비교 연산자, 몸통 vector, 방향 enum, 역방향 금지, 벽·몸통 충돌, 성장·사과 재생성, 실시간 키 입력.
**TextRPG:** 싱글톤 게임 매니저·씬 매니저·추상 씬·로비/게임/전투 씬·현재 씬의 Update/Draw·씬 전환. 던전·직업·상점 등의 전체 게임 로직은 앞으로 구현할 구상입니다.
## 숫자 야구 판정 — 복습용 완성 예제
같은 숫자이면서 같은 인덱스면 스트라이크, 숫자만 같으면 볼입니다. 아래는 수업에서 남긴 판정 부분을 채운 예제입니다. 입력 배열은 1~9의 서로 다른 숫자라는 전제입니다.

```cpp
#include <iostream>
int main() {
    int answer[3] = {1,2,3};
    int guess[3] = {1,3,2};
    int strikes = 0, balls = 0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (guess[i] == answer[j]) {
                if (i == j) ++strikes;
                else ++balls;
            }
        }
    }
    std::cout << strikes << "S " << balls << "B\n"; // 1S 2B
}
```

📎 [실행할 예제 파일](../examples/27_baseball.cpp)

## 보드의 대각선 검사 — 복습용 정리
가로는 row×N+col, 세로는 col+row×N, 왼쪽 위 대각선은 i×N+i, 오른쪽 위 대각선은 i×N+(N−1−i)로 접근합니다. 비교해야 하는 것은 계산한 인덱스가 아니라 **해당 인덱스에 저장된 값**입니다.

```cpp
#include <iostream>
int main() {
    constexpr int N = 3;
    char board[N*N] = {'*','1','*', '2','*','3', '*','4','*'};
    bool left = true, right = true;
    for (int i = 0; i < N; ++i) {
        left = left && board[i * N + i] == '*';
        right = right && board[i * N + (N - 1 - i)] == '*';
    }
    std::cout << left << ' ' << right << '\n'; // 1 1
}
```

📎 [실행할 예제 파일](../examples/28_diagonal.cpp)

## 게임 루프와 파일 분리
게임 매니저가 초기화 → 반복 실행 → 자원 정리를 맡고, 루프 안에서 입력·상태 갱신·화면 출력을 나눕니다. 수업 원본의 호출 순서는 프로젝트마다 다릅니다. 중요한 것은 각 함수의 책임과 실행 순서를 이해하는 것입니다.
.h에는 클래스·함수의 선언과 필요한 정의를 두고 .cpp에 구현을 분리합니다. pragma once는 헤더의 중복 포함을 막습니다. 공통 GameInfo.h와 미리 컴파일된 헤더(PCH)는 같은 개념이 아니며, PCH는 별도 빌드 설정을 필요로 합니다.
포인터 멤버만 선언할 때는 전방 선언으로 의존성을 줄일 수 있습니다. 실제 멤버를 사용하거나 객체를 삭제하는 구현 위치에서는 완전한 클래스 정의를 포함해야 합니다.
## 싱글톤 — TextRPG에서 배운 함수 static 방식

```cpp
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
```

📎 [실행할 예제 파일](../examples/29_singleton.cpp)

싱글톤은 하나의 인스턴스를 제공하는 패턴입니다. 패턴은 이름 붙인 설계 방식이며 모든 기능에 억지로 적용하는 목적은 아닙니다. inline은 호출부에 코드가 반드시 펼쳐진다는 보장이 아니고, 클래스 내부에 정의한 멤버 함수는 일반적으로 암시적으로 inline입니다.
## 씬 관리와 다형성
CBaseScene의 Update·Draw를 순수 가상 함수로 선언하고 파생 씬에서 구현합니다. vector<CBaseScene*>에 씬을 저장하면 공통 인터페이스로 서로 다른 씬을 실행할 수 있습니다.
씬 변경은 범위 검사 → 같은 씬인지 검사 → 기존 씬 Exit → 현재 포인터 교체 → 새 씬 Enter 순서입니다. Enter·Exit에도 씬별 동작을 넣고 싶다면 기반에서 virtual로 선언해야 합니다. 수업 원본에서는 두 함수가 비가상 함수입니다.

---

[← 전체 목차](../README.md) · [이전 챕터](12-templates-operators.md) · [다음 챕터 →](14-review-corrections.md)
