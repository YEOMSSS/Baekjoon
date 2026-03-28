# Authored by : marigold2003
# Date : 2026-03-28
# Link : https://www.acmicpc.net/problem/35409


import sys

input = sys.stdin.readline


# [Summary] 제4회 디미고 프로그래밍 챌린지

# 06:30-09:00
# 09:50-10:00
# 10:50-11:00
# 11:50-12:00
# 12:50-13:50
# 14:40-14:50
# 15:40-15:50
# 16:40-22:50

# 시와 분이 주어질 때 위 범위 내에 있는지 판단하시오.


def main() -> None:

    # [Ideas]

    # 많은 조건 분기. shit!

    ##########

    H, M = map(int, input().split())

    def func(H, M):
        if H == 6:
            if M >= 30:
                return True
        elif H == 7:
            return True
        elif H == 8:
            return True
        elif H == 9:
            if M == 0:
                return True
            elif M >= 50:
                return True
        elif H == 10:
            if M == 0:
                return True
            if M >= 50:
                return True
        elif H == 11:
            if M == 0:
                return True
            if M >= 50:
                return True
        elif H == 12:
            if M == 0:
                return True
            if M >= 50:
                return True
        elif H == 13:
            if M <= 50:
                return True
        elif H == 14:
            if 40 <= M <= 50:
                return True
        elif H == 15:
            if 40 <= M <= 50:
                return True
        elif H == 16:
            if 40 <= M:
                return True
        elif 17 <= H <= 21:
            return True
        elif H == 22:
            if M <= 50:
                return True

        return False

    print("Yes" if func(H, M) else "No")

    ##########

    return


# [Review]

# 아 싫다... 너무싫다.


if __name__ == "__main__":
    main()
