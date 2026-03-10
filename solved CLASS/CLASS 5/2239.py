# Authored by : marigold2003
# Date : 2026-03-10
# Link : https://www.acmicpc.net/problem/2239


import sys

input = sys.stdin.readline


# [Summary] 스도쿠

# 스도쿠는 풀다 만 스도쿠 퍼즐이 주어진다.
# 스도쿠를 해결하시오.


def main() -> None:

    # [Ideas]

    # 2580번이 생각나는 문제다.
    # 백트래킹을 또 잘 굴려보자.

    # 그냥 똑같은 문제같긴 한데, 7달이 지났으니 더 잘 풀겠지.

    ##########

    board = [list(map(int, input().rstrip())) for _ in range(9)]

    row_set = [set() for _ in range(9)]
    col_set = [set() for _ in range(9)]
    square_set = [set() for _ in range(9)]

    # curr square index
    def check_square(r, c):
        s = 0
        if 3 <= r < 6:
            s = 3
        elif 6 <= r < 9:
            s = 6

        if 3 <= c < 6:
            s += 1
        elif 6 <= c < 9:
            s += 2

        return s

    for r in range(9):
        for c in range(9):
            curr = board[r][c]
            if not curr:
                continue

            row_set[r].add(curr)
            col_set[c].add(curr)
            square_set[check_square(r, c)].add(curr)

    # sudoku backtracking
    def backtrack(i):
        if i == 81:
            return True

        r, c = i // 9, i % 9
        s = check_square(r, c)

        # 이미 차 있는 경우는 지나간다.
        # 이후 경로에서 False가 뜰 경우 가장 최근의 0으로 되돌아감
        if board[r][c]:
            return backtrack(i + 1)

        # 1~9 넣을 수 있면 넣어보기
        for n in range(1, 10):

            if n in row_set[r]:
                continue
            if n in col_set[c]:
                continue
            if n in square_set[s]:
                continue

            board[r][c] = n
            row_set[r].add(n)
            col_set[c].add(n)
            square_set[s].add(n)

            # 겹치지 않는 경우 n을 add하고 진행해본다.
            # 이후 경로에서 False가 뜰 경우 다음 n으로 넘어감
            if backtrack(i + 1):
                return True

            board[r][c] = 0
            row_set[r].remove(n)
            col_set[c].remove(n)
            square_set[s].remove(n)

        # 1~9를 전부 넣을 수 없으면 되돌아간다.
        return False

    backtrack(0)

    for row in board:
        print("".join(map(str, row)))

    ##########

    return


# [Review]

# 오랜만에 풀어보는 스도쿠 문제
# 뭔가 감회가 새롭다고 할까.


if __name__ == "__main__":
    main()
