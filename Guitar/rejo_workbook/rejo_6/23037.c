#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int sum = 0, check = 10000;

    for (int i = 0; i < 5; i++)
    {
        int temp = N / check;
        temp = temp * temp * temp * temp * temp;
        sum += temp;
        N %= check;
        check /= 10;
    }

    printf("%d", sum);

    return 0;
}
