# Authored by : marigold2003
# Date : 2026-04-02
# Link : https://www.acmicpc.net/problem/23032


import sys

input = sys.stdin.readline


# [Summary] 서프라이즈~

# 크기가 N(<= 2K)인 배열이 주어진다.
# 임의의 연속된 범위를 정하고, 그 범위를 임의로 연속된 두 그룹으로 나눈다.
# 각 그룹의 합의 차가 최솟값인 범위의 합을 구하시오.


def main() -> None:

    # [Ideas]

    # 가대생이 또 스테이크 좋아하지...

    # 일단 누적합은 무조건 사용해야 한다.
    # 2K 정도면 브루트포스로 돌릴 수 있을 법한 숫자인데.
    # 일단 처음에 연속된 범위를 정해야 한다.

    # 1 2 3 4 5
    # 12, 23, 34, 45, 123, 234, 345, 1234, 2345, 12345
    # 범위는 브루트포스로 다 해봐야 할 것 같고...
    # 이 안을 반으로 가르는 것도 브루트포스로 될 거 같은디?
    # 근데 브루트 브루트 조지니까 1K개 입력만 되도 시간초과가 난다.

    # 2K개면 범위 종류만 해도 1+2+...+1999개가 된다. 대충 2M개.
    # 각 범위 안에서 가르기도 대충 1K번이니까... 2M*1K? 절대불가능.

    # 범위를 만들지 않는 경우는 생각이 잘 안난다. 가르기를 줄여볼까.

    # 오, 아니면 그룹을 먼저 만드는건 어때?
    # 왼쪽 그룹이 될 수 있는 모든 경우에 대해 그 크기와 가장 비슷한 오른쪽 그룹을 이분탐색으로.
    # 누적합으로 되어있으니 값이 큰 것도 잘 처리해주면 되는거 아니야? start를 더해줘야겠네.
    # 누적합이고 다 양수였으니까 오름차순 정렬도 이미 되어있겠네? 그럼 그룹만 해서 O(n**2)잖아?

    ##########

    from itertools import accumulate
    from bisect import bisect_left

    N = int(input())
    arr = list(map(int, input().split()))
    prefixsum = list(accumulate(arr, initial=0))

    min_gap = sys.maxsize
    maxtotal = 0

    # 그룹 길이 정하기
    for n in range(1, N + 1):
        start, end = 0, n

        # 길이 n으로 슬라이딩 윈도우
        while end <= N:

            group_left = prefixsum[end] - prefixsum[start]

            b = bisect_left(prefixsum[end + 1 :], group_left + prefixsum[end]) + end + 1

            # 찾은 인덱스 앞뒤로 확인
            if b > end + 1:
                group_right = prefixsum[b - 1] - prefixsum[end]
                gap = abs(group_right - group_left)

                if min_gap > gap:
                    min_gap = gap
                    maxtotal = group_left + group_right
                elif min_gap == gap:
                    maxtotal = max(maxtotal, group_left + group_right)

            if b <= N:
                group_right = prefixsum[b] - prefixsum[end]
                gap = abs(group_right - group_left)

                if min_gap > gap:
                    min_gap = gap
                    maxtotal = group_left + group_right
                elif min_gap == gap:
                    maxtotal = max(maxtotal, group_left + group_right)

            start += 1
            end += 1

    print(maxtotal)

    ##########

    return


# [Review]

# 문제 진짜 좋은데?
# 투포인터로 브루트포스하게 왼쪽그룹이 될 수 있는 모든 경우 찾고,
# 누적합으로 만들어둬서 오름차순인 배열에 이분탐색 갈기고.


if __name__ == "__main__":
    main()
