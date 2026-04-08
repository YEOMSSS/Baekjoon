# Authored by : marigold2003
# Date : 2026-04-08
# Link : https://www.acmicpc.net/problem/14561


import sys

input = sys.stdin.readline


# [Summary] 회문

# 십진수 A를 n진수로 변환하시오.
# 그리고 그 n진수가 펠린드롬수인지 판별하시오.


def main() -> None:

    # [Ideas]

    # 이건 펠린드롬 검사보단 진법변환이 포인트네.
    # 나머지 구하기 그걸로 하자.

    ##########

    T = int(input())
    for _ in range(T):

        A, n = map(int, input().split())

        temp = []
        while A:
            temp.append(A % n)
            A //= n

        if temp == temp[::-1]:
            print(1)
        else:
            print(0)

    ##########

    return


# [Review]

# 나머지 구하는거야 뭐.
# 방법을 알고있으면 쉽다.


if __name__ == "__main__":
    main()
