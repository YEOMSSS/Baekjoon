# set은 파이썬이 편해
import sys

input = sys.stdin.readline

mo = set(["a", "e", "i", "o", "u"])


def main():
    string = input().rstrip()
    result = 0
    for char in string:
        if char in mo:
            result += 1
    print(result)


main()
