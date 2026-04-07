# Authored by : marigold2003
# Date : 2026-03-13
# Link : https://www.acmicpc.net/problem/1038


import sys

input = sys.stdin.readline


# [Summary] 감소하는 수

# 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소할 때,
# 그 수를 감소하는 수라고 한다.

# N번째 감소하는 수를 출력하고, 없다면 -1을 출력하시오.


def main() -> None:

    # [Ideas]

    # 9876543210이 끝이다.
    # 다 찾아서 리스트에 넣으면 되겠다.
    # 어떤 식으로 해야할까?

    ##########

    arr = [0]

    def backtrack(n):
        # 끝이 0이면 더 못 붙인다.
        arr.append(n * 10)
        # n보다 작은 애들을 1부터 붙여본다.
        for i in range(1, n % 10):
            backtrack(n * 10 + i)
            arr.append(n * 10 + i)

    for i in range(1, 10):
        arr.append(i)
        backtrack(i)

    arr.sort()

    N = int(input())
    if N >= len(arr):
        print(-1)
    else:
        print(arr[N])

    ##########

    return


# [Review]

# 진짜 쉽네 뭐냐
# 날먹 백트래킹이 쪼아요


if __name__ == "__main__":
    main()
