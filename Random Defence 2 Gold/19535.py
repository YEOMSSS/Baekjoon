# Authored by : marigold2003
# Date : 2026-04-07
# Link : https://www.acmicpc.net/problem/19535


import sys

input = sys.stdin.readline


# [Summary] ㄷㄷㄷㅈ

# 정점이 N(<= 300K)개인 트리가 주어진다.
# 1-2-3-4 형태로 이어지는 ㄷ 부분집합과
# 1-2, 1-3, 1-4 형태로 이어지는 ㅈ 부분집합의 개수를 센다.

# ㄷ이 ㅈ의 3배보다 많으면 D-트리
# ㄷ이 ㅈ의 3배보다 적으면 G-트리
# ㄷ이 ㅈ의 정확히 3배만큼 있으면 DUDUDUNGA-트리


def main() -> None:

    # [Ideas]

    # ㅈ은 각 정점에 연결된 정점 개수로 조합을 돌리면 된다.
    # 3개이상부터 3개선택으로 돌리면 되겠다.

    # ㄷ은 연결된 두 정점에서 서로를 제외한 연결정점을 각각 하나씩 고르면 된다.
    # 그럼 그냥 1씩 빼고 서로 곱하면 되겠다.
    # 입력에서 연결된애들이 들어오니까 그걸로 돌리면 된다.

    ##########

    from math import comb

    N = int(input())
    edges = []
    graph = [0] * (N + 1)

    for _ in range(N - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
        graph[u] += 1
        graph[v] += 1

    D = 0
    for u, v in edges:
        cu, cv = graph[u], graph[v]
        if not (cu - 1 and cv - 1):
            continue
        D += (cu - 1) * (cv - 1)

    G = 0
    for n in graph:
        if n < 3:
            continue
        G += comb(n, 3)

    G *= 3

    if D > G:
        print("D")
    elif D < G:
        print("G")
    else:
        print("DUDUDUNGA")

    ##########

    return


# [Review]

# G읒이 아니라 Ji읒 아니냐?
# 아무튼, 트리와 그래프를 잘 알고 있다면 꽤나 쉬운 문제가 될 것 같다.
# 익숙하면 빨리 풀텐데 아니라면 좀 빡셀지도


if __name__ == "__main__":
    main()
