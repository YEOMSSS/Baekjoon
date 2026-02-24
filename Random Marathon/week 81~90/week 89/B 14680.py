# Authored by : marigold2003
# Date : 2026-02-11
# Link : https://www.acmicpc.net/problem/14680


import sys

input = sys.stdin.readline


# [Summary] 효빈이의 과외

# 주어진 N개의 행렬을 곱하여라.


def main() -> None:

    # [Ideas]

    # 선형대수학을 좀 알아야 한다.
    # matrix의 곱셈에서는 교환법칙이 성립하지 않기 때문에 순서대로 처리해도 된다.

    # 현재a행렬 col개수 == 곱할b행렬 row개수가 matrix곱셈의 기본조건이다.
    # matrix곱셈을 구현하기만 하면 끝.

    ##########

    N = int(input())
    row_A, col_A = map(int, input().split())
    matrix_A = list(list(map(int, input().split())) for _ in range(row_A))

    for _ in range(N - 1):
        row_B, col_B = map(int, input().split())
        matrix_B = list(list(map(int, input().split())) for _ in range(row_B))

        if col_A != row_B:
            print(-1)
            return

        result = [[0 for _ in range(col_B)] for _ in range(row_A)]
        for r in range(row_A):
            for i in range(col_A):
                for c in range(col_B):
                    # 본래는 r, c가 정해진 후 그 안에서 i를 정하는 게 행렬곱셈의 순서이지만 어차피 이건 코드니까
                    # r -> i -> c 순서가 되면 [i][c]를 가로로 읽게 되어 메모리 접근 효율성이 좋아져 속도가 더 빠르다.
                    result[r][c] += matrix_A[r][i] * matrix_B[i][c]

        # 곱셈이 끝난 행렬로 a행렬 갱신
        matrix_A = result
        col_A = col_B

    MOD = 1_000_000_007
    # 원소의 값은 1 <= val <= 100으로 모두 양수니까 맘놓고 MOD로 나누자.
    answer = sum(map(lambda x: sum(x) % MOD, matrix_A))
    print(answer % MOD)

    ##########

    return


# [Review]

# 오랜만에 보는 선형대수학이었다.
# 뭔가 반갑다고 해야 할지.


if __name__ == "__main__":
    main()
