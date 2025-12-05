import sys

input = sys.stdin.readline

from math import gcd, lcm


def main() -> None:
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())

        print(lcm(a, b), gcd(a, b))


main()
