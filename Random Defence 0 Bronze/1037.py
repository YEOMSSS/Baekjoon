# Authored by : marigold2003
# Date : 2026-11-20
# Link : https://www.acmicpc.net/problem/1037


import sys

input = sys.stdin.readline


# [Summary] 약수

# N의 약수 중 1과 N을 제외한 약수가 전부 입력된다.
# 그때 N을 구하여라.


def main() -> None:

    # [Ideas]

    # 제일 작은거랑 제일 큰거 곱하면 되는거 아님?

    ##########

    n = int(input())
    A = list(map(int, input().split()))

    print(max(A) * min(A))

    ##########

    return


# [Review]

# 돌아왔구나!!!!! 백준 시즌2 시작합니다


if __name__ == "__main__":
    main()
