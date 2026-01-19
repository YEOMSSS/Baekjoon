import sys

input = sys.stdin.readline


def main():
    A, B = input().split()

    result = 0

    lenA, lenB = len(A), len(B)

    for i in range(lenA):
        for j in range(lenB):
            result += int(A[i]) * int(B[j])

    print(result)
    return


main()
