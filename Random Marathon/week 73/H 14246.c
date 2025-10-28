#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int arr[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }

    int K;
    scanf("%d", &K);

    int p1 = 0, p2 = 0, sum = 0;
    long result = 0;

    while (p1 < N)
    {
        if (p2 < N && sum <= K)
        {
            sum += arr[p2++];
        }
        else
        {
            if (sum > K)
            {
                result += (N - p2 + 1);
            }
            sum -= arr[p1++];
        }
    }
    printf("%ld", result);
}