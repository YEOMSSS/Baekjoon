
#include <stdio.h>

int main(void)
{
    int H, I, A, R, C;
    scanf("%d %d %d %d %d", &H, &I, &A, &R, &C);

    int result;
    result = (H * I) - (A * R * C);

    printf("%d", result);
    return 0;
}