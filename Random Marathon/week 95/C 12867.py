# Authored by : marigold2003
# Date : 2026-03-27
# Link : https://www.acmicpc.net/problem/12867


import sys

input = sys.stdin.readline


# [Summary] N차원 여행

# 원점에서 여행을 시작한다. 각 점은 좌표 N(1G)개로 이루어진다.

# 이동 방식은 다음과 같다.
# 1~N에서 움직일 좌표의 인덱스를 고른다.
# 그 좌표의 값을 1만큼 증가시킨 곳이나 감소시킨 곳으로 이동한다.

# 여행 계획의 길이는 M(<= 50)이다.


def main() -> None:

    # [Ideas]

    # 1G길이의 리스트를 만들긴 좀 그런데.
    # 이동이 있었던 좌표인덱스만 저장하면 될 듯?
    # set에 dict를 넣어도 잘 작동하려나?

    ##########

    from collections import Counter

    N = int(input())
    M = int(input())
    plans = list(map(int, input().split()))
    dirs = list(input().rstrip())

    changed = Counter()
    visited = set()

    # 원점을 방문시켜둔다.
    visited.add(())

    for i in range(M):
        delta = 1 if dirs[i] == "+" else -1
        changed[plans[i]] += delta
        if changed[plans[i]] == 0:
            del changed[plans[i]]

        snapshot = tuple(sorted(changed.items()))

        if snapshot in visited:
            print(0)
            return

        visited.add(snapshot)

    print(1)

    ##########

    return


# [Review]

# 오, 재밌는데?
# 원점 처리에 유의하세요.


if __name__ == "__main__":
    main()
