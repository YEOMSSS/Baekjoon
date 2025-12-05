import sys
from collections import deque

input = sys.stdin.readline


def main() -> None:
    N = int(input())
    value_DQ = deque(list(map(int, input().split())))
    index_DQ = deque(range(1, N + 1))

    while value_DQ:
        cur = value_DQ.popleft()

        if cur > 0:
            value_DQ.rotate(-cur + 1)
            print(index_DQ.popleft(), end=" ")
            index_DQ.rotate(-cur + 1)

        else:
            value_DQ.rotate(-cur)
            print(index_DQ.popleft(), end=" ")
            index_DQ.rotate(-cur)


main()
