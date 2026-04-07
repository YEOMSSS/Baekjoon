# Authored by : marigold2003
# Date : 2026-04-06
# Link : https://www.acmicpc.net/problem/2083


import sys

input = sys.stdin.readline


# [Summary] 럭비

# 나이가 17세보다 많거나, 몸무게가 80kg 이상이면 성인부이다.
# 그 밖에는 모두 청소년부이다. 입력을 구분하시오.


def main() -> None:

    # [Ideas]

    # 입력을 받고 if or로 처리한다.

    ##########

    while True:
        info = list(input().split())
        if info == ["#", "0", "0"]:
            return

        age, wei = int(info[1]), int(info[2])

        if age > 17 or wei >= 80:
            print(info[0], "Senior")
        else:
            print(info[0], "Junior")

    ##########

    return


# [Review]

# 럭비 너무 빡셈


if __name__ == "__main__":
    main()
