import sys

input = sys.stdin.readline


def main() -> None:
    print(sum(map(int, input().split())))


if __name__ == "__main__":
    main()
