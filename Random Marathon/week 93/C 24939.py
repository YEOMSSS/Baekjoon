# Authored by : marigold2003
# Date : 2026-03-14
# Link : https://www.acmicpc.net/problem/24939


import sys

input = sys.stdin.readline


# [Summary] Boardle

# 매우 큰 N*M Board에서 게임이 진행된다.
# 보물은 한 칸에만 숨겨져 있으며, 찾기 위해 Q회의 질문을 한다.
# 점 (x, y)를 기준으로 보물이 어느 방향에 숨겨져 있는가?
# 그 결과는 동(+x) 서(-x) 남(-y) 북(+y) 북동 북서 남동 남서 일치 9가지로 나타내어진다.
# 보물이 있을 수 있는 격자칸의 후보의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 9경우를 구현해야 한다.
    # 뭐 귀찮은 문제구만.

    # 1. +x | 2. -x | 3. -y | 4. +y
    # 5. +x +y | 6. +y -x | 7. -y +x | 8. -y -x | 9 ==

    # 변의 위치를 저장해놓고
    # 입력마다 잘라내면 될거같은데?

    ##########

    N, M = map(int, input().split())
    Q = int(input())

    up, down, left, right = 1, M, 1, N

    for _ in range(Q):
        x, y, d = map(int, input().split())

        match d:
            case 1:
                up = y
                down = y
                left = max(left, x + 1)
            case 2:
                up = y
                down = y
                right = min(right, x - 1)
            case 3:
                down = min(down, y - 1)
                left = x
                right = x
            case 4:
                up = max(up, y + 1)
                left = x
                right = x
            case 5:
                up = max(up, y + 1)
                left = max(left, x + 1)
            case 6:
                up = max(up, y + 1)
                right = min(right, x - 1)
            case 7:
                down = min(down, y - 1)
                left = max(left, x + 1)
            case 8:
                down = min(down, y - 1)
                right = min(right, x - 1)
            case 9:
                up = y
                down = y
                left = x
                right = x

    print((down - up + 1) * (right - left + 1))

    ##########

    return


# [Review]

# 이게 맞는 건가 싶구만.
# 구현이 너무 귀찮고 실수할 여지가 많아.
# 하지만 맞았으면 그만 아닐까?


if __name__ == "__main__":
    main()
