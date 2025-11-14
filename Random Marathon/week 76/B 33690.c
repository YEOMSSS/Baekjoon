// 포린드롬은 펠린드롬이면서 끝에 한자리를 떼도 펠린드롬인 수.
// 12321같은 걸 보면 1232는 안됨.
// 1111 11111 다 똑같을때밖에 없는거같은데??

#include <stdio.h>

int main(void)
{
    char buf[11], *p;
    int l;

    scanf("%s", buf);
    // 문자열 길이 계산하기
    for (l = 0; buf[l]; l++)
        ;

    // 숫자보다 큰 아스키코드 지정해두기
    buf[l] = '9' + 1;

    // 포인터 p = 포인터 buf로 두고, p는 한칸씩 앞으로 간다.
    // 둘이 달라질 때까지 앞으로 간다.
    for (p = buf; *p == *buf; p++)
        ;

    // 맨 앞 숫자보다 다음으로 오는 숫자가 큰지 확인한다. 크면 1을 더한다.
    // 11122는 11111이 포함되지만 11100은 11111이 포함되지 않는다.
    printf("%d", (l - 1) * 9 + (*buf - '0') + (*p >= *buf));
    return 0;
}

// #include <stdio.h>
// #include <math.h>

// int main(void)
// {
//     int N;
//     scanf("%d", &N);
//     int old = N;

//     int digit = 1;

//     while (N >= 10)
//     {
//         digit++;
//         N /= 10;
//     }

//     int result = (digit - 1) * 9 + 1 + N;

//     int check = 0;
//     while (digit--)
//         check += N * pow(10, digit);

//     if (old < check)
//         result--;

//     printf("%d\n", result);
//     return 0;
// }
