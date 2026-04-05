# Authored by : marigold2003
# Date : 2026-04-05
# Link : https://www.acmicpc.net/problem/15805


import sys

input = sys.stdin.readline


# [Summary] 트리 나라 관광 가이드

# 트리를 dfs로 순회한 경로가 N(200K)개 주어진다.
# 노드의 개수와 각 노드의 부모를 출력하시오.


def main() -> None:

    # [Ideas]

    # 그래서 방문할 도시를 최소한으로 하는 패키지 상품을 짜서 투어를 진행해왔다
    # 이 표현을 난 dfs라고 해석했다. 실제로도 맞는거같고.

    # 무방향 트리잖아. 그럼 루트가 없는거 아니냐?
    # 편하게 시작하는걸 루트로 잡고 가지 뭐.

    # 그렇다면 visited를 잘 관리해주면 되겠는데?
    # dfs로 들어가면 무조건 자기 전이 부모가 되잖아.
    # 방문하지 않은 노드는 이전노드가 부모가 된다. ok

    ##########

    N = int(input())
    paths = list(map(int, input().split()))

    size = len(set(paths))
    parents = [None] * size
    parents[paths[0]] = -1

    prev = paths[0]
    for i in range(1, N):
        curr = paths[i]
        if parents[curr] is not None:
            prev = curr
            continue

        parents[curr] = prev
        prev = curr

    print(size)
    print(*parents)

    ##########

    return


# [Review]

# 내 직관이 맞았으면 좋겠구만.
# 그래도 그래프는 꽤나 익숙해졌구나 싶긴하다.
# 굳이 방문배열을 따로 만들 필요는 없네. 퉁치면 된다.


if __name__ == "__main__":
    main()
