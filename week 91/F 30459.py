# Authored by : marigold2003
# Date : 2026-02-26
# Link : https://www.acmicpc.net/problem/30459


import sys

input = sys.stdin.readline


# [Summary] 현수막 걸기

# N(2K)개의 말뚝이 한 줄로 박혀 있다.
# 이중에 두개를 골라 현수막의 밑변으로 한다.
# M(40000)개의 깃대 중 하나를 골라 말뚝 사이에 꽂고, 현수막으 높이로 한다.
# 최대 R넓이로 설치 가능할 때, 현수막 넓이의 최댓값을 구하시오.


def main() -> None:

    # [Ideas]

    # 말뚝 2개 고르는 건 bruteforce로 해야겠다.
    # 좌표를 굳이 저장할 필요는 없으니, 차를 set에 저장하자.

    # 그럼 모든 밑변에 대하여 깃대를 이분탐색으로 R에 맞춰 최댓값을 찾으면 된다.

    ##########

    from itertools import combinations

    N, M, R = map(int, input().split())
    R *= 2

    # bruteforce 돌릴 밑변 길이들 set에 구해놓기
    coords = map(int, input().split())
    bases = set(map(lambda x: abs(x[0] - x[1]), combinations(coords, 2)))

    # bsearch 돌릴 높이들 정렬해놓기
    heights = list(map(int, input().split()))
    heights.sort()

    def b_search(base) -> int:
        left = 0
        right = M - 1

        result = -1
        while left <= right:
            mid = (left + right) // 2

            curr = heights[mid] * base

            # 더 넓힐 수 있으면 넓혀도 된다.
            if curr <= R:
                result = curr
                left = mid + 1
            # 더 넓힐 수 없다면 줄여야만 한다.
            else:
                right = mid - 1

        return result

    answer = -1
    for base in bases:
        answer = max(answer, b_search(base))

    print(f"{answer / 2:.1f}" if not answer == -1 else answer)

    ##########

    return


# [Review]

# 더 간단하게 풀 수 있을 것 같은디.
# 그냥 브포랑 이분탐색으로 되니까... 걍 하자. 뭐.


if __name__ == "__main__":
    main()
