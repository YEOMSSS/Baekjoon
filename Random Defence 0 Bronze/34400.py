# Authored by : marigold2003
# Date : 2026-02-13
# Link : https://www.acmicpc.net/problem/34400


import sys

input = sys.stdin.readline


# [Summary] 민규의 서카디안 리듬

# 25를 주기로 한다.
# 0~16은 online, 17~24는 offline


def main() -> None:

    # [Ideas]

    # 입력을 25로 나눈 나머지로 계산하면 된다.
    # 30분이 더해지기 때문에 편하다.

    ##########

    T = int(input())
    for _ in range(T):
        n = int(input())

        if 0 <= n % 25 < 17:
            print("ONLINE")
        else:
            print("OFFLINE")

    ##########

    return


# [Review]

# 25시 사우나는 실존한다


if __name__ == "__main__":
    main()
