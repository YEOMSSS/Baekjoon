"""
import sys

input = sys.stdin.readline


def main():
    string = list(input().rstrip())

    string.sort(reverse=True)

    for char in string:
        print(char, end="")

if __name__ == "__main__":
    main()
"""

for char in sorted(list(input().rstrip()), reverse=True):
    print(char, end="")
