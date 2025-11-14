#include <stdio.h>
#include <math.h>

int main(void)
{
    int N, K, C, R;
    scanf("%d %d %d %d", &N, &K, &C, &R);

    int base[K], s[K], p[K];
    for (int i = 0; i < K; i++)
    {
        scanf("%d", &base[i]);
    }
    for (int i = 0; i < K; i++)
    {
        scanf("%d", &s[i]);
    }
    for (int i = 0; i < K; i++)
    {
        scanf("%d", &p[i]);
    }

    int skill[K];
    for (int i = 0; i < K; i++)
    {
        skill[i] = 0;
    }

    int combo = 0, pirodo = 0;
    long long Stardust = 0;
    while (N--)
    {
        int l;
        scanf("%d", &l);

        if (l == 0)
        {
            combo = 0;
            pirodo -= R;
            if (pirodo < 0)
                pirodo = 0;
            continue;
        }

        l--;

        long long A = (long long)combo * C;
        long long B = (long long)skill[l] * s[l];

        long long inc = ((long long)base[l] * (100 + A) * (100 + B)) / 10000;
        Stardust += inc;

        skill[l]++;
        combo++;

        pirodo += p[l];
        if (pirodo > 100)
        {
            printf("-1");
            return 0;
        }
    }

    printf("%lld", Stardust);
    return 0;
}
