# dp[i][w]의 정의
# "배열의 [:i]만 사용해서, 합계 w를 만들 수 있는 최대(최소) value"


# 1차원 최소냅색 (value 1). 덧씌워가며 돌린다
def knapsack(weights: set[int]) -> int:
    N = len(weights)
    INF = 10**9

    # 가장 낮은 가치를 구하는 냅색(1차원)
    dp = [INF for _ in range(N + 1)]

    # 무게가 0일땐 요리를 하지 않는다.
    dp[0] = 0

    # 주어진 모든 원소를 확인한다.
    for curr in weights:
        # w는 현재 칸에서 사용중인 무게이다.
        for w in range(curr, N + 1):

            # 현재 원소의 무게를 뺀 이전 원소까지의 최솟값을 가져와 현재 값을 더한 값 vs 이전 값
            dp[w] = min(dp[w], dp[w - curr] + 1)

    return dp[N]


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
                    # 현재 원소의 무게를 뺀 이전 원소까지의 최댓값을 가져와 현재 값을 더한 값 vs 이전 값
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1],
                )
            # 현재 원소의 무게가 현재 칸에 들어올 수 없으면 이전 최댓값을 그대로 가져온다.
            else:
                dp[i][w] = dp[i - 1][w]

    # print(dp)
    return dp[n][max_weight]


# 가장 낮은 가치를 구하는 냅색
def min_knapsack(max_weight: int, weights: list[int], values: list[int]) -> int:
    n = len(weights)
    INF = float("inf")
    dp = [[INF for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    # 주어진 모든 원소를 확인한다.
    for i in range(1, n + 1):
        # w는 현재 칸에서 사용중인 무게이다.
        for w in range(1, max_weight + 1):
            # 현재 원소의 무게를 뺀 이전 원소까지의 최솟값과 0 중 큰 것을 가져와 현재 값을 더한 값 vs 이전 값
            dp[i][w] = min(
                dp[i - 1][w],
                # 무게가 넘어가는 경우에도 선택할 수 있다.
                dp[i - 1][max(0, w - weights[i - 1])] + values[i - 1],
                # 같은 물건을 중복 사용할 수 있으면 현재 행을 참고해야 한다.
                # dp[i][max(0, w - weights[i - 1])] + values[i - 1]
            )

    # print(dp)
    return dp[n][max_weight]
