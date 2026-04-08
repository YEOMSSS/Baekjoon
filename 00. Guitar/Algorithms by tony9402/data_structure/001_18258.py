import sys

input = sys.stdin.readline

from collections import deque


def main() -> None:
    N = int(input())

    Queue = deque()

    for _ in range(N):
        command = tuple(input().split())

        match command[0]:

            case "push":
                Queue.append(command[1])

            case "pop":
                if not Queue:
                    print(-1)
                    continue
                print(Queue.popleft())

            case "size":
                print(len(Queue))

            case "empty":
                if not Queue:
                    print(1)
                else:
                    print(0)

            case "front":
                if not Queue:
                    print(-1)
                    continue
                print(Queue[0])

            case "back":
                if not Queue:
                    print(-1)
                    continue
                print(Queue[-1])


main()
