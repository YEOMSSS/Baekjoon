# Authored by : marigold2003
# Date : 2026-03-08
# Link : https://www.acmicpc.net/problem/15727


import sys

input = sys.stdin.readline


# [Summary] 조별과제를 하려는데 조장이 사라졌다

# 0에서 시작해서 L(1M)까지 이동해야 한다.
# 1회 이동에 1~5를 갈 수 있다.
# 가장 적은 이동횟수를 구하시오.


def main() -> None:

    # [Ideas]

    # 5로 나누고 올림하면 되는거 아닌가

    ##########

    a = int(input())
    b = 5
    print((a + b - 1) // b)

    ##########

    return


# [Review]

# 올림법칙으로 빠르게


if __name__ == "__main__":
    main()
