# Authored by : marigold2003
# Date : 2026-04-06
# Link : https://www.acmicpc.net/problem/2845


import sys

input = sys.stdin.readline


# [Summary] 파티가 끝나고 난 뒤

# A와 B가 입력된다. 이후 양의 정수 5개가 들어온다.
# 각 양의 정수 - A*B를 구하시오.


def main() -> None:

    # [Ideas]

    # 해석을 하고 나니 간단한 수식이다.

    ##########

    L, P = map(int, input().split())

    answer = []
    for n in map(int, input().split()):
        answer.append(n - L * P)

    print(*answer)

    ##########

    return


# [Review]

# 파티가 많이 컸나봐.


if __name__ == "__main__":
    main()
