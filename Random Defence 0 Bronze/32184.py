# Authored by : marigold2003
# Date : 2026-02-14
# Link : https://www.acmicpc.net/problem/32184


import sys

input = sys.stdin.readline


# [Summary] 디미고에 가고 싶어!

# 홀수쪽이 왼쪽, 짝수쪽이 오른쪽이다.
# 사진촬영은 왼쪽+오른쪽을 가로로 한번에 찍거나 한 페이지씩 찍을 수 있다.
# 사진을 찍는 최소 횟수를 구하시오.


def main() -> None:

    # [Ideas]

    # 짝수에서 시작하면 한번 찍어서 홀수로 넘어간다.
    # 홀수로 끝나면 한번 찍어서 짝수로 돌아간다.

    # 홀수에서 시작해서 짝수로 끝나도록 다듬은 페이지를 2로 나누면 됨.

    ##########

    A, B = map(int, input().split())

    count = 0
    # A가 짝수라면 +1
    if not A % 2:
        count += 1
        A += 1
    # B가 홀수라면 +1
    if B % 2:
        count += 1
        B -= 1

    count += (B - A + 1) // 2

    print(count)

    ##########

    return


# [Review]

# 간단한 사칙연산
# 뇌 운동 많이 된다


if __name__ == "__main__":
    main()
