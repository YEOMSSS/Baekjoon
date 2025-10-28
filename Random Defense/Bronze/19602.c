#include <stdio.h>

int main(void)
{
    int S, M, L;
    scanf("%d%d%d", &S, &M, &L);

    int result = S * 1 + M * 2 + L * 3;

    if (result >= 10)
    {
        printf("happy");
    }
    else
    {
        printf("sad");
    }
    return 0;
}