// print(sum(range(0, int(input())))) 되겠냐?

// 이 썩을 놈의 long long

#include <stdio.h>

int main(void)
{
    long long A, B;
    scanf("%lld %lld", &A, &B);

    if (A == B)
    {
        printf("%lld", A);
        return 0;
    }

    if (A > B)
    {
        long long tmp = A;
        A = B;
        B = tmp;
    }

    // 시그마 공식 뭐더라?
    // 맨앞+맨뒤*개수/2 맞나.

    long long result;
    result = (A + B) * (B - A + 1) / 2;

    printf("%lld", result);
    return 0;
}
