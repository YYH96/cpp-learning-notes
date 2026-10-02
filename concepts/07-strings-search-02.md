# strlen과 sizeof

| 표현 | 구하는 것 | "Cat" 배열의 결과 |
| --- | --- | --- |
| strlen(word) | 널 문자 전까지의 문자열 길이 | 3 |
| sizeof(word) | 실제 배열의 저장 바이트 수 | 4 |
| sizeof(pointer) | 포인터 자체의 바이트 수 | 빌드 환경에 따라 다름 |

**주의:** std::string은 char 요소 수를 셉니다. UTF-8 한글의 화면 글자 수와 다를 수 있습니다.

