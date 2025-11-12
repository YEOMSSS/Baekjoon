#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    if (N % 2024 || N > 100000)
        puts("No");
    else
        puts("Yes");

    return 0;
}