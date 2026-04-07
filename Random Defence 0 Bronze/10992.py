# Authored by : marigold2003
# Date : 2026-03-18
# Link : https://www.acmicpc.net/problem/10992


import sys

input = sys.stdin.readline


# [Summary] 별 찍기 - 17

# 별을 찍자. 규칙에 맞춰 N(<= 100)줄 출력하시오.


def main() -> None:

    # [Ideas]

    # 가운데 구멍이 뚫려있네.

    # 맨 위는 무조건 중앙에 하나,
    # 맨 밑은 무조건 N*2-1개.
    # 중간은 그냥 양끝에만 별.

    ##########

    N = int(input())
    if N == 1:
        print("*")
        return

    print(" " * (N - 1) + "*")

    for i in range(1, N - 1):
        print(" " * (N - 1 - i) + "*" + " " * (i * 2 - 1) + "*")

    print("*" * (2 * N - 1))

    ##########

    return


# [Review]

# 이제 별은 잘 찍는 나


if __name__ == "__main__":
    main()
