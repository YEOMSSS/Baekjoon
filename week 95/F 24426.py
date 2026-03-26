# Authored by : marigold2003
# Date : 2026-03-26
# Link : https://www.acmicpc.net/problem/24426


import sys

input = sys.stdin.readline


# [Summary] 알고리즘 수업 - 행렬 경로 문제 3

# N*N(<= 1K) board가 주어진다.
# 오른쪽이나 아래로만 이동할 수 있다.

# 중간원소 Y가 주어질 때,
# 포함할 때의 경로의 최댓값과
# 포함하지 않을 때의 경로의 최댓값을 구하시오.


def main() -> None:

    # [Ideas]

    # matrix_path(m[][], n) {  # (1, 1)에서 (n, n)에 이르는 최고 점수를 구한다.
    #     for i <- 0 to n
    #         d[i, 0] <- 0;
    #     for j <- 1 to n
    #         d[0, j] <- 0;
    #     for i <- 1 to n
    #         for j <- 1 to n
    #             d[i, j] <- mij + max(d[i - 1, j], d[i, j - 1]);
    #     return d[n, n];
    # }

    # 근데 난 왜 bfs가 돌리고 싶지.
    # 그래도 하라는대로 합시다.

    # 기본 행렬경로 dp에서, Y를 사용해야 하는 경우는~
    # 1,1 에서 Y까지, Y부터 목적지까지를 각각 구해 더해야 한다.
    # Y를 사용하지 않는 경우는 Y에 INF 넣고 돌리면 되겠지.

    ##########

    INF = 10**18

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ty, tx = map(int, input().split())

    def dynamic(startY, startX, endY, endX):
        Ysize = endY - startY + 1
        Xsize = endX - startX + 1

        dp = [[0] * (Xsize + 1) for _ in range(Ysize + 1)]
        for y in range(Ysize + 1):
            dp[y][0] = -INF
        for x in range(Xsize + 1):
            dp[0][x] = -INF

        dp[1][1] = board[startY][startX]
        for y in range(1, Ysize + 1):
            for x in range(1, Xsize + 1):
                if x == 1 and y == 1:
                    continue

                # 위나 왼쪽 칸에서 이번 칸으로 올 수 있다.
                dp[y][x] = board[startY + y - 1][startX + x - 1] + max(
                    dp[y - 1][x], dp[y][x - 1]
                )

        return dp[Ysize][Xsize]

    # Y를 반드시 경유하는 경우의 최댓값
    start_to_Y = dynamic(0, 0, ty - 1, tx - 1)
    Y_to_end = dynamic(ty - 1, tx - 1, N - 1, N - 1)
    include_Y = start_to_Y + Y_to_end - board[ty - 1][tx - 1]

    # Y를 경유하지 않는 경우의 최댓값
    board[ty - 1][tx - 1] = -INF
    exclude_Y = dynamic(0, 0, N - 1, N - 1)

    print(include_Y, exclude_Y)

    ##########

    return


# [Review]

# dp를 함수로 정의해놓고 풀면 편하다.
# dp내부에서 인덱스를 처리할 때 주의할 것.
# 미방문 처리도 이슈가 많았다. dp의 0열과 0행은 -inf처리가 필요...
# 실제 경로가 아니라면 경유할 수 없도록 처리해줘야 한다.


if __name__ == "__main__":
    main()
