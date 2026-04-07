import sys

input = sys.stdin.readline

from collections import Counter


def main() -> None:
    N = int(input())

    answer = 0
    for _ in range(N):
        dice = tuple(map(int, input().split()))

        dice_counter = Counter(dice)

        score = dice_counter.most_common(1)
        d, c = score[0]

        if c == 3:
            current = 10000 + d * 1000
        elif c == 2:
            current = 1000 + d * 100
        else:
            current = max(dice) * 100

        answer = max(answer, current)

    print(answer)


if __name__ == "__main__":
    main()
