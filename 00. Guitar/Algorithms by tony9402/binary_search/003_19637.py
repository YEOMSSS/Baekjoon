# https://www.acmicpc.net/problem/19637

# 왜 이분탐색을 써야하나 했더니 칭호가 존나 많구나?
import sys

input = sys.stdin.readline


def main() -> None:
    N, M = map(int, input().split())
    title = [None for _ in range(N)]
    criterion = [None for _ in range(N)]

    for i in range(N):
        t, c = input().split()
        title[i] = t
        criterion[i] = int(c)

    # 비내림차순이 보장되고, 중복시 앞선 입력을 인정한다?
    # 이분탐색은 최좌측을 우선시하잖아.
    for i in range(M):
        score = int(input())

        left = 0
        right = N - 1

        result = 0
        while left <= right:
            mid = (left + right) // 2
            cur = criterion[mid]

            # 바로 여기에 등호가 있는 이유지. 같아도 가장 왼쪽 값으로 간다.
            if cur >= score:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        print(title[result])


main()
