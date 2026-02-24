import sys

input = sys.stdin.readline


def func(N, strings, graph, start) -> None:
    stack = []
    visited = [False] * (N + 1)

    stack.append(start)

    sequence = []
    while stack:
        current = stack.pop()
        sequence.append(current)

        for nei in graph[current][::-1]:

            if visited[nei]:
                continue

            stack.append(nei)
            visited[nei] = True

    for s in sequence:
        print(strings[s - 1], end="")


if __name__ == "__main__":

    # 입력
    N = int(input())
    strings = [input().rstrip() for _ in range(N)]

    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        i, o = map(int, input().split())
        graph[i].append(o)

    start = i

    func(N, strings, graph, start)
