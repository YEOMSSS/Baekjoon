#include <stdio.h>
#include <string.h>

int main()
{
    char bin[101]; // 최대 100자리 이진수
    char oct[35];  // 변환된 8진수 (최대 34자리)
    int len;

    scanf("%100s", bin);
    len = strlen(bin);

    int idx = 0;

    // 뒤에서 3자리씩 8진수로 변환
    // char형은 아스키코드 정수값을 가지는 것을 이용해 '0'을 더하고 빼면서 조절
    for (int i = len - 1; i >= 0; i -= 3)
    {
        int val = 0;
        if (i >= 0)
            val += (bin[i] - '0');
        if (i - 1 >= 0)
            val += (bin[i - 1] - '0') * 2;
        if (i - 2 >= 0)
            val += (bin[i - 2] - '0') * 4;

        oct[idx] = val + '0';
        idx++;
    }
    // oct[idx] = '\0';

    // 뒤집어서 출력
    for (int i = idx - 1; i >= 0; i--)
    {
        putchar(oct[i]);
    }
    putchar('\n');

    return 0;
}
