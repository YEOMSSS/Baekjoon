# 하나씩 집어서 긴거가 합한 스티커의의 한 변이고
# 집은 거의 나머지끼리 더한거가 합한 스티커의 나머지 변.

import sys
from itertools import combinations

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    if H < W:
        H, W = W, H
    N = int(input())

    stickers = []
    for _ in range(N):
        R, C = map(int, input().split())
        stickers.append((R, C))

    result = 0
    for s1, s2 in combinations(stickers, 2):

        for i, j in ((0, 0), (0, 1), (1, 0), (1, 1)):
            row = max(s1[i], s2[j])
            col = s1[(i + 1) % 2] + s2[(j + 1) % 2]
            if max(row, col) > H or min(row, col) > W:
                continue
            result = max(result, s1[0] * s1[1] + s2[0] * s2[1])
            break

    print(result)


if __name__ == "__main__":
    main()
