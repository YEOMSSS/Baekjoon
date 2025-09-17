
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_idx, M_idx = N * 3, M * 3

map = [list(input().rstrip()) for _ in range(N * 3)]

# 상하좌우
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

for row in range(N):
    for col in range(M):
        if (row + col) % 2 == 0:
            continue

        check = 0 # 상하좌우가 다 비었을 경우 확인용

        # 현 칸의 중앙을 가리키는 인덱스
        row_idx, col_idx = row * 3 + 1, col * 3 + 1

        for dy, dx in directions:
            ny, nx = row_idx + (dy * 2), col_idx + (dx * 2)

            # 인덱스 초과 방지
            if ny < 0 or N_idx <= ny or nx < 0 or M_idx <= nx:
                continue

            if map[ny][nx] == "#":
                map[row_idx + dy][col_idx + dx] = "#"
                check = 1

        if check:
            map[row_idx][col_idx] = "#"

for row in map:
    print("".join(row))