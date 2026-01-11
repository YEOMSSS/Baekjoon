#include <stdio.h>
#include <string.h>

int main(void)
{

    char string[1001];
    scanf("%s", string);

    int len = strlen(string);
    for (int i = 0; i < len; i++)
        // 아 스키스키 코드. char는 정수다
        printf("%c", string[i] > 'C' ? string[i] - 3 : string[i] + 23);

    return 0;
}