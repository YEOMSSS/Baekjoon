# Authored by : marigold2003
# Date : 2026-04-01
# Link : https://www.acmicpc.net/problem/2712


import sys

input = sys.stdin.readline


# [Summary] 미국 스타일

#  킬로그램 <-> 파운드, 리터 <-> 갤런을 변환하시오.

# 1.000 킬로그램    2.2046 파운드
# 0.4536 킬로그램   1.0000 파운드
# 1.0000 리터       0.2642 갤런
# 3.7854 리터       1.0000 갤런


def main() -> None:

    # [Ideas]

    # 주어진 대로 변환하자. 단위를 확인하면 될 듯.

    ##########

    N = int(input())

    for _ in range(N):
        n, unit = input().split()
        n = float(n)

        result = 0
        if unit == "kg":
            result = n * 2.2046
            unit = "lb"
        elif unit == "lb":
            result = n * 0.4536
            unit = "kg"
        elif unit == "l":
            result = n * 0.2642
            unit = "g"
        elif unit == "g":
            result = n * 3.7854
            unit = "l"

        print(f"{result:.4f} {unit}")

    ##########

    return


# [Review]

# 젠장 모나티엄, 또 파운드를 쓰는거야?


if __name__ == "__main__":
    main()
