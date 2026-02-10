"""
#include <stdio.h>

int main(void)
{
    int N, T;
    scanf("%d %d", &N, &T);

    N--;
    int px, ph;
    scanf("%d %d", &px, &ph);

    while (N--)
    {
        int x, h;
        scanf("%d %d", &x, &h);
    }
}
"""

# 아니 정렬까지 섞는건 에바

import sys

input = sys.stdin.readline


def main():
    N, T = map(int, input().split())

    board = []

    for _ in range(N):
        x, h = map(int, input().split())
        board.append((x, h))

    board.sort()

    result = 0

    px, ph = board[0]
    high = ph

    for x, h in board[1:]:
        shadow = high - (x - px) * T

        if shadow < 0:
            shadow = 0

        if 0 < shadow:
            result += min(shadow, h)

        # 이 발상이 어렵네.
        high = max(shadow, h)
        px = x

    print(result)


main()
