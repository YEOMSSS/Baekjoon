# Authored by : marigold2003
# Date : 2026-02-21
# Link : https://www.acmicpc.net/problem/24416


import sys

input = sys.stdin.readline


# [Summary] 알고리즘 수업 - 피보나치 수 1

# 재귀호출과 dp의 비용 차이를 테스트해보자.
# 코드1과 코드2의 실행횟수를 각각 출력하시오.


def main() -> None:

    # [Ideas]

    # 재귀는 그 피보나치수가 답이다. 오 신기한데?
    # dp는 처음에 1 1 넣고 시작하니까 N-2회임.

    ##########

    N = int(input())

    fibonacci = [0] * (N + 1)
    fibonacci[1], fibonacci[2] = 1, 1

    for i in range(2, N + 1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

    print(fibonacci[N], N - 2)

    ##########

    return


# [Review]

# 피보나치 햄은 대체 어떤 사람이었을까.


if __name__ == "__main__":
    main()
