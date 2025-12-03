# https://www.acmicpc.net/problem/29733

# 검사할 칸이 몇개냐? 26개.
# 위층, 옆8칸, 아래층

import sys

input = sys.stdin.readline

neighbors = [
    # 옆 8칸
    (0, -1, -1),
    (0, -1, 0),
    (0, -1, 1),
    (0, 0, -1),
    (0, 0, 1),
    (0, 1, -1),
    (0, 1, 0),
    (0, 1, 1),
    # 위 9칸
    (-1, -1, -1),
    (-1, -1, 0),
    (-1, -1, 1),
    (-1, 0, -1),
    (-1, 0, 0),
    (-1, 0, 1),
    (-1, 1, -1),
    (-1, 1, 0),
    (-1, 1, 1),
    # 아래 9칸
    (1, -1, -1),
    (1, -1, 0),
    (1, -1, 1),
    (1, 0, -1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, -1),
    (1, 1, 0),
    (1, 1, 1),
]


def main() -> None:
    R, C, H = map(int, input().split())
    cube = [[[] for _ in range(R)] for _ in range(H)]

    for z in range(H):
        for y in range(R):
            cube[z][y] = list(input().rstrip())

    result = [[[None for _ in range(C)] for _ in range(R)] for _ in range(H)]

    for z in range(H):
        for y in range(R):
            for x in range(C):

                cur = cube[z][y][x]
                if cur == "*":
                    result[z][y][x] = "*"
                    continue

                cnt = 0
                for dz, dy, dx in neighbors:
                    nz, ny, nx = z + dz, y + dy, x + dx
                    if nz >= H or nz < 0:
                        continue
                    if ny >= R or ny < 0:
                        continue
                    if nx >= C or nx < 0:
                        continue
                    if cube[nz][ny][nx] == "*":
                        cnt += 1

                result[z][y][x] = cnt % 10

    for z in range(H):
        for y in range(R):
            print("".join(map(str, result[z][y])))


main()
