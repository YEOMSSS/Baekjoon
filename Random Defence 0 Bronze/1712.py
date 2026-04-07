# Authored by : marigold2003
# Date : 2026-04-04
# Link : https://www.acmicpc.net/problem/1712


import sys

input = sys.stdin.readline


# [Summary] 손익분기점

# 고정 비용 A, 대당 생산 비용 B가 주어진다.
# 가격 C가 있을 때, 손익분기점은 몇 대인지 구하시오.


def main() -> None:

    # [Ideas]

    # 가격이 생산비용보다 비싸면 손익분기점은 언젠가 온다.
    # 팔 때마다 가격 - 생산비용만큼의 이득이 생기니, 그게 고정비용을 넘기면 된다.
    # 가격 - 생산비용이 음수면 팔 때마다 손해다. 손익분기점이 안 온다.
    # 0이어도 이익이 오르지 않아 손익분기점이 안 온다. 고정비용이 1 이상이므로...

    ##########

    A, B, C = map(int, input().split())

    profit = C - B
    if profit <= 0:
        print(-1)
        return

    # 딱 남아도 맞아떨어져도 하나 더 팔아야 한다.
    result = A // profit
    print(result + 1)

    ##########

    return


# [Review]

# 실수하지 않으면 되는 수학문제.


if __name__ == "__main__":
    main()
