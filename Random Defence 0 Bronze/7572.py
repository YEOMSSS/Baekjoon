# Authored by : marigold2003
# Date : 2026-02-02
# Link : https://www.acmicpc.net/problem/7572

import sys

input = sys.stdin.readline


# [Summary]

# 서양식으로 간지 표현하기
# 십간은 0~9로, 십이지는 "ABCDEFGHIJKL"로.
# 십이지 -> 십간 순서로 표현된다. 갑자는 A0.


def main() -> None:

    # [Ideas]

    # 일단 년도를 60으로 나눈 나머지를
    # 각각 12와 10으로 나누자.

    # 이때, 2013이 F9이며 2014가 G0이다.
    # 인덱스로 장난질하면 될듯. 0004년이 A0이다.

    ##########

    JIs = "ABCDEFGHIJKL"

    # 4년을 빼서 0으로 맞춰준다.
    year = int(input()) - 4
    year %= 60

    print(f"{JIs[year % 12]}{year % 10}")

    ##########

    return


# [Review]

# 예제가 있어 친절하다.
# 2013이 F9임을 잘 이용하면 된다.

if __name__ == "__main__":
    main()
