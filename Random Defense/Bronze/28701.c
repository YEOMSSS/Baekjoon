#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);
    int r1 = 0, r2 = 0, r3 = 0;

    for (int i = 1; i < N + 1; i++)
    {
        r1 += i;
        r3 += i * i * i;
    }

    r2 = r1 * r1;

    printf("%d\n%d\n%d\n", r1, r2, r3);

    return 0;
}