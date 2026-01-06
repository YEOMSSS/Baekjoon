"""
1 1 1 1 1 1
1 2 3 4 5 6
1 3 6 10 15 21
1 4 10 20 35 56
1 5 15 35 70 126
1 6 21 56 126 252

격자 경로 구하기임. n*n칸으로 한다고 생각하면 됨.
예시는 5*5의 경우다.
"""

import sys

input = sys.stdin.readline

from math import comb

MOD = 1_000_000_007


def main():
    N = int(input())
    # 밑에 쓸데없는 입력은 받을 필요가 없다.

    print(comb(2 * N, N) % MOD, N**2 % MOD)


if __name__ == "__main__":
    main()
