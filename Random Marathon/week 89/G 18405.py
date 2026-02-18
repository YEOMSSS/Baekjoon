# Authored by : marigold2003
# Date : 2026-02-15
# Link : https://www.acmicpc.net/problem/18405


import sys

input = sys.stdin.readline


# [Summary] 경쟁적 전염

# N*N board에 1번 바이러스부터 k번 바이러스까지 있다.
# 작은 숫자 바이러스부터 상하좌우로 퍼져나간다.
# 이미 바이러스가 퍼진 좌표에는 퍼질 수 없다.
# S초 후 (X, Y)에 있는 바이러스의 종류를 출력하시오.


def main() -> None:

    # [Ideas]

    # 딱 봐도 bfs죠?
    # 처음에 입력받을 때 visited만 대충 잘 해주자.

    ##########

    from collections import deque

    N, K = map(int, input().split())
    board = list(list(map(int, input().split())) for _ in range(N))
    S, X, Y = map(int, input().split())

    # 각 바이러스 시작 좌표 저장
    start = [[] for _ in range(K + 1)]

    for r in range(N):
        for c in range(N):

            if board[r][c]:
                start[board[r][c]].append((r, c))

    # bfs 시작
    queue = deque()
    for row in start:
        for coord in row:
            queue.append(coord)

    # 방문배열 대신 board를 사용할 것이다.

    level = 0
    while queue:

        # S초가 지나면 더이상 전염은 없다.
        if level == S:
            break

        for _ in range(len(queue)):
            r, c = queue.popleft()

            # r, c가 차있으면 종료해도 된다.
            if (r, c) == (X - 1, Y - 1):
                print(board[r][c])
                return

            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if board[nr][nc]:
                    continue

                # 전염시키고, 큐에 push
                board[nr][nc] = board[r][c]
                queue.append((nr, nc))

        level += 1

    print(board[X - 1][Y - 1])

    ##########

    return


# [Review]

# 구현에서 실수만 없으면 된다.
# bfs는 들어온 순서대로 퍼진다는 것을 이용하면 편함.


if __name__ == "__main__":
    main()
