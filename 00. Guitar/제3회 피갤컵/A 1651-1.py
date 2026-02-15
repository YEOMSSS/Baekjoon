# Authored by : marigold2003
# Date : 2026-02-15
# Link : https://www.acmicpc.net/contest/problem/1651/1


import sys

input = sys.stdin.readline


# [Summary] A번 - 피갤컵 들어왔으면 이 글부터 봐라

# string이 주어진다.
# eagle이 string 안에 포함되도록 string 내부의 ch를 바꿔야 한다.
# 최소 몇 개의 ch를 바꿔야 하는지 구하시오.


def main() -> None:

    # [Ideas]

    # 다섯칸을 만드는 모든 경우를 eagle과 비교하자.

    ##########

    N = int(input())
    string = input().rstrip()

    answer = 0

    for i in range(N - 4):
        count = 0
        for j, ch in enumerate("eagle"):
            if string[i + j] == ch:
                count += 1
        answer = max(answer, count)

    print(5 - answer)

    ##########

    return


# [Review]

# 산뜻한 시작


if __name__ == "__main__":
    main()
