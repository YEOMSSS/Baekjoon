# Authored by : marigold2003
# Date : 2026-02-24
# Link : https://www.acmicpc.net/problem/15681


import sys

input = sys.stdin.readline


# [Summary] 트리와 쿼리

# edge에 weight와 direction이 없는 임의의 root 있는 tree가 주어진다.
# node U를 root로 하는 subtree에 속한 node의 수를 출력하시오.


def main() -> None:

    # [Ideas]

    # weight와 direction이 없는 tree라.
    # cycle이 없는 graph라고 생각하고 풀어보자.

    # Q가 여러개 들어오니까, 받을 때마다 순회에서는 답이 없고...
    # 미리 순회를 다 해두던가 해야겠는데. node는 max 10K니까 가능.

    # 아무튼 tree니까, parent는 반드시 하나뿐이고.
    # leaf node들에서 시작해서 root로 타고 올라가야겠다.
    # 그러면 child들의 subtree size를 더한 게 parents의 size가 될 거고.
    # 오... dp의 냄새가 난다. tree dp가 이런거였나...

    ##########

    N, R, Q = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        U, V = map(int, input().split())
        graph[U].append(V)
        graph[V].append(U)

    # stack으로 dfs 순회 순서 찾기
    stack = []
    visited = [False] * (N + 1)

    stack.append(R)
    visited[R] = True

    parents = [0] * (N + 1)
    order = []

    while stack:
        curr = stack.pop()

        # dfs에 visited된 order를 기록해둔다.
        order.append(curr)

        for nei in graph[curr]:
            # 무방향으로 저장되어 있기 때문에 visited가 필요
            if visited[nei]:
                continue

            # parents가 누구였는지 기록해둔다.
            parents[nei] = curr
            visited[nei] = True
            stack.append(nei)

    # order를 역순으로 돌리면 dp효과를 낼 수 있다. postorder 느낌으로.
    # 깊은 node부터 parent에 subtree size를 더해주면 됨.

    # 기본적으로 subtree의 size는 자신을 포함한다.
    size = [1] * (N + 1)

    # root는 빼도 되지만, 굳이 list를 dup할 필요가 없으니 그냥 넣자.
    for curr in reversed(order):
        size[parents[curr]] += size[curr]

    answers = []
    for _ in range(Q):
        q = int(input())
        answers.append(str(size[q]))

    print("\n".join(answers))

    ##########

    return


# [Review]

# 굉장히 교육적인 문제네.
# 좀 더 일찍 접했어도 좋겠다.

# 문제에서는 recursion을 소개했지만, 난 stack이 더 편하드라


if __name__ == "__main__":
    main()
