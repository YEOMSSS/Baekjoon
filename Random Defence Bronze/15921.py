# Authored by : marigold2003
# Date : 2026-03-20
# Link : https://www.acmicpc.net/problem/15921


import sys

input = sys.stdin.readline


# [Summary] 수찬은 마린보이야!!

# 입력된 N개의 기록의 평균을 구하고 그 평균을 다시 N으로 나누어라.


def main() -> None:

    # [Ideas]

    # 요약한 대로 하자.

    ##########

    N = int(input())
    if not N:
        print("divide by zero")
        return

    total = sum(map(int, input().split()))
    if not total:
        print("divide by zero")
        return

    print(f"{total / total:.2f}")

    ##########

    return


# [Review]

# 아, 설마 말장난이야?


if __name__ == "__main__":
    main()
