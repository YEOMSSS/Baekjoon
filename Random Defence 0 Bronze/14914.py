# Authored by : marigold2003
# Date : 2026-03-17
# Link : https://www.acmicpc.net/problem/14914


import sys

input = sys.stdin.readline


# [Summary] 사과와 바나나 나눠주기

# 사과와 바나나를 공평하게 나눠준다.
# 남기지 않고 공평하게 나눠줄 수 있는 경우를 전부 출력하시오.


def main() -> None:

    # [Ideas]

    # 친구들은 무제한이다.
    # 약수 구하는 느낌이네.

    # 최대공약수의 약수를 구하면 된다.
    # 근데 뭐, 1000개밖에 안되면 브루트포스를 하자고.
    # 나머지가 없는 경우만 찾으면 되겠다.

    # 친구들은 a, b 중 적은 게 최대가 될 것.

    ##########

    a, b = map(int, input().split())

    for i in range(1, min(a, b) + 1):
        if a % i:
            continue
        if b % i:
            continue

        print(i, a // i, b // i)

    ##########

    return


# [Review]

# 사이좋은 친구들이에요.


if __name__ == "__main__":
    main()
