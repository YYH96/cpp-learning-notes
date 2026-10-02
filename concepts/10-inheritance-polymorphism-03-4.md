# reinterpret_cast

포인터 등의 저수준 변환에 사용합니다. 변환한 포인터로 임의 타입의 객체를 읽을 수 있다는 보장은 없습니다.

```cpp
int value = 10;
unsigned char* bytes = reinterpret_cast<unsigned char*>(&value);
std::cout << sizeof(value);
```

**결과:** int의 바이트 크기 출력. unsigned char로 객체 표현의 바이트를 살펴볼 수 있지만 바이트 순서와 크기는 환경에 따릅니다. 일반적인 숫자 변환에는 static_cast를 사용합니다.
