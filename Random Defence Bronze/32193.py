# Authored by : marigold2003
# Date : 2026-02-26
# Link : https://www.acmicpc.net/problem/32193


import sys

input = sys.stdin.readline


# [Summary] 승강장의 깊이

# 0번역에서 지표면높이와 승강장높이는 모두 0m이다.
# i-1번역에서 i번역으로 이동하면 지표면이 Ai만큼 높아지고 승강장은 Bi만큼 높아진다.
# i번역의 깊이는 (i역지표면높이 - i역승강장높이) 이다. 구하시오.


def main() -> None:

    # [Ideas]

    # 그냥 구현이다.
    # 있는 그대로 돌리면 됨.

    # 입력받는 족족 연산해서 바로바로 출력하자.

    ##########

    N = int(input())

    curr = 0
    for _ in range(N):
        a, b = map(int, input().split())
        curr += a - b
        print(curr)

    ##########

    return


# [Review]

# 이런 힐링도 필요하지.


if __name__ == "__main__":
    main()
