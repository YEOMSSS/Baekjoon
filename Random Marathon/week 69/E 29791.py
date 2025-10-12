import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))

    arr_A.sort()
    arr_B.sort()

    res_A = 0
    res_B = 0

    temp = -100
    for a in arr_A:
        if a < temp + 100:
            continue
        temp = a
        res_A += 1

    temp = -360
    for b in arr_B:
        if b < temp + 360:
            continue
        temp = b
        res_B += 1

    print(res_A, res_B)


if __name__ == "__main__":
    main()
