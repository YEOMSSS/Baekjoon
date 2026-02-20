# Authored by : marigold2003
# Date : 2026-02-20
# Link : https://www.acmicpc.net/problem/32754


import sys

input = sys.stdin.readline


# [Summary] 손이 닿는 범위

# (0, 0)을 중심으로 하는 반지름 R인 원에
# 입력된 직사각형이 접하거나 포함되는지 검사해라.

# 직사각형들은 무게중심을 기준으로 회전시킬 수 있다.
# 최대 몇 개까지 닿을 수 있는지 구하시오.


def main() -> None:

    # [Ideas]

    # 직사각형의 무게중심은 대각선의 중점이다.
    # 그 중점에서 나오는 반지름은 대각선 / 2이다.
    # 팔길이 + 대각선/2가 무게중심~원점 거리보다 짧으면 닿을 수 없다.

    # 구현만 하면 되겠구만. 다 제곱상태로 굴리자.

    ##########

    N, R = map(int, input().split())

    def squared_dist(x1, y1, x2, y2) -> float:
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    count = 0

    for _ in range(N):

        x1, y1, _, _, x3, y3, _, _ = map(int, input().split())

        mid_x, mid_y = (x1 + x3) / 2, (y1 + y3) / 2
        mid_r = squared_dist(x1, y1, mid_x, mid_y)

        # 반지름의 합이 거리보다 길거나 같으면 닿을 수 있다.
        if squared_dist(0, 0, mid_x, mid_y) <= ((mid_r) ** 0.5 + R) ** 2:
            count += 1

    print(count)

    ##########

    return


# [Review]

# 기하학은 기하학 하고 웃는다.
# 놀랄 때는 갸학! 기하학!

# 아, 루트 쓰기 싫었는데


if __name__ == "__main__":
    main()
