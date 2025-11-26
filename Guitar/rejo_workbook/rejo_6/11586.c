#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    char mirror[N][N + 1];
    for (int i = 0; i < N; i++)
        scanf("%s", mirror[i]);

    int K;
    scanf("%d", &K);

    switch (K)
    {
    case 1:
        for (int i = 0; i < N; i++)
            printf("%s\n", mirror[i]);
        break;
    case 2:
        for (int i = 0; i < N; i++)
        {
            for (int j = N - 1; j >= 0; j--)
                putchar(mirror[i][j]);
            putchar('\n');
        }
        break;
    case 3:
        for (int i = N - 1; i >= 0; i--)
            printf("%s\n", mirror[i]);
        break;

    default:
        break;
    }
    return 0;
}