# Authored by : marigold2003
# Date : 2026-03-18
# Link : https://www.acmicpc.net/problem/16394


import sys

input = sys.stdin.readline


# [Summary] 홍익대학교

# 개교년은 1946년이다.
# 입력된 해에 개교 몇 주년인지 구하시오.


def main() -> None:

    # [Ideas]

    # 입력에서 1946을 빼주면 된다.

    ##########

    N = int(input())
    print(N - 1946)

    ##########

    return


# [Review]

# 간단한 워밍업.


if __name__ == "__main__":
    main()
