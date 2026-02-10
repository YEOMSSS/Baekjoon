// 틀린 코드. 큰 수 연산은 역시 파이썬...

#include <stdio.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int M, N;
        scanf("%d %d", &M, &N);

        int arr[N][M];

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                scanf("%d", &arr[i][j]);
            }
        }

        __int128_t biggest = 0;

        int result = 0;
        for (int j = 0; j < M; j++)
        {
            __int128_t mult = 1;
            for (int i = 0; i < N; i++)
            {
                mult *= arr[i][j];
            }

            if (j == 0)
            {
                biggest = mult;
                continue;
            }

            if (biggest <= mult)
            {
                biggest = mult;
                result = j;
            }
        }
        printf("%d\n", result + 1);
    }
    return 0;
}