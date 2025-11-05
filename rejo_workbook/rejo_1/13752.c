#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    while (N--)
    {
        int k;
        scanf("%d", &k);

        while (k--)
            putchar('=');
        putchar('\n');
    }
    return 0;
}