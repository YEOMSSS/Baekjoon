# Authored by : marigold2003
# Date : 2026-02-07
# Link : https://www.acmicpc.net/problem/25601


import sys

input = sys.stdin.readline


# [Summary]

# 간선의 정보가 들어온다. 부모와 자식이 존재한다.
# N개의 정점과 N-1개의 간선이 있다.
# 두 정점이 주어졌을 때, 둘이 조상-자식 관계인지 확인하라.


def main() -> None:

    # [Ideas]

    # 자식->부모로 간선의 방향을 정해 만들어보자.
    # 그러면 입력된 정점 중 하나에서 시작해서 다른 것을 만나면 성공하게 될 듯.
    # 그러니까, 트리를 거꾸로 만들면 될 것 같은데?

    # 다중 상속은 지원하지 않는다 = 모든 자식 노드의 부모는 하나

    ##########

    N = int(input())
    name_to_idx = dict()
    graph = [None for _ in range(N)]

    # 인덱스 변환, 그래프 생성
    for _ in range(N - 1):
        child, parent = input().split()

        # child key검사 후 index 변환
        if child not in name_to_idx:
            i = len(name_to_idx)
            name_to_idx[child] = i

        # parent key검사 후 index 변환
        if parent not in name_to_idx:
            i = len(name_to_idx)
            name_to_idx[parent] = i

        graph[name_to_idx[child]] = name_to_idx[parent]

    # node가 부모로 올라가면서 target을 발견하면 True를 반환
    def check(node, target):

        while True:
            # 더 이상 부모가 없다면 탐색 실패
            # is None으로 정확히 확인해야 한다. not 사용시 인덱스 0과 혼동 가능
            if graph[node] is None:
                return False

            node = graph[node]
            if node == target:
                return True

    n1, n2 = map(lambda x: name_to_idx[x], input().split())

    print(1 if check(n1, n2) or check(n2, n1) else 0)

    ##########

    return


# [Review]

# 트리를 뒤집어보자.
# 부모가 하나라 좋으시겠어요. 뭐?

if __name__ == "__main__":
    main()
