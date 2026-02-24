# Authored by : marigold2003
# Date : 2026-02-21
# Link : https://www.acmicpc.net/problem/13902


import sys

input = sys.stdin.readline


# [Summary] 개업 2

# ~ 짜장면 신장개업 ~
# 다양한 크기의 웍이 존재한다. M(1K)개의 웍은 각각 크기 Si를 갖는다.
# 짜장면 주문은 N(10K)인분 들어온다.

# 양손에 웍을 잡고 요리하는 것이 가능하다.
# 주문보다 남거나 모자라지 않고 딱 맞아떨어지게 요리할 때,
# 요리해야 하는 최소 횟수를 구하시오.


def main() -> None:

    # [Ideas]

    # 요리 한번 할 때 웍을 최대 두 개 들 수 있다.
    # 그러면, 요리 한 번 할 때 만들 수 있는 양은 두개드는 경우 + 한개드는 경우
    # 양손에 드는 모든 경우를 더해서 각각의 무게랑 따로 저장할까.

    # 그리고 그것들을 가장 적게 선택하여 N을 만들면 된다. 일단 해볼까...
    # 아, 이거 설마... 최소 가치 구하는 냅색임? 요리 한번에 value가 1이네.

    ##########

    from itertools import combinations

    N, M = map(int, input().split())
    weights_list = list(map(int, input().split()))

    weights = set(weights_list)
    for w in map(sum, combinations(weights_list, 2)):
        if w > N:
            continue
        weights.add(w)

    INF = sys.maxsize

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

    print(dp[N] if dp[N] != sys.maxsize else -1)

    ##########

    return


# [Review]

# 배열 너무 큰가? 초과날라나?
# 나네. 1차원으로 줄여야겠다.


if __name__ == "__main__":
    main()
