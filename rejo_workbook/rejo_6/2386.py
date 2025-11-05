import sys

input = sys.stdin.readline


def main():
    while True:
        string = input().rstrip()
        target = string[0]

        if target == "#":
            return

        result = string[1:].lower().count(target)
        print(target, result)


main()
