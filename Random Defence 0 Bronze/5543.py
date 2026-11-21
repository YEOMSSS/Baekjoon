# Authored by : marigold2003
# Date : 2026-11-21
# Link : https://www.acmicpc.net/problem/5543


import sys

input = sys.stdin.readline


# [Summary] 상근날드

# 상덕버거, 중덕버거, 하덕버거, 콜라, 사이다의 가격이 주어진다.
# 세트메뉴는 버거와 음료를 하나씩 고른 후 50원을 빼면 그 가격이 된다.
# 가장 싼 세트메뉴의 가격을 출력하시오.


def main() -> None:

    # [Ideas]

    # 3 * 2 6가지의 경우가 있다.
    # 전부 구해서 비교하도록 하자. 2중포문을 쓸까.

    ##########

    burgers = []
    drinks = []

    for _ in range(3):
        burgers.append(int(input()))

    for _ in range(2):
        drinks.append(int(input()))

    # results = []
    # for b in burgers:
    #     for d in drinks:
    #         results.append(b + d)
    # print(min(results) - 50)

    result = min(b + d for b in burgers for d in drinks)
    print(result - 50)

    ##########

    return


# [Review]

# 파이썬 재활 중...


if __name__ == "__main__":
    main()
