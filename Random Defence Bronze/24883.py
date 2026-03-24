# Authored by : marigold2003
# Date : 2026-03-24
# Link : https://www.acmicpc.net/problem/24883


import sys

input = sys.stdin.readline


# [Summary] 자동완성

# 입력이 n 또는 N 인지 아닌지 판단하시오.


def main() -> None:

    # [Ideas]

    # ch 하나 달랑 입력된다.
    # ==으로 비교해서 쉽게 풀자.

    ##########

    ch = input().rstrip()

    if ch in ["n", "N"]:
        print("Naver D2")
        return

    print("Naver Whale")

    ##########

    return


# [Review]

# 브5가 또 좀 쌓였네?


if __name__ == "__main__":
    main()
