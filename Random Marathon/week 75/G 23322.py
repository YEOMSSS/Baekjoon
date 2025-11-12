# K-i는 항상 최솟값에 닿을 수 있다.
# 그러면 모든 배열을 최솟값으로 바꿀수 있다는 거지.
# 계속 재배치가 되니까 최솟값이 아닌 모든 배열을 하루에 하나씩 바꾸면 된다.

import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    choco = list(map(int, input().split()))

    result = [0, 0]

    temp = choco[0]
    for i in range(1, N):
        if temp == choco[i]:
            continue
        result[1] = N - i
        break

    result[0] = sum(choco) - temp * N

    print(*result)


main()
