# 이기는 방법은 단 하나뿐. 정렬된게 들어와서 에르맥이 바꾸고, 이후 아이작이 한번 바꿔서 해결되는 경우뿐이다.
# 그런데 정렬된 상태로 시작할 수는 없는데? 그건 0이란 말이지.
# 정렬되지 않았으며 에르맥이 바꿔야만 하는 경우가 존재하는가?
# 1 0 이 들어올 때. 에르맥은 건들지 않을수밖에 없다.

import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())
    nums = list(map(int, input().split()))

    diff = 0
    for i, num in enumerate(nums):
        if i != num:
            diff += 1

    M = int(input())
    for _ in range(M):
        x, y = map(int, input().split())
        if x == y:
            if N == 2 and diff == 2:
                print(1, end=" ")
            elif diff == 0:
                print(0, end=" ")
            else:
                print(-1, end=" ")
            continue
        if nums[x] == x and x != nums[y]:
            diff += 1
        if nums[y] == y and x != nums[y]:
            diff += 1
        if nums[x] != x and nums[y] == x:
            diff -= 1
        if nums[y] != y and nums[x] == y:
            diff -= 1

        nums[x], nums[y] = nums[y], nums[x]

        if N == 2 and diff == 2:
            print(1, end=" ")
        elif diff == 0:
            print(0, end=" ")
        else:
            print(-1, end=" ")


main()
