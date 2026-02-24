import sys

input = sys.stdin.readline

"""
000
011
011

모든 중심에 대하여 우측하단으로 2*2가 생기는지 확인하자.
"""

direction = ((0, 1), (1, 0), (1, 1))


def main() -> None:
    N, M = map(int, input().split())
    arr = [list(map(int, input().rstrip())) for _ in range(N)]

    for y in range(N - 1):
        for x in range(M - 1):

            # 중심이 혈관이 아니면 스킵
            if not arr[y][x]:
                continue

            # True면 종양이 있는 것.
            flag = True
            for dy, dx in direction:
                ny, nx = y + dy, x + dx

                # 0이 하나만 나와도 이 중심 기준으로는 종양이 없다.
                if not arr[ny][nx]:
                    flag = False

            if flag:
                print(1)
                return

    print(0)


if __name__ == "__main__":
    main()
