#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    N = 1000 - N;

    int result = 0;

    result += N / 500;
    N %= 500;
    result += N / 100;
    N %= 100;
    result += N / 50;
    N %= 50;
    result += N / 10;
    N %= 10;
    result += N / 5;
    N %= 5;
    result += N / 1;

    printf("%d", result);

    return 0;
}