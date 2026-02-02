# Authored by : marigold2003
# Date : 2026-01-29
# Link : https://www.acmicpc.net/problem/34231

import sys

input = sys.stdin.readline


# [Summary]

# 최대 15*15 배열이 들어오고, 그 안에서 직사각형으로 값을 선택한다.
# 만약 그 값이 1부터 x까지 서로 다른 정수 x개로 이루어져 있다면 순열이라 한다.
# 순열의 개수를 구하시오.


def main():

    # [Ideas]

    # 일단 1은 무조건 순열이다. 그 자체로.
    # 이후는 배열 내에서 서로 다른 값을 2개 선택하는 모든 조합을 보면 된다.
    # 225*224//2*1 = 25200 충분히 브루트포스 가능.
    # 검사는 set(range(1,x+1))로 가능할듯?

    ##########

    from itertools import combinations

    N = int(input())
    board = tuple(tuple(map(int, input().split())) for _ in range(N))

    # 1이면 무조건 센다. {1} = set(range(1))이라서 순열이다.
    count = sum(row.count(1) for row in board)

    coords = tuple((r, c) for r in range(N) for c in range(N))
    for comb in combinations(coords, 2):
        # 좌상에서 우하로 내려가는 경우만 확인한다.
        if comb[0][1] > comb[1][1]:
            continue

        temp = set(
            board[r][c]
            for r in range(comb[0][0], comb[1][0] + 1)
            for c in range(comb[0][1], comb[1][1] + 1)
        )

        # range 만족시 성공
        if temp == set(
            range(1, (comb[1][0] - comb[0][0] + 1) * (comb[1][1] - comb[0][1] + 1) + 1)
        ):
            count += 1

    print(count)

    ##########

    return


# [Review]

# 아이디어를 떠올리긴 쉬웠다.
# 구현이 조금 귀찮았음. 20분 타이머 걸었는데 26분 걸렸다.
# 아직 한참 멀었다! 더 정진해라.
# 아이디어는 있는데 구현이 오래 걸린다.

if __name__ == "__main__":
    main()
