// 오늘 컨디션 왜이리좋냐??

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int arr[10] = {
        0,
    };

    while (N)
    {
        arr[N % 10]++;
        N /= 10;
    }

    int result = (arr[6] + arr[9] + 2 - 1) / 2;
    for (int i = 0; i < 9; i++)
    {
        if (i == 6)
            continue;
        result = (result > arr[i]) ? result : arr[i];
    }

    printf("%d", result);
    return 0;
}