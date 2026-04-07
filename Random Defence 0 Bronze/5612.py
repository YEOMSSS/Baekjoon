# Authored by : marigold2003
# Date : 2026-03-12
# Link : https://www.acmicpc.net/problem/5612


import sys

input = sys.stdin.readline


# [Summary] 터널의 입구와 출구

# 터널의 입구와 출구에서 1분에 통과하는 차량의 수를 조사했다.
# 터널에 차량이 가장 많이 있었을 때 몇 대 있었는지 구하시오.
# 그러니까, 각 회차 조사가 끝난 시점 기준이다.

# 조사를 시작할 때 들어있는 차량의 수가 주어진다.


def main() -> None:

    # [Ideas]

    # 처음 시작 차량 수에서
    # 들어온만큼 더하고 나온만큼 뺀다.
    # 그 중 최댓값 구하기.

    ##########

    N = int(input())

    count = int(input())
    answer = count
    for _ in range(N):
        carin, carout = map(int, input().split())
        count += carin - carout
        if count < 0:
            print(0)
            return

        answer = max(answer, count)

    print(answer)

    ##########

    return


# [Review]

# 문제랑 입출력내용이랑 묘하게 다름.
# j분이 지난 시점이란 말이 있기 때문에 들어가고 나온 다음 터널을 확인해야함.


if __name__ == "__main__":
    main()
