# Authored by : marigold2003
# Date : 2026-02-02
# Link : https://www.acmicpc.net/problem/13752

import sys

input = sys.stdin.readline


# [Summary]

# 숫자를 받아 그만큼 "="을 출력하는 간단한 문제.


def main() -> None:

    # [Ideas]

    # 문자열 *로 풀자.

    ##########

    for _ in range(int(input())):
        print("=" * int(input()))

    ##########

    return


# [Review]

# 운동 많이 했다 이런 힐링도 필요해

if __name__ == "__main__":
    main()
