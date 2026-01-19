import sys

input = sys.stdin.readline


def main():
    N = int(input())
    for _ in range(N):
        string = set(list(input().rstrip()))

        result = 0
        for i in range(65, 91):
            if chr(i) in string:
                continue
            else:
                result += i

        print(result)


main()
