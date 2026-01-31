# Authored by : marigold2003
# Date : 2026-01-30
# Link : https://www.acmicpc.net/problem/13908

import sys

input = sys.stdin.readline


# [Summary]

# 최대 7자리 비밀번호를 찾아야 하고, 들어가는 숫자를 몇 개 알고 있다.
# 만들 수 있는 비밀번호의 경우의 수를 구하시오.


def main():

    # [Ideas]

    # 브루트포스다. 10**7. 10_000_000 되냐? 이건 아니고.

    # 일단 들어가는 숫자들로 조합을 만든다.
    # 그리고 남는 자리에는 0~9까지 들어갈 수 있으니 자리당 *10을 해주면?

    ##########

    from itertools import product

    N, M = map(int, input().split())
    nums = set(map(int, input().split()))

    count = 0
    for perm in product(range(10), repeat=N):
        # set 간의 포함연산은 부등호로 가능하다.
        if nums <= set(perm):
            count += 1

    print(count)

    ##########

    return


# [Review]

# 날먹했다. 역시 된다.
# 15분 타이머 성공

if __name__ == "__main__":
    main()
