
#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int arr_A[N]; // malloc을 사용 안해도 되는가?
    for (int i = 0; i < N; i++)
        scanf("%d", &arr_A[i]);

    int arr_B[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &arr_B[i]);

    int cnt = 0;
    for (int i = 0; i < N; i++)
    {
        if (arr_A[i] <= arr_B[i])
            cnt += 1;
    }

    printf("%d", cnt);
    return 0;
}