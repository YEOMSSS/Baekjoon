# Authored by : marigold2003
# Date : 2026-03-23
# Link : https://www.acmicpc.net/problem/7571


import sys

input = sys.stdin.readline


# [Summary] 점 모으기

# N*N(<= 10K) board가 있다.
# M(<= 100K)개의 좌표가 들어온다.

# 임의의 좌표를 정해 각 M개의 좌표의 맨해튼 거리의 총합을 구한다.
# 그 최솟값을 출력하시오.


def main() -> None:

    # [Ideas]

    # 이 문제는 생각보다 간단하다.
    # x열 중간값과 y열 중간값이 우리가 찾고 있는 좌표가 된다.
    # 정렬하고 중간값만 뽑아내면 끝.
    # N의 홀짝도 상관없다. 세상에나.

    ##########

    x_coords = []
    y_coords = []

    N, M = map(int, input().split())
    for _ in range(M):
        x, y = map(int, input().split())
        x_coords.append(x)
        y_coords.append(y)

    x_coords.sort()
    y_coords.sort()

    mid_x = x_coords[M // 2]
    mid_y = y_coords[M // 2]

    answer = 0
    for x, y in zip(x_coords, y_coords):
        answer += abs(x - mid_x)
        answer += abs(y - mid_y)

    print(answer)

    ##########

    return


# [Review]

# 발상만 하면 뭐, 아무것도 아니긴 한데.
# 바로 떠올리기는 생각보다 어려운 듯.


if __name__ == "__main__":
    main()
