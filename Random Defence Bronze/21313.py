# Authored by : marigold2003
# Date : 2026-03-09
# Link : https://www.acmicpc.net/problem/21313


import sys

input = sys.stdin.readline


# [Summary] 문어

# 문어의 팔은 8개, 1~8번으로 매겨져 있다.
# N마리의 문어 중 하나를 골라 1번 문어라 하고, 시계방향으로 N번까지 붙인다.
# 문어끼리 손을 잡는데, 서로 같은 번호의 손을 잡아야 한다.
# 손을 잡는 순서 중 사전순으로 제일 앞서는 수열을 출력하시오.


def main() -> None:

    # [Ideas]

    # 1 2 1 2...가 짝수일땐 제일 빠르고.
    # 홀수면?

    # 1 2 1 2 3? 3번을 써야 하는건가.

    ##########

    N = int(input())
    answer = [1, 2] * (N // 2)
    if N % 2:
        answer.append(3)

    print(*answer)

    ##########

    return


# [Review]

# 문어 다리는 8개.


if __name__ == "__main__":
    main()
