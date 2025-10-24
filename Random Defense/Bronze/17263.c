#include <stdio.h>

#define MAX(a, b) ((a > b) ? a : b)

int main(void)
{
    int N;
    scanf("%d", &N);

    int result = 0;
    while (N--)
    {
        int num;
        scanf("%d", &num);
        result = MAX(num, result);
    }

    printf("%d", result);

    return 0;
}