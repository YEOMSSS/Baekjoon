# Authored by : marigold2003
# Date : 2026-02-27
# Link : https://www.acmicpc.net/problem/31673


import sys

input = sys.stdin.readline


# [Summary] 특별한 학생회장 교체

# 학생회장은 N(100K)개의 단체에 예산 M을 분배한다.
# 분배하고 남은 예산이 학생회의 예산이 되며, 각 단체에 0 이상의 예산을 분배한다.

# 각 학생단체 i는 Vi개의 투표권을 획득하며, 학생회보다 더 많은 예산을 받기를 원한다.
# 예산을 적게 받은 단체는 학생회장 탄핵에 투표할 것이다.

# 과반 이상 찬성 시 학생회장은 탄핵된다.
# 탄핵되지 않으면서 가져올 수 있는 최대 예산을 구해보자.


def main() -> None:

    # [Ideas]

    # 투표권 적은 애들한테 다 0원 던져버리면 되는거 아님?
    # 진짜 미친새끼같네

    ##########

    N, M = map(int, input().split())
    votes = list(map(int, input().split()))
    votes.sort()

    half = sum(votes) / 2

    curr = 0
    for i, v in enumerate(votes):
        curr += v

        # 투표가 과반을 넘기 전까지 예산 0원
        if curr > half:
            break

    # 예산 // (학생회 + 분배해야할 단체 수)
    # 내림연산해야한다. 학생회가 가장 적게 먹어야하니까
    print(M // (N - i + 1))

    ##########

    return


# [Review]

# 썩을놈이네 이거


if __name__ == "__main__":
    main()
