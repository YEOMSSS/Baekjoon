# Authored by : marigold2003
# Date : 2026-03-08
# Link : https://www.acmicpc.net/problem/1297


import sys

input = sys.stdin.readline


# [Summary] TV 크기

# TV의 대각선의 길이, 높이 : 너비 가 주어진다.
# TV의 높이와 너비를 출력하시오. 소수점은 버린다.


def main() -> None:

    # [Ideas]

    # 피타고라스로 풀어야겠지?
    # 이건 수식을 써보는게 좋겠다.

    # c**2 = ax**2 + bx**2
    # x**2 = c**2 / (a**2 + b**2)
    # x = c / (a**2 + b**2) ** 0.5
    # H = ax, W = bx

    # 이거구만

    ##########

    D, H, W = map(int, input().split())

    ratio = D / (H**2 + W**2) ** 0.5
    H *= ratio
    W *= ratio
    print(int(H), int(W))

    ##########

    return


# [Review]

# 수학을 못해 수학을


if __name__ == "__main__":
    main()
