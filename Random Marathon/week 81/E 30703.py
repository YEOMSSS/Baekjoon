# 자신의 위치를 찾은 상태에서 더 이동해야 한다면 무조건 2회 움직여야한다.
# 각각의 움직여야 하는 횟수를 구한 후, 전부 홀수거나 전부 짝수일 때만 가능할 것.

import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())

    defaults = list(map(int, input().split()))
    targets = list(map(int, input().split()))
    changes = list(map(int, input().split()))

    result = 0

    odd_check = 0

    for i in range(N):
        change = changes[i]
        diff = abs(targets[i] - defaults[i])
        remain = diff % change
        if remain:
            print(-1)
            return

        quotient = diff // change
        result = max(result, quotient)

        cur = quotient % 2
        if not i:
            odd_check = cur
            continue
        if cur != odd_check:
            print(-1)
            return

    print(result)


main()
