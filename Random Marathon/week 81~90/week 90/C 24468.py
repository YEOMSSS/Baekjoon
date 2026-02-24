# Authored by : marigold2003
# Date : 2026-02-20
# Link : https://www.acmicpc.net/problem/24468


import sys

input = sys.stdin.readline


# [Summary] 충돌의 수

# 길이가 L인 선분에 점이 N개 있다.
# 모든 점은 1초에 1좌표씩 이동한다.
# 점이 선분의 끝이나 점끼리 부딪히면 즉시 운동 방향이 바뀐다.

# 각 점의 처음 운동 위치와 처음 운동 방향이 주어진다.
# 입력되는 임의의 두 점 사이의 거리는 짝수이다.
# 점끼리 충돌하는 횟수를 구하시오.


def main() -> None:

    # [Ideas]

    # 시작거리가 다 짝수면 0.5초간격으로 충돌하는 경우는 없다.
    # 1초간격으로 해서 공끼리 위치가 같아지는 타이밍만 세면 될 듯.

    ##########

    L, N, T = map(int, input().split())

    # L1 R0
    points_info = [
        [int(x[0]), 0 if x[1] == "R" else 1]
        for x in (input().split() for _ in range(N))
    ]
    points_info.sort()

    count = 0
    for _ in range(T):

        prev = -1
        for i in range(N):

            # L 처리
            if points_info[i][1]:
                points_info[i][0] -= 1
            # R 처리
            else:
                points_info[i][0] += 1

            if prev == points_info[i][0]:
                points_info[i][1] ^= 1
                points_info[i - 1][1] ^= 1
                count += 1

            if points_info[i][0] == 0 or points_info[i][0] == L:
                points_info[i][1] ^= 1

            prev = points_info[i][0]

    print(count)

    ##########

    return


# [Review]

# 시뮬레이션을 해보자.
# 정렬 입력이라는 말이 없었네? 이런!


if __name__ == "__main__":
    main()
