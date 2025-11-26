import sys

input = sys.stdin.readline


def main():
    R, C = map(int, input().split())

    arr = [None] * R

    for i in range(R):
        arr[i] = input().rstrip()[::-1][1:]

    result = [0] * 10
    rank = 1
    for i in range(C - 2):
        check = 0
        for j in range(R):
            current = arr[j][i]
            if current == ".":
                continue
            if result[int(current)]:
                continue
            result[int(current)] = rank
            check = 1
        if check:
            rank += 1

    print("\n".join(map(str, result[1:])))


main()
