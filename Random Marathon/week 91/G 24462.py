# Authored by : marigold2003
# Date : 2026-03-02
# Link : https://www.acmicpc.net/problem/24462


import sys

input = sys.stdin.readline


# [Summary] 일어나... 코딩해야지...

# N(1K)개의 알람시계가 있고, 이들은 각자 T시각부터 K시간마다 울린다.
# 두 알람시계를 골라 D시각까지 알람이 울리는 시각을 최대로 하고자 할 때,
# 두 알람시계와 알람이 울리는 횟수를 구하시오.


def main() -> None:

    # [Ideas]

    # 일단 배수관계다.
    # 그리고 브루트포스로 추정됨. 대충 1M회 알람횟수를 구해야한다.

    # 어떻게 해야 효율적으로 구할 수 있을까?
    # 공배수를 찾는 것이 중요해 보임.
    # 유클리드 형님 모셔와야하나? lcm 양이 해줄거임.

    # 일단 D를 //K해서 구하고, 여기서 D //lcm해서 빼주면 되겠지.
    # 아주아주 다행스럽게도 T는 K의 배수임이 보장된다.

    # 시작시각 T만 좀 관리해주면 될 듯.
    # 다 0에서 시작한다 치고, 0에서 시작시각까지로 한번 더 구해서 빼주지 뭐.

    # 관리할 부분이 생각보다 좀 있다.
    # 둘 중 큰놈의 시작점이 겹칠때 -1

    ##########

    from math import lcm

    N, D = map(int, input().split())

    alarms = [list(map(int, input().split())) for _ in range(N)]

    answer = [0, 0, 0]
    for i in range(N):
        a_start, a_snooze = alarms[i]
        for j in range(i + 1, N):
            b_start, b_snooze = alarms[j]
            lcm_ab = lcm(a_snooze, b_snooze)

            count = 0

            # A 알람이 울리는 횟수
            count += (D - a_start) // a_snooze + 1
            # B 알람이 울리는 횟수
            count += (D - b_start) // b_snooze + 1

            # 더 늦게 울리기 시작하는 알람에서 lcm은 제외
            # lcm이 처음으로 나오는 부분부터 확인하면 된다.
            later = max(a_start, b_start)
            S = ((later + lcm_ab - 1) // lcm_ab) * lcm_ab

            if D >= later:
                count -= (D - S) // lcm_ab + 1

            if answer[2] < count:
                answer = [i, j, count]

    print(answer[0] + 1, answer[1] + 1)
    print(answer[2])

    ##########

    return


# [Review]

# 엄청 헷갈린다. 무조건 노트에 그려라
# T가 K의 배수가 아니면 이거 어떻게 풀었을까

# 아 개좆같다 씨발.


if __name__ == "__main__":
    main()
