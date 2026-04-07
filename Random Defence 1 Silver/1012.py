"""
import sys

input = sys.stdin.readline

from collections import deque

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


def func():
    M, N, K = map(int, input().split())

    board = [[0 for _ in range(M)] for _ in range(N)]

    kimchi = set()
    for _ in range(K):
        x, y = map(int, input().split())
        kimchi.add((y, x))
        board[y][x] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]

    def bfs(sy, sx):
        queue = deque()
        queue.append((sy, sx))
        visited[sy][sx] = True

        while queue:
            y, x = queue.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if ny < 0 or N <= ny or nx < 0 or M <= nx:
                    continue
                if visited[ny][nx]:
                    continue
                if board[ny][nx] == 0:
                    continue

                visited[ny][nx] = True
                queue.append((ny, nx))

    result = 0
    for y, x in kimchi:
        if not visited[y][x]:
            bfs(y, x)
            result += 1

    print(result)


def main():
    T = int(input())

    for _ in range(T):
        func()


main()
"""

# O(M*N) 이잖아. O(K)도 가능한거같은데?
# 이거 굳이 board를 만들어야되나?

import sys

input = sys.stdin.readline

from collections import deque

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


def func():
    M, N, K = map(int, input().split())

    kimchi = set()
    for _ in range(K):
        x, y = map(int, input().split())
        kimchi.add((y, x))

    result = 0

    while kimchi:
        current = kimchi.pop()
        result += 1

        queue = deque()
        queue.append(current)

        while queue:
            y, x = queue.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if (ny, nx) not in kimchi:
                    continue
                kimchi.remove((ny, nx))
                queue.append((ny, nx))

    print(result)


def main():
    T = int(input())

    for _ in range(T):
        func()


main()
