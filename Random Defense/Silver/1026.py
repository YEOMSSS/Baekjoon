import sys

input = sys.stdin.readline

# 하나는 오름차, 하나는 내림차로 정렬하고 동일 인덱스끼리 곱하면 될 듯.


def main():
    N = int(input())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))

    arrA.sort()
    arrB.sort(reverse=True)

    result = 0
    for i in range(N):
        result += arrA[i] * arrB[i]

    print(result)


main()
