# 동적 할당과 소유권

```cpp
int* one = new int(10);
int* many = new int[3]{1, 2, 3};
delete one;
delete[] many;
```

**핵심:** new와 delete, new[]와 delete[]를 짝 맞춥니다. 포인터 변수가 사라져도 동적 객체는 자동 삭제되지 않습니다.

**주의:** 삭제한 주소를 다시 사용하거나 두 번 삭제하면 안 됩니다. 소유자는 자원 해제를 책임지는 주체입니다.

