# Authored by : marigold2003
# Date : 2026-11-26
# Link : https://www.acmicpc.net/problem/10797


import sys

input = sys.stdin.readline


# [Summary] 10부제

# 입력된 숫자와 같은 숫자가 몇 개 있는지 출력하라.


def main() -> None:

    # [Ideas]

    # 우리에게는 count가 있다.
    # 하나하나 다 읽어도 뭐... 5대라.

    ##########

    N = int(input())
    nums = list(map(int, input().split()))

    print(nums.count(N))

    ##########

    return


# [Review]

# 빠르게 풀고 할 일을 하러 가자.


if __name__ == "__main__":
    main()
