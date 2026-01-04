import sys

input = sys.stdin.readline


def main() -> None:

    M = int(input())
    board = [0] * 4
    board[1] ^= 1

    for _ in range(M):
        X, Y = map(int, input().split())
        board[X], board[Y] = board[Y], board[X]

    for i in range(4):
        if board[i]:
            print(i)


if __name__ == "__main__":
    main()
