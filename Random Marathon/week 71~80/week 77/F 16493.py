import sys

input = sys.stdin.readline


# DP 테이블을 이용한 구현
def knapsack(max_weight: int, weights: list[int], values: list[int]) -> int:
    n = len(weights)

    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    # 주어진 모든 원소를 확인한다.
    for i in range(1, n + 1):
        # w는 현재 칸에서 사용중인 무게이다.
        for w in range(1, max_weight + 1):
            # 현재 원소의 무게가 현재 칸의 무게보다 같거나 적은 경우 확인한다.
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    # 현재 원소의 무게를 뺀 이전 원소까지의 최대값을 가져와 더한 값 vs 이전 값
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1],
                )
            # 현재 원소의 무게가 현재 칸에 들어올 수 없으면 이전 최댓값을 그대로 가져온다.
            else:
                dp[i][w] = dp[i - 1][w]

    # print(dp)
    return dp[n][max_weight]


def main():
    N, M = map(int, input().split())

    days = [None] * M
    pages = [None] * M

    for i in range(M):
        d, p = map(int, input().split())
        days[i] = d
        pages[i] = p

    print(knapsack(N, days, pages))


main()
