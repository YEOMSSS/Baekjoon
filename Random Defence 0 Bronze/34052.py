# Authored by : marigold2003
# Date : 2026-04-23
# Link : https://www.acmicpc.net/problem/34052


import sys

input = sys.stdin.readline


# [Summary] 체육은 수학과목 입니다 2

# 입력 4회를 합쳐 1500보다 작으면 성공.


def main() -> None:

    # [Ideas]

    # 그렇습니다.

    ##########

    temp = sum(int(input()) for _ in range(4))
    print("No" if temp > 1500 else "Yes")

    ##########

    return


# [Review]

# 이런, 시간이 지나버렸어.


if __name__ == "__main__":
    main()
