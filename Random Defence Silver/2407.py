# 파이썬 이새끼 ㅋㅋ

from math import comb


def main():
    N, M = map(int, input().split())
    print(comb(N, M))


if __name__ == "__main__":
    main()
