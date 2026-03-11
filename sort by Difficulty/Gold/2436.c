/*
풀이 : 최대 공약수와 최소공배수
구하고자 하는 두 수의 최대공약수와, 최소공배수가 있으면, 그 두 수를 유추할 수가 있다.
최소공배수는 어떤 두수 의 값을 곱한 것에 최대공약수를 나눈 것이기 때문이다.

예제에서 의 6 108도 108 = (x*y)/6이 된다.
여기서 최대공약수를 좌변으로 옮기면 108*6 = x*y가 된다.
즉 x*y의 값이 최대공약수 * 최소공배수의 조건을 만족하는 경우에서,
x의 값을 점차 늘리고 (y값은 반비례하게 감소) x와 y의 최대공약수가 처음에 입력받은 것과 같은지를 비교 후
x+y값이 더 작을 때마다 x,y값을 교체해 주며 값이 같은 경우, x,y의 차가 더 작은 것을 구해서 교체해 준다.
*/

// 이건 뭐 수학이잖아...

#include <stdio.h>

// 유클리드 호제법으로 최대공약수 구하기
long long euclid(long long a, long long b) {
    while (b) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main(void) {

    // 최소공배수, 최대공약수
    long long gcd, lcm;
    scanf("%lld %lld", &gcd, &lcm);

    long long A, B, result_A, result_B;
    long long sum = 200000000; // A + B의 범위에서 가능한 가장 큰 값

    // B = gcd * (lcm / A), A * B = gcd * lcm (A * B / gcd = lcm 에서 나옴)
    for (long long i = 1;   ; i++) {

        // gcd에 i씩 곱해가며 A를 키운다.
        A = gcd * i;

        // A가 lcm보다 커지면 반복 종료
        if (A > lcm) {
            break;
        }

        // lcm / A가 나누어떨어지지 않으면 continue
        if (lcm % A) {
            continue;
        }

        // B = gcd * (lcm / A)를 이용 (lcm / A가 나누어떨어질 때만)
        B = gcd * (lcm / A);

        // A와 B의 gcd가 입력값과 다르면 continue
        if (euclid(A, B) != gcd) {
            continue;
        }

        // 이전 합보다 현재 합이 작으면 정답 갱신
        if (A + B < sum) {
            sum = A + B;
            result_A = A;
            result_B = B;
        }
    }

    printf("%lld %lld", result_A, result_B);

    return 0;
}