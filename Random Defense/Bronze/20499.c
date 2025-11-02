#include <stdio.h>

int main(void)
{
    int K, D, A;
    scanf("%d/%d/%d", &K, &D, &A);
    if (K + A < D || !D)
        printf("hasu");
    else
        printf("gosu");

    return 0;
}