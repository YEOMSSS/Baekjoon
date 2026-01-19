import sys

input = sys.stdin.readline


def main() -> None:
    for i in range(1, int(input()) + 1):
        print(f"Case {i}: {sum(map(int, input().split()))}")


if __name__ == "__main__":
    main()
