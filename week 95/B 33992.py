# Authored by : marigold2003
# Date : 2026-03-26
# Link : https://www.acmicpc.net/problem/33992


import sys

input = sys.stdin.readline


# [Summary] 사막 탐험

# 사막은 2차원 평면이다.
# 현위치는 ax, ay이고, 목표위치는 bx, by이다.
# 오아시스는 px, py를 중심으로 하며 반지름이 r인 원이다.

# 체력은 이동한 유클리드거리만큼 소모된다.
# 오아시스 안에서는 체력이 소모되지 않는다.
# 보물의 위치에 도달하기 위해 소모해야 하는 체력의 최솟값을 구하시오.


def main() -> None:

    # [Ideas]

    # 오아시르를 경유하냐, 안하냐로 나뉜다.
    # 경유 안할 땐 직선경로를 그으면 된다.

    # 경유할 땐 시작지에서 오아시스 중심까지 유클리드거리 - r
    # + 도착지에서 오아시스 중심까지 유클리드거리 - r 을 하면 된다.

    # 이 둘 중에 작은 걸 출력하면 된다.

    ##########

    from math import hypot

    ax, ay, bx, by, px, py, r = map(int, input().split())
    skip_oasis_dist = hypot(bx - ax, by - ay)
    via_oasis_dist = max(0, hypot(ax - px, ay - py) - r) + max(
        0, hypot(bx - px, by - py) - r
    )

    print(min(skip_oasis_dist, via_oasis_dist))

    ##########

    return


# [Review]

# 직관적으로 문제를 풀 수 있었다.
# 원의 중심까지 가는 거리에서 반지름을 빼면
# 원의 지름에 닿는 가장 짧은 거리가 된다.


if __name__ == "__main__":
    main()
