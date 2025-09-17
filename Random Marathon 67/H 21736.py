
import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
board = list(input().rstrip() for _ in range(N))

# 어차피 360_000밖에 안되는데 그냥 한번 더 돌아서 찾자
for y in range(N):
    for x in range(M):
        if board[y][x] == "I":
            start = (y, x)

# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque()
queue.append(start)

cnt = 0
visited = [[False for _ in range(M)] for _ in range(N)]

while queue:
    y, x = queue.popleft()

    for dy, dx in directions:
        ny, nx = y + dy, x + dx

        if ny < 0 or N <= ny or nx < 0 or M <= nx:
            continue
        if visited[ny][nx]:
            continue
        if board[ny][nx] == "X":
            continue
        if board[ny][nx] == "P":
            cnt += 1

        visited[ny][nx] = True
        queue.append((ny, nx))

print(cnt if cnt else "TT")

# 오랜만에 그래프인데 나쁘진 않았나.