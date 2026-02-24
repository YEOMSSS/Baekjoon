# Authored by : marigold2003
# Date : 2026-02-23
# Link : https://www.acmicpc.net/problem/1197


import sys

input = sys.stdin.readline


# [Summary] 최소 스패닝 트리

# graph가 주어졌을 때, 그 graph의 MST를 구하시오.

# graph는 A번 node와 B번 node가 weight가 C인 edge로 연결되어 있으며,
# node V(10K)개와 edge E(100K)개를 갖는다.


def main() -> None:

    # [Ideas]

    # prim으로 풀자. 대조군으로 그걸 쓸 거니까 연습해두자고.
    # prim을 정리해볼까? 강의를 떠올려라.

    # 아무 node에서 min weight로 neighbor에 이동해 MST를 시작한다.
    # 현재 MST에 연결된 제일 짧은 node를 또 MST에 넣는다.
    # 반복한다. 아, heapq를 사용하면 되겠군.

    ##########

    V, E = map(int, input().split())

    # graph[node] = (weight, neighbor)
    # 굳이 weight를 앞에 두는 이유는, min heap이 weight를 기준으로 작동하게 하기 위함이다.
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    import heapq

    # MST는 어느 node에서 start하냐에 따라 shape은 달라질 수 있지만
    # MST total weight는 불변이다. 아, dup weight가 있는 경우만 말이다.

    # 아무 이유 없이 1번 node에서부터 start한다. start weight는 0.
    min_heap = [(0, 1)]

    visited = [False for _ in range(V + 1)]
    total_wei = 0

    while min_heap:
        # curr MST에서 이동 가능한 node 중 min weight로 이동가능한 node
        wei, node = heapq.heappop(min_heap)

        # visited node 처리
        if visited[node]:
            continue

        # MST 확장, curr node visited 하고 total에 curr weight 더하기
        visited[node] = True
        total_wei += wei

        # curr node의 not visited인 neighbor 전부 heap에 push
        for nei_wei, nei_node in graph[node]:
            if visited[nei_node]:
                continue

            heapq.heappush(min_heap, (nei_wei, nei_node))

    print(total_wei)

    ##########

    return


# [Review]

# coffee에 prim은 빼주세요. pardon?


if __name__ == "__main__":
    main()
