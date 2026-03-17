# Authored by : marigold2003
# Date : 2026-03-17
# Link : https://www.acmicpc.net/problem/11758


import sys

input = sys.stdin.readline


# [Summary] CCW

# 점 3개가 들어온다.
# p1, p2, p3을 순서대로 이은 선분이 어떤 방향인지 구하시오.
# 반시계 1 시계 -1 일직선 0


def main() -> None:

    # [Ideas]

    # 외적하자.

    ##########

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    ccw = ((x2 - x1) * (y3 - y1)) - ((y2 - y1) * (x3 - x1))

    if ccw > 0:
        print(1)
    elif ccw < 0:
        print(-1)
    else:
        print(0)

    ##########

    return


# [Review]

# 기울기 비교라고 생각하면 된다.


if __name__ == "__main__":
    main()
