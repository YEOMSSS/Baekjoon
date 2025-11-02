#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    while (1)
    {
        int num;
        scanf("%d", &num);

        if (!num)
            break;

        if (num % N != 0)
        {
            printf("%d is NOT a multiple of %d.\n", num, N);
        }
        else // if (num % N == 0)
        {
            printf("%d is a multiple of %d.\n", num, N);
        }
    }

    return 0;
}