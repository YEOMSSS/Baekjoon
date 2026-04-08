import sys

input = sys.stdin.readline

lines = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]


def main() -> None:
    string = input().rstrip()

    result = 0
    for ch in string:
        # result += [ord(ch) - ord("A")]
        result += lines[ord(ch) - 65]
        result %= 10

    if result % 2:
        print("I'm a winner!")
    else:
        print("You're the winner?")


main()
