#include <stdio.h>
int main(void)
{
    int A, B;
    scanf("%d %d", &A, &B);

    printf("%d", A / 2 < B ? A / 2 : B);
    return 0;
}