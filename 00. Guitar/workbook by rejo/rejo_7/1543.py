import sys

input = sys.stdin.readline


def main():
    string = input().rstrip()
    target = input().rstrip()

    result = string.count(target)
    print(result)


main()
