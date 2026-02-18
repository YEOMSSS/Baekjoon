# Authored by : marigold2003
# Date : 2026-02-16
# Link : https://www.acmicpc.net/problem/17425


import sys

input = sys.stdin.readline


# [Summary] 약수의 합

# 자연수 N이 주어진다.
# 1~N까지 각각의 자연수들의 약수의 합의 합을 구하여라.


def main() -> None:

    # [Ideas]

    # 일단 누적합은 쓰고 싶고.
    # 약수의 합을 다 구해놓긴 해야겠다.

    # 체를 응용해서 배열에 넣어볼까?
    # 배수마다 더해주는 방식으로 가야겠다.

    # i에 1~1M을 넣고
    # i, i+i, i+2i, ...에 i씩 더해주자.
    # i로 나눠지는 칸은 i를 약수로 가지는 거니까.

    ##########

    MAX = 1_000_000
    sieve = [0] * (MAX + 1)

    # i의 배수인 모든 칸에 i를 더해준다.
    for i in range(1, MAX + 1):
        for j in range(i, MAX + 1, i):
            sieve[j] += i

    # 누적합. 이전칸을 현재칸에 더하는 것을 반복
    for i in range(1, MAX + 1):
        sieve[i] += sieve[i - 1]

    ##########

    T = int(input())

    for _ in range(T):
        N = int(input())
        print(sieve[N])

    ##########

    return


# [Review]

# 체에 대한 이해도가 높아지는 문제.
# 발상만 하면 구현은 쉽다.


if __name__ == "__main__":
    main()
