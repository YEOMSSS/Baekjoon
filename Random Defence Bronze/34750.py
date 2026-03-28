# Authored by : marigold2003
# Date : 2026-03-28
# Link : https://www.acmicpc.net/problem/34750


import sys

input = sys.stdin.readline


# [Summary] 추석은 언제나 좋아

# 받은 금액이 1M 이상일 경우 금액의 20% 제
# 받은 금액이 500K 이상일 경우 금액의 15% 제
# 받은 금액이 100K 이상일 경우 금액의 10% 제
# 받은 금액이 100K 미만일 경우 금액의 5% 제

# 받은 금액이 주어질 때, 제한 금액과 남는 금액을 출력하시오.


def main() -> None:

    # [Ideas]

    # 많은? 적당한 조건 분기.

    ##########

    N = int(input())

    if N >= 10**6:
        temp = N // 100 * 20
    elif N >= 5 * 10**5:
        temp = N // 100 * 15
    elif N >= 10**5:
        temp = N // 100 * 10
    else:
        temp = N // 100 * 5

    print(temp, N - temp)

    ##########

    return


# [Review]

# 내가 받은 세벳돈은 다 어디로 갔을까?
# 내가 모은 명절 용돈은 전부 어디에 사라져 있는 걸까?


if __name__ == "__main__":
    main()
