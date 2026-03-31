# Authored by : marigold2003
# Date : 2026-03-30
# Link : https://www.acmicpc.net/problem/1005


import sys

input = sys.stdin.readline


# [Summary] ACM Craft

# 단방향 graph가 있다. node N(<= 1K)개, edge K(<= 100K)개.
# W번 node에 도달하기 위해서는 그의 모든 조상을 거쳐야 한다.
# leaf에서 시작해 node에 도달할 때, 경로에 있는 node의 총합의 최댓값을 구하시오.

sys.setrecursionlimit(10**6)


def main() -> None:

    # [Ideas]

    # 말을 좀 이상하게 쓰긴 했는데, 이해는 지리게 했다.
    # 거꾸로 가면 된다는 거지. W에서부터 bfs 돌리면 되는거 아니야?
    # leaf까지 더해가면서, leaf에 도달하면 최댓값 갱신하기. 이거 아니야??

    # 근데 생각해보니, 시간초과 위험이 있다. 아;;;;;;; 왜.
    # 어떤 노드에 도달하기까지의 최댓값을 구해놓는게 가능하지. 그렇지.
    # dp로 풀었어야 한다는 것도 이해했는데, 이거 안되는구나.

    #   / 2 \       / 6 \
    # 1       4 - 5       8 이해가 쏙쏙 되잖아... 4 도달 최댓값을 구해두면 8에서 편하게 할 수 있네.
    #   \ 3 /       \ 7 /

    ##########

    T = int(input())

    for _ in range(T):
        # 노드의 수, 간선의 수
        N, K = map(int, input().split())
        values = list(map(int, input().split()))
        graph = [[] for _ in range(N + 1)]
        for _ in range(K):
            # u->v 입력이지만, 거꾸로 들어갈거니까 v->u 로 저장한다.
            u, v = map(int, input().split())
            graph[v].append(u)
        W = int(input())

        dp = [-1] * (N + 1)

        # dp[curr], 즉 curr까지 도달하는 최댓값이 반환된다.
        def dfsR(curr):

            # dp가 차있으면 반환한다.
            if dp[curr] != -1:
                return dp[curr]

            # 리프노드면 dp[curr]는 values가 된다.
            if not graph[curr]:
                dp[curr] = values[curr - 1]
                return dp[curr]

            # 리프노드가 아니면 만들어서 반환한다.
            mx = 0
            for nei in graph[curr]:
                # 더 작은 레벨로 들어가서 dp[nei]를 가져온다.
                mx = max(mx, dfsR(nei))

            # 최댓값에 curr value를 더해 dp에 저장한다.
            dp[curr] = mx + values[curr - 1]
            return dp[curr]

        dfsR(W)
        print(dfsR(W))

    ##########

    return


# [Review]

# 아~ 이거거든. 그래프를 뒤집는 거지.
# 문제를 쉽게 만들 수 있는 건 항상 발상이다.

# 까지는 맞았는데, dp가 없어도 괜찮을거라고 생각해버렸다.


if __name__ == "__main__":
    main()
