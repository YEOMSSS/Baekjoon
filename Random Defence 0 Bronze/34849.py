# Authored by : marigold2003
# Date : 2026-04-11
# Link : https://www.acmicpc.net/problem/34849


import sys

input = sys.stdin.readline


# [Summary] 이중 반복문

# 초당 10**8회 연산 가능한 컴퓨터가 있다.
# N이 주어질 때, N**2회 연산을 1초 안에 실행 가능한지 판단하시오.


def main() -> None:

    # [Ideas]

    # 제곱하고 판별하자.

    ##########

    N = int(input())

    print("Accepted" if N**2 <= 10**8 else "Time limit exceeded")

    ##########

    return


# [Review]

# 아, PS만 하고싶다. 교양 듣기 싫어~~


if __name__ == "__main__":
    main()
