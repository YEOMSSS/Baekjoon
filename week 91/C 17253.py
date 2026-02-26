# Authored by : marigold2003
# Date : 2026-02-26
# Link : https://www.acmicpc.net/problem/17253


import sys

input = sys.stdin.readline


# [Summary] 삼삼한 수 2


# N(sys.maxsize)을 3의 거듭제곱인 수들을 겹치지 않게
# 한번씩만 더해서 만들 수 있다면 그 수는 삼삼한 수이다.

# N이 삼삼한 수인지 판단하시오.


def main() -> None:

    # [Ideas]

    # 그리디가 사용 가능해 보인다.
    # 제곱을 더 많이한게 제곱이 더 적은걸 다 더한거보다 크니까.
    # 큰거부터 순서대로 빼면 될 듯. 못빼면 그냥 넘어가고.

    ##########

    N = int(input())

    powers_of_3 = []

    i = 0
    while 3**i <= N:
        powers_of_3.append(3**i)
        i += 1

    for p in reversed(powers_of_3):
        N -= p
        if N == 0:
            print("YES")
            return
        elif N < 0:
            N += p

    print("NO")

    ##########

    return


def base_3() -> None:

    # [Ideas]

    # 3진법으로 변환해서 2가 없으면 된다.
    # 뭐야, 이런 풀이도 가능하네.

    ##########

    N = int(input())

    if not N:
        print("NO")
        return

    while N:
        N, r = divmod(N, 3)

        if r == 2:
            print("NO")
            return

    print("YES")

    ##########

    return


# [Review]

# 다양한 풀이가 있었다.
# 배운 것을 써먹는 것도 능력...


if __name__ == "__main__":
    base_3()
    # main()
