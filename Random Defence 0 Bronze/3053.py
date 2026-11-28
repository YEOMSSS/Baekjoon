# Authored by : marigold2003
# Date : 2026-11-28
# Link : https://www.acmicpc.net/problem/3053


import sys

input = sys.stdin.readline


# [Summary] 택시 기하학

# 반지름이 주어질 때
# 유클리드 기하학에서의 원의 넓이와
# 택시 기하학에서의 원의 넓이를 출력하시오.

# D(T1,T2) = |x1-x2| + |y1-y2|
# 이것이 택시 기하학에서 두 점 사이 거리를 구하는 공식이다.
# 원: 평면 상의 어떤 점에서 거리가 일정한 점들의 집합


def main() -> None:

    # [Ideas]

    # 택시 기하학에서의 원은 마름모로 생겼겠네.
    # 그럼 반지름이 r이면 그게 원점에서의 거리인거니까
    # 그냥 2 * r**2가 택시기하학에서의 원넓이인것이다.
    # 유클리드에선 파이 * r**2인게 당연하고.

    ##########

    from math import pi

    r = int(input())
    rr = r**2

    print(pi * rr)
    print(2 * rr)

    ##########

    return


# [Review]

# 소수점 관리를 안해도 알아서 채점해준다.


if __name__ == "__main__":
    main()
