import sys

input = sys.stdin.readline

win = ("RS", "SP", "PR")
lose = ("RP", "PS", "SR")


def func(p1: str, p2: str) -> int:
    if p1 == p2:
        return 0

    if p1 + p2 in win:
        return 1

    if p1 + p2 in lose:
        return -1


def main() -> None:
    T = int(input())

    for _ in range(T):
        result = 0

        n = int(input())
        for _ in range(n):
            p1, p2 = input().split()
            result += func(p1, p2)

        if result > 0:
            print("Player 1")
        elif result == 0:
            print("TIE")
        else:  # count < 0
            print("Player 2")


if __name__ == "__main__":
    main()
