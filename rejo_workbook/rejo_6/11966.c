#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    for (int i = 0; i < 31; i++)
    {
        // 비트마스킹으로 제곱을 표현할 수 있다.
        if (N == 1 << i)
        {
            putchar('1');
            return 0;
        }
    }

    putchar('0');

    return 0;
}