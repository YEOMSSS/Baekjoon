# Authored by : marigold2003
# Date : 2026-01-30
# Link : https://www.acmicpc.net/problem/2312

import sys

input = sys.stdin.readline


# [Summary]

# N을 소인수분해한 결과를 출력하기.


def main():

    # [Ideas]

    # 테스트케이스가 여러개니까 소수표를 미리 만들어 두는 편이 좋긴 할듯.
    # 근데 수가 10만까지밖에 안들어오니까 6휠인수분해 정도만 써도 되겠다.
    # 가볍게 풀자 가볍게.

    ##########

    def wheel_6(n):

        prime_factors = dict()

        # 2와 3으로 먼저 처리
        for target in (2, 3):
            if n % target:
                continue

            count = 0
            while n % target == 0:
                count += 1
                n //= target
            prime_factors[target] = count

        # 제곱근까지만 검사
        k = 1

        # 소인수분해에서 이 n은 유동적으로 줄어들게 하는 편이 좋다.
        while (6 * k - 1) ** 2 <= n:
            for target in (6 * k - 1, 6 * k + 1):
                if n % target:
                    continue

                count = 0
                while n % target == 0:
                    count += 1
                    n //= target
                prime_factors[target] = count
            k += 1

        if n > 1:
            prime_factors[n] = 1

        return prime_factors.items()

    T = int(input())

    for _ in range(T):
        num = int(input())
        # 이미 오름차순 정렬된 상태이다.
        for a, b in wheel_6(num):
            print(a, b)

    ##########

    return


# [Review]

# 굳이 체를 뽑지 않아도 나름 빠르게 돌릴 수 있다.

if __name__ == "__main__":
    main()
