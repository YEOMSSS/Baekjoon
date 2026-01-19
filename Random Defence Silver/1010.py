# M개에서 N개를 집는 조합의 개수.
# mCn =(m-1)Cn + (m-1)C(n-1)

"""
def func():
    N, M = map(int, input().split())

    result = 1
    for i in range(M - N + 1, M + 1):
        result *= i

    for i in range(1, N + 1):
        result //= i

    print(result)


def main():
    T = int(input())

    for _ in range(T):
        func()


if __name__ == "__main__":
    main()
"""

# dp[m][n]으로 저장해보자.
dp = [[0 for _ in range(i + 1)] for i in range(30)]

for i in range(1, 30):
    dp[i][1] = i
    dp[i][i] = 1
    for j in range(2, i):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(dp[M][N])


if __name__ == "__main__":
    main()

# 파이썬이니까 comb날먹가능
"""
from math import comb


def main():
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        print(comb(M, N))


if __name__ == "__main__":
    main()
"""
