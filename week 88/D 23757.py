# Authored by : marigold2003
# Date : 2026-02-07
# Link : https://www.acmicpc.net/problem/23757

import sys

input = sys.stdin.readline


# [Summary]

# 선물이 몇 개 들어있는지 적혀있는 선물이 든 상자가 N개 있다.
# M명의 아이들은 현재 가장 많은 선물이 들어있는 상자에서 원하는 만큼 선물을 가져간다.
# 만약 현재 가장 많은 선물이 들어있는 상자에 원하는 만큼 선물이 없다면 실망한다.
# 모든 아이들이 실망하지 않고 선물을 가져갈 수 있을까?


def main() -> None:

    # [Ideas]

    # 시뮬레이션을 돌리면 되겠지.
    # 선물상자의 순서는 상관 없고, 가장 많이 들어있는 선물상자에서 원하는 만큼 빼기만 하면 된다.
    # 최대힙을 사용하면 되겠다.

    # pop해서 원하는 양과 비교하고, 꺼내간 만큼 뺀 후 다시 push해주면 되겠네.

    ##########

    import heapq

    N, M = map(int, input().split())

    max_heap = list(map(lambda x: -int(x), input().split()))
    heapq.heapify(max_heap)

    children = tuple(map(int, input().split()))

    for c in children:

        # 최대힙 pop해서 현재 가장 큰 선물상자 찾기
        largest = -heapq.heappop(max_heap)

        # 선물이 원하는 만큼 없다면 실망한다.
        if largest < c:
            print(0)
            return

        # 선물을 덜어내고 다시 최대힙에 push한다.
        heapq.heappush(max_heap, -(largest - c))

    print(1)

    ##########

    return


# [Review]

# 최대힙을 사용하는 기초적인 문제.
# push로 힙을 만드는 게 아니라면, heapify를 이용해 힙으로 재배치해줘야한다.

if __name__ == "__main__":
    main()
