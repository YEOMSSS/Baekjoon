# Authored by : marigold2003
# Date : 2026-01-28
# Link : https://www.acmicpc.net/problem/2467

import sys

input = sys.stdin.readline


# [Summary]

# 1~10억 산성용액과 -1~-10억 염기성용액 입력이 주어진다.
# 주어진 입력에서 두 용액을 골라 0에 가장 가깝게 하면 된다.


def main():

    # [Ideas]

    # 정렬된 입력을 제외하면 https://www.acmicpc.net/problem/2470과 같다고 보면 된다.
    # 이분탐색의 경우 모든 음수의 절댓값에 대해서 차가 가장 적은 양수를 찾으면 된다.

    # 이번엔 투포인터를 이용해 더 쉽게 풀어볼 예정.
    # 부호 구분 없이 리스트를 통짜로 사용하자.

    # start와 end 포인터를 두 개 만들어 각각 처음과 끝에서 시작한다.
    # 합이 음수면 start를 늘려 합을 늘린다.
    # 합이 양수면 end를 줄여 합을 줄인다.
    # 두 포인터는 항상 합의 최솟값 후보가 된다.

    ##########

    N = int(input())
    # 정렬되어 들어오므로, 후처리가 필요 없다.
    arr = list(map(int, input().split()))

    min_result = sys.maxsize
    start, end = 0, N - 1
    ans1, ans2 = 0, 0
    while start < end:
        curr = arr[start] + arr[end]

        # 최솟값 갱신은 항상 양수로 이루어지도록 한다.
        if abs(curr) <= min_result:
            min_result = abs(curr)
            ans1, ans2 = start, end

        # 현재 합이 음수라면, start를 늘려 합을 0에 더 가깝게 키운다.
        if curr < 0:
            start += 1
        # 현재 합이 양수라면, end를 줄여 합을 0에 더 가깝게 줄인다.
        else:  # curr >=0
            end -= 1

    print(arr[ans1], arr[ans2])

    ##########

    return


# [Review]

# 정석적인 투 포인터 문제이다.
# 이분탐색 연습용으로도 나쁘지 않다. 다만 이 경우는 예외상황에 대한 구현이 더 필요하다.

if __name__ == "__main__":
    main()
