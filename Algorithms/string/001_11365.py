import sys

input = sys.stdin.readline


def main() -> None:
    while True:
        string = input().rstrip()
        if string == "END":
            return
        print(string[::-1])


main()
