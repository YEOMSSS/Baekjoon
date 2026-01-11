#include <stdio.h>

int main(void)
{
    int A, B;
    scanf("%d %d", &A, &B);

    // 비트 XOR연산
    int C = A ^ B;

    printf("%d", C);
    return 0;
}