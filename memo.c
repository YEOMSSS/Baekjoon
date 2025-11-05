#include <stdio.h>
#include <string.h>

int main()
{

    char str[2501] = {0};
    char ans[51] = {0};

    fgets(str, sizeof(str), stdin);
    fgets(ans, sizeof(ans), stdin);

    str[strcspn(str, "\n")] = '\0';
    ans[strcspn(ans, "\n")] = '\0';

    int len = strlen(ans);
    int Count = 0;

    if (len == 0)
    {
        printf("0\n");
        return 0;
    }

    // 읽을 위치 저장하는 포인터 변수
    char *current_pos = str;
    char *found;

    // strstr 함수 인자로 str가 아닌 새로 포인터 변수로 검색 위치를 변경해야된다.
    // str는 배열이기 때문에 시작 주소를 변경할 수가 없다.
    while ((found = strstr(current_pos, ans)) != NULL)
    {
        // 찾는 문자열이 존재해서 while문 조건을 통과하면 증가
        Count++;
        // 찾은 문자열 주소 다음 위치로 검색 위치 이동
        // 찾은 단어 시작 위치 주소 + 찾은 단어 길이를 더하면 찾는 단어 바로 다음 문자부터 strstr 함수로 검색
        current_pos = found + len;
    }

    printf("%d\n", Count);
}