# Authored by : marigold2003
# Date : 2026-03-15
# Link : https://www.acmicpc.net/problem/31566


import sys

input = sys.stdin.readline


# [Summary] 힘세고 강한 아침

# 정점은 N(<= 100)개이다.
# b -c-> t 인 간선 M개가 주어진다.

# s번 정점에서 시작해서 e번 정점으로 갈 때
# k번 정점을 거치지 않고 가는 최소 비용을 구하시오.

# s k e는 200K회 주어진다.


def main() -> None:

    # [Ideas]

    # 일단 딱보면 최단경로.
    # bfs로 잘 풀어보자.
    # 가중치가 있는데 bfs가 되나?

    # 근데 애초에 문제가, 200K번 질문이 들어온다는거임.
    # 이런식으로 나온다는건 미리 구해놔야 된다는건데.

    # 정점 개수가 적은게 포인트가 될 것이다.
    # 각 정점마다 k를 경유하지 않는 최단경로를 전부 구할 수 있을까?

    # 근데 정점 200개면 그냥 200K번 다익도 가능하지 않냐?
    # 그래도 플로이드워셜을 배워보자.

    ##########

    INF = sys.maxsize

    N, M, Q = map(int, input().split())

    # dist[i][j] == i -> j 비용
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    # 대각선 0 처리
    for i in range(1, N + 1):
        dist[i][i] = 0

    # 간선 입력받기
    for _ in range(M):
        b, t, c = map(int, input().split())
        dist[b][t] = min(dist[b][t], c)

    # ans[k][i][j]
    # k를 사용하지 않는 i -> j 의 최단거리
    ans = [[[INF] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

    # 1 ~ N 까지 k가 될 수 있는 모든 경우를 구해둔다.
    for k in range(1, N + 1):

        # k 제거를 위한 dist 깊은복사
        d = [row[:] for row in dist]

        # k 제거하기 (정점 삭제)
        for i in range(1, N + 1):
            d[k][i] = INF
            d[i][k] = INF

        # 플로이드 전개
        for mid in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    # mid 사용안함 vs i -> mid -> j 경유
                    d[i][j] = min(d[i][j], d[i][mid] + d[mid][j])

        # 전개를 끝낸 dist 2차원 list를 그대로 ans[k]에 저장한다.
        ans[k] = d

    for _ in range(Q):

        s, k, e = map(int, input().split())

        res = ans[k][s][e]
        print("No" if res == INF else res)

    ##########

    return


# [Review]

# 이게 플로이드 워셜인가
# 졸라 어렵네.

# 할만한거같기도 하고?
# 다익 냄새가 좀 난다해야하나.
# 근데 전체 쌍을 한번에 다 구할수있는게 좀 좋네.


if __name__ == "__main__":
    main()
