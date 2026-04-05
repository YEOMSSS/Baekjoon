# Authored by : marigold2003
# Date : 2026-04-02
# Link : https://www.acmicpc.net/problem/1269


import sys

input = sys.stdin.readline


# [Summary] 대칭 차집합

# 원소가 200K개 이하인 집합 A, B가 있다.
# (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.
# A와 B의 대칭 차집합의 원소의 개수를 출력하시오.


def main() -> None:

    # [Ideas]

    # set으로 하면 되려나? ㅇㅇ.

    ##########

    A, B = map(int, input().split())
    Aset = set(map(int, input().split()))
    Bset = set(map(int, input().split()))

    AmB = Aset - Bset
    BmA = Bset - Aset

    print(len(AmB) + len(BmA))

    ##########

    return


# [Review]

# 집합은 영어로 set!!!


if __name__ == "__main__":
    main()
