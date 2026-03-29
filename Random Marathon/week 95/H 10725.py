# Authored by : marigold2003
# Date : 2026-03-28
# Link : https://www.acmicpc.net/problem/10725


import sys

input = sys.stdin.readline


# [Summary] 빛의 왕과 거울의 미로 1

# N*M(<= 8) board에 대각선 거울을 끼워넣는다.
# 밖에서 레이저를 쏘면 거울에 반사되어 나온다.
# 거울을 배치하는 모든 경우의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 일단 백트래킹 문제인건 알겠음.
    # 구현만 잘 하면 될 듯. 귀찮을거같은데...

    # 시뮬레이션하는거 하나 있어야하고.
    # dfs형식으로 백트래킹돌리면 될듯.

    ##########

    N, M, x, y = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    def func(x):
        if 1 <= x <= M:
            return (-1, x - 1, 2)
        elif M + 1 <= x <= M + N:
            return (x - M - 1, -1, 1)
        elif M + N + 1 <= x <= M + N + N:
            return (x - M - N - 1, M, 3)
        elif M + N + N + 1 <= x <= M + N + N + M:
            return (N, x - M - N - N - 1, 0)

    # 시작 r,c,dir 정보와 끝 r,c,dir 정보
    start = func(x)
    goal_coord = func(y)[:2]

    # / 일 때 상우, 우상, 하좌, 좌하
    slash = [1, 0, 3, 2]
    # \ 일 때 상좌, 우하, 하우, 좌상
    backslash = [3, 2, 1, 0]

    # 완성된 board에 대해 나오는 칸 찾기
    def simulation(start):
        r, c, dir = start

        while True:
            # 다음 방향으로 한 칸 이동한다.
            r += dr[dir]
            c += dc[dir]

            # 밖으로 나간 경우 종료
            if not (0 <= r < N and 0 <= c < M):
                return (r, c, dir)

            # 거울이면 방향이 바뀐다.
            if board[r][c] == "/":
                dir = slash[dir]
            elif board[r][c] == "\\":
                dir = backslash[dir]

    # 거울을 새로 놓을 수 있는 칸을 확인한다.
    q_marks = [(r, c) for r in range(N) for c in range(M) if board[r][c] == "?"]
    q_count = len(q_marks)

    answer = 0

    def dfsR_backtrack(qid):
        nonlocal answer

        if qid == q_count:
            if simulation(start)[:2] == goal_coord:
                answer += 1
            return

        r, c = q_marks[qid]

        # / 넣어보기
        board[r][c] = "/"
        dfsR_backtrack(qid + 1)

        # \ 넣어보기
        board[r][c] = "\\"
        dfsR_backtrack(qid + 1)

        # . 넣어보기
        board[r][c] = "."
        dfsR_backtrack(qid + 1)

        # ?로 돌려놓고 이전 단계로 이동
        board[r][c] = "?"

    dfsR_backtrack(0)
    print(answer % 10_007)

    ##########

    return


# [Review]

# ?에 두 종류의 거울과 점을 다 넣어봐야 한다.
# 시뮬레이션할때 들어온 방향과 거울, 다음 방향을 잘 생각해볼수있도록 하자.


if __name__ == "__main__":
    main()
