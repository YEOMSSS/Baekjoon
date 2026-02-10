"""
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 정점, 간선, 시작점
N, M, R = map(int, input().split())
depths = [-1] * (N + 1)


graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)


def dfsR(start, depth):
    visited[start] = True
    depths[start] = depth
    for nei in graph[start]:
        if visited[nei]:
            continue
        dfsR(nei, depth + 1)


dfsR(R, 0)

for i in range(1, N + 1):
    print(depths[i])
"""

import sys

input = sys.stdin.readline

# 정점, 간선, 시작점
N, M, R = map(int, input().split())
depths = [-1] * (N + 1)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
stack = [(R, 0)]

while stack:
    current, depth = stack.pop()

    if visited[current]:
        continue
    visited[current] = True
    depths[current] = depth

    for nei in reversed(graph[current]):
        if visited[nei]:
            continue

        stack.append((nei, depth + 1))

for i in range(1, N + 1):
    print(depths[i])
