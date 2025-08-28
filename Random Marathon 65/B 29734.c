
// 8시간 공부하고 자고 8시간 공부하고 ... 남은 시간 공부하고 바로 제출
// 가고 8시간 오고 자고 가고 8시간 오고 자고 가고 8시간 오고 자고 ... 가고 남은시간 제출

#include <stdio.h>

int main(void) {

    long long N, M;
    int T, S;
    scanf("%lld %lld %d %d", &N, &M, &T, &S);

    long long Zip, Dok;
    // N을 8로 나눈 몫의 올림 - 1에 수면시간을 곱해 N에 더해준다.
    Zip = N + (S * (((N + 8 - 1) / 8) - 1));
    // N을 8로 나눈 몫의 올림 - 1에 왕복시간+수면시간을 곱해 N에 더해주고, 가는시간을 한번 더 더해준다.
    Dok = M + ((S + (2 * T)) * (((M + 8 - 1) / 8) - 1)) + T;

    (Zip < Dok) ? printf("Zip\n%lld", Zip) : printf("Dok\n%lld", Dok);
    // printf("%d", (Zip < Dok) ? Zip : Dok);

    return 0;

}

// 입력되는 범위를 잘 보자.
//  long long %lld 를 사용해야 할 일이 있을지도 몰라.