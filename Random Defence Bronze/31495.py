# Authored by : marigold2003
# Date : 2026-03-03
# Link : https://www.acmicpc.net/problem/31945


import sys

input = sys.stdin.readline


# [Summary] 그게 무슨 코드니..

# 입력된 문자열의 양 끝이 "인지 판별하시오.


def main() -> None:

    # [Ideas]

    # [0]과 [-1]

    ##########

    string = input().rstrip()

    if len(string) == 1:
        print("CE")
        return

    if string[0] == '"' and string[-1] == '"':
        print(string[1:-1] if string[1:-1] else "CE")
        return

    print("CE")

    ##########

    return


# [Review]

# Hello World를 출력하고 있었네;


if __name__ == "__main__":
    main()
