import sys

input = sys.stdin.readline


# X의 모든 조상을 구한다.


def main() -> None:
    # 노드 개수, 간선 개수
    N, M = map(int, input().split())

    # 단방향 그래프, 트리형태로 입력
    # X에서부터 내려갈 것이므로 간선을 뒤집는다.
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)

    # 도달 목표, 시작점으로 사용
    X = int(input())

    # bfs
    from collections import deque

    def bfs(start):
        queue = deque()
        visited = [False for _ in range(N + 1)]

        queue.append(start)
        visited[start] = True

        while queue:
            curr = queue.popleft()

            for nei in graph[curr]:
                if visited[nei]:
                    continue
                queue.append(nei)
                visited[nei] = True

        # X를 루트로 해서 방문한 모든 노드가 X에 선행되는 노드가 된다.
        return sum(visited) - 1

    print(bfs(X))


if __name__ == "__main__":
    main()
