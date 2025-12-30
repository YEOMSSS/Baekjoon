import sys

input = sys.stdin.readline

from collections import deque

nums = set(map(str, range(10)))


def main() -> None:
    string = input().rstrip()
    target = input().rstrip()
    result = ""

    for s in string:
        if s in nums:
            continue
        result += s

    print(1 if target in result else 0)


main()
