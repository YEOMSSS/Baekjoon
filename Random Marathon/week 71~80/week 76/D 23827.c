// 1*2 + 1*3 + 1*4 + 2*3 + 2*4 + 3*4
// = 1(2+3+4) + 2(3*4) + 3(4) 인거잖아?

#include <stdio.h>

const int MOD = 1000000007;

int main(void)
{
    int N;
    scanf("%d", &N);

    int arr[N];
    long long sum[N];
    scanf("%d", arr);
    sum[0] = arr[0];

    for (int i = 1; i < N; i++)
    {
        scanf("%d", &arr[i]);
        sum[i] = (sum[i - 1] + arr[i]) % MOD;
    }

    long long result = 0;
    for (int i = 0; i < N - 1; i++)
    {
        result += (arr[i] * (sum[N - 1] - sum[i]) % MOD);
        result %= MOD;
    }

    printf("%lld", result % MOD);
    return 0;
}
