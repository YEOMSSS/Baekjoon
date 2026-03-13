# Authored by : marigold2003
# Date : 2026-03-13
# Link : https://www.acmicpc.net/problem/32642


import sys

input = sys.stdin.readline


# [Summary] 당구 좀 치자 제발

# 비가 오면 분노하고 비가 안오면 분노가 감소한다.
# 매일 분노의 합을 구하시오.


def main() -> None:

    # [Ideas]

    # 분노를 변수로 관리해서 답에 매일매일 쌓아준다.

    ##########

    N = int(input())
    fury = 0

    answer = 0
    for r in map(int, input().split()):
        if r:
            fury += 1
        else:
            fury -= 1

        answer += fury

    print(answer)

    ##########

    return


# [Review]

# 시뮬레이션 느낌.


if __name__ == "__main__":
    main()
