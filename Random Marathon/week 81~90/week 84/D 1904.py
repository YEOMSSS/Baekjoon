# 타일링 문제다!
# 맨 끝은 항상 00 아니면 1이다.

"""
1   1
2   00          11
3   100         001 111
4   0000 1100   1001 0011 1111
dp[n-1] + dp[n-2] = dp[n]이 된다.
"""

MOD = 15746


def main() -> None:
    N = int(input())

    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1

    for n in range(2, N + 1):
        dp[n] = (dp[n - 1] + dp[n - 2]) % MOD

    print(dp[-1])


if __name__ == "__main__":
    main()
