# Authored by : marigold2003
# Date : 2026-04-15
# Link : https://www.acmicpc.net/problem/33612


import sys

input = sys.stdin.readline


# [Summary] 피갤컵

# 제1회 피갤컵이 2024년 8월에 열렸다.
# 제2회 피갤컵은 2025년 3월에 열린다.
# 이를 통해 피갤컵은 7개월 주기로 열린다는 사실을 알 수 있다.
# 그렇다면 N번째 피갤컵은 언제 열릴까?


def main() -> None:

    # [Ideas]

    # 1회가 24년 8월이니까, 1 + (7*N) 해서 12로 나누자.

    ##########

    N = int(input())

    year = 2024
    month = 1 + 7 * N

    print(year + (month - 1) // 12, (month - 1) % 12 + 1)

    ##########

    return


# [Review]

# 사실 다 구해서 출력해도 된다.
# 아, 12월이 생각보다 애매하네?


if __name__ == "__main__":
    main()
