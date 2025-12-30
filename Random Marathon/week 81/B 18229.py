import sys

input = sys.stdin.readline


def main() -> None:
    N, M, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    currents = [0 for _ in range(N)]

    for m in range(M):
        for n in range(N):
            currents[n] += arr[n][m]
            if currents[n] >= K:
                print(n + 1, m + 1)
                return


main()
