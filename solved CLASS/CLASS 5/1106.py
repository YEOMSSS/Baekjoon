# Authored by : marigold2003
# Date : 2026-02-03
# Link : https://www.acmicpc.net/problem/1106

import sys

input = sys.stdin.readline


# [Summary]

# 비용 x로 고객을 y명 부를 수 있다.
# 비용과 고객이 다양하게 입력될 때 최소 C명을 부르는 총 비용의 최솟값 구하기


def main() -> None:

    # [Ideas]

    # 이거 그리디로 안되는거임?
    # 일단 제일 싼 걸로 최대한 고객 부르고.
    # 남는칸을 채우는 가장 싼 편으로 부르면 되는거 아님?

    # 어!! 이거 아니다. 비율이 같을때 너무 애매하다.
    # 3 3이랑 5 5만 있는데 10명채우기면 5 5를 두번 골라야한다.

    # dp를 써야겠다. 냅색이네 이거. 근데 가치의 합이 최저가 되는
    # 냅색이 끝난 후 남은 고객을 어떻게 채울지만 생각해보자. 이거야말로 그리디아님?
    # 흠, 이것까지도 냅색으로 처리할 수 있을 것 같다.

    ##########

    # 목표고객수, 도시수
    C, N = map(int, input().split())
    prices = []
    customers = []
    for _ in range(N):
        price, customer = map(int, input().split())
        prices.append(price)
        customers.append(customer)

    # DP 테이블을 이용한 구현
    def knapsack(max_weight: int, weights: list[int], values: list[int]) -> int:
        n = len(weights)
        INF = float("inf")
        dp = [[INF for _ in range(max_weight + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        # 주어진 모든 원소를 확인한다.
        for i in range(1, n + 1):
            # w는 현재 칸에서 사용중인 무게이다.
            for w in range(1, max_weight + 1):
                # 현재 원소의 무게를 뺀 이전 원소까지의 최대값과 0 중 큰 것을 가져와 현재 값을 더한 값 vs 이전 값
                dp[i][w] = min(
                    dp[i - 1][w],
                    # 무게가 넘어가는 경우에도 선택할 수 있다.
                    # 중복 사용 가능하니 현재 행을 참고한다.
                    dp[i][max(0, w - weights[i - 1])] + values[i - 1],
                )

        # print(dp)
        return dp[n][max_weight]

    print(knapsack(C, customers, prices))

    ##########

    return


# [Review]

# 냅색은 정말 신기하구나.
# 2차원배열을 쓰지 않아도 될 것 같다.

if __name__ == "__main__":
    main()
