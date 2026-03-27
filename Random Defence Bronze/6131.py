# Authored by : marigold2003
# Date : 2026-03-27
# Link : https://www.acmicpc.net/problem/6131


import sys

input = sys.stdin.readline


# [Summary] 완전 제곱수

# A의 제곱은 B의 제곱보다 N만큼 크다. (1 <= B <= A <= 500)
# N이 주어질 때, 조건을 만족하는 A와 B의 쌍의 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 입력이 크지 않으니 브루트포스.

    ##########

    N = int(input())

    count = 0
    for a in range(1, 501):
        for b in range(1, a + 1):
            if a**2 - b**2 == N:
                count += 1

    print(count)

    ##########

    return


# [Review]

# 이중포문 브루트포스.


if __name__ == "__main__":
    main()
