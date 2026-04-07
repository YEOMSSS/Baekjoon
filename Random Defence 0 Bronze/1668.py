# Authored by : marigold2003
# Date : 2026-04-04
# Link : https://www.acmicpc.net/problem/1668


import sys

input = sys.stdin.readline


# [Summary] 트로피 진열

# 수직선 위에 트로피가 N(<= 50)개 놓여 있다.
# 각 트로피의 높이가 주어진다.

# 왼쪽에서 볼 때 보이는 트로피의 개수와
# 오른쪽에서 볼 때 보이는 트로피의 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 트로피가 50개뿐이니 시뮬레이션하자.

    ##########

    N = int(input())
    Trophies = list(int(input()) for _ in range(N))

    left_max = 0
    left_count = 0

    right_max = 0
    right_count = 0

    for i in range(N):
        l = Trophies[i]
        if left_max < l:
            left_count += 1
            left_max = l

        r = Trophies[N - i - 1]
        if right_max < r:
            right_count += 1
            right_max = r

    print(left_count)
    print(right_count)

    ##########

    return


# [Review]

# 역시 입력이 작아야 편해~


if __name__ == "__main__":
    main()
