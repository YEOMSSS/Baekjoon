# Authored by : marigold2003
# Date : 2026-02-03
# Link : https://www.acmicpc.net/problem/11006

import sys

input = sys.stdin.readline


# [Summary]

# 닭장에 닭이 많다. 다리를 세 봤다. 개수가 안 맞는다.
# 다리가 잘린 닭은 몇 마리일까?


def main() -> None:

    # [Ideas]

    # 닭의 수*2 - 다리 수 하면 부족한 다리 개수.
    # 그게 곧 다리가 하나인 닭의 수다.

    # 2*닭수 - 다리수 = 다리없
    # 닭수 - 다리없 = 다리있
    # 다리있 = 닭수 - 2닭수 + 다리수
    # 다리있 = 다리수 - 닭수 오...

    ##########

    T = int(input())
    for _ in range(T):
        # 다리 개수 총합, 닭의 수
        N, M = map(int, input().split())
        print(2 * M - N, N - M)

    ##########

    return


# [Review]

# 닭 불쌍해. 닭다리는 맛있어...

if __name__ == "__main__":
    main()
