import sys

input = sys.stdin.readline

from collections import Counter


def main() -> None:
    N = int(input())

    answer = 0
    for _ in range(N):
        dice = tuple(map(int, input().split()))

        dice_counter = Counter(dice)

        score = dice_counter.most_common(2)
        d1, c1 = score[0]

        if c1 == 4:
            current = 50000 + d1 * 5000
        elif c1 == 3:
            current = 10000 + d1 * 1000
        elif c1 == 2:
            d2, c2 = score[1]
            if c2 == 2:
                current = 2000 + d1 * 500 + d2 * 500
            else:
                current = 1000 + d1 * 100
        else:
            current = max(dice) * 100

        answer = max(answer, current)

    print(answer)


if __name__ == "__main__":
    main()
