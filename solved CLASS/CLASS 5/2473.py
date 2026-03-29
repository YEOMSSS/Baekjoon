# Authored by : marigold2003
# Date : 2026-03-29
# Link : https://www.acmicpc.net/problem/2473


import sys

input = sys.stdin.readline


# [Summary] 세 용액

# -1G ~ 1G 범위의 정수가 N(<= 5K)개 주어진다.
# 임의의 세 정수의 합의 절댓값의 최솟값을 구하시오.


def main() -> None:

    # [Ideas]

    # 경우는 4가지다.
    # 정수+정수+정수, 음수+음수+음수. 근데 이걸 정수나 음수만 있을때고.
    # 보통은 정수+음수+음수 또는 음수+정수+정수로 진행될 것이다.

    # 그럼 일단 정수랑 음수로 나눠놓고 정렬해둔 후
    # 정수 둘을 합친 것 전부와 음수 둘을 합친 것 전부의 set을 만들어 list로 정렬하자고.
    # 그리고 정수 하나 집어서 음수둘합에 이분탐색
    # 그리고 음수 하나 집어서 정수둘합에 이분탐색
    # 반복해주면 되겠다.

    # 만약에 음수밖에 없거나 정수밖에 없거나 하면 절댓값최소 3개 더하면된다.
    # 투포인터로도 할 수 있겠구만. 이게 정해일지도.

    ##########

    """
    from bisect import bisect_left

    N = int(input())
    positives = []
    negatives = []

    for n in map(int, input().split()):
        if n >= 0:
            positives.append(n)
        else:
            negatives.append(n)

    positives.sort()
    negatives.sort()

    # 양수와 음수 중 하나가 없는 경우
    if not positives:
        print(*negatives[-3:])
        return
    if not negatives:
        print(*positives[:3])
        return

    pcomb = set(
        (positives[i], positives[j])
        for i in range(len(positives))
        for j in range(i + 1, len(positives))
    )
    ncomb = set(
        (negatives[i], negatives[j])
        for i in range(len(negatives))
        for j in range(i + 1, len(negatives))
    )

    pcomb = sorted(pcomb, key=lambda x: sum(x))
    ncomb = sorted(ncomb, key=lambda x: sum(x))

    psum = list(sum(pc) for pc in pcomb)
    nsum = list(sum(nc) for nc in ncomb)

    psum_len = len(psum)
    nsum_len = len(nsum)

    result = (10**9, 10**9, 10**9)

    for p in positives:
        i = bisect_left(nsum, -p)

        if i < nsum_len:
            ns1, ns2 = ncomb[i]
            curr1 = (ns1, ns2, p)
            if abs(sum(result)) > abs(sum(curr1)):
                result = curr1

        if i > 0:
            ns1, ns2 = ncomb[i - 1]
            curr2 = (ns1, ns2, p)
            if abs(sum(result)) > abs(sum(curr2)):
                result = curr2

    for n in negatives:
        i = bisect_left(psum, -n)

        if i < psum_len:
            ps1, ps2 = pcomb[i]
            curr1 = (ps1, ps2, n)
            if abs(sum(result)) > abs(sum(curr1)):
                result = curr1

        if i > 0:
            ps1, ps2 = pcomb[i - 1]
            curr2 = (ps1, ps2, n)
            if abs(sum(result)) > abs(sum(curr2)):
                result = curr2

    if len(positives) >= 3:
        if abs(sum(result)) > abs(sum(positives[:3])):
            result = tuple(positives[:3])
    if len(negatives) >= 3:
        if abs(sum(result)) > abs(sum(negatives[-3:])):
            result = tuple(negatives[-3:])

    print(*sorted(result))
    """

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    # abs(sum), i, j, k
    best = (10**18, 0, 0, 0)

    # 일단 원소 하나 고정하고, 나머지 공간에서 투포인터
    for i in range(N - 2):
        start = i + 1
        end = N - 1

        while start < end:
            s = arr[i] + arr[start] + arr[end]

            if abs(s) < best[0]:
                best = (abs(s), arr[i], arr[start], arr[end])

            # 0보다 크면 줄여본다.
            if s > 0:
                end -= 1
            # 0보다 작으면 키워본다.
            elif s < 0:
                start += 1
            # 0이면 즉시 종료 가능.
            else:
                print(arr[i], arr[start], arr[end])
                return

    print(best[1], best[2], best[3])

    ##########

    return


# [Review]

# 시간초과 안나려나. 메모리초과가 나려나.
# 역시 투포인터가 편하긴 하구나.


if __name__ == "__main__":
    main()
