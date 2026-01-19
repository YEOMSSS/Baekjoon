#include <stdio.h>

#define MIN(a, b) ((a < b) ? a : b)

int main(void)
{
    int A, B, C, D;
    scanf("%d %d %d %d", &A, &B, &C, &D);

    // 노력하지 않고 살기 위해서는
    // 많은 노력이 필요하다.

    printf("%d", MIN(A + D, B + C));
}