import sys

input = sys.stdin.readline


def main():

    N = int(input())
    result = 0

    while N > 0:
        i = 1
        while N >= i:
            N -= i

            i += 1
            result += 1

    print(result)


if __name__ == "__main__":
    main()
