# Authored by : marigold2003
# Date : 2026-03-31
# Link : https://www.acmicpc.net/problem/34511


import sys

input = sys.stdin.readline


# [Summary] Polyominonal Puzzle

# N*M(<= 100) board가 X, Y, .으로 채워져서 입력된다.
# 각 뭉치는 연결되어있으며, 뭉치끼리는 겹치지 않는다.
# X뭉치와 Y뭉치가 맞닿아있는 선분의 길이의 총합을 구하시오.


def main() -> None:

    # [Ideas]

    # 좌상부터 시작해서 우하비교하며 내려가자.
    # 자신과 다르면 +1하면 되겠지.

    ##########

    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    count = 0
    for r in range(N):
        for c in range(M):
            curr = board[r][c]

            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                next = board[nr][nc]
                if curr == "X" and next == "Y":
                    count += 1
                elif curr == "Y" and next == "X":
                    count += 1

    print(count)

    ##########

    return


# [Review]

# delta를 이용해서 좌표를 탐험하자.


if __name__ == "__main__":
    main()
