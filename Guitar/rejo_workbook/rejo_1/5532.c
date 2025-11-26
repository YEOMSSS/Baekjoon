#include <stdio.h>
#include <math.h>

int main(void)
{
    int L, A, B, C, D;
    scanf("%d %d %d %d %d", &L, &A, &B, &C, &D);

    int K, M;
    K = (A + C - 1) / C;
    M = (B + D - 1) / D;

    int work = K > M ? K : M;
    printf("%d", L - work);
}