# Authored by : marigold2003
# Date : 2026-02-25
# Link : https://www.acmicpc.net/problem/30822


import sys

input = sys.stdin.readline


# [Summary] USOPC 세기

# input된 string을 재배열하여 얻을 수 있는 "usopc"의 최대 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # Counter를 사용해서 u, s, o, p, c의 개수 중 가장 적은 것을 찾자.

    ##########

    N = int(input())
    string = input().rstrip()

    from collections import Counter

    string_counter = Counter(string)

    answer = 1000
    for ch in "usopc":
        if ch in string_counter:
            answer = min(answer, string_counter[ch])
        else:
            print(0)
            return

    print(answer)

    ##########

    return


# [Review]

# 간단한 char count 문제


if __name__ == "__main__":
    main()
