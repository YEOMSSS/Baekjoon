# Authored by : marigold2003
# Date : 2026-03-25
# Link : https://www.acmicpc.net/problem/10768


import sys

input = sys.stdin.readline


# [Summary] 특별한 날

# 입력받은 월 일이
# 2월 18일 이전인지 확인하시오.


def main() -> None:

    # [Ideas]

    # 일단 월에서 컷하고.
    # 동일월일 시 일에서 컷하면 된다.

    ##########

    M = int(input())
    D = int(input())

    if M < 2:
        print("Before")
    elif M > 2:
        print("After")
    else:  # M == 2
        if D < 18:
            print("Before")
        elif D > 18:
            print("After")
        else:  # D == 18
            print("Special")

    ##########

    return


# [Review]

# 뇌가 말랑말랑


if __name__ == "__main__":
    main()
