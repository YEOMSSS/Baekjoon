# Authored by : marigold2003
# Date : 2026-02-15
# Link : https://www.acmicpc.net/contest/problem/1651/2


import sys

input = sys.stdin.readline


# [Summary] B번 - 지금부터 완장 찬양을 시작하겠습니다

# N일간의 방문 기록이 주어진다.
# 연속으로 방문하지 않은 기간이 K일 이상인 경우가 있는지 확인하시오.


def main() -> None:

    # [Ideas]

    # 최대 1M일까지 주어진다.
    # pypy브루트포스 가능하겠지?

    ##########

    N, K = map(int, input().split())
    arr = tuple(map(int, input().rstrip()))

    count = 0
    for a in arr:
        if a:
            count = 0
        else:
            count += 1
            if count == K:
                print(0)
                return

    print(1)

    ##########

    return


# [Review]

# 일단 해봅시다.


if __name__ == "__main__":
    main()
