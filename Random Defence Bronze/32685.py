# Authored by : marigold2003
# Date : 2026-03-30
# Link : https://www.acmicpc.net/problem/32685


import sys

input = sys.stdin.readline


# [Summary]  4-LSB

# 십진수가 3개 주어진다.
# 각 십진수를 이진수로 바꾼 후 하위 4비트를 뽑아내 이어붙인다.
# 그 이어붙인 이진수를 다시 십진수로 바꾼 값이 비밀번호가 된다.
# 비밀번호는 항상 4자리이므로, 앞에는 0을 채운다.


def main() -> None:

    # [Ideas]

    # bin 이랑 int( ,2)를 사용하면 될 듯.
    # 그리고 그냥 parsing하자.

    ##########

    a = bin(int(input()))[2:]
    b = bin(int(input()))[2:]
    c = bin(int(input()))[2:]

    binum = f"{a[-4:]:0>4}{b[-4:]:0>4}{c[-4:]:0>4}"
    num = int(binum, 2)

    print(f"{num:04}")

    ##########

    return


# [Review]

# 막 쉽지만은 않은디?


if __name__ == "__main__":
    main()
