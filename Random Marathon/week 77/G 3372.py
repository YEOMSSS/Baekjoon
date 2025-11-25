def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    # 오른쪽, 아래쪽으로만 갈 수 있기 때문에 위에서 아래로 읽어도 상관없다.
    for row in range(N):
        for col in range(N):
            # 방문했는데 dp가 0이면 여기로는 올 일 없으니 패스
            if not dp[row][col]:
                continue
            # 보드가 0이면 이동불가이니 패스. 종착점.
            if not board[row][col]:
                continue
            # 오른쪽
            if col + board[row][col] < N:
                dp[row][col + board[row][col]] += dp[row][col]
            # 아래쪽
            if row + board[row][col] < N:
                dp[row + board[row][col]][col] += dp[row][col]

    print(dp[N - 1][N - 1])


main()
