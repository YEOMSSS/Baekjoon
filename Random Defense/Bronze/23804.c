#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N * 5; j++)
            putchar('@');
        putchar('\n');
    }
    for (int i = 0; i < N * 3; i++)
    {
        for (int j = 0; j < N; j++)
            putchar('@');
        putchar('\n');
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N * 5; j++)
            putchar('@');
        putchar('\n');
    }
}