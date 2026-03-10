# Authored by : marigold2003
# Date : 2026-03-10
# Link : https://www.acmicpc.net/problem/28281


import sys

input = sys.stdin.readline


# [Summary] 선물

# i번째 날 양말의 가격은 Ai 원이다.
# 연속된 이틀에 걸쳐 시장에서 양말을 X개씩 사올 것이다.
# N일 안에 연속한 이틀에 걸쳐 양말 2X개를 사는 데 드는 최소 비용을 구하시오.


def main() -> None:

    # [Ideas]

    # 생긴 건 무슨 슬라이딩윈도우네.
    # 누적합으로도 할 수 있을거같은데?

    ##########

    N, X = map(int, input().split())
    prices = list(map(int, input().split()))
    for i in range(N - 1):
        prices[i] += prices[i + 1]

    prices.pop()
    answer = min(prices) * X

    print(answer)

    ##########

    return


# [Review]

# 어떤 식으로 풀어야 잘 풀었다고 소문이 날까.


if __name__ == "__main__":
    main()
