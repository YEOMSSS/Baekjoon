#include <stdio.h>

int main(void)
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);

    int N;
    scanf("%d", &N);

    int result = 0;
    while (N--)
    {
        int score_sum = 0;
        for (int i = 0; i < 3; i++)
        {
            int a, b, c;
            scanf("%d %d %d", &a, &b, &c);

            score_sum += a * A + b * B + c * C;
        }

        if (result < score_sum)
            result = score_sum;
    }
    printf("%d", result);
    return 0;
}