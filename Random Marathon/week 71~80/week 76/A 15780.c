#include <stdio.h>

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);

    int codes = 0;
    while (K--)
    {
        int tab;
        scanf("%d", &tab);

        // codes += ceil((float)tab / 2);
        codes += (tab + 2 - 1) / 2;
    }

    if (codes < N)
        printf("NO");
    else
        printf("YES");

    return 0;
}