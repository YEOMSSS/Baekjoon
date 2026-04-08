import sys

input = sys.stdin.readline

from collections import deque


def main():
    N = int(input())

    commands = list(map(int, input().split()))[::-1]

    cards = deque()
    cards.append(1)
    for i, command in enumerate(commands[1:]):
        match command:
            case 1:
                cards.appendleft(i + 2)
            case 2:
                tmp = cards.popleft()
                cards.appendleft(i + 2)
                cards.appendleft(tmp)
            case 3:
                cards.append(i + 2)

    print(*cards)


main()
