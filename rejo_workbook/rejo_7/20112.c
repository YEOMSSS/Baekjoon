#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    char arr[N][N];

    for (int r = 0; r < N; r++)
        scanf("%s", arr[r]);

    for (int r = 0; r < N; r++)
    {
        for (int c = 0; c < N; c++)
        {
            if (arr[r][c] != arr[c][r])
            {
                printf("NO");
                return 0;
            }
        }
    }

    printf("YES");
    return 0;
}