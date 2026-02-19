# Authored by : marigold2003
# Date : 2026-02-18
# Link : https://www.acmicpc.net/problem/10451


import sys

input = sys.stdin.readline


# [Summary] 순열 사이클

# arr이 input된다.
# 이 arr은 index -> value로 가는 방향 graph의 의미를 가진다.
# cycle의 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # graph 만들고, dfs든 bfs든 탐색하면 끝.
    # 아, 입력 자체가 graph가 되겠구나?
    # 가지도 무조건 하나니까 queue도 필요없다.

    # 이제 이런 문제는 익숙하게 풀 수 있다.
    # 최적화나 해보자. 빨리 풀기 해보던가.

    ##########

    T = int(input())

    # cycle을 찾을때까지 돌며 지나간 칸을 visited에 새긴다.
    # 딱히 return할 value도 없다. 그냥 visited만 해주면 됨.
    def bfs(start, graph, visited):

        visited[start] = True
        curr = graph[start]

        while curr != start:
            visited[curr] = True
            curr = graph[curr]

        return

    ##########

    for _ in range(T):

        N = int(input())

        graph = [0] + list(map(int, input().split()))
        visited = [False] * (N + 1)

        count = 0
        for i in range(1, N + 1):
            if visited[i]:
                continue
            bfs(i, graph, visited)
            count += 1

        print(count)

    ##########

    return


# [Review]

# 그래프 이론 확인.
# 그래프라고 하기도 묘~함. 맞긴하지


if __name__ == "__main__":
    main()
