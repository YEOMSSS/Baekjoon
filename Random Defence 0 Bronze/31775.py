# Authored by : marigold2003
# Date : 2026-03-16
# Link : https://www.acmicpc.net/problem/31775


import sys

input = sys.stdin.readline


# [Summary] 글로벌 포닉스

# string이 3회 주어진다.
# 각각 순서에 상관없이 l, k, p로 시작하는지 검사하시오.


def main() -> None:

    # [Ideas]

    # 빨리빨리 보자.
    # set으로 검사할거임.

    ##########

    result = set()

    for _ in range(3):
        string = input().rstrip()
        result.add(string[0])

    if result == set("lkp"):
        print("GLOBAL")
    else:
        print("PONIX")

    ##########

    return


# [Review]

# 간단하게 set으로 풀었다.


if __name__ == "__main__":
    main()
