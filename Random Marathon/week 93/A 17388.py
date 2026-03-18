# Authored by : marigold2003
# Date : 2026-03-11
# Link : https://www.acmicpc.net/problem/17388


import sys

input = sys.stdin.readline


# [Summary] 제목

# 3개의 입력이 들어온다.
# 만약 입력의 합이 100이 되지 않으면
# 가장 적은 입력 남긴 대학을 출력한다.


def main() -> None:

    # [Ideas]

    # sum으로 확인하고 부족하면 찾자.

    ##########

    SKH = list(map(int, input().split()))
    total = sum(SKH)

    if total >= 100:
        print("OK")
        return

    match SKH.index(min(SKH)):
        case 0:
            print("Soongsil")
        case 1:
            print("Korea")
        case 2:
            print("Hanyang")

    ##########

    return


# [Review]

# index를 안 쓰고 풀려면 dict를 써야 하겠지?


if __name__ == "__main__":
    main()
