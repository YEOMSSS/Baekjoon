# Authored by : marigold2003
# Date : 2026-03-31
# Link : https://www.acmicpc.net/problem/34529


import sys

input = sys.stdin.readline


# [Summary] Acquiring SW-IT Corn

# 100g당 X원으로 Ug 산다.
# 50g당 Y원으로 Vg 산다.
# 20g당 Z원으로 Wg 산다.
# 구매에 필요한 총금액을 구하시오.


def main() -> None:

    # [Ideas]

    # 주어진 대로 구매하면 된다.

    ##########

    X, Y, Z = map(int, input().split())
    U, V, W = map(int, input().split())

    result = 0
    result += (U // 100) * X
    result += (V // 50) * Y
    result += (W // 20) * Z

    print(result)

    ##########

    return


# [Review]

# 스위트콘 먹을 날씨가 되어가는구나.


if __name__ == "__main__":
    main()
