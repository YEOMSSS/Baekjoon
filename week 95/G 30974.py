# Authored by : marigold2003
# Date : 2026-03-27
# Link : https://www.acmicpc.net/problem/30974


import sys

input = sys.stdin.readline


# [Summary] What's your ETA?

# 1~N의 번호가 부여된 N(400K)개의 정류장이 있다.
# 정류장 사이에는 소요시간이 정해진 양방향 도로가 M(1M)개 있다.
# 버스는 두 정류장 코드의 합이 소수인 경우만 운행된다.

# 1번에서 N번으로 가는 최소 소요 시간을 구하시오.
# 불가능한 경우 Now where are you?를 출력한다.


def main() -> None:

    # [Ideas]

    # 일단 소수판정인데, 코드가 <= 5M이다.
    # 10M까지 소수판정을 해야한다는 소리. 에테체 돌려놓고.

    # 그리고 도로를 입력받을때 소수판정을 다 해서 그래프를 만들자.
    # 거기서 N까지 돌리면 되지롱. 가중치 있으니까 다익으로 해야할듯.

    ##########

    INF = 10**18

    from heapq import heappop, heappush

    def sieve(n):
        # 입력: n (정수)
        # 상태: 0~n까지 소수 여부 배열
        is_prime = [True] * (n + 1)

        # 조건: 0,1은 소수가 아님 (불변량 정리)
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False

        # 연산: i ≤ sqrt(n) 까지만 배수 제거
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:  # 아직 제거되지 않았다면
                # 상태 변화: i의 배수 제거
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False

        # 결과 확인: True인 인덱스만 반환
        return is_prime

    is_prime = sieve(10_000_000)

    # 노드 N개, 간선 M개
    N, M = map(int, input().split())
    codes = tuple(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        if is_prime[codes[u - 1] + codes[v - 1]]:
            graph[u].append((v, w))
            graph[v].append((u, w))

    def dijkstra(graph: list, start, end):

        heap = [(0, start)]
        visited = [False] * (N + 1)
        dist = [INF] * (N + 1)
        dist[start] = 0

        while heap:
            _, curr = heappop(heap)
            if visited[curr]:
                continue
            visited[curr] = True

            if curr == end:
                return dist[curr]

            for nei, w in graph[curr]:
                if dist[curr] + w < dist[nei]:
                    dist[nei] = dist[curr] + w
                    heappush(heap, (dist[nei], nei))

        if end:
            return dist[end]

    answer = dijkstra(graph, 1, N)
    print("Now where are you?" if answer == INF else answer)

    ##########

    return


# [Review]

# 소수판정 + 다익스트라.
# 입력되는 데이터가 크다.


if __name__ == "__main__":
    main()
