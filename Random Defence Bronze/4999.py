# Authored by : marigold2003
# Date : 2026-03-24
# Link : https://www.acmicpc.net/problem/4999


import sys

input = sys.stdin.readline


# [Summary] 아!

# 내가 낼 수 있는 최대 길이가
# 의사가 원하는 길이 이상이면 그 병원에 갈 수 있다.

# 입력으로 주어진 두 길이를 보고 병원에 갈 수 있는지 판단하시오.


def main() -> None:

    # [Ideas]

    # 길이를 재고 비교하자.

    ##########

    a = len(input().rstrip())
    b = len(input().rstrip())

    print("go" if a >= b else "no")

    ##########

    return


# [Review]

# 병원을 자주 가는 건 나쁜 게 아니다.
# 병이 없다면 말이지


if __name__ == "__main__":
    main()
