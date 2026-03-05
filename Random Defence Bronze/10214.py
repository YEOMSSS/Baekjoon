# Authored by : marigold2003
# Date : 2026-03-05
# Link : https://www.acmicpc.net/problem/10214


import sys

input = sys.stdin.readline


# [Summary] Baseball

# 야구경기의 점수표가 입력된다.
# 승자를 출력하시오.


def main() -> None:

    # [Ideas]

    # 변수 두개 만들어서 쌓지 뭐.

    ##########

    T = int(input())

    for _ in range(T):
        Y, K = 0, 0
        for _ in range(9):
            y, k = map(int, input().split())
            Y += y
            K += k

        if Y > K:
            print("Yonsei")
        elif Y == K:
            print("Draw")
        else:
            print("Korea")

    ##########

    return


# [Review]

# 손이 가는대로 구현해!


if __name__ == "__main__":
    main()
