# Authored by : marigold2003
# Date : 2026-02-10
# Link : https://www.acmicpc.net/problem/34665


import sys

input = sys.stdin.readline


# [Summary] 가희와 교통 요금

# A입력과 B입력이 같으면 1550을 출력해라.


def main() -> None:

    # [Ideas]

    # 두 입력을 비교하면 된다.

    ##########

    if input().rstrip() == input().rstrip():
        print(0)
    else:
        print(1550)

    ##########

    return


# [Review]

# 이래도 돌아가네


if __name__ == "__main__":
    main()
