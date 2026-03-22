# Authored by : marigold2003
# Date : 2026-03-22
# Link : https://www.acmicpc.net/problem/16113


import sys

input = sys.stdin.readline


# [Summary] 시그널

# 5의 배수인 N(<= 100K)길이의 string이 들어온다.
# 다섯 개로 끊어 위아래로 붙이면 디지털 숫자의 모양이 나온다.
# 숫자와 숫자 사이에는 1열 이상의 공백이 있다.
# string을 해독하시오.


def main() -> None:

    # [Ideas]

    # 1열 공백을 잘 이용해야 한다.
    # 포인터를 5개 사용하면 어떨까?

    # 비트마스킹으로 진짜 깔끔하게 풀릴거같은데.

    ##########

    numbers = [
        [31, 17, 31],
        [31],
        [23, 21, 29],
        [21, 21, 31],
        [28, 4, 31],
        [29, 21, 23],
        [31, 21, 23],
        [16, 16, 31],
        [31, 21, 31],
        [29, 21, 31],
    ]

    N = int(input())

    signal = input().rstrip()
    pointers = [p for p in range(0, N, N // 5)]

    answer = []

    buf = []
    for _ in range(N // 5):

        bit = 0
        for i in range(5):
            curr = signal[pointers[i]]
            if curr == "#":
                bit |= 1 << (4 - i)
            pointers[i] += 1

        if not bit:
            # 디지털 숫자로 변환하기
            if buf:
                answer.append(numbers.index(buf))
                buf = []

        else:  # if bit:
            buf.append(bit)

    if buf:
        answer.append(numbers.index(buf))

    print("".join(map(str, answer)))

    ##########

    return


# [Review]

# 오, 이런 식으로 사용할 수 있구만.
# 근데 실수 안하게 조심해야할듯
# 봐, 인덱스 실수 바로나잖아. 거꾸로 마스킹했네.


if __name__ == "__main__":
    main()
