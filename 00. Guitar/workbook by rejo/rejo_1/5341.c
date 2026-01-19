#include <stdio.h>

int main(void)
{

    while (1)
    {
        int N;
        scanf("%d", &N);

        if (!N)
            return 0;

        int result = 0;
        for (int i = 1; i <= N; i++)
            result += i;

        printf("%d\n", result);
    }
    return 0;
}