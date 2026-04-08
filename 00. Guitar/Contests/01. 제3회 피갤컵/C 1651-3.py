# Authored by : marigold2003
# Date : 2026-02-15
# Link : https://www.acmicpc.net/contest/problem/1651/3


import sys

input = sys.stdin.readline


# [Summary] C번 - 폭탄의 악마

# 길이 N 정수열 A에 폭탄을 던진다!
# 폭탄에 맞으면 자신의 소인수 중 하나로 바뀌어 버린다.
# 소인수로 변할 확률은 균일하다.

# 폭탄은 [i:j+1]에 던져진다. 각 값은 전부 폭탄에 맞는다.
# 계획은 M번이다. 계획된 모든 폭발이 일어난 후 sum(A)의 기댓값을 구하시오.

# N, M은 최대 20만이고, 배열 A 내부 값은 각각 최대 50만인 정수.


def main() -> None:

    # [Ideas]

    # 기댓값이니까 소인수들의 합을 평균내면 될 듯.

    ##########

    from math import isqrt

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 폭탄이 한 칸에 몇번 터지는지를 세자.
    bomb_cnt = [0] * (N + 2)
    for _ in range(M):
        i, j = map(int, input().split())
        bomb_cnt[i - 1] += 1
        bomb_cnt[j] -= 1

    for k in range(1, N):
        bomb_cnt[k] += bomb_cnt[k - 1]

    # 소인수 구하는 함수
    def prime_factors(n):
        factors = set()
        x = n

        for p in range(2, isqrt(n) + 1):
            if x % p == 0:
                factors.add(p)
                while x % p == 0:
                    x //= p
        if x > 1:
            factors.add(x)
        return factors

    answer = 0.0
    for i in range(N):
        if bomb_cnt[i] == 0:
            answer += A[i]
        else:
            temp = prime_factors(A[i])
            answer += sum(temp) / len(temp)

    print(f"{answer:.9f}")

    ##########

    return


# [Review]

# 아니, 계획을 막을 수 있으면 막으라니까?
# 예측하기도 귀찮아? 이런 씨


if __name__ == "__main__":
    main()
