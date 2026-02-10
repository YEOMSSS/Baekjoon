#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    if (N == 1 || N == 3)
        printf("NO");
    else
        printf("YES");

    return 0;
}