#include <stdio.h>

int main(void)
{
    int arr[11];
    for (int i = 0; i < 11; i++)
        scanf("%d", &arr[i]);

    int N;
    scanf("%d", &N);

    int result = 0;

    while (N--)
    {
        int B, S;
        float L;

        scanf("%d %f %d", &B, &L, &S);

        if (S >= 17 && L >= 2.0)
            result += arr[B];
    }
    printf("%d", result);
    return 0;
}
