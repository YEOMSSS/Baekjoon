#include <stdio.h>

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    int arr[N][M];
    for (int r = 0; r < N; r++)
    {
        for (int c = 0; c < M; c++)
            scanf("%d", &arr[r][c]);
    }

    int T;
    scanf("%d", &T);

    while (T--)
    {
        int i, j, x, y;
        scanf("%d %d %d %d", &i, &j, &x, &y);

        int result = 0;
        for (int r = i - 1; r < x; r++)
        {
            for (int c = j - 1; c < y; c++)
                result += arr[r][c];
        }
        printf("%d\n", result);
    }

    return 0;
}