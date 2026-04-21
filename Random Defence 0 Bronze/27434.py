# Authored by : marigold2003
# Date : 2026-04-21
# Link : https://www.acmicpc.net/problem/27434


import sys

input = sys.stdin.readline


# [Summary] 팩토리얼 3

# N!을 출력하시오.


def main() -> None:

    # [Ideas]

    # python3 제출 불가라고? pypy3으로 내야겠군

    ##########

    # N = int(input())

    # answer = 1
    # for i in range(1, N + 1):
    #     answer *= i

    # print(answer)

    ##########

    from math import factorial

    print(factorial(int(input())))

    ##########

    return


# [Review]

# math.factorial을 써도 된다.


if __name__ == "__main__":
    main()
