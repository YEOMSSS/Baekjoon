# Authored by : marigold2003
# Date : 2026-04-09
# Link : https://www.acmicpc.net/problem/34891


import sys

input = sys.stdin.readline


# [Summary] MT 준비

# 필요한 물건을 박스에 정리해 버스에 실으려 한다.
# 박스에 담을 물건들의 개수가 박스의 크기를 초과하지 않을 때만
# 박스에 안전하게 물건을 담을 수 있다.
# 필요한 박스의 최소 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 올림하면 되겠네.

    ##########

    N, M = map(int, input().split())
    print((N + M - 1) // M)

    ##########

    return


# [Review]

# 편하게 올림법칙으로 풀자.


if __name__ == "__main__":
    main()
