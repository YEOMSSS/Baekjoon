# Authored by : marigold2003
# Date : 2026-03-23
# Link : https://www.acmicpc.net/problem/25642


import sys

input = sys.stdin.readline


# [Summary] 젓가락 게임

# 한 손으로 젓가락 게임을 한다. 5손가락을 펴면 진다.
# 용태와 유진이가 펴고 있는 손가락의 개수가 주어진다. (<= 4)
# 용태가 먼저 공격한다. 유진이는 용태가 펴고 있는 손가락 수만큼 펴야 한다.
# 다음은 유진이가 공격하고, 누군가 5손가락 이상을 펴게 될 때까지 반복한다.
# 승자를 출력하시오.


def main() -> None:

    # [Ideas]

    # 시뮬레이션이네.
    # 빠르게 구현해보자.

    ##########

    yt, yj = map(int, input().split())

    while True:
        yj += yt
        if yj >= 5:
            print("yt")
            return

        yt += yj
        if yt >= 5:
            print("yj")
            return

    ##########

    return


# [Review]

# 가르기 없는 젓가락 게임은
# 젓가락 게임이 아니다!!


if __name__ == "__main__":
    main()
