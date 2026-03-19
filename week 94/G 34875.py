# Authored by : marigold2003
# Date : 2026-03-19
# Link : https://www.acmicpc.net/problem/34875


import sys

input = sys.stdin.readline


# [Summary] 자벌레 세기

# N(<= 300K)개의 정점으로 구성된 트리가 주어진다.
# 6개의 서로 다른 정점이 >-< 형태로 연결되어 있으면 자벌레라고 한다.
# 주어진 트리에 존재하는 서로 다른 자벌레의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 조합을 사용해야 한다. 순회를 굳이 돌 필요가 있을까 싶음.

    # 연결된 두 정점을 고르고, 두 정점 모두 서로를 제외한 이웃이 둘씩 있어야 한다.
    # 입력이 트리니까, 사이클 걱정 없이 개수만 잘 세면 되겠다.
    # 그리고 조합으로 수를 구해서 곱하면 될 듯.
    # 모든 인접 노드에 대해서 하면 되는데, 그게 곧 입력이 되겠다.

    # 어차피 서로 이웃이 겹칠 일이 없으니 그냥 Counter로 세자.
    # 입력된 후보들에서 1씩 빼주고 조합 굴리면 될 듯.

    # 조합은 (이웃개수-1)_C_2 로. 그러니까 (이웃개수-1)(이웃개수-2) // 2 가 되겠다.
    # 그걸 u랑 v 따로 하고 서로 곱해주면 자벌레의 개수가 된다.

    ##########

    # from collections import Counter

    # N = int(input())
    # node_to_nei_count = Counter()

    # candidates = []

    # for _ in range(N - 1):
    #     u, v = map(int, input().split())
    #     candidates.append((u, v))
    #     node_to_nei_count[u] += 1
    #     node_to_nei_count[v] += 1

    # answer = 0
    # for u, v in candidates:
    #     u_count = (node_to_nei_count[u] - 1) * (node_to_nei_count[u] - 2) // 2
    #     v_count = (node_to_nei_count[v] - 1) * (node_to_nei_count[v] - 2) // 2
    #     answer += u_count * v_count

    # print(answer)

    ##########

    N = int(input())
    node_to_nei_count = [-1] * (N + 1)

    candidates = []

    for _ in range(N - 1):
        u, v = map(int, input().split())
        candidates.append((u, v))
        node_to_nei_count[u] += 1
        node_to_nei_count[v] += 1

    answer = 0
    for u, v in candidates:
        u_count = (node_to_nei_count[u] - 1) * (node_to_nei_count[u]) // 2
        v_count = (node_to_nei_count[v] - 1) * (node_to_nei_count[v]) // 2
        answer += u_count * v_count

    print(answer)

    ##########

    return


# [Review]

# 트리에 사이클이 없다는게 무슨의미인지 이해하고 있다면
# 발상이 어렵지 않았을 것이다.
# 노드번호가 N 이하로 주어지므로 굳이 Counter를 쓸 것까진 없었을 듯.


if __name__ == "__main__":
    main()
