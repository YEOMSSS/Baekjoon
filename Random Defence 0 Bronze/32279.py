# Authored by : marigold2003
# Date : 2026-11-27
# Link : https://www.acmicpc.net/problem/32279


import sys

input = sys.stdin.readline


# [Summary] 수열의 비밀 (Easy)

# 길이가 n인 수열 a1, a2, ..., an
# a{2i} = p * ai + q      (2 <= 2i <= n)
# a{2i+1} = r * ai + s    (3 <= 2i+1 <= n)
# Sn = a1 + a2 + ... + an

# 이 때, Sn을 가져와


def main() -> None:

    # [Ideas]

    # 구현하고 시뮬레이션할까.
    # 약간 dp라고 생각할 수도 있을것 같고.
    # 점화식이 주어진 dp 아닌가?

    ##########

    N = int(input())
    p, q, r, s = map(int, input().split())
    a1 = int(input())

    dp = [0 for _ in range(N + 2)]
    dp[1] = a1

    for i in range(1, N // 2 + 1):
        dp[2 * i] = p * dp[i] + q
        dp[2 * i + 1] = r * dp[i] + s

    print(sum(dp[: N + 1]))

    ##########

    return


# [Review]

# 은근히 어려운데? 헷갈릴 부분이 있다.


if __name__ == "__main__":
    main()
