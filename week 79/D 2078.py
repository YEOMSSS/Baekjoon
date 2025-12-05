# 일종의 백트래킹이 아닌가?
# a가 더 크면 a에서 b만큼 빼주고, b가 더 크면 b에서 a만큼 빼주고.

import sys

input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

L, R = 0, 0


def func(a, b):
    global L, R

    if a == b:
        return
    if a == 1:
        R += b - 1
        return
    if b == 1:
        L += a - 1
        return
    if a > b:
        L += a // b
        func(a % b, b)
    else:
        R += b // a
        func(a, b % a)
    return


def main():
    A, B = map(int, input().split())

    func(A, B)

    print(L, R)


main()

# 재귀는 역시 python3으로.
