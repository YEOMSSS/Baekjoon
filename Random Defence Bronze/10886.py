import sys

input = sys.stdin.readline

from collections import Counter


def main() -> None:
    lst = [int(input()) for _ in range(int(input()))]
    lst_counter = Counter(lst)

    if lst_counter[1] > lst_counter[0]:
        print("Junhee is cute!")
    else:
        print("Junhee is not cute!")


if __name__ == "__main__":
    main()
