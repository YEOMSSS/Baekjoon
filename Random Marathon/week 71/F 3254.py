# 김밥을 던질 때마다 검사를 돌려버리자
# 개 노가다로 풀 수 있을 거 같은디?

import sys

input = sys.stdin.readline

board = [[None for _ in range(7)] for _ in range(6)]
check = [5 for _ in range(7)]

# 가로 검사
directions_row = ((-3, -2, -1), (-2, -1, 1), (-1, 1, 2), (1, 2, 3))

# 세로 검사
directions_col = (1, 2, 3)

# 대각선 검사
directions_diag = (
    ((-3, -3), (-2, -2), (-1, -1)),
    ((1, 1), (-2, -2), (-1, -1)),
    ((1, 1), (2, 2), (-1, -1)),
    ((1, 1), (2, 2), (3, 3)),
    ((-3, 3), (-2, 2), (-1, 1)),
    ((1, -1), (-2, 2), (-1, 1)),
    ((1, -1), (2, -2), (-1, 1)),
    ((1, -1), (2, -2), (3, -3)),
)


def func(n, b):
    y, x = check[n - 1], n - 1

    # 가로
    for temp in directions_row:
        for dx in temp:
            nx = x + dx
            if nx < 0 or 6 < nx:
                break
            if board[y][nx] != b:
                break
        else:
            return True
    # 세로
    for dy in directions_col:
        ny = y + dy
        if ny < 0 or 5 < ny:
            break
        if board[ny][x] != b:
            break
    else:
        return True

    # 대각선
    for temp in directions_diag:
        for dy, dx in temp:
            ny, nx = y + dy, x + dx
            if nx < 0 or 6 < nx or ny < 0 or 5 < ny:
                break
            if board[ny][nx] != b:
                break
        else:
            return True

    return False


def main():

    sj_list = [list(map(int, input().split())) for _ in range(21)]

    for i in range(21):
        s, j = sj_list[i]

        board[check[s - 1]][s - 1] = True
        if func(s, True):
            print("sk", i + 1)
            return
        check[s - 1] -= 1

        board[check[j - 1]][j - 1] = False
        if func(j, False):
            print("ji", i + 1)
            return
        check[j - 1] -= 1

    print("ss")


if __name__ == "__main__":
    main()
