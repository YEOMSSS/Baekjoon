# 십자가 나오는 지점이 심장이다.

import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())

    board = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if board[r][c] != "*":
                continue

            count = 0
            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if board[nr][nc] == "*":
                    count += 1

            # 상하좌우가 전부 *이면 심장
            if count == 4:
                heart = (r, c)

    # 왼팔
    left_arm = 0
    for nc in range(heart[1] - 1, -1, -1):
        if board[heart[0]][nc] == "*":
            left_arm += 1
        else:
            break
    # 오른팔
    right_arm = 0
    for nc in range(heart[1] + 1, N):
        if board[heart[0]][nc] == "*":
            right_arm += 1
        else:
            break

    # 허리
    waist = 0
    for nr in range(heart[0] + 1, N):
        if board[nr][heart[1]] == "*":
            waist += 1
        else:
            break

    # 왼다리
    right_leg = 0
    for nr in range(heart[0] + waist + 1, N):
        if board[nr][heart[1] + 1] == "*":
            right_leg += 1
        else:
            break

    # 오른다리
    left_leg = 0
    for nr in range(heart[0] + waist + 1, N):
        if board[nr][heart[1] - 1] == "*":
            left_leg += 1
        else:
            break

    print(*map(lambda x: x + 1, heart))
    print(left_arm, right_arm, waist, left_leg, right_leg)


if __name__ == "__main__":
    main()
