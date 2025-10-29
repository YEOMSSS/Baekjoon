// SW수열은 앞의거랑의 차가 뒤에거랑의 차보다 큰 수열.
// 01, 12, 23... 의 차가 내림차순이라는거.

// 1 3 2
// 4 1 3 2
// 5 1 4 2 3
// 6 1 5 2 4 3 보인다 보여

// 1 3 2
// 1 4 2 3
// 1 5 2 4 3 이것도 되는구나??

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int arr[N];
    int check = 0;

    for (int i = 0; i < N; i += 2)
    {
        arr[i] = N - check++;
        arr[i + 1] = check; // c언어에는 인덱스에러가 없다.
    }

    for (int i = 0; i < N; i++)
        printf("%d ", arr[i]);

    return 0;
}