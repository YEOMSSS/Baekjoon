# Authored by : marigold2003
# Date : 2026-02-15
# Link : https://www.acmicpc.net/problem/16486


import sys

input = sys.stdin.readline


# [Summary] 운동장 한 바퀴

# 영역 A와 B는 반원이며 반지름은 d2이다.
# C는 d1 * (d2 * 2) 인 직사각형이다.
# 원주율은 3.141592이다.

# 도형 A + C + B의 둘레의 값을 구하시오.


def main() -> None:

    # [Ideas]

    # 그니까 이게 그림이 없어서 설명이 좀 어려운데.
    # 결국에 2 * 가로길이 + 원의 지름이다.
    # 그러니까 (d1 * 2) + (2 * 3.141592 * d2) 라는 거지.

    ##########

    d1 = int(input())
    d2 = int(input())

    print((d1 * 2) + (2 * d2 * 3.141592))

    ##########

    return


# [Review]

# 수학익힘책을 펼친 기분이군요


if __name__ == "__main__":
    main()
