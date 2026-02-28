# Authored by : marigold2003
# Date : 2026-02-28
# Link : https://www.acmicpc.net/problem/1404


import sys

input = sys.stdin.readline


# [Summary] 토너먼트 승자

# 백준햄이 스타대회를 열었다.
# 8명이 참가하며, 12번, 34번, 56번, 78번이 대결한다.
# 1234승자끼리, 5678승자끼리 대결하고 결승을 한 게임 한다.

# 8명의 참가자가 나머지 7명과 싸웟을 때 이길 수 있는 승률이 각각 주어질 때,
# 각 참가자가 우승할 수 있는 확률을 구하시오.


def main() -> None:

    # [Ideas]

    # 시뮬레이션을 돌리면 되겠다.
    # 다 해보지 뭐.

    # 1이 이기는 경우, 2가 이기는 경우...
    # 각자가 이기기 위해서는 계속 밟고 올라가야 한다.
    # 각자의 준결승 확률과 결승 확률을 구해야 할 듯...

    ##########

    it = map(int, input().split())
    rate = [[0] * 8 for _ in range(8)]

    for i in range(8):
        for j in range(i + 1, 8):
            rate[i][j] = next(it)
            rate[j][i] = 100 - rate[i][j]

    semi_final = [0] * 8
    for i in range(0, 8, 2):
        semi_final[i] = rate[i][i + 1]
        semi_final[i + 1] = rate[i + 1][i]

    final = [0] * 8
    for i in range(0, 8, 4):
        for d in range(2):
            final[i + d] = (
                semi_final[i + d]
                * (
                    semi_final[i + 2] * rate[i + d][i + 2]
                    + semi_final[i + 3] * rate[i + d][i + 3]
                )
                / 10000
            )
            final[i + d + 2] = (
                semi_final[i + d + 2]
                * (
                    semi_final[i + 0] * rate[i + d + 2][i + 0]
                    + semi_final[i + 1] * rate[i + d + 2][i + 1]
                )
                / 10000
            )

    answer = [0] * 8

    for i in [0, 1, 2, 3]:
        temp_sum = 0
        for d in [4, 5, 6, 7]:
            temp_sum += final[d] * rate[i][d]
        temp_sum *= final[i] / 10000
        answer[i] = temp_sum / 100

    for i in [4, 5, 6, 7]:
        temp_sum = 0
        for d in [0, 1, 2, 3]:
            temp_sum += final[d] * rate[i][d]
        temp_sum *= final[i] / 10000
        answer[i] = temp_sum / 100

    print(*answer)

    ##########

    return


# [Review]

# 마치 그림을 그리는 듯한 구현
# 옛날에 수학문제 풀때 카드 탑 그리던게 생각난다.


if __name__ == "__main__":
    main()
