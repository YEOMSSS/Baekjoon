# Authored by : marigold2003
# Date : 2026-03-24
# Link : https://www.acmicpc.net/problem/2141


import sys

input = sys.stdin.readline


# [Summary] 우체국

# 수직선에 N(<= 100K)개의 마을이 있다.
# 각 마을에는 A(<= 1G)명의 사람이 있다.

# 우체국을 하나 세우려고 하는데, 각 마을과의 거리의 합이 최소가 되게 하려고 한다.
# 어디에 우체국을 세워야 할지 구하시오.


def main() -> None:

    # [Ideas]

    # 풀었던 문제 느낌. #7571 열화판이다.
    # 근데 이제 사람 수가 추가된. 그럼 중간값을 찾는 방식이 좀 달라지겠다.

    # 일단 사람 수를 다 세고, 그것의 중간값을 찾자.
    # 그게 어느 마을인지 찾고 묶음으로 계산하면 되겠다.
    # 어쨋든 마을에서 시작해야될거아니냐?

    ##########

    N = int(input())
    X_A = [list(map(int, input().split())) for _ in range(N)]
    X_A.sort()

    count = 0
    for _, a in X_A:
        count += a

    # 여기서도 총 인원의 홀짝성은 큰 의미가... 있네???
    # 여기서는 마을에 사람이 다를 수가 있어서 그렇구나... 맞네.
    # 홀수면 중앙이니 count//2 +1이 되어야 한다.
    # 짝수면 중앙기준 좌우값이 다 가능한데, 작은걸 출력해야한다. //2
    mid = (count + 1) // 2

    temp = 0
    for x, a in X_A:
        temp += a
        if temp >= mid:
            print(x)
            return

    ##########

    return


# [Review]

# 중간값을 찾은 후 처리할 부분이 조금 있다.
# 발상만 하면 그리 어렵지는 않음.


if __name__ == "__main__":
    main()
