# Authored by : marigold2003
# Date : 2026-02-15
# Link : https://www.acmicpc.net/problem/3034


import sys

input = sys.stdin.readline


# [Summary] 앵그리 창영

# 성냥을 상자에 넣어야 한다.
# N개의 성냥이 있으며, 상자의 크기는 가로 W에 세로 H다.
# 상자의 밑면에 성냥이 모두 닿아야 넣을 수 있다.
# 각 성냥이 상자에 들어갈 수 있을지 없을지 알아내시오.


def main() -> None:

    # [Ideas]

    # 피타고라스 정리를 사용하면 된다.
    # 성냥의 길이가 상자 밑면 대각선의 길이보다 길면 넣을 수 없다.

    # 루트 쓰기 싫으니까 그냥 다 제곱해서 굴리자.

    ##########

    N, W, H = map(int, input().split())

    check = W * W + H * H

    for _ in range(N):
        stick = (int(input())) ** 2

        print("DA" if stick <= check else "NE")

    ##########

    return


# [Review]

# 오랜만에 앵그리버드 하고싶네.


if __name__ == "__main__":
    main()
