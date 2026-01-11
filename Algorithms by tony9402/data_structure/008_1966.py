import sys

input = sys.stdin.readline

from collections import deque


def func() -> int:
    N, M = map(int, input().split())
    docs = deque(map(int, input().split()))

    count = 0
    target = M
    large = max(docs)

    while True:
        if docs[0] != large:
            docs.rotate(-1)
            if not target:
                target = len(docs) - 1
                continue
            target -= 1
            continue

        if not target:
            print(count + 1)
            break

        docs.popleft()
        count += 1
        if docs:
            large = max(docs)
            target -= 1


def main() -> None:
    N = int(input())
    for _ in range(N):
        func()


main()
