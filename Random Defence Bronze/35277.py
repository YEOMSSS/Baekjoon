# Authored by : marigold2003
# Date : 2026-04-05
# Link : https://www.acmicpc.net/problem/35277


import sys

input = sys.stdin.readline


# [Summary] 유림이와 하람이의 두쫀쿠 대작전

# 구운 카다이프 900원
# 버터 60원
# 피스타치오 스프레드 600원
# 화이트초콜릿 170원
# 마시멜로 160원
# 코코아파우더 110원

# 이상이 두쫀쿠 하나를 만드는 데 필요한 재료의 비용이다.
# N원으로 두쫀쿠를 몇 개나 만들 수 있을지 알아내 보자.


def main() -> None:

    # [Ideas]

    # 다 더하고 정수나눗셈하면 되지롱.

    ##########

    N = int(input())
    price = 900 + 60 + 600 + 170 + 160 + 110

    print(N // price)

    ##########

    return


# [Review]

# 맛있긴 해, 비싸서 문제지
# 3K원만 되도 하루에 하나씩 먹는다


if __name__ == "__main__":
    main()
