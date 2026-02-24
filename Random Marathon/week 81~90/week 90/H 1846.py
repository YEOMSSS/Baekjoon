# Authored by : marigold2003
# Date : 2026-02-23
# Link : https://www.acmicpc.net/problem/1846


import sys

input = sys.stdin.readline


# [Summary] 장기

# N(100K)개의 차를 경로가 겹치지 않도록 N*N board에 배치하시오.
# 다만, 대각선이 지나는 칸에는 차가 위치할 수 없다.


def main() -> None:

    # [Ideas]

    # 괜히 장기가 어쩌구 차가 어쩌구 하는데,
    # 그냥 i번째에 i, abs(N-i) 가 안오게 1~N 을 배치하는 문제다.

    # 그림으로 그려보니까, 반으로 갈라서 생각하면 된다.
    # 1줄에 못놓는걸 2줄에 놓는걸 반복,
    # N//2줄에 못놓는 가운데는 1줄에 놓으면 된다.

    ##########

    N = int(input())

    if N == 3:
        print(-1)
        return

    front_half = range(1, N // 2 + 1)
    back_half = range(N // 2 + 1, N + 1)

    print(front_half[-1])
    for i in front_half[:-1]:
        print(i)
    print(back_half[-1])
    for i in back_half[:-1]:
        print(i)

    ##########

    return


# [Review]

# 멘사퀴즈 푸는거같네.


if __name__ == "__main__":
    main()
