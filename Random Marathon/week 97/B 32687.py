# Authored by : marigold2003
# Date : 2026-04-10
# Link : https://www.acmicpc.net/problem/32687


import sys

input = sys.stdin.readline


# [Summary] 반복수

# K(<= 6)자리수를 원하는만큼 이어붙인다.
# 이후 뒤에서부터 0개 이상의 수를 제거해 만든 K자리 이상의 수를 K반복수라 한다.
# A 이상 B(<= 10**12) 이하의 K반복수 중 M으로 나누어떨어지는 수의 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # 많아봤자 6자리면 100000~999999. 할만하지.
    # 이러면 쉽게 풀 수 있다. 브루트포스.

    ##########

    A, B, K, M = map(int, input().split())

    count = 0
    loop = 12 // K + 1
    for n in range(10 ** (K - 1), 10 ** (K)):
        temp = str(n) * loop

        for i in range(12, K - 1, -1):
            num = int(temp[:i])

            if num > B:
                continue
            if num < A:
                break

            if not num % M:
                count += 1

    print(count)

    ##########

    return


# [Review]

# 오, 하다보니 막 엄청나게 빡센 건 아니네.
# 아 뭐야, 반례가 왜 있지? 아, 최소 1회 반복!!


if __name__ == "__main__":
    main()
