// 입력받아서 10개씩 끊어 출력하기

/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *string = malloc(101);
    fgets(string, 101, stdin);
    string[strcspn(string, "\n")] = '\0';

    int cnt = 0;
    for (size_t i = 0; i < strlen(string); i++)
    {
        putchar(string[i]);
        cnt++;
        if (cnt == 10)
        {
            putchar('\n');
            cnt = 0;
        }
    }
    free(string);
    return 0;
}
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h> // strcpn

int main(void)
{
    char *string = malloc(101);
    fgets(string, 101, stdin);
    string[strcspn(string, "\n")] = '\0';

    // string[0]을 가리키는 포인터
    // p는 string[0]의 주소, *p는 그 값. 즉 string[0] 자체
    char *p = string;

    while (*p != '\0')
    {
        // p++는 포인터 연산으로, 다음 칸으로 가는 것이다.
        for (int i = 0; i < 10 && *p != '\0'; i++, p++)
        {
            putchar(*p);
        }
        putchar('\n');
    }
    free(string);

    return 0;
}