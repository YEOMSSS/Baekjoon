# Authored by : marigold2003
# Date : 2026-02-19
# Link : https://www.acmicpc.net/problem/11034


import sys

input = sys.stdin.readline


# [Summary] 캥거루 세마리2

# 수직선이 하나 있고 캥거루가 세 마리 있다.
# 바깥 캥거루 둘 중 하나가 나머지 캥거루 사이로 이동하는 것이 이동 1회다.
# 한 좌표 위에 캥거루가 두 마리일 수 없다.
# 이동 횟수는 최대 몇 회인가?


def main() -> None:

    # [Ideas]

    # 12사이 거리랑 23사이 거리 중 더 긴 게 답이 된다.
    # 한칸씩만 들어가면 되니까.

    ##########

    while True:
        data = input()
        if not data:
            return

        A, B, C = map(int, data.split())

        print(max(C - B, B - A) - 1)

    ##########

    return


# [Review]

# 마음이 편안해지는 greedy


if __name__ == "__main__":
    main()
