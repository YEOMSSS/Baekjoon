import sys

input = sys.stdin.readline


def main():
    N, M, R = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(N + 1):
        graph[i].sort()

    result = [-1 for _ in range(N + 1)]

    stack = [(R, 0)]
    result[R] = 0

    while stack:
        current, depth = stack.pop()
        if result[current] == -1:
            result[current] = depth
        for nei in graph[current]:
            if result[nei] != -1:
                continue
            stack.append((nei, depth + 1))

    print("\n".join(map(str, result[1:])))


main()
