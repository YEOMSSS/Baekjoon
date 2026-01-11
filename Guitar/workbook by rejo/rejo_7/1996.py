import sys

input = sys.stdin.readline


directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def main():
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]

    result = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):

            if arr[r][c] != ".":
                result[r][c] = "*"
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or N <= nr or nc < 0 or N <= nc:
                    continue

                temp = arr[nr][nc]
                if temp == ".":
                    continue

                result[r][c] += int(temp)

            if result[r][c] >= 10:
                result[r][c] = "M"

    for r in result:
        print("".join(map(str, r)))


main()
