"""
import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())
    slimes = list(map(int, input().split()))
    slimes.sort(reverse=True)

    result = 0

    while True:
        s1 = slimes.pop()
        if not slimes:
            print(result)
            break
        s2 = slimes.pop()
        result += s1 * s2
        slimes.append(s1 + s2)


main()
"""

# 정렬할 필요가 없었다.
import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())
    slimes = list(map(int, input().split()))

    result = 0
    current = slimes[0]

    for s in slimes[1:]:
        result += s * current
        current += s

    print(result)


main()
