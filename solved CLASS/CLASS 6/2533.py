# Authored by : marigold2003
# Date : 2026-03-31
# Link : https://www.acmicpc.net/problem/2533


import sys

input = sys.stdin.readline


# [Summary] 사회망 서비스(SNS)

# 사람들을 정점으로 하는 트리가 주어진다.
# 각 사람은 자신의 모든 이웃이 얼리어답터일 때 아이디어를 받아들인다.
# 모든 사람이 아이디어를 받아들이는 데 필요한 최소 얼리어답터의 수를 구하시오.

sys.setrecursionlimit(10**6)


def main() -> None:

    # [Ideas]

    # 리프노드들에서부터 시작해서 거꾸로 루트를 향해 들어가자.
    # 각 노드에는 자신이 얼리어답터일때와 아닐때에 대해 dp로 얼리어답터 수의 최솟값을 저장하자.
    # 자신이 얼리어답터일 때는 그냥 각 자식노드의 min을 다 합치면 되고,
    # 얼리어답터가 아니려면 자식노드가 얼리어답터일 때를 전부 합치면 된다.

    # 그럼 자신의 모든 자식이 처리된 후 부모가 처리되어야 하니까 bfs를 사용해야 할 듯.
    # 아니면... 그냥 정방향 저장하고 dfsR을 사용하거나. 이게 더 편할지도 모르겠는데?

    # 젠장맞을, 애초에 트리형태기만 한거지 무방향이잖아??

    ##########

    N = int(input())

    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # n이 얼리어답터일때, 얼리어답터가 아닐 때
    dp = [[0, 0] for _ in range(N + 1)]

    def dfsR(curr, parent):

        # 자신이 얼리어답터면 1을 가진 채로 시작
        dp[curr][0] = 1
        dp[curr][1] = 0

        for nei in graph[curr]:
            # 부모 쪽으로 다시 이동할 수 없게 제한
            if nei == parent:
                continue

            # dp 채우기
            dfsR(nei, curr)
            # curr가 얼리어답터면 nei가 뭐든 상관없음
            dp[curr][0] += min(dp[nei])
            # curr가 얼리어답터가 아니면 nei가 얼리어답터여야만 함
            dp[curr][1] += dp[nei][0]

        return dp[curr]

    # 처음엔 부모가 없다고 생각하고 돌리기
    dfsR(1, 0)

    print(min(dp[1]))

    ##########

    return


# [Review]

# dfsR로 쭉 들어가서 리프부터 순서대로 dp에 털면서 나오기.


if __name__ == "__main__":
    main()
