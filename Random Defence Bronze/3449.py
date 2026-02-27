# Authored by : marigold2003
# Date : 2026-02-27
# Link : https://www.acmicpc.net/problem/3449


import sys

input = sys.stdin.readline


# [Summary] 해밍 거리

# 길이가 서로 같은 이진수가 주어진다.
# 해밍 거리는 두 숫자의 서로 다른 자리수의 개수를 말한다.
# 두 이진수가 주어졌을 때, 해밍 거리를 계산하시오.


def main() -> None:

    # [Ideas]

    # 이건 뭐.. 인덱스로 비교하자.

    ##########

    T = int(input())

    for _ in range(T):
        temp = list(map(int, input().rstrip()))

        count = 0
        for i, a in enumerate(list(map(int, input().rstrip()))):
            if temp[i] != a:
                count += 1

        print(f"Hamming distance is {count}.")

    ##########

    return


# [Review]

# 쉽고 빠르게 작성
# 최적화는 하지 않겠다.


if __name__ == "__main__":
    main()
