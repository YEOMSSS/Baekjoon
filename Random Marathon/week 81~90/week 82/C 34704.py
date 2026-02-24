import sys

input = sys.stdin.readline

from collections import Counter


def main() -> None:
    N = int(input())
    items = list(map(int, input().split()))

    items_counter = Counter(items)
    result = items_counter[4] + items_counter[3] + (items_counter[2] // 2)

    rest_1 = items_counter[1] - items_counter[3]

    if items_counter[2] % 2:
        result += 1
        rest_1 -= 2

    if rest_1 < 0:
        print(result)
        return

    result += (rest_1 + 4 - 1) // 4

    print(result)


main()
