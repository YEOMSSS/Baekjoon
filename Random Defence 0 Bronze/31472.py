# Authored by : marigold2003
# Date : 2026-03-14
# Link : https://www.acmicpc.net/problem/31472


import sys

input = sys.stdin.readline


# [Summary] 갈래의 색종이 자르기

# 가로로 이등분하고 난 후의 색종이 절반의 넓이 W가 주어진다.
# 처음 색종이의 둘레를 구하시오.

# 처음 색종이는 정사각형이다.


def main() -> None:

    # [Ideas]

    # W = a*a//2
    # 구해야 하는 건 4a
    # 2W **0.5 = a

    ##########

    W = int(input())
    a = (W * 2) ** 0.5
    print(int(4 * a))

    ##########

    return


# [Review]

# 문제를 잘 읽자!!!!


if __name__ == "__main__":
    main()
