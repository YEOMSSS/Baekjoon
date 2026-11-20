# Authored by : marigold2003
# Date : 2026-11-20
# Link : https://www.acmicpc.net/problem/9251


import sys

input = sys.stdin.readline


# [Summary] LCS

# 두 수열이 주어졌을 때,
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾고 그 길이를 반환하라.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK이다.


def main() -> None:

    # [Ideas]

    # LIS랑 비슷하게 생긴 것이 dp를 쓸 것 같긴 하다.
    # 점화식이라는 놈은, 확실히 알면 참 쉽다.

    # 어떤 식으로 dp 테이블을 짜야 할까?
    # 일단, 문자열 1을 기준으로 잡고 생각하자.
    # 그리고 문자열 2의 앞 char부터 문자열 1의 모든 char와 각각 비교하는 것이다.
    # 같을 때 1로 갱신해주는 것으로 시작하자. 거기서부터 이후 전부 1이 된다.
    # 왜냐면 부분수열은 끊길 수 있기 때문에, 앞에서 한번 겹치면 뒤도 다 겹친다.

    # 문자열 2의 두 번째 ch부터는, dp의 윗 줄을 사용해야 한다.
    # 문자열 2의 ch가 문자열 1의 어떤 ch와 같다면,
    # 그 윗 줄을 확인했을 때 이미 1이 쌓여 있는 경우 부분문자열 길이를 2로 +1해주면 된다.

    # 정리하자면, dp테이블은 문자열 2의 길이를 하나씩 늘려간다고 생각하면 되겠다.
    # 그런 방식으로 한줄씩 늘려 가는 것이다.

    # 음, 동일한 경우를 처리할 때 현재 문자열 2의 행을 볼 필요 없이
    # 그냥 그 이전 행에서 이전 칸을 봐도 아무 문제가 없다.
    # 그러니까, 현재까지의 최대 lcs에 1을 더해주면 되는 것이다.

    # dp[i][j]는 w1의 i번까지의 문자열과 w2의 j번까지의 문자열의 lcs 길이가 된다.

    # 동일하지 않은 경우는 어떻게 처리해야 할까?
    # 관점에 따라 dp[i][j]는 w1에 하나 더 추가한 것일수도, w2에 하나 더 추가한 것일수도 있다.
    # 그렇기 때문에 i-1과 j-1을 한 dp값을 좌, 상에서 가져와 큰 값을 사용하면 된다.

    ##########

    w1 = input().rstrip()
    w2 = input().rstrip()

    n1 = len(w1)
    n2 = len(w2)

    dp = [[0 for j in range(n1 + 1)] for i in range(n2 + 1)]

    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if w1[j - 1] == w2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n2][n1])

    ##########

    return


# [Review]

# 역시 dp는 여전히 어려우시다.


if __name__ == "__main__":
    main()
