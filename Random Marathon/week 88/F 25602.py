# Authored by : marigold2003
# Date : 2026-02-08
# Link : https://www.acmicpc.net/problem/25602


import sys

input = sys.stdin.readline


# [Summary] 캔 주기

# N(5)가지 종류의 캔을 K(4)일동안 두 마리 고양이에게 한 캔씩 줄 것이다.
# 고양이들의 각 캔에 대한 만족도는 매일 달라진다.
# 두 고양이의 만족도의 총합의 최댓값을 구하시오.


def main() -> None:

    # [Ideas]

    # 브루트포스로 충분히 풀 수 있는 문제 같다.
    # 5종의 캔, 캔 부여 횟수 4*2 =8회.
    # 5*5*5*5*5*5*5*5 = 390625개 순열(최악) 괜찮네.
    # 전부 확인하도록 하자.

    ##########

    N, K = map(int, input().split())
    arr = tuple(map(int, input().split()))
    catA = tuple(tuple(map(int, input().split())) for _ in range(K))
    catB = tuple(tuple(map(int, input().split())) for _ in range(K))

    from itertools import product
    from collections import Counter

    answer = 0
    for perm in product(range(N), repeat=K * 2):
        for i, v in Counter(perm).items():
            if arr[i] < v:
                break
        else:
            score = 0
            for i, p in enumerate(perm[:K]):
                score += catA[i][p]
            for i, p in enumerate(perm[K:]):
                score += catB[i][p]
            answer = max(answer, score)

    print(answer)

    ##########

    return


# [Review]

# 무식하게 푸는 것이 좋을 때도 있는 법이지

if __name__ == "__main__":
    main()
