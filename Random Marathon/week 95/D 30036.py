# Authored by : marigold2003
# Date : 2026-03-29
# Link : https://www.acmicpc.net/problem/30036


import sys

input = sys.stdin.readline


# [Summary] INK

# N*N(<= 100) board가 주어진다.

# U, D, L, R은 각 상 하 좌 우 이동을 의미한다.

# j는 잉크 충전, J는 잉크 발산이다.
# 잉크를 i번 충전했을 때 i크기의 마름모꼴로 퍼진다.
# 범위에 벽이 있으면 칠한다.

# 잉크의 색은 점프할 때마다 1씩 인덱스가 옮겨진다.

# 시뮬레이션한 결과를 출력하시오.


def main() -> None:

    # [Ideas]

    # 시뮬레이션이다. 시뮬레이션.
    # 구현을 잘 해보자.

    # 마름모 범위를 어떻게 효율적으로 처리할 수 있을까?

    ##########

    # 잉크문자열 길이, board size, 커맨드 횟수
    I, N, K = map(int, input().split())
    ink_string = input().rstrip()
    board = [list(input().rstrip()) for _ in range(N)]
    commands = list(input().rstrip())

    walls = set()
    for y in range(N):
        for x in range(N):
            if board[y][x] == "#":
                walls.add((y, x))
            if board[y][x] == "@":
                # 시작좌표 (r, c)
                r, c = (y, x)

    curr_ink = 0
    jump_count = -1
    for cmd in commands:

        if cmd == "j":
            # 잉크 증가
            curr_ink += 1
            # 커맨드 j 종료
            continue

        elif cmd == "J":
            # 점프 횟수 증가
            jump_count = (jump_count + 1) % I

            if not curr_ink:
                continue

            # 마름모 범위 확인 후 벽 있으면 색칠
            for n in range(1, curr_ink + 1):
                for dr in range(n + 1):
                    dc = n - dr
                    for i, j in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
                        if (r + dr * i, c + dc * j) in walls:
                            board[r + dr * i][c + dc * j] = ink_string[jump_count]

            # 잉크 초기화
            curr_ink = 0
            # 커맨드 J 종료
            continue

        # 상하좌우 이동
        elif cmd == "U":
            dr, dc = -1, 0
        elif cmd == "D":
            dr, dc = 1, 0
        elif cmd == "L":
            dr, dc = 0, -1
        elif cmd == "R":
            dr, dc = 0, 1

        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if board[nr][nc] != ".":
            continue

        # 있던 자리, 이동할 자리 갱신
        board[r][c] = "."
        board[nr][nc] = "@"

        # 좌표 갱신
        r, c = nr, nc

    for row in board:
        print("".join(row))

    ##########

    return


# [Review]

# 구현은 재밌게 하면 된다.
# 게임 만드는 느낌이 드는걸, 정말로 게임만들기는 구현의 끝이구나.


if __name__ == "__main__":
    main()
