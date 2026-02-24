# Authored by : marigold2003
# Date : 2026-01-28
# Link : https://www.acmicpc.net/problem/9372

import sys

input = sys.stdin.readline


# [Summary]

# 비행 스케줄이 주어졌을 때, 비행기를 가장 적은 종류로 타고 모든 국가를 여행햐야 한다.
# 이미 방문한 국가를 또 여행할 수 있다.


def main():

    # [Ideas]

    # 그래프 순회. bfs나 dfs중 아무거나 쓰면 된다.
    # 근데, N개의 정점을 순회하기 위한 간선의 수는 무조건 N-1개가 아니었던가?

    ##########

    T = int(input())

    for _ in range(T):
        # 국가(정점) 수, 종류(간선) 수
        N, M = map(int, input().split())
        for _ in range(M):
            input()
        print(N - 1)

    ##########

    return


# [Review]

# 순회를 구현할 필요가 없는 그래프 기초 문제.

if __name__ == "__main__":
    main()
