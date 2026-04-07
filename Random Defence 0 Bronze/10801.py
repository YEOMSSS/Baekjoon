# Authored by : marigold2003
# Date : 2026-03-10
# Link : https://www.acmicpc.net/problem/10801


import sys

input = sys.stdin.readline


# [Summary] 카드게임

# 두 사람 A와 B가 카드게임을 한다.
# 한 라운드에 카드 한 장을 내서 더 높은 카드를 낸 사람이 이긴다.

# 10게임을 해서 더 많이 이긴 사람이 누구인지 출력하시오.
# 무승부일 경우 D를 출력한다.


def main() -> None:

    # [Ideas]

    # 다 비교해보지 뭐.

    ##########

    A = map(int, input().split())
    B = map(int, input().split())

    answer = 0

    # zip으로 편하게 하나씩 뽑자.
    for a, b in zip(A, B):
        if a > b:
            answer += 1
        elif a < b:
            answer -= 1

    if answer > 0:
        print("A")
    elif answer < 0:
        print("B")
    else:
        print("D")

    ##########

    return


# [Review]

# 아는 게 많아질수록 브론즈 풀이가 빨라진다.


if __name__ == "__main__":
    main()
