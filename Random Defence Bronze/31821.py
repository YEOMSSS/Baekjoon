# Authored by : marigold2003
# Date : 2026-03-02
# Link : https://www.acmicpc.net/problem/31821


import sys

input = sys.stdin.readline


# [Summary] 학식 사주기

# 메뉴 N(10)개가 있고, 각각 가격은 A원이다.
# M(10)명이 각각 메뉴를 고른다.
# 결제해야 하는 금액의 총액을 출력하시오.


def main() -> None:

    # [Ideas]

    # 지들이 사먹으라하지 왜 사달라는거냐

    ##########

    N = int(input())

    menu = [int(input()) for _ in range(N)]

    answer = 0
    for _ in range(int(input())):
        answer += menu[int(input()) - 1]

    print(answer)

    ##########

    return


# [Review]

# 뇌가 휴식을 필요로 한다.
# 이런거만 평생 풀면서 살고싶다 씨발.


if __name__ == "__main__":
    main()
