# Authored by : marigold2003
# Date : 2026-04-05
# Link : https://www.acmicpc.net/problem/1253


import sys

input = sys.stdin.readline


# [Summary] 좋다

# 수가 N(2K)개 주어진다.
# N개의 수 중 어떤 수가 다른 두 수의 합으로 나타낼 수 있다면
# 그 수를 좋다고 말한다.

# 좋은 수가 몇 개인지 출력하시오.
# 수의 위치가 다르면 값이 같아도 다른 수이다.


def main() -> None:

    # [Ideas]

    # 자신은 제외된다는 부분이 포인트인 듯 하다.
    # 풀이는 대충 두 가지가 떠오른다.

    # 일단 정렬을 해놓고
    # 투포인터로 자신을 제외한 모든 수로 돌리거나
    # 모든 두 수의 합이 생기는 경우를 정렬해서 모든 수에 이분탐색하거나.

    # 근데 자신을 제외하는 행동이 필요하니까...
    # 투포인터로 돌리는게 훨씬 편해보이긴 하는데.

    ##########

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    count = 0
    # 투포인터를 돌릴 때, 양 끝에서 시작하자.
    # 만든 숫자가 목표보다 작으면 왼쪽을 키워보고
    # 만든 숫자가 목표보다 크면 오른쪽을 줄여봐야 한다.
    for i in range(N):

        target = arr[i]
        arr[i] = None

        left = 0
        right = N - 1

        while left < right:

            if arr[left] is None:
                left += 1
                continue
            if arr[right] is None:
                right -= 1
                continue

            curr = arr[left] + arr[right]
            if curr < target:
                left += 1
            elif curr > target:
                right -= 1
            else:
                count += 1
                break

        else:
            pass

        arr[i] = target

    print(count)

    ##########

    return


# [Review]

# 사용한거 빼는거 신경쓰기 싫어서 투포인터를 사용했다.
# 용액문제와 다른 방식으로 포인터를 관리해야 한다.


if __name__ == "__main__":
    main()
