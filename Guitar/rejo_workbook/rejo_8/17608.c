#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int arr[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &arr[i]);

    int temp = 0, result = 0;
    for (int i = N - 1; i >= 0; i--)
    {
        if (arr[i] > temp)
        {
            result++;
            temp = arr[i];
        }
    }

    printf("%d", result);
    return 0;
}