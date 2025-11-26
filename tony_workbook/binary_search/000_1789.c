// 이 문제의 포인트는 가능한 최대 1~n의 합을 찾는 것이다.
// 남는건 마지막에 그냥 다 더해버리면 됨.
// 200의 경우
// 1 ... 18 19 + 10
// 1 ... 18 29

#include <stdio.h>
#include <math.h>

typedef long long ll;

ll S;

// 1~n의 합이 S보다 크면 1 반환
int func(ll n)
{
    return n * (n + 1) / 2 > S;
}

int main()
{
    scanf("%lld", &S);
    // n*(n+1)/2 <= 4294967295, 대충 n*n <= 4294967295*2
    // right는 sqrt(4294967295*2)으로 설정
    ll left = 1, right = sqrt(4294967295 * 2) + 10;

    while (left <= right)
    {
        ll mid = (left + right) / 2;

        if (func(mid))
            right = mid - 1;
        else
            left = mid + 1;
    }

    // 이경우는 정확히 찾는게아니라 더 작은거기만 하면 되서 마무리된 right값을 가져오면 된다.
    printf("%lld\n", right);
    return 0;
}
