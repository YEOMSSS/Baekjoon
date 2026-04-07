# Authored by : marigold2003
# Date : 2026-03-15
# Link : https://www.acmicpc.net/problem/5576


import sys

input = sys.stdin.readline


# [Summary] 콘테스트

# W대학 10명, K대학 10명이 콘테스트에 참여했다.
# 10명 중 상위 3인의 점수를 합산해 대학의 득점으로 한다.
# 각 대학의 점수를 구하시오.


def main() -> None:

    # [Ideas]

    # 정렬하지 뭐

    ##########

    W = list(int(input()) for _ in range(10))
    K = list(int(input()) for _ in range(10))

    W.sort(reverse=True)
    K.sort(reverse=True)

    print(sum(W[:3]), sum(K[:3]))

    ##########

    return


# [Review]

# 쉽고 빠르게


if __name__ == "__main__":
    main()
