# Authored by : marigold2003
# Date : 2026-04-26
# Link : https://www.acmicpc.net/contest/problem/1675/1


import sys

input = sys.stdin.readline


# [Summary] A번 - Good Bye, 별 찍기!

# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.


def main() -> None:

    # [Ideas]

    # 좌하로 내려긋는 대각선 하나와
    # 대각선 4개로 이루어진 마름모 하나.

    ##########

    N = int(input()) * 2
    answer = [[] for _ in range(N)]

    for i in range(N):
        temp = []
        temp.append(" " * (N - i - 1))
        temp.append("*")
        temp.append(" " * i)
        temp.append(" ")
        answer[i].extend(temp)

    for i in range(N // 2):
        temp = []
        temp.append(" " * (N // 2 - i - 1))
        temp.append("*")
        temp.append(" " * i)
        temp.append(" ")
        answer[i].extend(temp)

    for i in range(N // 2, N):
        temp = []
        temp.append(" " * (i - N // 2))
        temp.append("*")
        temp.append(" " * (N // 2 - i - 1 + N // 2))
        temp.append(" ")
        answer[i].extend(temp)

    for i in range(N // 2):
        temp = []
        temp.append(" " * i)
        temp.append("*")
        temp.append(" " * (N // 2 - i - 1))
        temp.append(" ")
        answer[i].extend(temp)

    for i in range(N // 2, N):
        temp = []
        temp.append(" " * (N // 2 - i - 1 + N // 2))
        temp.append("*")
        temp.append(" " * (i - N // 2))
        temp.append(" ")
        answer[i].extend(temp)

    for i in range(N):
        print("".join(answer[i]))

    ##########

    return


# [Review]

# /<> 을 남기고 가다


if __name__ == "__main__":
    main()
