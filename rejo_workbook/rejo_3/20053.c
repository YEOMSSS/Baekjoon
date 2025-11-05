#include <stdio.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int n;
        scanf("%d", &n);

        int min = 1000000, max = -1000000;
        while (n--)
        {
            int num;
            scanf("%d", &num);

            if (num < min)
                min = num;
            if (num > max)
                max = num;
        }
        printf("%d %d\n", min, max);
    }
    return 0;
}