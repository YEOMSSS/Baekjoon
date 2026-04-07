# Authored by : marigold2003
# Date : 2026-04-07
# Link : https://www.acmicpc.net/problem/16430


import sys

input = sys.stdin.readline


# [Summary] 제리와 톰

# 톰은 마트에서 1kg 짜리 치즈를 샀다.
# 제리가 A / B(A < B)만큼 훔쳐갔다. A와 B는 서로소다.
# 남은 치즈의 무게는? 기약분수 형태로 출력하시오.


def main() -> None:

    # [Ideas]

    # 서로소니까 B-A와 B도 서로소.
    # 저 둘을 그대로 출력하면 된다.

    ##########

    A, B = map(int, input().split())
    print(B - A, B)

    ##########

    return


# [Review]

# 오, 왜 서로소일까?
# 뭐, 그럴 수 있지. 불쌍한 톰.


if __name__ == "__main__":
    main()
