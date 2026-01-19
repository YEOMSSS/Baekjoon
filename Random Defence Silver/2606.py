# c언어에서 append는 어떻게 해야 할까?

import sys

input = sys.stdin.readline

from collections import deque


def main():
    N = int(input())
    C = int(input())

    graph = [[] for _ in range(N + 1)]

    for _ in range(C):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    visited = [False] * (N + 1)

    queue.append(1)
    visited[1] = True

    result = 0

    while queue:
        current = queue.popleft()

        for nei in graph[current]:
            if visited[nei]:
                continue
            visited[nei] = True
            queue.append(nei)
            result += 1

    print(result)


main()
