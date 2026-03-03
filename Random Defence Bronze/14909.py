# Authored by : marigold2003
# Date : 2026-03-03
# Link : https://www.acmicpc.net/problem/14909


import sys

input = sys.stdin.readline


# [Summary] 양수 개수 세기

# 주어진 N(1M)개 정수 중에서 양의 정수의 개수를 출력하시오.


def main() -> None:

    # [Ideas]

    # 정렬은 필요 없고... 그냥 하나하나 다 보지 뭐.

    ##########

    answer = 0
    for num in map(int, input().split()):
        if num > 0:
            answer += 1

    print(answer)

    ##########

    return


# [Review]

# 이런 게 힐링이지 다른 게 아니라


if __name__ == "__main__":
    main()
