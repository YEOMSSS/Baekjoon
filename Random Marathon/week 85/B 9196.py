import sys

input = sys.stdin.readline


arr = []

for w in range(1, 151):
    for h in range(1, 151):
        if w <= h:
            continue
        arr.append((h, w))

arr.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2, x[0]))


def main() -> None:
    while True:
        h, w = map(int, input().split())
        if not h and not w:
            return

        print(*arr[arr.index((h, w)) + 1])


if __name__ == "__main__":
    main()
