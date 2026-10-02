# 비트 연산자와 플래그

정수의 각 비트를 조합합니다. 플래그는 1, 2, 4, 8처럼 서로 다른 비트를 사용합니다.

| 기호 | 의미 | 예와 결과 |
| --- | --- | --- |
| & | 둘 다 1인 비트 유지 | 6u & 3u = 2 |
| \| | 하나라도 1이면 유지 | 6u \| 3u = 7 |
| ^ | 서로 다른 비트만 1 | 6u ^ 3u = 5 |
| ~ | 모든 비트 반전 | ~mask |
| << | 왼쪽 비트 이동 | 1u << 2 = 4 |
| >> | 오른쪽 비트 이동 | 8u >> 1 = 4 |

```cpp
constexpr unsigned Shield = 1u << 0;
constexpr unsigned Fury = 1u << 1;
unsigned flags = 0;
flags |= Shield;               // 켜기
bool hasShield = (flags & Shield) != 0; // 확인
flags ^= Fury;                // 토글
flags &= ~Shield;             // 끄기
std::cout << hasShield << ' ' << flags;
```

**결과:** 1 2. Fury만 남습니다.

**주의:** 플래그에는 unsigned를 사용합니다. 이동 횟수는 음수이거나 승격된 왼쪽 타입의 비트 수 이상이면 안 됩니다. ~는 전체 비트를 반전하므로 값은 타입의 비트 수에 따라 달라집니다. (flags & mask) == mask는 마스크의 모든 비트, != 0은 하나 이상 존재하는지 확인합니다.
