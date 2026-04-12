# Authored by : marigold2003
# Date : 2026-04-12
# Link : https://www.acmicpc.net/problem/3733


import sys

input = sys.stdin.readline


# [Summary] Shares

# N명의 사람과 1명의 판사가 S개의 주식을 똑같이 나눠가진다.
# 각 사람이 소유하게 되는 주식의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # EOF만 잘 털어주고, 정수나눗셈 조져주자.

    ##########

    while True:
        data = input()
        if not data:
            return

        N, S = map(int, data.split())
        print(S // (N + 1))

    ##########

    return


# [Review]

# EOF도 오랜만에하니까 헷갈리네.
# 영어문제 싫어. 영어도 잘해야하는데.


if __name__ == "__main__":
    main()
