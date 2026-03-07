# Authored by : marigold2003
# Date : 2026-03-07
# Link : https://www.acmicpc.net/problem/27942


import sys

input = sys.stdin.readline


# [Summary] :danceplant:

# N*N(3K) board가 있다. 각 칸에는 -25~25의 정수가 써 있다.
# 중심 2*2직사각형 범위로 시작해서 숫자의 합이 큰 쪽으로 직사각형을 늘려 포함시킨다.
# 합이 같은 방향이 여럿이면 상하좌우 순으로 늘린다.
# 늘릴 공간이 없거나 합이 0 이하라면 종료.

# 범위에 포함된 숫자의 합을 출력하시오.


def main() -> None:

    # [Ideas]

    # 누적합이 필요해 보인다.
    # 가로와 세로로 모두 누적합을 구해둬야 할 듯.

    ##########

    from itertools import accumulate

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    row_acc = []
    for row in board:
        row_acc.append(list(accumulate(row, initial=0)))

    col_acc = []
    for col in zip(*board):
        col_acc.append(list(accumulate(col, initial=0)))

    # 상 하 좌 우 변의 위치
    pos = [N // 2 - 1, N // 2, N // 2 - 1, N // 2]
    u, d, l, r = 0, 1, 2, 3

    directions = "UDLR"
    count = 0
    answer = []

    while True:
        curr = 0
        dir = 0

        # 상
        if pos[u] >= 1:
            up = row_acc[pos[u] - 1][pos[r] + 1] - row_acc[pos[u] - 1][pos[l]]
            if curr < up:
                curr = up
                dir = u
        # 하
        if pos[d] < N - 1:
            down = row_acc[pos[d] + 1][pos[r] + 1] - row_acc[pos[d] + 1][pos[l]]
            if curr < down:
                curr = down
                dir = d
        # 좌
        if pos[l] >= 1:
            left = col_acc[pos[l] - 1][pos[d] + 1] - col_acc[pos[l] - 1][pos[u]]
            if curr < left:
                curr = left
                dir = l
        # 우
        if pos[r] < N - 1:
            right = col_acc[pos[r] + 1][pos[d] + 1] - col_acc[pos[r] + 1][pos[u]]
            if curr < right:
                curr = right
                dir = r

        if not curr:
            break

        if dir == u or dir == l:
            pos[dir] -= 1
        else:
            pos[dir] += 1

        count += curr
        answer.append(directions[dir])

    print(count)
    print("".join(answer))

    ##########

    return


# [Review]

# 발상은 쉬운데 생각보다 구현이 귀찮음


if __name__ == "__main__":
    main()
