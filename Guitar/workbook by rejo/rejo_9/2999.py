import sys

input = sys.stdin.readline


def main():
    string = input().rstrip()
    length = len(string)

    row = 0
    for i in range(1, int(length**0.5) + 1):
        if length % i:
            continue
        row = i
    col = length // row

    for i in range(row):
        for j in range(col):
            print(string[j * row + i], end="")


main()
