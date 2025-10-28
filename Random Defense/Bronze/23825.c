#include <stdio.h>

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    int small = N < M ? N : M;
    printf("%d", small / 2);

    return 0;
}