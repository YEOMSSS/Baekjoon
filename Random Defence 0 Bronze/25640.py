# Authored by : marigold2003
# Date : 2026-03-21
# Link : https://www.acmicpc.net/problem/25640


import sys

input = sys.stdin.readline


# [Summary] MBTI

# MBTI 유형이 N(<= 100)개 주어진다.
# 진호와 MBTI가 같은 사람의 수를 출력하시오.


def main() -> None:

    # [Ideas]

    # 입력받는대로 비교해서 카운트하자.

    ##########

    string = input().rstrip()

    N = int(input())

    count = 0
    for _ in range(N):
        if string == input().rstrip():
            count += 1

    print(count)

    ##########

    return


# [Review]

#


if __name__ == "__main__":
    main()
