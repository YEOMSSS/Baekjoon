# Authored by : marigold2003
# Date : 2026-03-12
# Link : https://www.acmicpc.net/problem/2121


import sys

input = sys.stdin.readline


# [Summary] 넷이 놀기

# 점이 여러개 존재한다. (<= 500K)
# 점 4개를 골라서 직사각형을 만들 것이다.
# A*B 인 직사각형을 몇 가지 만들 수 있는지 출력하시오.


def main() -> None:

    # [Ideas]

    # 포인트는 직사각형 판정이다.
    # (r,c)인 점이 있으면 직사각형은
    # (r+A,c), (r,c+B), (r+A,c+B)가 있다.

    # 그러면 x:y dict와 y:x dict가 둘 다 필요할듯

    ##########

    from collections import defaultdict

    N = int(input())
    A, B = map(int, input().split())

    row_to_col = defaultdict(list)
    col_to_row = defaultdict(list)

    for _ in range(N):
        r, c = map(int, input().split())
        row_to_col[r].append(c)
        col_to_row[c].append(r)

    count = 0
    for r, cols in row_to_col.items():
        for c in cols:
            # (r, c)를 좌상단이라 한다.

            # 좌하단 확인
            left_down_candidates = row_to_col.get(r + A)
            if not left_down_candidates:
                continue
            if c not in left_down_candidates:
                continue

            # 우상단 확인
            right_up_candidates = col_to_row.get(c + B)
            if not right_up_candidates:
                continue
            if r not in right_up_candidates:
                continue

            # 우하단 확인
            if r + A not in right_up_candidates:
                continue

            count += 1

    print(count)

    ##########

    return


# [Review]

# 코드는 멀쩡해 보이긴 하는데
# 시간 안에 될까 이거?
# 잘만 되네, dict가 좋긴 좋은가보다?


if __name__ == "__main__":
    main()
